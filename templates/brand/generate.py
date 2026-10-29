#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generates the {{name}} brand kit: master SVGs, PNG exports, favicon.ico and the website's head icons.

PROVISIONAL – the placeholder design from falkoss/starterpack until {{name}} has its own: a chamfered frame with a block
cursor, the name set in the system's monospace font, one accent. Replace the colours and the drawing functions below
(mark, small_mark, wordmark_body, social); the export (brandkit.py) stays. Convert the wordmark to outlines once it
is final (kernoid's brand/generate.py does that with fontTools), so it needs no font where it is shown.

Needs rsvg-convert (Homebrew: librsvg). Run from anywhere:
    python3 generate.py
Edit this file, not the exports.
"""
import os

from brandkit import export, svg

HERE = os.path.dirname(os.path.abspath(__file__))
NAME = "{{name}}"
TAGLINE = "{{tagline}}"

NIGHT = "{{night}}"         # near-black – backgrounds
PAPER = "{{paper}}"         # text and strokes on dark
INK = "{{ink}}"             # text and strokes on light
ACCENT = "{{accent}}"       # the one accent, on dark
ACCENT_DARK = "{{accent_dark}}"  # the accent on light backgrounds
STEEL = "#5B7083"           # rules, secondary
REED = "#8B949E"            # muted text
GRID = "{{line}}"           # faint grid on dark
MONO = "ui-monospace, 'SF Mono', Menlo, 'DejaVu Sans Mono', Consolas, monospace"

DARK = dict(face=PAPER, accent=ACCENT, bg=NIGHT)
LIGHT = dict(face=INK, accent=ACCENT_DARK, bg="#FFFFFF")

# --- mark (drawn in a 100×100 box) -----------------------------------------------------------------------------------

FRAME = "M24,8 H76 L92,24 V76 L76,92 H24 L8,76 V24 Z"   # square with chamfered corners
MARK_BOX = "0 0 100 100"


def mark(p=DARK, width=8):
    return (f'<path d="{FRAME}" fill="none" stroke="{p["face"]}" stroke-width="{width}" stroke-linejoin="miter"/>'
            f'<rect x="38" y="30" width="24" height="40" fill="{p["accent"]}"/>')


def flat_mark(color):
    return mark(dict(face=color, accent=color))


def small_mark(p=DARK):
    """16–48 px: heavier frame, larger cursor."""
    return (f'<path d="{FRAME}" fill="none" stroke="{p["face"]}" stroke-width="13" stroke-linejoin="miter"/>'
            f'<rect x="34" y="26" width="32" height="48" fill="{p["accent"]}"/>')


def placed(body, cx, cy, width, box=100):
    k = width / box
    return f'<g transform="translate({cx} {cy}) scale({k:.4f}) translate({-box / 2} {-box / 2})">{body}</g>'


def icon(rounded=True, small=False):
    r = 160 if rounded else 0
    body = small_mark() if small else mark()
    return svg("0 0 1024 1024", f'<rect width="1024" height="1024" rx="{r}" fill="{NIGHT}"/>'
               + placed(body, 512, 512, 800 if small else 720))


# --- wordmark (system monospace, 80 px; about 0.6 em per character) --------------------------------------------------

SIZE = 80
ADVANCE = SIZE * 0.6


def wordmark_body(p=DARK):
    """The name and a block cursor in the accent. Returns the body and its width."""
    w = len(NAME) * ADVANCE
    body = (f'<text x="0" y="80" font-family="{MONO}" font-size="{SIZE}" font-weight="700" fill="{p["face"]}">'
            f'{NAME}</text><rect x="{w + 8:.0f}" y="26" width="{ADVANCE * 0.8:.0f}" height="58" fill="{p["accent"]}"/>')
    return body, w + 8 + ADVANCE * 0.8


def wordmark(p=DARK):
    body, width = wordmark_body(p)
    return svg(f"-8 10 {width + 16:.0f} 90", body)


def lockup(p=DARK):
    body, width = wordmark_body(p)
    return svg(f"-4 2 {width + 140:.0f} 106",placed(mark(p), 50, 55, 92) + f'<g transform="translate(122 0)">{body}</g>')


def social():
    """1280×640: GitHub social preview, link previews – terminal style."""
    body, _ = wordmark_body(DARK)
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="640" stroke="{GRID}"/>' for x in range(0, 1281, 64)) + \
           "".join(f'<line x1="0" y1="{y}" x2="1280" y2="{y}" stroke="{GRID}"/>' for y in range(0, 641, 64))
    return svg("0 0 1280 640", f'<rect width="1280" height="640" fill="{NIGHT}"/>{grid}'
               + placed(mark(), 260, 320, 300) +
               f'<text x="480" y="200" font-family="{MONO}" font-size="26" fill="{REED}">$ {NAME} --about</text>'
               f'<g transform="translate(476 220) scale(1.3)">{body}</g>'
               f'<text x="480" y="420" font-family="{MONO}" font-size="28" fill="{PAPER}">{TAGLINE}</text>'
               f'<text x="480" y="466" font-family="{MONO}" font-size="24" fill="{REED}">// free software · a falkOSS project</text>',
               (1280, 640))


def favicon():
    """The small mark, transparent: paper on dark tabs, ink on light ones."""
    style = (f'<style>.f{{stroke:{PAPER}}}.c{{fill:{ACCENT}}}'
             f'@media (prefers-color-scheme: light){{.f{{stroke:{INK}}}.c{{fill:{ACCENT_DARK}}}}}</style>')
    body = small_mark().replace(f'stroke="{PAPER}"', 'class="f"').replace(f'fill="{ACCENT}"', 'class="c"')
    return svg(MARK_BOX, style + body)


def main():
    kit = {
        "icon": icon(),
        "icon-square": icon(rounded=False),
        "icon-small": icon(small=True),
        "mark-on-dark": svg(MARK_BOX, mark(DARK)),
        "mark-on-light": svg(MARK_BOX, mark(LIGHT)),
        "mark-black": svg(MARK_BOX, flat_mark("#000000")),
        "mark-white": svg(MARK_BOX, flat_mark("#FFFFFF")),
        "wordmark-on-dark": wordmark(DARK),
        "wordmark-on-light": wordmark(LIGHT),
        "lockup-on-dark": lockup(DARK),
        "lockup-on-light": lockup(LIGHT),
        "social": social(),
        "favicon": favicon(),
    }
    export(HERE, NAME, kit, NIGHT)


if __name__ == "__main__":
    main()
