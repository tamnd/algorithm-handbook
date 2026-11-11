The Handbook of Algorithms, edition 0.19.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.19.0](https://github.com/tamnd/algorithm/releases/tag/v0.19.0)
(`372ce4fb42a4c8e4d9777d5f2dc0954c5f97fffe`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 913 |
| 1 | Foundations | 204 | 920 |
| 2 | Techniques | 208 | 1,033 |
| 3 | Data structures | 427 | 3,230 |
| 4 | Sorting | 156 | 842 |
| 5 | Searching | 115 | 592 |
| 6 | Sequences | 120 | 540 |
| 7 | Graphs | 685 | 3,372 |
| 8 | Strings | 216 | 1,146 |
| 9 | Automata and parsing | 270 | 1,594 |
| 10 | Number theory | 238 | 1,321 |
| 11 | Algebra | 328 | 1,963 |
| 12 | Numerical | 465 | 2,814 |
| 13 | Geometry | 280 | 1,650 |
| 14 | Combinatorics | 174 | 795 |
| 15 | Optimization | 301 | 1,626 |
| 16 | Logic and constraints | 325 | 1,948 |
| 17 | Randomized | 141 | 775 |
| 18 | Approximation | 213 | 1,325 |
| 19 | Online and streaming | 195 | 1,033 |
| 20 | Parallel | 128 | 825 |
| | **All** | **5,189** | **30,257** |

- **New in this edition: Volume 20, Parallel**: the work-span model and its laws, Brent's theorem and work
  stealing, the PRAM; parallel primitives (reduce, scan, pack, merge, list ranking, tree contraction); parallel
  graph algorithms (BFS, delta-stepping, Luby's independent set, Shiloach-Vishkin); GPU algorithms (the SIMT
  model, memory coalescing, tiling, the roofline model); and the BSP, MapReduce and Pregel models of a cluster.
  It has the same apparatus as the other volumes: a volume introduction, chapter openings, summaries, exercises
  with hints, notes, concept maps and indexes.
- **Volume 0, Guide and Index**, covers the whole set of 5,189 entries and has a new learning path, *Parallel
  algorithms*.
- **Volumes 1 to 19** are rebuilt from the new release of the site, with the same entries under the same numbers
  as in 0.18.0. Their cross-references to entries of Volume 20 now give entry numbers.
- Volumes 21 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.19.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry numbers (such as 4.1.12) belong to this edition. The entries are the text of the site; the learner pages
were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text CC BY-SA 4.0, code MIT.
Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the books at
https://github.com/tamnd/algorithm-handbook/issues.
