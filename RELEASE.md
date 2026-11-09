The Handbook of Algorithms, edition 0.13.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.13.0](https://github.com/tamnd/algorithm/releases/tag/v0.13.0)
(`48e91f799a03f91e89978716fa13d84f8be850a8`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 645 |
| 1 | Foundations | 204 | 920 |
| 2 | Techniques | 208 | 1,030 |
| 3 | Data structures | 427 | 3,228 |
| 4 | Sorting | 156 | 836 |
| 5 | Searching | 115 | 592 |
| 6 | Sequences | 120 | 540 |
| 7 | Graphs | 685 | 3,370 |
| 8 | Strings | 216 | 1,146 |
| 9 | Automata and parsing | 270 | 1,592 |
| 10 | Number theory | 238 | 1,321 |
| 11 | Algebra | 328 | 1,963 |
| 12 | Numerical | 465 | 2,814 |
| 13 | Geometry | 280 | 1,648 |
| 14 | Combinatorics | 174 | 795 |
| | **All** | **3,886** | **22,440** |

- **Volume 0, Guide and Index**: preface, how to use the set, notation, the volumes and their map, learning
  paths, problems and their algorithms, glossary, timeline, bibliography and indexes of the whole set.
- **Volumes 1 to 14**, from Foundations to Combinatorics: every written entry of the area, with volume
  introductions, chapter openings, summaries, exercises with hints, notes, concept maps and indexes.
  Volumes 13 (Geometry) and 14 (Combinatorics) are complete in this edition: their chapters on Voronoi and
  Delaunay, range searching, proximity, geometric optimization, partitions and trees, Gray codes, counting
  and exhaustive search are new.
- Volumes 15 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.13.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry numbers (such as 4.1.12) belong to this edition. The entries are the text of the site; the learner pages
were drafted by AI agents (Claude) and checked as described in `content/PROVENANCE.md`. Two damaged passages of
the source were repaired for the books (`hb/patches.py`): a missing `$`, and a proof paragraph whose symbols
were lost, which carries a footnote saying so. Known issue: two characters (`𝛷`, a
mathematical italic capital phi) near page 530 of Volume 1 are missing from the PDF. Text CC BY-SA 4.0,
code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the books at
https://github.com/tamnd/algorithm-handbook/issues.
