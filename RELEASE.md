The Handbook of Algorithms, edition 0.32.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.32.0](https://github.com/tamnd/algorithm/releases/tag/v0.32.0)
(`f8d4d6a217e3fb7d9058c9137d66c70534fa4ab1`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,718 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,140 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 594 |
| 7 | Graphs | 685 | 3,693 |
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
| 28 | Graphics and signals | 401 | 2,745 |
| 29 | Games and search | 209 | 1,612 |
| 30 | Quantum | 152 | 1,582 |
| 31 | CAD | 125 | 980 |
| 32 | Electronic design automation | 358 | 2,690 |
| 33 | Statistics and inference | 276 | 2,168 |
| | **All** | **8,871** | **61,746** |

- **Volume 32, Electronic design automation, is now complete**: the six chapters that were openings only in 0.31.0
  are written, and the volume has 358 entries in ten chapters. The new chapters are *High-level synthesis and
  scheduling* (33 entries: control data flow graphs, Kahn process networks and synchronous dataflow, scheduling a
  block under resource and latency limits, allocation and binding of units and registers, branches and loops with
  speculation and modulo scheduling, the iteration bound, folding and unfolding for signal processing, state
  assignment and decomposition of controllers, and interface synthesis and hardware-software partitioning), *Logic and circuit simulation* (36 entries: multi-valued logic and delay
  models, event-driven and compiled logic simulators, hazards and switch-level simulation, modified nodal analysis
  and device models, sparse LU factorization, the DC operating point with gmin and source stepping, transient
  analysis with companion models and TR-BDF2, small-signal AC, sensitivity and noise analysis, periodic steady
  state by shooting and harmonic balance, and timing and mixed-mode simulation), *Hardware verification* (28 entries: coverage
  of simulation, constrained random stimulus, assertions, combinational equivalence checking and debugging,
  sequential equivalence, symbolic simulation and symbolic trajectory evaluation, verification of arithmetic circuits and processors, and clock
  domain crossings with synchronizers), *Power, reliability and manufacturability* (41 entries: switching activity
  and its estimation, clock and power gating, multiple threshold voltages and other ways to reduce power, power grid
  analysis and vectorless verification, coupling noise, electromigration, aging, soft errors and thermal models,
  critical area and yield models, and dummy fill, imaging models and inverse lithography), *Test and diagnosis* (37 entries: fault coverage and defect
  level, fault models for defects and delay, test generation and compaction, fault simulation, testability measures
  and random-pattern test, scan test and test compression, board, core and memory test, and diagnosis of failing
  chips) and *FPGA, analog and emerging technologies* (35 entries: FPGA architecture, technology mapping into lookup
  tables, packing, placement and routing of FPGAs, analog sizing and symbolic analysis, analog layout,
  three-dimensional integration, and reversible circuits and qubit mapping). As in the rest of the volume, the
  pages say which methods are exact, which come with a proved bound, and which are judged by measured results on
  benchmarks. The introduction of the volume now covers all ten chapters.
- **Volume 0, Guide and Index**, covers the whole set of 8,871 entries. It has a new learning path, *Electronic
  design automation*, in eight stages.
- **Volumes 1 to 31 and 33** have the same entries under the same numbers as in 0.31.0. Cross-references from
  other volumes to the new entries of Volume 32 now give entry numbers.
- Volumes 34 to 39 (Compilers and program analysis, Information retrieval and AI reasoning, Control, Robotics,
  Computer vision, Complexity) are forthcoming; Volume 0 lists their chapters. Chapters 31.2, 31.4, 31.6, 31.7, 31.9
  and 31.10 of Volume 31 are still openings only.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.32.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
