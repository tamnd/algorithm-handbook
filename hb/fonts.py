"""The fallback fonts (spec handbook 05.2).

Libertinus Serif lacks some characters of the corpus (⌊ ⌋ ∎ box drawing, CJK, …). The builder wraps each
such character, outside mathematics, in \\hbfb{X}{c}, where X names the first font of the chain that has it.
Mathematics needs no help: unicode-math takes the glyph from Libertinus Math.
"""

from __future__ import annotations

import functools
import glob
import os
import re
import subprocess
import tempfile

# the fonts the text uses, and the chain of fallbacks with their letters in handbook.sty
TEXT_FONTS = ["LibertinusSerif-Regular.otf", "LibertinusSerif-Italic.otf", "LibertinusSerif-Bold.otf",
              "LibertinusSans-Regular.otf", "LibertinusSans-Bold.otf", "DejaVuSansMono.ttf"]
CHAIN = [("F", "LibertinusSerif-Regular.otf"), ("A", "LibertinusMath-Regular.otf"), ("B", "DejaVuSansMono.ttf"),
         ("C", "STIXTwoMath-Regular.otf"), ("D", "FreeSerif.otf"), ("E", "FandolSong-Regular.otf")]


def _cache_dirs():
    pats = ["~/Library/Caches/TectonicProject.Tectonic/bundles/data/*/", "~/.cache/Tectonic/bundles/data/*/",
            "~/.cache/tectonic/bundles/data/*/"]
    out = []
    for p in pats:
        out += glob.glob(os.path.expanduser(p))
    return out


def _find(name: str) -> str | None:
    for d in _cache_dirs():
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    return None


def ensure_fonts():
    """Make tectonic fetch every font of the chain into its cache, so that fontTools can read them."""
    names = sorted(set(TEXT_FONTS) | {f for _, f in CHAIN})
    if all(_find(n) for n in names):
        return
    body = "".join(r"\newfontfamily\f%s{%s}" % ("abcdefghijklmnop"[i], n) for i, n in enumerate(names))
    doc = r"\documentclass{article}\usepackage{fontspec}" + body + r"\begin{document}x\end{document}"
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "f.tex"), "w").write(doc)
        subprocess.run(["tectonic", "f.tex"], cwd=d, capture_output=True)


@functools.cache
def cmap(name: str) -> frozenset:
    from fontTools.ttLib import TTFont
    p = _find(name)
    if not p:
        return frozenset()
    return frozenset(TTFont(p, fontNumber=0).getBestCmap())


class Fallback:
    def __init__(self):
        ensure_fonts()
        self.common = set.intersection(*(set(cmap(f)) for f in TEXT_FONTS))
        self.memo: dict[str, str | None] = {}
        self.missing: dict[str, int] = {}

    def letter(self, c: str) -> str | None:
        if c in self.memo:
            return self.memo[c]
        o = ord(c)
        res = None
        if o >= 128 and o not in self.common and not (0x300 <= o <= 0x36F):
            for letter, f in CHAIN:
                if o in cmap(f):
                    res = letter
                    break
            else:
                self.missing[c] = self.missing.get(c, 0) + 1
        self.memo[c] = res
        return res

    # A scanner over pandoc's LaTeX: skip \( … \), \[ … \], math environments, \url{…} and \href{…}.
    # A delimiter preceded by a backslash is not one: in `\\[2ex]` the row break is followed by an option.
    _TOKEN = re.compile(r"(?<!\\)\\\(|(?<!\\)\\\)|(?<!\\)\\\[|(?<!\\)\\\]|\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath|math)\}"
                        r"|\\end\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath|math)\}|\\(?:url|href|label|hyperref\[)")

    def apply(self, s: str) -> str:
        out, i, n = [], 0, len(s)
        math = 0
        while i < n:
            m = self._TOKEN.search(s, i)
            j = m.start() if m else n
            seg = s[i:j]
            out.append(seg if math else self._wrap(seg))
            if not m:
                break
            tok = m.group(0)
            if tok in ("\\(", "\\[") or tok.startswith("\\begin"):
                math += 1
                out.append(tok); i = m.end()
            elif tok in ("\\)", "\\]") or tok.startswith("\\end"):
                math = max(0, math - 1)
                out.append(tok); i = m.end()
            else:  # \url{…}, \href{…}, \label{…}, \hyperref[…]: copy the argument as it is
                k = m.end()
                close = "]" if tok.endswith("[") else "}"
                depth, k2 = 0, k
                if close == "}" and k < n and s[k] == "{":
                    k2 = k
                    while k2 < n:
                        if s[k2] == "{": depth += 1
                        elif s[k2] == "}":
                            depth -= 1
                            if depth == 0: break
                        k2 += 1
                    out.append(s[m.start():k2 + 1]); i = k2 + 1
                elif close == "]":
                    k2 = s.find("]", k)
                    out.append(s[m.start():k2 + 1]); i = k2 + 1
                else:
                    out.append(tok); i = m.end()
        return "".join(out)

    def _wrap(self, seg: str) -> str:
        if seg.isascii():
            return seg
        buf = []
        for c in seg:
            L = self.letter(c) if ord(c) >= 128 else None
            buf.append(f"\\hbfb{{{L}}}{{{c}}}" if L else c)
        return "".join(buf)
