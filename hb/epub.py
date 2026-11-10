"""The EPUB of a volume (spec handbook 04.6).

The volume Markdown → pandoc → EPUB 3 with MathML. Raw LaTeX blocks fall away; the `html-only`
headings carry the structure: # chapter, ## group, ### entry. Each chapter is a file of its own.
"""

from __future__ import annotations

import os
import re
import subprocess
import time
import zipfile

from .book import Book, Volume
from .cover import cover_png
from .volume import volume_hue


def volume_css(vol: Volume, outdir: str) -> str:
    """tex/epub.css with the blue of the template replaced by the hue of the volume (05.6)."""
    hue = volume_hue(vol.number)
    rgb = [int(hue[i:i + 2], 16) for i in (0, 2, 4)]
    dark = "".join(f"{int(c * 0.75):02X}" for c in rgb)
    tint = "".join(f"{int(c + (255 - c) * 0.94):02X}" for c in rgb)
    soft = "".join(f"{int(c + (255 - c) * 0.6):02X}" for c in rgb)
    css = open(os.path.join(ROOT, "tex", "epub.css")).read()
    css = (css.replace("#2B59C3", f"#{hue}").replace("#20448f", f"#{dark}")
              .replace("#F1F4FB", f"#{tint}").replace("#A9B9E3", f"#{soft}"))
    path = os.path.join(outdir, "epub.css")
    open(path, "w").write(css)
    return path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def metadata(book: Book, vol: Volume, edition: str, date: str) -> str:
    commit = book.corpus.commit()[:8]
    q = lambda s: s.replace('"', '\\"')
    return f"""---
title:
- type: main
  text: "{q(vol.name)}"
- type: subtitle
  text: "The Handbook of Algorithms, Volume {vol.number}"
creator:
- role: author
  text: "The Algorithm Project"
publisher: "algorithm.tamnd.com"
date: "{date}"
lang: en
identifier:
- scheme: URI
  text: "https://algorithm.tamnd.com/handbook/{vol.id}/{edition}"
rights: "Text CC BY-SA 4.0; code MIT. Edition {edition}, content commit {commit}."
description: "{q(vol.summary.strip())}"
subject: "Algorithms"
...
"""


def copyright_md(book: Book, vol: Volume, edition: str, date: str) -> str:
    commit = book.corpus.commit()[:8]
    return f"""# About this edition {{.unnumbered .unlisted}}

**The Handbook of Algorithms, Volume {vol.number}: {vol.name}.** Edition {edition}, {date}.

Built from the content of the Algorithm project at commit `{commit}` (<https://github.com/tamnd/algorithm>).
The online edition, with every entry, the code in several languages and the interactive figures, is at
<https://algorithm.tamnd.com>.

The text of the entries and proofs is licensed under Creative Commons Attribution-ShareAlike 4.0
International (CC BY-SA 4.0). The code is licensed under the MIT licence. The learner pages of this book
(introductions, openings, summaries, exercises, hints and notes) are licensed under CC BY-SA 4.0.

Much of the text was drafted by AI agents working from the sources cited in each entry, and then checked by
tests and reviews in the project. Errors remain. Please report them at
<https://github.com/tamnd/algorithm/issues>.
"""


# TeX that pandoc's MathML writer (texmath) cannot read and prints as source. XeTeX reads all of it; the EPUB
# gets equivalent forms: `{n \atop k}` (Stirling and Eulerian numbers), `\xRightarrow{a}`, `\textsc{update}` (a
# procedure name; MathML has no small capitals, so capitals), `{\rm best}`, `\cfrac`, `\tbinom` and `\bmod`.
_MATH = re.compile(r"\$\$.*?\$\$|(?<![\\$])\$[^$\n]+\$", re.S)
_MATHML = [
    (re.compile(r"(?<!\\)\{\s*([^{}$]*?)\s*\\atop\s*([^{}$]*?)\s*(?<!\\)\}"),
     lambda m: "{\\begin{matrix}" + m[1] + "\\\\" + m[2] + "\\end{matrix}}"),
    (re.compile(r"(\\left(?:\\[A-Za-z]+|\\.|.))\s*([^{}$]*?)\s*\\atop\s*([^{}$]*?)\s*(\\right(?:\\[A-Za-z]+|\\.|.))"),
     lambda m: m[1] + " \\begin{matrix}" + m[2] + "\\\\" + m[3] + "\\end{matrix} " + m[4]),
    (re.compile(r"\\texttt\{([^{}$]*)\}"), lambda m: "\\texttt{" + m[1].replace("\\dots", "...") + "}"),
    (re.compile(r"\\dbinom(?![A-Za-z])"), lambda m: "\\binom"),
    (re.compile(r"\\xRightarrow\{([^{}$]*)\}"), lambda m: "\\overset{" + m[1] + "}{\\Rightarrow}"),
    (re.compile(r"\\textsc\{([^{}$]*)\}"), lambda m: "\\text{" + m[1].upper() + "}"),
    (re.compile(r"\{\\rm\s+([^{}$]*)\}"), lambda m: "\\mathrm{" + m[1] + "}"),
    (re.compile(r"\\cfrac(?![A-Za-z])"), lambda m: "\\dfrac"),
    (re.compile(r"\\tbinom(?![A-Za-z])"), lambda m: "\\binom"),
    (re.compile(r"\\bmod(?![A-Za-z])"), lambda m: "\\mathbin{\\mathrm{mod}}"),
]


def mathml_safe(md: str) -> str:
    def span(m: re.Match) -> str:
        t = m.group(0)
        for rx, f in _MATHML:
            t = rx.sub(f, t)
        return t
    return _MATH.sub(span, md)


_HEADING = re.compile(r"^(#{1,6} .*?)(?:\s*(?<!\])\{([^{}]*)\})?\s*$")
_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def heading_ids(md: str) -> str:
    """Give every heading without an identifier one of its own (`h-1`, `h-2`, …). Pandoc's EPUB writer would
    otherwise make one from the text, and the section "Termination" of one entry would take the identifier of
    the entry `termination`, and its links."""
    out, fence, n = [], None, 0
    for ln in md.split("\n"):
        f = _FENCE.match(ln)
        if f:
            if fence is None:
                fence = f.group(1)[0]
            elif f.group(1)[0] == fence:
                fence = None
        elif fence is None and ln.startswith("#") and (m := _HEADING.match(ln)):
            attrs = m.group(2) or ""
            if not re.search(r"(^|\s)#", attrs):
                n += 1
                ln = f"{m.group(1)} {{#h-{n}{' ' + attrs if attrs else ''}}}"
        out.append(ln)
    return "\n".join(out)


def build(book: Book, vol: Volume, md: str, outdir: str, edition: str, date: str) -> dict:
    os.makedirs(outdir, exist_ok=True)
    t = time.time()
    src = os.path.join(outdir, "epub.md")
    open(src, "w").write(metadata(book, vol, edition, date) + "\n" + copyright_md(book, vol, edition, date)
                         + "\n\n" + heading_ids(mathml_safe(md)))
    cover = os.path.join(outdir, "cover.png")
    cover_png(vol, edition, cover)
    out = os.path.join(outdir, "main.epub")
    cmd = ["pandoc", src, "-f", "markdown-auto_identifiers", "-t", "epub3", "-o", out,
           "--lua-filter", os.path.join(ROOT, "filters", "hb.lua"),
           "--math-method=mathml", "--toc", "--toc-depth=3", "--split-level=1",
           "--css", volume_css(vol, outdir),
           "--epub-cover-image", cover, "--resource-path", outdir,
           "--syntax-highlighting=pygments"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    info = {"epub_s": round(time.time() - t, 1), "epub_ok": r.returncode == 0}
    if r.returncode:
        info["error"] = r.stderr[-4000:]
    elif r.stderr.strip():
        info["epub_warnings"] = r.stderr.count("[WARNING]")
        open(os.path.join(outdir, "epub.log"), "w").write(r.stderr)
    if os.path.exists(out):
        space_functions(out)
        info["epub"] = out
        info["epub_mb"] = round(os.path.getsize(out) / 1e6, 1)
    return info


# `log n` in MathML is <mi>log</mi><mo>&#8289;</mo>; WebKit and Blink, which most reading systems use, put no
# space around it, so `n log n` prints as `nlogn`. A thin space on both sides, as TeX gives.
_FN = re.compile(r'(<mrow>)?(<mi mathvariant="normal">[A-Za-z]{2,}\*?</mi><mo>&#8289;</mo>)(</mrow>)?')
_SP = '<mspace width="0.1667em"></mspace>'


def space_functions(path: str) -> None:
    tmp = path + ".tmp"
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w") as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.endswith(".xhtml"):
                data = _FN.sub(lambda m: (m.group(1) or "") + _SP + m.group(2) + _SP + (m.group(3) or ""),
                               data.decode()).encode()
            # mimetype first and stored, as EPUB requires
            zout.writestr(item, data, compress_type=zipfile.ZIP_STORED if item.filename == "mimetype"
                          else zipfile.ZIP_DEFLATED)
    os.replace(tmp, path)
