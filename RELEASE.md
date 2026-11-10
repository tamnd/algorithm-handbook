The Handbook of Algorithms, edition 0.16.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.16.0](https://github.com/tamnd/algorithm/releases/tag/v0.16.0)
(`daf7502a7e0e04e831fe0648a57951da63a3e390`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 823 |
| 1 | Foundations | 204 | 920 |
| 2 | Techniques | 208 | 1,030 |
| 3 | Data structures | 427 | 3,228 |
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
| 18 | Approximation | 35 | 203 |
| | **All** | **4,688** | **27,178** |

- **New in this edition: Volumes 15 to 18.**
  - **Volume 15, Optimization**: linear and integer programming, convex optimization, gradient methods,
    combinatorial optimization, metaheuristics, multi-objective optimization.
  - **Volume 16, Logic and constraints**: SAT solving, SMT, constraint satisfaction, binary decision diagrams,
    unification and resolution, model checking.
  - **Volume 17, Randomized**: sampling, shuffling, random hashing, Monte Carlo and Las Vegas algorithms,
    Markov chain Monte Carlo, derandomization.
  - **Volume 18, Approximation** (partial): Chapter 18.1, covering and packing, is complete. The other five
    chapters have an opening only, because the site has not yet written their entries.
  - Each new volume has the same apparatus as the others: a volume introduction, chapter openings, summaries,
    exercises with hints, notes, concept maps and indexes.
- **Volume 0, Guide and Index**: preface, how to use the set, notation, the volumes and their map, learning
  paths, problems and their algorithms, glossary, timeline, bibliography and indexes of the whole set. It has
  two new learning paths: *Optimization and constraint solving* and *Randomized and approximation algorithms*.
- **Volumes 1 to 14** are rebuilt from the new release of the site, with the same entries under the same numbers
  as in 0.13.0.
- Volumes 19 to 31 are forthcoming; Volume 0 lists their chapters.

**Fixes since 0.13.0.**
- **Mathematics printed as text.** Pandoc does not close an inline formula whose closing `$` follows a space,
  as in `$\Phi = $`. A few entries and exercises printed their dollar signs and TeX source as text, including
  the two `𝛷` that were missing from Volume 1 in 0.13.0. The builder now repairs such formulas in the entries and
  in the learner pages, and four entries whose source mathematics was damaged are patched (`hb/patches.py`).
- **EPUB formulas shown as TeX source.** Some EPUB formulas (`\textsc`, `\atop`, `\cfrac`, `\bmod` and a few
  others) appeared as TeX source; they are now written in forms that MathML can show.
- **EPUB links.** A group or section heading with the same name as an entry ("Quicksort", "Termination") took
  the entry's identifier, so some links in the EPUB went to the heading and not to the entry. Every heading now
  has an identifier of its own, and links from an entry to one of its own sections ("see Variants below") now
  go to that section of that entry, in the PDF and the EPUB.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.16.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry numbers (such as 4.1.12) belong to this edition. The entries are the text of the site; the learner pages
were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text CC BY-SA 4.0, code MIT.
Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the books at
https://github.com/tamnd/algorithm-handbook/issues.
