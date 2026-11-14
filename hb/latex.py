"""The LaTeX and PDF of a volume (spec handbook 04.5).

volume Markdown → pandoc (filters/hb.lua) → body.tex → fallback fonts → main.tex → tectonic → PDF.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import time

from .book import Book, Volume
from .fonts import Fallback
from .prep import tex
from .volume import volume_hue

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pandoc_latex(md: str) -> str:
    cmd = ["pandoc", "-f", "markdown-auto_identifiers", "-t", "latex",
           "--lua-filter", os.path.join(ROOT, "filters", "hb.lua"),
           "--top-level-division=chapter", "--wrap=preserve", "--syntax-highlighting=pygments"]
    r = subprocess.run(cmd, input=md, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError("pandoc failed:\n" + r.stderr[-4000:])
    if r.stderr.strip():
        print(r.stderr.strip()[:2000])
    return r.stdout


def main_tex(book: Book, vol: Volume, edition: str, date: str) -> str:
    commit = book.corpus.commit()[:8]
    hue = volume_hue(vol.number)
    title = tex(vol.name)
    summary = tex(vol.summary.strip())
    return rf"""\documentclass[10pt,twoside,openany]{{book}}
\RequirePackage{{xcolor}}
\definecolor{{hbaccent}}{{HTML}}{{{hue}}}
\usepackage{{handbook}}
\renewcommand\hbvolnum{{{vol.number}}}
\renewcommand\hbvolname{{{title}}}
\hypersetup{{pdftitle={{The Handbook of Algorithms, Volume {vol.number}: {title}}},pdfauthor={{The Algorithm Project}},
  pdfsubject={{{title}}},pdfkeywords={{algorithms, {title}}}}}
\begin{{document}}
\frontmatter
\hbtitlepage{{{vol.number}}}{{{title}}}{{{summary}}}{{{edition}}}{{{date}}}
\hbcopyright{{{edition}}}{{{date}}}{{{commit}}}{{{vol.number}}}{{{title}}}
\tableofcontents
\mainmatter
\input{{body.tex}}
\end{{document}}
"""



_BARE_SCRIPT = re.compile(r"(?<!\\)([_^])(\\(?:math[a-z]+|operatorname\*?|text[a-z]*|boldsymbol)\{[^{}]*\})")


def brace_scripts(tex: str) -> str:
    """Repair math that KaTeX accepts and XeTeX with unicode-math does not: `x_\\mathcal{R}` becomes
    `x_{\\mathcal{R}}`, and `\\not\\leadsto` becomes `\\centernot\\leadsto`."""
    tex = _BARE_SCRIPT.sub(r"\1{\2}", tex)
    # amssymb's \triangle is a macro, not a math character: `Q_\triangle` gives "Missing { inserted"
    tex = re.sub(r"(?<!\\)([_^])(\\triangle)(?![a-zA-Z])", r"\1{\2}", tex)
    # a prime, then a subscript, then a superscript: KaTeX allows it, TeX sees a double superscript
    tex = _PRIME_SUB_SUP.sub(_prime_sub_sup, tex)
    # unicode-math's \not looks for a negated character; ↝ has none and XeTeX dies ("bad native font flag")
    return tex.replace(r"\not\leadsto", r"\centernot\leadsto")


_PRIME_SUB_SUP = re.compile(r"(\\[a-zA-Z]+|[A-Za-z0-9)\]}])('+)(_(?:\{[^{}]*\}|\\?[A-Za-z0-9]+))(?=\^)")
_BIG_OPS = {r"\sum", r"\prod", r"\coprod", r"\bigcup", r"\bigcap", r"\bigoplus", r"\int", r"\oint"}


def _prime_sub_sup(m: re.Match) -> str:
    base, primes, sub = m.groups()
    if base in _BIG_OPS:   # Σ'' with limits: amsmath's \sideset
        return r"\sideset{}{" + primes + "}" + base + sub
    return base + primes + sub + "{}"


def _math_hats(m: re.Match) -> str:
    s = m.group(0)
    return re.sub(r"([A-Za-z])\u0302", r"\\hat{\1}", s) if "\u0302" in s else s


_AUX = ("main.aux", "main.toc", "main.out")


def _aux_state(outdir: str) -> tuple:
    state = []
    for f in _AUX:
        p = os.path.join(outdir, f)
        state.append(open(p, "rb").read() if os.path.exists(p) else None)
    return tuple(state)


def run_tex(outdir: str, max_passes: int = 5):
    """Run XeTeX one pass per tectonic process until the aux, toc and bookmark files are stable.

    Within one process tectonic keeps XeTeX's cache of glyph boxes from pass to pass, keyed by font number.
    Once the contents fill in, later passes load the fonts in another order, and a small font can get the
    boxes of a large one: a line with a 7 pt cross-reference got the height of a 54 pt chapter number.
    A fresh process for every pass has no such cache."""
    for f in _AUX:
        p = os.path.join(outdir, f)
        if os.path.exists(p):
            os.remove(p)
    passes = 0
    while True:
        before = _aux_state(outdir)
        r = subprocess.run(["tectonic", "-X", "compile", "--keep-logs", "--keep-intermediates", "-r", "0",
                            "main.tex"], cwd=outdir, capture_output=True, text=True)
        passes += 1
        if r.returncode or _aux_state(outdir) == before or passes >= max_passes:
            break
    for f in os.listdir(outdir):   # the intermediates are not part of the build
        if f.startswith("main.") and f not in ("main.tex", "main.pdf", "main.log", "main.epub"):
            os.remove(os.path.join(outdir, f))
    return r, passes


def build(book: Book, vol: Volume, md: str, outdir: str, edition: str, date: str, pdf: bool = True) -> dict:
    os.makedirs(outdir, exist_ok=True)
    t0 = time.time()
    open(os.path.join(outdir, "body.md"), "w").write(md)
    body = pandoc_latex(md)
    t1 = time.time()
    fb = Fallback()
    body = fb.apply(body)
    body = brace_scripts(body)
    # ⧺ (concatenation) is absent from Libertinus Math; in mathematics it is drawn as two overlapping plus signs
    body = re.sub(r"(?<!\}\{)⧺", lambda m: r"\mathbin{+\mkern-10mu+}", body)
    # the outer joins ⟕ ⟖ ⟗ are absent from Libertinus Math; in mathematics they come from STIX Two Math
    body = re.sub(r"(?<!\}\{)([⟕⟖⟗])", lambda m: r"\mathbin{\text{\hbfbC " + m.group(1) + "}}", body)
    # so is the diamond operator ⋄ (\diamond, U+22C4); as a bare subscript (the diamond norm, `\|X\|_\diamond`)
    # the replacement needs braces, or TeX stops with "Missing { inserted"
    body = re.sub(r"(?<!\\)([_^])\s*\\diamond(?![a-zA-Z])", lambda m: m.group(1) + r"{\text{\hbfbC ⋄}}", body)
    body = re.sub(r"\\diamond(?![a-zA-Z])", lambda m: r"\mathbin{\text{\hbfbC ⋄}}", body)
    # a combining circumflex (U+0302) after a letter in mathematics, as in N̂, has no glyph there: it is \hat
    body = re.sub(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", _math_hats, body, flags=re.S)
    open(os.path.join(outdir, "body.tex"), "w").write(body)
    open(os.path.join(outdir, "main.tex"), "w").write(main_tex(book, vol, edition, date))
    shutil.copy(os.path.join(ROOT, "tex", "handbook.sty"), outdir)
    info = {"pandoc_s": round(t1 - t0, 1), "missing_glyphs": dict(sorted(fb.missing.items(), key=lambda x: -x[1]))}
    if pdf:
        t2 = time.time()
        r, passes = run_tex(outdir)
        info["tectonic_s"] = round(time.time() - t2, 1)
        info["passes"] = passes
        info["ok"] = r.returncode == 0
        if r.returncode:
            info["error"] = (r.stdout + r.stderr)[-6000:]
        pdfp = os.path.join(outdir, "main.pdf")
        if os.path.exists(pdfp):
            info["pdf"] = pdfp
            try:
                out = subprocess.run(["pdfinfo", pdfp], capture_output=True, text=True).stdout
                info["pages"] = int(next(l.split()[-1] for l in out.splitlines() if l.startswith("Pages")))
            except Exception:
                pass
    return info
