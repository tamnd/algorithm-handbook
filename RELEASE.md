The Handbook of Algorithms, edition 0.33.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.33.0](https://github.com/tamnd/algorithm/releases/tag/v0.33.0)
(`087d0ac163dde33af2a0b0ddc2f6bd8568885f09`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,777 |
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
| 12 | Numerical | 465 | 3,026 |
| 13 | Geometry | 280 | 1,796 |
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
| 28 | Graphics and signals | 401 | 2,747 |
| 29 | Games and search | 209 | 1,612 |
| 30 | Quantum | 152 | 1,582 |
| 31 | CAD | 374 | 3,026 |
| 32 | Electronic design automation | 358 | 2,690 |
| 33 | Statistics and inference | 276 | 2,168 |
| | **All** | **9,120** | **63,857** |

- **Volume 31, CAD, is now complete**: the six chapters that were openings only in 0.32.0 are written, and the
  volume has 374 entries in ten chapters. The new chapters are *Surface interrogation and design* (34 entries: point
  projection and inversion, distances and intersections of curves and surfaces with implicitization, lattice
  evaluation, the interval projected polyhedron algorithm and loop detection, curvature combs, isophotes, reflection
  lines, silhouettes and lines of curvature, continuity between patches with Gregory, n-sided and vertex blend
  patches, skinning and Gordon surfaces, fairing, developable surfaces, geodesics, offset trimming and Pythagorean
  hodograph curves), *Mechanism and assembly design* (40 entries: four-bar and slider-crank linkages with the Grashof
  condition, instant centers and coupler curves, six-bar and straight-line linkages and Kempe's universality
  theorem, function, path and motion generation with Freudenstein's equation and Burmester theory, cams, involute
  gears and planetary trains, and assembly and disassembly sequence planning with liaison graphs, AND/OR graphs and
  blocking graphs), *Mesh generation for analysis* (41 entries: quality measures and slivers, structured, elliptic
  and transfinite grids, advancing front, quadtree and octree meshing, constrained Delaunay tetrahedralization and
  Delaunay refinement, sliver exudation, surface meshing with restricted Delaunay triangulations and protecting
  balls, boundary layers, anisotropic adaptation and curved high-order meshes, quadrilateral meshing by paving,
  Q-Morph and Blossom-Quad, hexahedral meshing by whisker weaving, plastering, sweeping, polycubes and frame fields,
  and smoothing, untangling and improvement), *Isogeometric analysis and CAD-CAE integration* (25 entries: Bézier
  extraction, k-refinement, quadrature and collocation, T-splines and analysis-suitable T-splines, hierarchical,
  truncated and locally refined splines, volumetric parameterization, trimmed and immersed analysis with the finite
  cell and cut finite element methods, shells, boundary elements, shape optimization, defeaturing and mid-surface
  extraction), *Manufacturing process planning* (25 entries: computer-aided process planning and manufacturability,
  setups and operation sequences, locating and fixture planning with the Brost-Goldberg algorithm, tool life and
  cutting parameters, sheet metal with bend allowance, flat patterns, springback and bend sequences, molding with
  draft, undercuts, parting lines, gates and conformal cooling, and casting with Chvorinov's rule, risers and hot
  spots) and *Reverse engineering, inspection and tolerancing* (29 entries: algebraic and geometric fitting of
  circles, spheres, cylinders, cones and tori, parameter correction and squared distance minimization,
  segmentation and slippage analysis, B-rep reconstruction from scans, geometric dimensioning and tolerancing with
  datum frames, tolerance zones, the small displacement torsor and tolerance maps, localization, sampling and probe
  paths for inspection, minimum zone form error, and tolerance analysis and allocation). The four chapters written
  in 0.30.0 have 55 more entries: 31.1 *Solid modeling* adds offsets, Minkowski sums and medial surfaces, healing
  and tolerant modeling, Nef polyhedra and selective geometric complexes, direct modeling and persistent naming, and
  feature recognition; 31.3 *Geometric constraint solving* adds infinitesimal and global rigidity and distance
  geometry; 31.5 *Mesh processing and repair* adds mesh compression, curvature estimation, surface deformation,
  conformal parameterization, direction fields and segmentation; and 31.8 *CAM and additive manufacturing* adds
  slicing of exact models and curved layers, trochoidal and five-axis machining, feedrate scheduling and more
  topology optimization. As in the rest of the volume, the pages say which methods are exact, which come with a
  proved bound, and which are judged by measured results on test parts. The introduction of the volume now covers
  all ten chapters.
- **Volume 0, Guide and Index**, covers the whole set of 9,120 entries. It has a new learning path, *CAD*, in ten
  stages.
- **Volumes 1 to 30, 32 and 33** have the same entries under the same numbers as in 0.32.0. Cross-references from
  other volumes to the new entries of Volume 31 now give entry numbers.
- Volumes 34 to 39 (Compilers and program analysis, Information retrieval and AI reasoning, Control, Robotics,
  Computer vision, Complexity) are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.33.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
