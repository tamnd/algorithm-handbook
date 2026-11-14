The Handbook of Algorithms, edition 0.30.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.30.0](https://github.com/tamnd/algorithm/releases/tag/v0.30.0)
(`6ccf9a13ccfb8f2c88cabedad23c314bf0b6cdb7`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,594 |
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
| 32 | Electronic design automation | 148 | 1,103 |
| | **All** | **8,385** | **57,867** |

- **New in this edition: Volume 31, CAD**, with four of its ten chapters written: *Solid modeling* (35 entries:
  r-sets and regularized set operations, boundary representations with the winged-edge and radial-edge structures,
  Euler operators and the Euler-Poincaré formula, constructive solid geometry, set membership classification and
  boundary evaluation, Booleans on solids, surface-surface intersection by marching and by subdivision, offsets and
  blends, the robustness problem, exact geometric computation and simulation of simplicity, mass properties, and
  feature recognition and persistent naming), *Geometric constraint solving* (24 entries: constraint graphs, local
  propagation, graph-constructive solvers and the Fudos-Hoffmann and Owen methods, degrees-of-freedom analysis and
  decomposition-recombination plans, the root identification problem, and rigidity: Maxwell's count, Laman's and
  Tay's theorems, Henneberg constructions, the pebble game and global rigidity), *Mesh processing and repair* (32
  entries: mesh data structures, cleaning and hole filling, intersections, winding numbers and mesh Booleans,
  smoothing and fairing, discrete curvature, geodesics, parameterization, remeshing, segmentation and mesh
  comparison) and *CAM and additive manufacturing* (34 entries: slicing, build orientation and supports, cutter
  location and gouge detection, pocket and surface toolpaths, NC verification by z-maps and dexels, tolerance
  stack-up, nesting, and topology optimization). The other six chapters have openings that say what they will
  cover and what to read meanwhile.
- **New in this edition: Volume 32, Electronic design automation**, with four of its ten chapters written: *Logic
  synthesis and technology mapping* (40 entries: two-level minimization exactly and by Espresso, Boolean networks
  and algebraic division, kernels, technology mapping by tree covering and by cuts, FlowMap, and-inverter graphs and
  SAT sweeping, retiming, state assignment and high-level synthesis), *Partitioning, floorplanning and placement*
  (36 entries: Kernighan-Lin, Fiduccia-Mattheyses and multilevel partitioning, ratio cuts and spectral methods,
  Rent's rule, slicing floorplans, sequence pairs, B*-trees and O-trees, placement by simulated annealing, by
  quadratic and analytic methods and by electrostatics, and legalization), *Routing* (30 entries: Lee's and
  Hadlock's maze routers, rectilinear Steiner trees, trees with short source paths, global routing with rip-up and
  reroute and negotiated congestion, channel routing by the left-edge algorithm and its successors, and switchbox,
  river and escape routing) and *Timing, verification and test* (42 entries: Elmore delay and moment matching,
  static and statistical timing analysis, clock trees, buffering and gate sizing, design rule checking, extraction
  and lithography corrections, the stuck-at model, test generation by the D-algorithm, PODEM and SAT, fault
  simulation, scan and built-in self-test). The other six chapters have openings. The pages of both volumes say which
  problems are NP-hard, which algorithms are exact, and which heuristics are judged only by measured results.
- **Volume 0, Guide and Index**, covers the whole set of 8,385 entries. The guide now says that the site has 39
  areas, and lists the chapters of Volumes 31 and 32 with their state. It has no learning paths for the two new
  volumes yet; they will come when the volumes are complete.
- **Volumes 1 to 30** have the same entries under the same numbers as in 0.29.0. The entries of Volumes 29 and 30
  have the corrections that the site made in its release v0.30.0. Cross-references from earlier volumes to entries of
  Volumes 31 and 32 now give entry numbers. The site has added one area, Electronic design automation, before Complexity, which is now Volume 39;
  the learner pages that named it as Volume 38 now say Volume 39.
- Volumes 33 to 39 (Statistics and inference, Compilers and program analysis, Information retrieval and AI
  reasoning, Control, Robotics, Computer vision, Complexity) are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.30.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
