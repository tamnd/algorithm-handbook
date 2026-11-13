"""Repairs of damaged text in the content, applied when the corpus is loaded.

Each patch names a file of tamnd/algorithm (relative to nodes/), the exact damaged text and its repair. A patch
applies only if the damaged text is still there, so a fixed source makes its patch a no-op. Every patch is
listed in the project notes (spec handbook 11) to be reported upstream; remove it once the source is fixed.
"""
from __future__ import annotations

# The eleven patches of earlier editions were fixed upstream (tamnd/algorithm #467) and are in the site from
# release v0.26.0, so they were removed. Add a patch here only for damage the site still has.
PATCHES: dict[str, list[tuple[str, str]]] = {}


def apply(rel: str, text: str) -> str:
    for old, new in PATCHES.get(rel, ()):
        if old in text:
            text = text.replace(old, new, 1)
    return text
