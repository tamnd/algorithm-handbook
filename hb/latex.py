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
    open(os.path.join(outdir, "body.tex"), "w").write(body)
    open(os.path.join(outdir, "main.tex"), "w").write(main_tex(book, vol, edition, date))
    shutil.copy(os.path.join(ROOT, "tex", "handbook.sty"), outdir)
    info = {"pandoc_s": round(t1 - t0, 1), "missing_glyphs": dict(sorted(fb.missing.items(), key=lambda x: -x[1]))}
    if pdf:
        t2 = time.time()
        r = subprocess.run(["tectonic", "-X", "compile", "--keep-logs", "main.tex"], cwd=outdir,
                           capture_output=True, text=True)
        info["tectonic_s"] = round(time.time() - t2, 1)
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
