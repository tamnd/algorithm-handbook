"""hb: build The Handbook of Algorithms from the Algorithm project.

    python -m hb survey  [--content ../algorithm]
    python -m hb check   [--content ../algorithm] [--volume N]
    python -m hb build   [--content ../algorithm] [--volume N|all] [--formats tex,pdf,epub]
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import time

from .book import Book
from .corpus import Corpus

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _edition() -> dict:
    """The file EDITION: 'version 0.1' and 'content <commit of tamnd/algorithm>' (spec handbook 09.2)."""
    out = {"version": "0.1", "content": ""}
    path = os.path.join(ROOT, "EDITION")
    if os.path.exists(path):
        for line in open(path):
            k, _, v = line.strip().partition(" ")
            if k:
                out[k] = v.strip()
    return out


EDITION = _edition()["version"]


def load(args) -> Book:
    t = time.time()
    corpus = Corpus(os.path.abspath(args.content))
    book = Book(corpus, os.path.join(ROOT, "content"))
    print(f"corpus {corpus.commit()[:8]}: {len(corpus.nodes)} nodes, loaded in {time.time() - t:.1f}s",
          file=sys.stderr)
    pinned = _edition()["content"]
    if pinned and not corpus.commit().startswith(pinned[:8]) and not pinned.startswith(corpus.commit()[:8]):
        print(f"note: EDITION pins content {pinned[:8]}, but the content is at {corpus.commit()[:8]}",
              file=sys.stderr)
    return book


def volumes(book: Book, which: str):
    if which == "all":
        return [v for v in book.volumes if v.built]
    nums = {int(x) for x in which.split(",")}
    return [v for v in book.volumes if v.number in nums]


def cmd_survey(args):
    book = load(args)
    for v in book.volumes:
        e = len(v.entries)
        s = sum(len(c.stubs) for c in v.chapters)
        w = sum(n.words for n in v.entries)
        print(f"{v.number:>2} {v.name:<34} chapters {len(v.chapters):>3}  entries {e:>4}  stubs {s:>4}  words {w:>9,}")


BANNED = (r"\b(leverag(?:e|es|ed|ing)|showcas(?:e|es|ed|ing)|powerful|elegant(?:ly)?|seamless(?:ly)?|crucial(?:ly)?|"
          r"delv(?:e|es|ed|ing)|journey|landscape)\b")


def check_content(book: Book) -> list[str]:
    """Problems in the learner layer: links to unknown slugs, files in unknown places, bad exercise numbers."""
    import glob
    import re
    probs = []
    areas = {a.id: {s.id for s in a.children} for a in book.corpus.areas}
    for f in sorted(glob.glob(os.path.join(book.content, "**", "*.*"), recursive=True)):
        rel = os.path.relpath(f, book.content)
        parts = rel.split(os.sep)
        if len(parts) == 1:
            continue   # PROVENANCE.md and other notes about the directory
        if parts[0] not in areas and parts[0] not in ("front",):
            probs.append(f"{rel}: unknown area {parts[0]}")
        elif len(parts) == 3 and parts[1] not in areas.get(parts[0], {}):
            probs.append(f"{rel}: unknown chapter {parts[1]}")
        t = open(f, encoding="utf-8").read()
        for slug in re.findall(r"\]\(/([a-z0-9][a-z0-9-]*)/(?:#[^)]*)?\)", t):
            if slug not in book.corpus.nodes and slug != "areas":
                probs.append(f"{rel}: link to unknown slug /{slug}/")
        prose = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$|`[^`\n]*`|```.*?```", " ", t, flags=re.S)
        for w in sorted(set(re.findall(BANNED, prose, flags=re.I))):
            probs.append(f"{rel}: style: '{w}' (see the writing standard in prompts/area.md)")
        if re.search(r"[A-Za-z)]!(\s|$)", prose):
            probs.append(f"{rel}: style: exclamation mark")
        if re.search(r"\bIn this chapter,? we will\b", prose):
            probs.append(f"{rel}: style: 'In this chapter, we will'")
        if f.endswith("exercises.md"):
            nums = [int(x) for x in re.findall(r"^(\d+)\.\s", t, flags=re.M)]
            if nums != list(range(1, len(nums) + 1)):
                probs.append(f"{rel}: exercises are not numbered 1..{len(nums)}")
            for n, band in re.findall(r"^(\d+)\.\s+(\S)", t, flags=re.M):
                if band not in "◦•★":
                    probs.append(f"{rel}: exercise {n} has no band mark")
            hp = f.replace("exercises.md", "hints.md")
            if os.path.exists(hp):
                hn = [int(x) for x in re.findall(r"^(\d+)\.\s", open(hp).read(), flags=re.M)]
                bad = [h for h in hn if h > len(nums)]
                if bad:
                    probs.append(f"{rel}: hints for missing exercises {bad}")
    return probs


def cmd_check(args):
    book = load(args)
    from .guide import guide_md
    for w in guide_md(book)[1]["warnings"]:
        print("front:", w)
    for v in volumes(book, args.volume):
        for c in v.chapters:
            for w in c.warnings:
                print(f"{c.num} {c.id}: {w}")
    for p in check_content(book):
        print(p)


def cmd_brief(args):
    """A brief of a volume or chapter for writers of the learner layer: entries, summaries, prerequisites."""
    from .prep import complexity_rows
    book = load(args)
    v = book.volume(args.volume)
    print(f"# Volume {v.number}: {v.name}\n\n{v.summary.strip()}\n")
    for ch in v.chapters:
        if args.chapter and str(ch.number) != str(args.chapter):
            continue
        print(f"## Chapter {ch.num} `{ch.id}`: {ch.name} ({len(ch.entries)} entries, {len(ch.stubs)} stubs)\n")
        for e in ch.entries:
            pre = [p for p in (e.fm.get("prereqs") or [])]
            pre = ", ".join(f"{p}" + (f" ({book.ref(p)})" if book.ref(p) else "") for p in pre)
            cx = "; ".join(f"{k} {x}" for k, x in complexity_rows(e.fm.get("complexity") or {})[:3])
            heads = [l[3:].strip() for l in e.body.split("\n") if l.startswith("## ")]
            print(f"- **{book.ref(e.slug)} {e.name}** `{e.slug}` [{e.kind}, {e.level}, {e.words} words]. "
                  f"{e.summary.strip()}" + (f" Cost: {cx}." if cx else "") + (f" Needs: {pre}." if pre else "")
                  + (f" Sections: {' / '.join(heads)}." if args.sections else ""))
        if ch.stubs:
            print("\nStubs (not written): " + ", ".join(f"{s.name} `{s.slug}`" for s in ch.stubs))
        print()


def slugname(v) -> str:
    return f"{v.number:02d}-{v.id}"


def cmd_build(args):
    from . import latex
    from .volume import volume_md
    book = load(args)
    date = datetime.date.today().isoformat()
    formats = set(args.formats.split(","))
    report = {}
    failed = []
    todo = volumes(book, args.volume)
    if args.volume == "all" or "0" in args.volume.split(","):
        from .guide import guide_volume
        todo = [guide_volume(book)] + todo
    for v in todo:
        t = time.time()
        out = os.path.join(ROOT, "build", slugname(v))
        from .figures import guide_figures, make_figures
        if v.number == 0:
            from .guide import guide_md
            figs = guide_figures(book, out)
            md, stats = guide_md(book, figs)
        else:
            figs = make_figures(book, v, out)
            md, stats = volume_md(book, v, figs)
        info = dict(stats, warnings=len(stats["warnings"]), figures=len(figs))
        if formats & {"tex", "pdf"}:
            info.update(latex.build(book, v, md, out, EDITION, date, pdf="pdf" in formats))
            if "pdf" in formats and not info.get("ok"):
                failed.append(v.number)
        if "epub" in formats:
            from . import epub
            info.update(epub.build(book, v, md, out, EDITION, date))
        info["seconds"] = round(time.time() - t, 1)
        report[v.number] = info
        err = info.pop("error", None)
        print(f"vol {v.number} {v.name}: " + json.dumps({k: x for k, x in info.items() if k != "missing_glyphs"}))
        if info.get("missing_glyphs"):
            print("  missing glyphs:", "".join(list(info["missing_glyphs"])[:60]))
        if err:
            print(err)
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    json.dump(report, open(os.path.join(ROOT, "build", "report.json"), "w"), indent=1, ensure_ascii=False)
    if failed:
        sys.exit(f"LaTeX failed for volume(s) {', '.join(map(str, failed))}")


def main():
    ap = argparse.ArgumentParser(prog="hb")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("survey", "check", "build", "brief"):
        p = sub.add_parser(name)
        p.add_argument("--content", default=os.path.join(ROOT, "..", "algorithm"))
        if name != "survey":
            p.add_argument("--volume", default="all")
        if name == "build":
            p.add_argument("--formats", default="tex,pdf")
        if name == "brief":
            p.add_argument("--chapter", default="")
            p.add_argument("--sections", action="store_true")
    args = ap.parse_args()
    {"survey": cmd_survey, "check": cmd_check, "build": cmd_build, "brief": cmd_brief}[args.cmd](args)


if __name__ == "__main__":
    main()
