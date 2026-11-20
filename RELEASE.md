The Handbook of Algorithms, edition 0.45.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.45.0](https://github.com/tamnd/algorithm/releases/tag/v0.45.0)
(`91e1d11ae55f72130a50cdc92dc2f6d9af6115be`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 2,351 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,140 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 596 |
| 7 | Graphs | 685 | 3,693 |
| 8 | Strings | 259 | 1,632 |
| 9 | Automata and parsing | 270 | 1,604 |
| 10 | Number theory | 238 | 1,438 |
| 11 | Algebra | 328 | 2,122 |
| 12 | Numerical | 463 | 3,008 |
| 13 | Geometry | 280 | 1,796 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,766 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,309 |
| 19 | Online and streaming | 195 | 1,135 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 389 | 3,128 |
| 24 | Compression and coding | 220 | 1,741 |
| 25 | Machine learning | 419 | 2,982 |
| 26 | Systems | 346 | 2,550 |
| 27 | Biology | 468 | 3,346 |
| 28 | Graphics and signals | 594 | 4,817 |
| 29 | Games and search | 205 | 1,592 |
| 30 | Quantum | 152 | 1,582 |
| 31 | CAD | 374 | 3,027 |
| 32 | Electronic design automation | 358 | 2,690 |
| 33 | Statistics and inference | 276 | 2,168 |
| 34 | Compilers and program analysis | 272 | 2,793 |
| 35 | Information retrieval and AI reasoning | 276 | 1,716 |
| 36 | Control | 279 | 2,334 |
| 37 | Robotics | 264 | 2,135 |
| 38 | Computer vision | 277 | 2,593 |
| 39 | Complexity | 284 | 1,225 |
| 40 | Databases | 296 | 2,420 |
| 41 | Natural language and speech | 299 | 2,157 |
| 42 | Algorithmic game theory | 6 | 102 |
| 43 | Scientific computing | 292 | 2,441 |
| 45 | Security and privacy | 2 | 75 |
| 46 | Imaging and inverse problems | 1 | 61 |
| | **All** | **12,015** | **87,964** |

- **Volume 43, Scientific computing**, now has all nine of its chapters written, 292 entries in all (3 in
  0.43.0): *N-body and particle methods* (30 entries: direct sums, Barnes-Hut trees and the fast multipole
  method, particle-mesh and P3M methods, plasma particle-in-cell, integrators for gravitating bodies, the material
  point method), *Molecular simulation* (40: molecular dynamics, force fields, Ewald and particle-mesh Ewald sums,
  constraints and multiple time steps, ab initio dynamics, thermostats and barostats, free energy methods),
  *Conservation laws and shock capturing* (34: Riemann solvers and numerical fluxes, MUSCL, ENO and
  discontinuous Galerkin schemes, entropy stability, well-balanced schemes, adaptive mesh refinement),
  *Incompressible flow and turbulence* (35: projection and pressure-correction methods, interfaces and immersed
  bodies, turbulence models from k-epsilon to large eddy simulation, lattice Boltzmann methods and smoothed
  particle hydrodynamics), *Finite element practice* (39: weak forms, elements and assembly, locking and mixed
  methods, stabilized and discontinuous methods, error estimation and adaptivity, high order, dynamics and
  nonlinear solids, boundary, virtual and extended elements), *Particle transport* (27: Monte Carlo transport,
  variance reduction, criticality, discrete ordinates, hybrid methods, thermal radiation and rarefied gas),
  *Multiscale methods* (29: homogenization, multiscale finite elements, heterogeneous multiscale methods,
  coarse-graining, saddle points, rare transitions and accelerated molecular dynamics), *Uncertainty
  quantification* (29: sampling and multilevel Monte Carlo, rare failures, polynomial chaos and stochastic
  collocation, sensitivity analysis, calibration and inverse problems, reduced models) and *Data assimilation*
  (29: optimal interpolation, 3D-Var and 4D-Var, the ensemble Kalman filter and its repairs, ensemble smoothers,
  hybrid methods, particle filters). The introduction of the volume is rewritten for the complete volume.
- **Volume 0, Guide and Index**, covers the whole set of 12,015 entries and has a new learning path, *Simulation
  of physical systems*, in seven stages from time stepping to data assimilation.
- The subject index of a volume now lists every topic of another volume that it uses, also when two of them have
  the same name (such as *Bit vector*, 2.12.8 and 3.12.1); before, only one of the two was listed, and which one
  could change from build to build. References from Volumes 27 and 28 to Volume 41 now carry the numbers that
  Volume 41 gives its entries, and a link from a proof to the proof of another entry, written as a relative path,
  now leads to that proof.
- Only the volumes whose text changed were built again: 0, 1, 2, 7, 10, 12, 17, 23 to 29, 31, 32, 38, 41 and 43.
  The other volumes have the same text as in 0.43.0, and their files are those of 0.43.0 under the new names, so
  their covers, title pages and copyright pages say edition 0.43.0.
- The entries have the corrections that the site made up to its release v0.45.0, among them those found while
  writing edition 0.42.0 in Volumes 3, 8 and 28 and edition 0.43.0 in Volume 41. The builder no longer patches
  any entry.
- Volume 44 (Communications) is not built: the site has only short pages for it so far. Volume 0 lists its
  chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.45.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
