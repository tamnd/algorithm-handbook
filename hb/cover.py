"""The covers (spec handbook 06.3): one hue per volume, a quiet grid of the volume's chapters."""

from __future__ import annotations

import textwrap

from .fonts import _find, ensure_fonts
from .volume import volume_hue


def _rgb(hexs: str):
    return tuple(int(hexs[i:i + 2], 16) for i in (0, 2, 4))


def cover_png(vol, edition: str, path: str, w: int = 1600, h: int = 2286):
    from PIL import Image, ImageDraw, ImageFont
    ensure_fonts()
    hue = _rgb(volume_hue(vol.number))
    img = Image.new("RGB", (w, h), hue)
    d = ImageDraw.Draw(img)
    sans_b = lambda s: ImageFont.truetype(_find("LibertinusSans-Bold.otf"), s)
    sans = lambda s: ImageFont.truetype(_find("LibertinusSans-Regular.otf"), s)
    serif_i = lambda s: ImageFont.truetype(_find("LibertinusSerif-Italic.otf"), s)
    white = (255, 255, 255)
    soft = tuple(int(c + (255 - c) * 0.55) for c in hue)
    m = 130
    # a grid of squares, one per chapter, filled by how much of it is written
    cols, size, gap = 6, 120, 26
    x0, y0 = m, h - m - 520
    for i, ch in enumerate(vol.chapters):
        r, c = divmod(i, cols)
        x, y = x0 + c * (size + gap), y0 + r * (size + gap)
        if y + size > h - m - 120:
            break
        total = len(ch.entries) + len(ch.stubs)
        frac = len(ch.entries) / total if total else 0
        d.rectangle([x, y, x + size, y + size], outline=soft, width=3)
        if frac:
            d.rectangle([x, y + size - int(size * frac), x + size, y + size], fill=soft)
    d.rectangle([m, m, w - m, m + 14], fill=white)
    d.text((m, m + 60), "THE HANDBOOK OF ALGORITHMS", font=sans(46), fill=white, spacing=8)
    d.text((m, 520), f"Volume {vol.number}", font=sans_b(84), fill=soft)
    y = 630
    for line in textwrap.wrap(vol.name, 14):
        d.text((m, y), line, font=sans_b(170), fill=white)
        y += 190
    y += 30
    for line in textwrap.wrap(vol.summary.strip(), 40):
        d.text((m, y), line, font=serif_i(58), fill=soft)
        y += 72
    d.text((m, h - m - 40), f"Edition {edition}  ·  algorithm.tamnd.com", font=sans(42), fill=soft)
    img.save(path)
    return path
