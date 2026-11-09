"""The figures the book makes itself (spec handbook 06): concept maps of chapters, the map of a volume.

Each figure is drawn with Graphviz twice: PDF for the LaTeX book and SVG for the EPUB.
"""

from __future__ import annotations

import os
import subprocess
import textwrap
from collections import defaultdict

from .book import Book, Chapter, Volume
from .volume import volume_hue

KIND_SHAPE = {"problem": ("box", "rounded,filled"), "algorithm": ("box", "filled"),
              "data-structure": ("box", "filled"), "concept": ("ellipse", "filled"),
              "definition": ("ellipse", "filled"), "theorem": ("box", "rounded,filled,dashed")}
MAX_NODES = 70


def _mix(hexs: str, t: float) -> str:
    r, g, b = (int(hexs[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02X%02X%02X" % tuple(int(c + (255 - c) * t) for c in (r, g, b))


def _esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def _label(num: str, name: str, width=18) -> str:
    lines = textwrap.wrap(name, width)[:3]
    return _esc(num + "\n" + "\n".join(lines))


def transitive_reduction(nodes, edges):
    succ = defaultdict(set)
    for a, b in edges:
        succ[a].add(b)

    def reach(a, skip):
        seen, stack = set(), [x for x in succ[a] if x != skip]
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            stack += succ[x]
        return seen
    return [(a, b) for a, b in edges if b not in reach(a, b)]


def chapter_dot(book: Book, ch: Chapter) -> str | None:
    es = ch.entries
    if len(es) < 4 or len(es) > MAX_NODES:
        return None
    inch = {e.slug for e in es}
    edges = sorted({(p, e.slug) for e in es for p in (e.fm.get("prereqs") or []) if p in inch and p != e.slug})
    edges = transitive_reduction(inch, edges)
    if len(edges) < 3:
        return None
    hue = volume_hue(ch.volume)
    lines = ["digraph G {", 'graph [rankdir=LR, nodesep=0.12, ranksep=0.35, fontname="Helvetica", '
             'bgcolor="transparent", pad=0.05, size="6.2,8.6", ratio=compress];',
             f'node [fontname="Helvetica", fontsize=9, color="#{hue}", penwidth=0.6, margin="0.06,0.03", '
             f'fillcolor="{_mix(hue, 0.88)}", fontcolor="#1F2328", height=0.3];',
             'edge [color="#9AA3AF", arrowsize=0.45, penwidth=0.6];']
    groups = defaultdict(list)
    for g in ch.groups:
        for e in g.entries:
            groups[g.title or ""].append(e)
    for e in es:
        shape, style = KIND_SHAPE.get(e.kind, ("box", "filled"))
        extra = f', fillcolor="{_mix(hue, 0.7)}"' if e.kind == "problem" else ""
        lines.append(f'"{e.slug}" [label="{_label(book.ref(e.slug), e.name)}", shape={shape}, style="{style}"{extra}, '
                     f'href="#{e.slug}"];')
    for a, b in edges:
        lines.append(f'"{a}" -> "{b}";')
    lines.append("}")
    return "\n".join(lines)


def volume_dot(book: Book, vol: Volume) -> str | None:
    chs = [c for c in vol.chapters if c.entries]
    if len(chs) < 2:
        return None
    hue = volume_hue(vol.number)
    of = {e.slug: c.num for c in chs for e in c.entries}
    w = defaultdict(int)
    for c in chs:
        for e in c.entries:
            for p in e.fm.get("prereqs") or []:
                if p in of and of[p] != c.num:
                    w[(of[p], c.num)] += 1
    lines = ["digraph G {", 'graph [rankdir=TB, nodesep=0.3, ranksep=0.45, bgcolor="transparent", pad=0.05, '
             'size="6.2,8.2"];',
             f'node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#{hue}", '
             f'fillcolor="{_mix(hue, 0.85)}", fontcolor="#1F2328", penwidth=0.8, margin="0.15,0.08"];',
             'edge [color="#9AA3AF", arrowsize=0.6];']
    for c in chs:
        lab = _esc(f"{c.num}  {c.name}\n{len(c.entries)} entries")
        lines.append(f'"{c.num}" [label="{lab}", href="#ch-{c.id}"];')
    for (a, b), n in sorted(w.items()):
        if n >= 2:
            lines.append(f'"{a}" -> "{b}" [penwidth={min(4.0, 0.5 + n / 6):.1f}];')
    lines.append("}")
    return "\n".join(lines)


def set_dot(book: Book, min_links: int = 12) -> str:
    """The map of the set: one box per volume, an arrow where one volume's entries need another's."""
    vol_of = {e.slug: v.number for v in book.volumes for e in v.entries}
    w = defaultdict(int)
    for v in book.volumes:
        for e in v.entries:
            for p in e.fm.get("prereqs") or []:
                if p in vol_of and vol_of[p] != v.number:
                    w[(vol_of[p], v.number)] += 1
    built = [v for v in book.volumes if v.entries]
    lines = ["digraph G {", 'graph [rankdir=TB, nodesep=0.25, ranksep=0.4, bgcolor="transparent", pad=0.05, '
             'size="6.2,8.4"];',
             'node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, penwidth=0.8, '
             'margin="0.14,0.07", fontcolor="#1F2328"];',
             'edge [color="#9AA3AF", arrowsize=0.6];']
    for v in built:
        hue = volume_hue(v.number)
        lab = _esc(f"{v.number}  {v.name}\n{len(v.entries)} entries")
        lines.append(f'"{v.number}" [label="{lab}", color="#{hue}", fillcolor="{_mix(hue, 0.82)}", '
                     f'href="#vol-{v.id}"];')
    # the volumes lean on each other in cycles (3 and 7, 11 and 12), so a transitive reduction would empty
    # the figure; keep, for each volume, its three strongest sources with at least min_links links
    keep = set()
    for b in {b for _, b in w}:
        srcs = sorted(((n, a) for (a, bb), n in w.items() if bb == b and n >= min_links), reverse=True)[:3]
        keep |= {(a, b) for _, a in srcs}
    for (a, b), n in sorted(w.items()):
        if (a, b) in keep:
            lines.append(f'"{a}" -> "{b}" [penwidth={min(4.0, 0.5 + n / 25):.1f}];')
    lines.append("}")
    return "\n".join(lines)


def render(dot: str, base: str) -> bool:
    os.makedirs(os.path.dirname(base), exist_ok=True)
    open(base + ".dot", "w").write(dot)
    ok = True
    for fmt in ("pdf", "svg"):
        r = subprocess.run(["dot", "-T" + fmt, "-o", f"{base}.{fmt}", base + ".dot"], capture_output=True, text=True)
        ok &= r.returncode == 0
    return ok


def figure_md(base_rel: str, caption: str, label: str) -> str:
    """The Markdown of a figure: a LaTeX float for the PDF, an image for the EPUB."""
    from .prep import tex, md_plain
    return (f"```{{=latex}}\n\\hbfigure{{{base_rel}.pdf}}{{{tex(caption)}}}{{{label}}}\n```\n\n"
            f"::: {{.figure .html-only}}\n![{md_plain(caption)}]({base_rel}.svg)\n:::\n")


def guide_figures(book: Book, outdir: str) -> dict:
    figs = {}
    if render(set_dot(book), os.path.join(outdir, "fig", "set")):
        figs["set"] = figure_md("fig/set", "The volumes of this edition and how they lean on each other. An "
                                "arrow runs from a volume to one whose entries need it; each volume shows the "
                                "(at most) three volumes it needs most, when there are at least twelve links. "
                                "A thicker arrow means more links.", "fig:set")
    return figs


def make_figures(book: Book, vol: Volume, outdir: str) -> dict:
    """Draw the figures of a volume into outdir/fig. Returns {key: markdown} for the assembler."""
    figs = {}
    d = volume_dot(book, vol)
    if d and render(d, os.path.join(outdir, "fig", "volume")):
        figs["volume"] = figure_md("fig/volume", f"The chapters of Volume {vol.number} and how they lean on "
                                   "each other. An arrow runs from a chapter to one that uses its entries; "
                                   "a thicker arrow means more links.", "fig:volume")
    for ch in vol.chapters:
        d = chapter_dot(book, ch)
        if d and render(d, os.path.join(outdir, "fig", f"ch-{ch.num}")):
            figs[ch.num] = figure_md(f"fig/ch-{ch.num}", f"The entries of chapter {ch.num} and their "
                                     "prerequisites. An arrow runs from an entry to one that needs it. "
                                     "Rounded boxes are problems, ovals are concepts and definitions.",
                                     f"fig:ch-{ch.num}")
    return figs
