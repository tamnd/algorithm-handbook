"""The structure of the set: volumes, chapters, groups and entries, with their numbers (spec handbook 02)."""

from __future__ import annotations

import heapq
import os
from dataclasses import dataclass, field

import yaml

from .corpus import Corpus, Node


@dataclass
class Group:
    title: str
    intro: str = ""
    entries: list = field(default_factory=list)   # [Node]


@dataclass
class Chapter:
    volume: int
    number: int
    id: str
    name: str
    groups: list = field(default_factory=list)    # [Group]
    stubs: list = field(default_factory=list)     # [Node]
    warnings: list = field(default_factory=list)

    @property
    def num(self): return f"{self.volume}.{self.number}"
    @property
    def entries(self): return [e for g in self.groups for e in g.entries]


@dataclass
class Volume:
    number: int
    id: str
    name: str
    summary: str
    chapters: list = field(default_factory=list)

    @property
    def entries(self): return [e for c in self.chapters for e in c.entries]
    @property
    def built(self): return any(c.entries for c in self.chapters)


class Book:
    def __init__(self, corpus: Corpus, content_dir: str):
        self.corpus = corpus
        self.content = content_dir
        self.volumes: list[Volume] = []
        self.number: dict[str, str] = {}     # slug -> "4.1.12" for written nodes
        self.volume_of: dict[str, int] = {}  # slug -> volume number for written nodes
        self.chapter_of: dict[str, Chapter] = {}
        self._build()

    # -- files of the learner layer --------------------------------------------------------
    def path(self, *parts) -> str:
        return os.path.join(self.content, *parts)

    def text(self, *parts) -> str:
        p = self.path(*parts)
        return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

    # -- structure --------------------------------------------------------------------------
    def _build(self):
        for a in self.corpus.areas:
            v = Volume(a.number, a.id, a.name, a.summary)
            for s in a.children:
                ch = Chapter(a.number, s.number, s.id, s.name)
                nodes = self.corpus.nodes_in(a.id, s.id)
                written = [n for n in nodes if n.written]
                ch.stubs = sorted([n for n in nodes if not n.written], key=lambda n: n.name.lower())
                ch.groups = self._groups(a.id, s.id, written, ch)
                v.chapters.append(ch)
                k = 0
                for e in ch.entries:
                    k += 1
                    self.number[e.slug] = f"{a.number}.{s.number}.{k}"
                    self.volume_of[e.slug] = a.number
                    self.chapter_of[e.slug] = ch
            self.volumes.append(v)

    def _groups(self, area: str, sub: str, written: list[Node], ch: Chapter) -> list[Group]:
        p = self.path(area, sub, "outline.yaml")
        if not written:
            return []
        by_slug = {n.slug: n for n in written}
        if not os.path.exists(p):
            return [Group("", "", topo_order(written))]
        spec = yaml.safe_load(open(p, encoding="utf-8")) or {}
        groups, seen = [], set()
        for g in spec.get("groups", []):
            grp = Group(g.get("title", ""), (g.get("intro") or "").strip())
            for slug in g.get("entries", []):
                if slug in seen:
                    ch.warnings.append(f"outline lists {slug} twice")
                    continue
                if slug not in by_slug:
                    node = self.corpus.nodes.get(slug)
                    why = "not a node" if node is None else (
                        "a stub" if not node.written else f"in {node.area}")
                    ch.warnings.append(f"outline entry {slug} is {why}; dropped")
                    continue
                seen.add(slug)
                grp.entries.append(by_slug[slug])
            if grp.entries:
                groups.append(grp)
        rest = [n for n in written if n.slug not in seen]
        if rest:
            ch.warnings.append("not in the outline: " + ", ".join(n.slug for n in rest))
            groups.append(Group("Other entries", "", topo_order(rest)))
        # forward references inside the chapter
        pos = {e.slug: i for i, e in enumerate(e for g in groups for e in g.entries)}
        for g in groups:
            for e in g.entries:
                for p_ in e.fm.get("prereqs") or []:
                    if p_ in pos and pos[p_] > pos[e.slug]:
                        ch.warnings.append(f"forward prerequisite: {e.slug} needs {p_}, which comes later")
        return groups

    def volume(self, n) -> Volume:
        for v in self.volumes:
            if str(v.number) == str(n) or v.id == n:
                return v
        raise KeyError(n)

    def ref(self, slug: str) -> str | None:
        return self.number.get(slug)


def topo_order(nodes: list[Node]) -> list[Node]:
    """Kahn's algorithm with the key (level, kind, slug); a cycle breaks at the smallest key (spec 02.5)."""
    inside = {n.slug: n for n in nodes}
    need = {n.slug: {p for p in (n.fm.get("prereqs") or []) if p in inside and p != n.slug} for n in nodes}
    users: dict[str, list[str]] = {s: [] for s in inside}
    for s, ps in need.items():
        for p in ps:
            users[p].append(s)
    heap = [(inside[s].key(), s) for s, ps in need.items() if not ps]
    heapq.heapify(heap)
    out, done = [], set()
    while len(out) < len(nodes):
        if not heap:  # a cycle: take the smallest node not yet placed
            s = min((s for s in inside if s not in done), key=lambda s: inside[s].key())
            heap = [(inside[s].key(), s)]
        _, s = heapq.heappop(heap)
        if s in done:
            continue
        done.add(s)
        out.append(inside[s])
        for u in users[s]:
            need[u].discard(s)
            if not need[u] and u not in done:
                heapq.heappush(heap, (inside[u].key(), u))
    return out
