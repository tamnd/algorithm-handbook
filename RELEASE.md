The Handbook of Algorithms, edition 0.34.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.34.0](https://github.com/tamnd/algorithm/releases/tag/v0.34.0)
(`77b456a32af754bde203884ba01acc9a4d256248`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,832 |
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
| 34 | Compilers and program analysis | 273 | 2,797 |
| | **All** | **9,393** | **66,709** |

- **New in this edition: Volume 34, Compilers and program analysis**, with all eight of its chapters written: *Type
  systems and inference* (31 entries: the simply typed lambda calculus, type soundness and the Curry-Howard
  correspondence, Hindley-Milner inference with algorithms W and J, principal types and the value restriction, the
  DEXPTIME-completeness of ML typability, the undecidability of polymorphic recursion and of System F inference,
  bidirectional checking, type classes and monomorphization, subtyping, row polymorphism, recursive and gradual
  types, and effect systems, linear types, borrow checking, dependent, refinement and liquid types), *Intermediate
  representations* (35 entries: three-address code, basic blocks and control flow graphs, dominators by the
  Cooper-Harvey-Kennedy algorithm, dominance frontiers, natural loops and reducible graphs, static single assignment
  form with Cytron's and Braun's constructions, leaving SSA form, control dependence, the program dependence graph
  and the sea of nodes, and continuation-passing style, A-normal form, closure conversion and defunctionalization),
  *Dataflow analysis and abstract interpretation* (44 entries: liveness, reaching definitions and the other classic
  problems, monotone and distributive frameworks, the meet-over-all-paths and maximal fixed point solutions, the
  worklist algorithm and the Kam-Ullman bound, sparse conditional constant propagation, Galois connections, the
  interval, octagon and polyhedra domains with widening and narrowing, interprocedural analysis with IFDS and IDE,
  taint analysis, program slicing, shape analysis, bi-abduction and analysis in Datalog), *Optimizations* (32
  entries: value numbering, dead code elimination, common subexpressions and global value numbering, loop-invariant
  code motion, partial redundancy elimination with lazy code motion and SSAPRE, strength reduction, inlining,
  devirtualization, profile-guided optimization with Ball-Larus path profiling and Pettis-Hansen code positioning,
  partial evaluation and the Futamura projections, deforestation and supercompilation, the full employment theorem,
  superoptimization and equality saturation), *Loop transformations* (33 entries: data dependences with distance
  and direction vectors, induction variables and chains of recurrences, the GCD and Banerjee tests, unrolling,
  interchange, fusion, distribution, skewing and tiling, vectorization with the Allen-Kennedy algorithm and SLP,
  DOACROSS loops, unimodular transformations, the Wolf-Lam locality algorithm, and the polyhedral model with
  Feautrier's dataflow and scheduling, the Pluto algorithm and polyhedral scanning), *Code generation and JIT
  compilation* (41 entries: activation records and threaded code, instruction selection by maximal munch, Sethi-Ullman
  numbering, tree tiling and BURS, register allocation by graph coloring with Chaitin's and Briggs's allocators,
  spilling, splitting, rematerialization and coalescing, linear scan, chordal interference graphs in SSA form,
  instruction scheduling, trace and superblock scheduling and software pipelining, inline caches, hidden classes,
  type feedback, deoptimization and on-stack replacement, tracing and meta-tracing JIT compilers, self-optimizing
  interpreters and copy-and-patch compilation), *Pointer and alias analysis* (25 entries: Andersen's and
  Steensgaard's analyses and Das's one-level flow, field sensitivity, cycle elimination and offline variable
  substitution, demand-driven and sparse flow-sensitive analysis, call graphs by class hierarchy, rapid type and
  variable type analysis, 0-CFA and k-CFA, object sensitivity, BDD-based analysis, type-based alias analysis,
  mod-ref and escape analysis, and the undecidability and hardness results) and *Verification, symbolic execution
  and synthesis* (32 entries: path conditions, symbolic execution and path explosion, concolic testing, coverage-guided
  and grammar-based fuzzing, delta debugging, verification condition generation, loop invariants by Houdini and by
  Farkas' lemma, proof-carrying code, ranking functions and transition invariants, noninterference and
  self-composition, verified compilation and translation validation, program synthesis by enumeration, version space
  algebras, sketching, deduction and types, program repair, and reactive synthesis with the Pnueli-Rosner theorem).
  The pages say which analyses are proved sound or optimal, which problems are undecidable or NP-hard, and which
  methods are heuristics judged by measured results.
- **Volume 0, Guide and Index**, covers the whole set of 9,393 entries. It has a new learning path, *Compilers and
  program analysis*, in eight stages.
- **Volumes 1 to 33** have the same entries under the same numbers as in 0.33.0. The entries of Volume 33 have the
  corrections that the site made in its release v0.34.0. Cross-references from other volumes to entries of Volume 34
  now give entry numbers.
- Volumes 35 to 39 (Information retrieval and AI reasoning, Control, Robotics, Computer vision, Complexity) are
  forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.34.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
