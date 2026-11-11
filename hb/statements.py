"""Numbered statements and algorithms inside an entry (spec handbook 04.3).

The site writes a statement as a paragraph that starts with a bold label: `**Lemma 2 (the loop).** If …`, and
numbers lemmas, theorems and claims on their own, page by page, or not at all. The book numbers every statement and
every pseudocode block of an entry with one counter, after the entry's number, as a mathematics book numbers them
within a section: Definition 4.1.12.1, Lemma 4.1.12.2, Algorithm 4.1.12.3, Theorem 4.1.12.4. References in the
text to the site's numbers ("by Lemma 2", "Lemmas 1 and 3") become links that carry the book's numbers.

The work is done in two passes, because the proofs of an entry are placed among its sections only after they are
read. `mark` and `refs` put private-use markers into the Markdown of each part (the body, each proof); `finalize`
numbers the markers of the assembled entry in reading order and replaces them.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# kind → environment: theorem-like statements are set in italics, the others upright
KIND_ENV = {
    "Theorem": "hbthm", "Lemma": "hbthm", "Corollary": "hbthm", "Proposition": "hbthm",
    "Conjecture": "hbthm", "Claim": "hbthm", "Fact": "hbthm", "Invariant": "hbthm", "Observation": "hbthm",
    "Definition": "hbdefn", "Example": "hbdefn",
    "Remark": "hbrem",
}
LISTED = {"Theorem", "Proposition", "Corollary", "Definition", "Conjecture"}   # in the list of statements

_NOTE = r"(?:[^()\n]|\([^()\n]*\))*"
LABEL = re.compile(
    r"^\*\*(?P<kind>" + "|".join(KIND_ENV) + r")"
    r"(?: (?P<id>\d+(?:\.\d+)*[a-z]?|[A-H]|[IVX]+))?"
    r"(?: \((?P<note>" + _NOTE + r")\))?"
    r"(?P<dot>[.:]?)\*\*"
    r"(?: \((?P<note2>" + _NOTE + r")\)[.:])?"
    r"(?=\s|$)")
PROOF_START = re.compile(r"(?:^|\s)\*Proof\b[^*\n]{0,30}\.\*")
LIST_ITEM = re.compile(r"^(?:\d+[.)]|[-*+]|\([a-z0-9]+\))\s")
QED = re.compile(r"[ \t]*(\$\\(?:square|blacksquare|Box|qed)\$|∎|□)[ \t]*$", re.M)

S, E = "\ue000", "\ue001"        # private-use markers: S<tag><n>E
_MARK = re.compile(S + r"([SINA])(\d+)" + E)


@dataclass
class Stmt:
    kind: str
    sid: str          # the site's own label, '' if none
    note: str
    doc: str
    key: str          # the start of the statement text, to recognise a restatement
    algo: bool = False
    name: str = ""    # for an algorithm: the procedure


def _blocks(text: str) -> list[list[str]]:
    """The blocks of a Markdown text: runs of non-blank lines, with each fenced code block kept whole."""
    blocks, cur, fence = [], [], None
    for line in text.split("\n"):
        f = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence is None and f:
            fence = f.group(1)
        elif fence is not None and re.match(r"^\s*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", line):
            fence = None
            cur.append(line)
            continue
        if fence is None and not line.strip() and not f:
            if cur:
                blocks.append(cur)
                cur = []
            continue
        cur.append(line)
    if cur:
        blocks.append(cur)
    return blocks


def _is_fence(b: list[str]) -> bool:
    return bool(re.match(r"^\s*(`{3,}|~{3,})", b[0]))


def _norm(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", t.lower())[:80]


class Statements:
    def __init__(self, slug: str):
        self.slug = slug
        self.items: list[Stmt] = []
        self.defs: dict[str, dict[tuple[str, str], int]] = {}    # doc -> (kind, sid) -> index

    # ------------------------------------------------------------------ pass 1
    def _new(self, st: Stmt) -> tuple[int, bool]:
        """The index of a statement; a restatement of an earlier one (same label, or same text) gets its index."""
        for i, o in enumerate(self.items):
            if o.algo or o.kind != st.kind:
                continue
            if (st.sid and o.sid == st.sid) or (st.key and len(st.key) >= 30 and o.key == st.key):
                if o.doc != st.doc:
                    return i, False
        self.items.append(st)
        return len(self.items) - 1, True

    def mark(self, text: str, doc: str) -> str:
        """Wrap each statement of a part in a Div with a marker for its head; mark the end of each proof."""
        defs = self.defs.setdefault(doc, {})
        blocks = _blocks(text)
        out: list[str] = []
        i = 0
        while i < len(blocks):
            b = blocks[i]
            first = b[0]
            m = None if _is_fence(b) else LABEL.match(first)
            if m is None:
                out.append("\n".join(b))
                i += 1
                continue
            kind, sid = m.group("kind"), m.group("id") or ""
            note = m.group("note") or m.group("note2") or ""
            rest = "\n".join([first[m.end():].lstrip()] + b[1:])
            proof = ""
            pm = PROOF_START.search(rest)
            if pm:
                rest, proof = rest[:pm.start()].rstrip(), rest[pm.start():].lstrip()
            body = [rest] if rest.strip() else []
            j = i + 1
            if not proof:
                prev, label_only, in_list = rest, not rest.strip(), False
                while j < len(blocks):
                    nb = blocks[j]
                    if _is_fence(nb):
                        break
                    s = nb[0].lstrip()
                    if s.startswith("#") or PROOF_START.match(s) or LABEL.match(nb[0]) or s.startswith(":::"):
                        break
                    display = s.startswith("$$")
                    is_list = bool(LIST_ITEM.match(s))
                    cont = nb[0].startswith(("    ", "\t", "   ")) and in_list
                    prev_display = prev.rstrip().endswith("$$")
                    if (label_only or display or (is_list and (prev.rstrip().endswith(":") or in_list or label_only))
                            or cont or (prev_display and s[:1].islower())):
                        body.append("\n".join(nb))
                        prev, label_only, in_list = "\n".join(nb), False, is_list or cont
                        j += 1
                        continue
                    break
            st = Stmt(kind, sid, note.strip(), doc, _norm(" ".join(body))[:80])
            idx, fresh = self._new(st)
            if sid:
                defs.setdefault((kind, sid), idx)
            head = f"{S}S{idx}{E}"
            env = KIND_ENV[kind]
            text_ = "\n\n".join(body)
            cls = {"hbthm": "thm", "hbdefn": "defn", "hbrem": "rem"}[env]
            out.append(f'::: {{#{S}I{idx}{E} .stmt .{cls} latex-env="{env}"}}\n{head} {text_}\n:::')
            if proof:
                out.append(proof)
            i = j
        return QED.sub(lambda q: f' [{q.group(1)}]{{.qed latex-cmd="hbqed"}}', "\n\n".join(out))

    def refs(self, text: str, doc: str) -> str:
        """Replace the site's numbers in references ("by Lemma 2") with markers for the book's numbers."""
        own, body = self.defs.get(doc, {}), self.defs.get("body", {})
        if not own and not body:
            return text

        def find(kind, sid):
            return own.get((kind, sid), body.get((kind, sid)))

        kinds = "|".join(KIND_ENV)
        num = r"(?:\d+(?:\.\d+)*[a-z]?|[A-H])"
        pat = re.compile(r"(?<![\[\w*])(" + kinds + r")(s?)( " + num + r"(?:(?:,? and |, | or | to |–|-|, and )" + num + r")*)"
                         r"(?![\w.]\d)(?! (?:of|in|from) )")

        def repl(m):
            pre = m.string[max(0, m.start() - 40):m.start()]
            # a citation of a book or paper: "(Higham, Lemma 3.1)", "Goldberg, Theorem 8", "[2, Theorem 3]"
            if re.search(r"(?:[A-Z][\w'’-]+(?: et al\.)?|\d{4}|\d+),\s*$", pre):
                return m.group(0)
            kind = m.group(1)
            hit = False

            def one(n):
                nonlocal hit
                i = find(kind, n.group(0))
                if i is None:
                    return n.group(0)
                hit = True
                return f"{S}N{i}{E}"
            ids = re.sub(num, one, m.group(3))
            return m.group(1) + m.group(2) + ids if hit else m.group(0)

        out, fence = [], None
        for line in text.split("\n"):
            f = re.match(r"^\s*(`{3,}|~{3,})", line)
            if f:
                fence = None if fence else f.group(1)
                out.append(line)
                continue
            if fence:
                out.append(line)
                continue
            parts = re.split(r"(\$\$.*?\$\$|\$[^$]+\$|`[^`]*`|\]\([^)]*\))", line)
            out.append("".join(p if k % 2 else pat.sub(repl, p) for k, p in enumerate(parts)))
        return "\n".join(out)

    def algorithm(self, body: str) -> str:
        """A marker for the caption of a pseudocode block."""
        name = ""
        for line in body.split("\n"):
            s = re.sub(r"^L\d+[a-z]?\s+", "", line.strip())
            if s:
                mm = re.match(r"([A-Z][A-Z0-9]*(?:[-_][A-Z0-9]+)*)\s*\(", s)
                name = mm.group(1) if mm else ""
                break
        self.items.append(Stmt("Algorithm", "", "", "", "", algo=True, name=name))
        return f"{S}A{len(self.items) - 1}{E}"

    # ------------------------------------------------------------------ pass 2
    def finalize(self, md: str, num: str, entry: str, listed: list | None = None) -> str:
        """Number the statements in the order they appear, and put the numbers in place of the markers."""
        numbers: dict[int, str] = {}
        ids: dict[int, str] = {}
        k = 0
        for m in _MARK.finditer(md):
            tag, i = m.group(1), int(m.group(2))
            if tag in "SA" and i not in numbers:
                k += 1
                numbers[i] = f"{num}.{k}"
                ids[i] = f"{self.slug}--st-{k}"
        seen_id: dict[int, int] = {}

        def repl(m):
            tag, i = m.group(1), int(m.group(2))
            st = self.items[i]
            n = numbers.get(i)
            if n is None:          # a reference to a statement that is not printed: keep the site's label
                return st.sid or "?"
            if tag == "I":
                c = seen_id.get(i, 0)
                seen_id[i] = c + 1
                return ids[i] if c == 0 else f"{ids[i]}-again{c}"
            if tag == "N":
                return f"[{n}](#{ids[i]})"
            if tag == "A":
                return f"{n}"
            head = f"{st.kind} {n}"
            if st.note:
                return f'[{head}]{{.sthead latex-cmd="hbsthead"}} [({st.note}).]{{.stnote latex-cmd="hbstnote"}}'
            return f'[{head}.]{{.sthead latex-cmd="hbsthead"}}'

        md = _MARK.sub(repl, md)
        if listed is not None:
            for i, n in sorted(numbers.items(), key=lambda x: [int(p) for p in x[1].split(".")]):
                st = self.items[i]
                if st.kind in LISTED:
                    listed.append((n, st.kind, st.note, ids[i], entry))
        return md

    def algorithm_names(self) -> dict[int, str]:
        return {i: s.name for i, s in enumerate(self.items) if s.algo}


def statements_md(book, vol, refs) -> str:
    """The appendix *Theorems and definitions*: the main numbered statements of the volume, chapter by chapter,
    with their pages. Lemmas, claims, facts, examples and remarks are left out; they serve a nearby theorem."""
    from .prep import md_plain
    by_ch: dict[str, list] = {}
    for n, kind, note, ident, slug in refs.statements:
        by_ch.setdefault(".".join(n.split(".")[:2]), []).append((n, kind, note, ident, slug))
    if not by_ch:
        return ""
    out = ["The definitions, theorems, propositions, corollaries and conjectures of this volume, in the order of "
           "the text. Each has the number of its entry and its place in the entry; a theorem stated again in a "
           "proof keeps its first number.\n"]
    for ch in vol.chapters:
        rows = by_ch.get(ch.num)
        if not rows:
            continue
        out.append(f"#### Chapter {ch.num}: {md_plain(ch.name)} {{.unnumbered}}\n")
        lines = []
        for n, kind, note, ident, slug in rows:
            node = book.corpus.nodes[slug]
            nt = f" ({note})" if note else ""
            lines.append(f"[{kind} {n}](#{ident}){nt}, in *{md_plain(node.name)}* `\\hbstpage{{{ident}}}`{{=latex}}\n")
        out.append('::: {.stlist latex-env="hbstlist"}\n' + "\n".join(lines) + ":::\n")
    return "\n".join(out)


def numbering_note(vol, refs) -> str:
    """A paragraph of the volume introduction on how the volume is numbered, with examples from the volume."""
    ex = refs.statements[0] if refs.statements else None
    ch = next((c for c in vol.chapters if c.entries), None)
    if ch is None:
        return ""
    k = min(3, len(ch.entries))
    e = f"{ch.num}.{k}"
    s = (f"Entries are numbered within their chapter: {e} is entry {k} of Chapter {ch.num}. Inside an entry, the "
         "definitions, theorems, lemmas and other statements, and the algorithms in pseudocode, share one counter "
         "that continues the number of the entry")
    if ex:
        s += f", so that {ex[1]} {ex[0]} is item {ex[0].split('.')[-1]} of entry {'.'.join(ex[0].split('.')[:3])}"
    s += (". Theorems, lemmas and the other claims are set in italics, definitions and examples in roman type, and "
          "a proof ends with a square at the right of its last line. Exercises are numbered within the chapter, as "
          f"{ch.num}.1, and so are figures. A small grey number after a link gives the entry it points to. The "
          "appendix *Theorems and definitions* lists the main statements of the volume with their pages.\n")
    return s
