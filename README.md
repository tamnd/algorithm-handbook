# The Handbook of Algorithms

The content of [algorithm.tamnd.com](https://algorithm.tamnd.com) as a set of books that a person can learn from,
from the first page to the last: one volume per area of the site, in PDF, EPUB and LaTeX.

Each area of the site is a volume, each sub-area a chapter, and each written page an entry with a fixed number
(4.1.12 is the twelfth entry of chapter 1 of Volume 4, *Sorting*). Around the entries, the handbook adds the
pages a reference site does not need and a textbook does: an introduction to each volume, an opening, groups and
a reading order for each chapter, summaries, exercises with hints, notes on history and further reading,
concept maps, problem tables, a bibliography and indexes. Volume 0, *Guide and Index*, holds the preface, the
notation, learning paths across the set, a catalogue of problems, a glossary, a timeline and the master index.

## Volumes in edition 0.16.0

Built from [`tamnd/algorithm`](https://github.com/tamnd/algorithm) release
[v0.16.0](https://github.com/tamnd/algorithm/releases/tag/v0.16.0), the commit named in [`EDITION`](EDITION). The edition
number of the handbook follows the release of the site it is built from. The books are on the
[releases page](https://github.com/tamnd/algorithm-handbook/releases).

| | Volume | Entries | Learner pages |
|---|---|---|---|
| 0 | Guide and Index | the whole set | written |
| 1 | Foundations | 204 | written |
| 2 | Techniques | 208 | written |
| 3 | Data structures | 427 | written |
| 4 | Sorting | 156 | written |
| 5 | Searching | 115 | written |
| 6 | Sequences | 120 | written |
| 7 | Graphs | 685 | written |
| 8 | Strings | 216 | written |
| 9 | Automata and parsing | 270 | written |
| 10 | Number theory | 238 | written |
| 11 | Algebra | 328 | written |
| 12 | Numerical | 465 | written |
| 13 | Geometry | 280 | written |
| 14 | Combinatorics | 174 | written |
| 15 | Optimization | 301 | written |
| 16 | Logic and constraints | 325 | written |
| 17 | Randomized | 141 | written |
| 18 | Approximation | 35 | Chapter 18.1 written; openings only for 18.2–18.6 |
| 19–31 | Online and streaming … Complexity | – | forthcoming: the site has only short pages so far |

## Building

Requirements: Python 3.11+, [pandoc](https://pandoc.org) 3.8 or later, [tectonic](https://tectonic-typesetting.github.io),
Graphviz, and poppler (`pdfinfo`). Fonts come from tectonic's TeX Live bundle; nothing else is installed.

```sh
git clone https://github.com/tamnd/algorithm ../algorithm      # the content, next to this repository
pip install .
python -m hb survey                                            # the volumes, chapters, entries and stubs
python -m hb check --volume all                                # the learner pages: links, outlines, exercises, style
python -m hb build --volume 4 --formats tex,pdf,epub           # build/04-sorting/main.pdf, main.epub, main.tex
python -m hb build --volume all --formats tex,pdf,epub         # Volume 0 and every volume with entries
```

`--content` points at another checkout of the content. A volume takes 2 to 12 minutes, most of it in tectonic.

## Layout

| Path | What |
|---|---|
| `hb/` | the builder: corpus, book structure, Markdown assembly, figures, apparatus, LaTeX, EPUB, covers |
| `filters/hb.lua` | the pandoc filter that lets one Markdown file serve LaTeX and EPUB |
| `tex/handbook.sty`, `tex/epub.css` | the design of the PDF and the EPUB |
| `content/front/` | Volume 0: preface, how to use, notation, volumes, learning paths (`paths.yaml`) |
| `content/<area>/` | the learner pages of a volume: `volume.md`, and per chapter `outline.yaml`, `opening.md`, `summary.md`, `exercises.md`, `hints.md`, `notes.md` |
| `prompts/area.md` | the brief the learner pages are written from |

## How the text was made

The entries are the text of the site. The learner pages were drafted by AI agents (Claude) from a written brief
and a sample chapter, checked by `hb check`, and spot-checked; see [`content/PROVENANCE.md`](content/PROVENANCE.md).
Report errors in an entry at [tamnd/algorithm issues](https://github.com/tamnd/algorithm/issues) and errors in
the learner pages or the books here.

## Licences

The text of the books and of `content/` is licensed under [CC BY-SA 4.0](LICENSE-CONTENT), as on the site. The
code in the books is MIT, as on the site. The builder is [MIT](LICENSE).
