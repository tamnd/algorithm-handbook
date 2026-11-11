The Handbook of Algorithms, edition 0.20.1: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.20.0](https://github.com/tamnd/algorithm/releases/tag/v0.20.0)
(`0e2d301058ec9c55aaf9f5c6f8450d4a651f6b76`); the edition number follows the release of the site, and the third
number (0.20.1) marks a new build of the same release.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 963 |
| 1 | Foundations | 204 | 928 |
| 2 | Techniques | 208 | 1,049 |
| 3 | Data structures | 427 | 3,272 |
| 4 | Sorting | 156 | 848 |
| 5 | Searching | 115 | 600 |
| 6 | Sequences | 120 | 546 |
| 7 | Graphs | 685 | 3,425 |
| 8 | Strings | 216 | 1,168 |
| 9 | Automata and parsing | 270 | 1,618 |
| 10 | Number theory | 238 | 1,343 |
| 11 | Algebra | 328 | 1,988 |
| 12 | Numerical | 465 | 2,856 |
| 13 | Geometry | 280 | 1,682 |
| 14 | Combinatorics | 174 | 809 |
| 15 | Optimization | 301 | 1,654 |
| 16 | Logic and constraints | 325 | 1,984 |
| 17 | Randomized | 141 | 793 |
| 18 | Approximation | 213 | 1,343 |
| 19 | Online and streaming | 195 | 1,059 |
| 20 | Parallel | 128 | 841 |
| 21 | Distributed | 281 | 1,948 |
| | **All** | **5,470** | **32,717** |

- **New in this edition: Volume 21, Distributed**: consensus (FLP, Paxos, Raft), leader election on rings and
  general networks, logical, vector and hybrid clocks and the ordering of events, replication and CRDTs,
  distributed graph algorithms in the LOCAL and CONGEST models, Byzantine agreement, and gossip. It has the same
  apparatus as the other volumes: a volume introduction, chapter openings, summaries, exercises with hints, notes,
  concept maps and indexes.
- **New typesetting of the entries, in every volume.** Definitions, theorems, lemmas, corollaries, claims,
  invariants, examples and remarks are numbered within their entry (Lemma 8.4.21.3 is the third numbered
  statement of entry 8.4.21), and so are the pseudocode algorithms, which now carry a caption with the name of the
  procedure. A reference such as "by Lemma 2" in an entry becomes a link to the statement with its full number. A
  proof ends with a square at the right of its last line. Each volume has a new appendix, *Theorems and
  definitions*, listing its theorems, propositions, corollaries, definitions and conjectures by chapter with their
  pages, and its introduction says how the numbering works. Links inside proofs, which earlier editions left
  pointing to the site, now go to the entry in the book.
- **Volume 0, Guide and Index**, covers the whole set of 5,470 entries, has a new learning path, *Distributed
  algorithms*, and a new section of Chapter 0.1, *Statements, algorithms and proofs*.
- **Volumes 1 to 20** are rebuilt with the new typesetting, with the same entries under the same numbers as in
  0.19.0. Their cross-references to entries of Volume 21 now give entry numbers.
- Volumes 22 to 31 are forthcoming; Volume 0 lists their chapters.
- Edition 0.20.0 was assembled but not released; this edition replaces it.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.20.1-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
