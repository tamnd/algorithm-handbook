"""The Markdown of a whole volume: introduction, chapters, appendices (spec handbook 02.3).

The same text feeds the LaTeX and the EPUB writers. Headings that LaTeX makes with its own macros
(\\hbchapter, \\hbintro, \\hbentry) are repeated as `html-only` Markdown headings for the EPUB.
"""

from __future__ import annotations

from . import apparatus
from .book import Book, Volume
from .prep import SITE, Refs, chapter_md, glue, hints_md, md_plain, tex


def _intro_head(title: str, label: str) -> str:
    return (f"```{{=latex}}\n\\hbintro{{{tex(title)}}}{{{label}}}\n```\n\n"
            f"# {md_plain(title)} {{#{label} .html-only .unnumbered}}\n")


def chapter_table(book: Book, vol: Volume, refs: Refs) -> str:
    rows = ["| | Chapter | Entries | Further topics |", "|--|------------------------|-----:|-----:|"]
    for ch in vol.chapters:
        name = f"[{md_plain(ch.name)}](#ch-{ch.id})"
        rows.append(f"| {ch.num} | {name} | {len(ch.entries) or '–'} | {len(ch.stubs) or '–'} |")
    return "\n".join(rows) + f"\n\n: The chapters of Volume {vol.number}.\n"


def introduction(book: Book, vol: Volume, refs: Refs, fig: str = "") -> str:
    out = [_intro_head("Introduction", f"intro-{vol.id}")]
    t = glue(book, refs, vol.id, "volume.md")
    if t:
        out.append(t)
    else:
        out.append(f"{vol.summary.strip()}\n")
    n_e = len(vol.entries)
    n_s = sum(len(c.stubs) for c in vol.chapters)
    out.append("```{=latex}\n\\hbgroup{The volume at a glance}\n```\n\n## The volume at a glance {.html-only}\n")
    more = (f" A further {n_s} topics are planned; each chapter lists its own at the end." if n_s else "")
    out.append(f"This edition of the volume has {len(vol.chapters)} chapters with {n_e} entries.{more}\n")
    out.append(chapter_table(book, vol, refs))
    if fig:
        out.append(fig)
    return "\n".join(out)


def volume_md(book: Book, vol: Volume, figs: dict | None = None) -> tuple[str, dict]:
    """The Markdown of the volume, and some numbers about it. figs: from figures.make_figures."""
    figs = figs or {}
    refs = Refs(book, vol)
    parts = [introduction(book, vol, refs, figs.get("volume", ""))]
    for ch in vol.chapters:
        parts.append(chapter_md(book, vol, ch, refs, figs.get(ch.num, "")))
    parts.append("```{=latex}\n\\hbbackmatter\n```\n")
    appx = [
        ("Hints to the exercises", "hints", lambda: hints_md(book, vol, refs)),
        ("Problems and their algorithms", "problems", lambda: apparatus.problems_appendix(book, vol, refs)),
        ("Bibliography", "bibliography", lambda: apparatus.bibliography(book, vol, refs)),
        ("Index of names", "names", lambda: apparatus.name_index(book, vol, refs)),
        ("Index", "index", lambda: apparatus.subject_index(book, vol, refs)),
    ]
    for title, label, make in appx:
        body = make()
        if body and body.strip():
            parts.append(_intro_head(title, label) + "\n" + body + "\n")
    stats = {"chapters": len(vol.chapters), "entries": len(vol.entries),
             "stubs": sum(len(c.stubs) for c in vol.chapters),
             "words": sum(e.words for e in vol.entries),
             "warnings": [w for c in vol.chapters for w in c.warnings]}
    return "\n\n".join(parts), stats


def volume_hue(n: int) -> str:
    """One hue per volume, spread round the wheel with the golden angle, at an even darkness."""
    import colorsys
    if n == 0:
        return "34495E"   # Volume 0, the guide: a quiet slate
    h = ((n * 137.508) % 360) / 360
    r, g, b = colorsys.hls_to_rgb(h, 0.38, 0.55)
    return "%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))


__all__ = ["volume_md", "volume_hue", "SITE"]
