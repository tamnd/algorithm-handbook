"""Turn the cost strings of the front matter, such as 'O(n log^2 n)' or 'Θ(√n · m)', into TeX math.

The corpus writes costs in a plain ASCII-and-Unicode form. Printed as text, 'n^3' shows its caret; set as
math, it is n³. A string that does not look like a formula (a word of four letters or more that is not a
known function, an unbalanced bracket, a character outside the table) is left as text.
"""
from __future__ import annotations

import re

GREEK = {
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta", "ε": r"\varepsilon", "ζ": r"\zeta",
    "η": r"\eta", "θ": r"\theta", "κ": r"\kappa", "λ": r"\lambda", "μ": r"\mu", "ν": r"\nu", "ξ": r"\xi",
    "π": r"\pi", "ρ": r"\rho", "σ": r"\sigma", "τ": r"\tau", "φ": r"\varphi", "ϕ": r"\phi", "χ": r"\chi",
    "ψ": r"\psi", "ω": r"\omega", "Γ": r"\Gamma", "Δ": r"\Delta", "Θ": r"\Theta", "Λ": r"\Lambda",
    "Π": r"\Pi", "Σ": r"\Sigma", "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega", "ℓ": r"\ell",
}
SYMBOLS = {
    "·": r"\cdot ", "×": r"\times ", "−": "-", "–": "-", "⌈": r"\lceil ", "⌉": r"\rceil ", "⌊": r"\lfloor ",
    "⌋": r"\rfloor ", "≤": r"\le ", "≥": r"\ge ", "≈": r"\approx ", "∞": r"\infty ", "…": r"\ldots ",
    "∈": r"\in ", "|": "|", "!": "!", "+": "+", "-": "-", "/": "/", "=": "=", "<": "<", ">": ">", ",": ",\\,",
    ".": ".", "'": "'", "*": r"\cdot ",
}
SUPERS = {"²": "2", "³": "3", "⁴": "4", "ⁿ": "n", "¹": "1", "⁰": "0", "ᵏ": "k"}
SUBS = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "ᵢ": "i", "ₖ": "k"}
FUNCS = {"log": r"\log", "lg": r"\lg", "ln": r"\ln", "exp": r"\exp", "min": r"\min", "max": r"\max",
         "sqrt": r"\sqrt", "poly": r"\operatorname{poly}", "polylog": r"\operatorname{polylog}",
         "loglog": r"\log\log", "gcd": r"\gcd", "det": r"\det", "sin": r"\sin", "cos": r"\cos"}
TOKEN = re.compile(r"\s+|[A-Za-z]+|\d+(?:\.\d+)?|.", re.S)


def _group(toks: list[str], i: int) -> tuple[list[str], int]:
    """The tokens of one operand starting at toks[i]: a bracketed group (brackets dropped) or one token."""
    while i < len(toks) and toks[i].isspace():
        i += 1
    if i >= len(toks):
        raise ValueError
    if toks[i] in "({":
        close = ")" if toks[i] == "(" else "}"
        depth, j = 0, i
        while j < len(toks):
            if toks[j] in "({":
                depth += 1
            elif toks[j] in ")}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if j >= len(toks) or toks[j] != close:
            raise ValueError
        return toks[i + 1:j], j + 1
    if toks[i] == "-" and i + 1 < len(toks):  # n^-1
        g, k = _group(toks, i + 1)
        return ["-"] + g, k
    return [toks[i]], i + 1


def _conv(toks: list[str]) -> str:
    out: list[str] = []
    i = 0
    while i < len(toks):
        t = toks[i]
        if t.isspace():
            out.append(" ")
            i += 1
        elif t in "^_":
            g, i = _group(toks, i + 1)
            out.append(t + "{" + _conv(g) + "}")
        elif t in SUPERS:
            out.append("^{" + SUPERS[t] + "}")
            i += 1
        elif t in SUBS:
            out.append("_{" + SUBS[t] + "}")
            i += 1
        elif t == "√" or t == "sqrt":
            g, i = _group(toks, i + 1)
            out.append(r"\sqrt{" + _conv(g) + "}")
        elif t[0].isalpha() and t.isascii():
            if t in FUNCS:
                out.append(FUNCS[t] + " ")
                if i + 1 < len(toks) and toks[i + 1] == "*":  # log* n
                    out.append("^{*}")
                    i += 1
            elif len(t) == 1:
                out.append(t)
            elif len(t) <= 3:
                out.append(r"\mathit{" + t + "}")
            else:
                raise ValueError(t)
            i += 1
        elif t[0].isdigit():
            out.append(t)
            i += 1
        elif t in GREEK:
            out.append(GREEK[t] + " ")
            i += 1
        elif t in SYMBOLS:
            out.append(SYMBOLS[t])
            i += 1
        elif t in "()[]":
            out.append(t)
            i += 1
        elif t in "{}":
            raise ValueError(t)
        else:
            raise ValueError(t)
    return "".join(out)


def tex(s: str) -> str | None:
    """The TeX math of a cost string, or None when it is not a formula."""
    s = s.strip()
    if not s or "$" in s or "\\" in s:
        return None
    toks = TOKEN.findall(s)
    depth = 0
    for t in toks:
        depth += t in "(["
        depth -= t in ")]"
        if depth < 0:
            return None
    if depth:
        return None
    try:
        m = _conv(toks)
    except (ValueError, IndexError):
        return None
    return re.sub(r" +", " ", m).strip()


def cost_md(s: str, plain) -> str:
    """Markdown for a cost: inline math when the string is a formula, else plain(s)."""
    s = str(s)
    m = tex(s)
    if m:
        return f"${m}$"
    words = s.split()
    k = len(words)
    while k > 1 and words[k - 1].isalpha() and words[k - 1].islower() and len(words[k - 1]) >= 4:
        k -= 1
    if k < len(words):
        m = tex(" ".join(words[:k]))
        if m:
            return f"${m}$ " + plain(" ".join(words[k:]))
    return plain(s)
