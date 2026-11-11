The Handbook of Algorithms, edition 0.18.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.18.0](https://github.com/tamnd/algorithm/releases/tag/v0.18.0)
(`aea3293f66757588daf1d5493e06ecf4ffe5e768`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 898 |
| 1 | Foundations | 204 | 920 |
| 2 | Techniques | 208 | 1,033 |
| 3 | Data structures | 427 | 3,230 |
| 4 | Sorting | 156 | 840 |
| 5 | Searching | 115 | 592 |
| 6 | Sequences | 120 | 540 |
| 7 | Graphs | 685 | 3,370 |
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
| | **All** | **5,061** | **29,413** |

- **New in this edition: Volume 19, Online and streaming**, and the whole of **Volume 18, Approximation**.
  - **Volume 18, Approximation**, is now complete. Besides covering and packing (Chapter 18.1, as in 0.16.0) it
    has scheduling, the travelling salesman problem, LP rounding, approximation schemes and hardness of
    approximation: 213 entries in place of 35.
  - **Volume 19, Online and streaming**: paging and caching, online scheduling, competitive analysis (ski rental,
    secretary and prophet problems, online matching, learning from experts), streaming sketches (Count-Min,
    HyperLogLog, Misra-Gries, quantile summaries) and sliding windows.
  - Both have the same apparatus as the other volumes: a volume introduction, chapter openings, summaries,
    exercises with hints, notes, concept maps and indexes.
- **Volume 0, Guide and Index**, covers the whole set of 5,061 entries and has two new learning paths:
  *Approximation algorithms* and *Online and streaming algorithms*.
- **Volumes 1 to 17** are rebuilt from the new release of the site, with the same entries under the same numbers
  as in 0.16.0. Their cross-references to entries of Volumes 18 and 19 now give entry numbers.
- Volumes 20 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.18.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry numbers (such as 4.1.12) belong to this edition. The entries are the text of the site; the learner pages
were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text CC BY-SA 4.0, code MIT.
Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the books at
https://github.com/tamnd/algorithm-handbook/issues.
