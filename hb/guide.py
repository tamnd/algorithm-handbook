"""Volume 0, *Guide and Index* (spec handbook 02.7): the way into the set.

Preface, how to use the handbook, notation, the volumes, the learning paths, the problem catalogue, the
glossary, the timeline, and the indexes and bibliography of the whole set. Every link to an entry goes to
the site and carries the entry's number, which says in which volume it is.
"""

from __future__ import annotations

import os
import re
from collections import defaultdict
from types import SimpleNamespace

import yaml

from . import apparatus
from .book import Book
from .corpus import KIND_LABEL
from .prep import SITE, Refs, convert_fences, glue, glue_inline, md_plain, tex

GUIDE_SUMMARY = ("The way into the set: how the handbook works, its notation, a map of all the volumes, "
                 "learning paths across them, and the indexes of the whole set.")


def guide_volume(book: Book):
    """A stand-in for Volume 0 with what the LaTeX, EPUB and cover writers read."""
    chs = [SimpleNamespace(entries=v.entries, stubs=[s for c in v.chapters for s in c.stubs])
           for v in book.volumes]
    return SimpleNamespace(number=0, id="guide", name="Guide and Index", summary=GUIDE_SUMMARY,
                           chapters=chs, entries=[e for v in book.volumes for e in v.entries])


def _chapter(num: str, title: str, label: str) -> str:
    return (f"```{{=latex}}\n\\hbchapter{{{num}}}{{{tex(title)}}}{{{label}}}\n```\n\n"
            f"# [{num}]{{.num}} {md_plain(title)} {{#{label} .html-only}}\n")


def _intro(title: str, label: str) -> str:
    return (f"```{{=latex}}\n\\hbintro{{{tex(title)}}}{{{label}}}\n```\n\n"
            f"# {md_plain(title)} {{#{label} .html-only .unnumbered}}\n")


def _group(title: str, label: str = "") -> str:
    ident = f"#{label} " if label else ""
    lab = f"\\phantomsection\\label{{{label}}}" if label else ""
    return f"```{{=latex}}\n{lab}\\hbgroup{{{tex(title)}}}\n```\n\n## {md_plain(title)} {{{ident}.html-only}}\n"


def front_page(book: Book, refs: Refs, name: str) -> str:
    """A page of content/front/: its `## ` headings become groups (in the contents), deeper ones stay."""
    t = book.text("front", name)
    if not t.strip():
        return ""
    t = glue(book, refs, "front", name, shift=0)
    out, fence = [], None
    for line in t.split("\n"):
        f = re.match(r"^(`{3,})", line)
        if f:
            fence = None if fence else f.group(1)
        m = re.match(r"^## (.*?)(?: \{\.unnumbered\})?\s*$", line) if fence is None else None
        if m:
            out.append(_group(m.group(1)))
            continue
        m = re.match(r"^(#{3,5}) (.*)$", line) if fence is None else None
        if m:
            line = "#" * (len(m.group(1)) + 1) + " " + m.group(2)
        out.append(line)
    return "\n".join(out)


# --------------------------------------------------------------------------- the volumes


def _status(v) -> str:
    if not v.entries:
        return "forthcoming"
    return "in this edition"


def volumes_overview(book: Book) -> str:
    rows = ["| | Volume | Chapters | Entries | Further topics | |",
            "|--:|--------------------------|-----:|-----:|-----:|---------|"]
    for v in book.volumes:
        stubs = sum(len(c.stubs) for c in v.chapters)
        rows.append(f"| {v.number} | [{md_plain(v.name)}](#vol-{v.id}) | {len(v.chapters)} | "
                    f"{len(v.entries) or '–'} | {stubs or '–'} | {_status(v)} |")
    tot_e = sum(len(v.entries) for v in book.volumes)
    tot_s = sum(len(c.stubs) for v in book.volumes for c in v.chapters)
    tot_c = sum(len(v.chapters) for v in book.volumes)
    rows.append(f"| | **The set** | **{tot_c}** | **{tot_e}** | **{tot_s}** | |")
    return "\n".join(rows) + "\n\n: The volumes of the handbook.\n"


def volume_pages(book: Book, refs: Refs) -> str:
    out = []
    for v in book.volumes:
        out.append(_group(f"Volume {v.number}: {v.name}", f"vol-{v.id}"))
        out.append(f"{v.summary.strip()}\n")
        stubs = sum(len(c.stubs) for c in v.chapters)
        if v.entries:
            words = sum(e.words for e in v.entries)
            first = _first_entries(book, v)
            out.append(f"*In this edition.* {len(v.chapters)} chapters, {len(v.entries)} entries "
                       f"(about {round(words, -3):,} words of entries)"
                       + (f", and {stubs} further topics still to be written." if stubs else ".")
                       + (f" Good places to start: {', '.join(refs.link(s) for s in first)}." if first else "")
                       + "\n")
        else:
            out.append(f"*Forthcoming.* The volume has {len(v.chapters)} chapters and {stubs} planned topics; "
                       f"each topic has a short page on the site, <{SITE}/areas/>.\n")
        rows = ["| | Chapter | Entries | Further topics |", "|--|------------------------|-----:|-----:|"]
        for c in v.chapters:
            rows.append(f"| {c.num} | {md_plain(c.name)} | {len(c.entries) or '–'} | {len(c.stubs) or '–'} |")
        out.append("\n".join(rows) + f"\n\n: The chapters of Volume {v.number}.\n")
    return "\n".join(out)


def _first_entries(book: Book, v, k: int = 4) -> list[str]:
    """The intro-level entries that open the volume's first chapters."""
    out = []
    for c in v.chapters:
        for e in c.entries:
            if e.level == "intro":
                out.append(e.slug)
                break
        if len(out) >= k:
            break
    return out


# --------------------------------------------------------------------------- learning paths


def paths_md(book: Book, refs: Refs) -> tuple[str, list[str]]:
    p = book.path("front", "paths.yaml")
    if not os.path.exists(p):
        return "", []
    spec = yaml.safe_load(open(p, encoding="utf-8")) or {}
    out, warn = [], []
    intro = (spec.get("intro") or "").strip()
    if intro:
        out.append(glue_inline(book, refs, intro) + "\n")
    chapters = {c.id: c for v in book.volumes for c in v.chapters}
    chapters.update({c.num: c for v in book.volumes for c in v.chapters})
    for path in spec.get("paths", []):
        out.append(_group(path["title"], "path-" + path["id"]))
        if path.get("for"):
            out.append(f"*For:* {md_plain(path['for'].strip())}\n")
        if path.get("intro"):
            out.append(glue_inline(book, refs, path["intro"].strip()) + "\n")
        for stage in path.get("stages", []):
            out.append(f"#### {md_plain(stage['title'])} {{.unnumbered}}\n")
            if stage.get("intro"):
                out.append(glue_inline(book, refs, stage["intro"].strip()) + "\n")
            items = []
            for step in stage.get("steps", []):
                if isinstance(step, str):
                    step = {"entry": step}
                why = step.get("why", "").strip()
                why = (". " + glue_inline(book, refs, why[0].upper() + why[1:])) if why else ""
                if "entry" in step:
                    s = step["entry"]
                    n = book.corpus.nodes.get(s)
                    if n is None:
                        warn.append(f"paths: {path['id']}: unknown slug {s}")
                        continue
                    if book.ref(s):
                        items.append(f"- [ ] {refs.link(s)}{why}")
                    else:
                        items.append(f"- [ ] [{md_plain(n.name)}]({SITE}/{s}/) (forthcoming){why}")
                elif "chapter" in step:
                    c = chapters.get(str(step["chapter"]))
                    if c is None:
                        warn.append(f"paths: {path['id']}: unknown chapter {step['chapter']}")
                        continue
                    state = f"{len(c.entries)} entries" if c.entries else "forthcoming"
                    items.append(f"- [ ] Chapter {c.num}, *{md_plain(c.name)}* ({state}){why}")
            out.append("\n".join(items) + "\n")
    return "\n".join(out), warn


# --------------------------------------------------------------------------- catalogue, glossary, timeline


def problem_catalogue(book: Book, refs: Refs) -> str:
    out = []
    for v in book.volumes:
        body = apparatus.problems_appendix(book, v, refs)
        if body.strip():
            out.append(_group(f"Volume {v.number}: {v.name}"))
            out.append(body)
    return "\n".join(out)


def glossary(book: Book, refs: Refs) -> str:
    defs = [e for v in book.volumes for e in v.entries if e.kind == "definition"]
    groups = defaultdict(list)
    for e in sorted(defs, key=lambda e: apparatus.fold(e.name)):
        s = re.sub(r"\s+", " ", e.summary.strip())
        groups[apparatus._letter(e.name)].append(f"**{md_plain(e.name)}** [{book.ref(e.slug)}]({refs.target(e.slug)}). "
                                                 f"{glue_inline(book, refs, s)}\n")
    out = ['::: {.glossary latex-env="hbglossary"}']
    for letter in sorted(groups, key=lambda x: (len(x) > 1, x)):
        out.append(f"```{{=latex}}\n\\hbidxletter{{{letter}}}\n```\n")
        out.append(f"[{letter}]{{.idxletter .html-only}}\n")
        out += groups[letter]
    out.append(":::")
    return "\n".join(out)


def _era(y: int) -> str:
    if y < 1900:
        return "Before 1900"
    if y < 1940:
        return "1900 to 1939"
    return f"The {y // 10 * 10}s"


def timeline(book: Book, refs: Refs) -> str:
    events = []
    for v in book.volumes:
        for e in v.entries:
            h = e.fm.get("history")
            if not isinstance(h, dict) or not isinstance(h.get("year"), int):
                continue
            events.append((h["year"], book.ref(e.slug), e, h))
    events.sort(key=lambda x: (x[0], apparatus.numkey(x[1])))
    out, era = ['::: {.timeline latex-env="hbtimeline"}'], None
    for y, _, e, h in events:
        if _era(y) != era:
            era = _era(y)
            out.append(f"```{{=latex}}\n\\hbidxletter{{{era}}}\n```\n")
            out.append(f"[{era}]{{.idxletter .html-only}}\n")
        people = ", ".join(str(p) for p in (h.get("people") or []))
        note = re.sub(r"\s+", " ", str(h.get("note") or "").strip())
        yr = f"{-y} BC" if y < 0 else str(y)
        out.append(f"**{yr}.** {refs.link(e.slug)}" + (f". {md_plain(people)}" if people else "")
                   + (f". {md_plain(note)}" if note else "") + "\n")
    out.append(":::")
    return "\n".join(out)


def master_index(book: Book, refs: Refs) -> str:
    """Every entry of the set by name and alias, with its number."""
    terms = {}
    for v in book.volumes:
        for e in v.entries:
            terms.setdefault(apparatus.fold(e.name) + "\0" + e.slug,
                             f"{md_plain(e.name)}, **[{book.ref(e.slug)}]({refs.target(e.slug)})**\n")
    names = {apparatus.fold(t.split("\0")[0]) for t in terms}
    for v in book.volumes:
        for e in v.entries:
            for a in e.fm.get("aliases") or []:
                a = str(a)
                if apparatus.fold(a) in names:
                    continue
                terms[apparatus.fold(a) + "\0" + e.slug] = (
                    f"{md_plain(a)}, *see* {md_plain(e.name)} [{book.ref(e.slug)}]({refs.target(e.slug)})\n")
    groups = defaultdict(list)
    for k in sorted(terms):
        groups[apparatus._letter(k.split("\0")[0])].append(terms[k])
    return apparatus._render(groups)


# --------------------------------------------------------------------------- the whole volume


def guide_md(book: Book, figs: dict | None = None) -> tuple[str, dict]:
    figs = figs or {}
    g = guide_volume(book)
    refs = Refs(book, g)
    parts = []
    pre = front_page(book, refs, "preface.md")
    if pre:
        parts.append(_intro("Preface", "preface") + "\n" + pre)
    chapters = [
        ("How to use the handbook", "how-to-use", lambda: front_page(book, refs, "how-to-use.md")),
        ("Notation and conventions", "notation", lambda: front_page(book, refs, "notation.md")),
        ("The volumes", "volumes", lambda: "\n".join(
            [front_page(book, refs, "volumes.md"), volumes_overview(book), figs.get("set", ""),
             volume_pages(book, refs)])),
        ("Learning paths", "paths", lambda: paths_md(book, refs)[0]),
        ("Problems and their algorithms", "problems", lambda: (
            "Each problem of the set that has a written entry, with the algorithms that solve it and the time "
            "each one takes, as their entries give it. The entries are grouped by volume and chapter.\n\n"
            + problem_catalogue(book, refs))),
        ("Glossary", "glossary", lambda: (
            "The definitions of the set, each with its summary and the number of its entry.\n\n"
            + glossary(book, refs))),
        ("Timeline", "timeline", lambda: (
            "The dates in the history of the entries: when a method or a result was first published or "
            "described, by whom, and where to read about it.\n\n" + timeline(book, refs))),
    ]
    k = 0
    for title, label, make in chapters:
        body = make()
        if body.strip():
            k += 1
            parts.append(_chapter(f"0.{k}", title, label) + "\n" + body)
    parts.append("```{=latex}\n\\hbbackmatter\n```\n")
    appx = [
        ("Bibliography", "bibliography", lambda: apparatus.bibliography(book, g, refs)),
        ("Index of names", "names", lambda: apparatus.name_index(book, g, refs)),
        ("Index of entries", "index", lambda: master_index(book, refs)),
    ]
    for title, label, make in appx:
        body = make()
        if body and body.strip():
            parts.append(_intro(title, label) + "\n" + body + "\n")
    stats = {"chapters": k, "entries": len(g.entries), "stubs": sum(len(c.stubs) for c in g.chapters),
             "words": 0, "warnings": paths_md(book, refs)[1]}
    return "\n\n".join(parts), stats


__all__ = ["guide_md", "guide_volume", "convert_fences", "KIND_LABEL"]
