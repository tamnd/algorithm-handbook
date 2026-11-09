"""Repairs of damaged text in the content, applied when the corpus is loaded.

Each patch names a file of tamnd/algorithm (relative to nodes/), the exact damaged text and its repair. A patch
applies only if the damaged text is still there, so a fixed source makes its patch a no-op. Every patch is
listed in the project notes (spec handbook 11) to be reported upstream; remove it once the source is fixed.
"""
from __future__ import annotations

_NOTE = ("^[The source of this paragraph lost its variables (each `$i`, `$d`, … was dropped, as if expanded by a "
         "shell). The symbols were restored for this edition by the handbook's editor (AI-drafted) from the "
         "surrounding proof; check them against the site.]")

PATCHES: dict[str, list[tuple[str, str]]] = {
    # every $x was expanded away; restored from the proof's own definitions (W, w, d, e, t, k)
    "numerical/root-finding/brent-method/proofs/correctness.md": [(
        "We claim that after $ passes of a run, at the next test of L6, $|d| \\le w 2^{-\\lceil i/2 \\rceil}$ and "
        "$|e| \\le w 2^{-\\lfloor i/2 \\rfloor}$. This holds for  = 0$. An accepted step has |p| < |eq|$, so the new "
        "$ is less than $|e|/2 \\le w 2^{-\\lfloor i/2 \\rfloor - 1} = w 2^{-\\lceil (i+1)/2 \\rceil}$, and the new $ "
        "is the old $, at most  2^{-\\lceil i/2 \\rceil} = w 2^{-\\lfloor (i+1)/2 \\rfloor}$. A reset at L3 sets  = e "
        "= b - a$, the move just made. If that move was a step $ with $|d| > t$, the reset sets both to the stored "
        "$|d|$ and the claim still holds. If it was a minimum step of size $, the reset makes the old $ the "
        "contrapoint, so  = t \\le 2t$, and L5 returns at once. This proves the claim. An interpolation pass needs "
        "$|e| \\ge t \\ge \\delta/2$ at L6, so  2^{-\\lfloor i/2 \\rfloor} \\ge \\delta/2$, which gives "
        "$\\lfloor i/2 \\rfloor \\le k + 1$ and  \\le 2k + 3$. So a run has at most k + 4$ passes;",
        "We claim that after $i$ passes of a run, at the next test of L6, $|d| \\le w 2^{-\\lceil i/2 \\rceil}$ and "
        "$|e| \\le w 2^{-\\lfloor i/2 \\rfloor}$. This holds for $i = 0$. An accepted step has $2|p| < |eq|$, so the "
        "new $|d|$ is less than $|e|/2 \\le w 2^{-\\lfloor i/2 \\rfloor - 1} = w 2^{-\\lceil (i+1)/2 \\rceil}$, and the "
        "new $|e|$ is the old $|d|$, at most $w 2^{-\\lceil i/2 \\rceil} = w 2^{-\\lfloor (i+1)/2 \\rfloor}$. A reset "
        "at L3 sets $d = e = b - a$, the move just made. If that move was a step $d$ with $|d| > t$, the reset sets "
        "both to the stored $|d|$ and the claim still holds. If it was a minimum step of size $t$, the reset makes "
        "the old $b$ the contrapoint, so $W = t \\le 2t$, and L5 returns at once. This proves the claim. An "
        "interpolation pass needs $|e| \\ge t \\ge \\delta/2$ at L6, so $w 2^{-\\lfloor i/2 \\rfloor} \\ge \\delta/2$, "
        "which gives $\\lfloor i/2 \\rfloor \\le k + 1$ and $i \\le 2k + 3$. So a run has at most $2k + 4$ passes;",
    ), (
        "and both are bisections.",
        "and both are bisections." + _NOTE,
    )],
    # a closing $ is missing
    "foundations/asymptotic-analysis/geometric-series/node.md": [(
        '"the sum is $O(\\text{largest term})" is valid',
        '"the sum is $O(\\text{largest term})$" is valid',
    )],
}


def apply(rel: str, text: str) -> str:
    for old, new in PATCHES.get(rel, ()):
        if old in text:
            text = text.replace(old, new, 1)
    return text
