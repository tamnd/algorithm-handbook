"""The apparatus of a volume: indexes, bibliography, the problem appendix (spec handbook 07)."""

from __future__ import annotations

import re
import unicodedata
from collections import defaultdict

from .mathcost import cost_md
from .book import Book, Volume
from .prep import Refs, fmt_sources, md_plain

PARTICLES = {"von", "van", "de", "der", "den", "di", "da", "du", "le", "la", "del", "della", "ten", "ter"}
MAX_REFS = 24


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"^[^A-Za-z0-9]+", "", s.lower())
    return s


def numkey(num: str):
    return [int(x) for x in num.split(".")]


def _letter(term: str) -> str:
    f = fold(term)
    if f and f[0].isalpha():
        return f[0].upper()
    return "0–9" if f and f[0].isdigit() else "Symbols"


def _links(book: Book, refs: Refs, slugs, main: str | None = None) -> str:
    nums = sorted({s for s in slugs if book.ref(s)}, key=lambda s: numkey(book.ref(s)))
    more = 0
    if len(nums) > MAX_REFS:
        more = len(nums) - MAX_REFS
        nums = nums[:MAX_REFS]
    parts = []
    for s in nums:
        t = f"[{book.ref(s)}]({refs.target(s)})"
        parts.append(f"**{t}**" if s == main else t)
    if more:
        parts.append(f"and {more} more")
    return ", ".join(parts)


def _render(groups: dict[str, list[str]]) -> str:
    out = ['::: {.index latex-env="hbindex"}']
    for letter in sorted(groups, key=lambda x: (len(x) > 1, x)):
        out.append(f"```{{=latex}}\n\\hbidxletter{{{letter}}}\n```\n")
        out.append(f"[{letter}]{{.idxletter .html-only}}\n")
        out += groups[letter]
    out.append(":::")
    return "\n".join(out)


def subject_index(book: Book, vol: Volume, refs: Refs) -> str:
    entries = vol.entries
    mentioned = defaultdict(set)   # slug -> entries of this volume that link to it
    for e in entries:
        for s in set(re.findall(r"\]\(/([a-z0-9][a-z0-9-]*)/", e.body)) | set(e.fm.get("prereqs") or []):
            if s != e.slug and s in book.corpus.nodes:
                mentioned[s].add(e.slug)
    terms = {}   # display -> markdown line
    for e in entries:
        refs_md = _links(book, refs, {e.slug} | mentioned.get(e.slug, set()), main=e.slug)
        terms[e.name] = f"{md_plain(e.name)}, {refs_md}\n"
        for a in e.fm.get("aliases") or []:
            a = str(a)
            if fold(a) != fold(e.name) and a not in terms:
                terms[a] = f"{md_plain(a)}, *see* [{md_plain(e.name)}]({refs.target(e.slug)})\n"
    # topics of other volumes that this volume uses
    for s, users in mentioned.items():
        if book.volume_of.get(s) == vol.number:
            continue
        n = book.corpus.nodes[s]
        if n.name in terms:
            continue
        where = f"[{book.ref(s)}]({refs.target(s)})" if book.ref(s) else f"[site]({refs.target(s)})"
        terms[n.name] = f"{md_plain(n.name)} ({where}), used in {_links(book, refs, users)}\n"
    groups = defaultdict(list)
    for t in sorted(terms, key=fold):
        groups[_letter(t)].append(terms[t])
    return _render(groups)


def surname_form(name: str) -> str:
    toks = name.split()
    if len(toks) < 2:
        return name
    i = len(toks) - 1
    while i > 0 and toks[i - 1].lower() in PARTICLES:
        i -= 1
    last = " ".join(t for t in toks[i:])
    first = " ".join(toks[:i])
    # "Neumann, John von": particles go after the given names
    lead = [t for t in last.split() if t.lower() in PARTICLES]
    core = " ".join(t for t in last.split() if t.lower() not in PARTICLES)
    return f"{core}, {first}" + (" " + " ".join(lead) if lead else "")


def name_index(book: Book, vol: Volume, refs: Refs) -> str:
    people = defaultdict(set)
    for e in vol.entries:
        h = e.fm.get("history")
        if isinstance(h, dict):
            for p in h.get("people") or []:
                people[str(p).strip()].add(e.slug)
    if not people:
        return ""
    groups = defaultdict(list)
    for p in sorted(people, key=lambda p: fold(surname_form(p))):
        groups[_letter(surname_form(p))].append(f"{md_plain(surname_form(p))}, {_links(book, refs, people[p])}\n")
    return _render(groups)


def _source_key(s: dict) -> str:
    for k in ("paper", "book", "url"):
        if s.get(k):
            return f"{k}:{s[k]}"
    return "title:" + (s.get("title") or "")


def bibliography(book: Book, vol: Volume, refs: Refs) -> str:
    cites = {}
    where = defaultdict(set)
    for e in vol.entries:
        for s in e.fm.get("sources") or []:
            k = _source_key(s)
            if k not in cites:
                cites[k] = dict(s, locator="")
            where[k].add(e.slug)
    out = ['::: {.bibliography latex-env="hbbib"}']
    for k in sorted(cites, key=lambda k: fold(cites[k].get("title") or k)):
        txt = fmt_sources([cites[k]])[0]
        out.append(f"{txt} Cited in {_links(book, refs, where[k])}.\n")
    out.append(":::")
    return "\n".join(out)


def problems_appendix(book: Book, vol: Volume, refs: Refs) -> str:
    out = []
    for ch in vol.chapters:
        probs = [e for e in ch.entries if e.kind == "problem"]
        rows = []
        for p in probs:
            solvers = [n for n in book.corpus.nodes.values() if p.slug in (n.fm.get("solves") or [])]
            if not solvers:
                continue
            solvers.sort(key=lambda n: (0 if book.ref(n.slug) else 1, numkey(book.ref(n.slug)) if book.ref(n.slug) else [], n.name))
            for i, n in enumerate(solvers):
                t = (n.fm.get("complexity") or {}).get("time") or {}
                tv = ""
                if isinstance(t, dict) and t:
                    tv = t.get("worst") or t.get("expected") or t.get("average") or next(iter(t.values()))
                first = refs.link(p.slug) if i == 0 else ""
                rows.append(f"| {first} | {refs.link(n.slug)} | {cost_md(tv, md_plain) if tv else ""} |")
        if rows:
            out.append(f"#### Chapter {ch.num}: {md_plain(ch.name)} {{.unnumbered}}\n")
            out.append("| Problem | Algorithm | Time |\n|---|---|---|\n" + "\n".join(rows) + "\n")
    return "\n".join(out)
