"""Make the pandoc Markdown of a volume from the nodes and the learner layer (spec handbook 04.3).

One Markdown file serves both targets. Raw blocks carry what differs:
```{=latex}``` blocks are dropped by the EPUB writer, and elements with the class
`html-only` are dropped from the LaTeX output by filters/hb.lua.
"""

from __future__ import annotations

import re

from .mathcost import cost_md
from .book import Book, Chapter, Volume
from .corpus import KIND_LABEL, Node, clean_code
from .statements import Statements

SITE = "https://algorithm.tamnd.com"
LEVEL_LABEL = {"intro": "Intro", "core": "Core", "advanced": "Advanced", "research": "Research"}
CASE_ORDER = ["worst", "average", "expected", "amortized", "best", "build", "preprocessing",
              "extra", "aux", "total"]

# --------------------------------------------------------------------------- escaping

_TEX_SPECIAL = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$", "&": r"\&",
                "#": r"\#", "^": r"\textasciicircum{}", "_": r"\_", "%": r"\%", "~": r"\textasciitilde{}"}


def _math_ok(m: str) -> bool:
    """A $…$ span is mathematics only if it looks like it: no leading space or
    punctuation, balanced braces. Pseudocode such as `t = $; I ← {$}` uses $ as a symbol."""
    if not m or m[0] in " ;,.)" or m[-1] == " ":
        return False
    depth = 0
    for c in re.sub(r"\\[{}]", "", m):
        depth += (c == "{") - (c == "}")
        if depth < 0:
            return False
    return depth == 0


def tex(s: str) -> str:
    """Escape plain text for LaTeX; $…$ stays mathematics."""
    out = []
    for i, part in enumerate(re.split(r"(\$[^$]+\$)", s)):
        if i % 2 and _math_ok(part[1:-1]):
            out.append(r"\(" + part[1:-1] + r"\)")
        else:
            out.append("".join(_TEX_SPECIAL.get(c, c) for c in part))
    return "".join(out)


def md_plain(s: str) -> str:
    """Escape plain text for a Markdown heading or link text."""
    return re.sub(r"([*_`\[\]<>#\\])", r"\\\1", s)


def attr(s: str) -> str:
    return s.replace('"', "'")

# --------------------------------------------------------------------------- references


# Slugs that the site gives to a narrow entry while other areas link them in a wider sense: /total-order/ is
# Lamport's total order of events (Volume 21), but sorting, searching and heaps link it for the order relation.
# Outside the area of the entry such a link keeps its text and loses its target.
NARROW_SLUGS = {"total-order": "distributed",   # elsewhere: the order relation of sorting and searching
                "tree-hashing": "cryptography"}   # elsewhere: canonical hashes of rooted trees (isomorphism)


def narrow_ok(slug: str, node) -> bool:
    top = NARROW_SLUGS.get(slug)
    return top is None or node is None or node.top == top


class Refs:
    """Turn a slug into a link with its number (spec handbook 07.1)."""

    def __init__(self, book: Book, volume: Volume):
        self.book, self.volume = book, volume
        self.statements: list = []     # (number, kind, note, id, entry slug) for the list of statements

    def target(self, slug: str, frag: str = "") -> str:
        if self.book.volume_of.get(slug) == self.volume.number:
            return "#" + slug
        return f"{SITE}/{slug}/{frag or ''}"

    def link(self, slug: str, text: str | None = None, number=True) -> str:
        n = self.book.corpus.nodes.get(slug)
        name = text or (n.name if n else slug)
        s = f"[{md_plain(name)}]({self.target(slug)})"
        num = self.book.ref(slug)
        if number and num:
            s += f" [{num}]{{.ref}}"
        return s

    def rewrite_body(self, md: str, node: Node, in_proof: bool = False) -> str:
        for slug in NARROW_SLUGS:
            if not narrow_ok(slug, node):
                md = re.sub(r"\[([^\[\]]*)\]\(/" + slug + r"/(?:#[^)]*)?\)", r"\1", md)

        def repl(m):
            slug, frag = m.group(1), m.group(2) or ""
            if slug == node.slug and frag:
                return "](" + frag + ")"
            if slug in self.book.corpus.nodes:
                return "](" + self.target(slug, frag) + ")"
            return f"]({SITE}/{slug}/{frag})"
        md = re.sub(r"\]\(/([a-z0-9][a-z0-9-]*)/(#[^)]*)?\)", repl, md)

        def proof(slug, pid):
            n = self.book.corpus.nodes.get(slug)
            if n is None:
                return f"]({SITE}/{slug}/proofs/{pid}/)"
            if pid not in {p.id for p in n.proofs}:
                return "](" + self.target(slug) + ")"
            if self.book.volume_of.get(slug) == self.volume.number:
                return f"](#{slug}--proof-{pid})"
            return f"]({SITE}/{slug}/proofs/{pid}/)"
        # links to the proofs of another node, of the same node, and (inside a proof) of a sibling proof
        md = re.sub(r"\]\(/([a-z0-9][a-z0-9-]*)/proofs/([a-z0-9-]+)(?:\.md|/)?\)", lambda m: proof(m[1], m[2]), md)
        md = re.sub(r"\]\((?:\./)?proofs/([a-z0-9-]+)(?:\.md|/)?\)", lambda m: proof(node.slug, m[1]), md)
        ids = {p.id for p in node.proofs}
        md = re.sub(r"\]\((?:\./)?([a-z0-9-]+)\.md\)",
                    lambda m: proof(node.slug, m[1]) if m[1] in ids else m[0], md)
        if in_proof:   # a proof page sits at /slug/proofs/id/: ../ is the entry, ../other/ (or other/) a sibling proof
            md = re.sub(r"\]\((?:\.\./)?([a-z0-9-]+)/\)", lambda m: proof(node.slug, m[1]) if m[1] in ids else m[0], md)
            md = re.sub(r"\]\(\.\./([a-z0-9-]+)\)", lambda m: proof(node.slug, m[1]) if m[1] in ids else m[0], md)
            md = re.sub(r"\]\(\.\./\)", "](" + self.target(node.slug) + ")", md)
        md = re.sub(r"\]\((?:\./)?impl/[^)]*\)", f"]({SITE}/{node.slug}/#code-tabs)", md)
        return md

# --------------------------------------------------------------------------- pseudocode

_KW = r"if|then|else|elif|while|do|for|each|repeat|until|return|break|continue|loop|procedure|function|end|yield|goto|case|of|downto|to|and|or|not|in"
_KW_RE = re.compile(r"(?<![\w-])(" + _KW + r")(?![\w-])")
_PROC_RE = re.compile(r"(?<![\w])([A-Z][A-Z0-9]*(?:[-_][A-Z0-9]+)+|[A-Z]{3,}[0-9]*)(?![\w])")
_LABEL_RE = re.compile(r"^(L\d+[a-z]?)(\s+|$)")


def _split_comment(line: str):
    i = line.find("▷")
    if i < 0:
        return line.rstrip(), ""
    return line[:i].rstrip(), line[i + 1:].strip()


def _kw_ok(code: str) -> set:
    """Which keywords to set in bold on this line. 'to', 'in', 'of', 'and', 'or', 'not' only in control lines."""
    first = code.strip().split(" ", 1)[0].lower() if code.strip() else ""
    control = first in {"if", "while", "for", "until", "elif", "else", "repeat", "return", "loop"}
    allowed = {"if", "then", "else", "elif", "while", "do", "for", "repeat", "until", "return",
               "break", "continue", "loop", "procedure", "function", "end", "yield", "goto"}
    if control:
        allowed |= {"each", "to", "downto", "in", "and", "or", "not", "of", "case"}
    return allowed


def pseudo_lines(text: str):
    """Parse a pseudo block into (label, indent, code, comment) rows (spec 06.4 of the site)."""
    rows = []
    lines = text.rstrip("\n").split("\n")
    for raw in lines:
        if not raw.strip():
            rows.append(None)
            continue
        m = _LABEL_RE.match(raw)
        if m:
            label = m.group(1)
            rest = raw[4:] if len(raw) >= 4 and len(m.group(0)) <= 4 else raw[len(m.group(0)):]
            if len(raw) > 4 and raw[:4].strip() == label:
                rest = raw[4:]
        else:
            label = ""
            rest = raw[4:] if raw.startswith("    ") else raw
        indent = len(rest) - len(rest.lstrip(" "))
        code, comment = _split_comment(rest.strip())
        rows.append((label, indent // 4 if indent >= 4 else (indent + 1) // 4, code, comment))
    return rows


def _pseudo_tex_code(code: str) -> str:
    allowed = _kw_ok(code)
    parts = re.split(r"(\"[^\"]*\")", code)   # leave quoted strings alone
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(tex(p))
            continue
        toks = re.split(r"(" + _PROC_RE.pattern + r")", p)
        buf = []
        j = 0
        while j < len(toks):
            t = toks[j]
            if j % 3 == 1:   # a procedure name (the regex has one inner group, so step 3)
                buf.append(r"\hbproc{" + tex(t) + "}")
                j += 2
                continue
            if j % 3 == 2:
                j += 1
                continue
            esc = tex(t)
            esc = _KW_RE.sub(lambda m: r"\hbkw{" + m.group(1) + "}" if m.group(1) in allowed else m.group(1), esc)
            buf.append(esc)
            j += 1
        out.append("".join(buf))
    return "".join(out)


def pseudo_latex(text: str, caption: tuple | None = None) -> str:
    rows = pseudo_lines(text)
    out = [r"\begin{hbpseudo}"]
    if caption:
        out.append(r"\hbpcap{%s}{%s}{%s}" % (caption[0], tex(caption[1]), caption[2]))
    for r in rows:
        if r is None:
            out.append(r"\hbpgap")
            continue
        label, ind, code, comment = r
        out.append(r"\hbpl{%s}{%d}{%s}{%s}" % (label, ind, _pseudo_tex_code(code), tex(comment)))
    out.append(r"\end{hbpseudo}")
    return "\n".join(out)


def _html(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def pseudo_html(text: str, caption: tuple | None = None) -> str:
    rows = pseudo_lines(text)
    out = ['<div class="pseudo">']
    if caption:
        name = f' <span class="proc">{_html(caption[1])}</span>' if caption[1] else ""
        out.append(f'<div class="pcap"><b>{caption[0]}</b>{name}</div>')
    for r in rows:
        if r is None:
            out.append('<div class="pl gap"></div>')
            continue
        label, ind, code, comment = r
        allowed = _kw_ok(code)
        c = _html(code)
        c = _PROC_RE.sub(lambda m: f'<span class="proc">{m.group(1)}</span>', c)
        c = _KW_RE.sub(lambda m: f"<b>{m.group(1)}</b>" if m.group(1) in allowed else m.group(1), c)
        cm = f'<span class="cm">▷ {_html(comment)}</span>' if comment else ""
        out.append(f'<div class="pl"><span class="ln">{label}</span>'
                   f'<span class="code" style="padding-left:{1.5 * ind:.1f}em">{c}</span>{cm}</div>')
    out.append("</div>")
    return "\n".join(out)

# --------------------------------------------------------------------------- code blocks and html


FENCE_RE = re.compile(r"^(`{3,})([^\n`]*)\n(.*?)^\1[ \t]*$", re.M | re.S)


def convert_fences(md: str, st: Statements | None = None) -> str:
    """Code fences to the forms of the book. With `st`, each pseudocode block is a numbered algorithm."""
    def repl(m):
        info, body = m.group(2).strip(), m.group(3)
        lang = info.split()[0] if info else ""
        if lang == "pseudo":
            cap = None
            if st is not None:
                mk = st.algorithm(body)
                cap = ("Algorithm " + mk, st.items[-1].name, mk.replace("A", "I", 1))
            return ("```{=latex}\n" + pseudo_latex(body, cap) + "\n```\n\n```{=html}\n" + pseudo_html(body, cap) + "\n```\n")
        if lang in ("", "text", "txt", "plain"):
            return "```{.plain}\n" + body + "```"
        return "```" + lang + "\n" + body + "```"
    return FENCE_RE.sub(repl, md)


def clean_html(md: str) -> str:
    md = re.sub(r"<summary>(.*?)</summary>", r"**\1.**", md, flags=re.S)
    md = re.sub(r"</?details[^>]*>", "", md)
    md = re.sub(r"<sub>(.*?)</sub>", lambda m: "~" + m.group(1).replace(" ", "\\ ") + "~", md)
    md = re.sub(r"<sup>(.*?)</sup>", lambda m: "^" + m.group(1).replace(" ", "\\ ") + "^", md)
    md = re.sub(r"<br\s*/?>", " ", md)
    return fix_math(md)


# `$j' $`: KaTeX on the site accepts a space before the closing dollar; pandoc does not, and prints the dollars
# and the TeX between them as text. Two forms are repaired: a span after a space or punctuation (`the potential
# $\Phi = $ the number`), and an argument list after a procedure name (`RANK$(b) - $ RANK$(a)$`,
# `UseHint$(h, r) = $ HighBits$(r + z)$`), where the closing dollar may also touch the next name
# (`X25519$(a, $X25519$(b, 9))`).
_MATH_TRAIL = re.compile(r"(?:(?<![\\$\w])\$([^\s$][^$\n]{0,60}?)\s+\$(?![\w$])"
                         r"|(?<=\w)(?=\$\()\$([^\s$][^$\n]{0,60}?)\s+\$(?![\d$]))")


def fix_math(md: str) -> str:
    def line(ln: str) -> str:
        if "$" not in ln or "$$" in ln:
            return ln
        i = 0
        while (m := _MATH_TRAIL.search(ln, i)):
            if ln[:m.start()].replace("\\$", "").count("$") % 2:
                i = m.start() + 1          # this dollar closes a span: try the next one
                continue
            g = m.group(1) if m.group(1) is not None else m.group(2)
            ln = ln[:m.start()] + "$" + g + "$" + ln[m.end():]
            i = m.start() + len(g) + 2
        return ln
    return "\n".join(line(x) for x in md.split("\n"))

# --------------------------------------------------------------------------- sections of a body


def split_h2(body: str):
    """Split a body into [(heading or None, text)], ignoring headings inside code fences."""
    parts, cur_h, buf, fence = [], None, [], None
    for line in body.split("\n"):
        f = re.match(r"^(`{3,})", line)
        if f:
            if fence is None:
                fence = f.group(1)
            elif line.strip().startswith(fence) and line.strip() == line.strip()[:len(line.strip())]:
                if re.match(r"^" + fence + r"\s*$", line):
                    fence = None
        if fence is None and line.startswith("## "):
            parts.append((cur_h, "\n".join(buf)))
            cur_h, buf = line[3:].strip(), []
        else:
            buf.append(line)
    parts.append((cur_h, "\n".join(buf)))
    return parts


def shift_headings(md: str, by: int) -> str:
    """Move every ATX heading down by `by` levels, outside code fences; mark them unnumbered."""
    out, fence = [], None
    for line in md.split("\n"):
        f = re.match(r"^(`{3,})", line)
        if f:
            if fence is None:
                fence = f.group(1)
            elif re.match(r"^" + fence + r"\s*$", line):
                fence = None
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line) if fence is None else None
        if m:
            lvl = min(6, len(m.group(1)) + by)
            text = m.group(2)
            if not text.endswith("}"):
                text += " {.unnumbered}"
            line = "#" * lvl + " " + text
        out.append(line)
    return "\n".join(out)

# --------------------------------------------------------------------------- an entry


def _md_backslash(t: str) -> str:
    """A backslash in source text outside $…$ is a character (POSIX "\\n"), not a TeX command."""
    parts = re.split(r"(\$[^$]+\$)", t)
    return "".join(p if i % 2 else p.replace("\\", "\\\\") for i, p in enumerate(parts))


def fmt_sources(sources) -> list[str]:
    items = []
    for s in sources or []:
        title = _md_backslash((s.get("title") or "").strip().rstrip("."))
        loc = _md_backslash((s.get("locator") or "").strip().rstrip("."))
        # editorial markers in the source data, e.g. "(pages to be checked)", are not for readers
        loc = re.sub(r"\s*\([^()]*to be checked[^()]*\)", "", loc).strip().rstrip(".")
        if re.fullmatch(r"[^()]*to be checked[^()]*", loc):
            loc = ""
        link = ""
        if s.get("paper"):
            p = str(s["paper"])
            if p.startswith("doi:"):
                link = f"<https://doi.org/{p[4:]}>"
            elif p.startswith("arxiv:"):
                link = f"<https://arxiv.org/abs/{p[6:]}>"
            else:
                link = p
        elif s.get("book"):
            b = str(s["book"])
            link = "ISBN " + b[5:] if b.startswith("isbn:") else b
        elif s.get("url"):
            link = f"<{s['url']}>"
        parts = [title] if title else []
        if loc:
            parts.append(loc[0].upper() + loc[1:])
        if link:
            parts.append(link)
        if parts:
            items.append(". ".join(parts) + ".")
    return items


def complexity_rows(c: dict, md: bool = False) -> list[tuple[str, str]]:
    """(label, value) rows of a complexity field; with md=True the values are Markdown with math."""
    rows = []
    if not c:
        return rows
    for k, v in c.items():
        if k == "vars" or not isinstance(v, dict):
            continue
        keys = sorted(v, key=lambda x: (CASE_ORDER.index(x) if x in CASE_ORDER else 50, x))
        if md:
            val = " · ".join(f"{cost_md(v[x], md_plain)} {x.replace('_', ' ')}" for x in keys)
        else:
            val = " · ".join(f"{v[x]} {x.replace('_', ' ')}" for x in keys)
        label = {"time": "Time", "space": "Space"}.get(k, k.replace("_", " ").capitalize())
        rows.append((label, val))
    vars_ = c.get("vars")
    if isinstance(vars_, dict) and vars_:
        if md:
            rows.append(("Where", "; ".join(f"{cost_md(k, md_plain)} is {md_plain(str(v))}" for k, v in vars_.items())))
        else:
            rows.append(("Where", "; ".join(f"{k} is {v}" for k, v in vars_.items())))
    return rows


def properties_text(p: dict) -> str:
    out = []
    for k, v in (p or {}).items():
        name = k.replace("_", " ")
        if v is True:
            out.append(name)
        elif v is False:
            out.append("not " + name)
        else:
            out.append(f"{name}: {v}")
    return " · ".join(out)


def facts(node: Node, refs: Refs) -> str:
    fm = node.fm
    rows = []
    if fm.get("solves"):
        rows.append(("Solves", ", ".join(refs.link(s) for s in fm["solves"])))
    if fm.get("implements"):
        rows.append(("Implements", ", ".join(refs.link(s) for s in fm["implements"])))
    if fm.get("model"):
        m = fm["model"]
        rows.append(("Model", refs.link(m) if m in refs.book.corpus.nodes else md_plain(str(m))))
    for k, v in complexity_rows(fm.get("complexity"), md=True):
        rows.append((k, v))
    if fm.get("properties"):
        rows.append(("Properties", md_plain(properties_text(fm["properties"]))))
    if fm.get("prereqs"):
        need = [s for s in fm["prereqs"] if narrow_ok(s, node)]
        if need:
            rows.append(("Needs", ", ".join(refs.link(s) for s in need)))
    h = fm.get("history")
    if isinstance(h, dict) and (h.get("year") or h.get("people")):
        who = ", ".join(h.get("people") or [])
        rows.append(("Origin", md_plain(", ".join(x for x in [str(h.get("year") or ""), who] if x))))
    if not rows:
        return ""
    lines = ['::: {.facts latex-env="hbfacts"}']
    for k, v in rows:
        lines.append(f'[{k}]{{.fk latex-cmd="hbfk"}} {v}\n')
    lines.append(":::")
    return "\n".join(lines)


def solver_table(node: Node, refs: Refs) -> str:
    solvers = [n for n in refs.book.corpus.nodes.values() if node.slug in (n.fm.get("solves") or [])]
    if not solvers:
        return ""
    def sk(n):
        num = refs.book.ref(n.slug)
        return (0 if num else 1, [int(x) for x in num.split(".")] if num else [], n.name.lower())
    rows = ["| Algorithm | Time | Space |", "|---|---|---|"]
    for n in sorted(solvers, key=sk):
        t = (n.fm.get("complexity") or {}).get("time") or {}
        s = (n.fm.get("complexity") or {}).get("space") or {}
        tv = t.get("worst") or t.get("expected") or t.get("average") or next(iter(t.values()), "") if isinstance(t, dict) else ""
        sv = s.get("extra") or s.get("total") or next(iter(s.values()), "") if isinstance(s, dict) else ""
        rows.append(f"| {refs.link(n.slug)} | {cost_md(tv, md_plain) if tv else ""} | {cost_md(sv, md_plain) if sv else ""} |")
    return "\n".join(rows) + "\n\n: The algorithms of this handbook that solve the problem. {.solvers}\n"


def implementation(node: Node, refs: Refs) -> str:
    if "python" not in node.impls:
        if node.langs:
            return (f"Tested implementations in {len(node.langs)} languages are on the site: "
                    f"<{SITE}/{node.slug}/>.\n")
        return ""
    out = []
    others = [l for l in node.langs if l != "python"]
    for name, text in node.impls["python"].files:
        out.append(f"::: {{.code latex-env=\"hbcode\" latex-arg=\"{name}\"}}\n```python\n{clean_code(text)}```\n:::\n")
    tail = "The code above passes its tests in the repository of the site."
    if others:
        tail += f" The site also has the code in {len(others)} more languages: <{SITE}/{node.slug}/#code-tabs>."
    out.append(tail + "\n")
    return "\n".join(out)


def proofs_md(node: Node, bodies: dict | None = None) -> str:
    out = []
    for p in node.proofs:
        body = (bodies or {}).get(p.id) or fix_math(shift_headings(p.body, 4))
        status = {"full": "", "sketch": " (sketch)"}.get(p.status, "")
        out.append(f'::: {{#{node.slug}--proof-{p.id} .proof latex-env="hbproof"}}\n'
                   f'[Proof: {md_plain(p.title)}{status}]{{.prooftitle latex-cmd="hbprooftitle"}}\n\n'
                   f'{body.strip()}\n:::\n')
    return "\n".join(out)


def entry_md(node: Node, num: str, refs: Refs) -> str:
    kind = KIND_LABEL.get(node.kind, node.kind.title())
    level = LEVEL_LABEL.get(node.level, node.level.title())
    head = [
        "```{=latex}",
        r"\hbentry{%s}{%s}{%s}{%s}{%s}" % (num, tex(node.name), node.slug, kind, level),
        "```",
        "",
        f"### [{num}]{{.num}} {md_plain(node.name)} {{#{node.slug} .html-only}}",
        "",
        f"[{kind} · {level}]{{.badge .html-only}}",
        "",
        f'::: {{.lead latex-env="hblead"}}\n{node.summary.strip()}\n:::',
        "",
        facts(node, refs),
        "",
    ]
    body = clean_html(refs.rewrite_body(node.body, node))
    st = Statements(node.slug, node.name, node.kind)
    body = st.mark(body, "body")
    pbodies = {p.id: st.mark(fix_math(shift_headings(refs.rewrite_body(p.body, node, in_proof=True), 4)), p.id) for p in node.proofs}
    body = st.refs(body, "body")
    pbodies = {k: st.refs(v, k) for k, v in pbodies.items()}
    sections = split_h2(body)
    have = {h for h, _ in sections if h}
    out = []
    proofs_placed = not node.proofs
    impl_placed = False
    proof_anchor = next((h for h in ["Correctness", "Proof", "Complexity", "History"] if h in have), None)
    for h, text in sections:
        if h is None:
            out.append(text.strip())
            continue
        if h in ("Implementations", "Implementation"):
            impl = implementation(node, refs)
            impl_placed = True
            if impl:
                out.append(f"## Implementation\n\n{text.strip()}\n\n{impl}")
            continue
        if h == "References":
            if not proofs_placed:
                out.append(proofs_md(node, pbodies)); proofs_placed = True
            if not impl_placed and node.langs:
                out.append("## Implementation\n\n" + implementation(node, refs)); impl_placed = True
            items = fmt_sources(node.fm.get("sources"))
            if text.strip() or items:
                out.append("## References\n\n" + text.strip() + "\n\n" + (
                    '::: {.refs latex-env="hbrefs"}\n' + "\n".join(f"1. {i}" for i in items) + "\n:::" if items else ""))
            continue
        if h in ("History",) and not impl_placed and node.langs and "Implementations" not in have:
            out.append("## Implementation\n\n" + implementation(node, refs)); impl_placed = True
        sec = f"## {h}\n\n{text.strip()}"
        if h == "Known algorithms":
            sec += "\n\n" + solver_table(node, refs)
        out.append(sec)
        if h == proof_anchor and not proofs_placed:
            out.append(proofs_md(node, pbodies)); proofs_placed = True
    if not proofs_placed:
        out.append(proofs_md(node, pbodies))
    if not impl_placed and node.langs:
        out.append("## Implementation\n\n" + implementation(node, refs))
    see = [s for s in node.fm.get("see_also") or [] if s in refs.book.corpus.nodes]
    if see:
        out.append('::: {.seealso latex-env="hbseealso"}\n' + ", ".join(refs.link(s) for s in see) + ".\n:::")
    md = "\n\n".join(x for x in out if x and x.strip())
    md = convert_fences(md, st)
    md = shift_headings(md, 2)     # ## → ####, ### → #####
    md = scope_anchors(md, node.slug)
    md = st.finalize(md, num, node.slug, refs.statements)
    return "\n".join(head) + "\n" + md + "\n"


def _anchor(text: str) -> str:
    """The identifier the site gives a heading: lower case, punctuation dropped, spaces to hyphens."""
    t = re.sub(r"\{[^{}]*\}\s*$", "", text).strip().lower()
    t = re.sub(r"[^\w\s-]", "", t)
    return re.sub(r"\s+", "-", t).strip("-")


def scope_anchors(md: str, slug: str) -> str:
    """Give the section headings of an entry identifiers of their own (`quicksort--complexity`), and point the
    entry's links to its own sections (`[below](#complexity)`) at them. Without this, such a link found the first
    heading of that name in the whole volume, in another entry."""
    out, fence, ids = [], None, set(re.findall(r"\{#(" + re.escape(slug) + r"--[^\s}]+)", md))
    for line in md.split("\n"):
        f = re.match(r"^(`{3,}|~{3,})", line)
        if f:
            if fence is None:
                fence = f.group(1)[0]
            elif f.group(1)[0] == fence:
                fence = None
        elif fence is None and (m := re.match(r"^(#{4,6} )(.*?)(?:\s*\{([^{}]*)\})?\s*$", line)):
            attrs = m.group(3) or ""
            if "#" not in attrs and (a := _anchor(m.group(2))):
                ident, k = f"{slug}--{a}", 1
                while ident in ids:
                    k += 1
                    ident = f"{slug}--{a}-{k}"
                ids.add(ident)
                line = f"{m.group(1)}{m.group(2)} {{#{ident}{' ' + attrs if attrs else ''}}}"
        out.append(line)
    md = "\n".join(out)
    return re.sub(r"\]\(#([a-z0-9][a-z0-9-]*)\)",
                  lambda m: f"](#{slug}--{m[1]})" if f"{slug}--{m[1]}" in ids else m.group(0), md)

# --------------------------------------------------------------------------- learner layer


def glue(book: Book, refs: Refs, *parts, shift: int = 2) -> str:
    """A page of the learner layer, with its links rewritten and its headings moved down."""
    t = book.text(*parts)
    if not t.strip():
        return ""
    t = fix_math(re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S))

    def repl(m):
        slug, frag = m.group(1), m.group(2) or ""
        return "](" + refs.target(slug, frag) + ")"
    t = re.sub(r"\]\(/([a-z0-9][a-z0-9-]*)/(#[^)]*)?\)", repl, t)
    # add the number after each link to an entry: [merge sort](#merge-sort) → … [4.1.12]
    def addnum(m):
        txt, tgt = m.group(1), m.group(2)
        slug = tgt[1:] if tgt.startswith("#") else tgt.rstrip("/").split("/")[-1]
        num = book.ref(slug)
        return f"[{txt}]({tgt})" + (f" [{num}]{{.ref}}" if num else "")
    t = re.sub(r"(?<!!)\[([^\]]+)\]\(((?:#|" + re.escape(SITE) + r"/)[a-z0-9-]+/?)\)", addnum, t)
    t = convert_fences(t)
    return shift_headings(t, shift)


def chapter_md(book: Book, vol: Volume, ch: Chapter, refs: Refs, fig: str = "") -> str:
    out = [
        "```{=latex}",
        r"\hbchapter{%s}{%s}{ch-%s}" % (ch.num, tex(ch.name), ch.id),
        "```",
        "",
        f"# [{ch.num}]{{.num}} {md_plain(ch.name)} {{#ch-{ch.id} .html-only}}",
        "",
    ]
    opening = glue(book, refs, vol.id, ch.id, "opening.md")
    if opening:
        out.append(opening)
    if ch.entries:
        out.append(roadmap(book, ch, refs))
    if fig:
        out.append(fig)
    elif not opening:
        out.append("The entries of this chapter are being written. "
                   f"The planned topics are listed below and on the site: <{SITE}/areas/>.")
    # Group headings get their own identifiers: without one, pandoc's EPUB writer makes `quicksort` from the
    # heading "Quicksort", which then collides with the entry of that name and can capture its links.
    cid = "ch-" + ch.num.replace(".", "-")
    for gi, g in enumerate(ch.groups, 1):
        if g.title:
            out += ["```{=latex}", r"\hbgroup{%s}" % tex(g.title), "```", "",
                    f"## {md_plain(g.title)} {{#{cid}-g{gi} .html-only}}", ""]
            if g.intro:
                out.append(f'::: {{.groupintro latex-env="hbgroupintro"}}\n{glue_inline(book, refs, g.intro)}\n:::\n')
        for e in g.entries:
            out.append(entry_md(e, book.ref(e.slug), refs))
    if ch.stubs:
        out += ["```{=latex}", r"\hbgroup{Further topics}", "```", "",
                f"## Further topics {{#{cid}-further .html-only}}", "",
                "These topics belong to the chapter. Their entries are not written yet; "
                "the site has a short page for each.\n",
                '::: {.further latex-env="hbfurther"}']
        for s in ch.stubs:
            out.append(f"- **{md_plain(s.name)}** ({KIND_LABEL.get(s.kind, s.kind)}). {s.summary.strip()} "
                       f"<{SITE}/{s.slug}/>")
        out.append(":::\n")
    for fname, title in [("summary.md", "Summary"), ("exercises.md", "Exercises"),
                         ("notes.md", "Notes and further reading")]:
        t = glue(book, refs, vol.id, ch.id, fname)
        if not t:
            continue
        if fname == "exercises.md":
            t = number_exercises(t, ch.num)
        out += ["```{=latex}", r"\hbgroup{%s}" % title, "```", "", f"## {title} {{#{cid}-{fname[:-3]} .html-only}}", "", t]
    return "\n".join(out) + "\n"


def glue_inline(book: Book, refs: Refs, text: str) -> str:
    def repl(m):
        slug = m.group(1)
        num = book.ref(slug)
        return "](" + refs.target(slug) + ")" + (f" [{num}]{{.ref}}" if num else "")
    return re.sub(r"\]\(/([a-z0-9][a-z0-9-]*)/\)", repl, text)


def roadmap(book: Book, ch: Chapter, refs: Refs) -> str:
    rows = ["| | Entry | Kind | Level |", "|---|---|---|---|"]
    for e in ch.entries:
        rows.append(f"| {book.ref(e.slug)} | [{md_plain(e.name)}](#{e.slug}) | "
                    f"{KIND_LABEL.get(e.kind, e.kind)} | {LEVEL_LABEL.get(e.level, e.level)} |")
    return ('::: {.roadmap latex-env="hbroadmap"}\n' + "\n".join(rows) +
            f"\n\n: The entries of chapter {ch.num}.\n:::\n")


def number_exercises(md: str, chnum: str) -> str:
    """Give each exercise the number <chapter>.<k>: an item `7.` at the start of a line becomes **4.1.7**."""
    out = []
    for line in md.split("\n"):
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            k = m.group(1)
            line = (f'::: {{.exercise #ex-{chnum.replace(".", "-")}-{k} latex-env="hbexercise"}}\n'
                    f'**{chnum}.{k}** {m.group(2)}')
            out.append("§§OPEN")
            out.append(line)
        else:
            out.append(line)
    # close each exercise div before the next one or at a heading or the end
    res, open_ = [], False
    for line in out:
        if line == "§§OPEN":
            if open_:
                res.append(":::\n")
            open_ = True
            continue
        if open_ and re.match(r"^#{1,6} ", line):
            res.append(":::\n")
            open_ = False
        res.append(line)
    if open_:
        res.append(":::")
    return "\n".join(res)


def hints_md(book: Book, vol: Volume, refs: Refs) -> str:
    out = []
    for ch in vol.chapters:
        t = glue(book, refs, vol.id, ch.id, "hints.md")
        if not t:
            continue
        t = re.sub(r"^(\d+)\.\s+", lambda m: f"**[{ch.num}.{m.group(1)}](#ex-{ch.num.replace('.', '-')}-{m.group(1)})** ",
                   t, flags=re.M)
        out.append(f"#### Chapter {ch.num}: {md_plain(ch.name)} {{.unnumbered}}\n\n"
                   f'::: {{.hints latex-env="hbhints"}}\n{t}\n:::')
    return "\n\n".join(out)
