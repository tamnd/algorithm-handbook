The Handbook of Algorithms, edition 0.26.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.26.0](https://github.com/tamnd/algorithm/releases/tag/v0.26.0)
(`f1e874c8c2165fa636d4556fa3534cadaf5df795`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,402 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,140 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 594 |
| 7 | Graphs | 685 | 3,691 |
| 8 | Strings | 216 | 1,256 |
| 9 | Automata and parsing | 270 | 1,604 |
| 10 | Number theory | 238 | 1,438 |
| 11 | Algebra | 328 | 2,122 |
| 12 | Numerical | 465 | 3,024 |
| 13 | Geometry | 280 | 1,794 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,764 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,309 |
| 19 | Online and streaming | 195 | 1,135 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 390 | 3,136 |
| 24 | Compression and coding | 220 | 1,741 |
| 25 | Machine learning | 419 | 2,982 |
| 26 | Systems | 442 | 3,209 |
| 27 | Biology | 254 | 1,611 |
| 28 | Graphics and signals | 82 | 569 |
| | **All** | **7,432** | **50,220** |

- **New in this edition: Volume 27, Biology**, in four chapters: sequence alignment (scoring matrices and gap
  penalties, the dynamic programs of Needleman-Wunsch, Smith-Waterman and Gotoh, Hirschberg's linear space, banded
  alignment, seeds, BLAST and the Karlin-Altschul statistics, read mapping with minimizers and the FM-index,
  multiple alignment, its NP-hardness and the progressive methods, profile hidden Markov models), genome assembly
  (shotgun sequencing and the Lander-Waterman model, the shortest common superstring, overlap and string graphs,
  de Bruijn graphs and their simplification, scaffolding and the measures of an assembly), phylogenetics (tree
  metrics and the four-point condition, UPGMA and neighbor joining, small and large parsimony, substitution models
  and Felsenstein's pruning algorithm, tree search and the bootstrap, consensus and the distances between trees,
  perfect phylogeny, the coalescent, reconciliation and phylogenetic networks) and structure prediction (RNA
  secondary structure by the Nussinov, Zuker and McCaskill algorithms and the hardness of pseudoknots, protein
  secondary and tertiary structure, the HP model, threading and comparative modeling, side-chain packing,
  superposition by the Kabsch algorithm, RMSD and TM-score). Each page says which part of a method is exact and
  which part is a model of biology.
- **New: Volume 28, Graphics and signals**, with two chapters written: *Rasterization* (47 entries: lines by
  Bresenham's, the DDA and Wu's algorithms, circles and ellipses, triangles by edge functions and fill rules,
  polygon scan conversion, clipping by Cohen-Sutherland, Liang-Barsky and Sutherland-Hodgman, perspective-correct
  interpolation, shading, texture mapping and mipmaps, antialiasing and compositing) and *Visibility* (35 entries:
  the z-buffer and its hierarchy, the painter's, Newell-Newell-Sancha and Warnock algorithms, BSP trees, hidden
  lines, culling, portals and potentially visible sets, shadow volumes and shadow maps, and the art gallery
  theorems). Chapters 28.2, 28.4, 28.5 and 28.6 have an opening only, until the site writes their entries.
- **Volume 0, Guide and Index**, covers the whole set of 7,432 entries and has a new learning path,
  *Biology*.
- **Volumes 1 to 26** have the same entries under the same numbers as in 0.25.0, with the corrections that the
  site's release v0.26.0 made to them; their cross-references to entries of Volumes 27 and 28 (Needleman-Wunsch,
  the de Bruijn graph, neighbor joining, Bresenham's algorithm, the z-buffer and others) now give entry numbers.
- Volumes 29 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.26.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
