"""Load the content of tamnd/algorithm: the area tree, the nodes, their proofs and their Python code."""

from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass, field

import yaml

from . import patches

WRITTEN_MIN_WORDS = 400  # spec handbook 00.5: a body of fewer words is a stub

LEVELS = ["intro", "core", "advanced", "research"]
KINDS = ["definition", "concept", "model", "abstract-type", "problem", "data-structure",
         "technique", "algorithm", "theorem"]
KIND_LABEL = {
    "definition": "Definition", "concept": "Concept", "model": "Model",
    "abstract-type": "Abstract type", "problem": "Problem", "data-structure": "Data structure",
    "technique": "Technique", "algorithm": "Algorithm", "theorem": "Theorem",
}


@dataclass
class Proof:
    id: str          # file stem, e.g. "correctness"
    title: str
    proves: list
    status: str
    body: str


@dataclass
class Impl:
    lang: str
    files: list      # [(name, text)] main files, tests excluded


@dataclass
class Node:
    slug: str
    dir: str
    fm: dict
    body: str
    proofs: list = field(default_factory=list)
    impls: dict = field(default_factory=dict)   # lang -> Impl (only python is loaded with text)
    langs: list = field(default_factory=list)   # every language with an impl dir

    @property
    def name(self): return self.fm["name"]
    @property
    def kind(self): return self.fm.get("kind", "concept")
    @property
    def level(self): return self.fm.get("level", "core")
    @property
    def area(self): return self.fm["area"]          # "sorting/comparison-sorts"
    @property
    def top(self): return self.area.split("/")[0]
    @property
    def sub(self): return self.area.split("/")[1] if "/" in self.area else ""
    @property
    def summary(self): return self.fm.get("summary", "")
    @property
    def words(self): return len(self.body.split())
    @property
    def written(self): return self.words >= WRITTEN_MIN_WORDS

    def key(self):
        lv = LEVELS.index(self.level) if self.level in LEVELS else 9
        kd = KINDS.index(self.kind) if self.kind in KINDS else 9
        return (lv, kd, self.slug)


@dataclass
class Area:
    id: str
    name: str
    summary: str
    number: int
    children: list    # [Sub]


@dataclass
class Sub:
    id: str
    name: str
    area: str
    number: int


def split_front(text: str):
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm) or {}, body.lstrip("\n")


class Corpus:
    def __init__(self, root: str):
        self.root = root
        self.areas: list[Area] = []
        self.nodes: dict[str, Node] = {}
        self._load_areas()
        self._load_nodes()

    def commit(self) -> str:
        try:
            out = subprocess.run(["git", "-C", self.root, "log", "-1", "--format=%H %cs %s"],
                                 capture_output=True, text=True, check=True).stdout.strip()
            return out
        except Exception:
            return "unknown"

    def _load_areas(self):
        tree = yaml.safe_load(open(os.path.join(self.root, "topics/areas.yaml")))
        for i, a in enumerate(tree, 1):
            subs = [Sub(c["id"], c["name"], a["id"], j) for j, c in enumerate(a.get("children") or [], 1)]
            self.areas.append(Area(a["id"], a["name"], a.get("summary", ""), i, subs))

    def area(self, ident) -> Area:
        for a in self.areas:
            if a.id == ident or str(a.number) == str(ident):
                return a
        raise KeyError(ident)

    def _load_nodes(self):
        base = os.path.join(self.root, "nodes")
        for dp, dn, fn in os.walk(base):
            dn.sort()
            if "node.md" not in fn:
                continue
            fm, body = split_front(patches.apply(os.path.relpath(os.path.join(dp, "node.md"), base),
                                                 open(os.path.join(dp, "node.md"), encoding="utf-8").read()))
            n = Node(fm["slug"], dp, fm, body)
            pdir = os.path.join(dp, "proofs")
            if os.path.isdir(pdir):
                for f in sorted(os.listdir(pdir)):
                    if f.endswith(".md"):
                        pfm, pbody = split_front(patches.apply(os.path.relpath(os.path.join(pdir, f), base),
                                                             open(os.path.join(pdir, f), encoding="utf-8").read()))
                        n.proofs.append(Proof(f[:-3], pfm.get("title", "Proof"), pfm.get("proves") or [],
                                              pfm.get("status", ""), pbody))
            idir = os.path.join(dp, "impl")
            if os.path.isdir(idir):
                n.langs = sorted(d for d in os.listdir(idir) if os.path.isdir(os.path.join(idir, d)))
                py = os.path.join(idir, "python")
                if os.path.isdir(py):
                    files = []
                    for f in sorted(os.listdir(py)):
                        if f.endswith(".py") and not f.startswith("test_") and not f.startswith("conftest"):
                            files.append((f, open(os.path.join(py, f), encoding="utf-8").read()))
                    if files:
                        n.impls["python"] = Impl("python", files)
            self.nodes[n.slug] = n

    def nodes_in(self, area_id: str, sub_id: str | None = None):
        out = [n for n in self.nodes.values() if n.top == area_id and (sub_id is None or n.sub == sub_id)]
        return sorted(out, key=lambda n: n.slug)


def clean_code(text: str) -> str:
    """Drop the SPDX and provenance header of an implementation file."""
    lines = text.split("\n")
    while lines and (lines[0].startswith("# SPDX") or lines[0].startswith("# Part of ") or lines[0].strip() == ""):
        lines.pop(0)
    text = "\n".join(lines).rstrip() + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)   # the book keeps one blank line where PEP 8 has two


LINK_RE = re.compile(r"\]\(/([a-z0-9][a-z0-9-]*)/(#[^)]*)?\)")
