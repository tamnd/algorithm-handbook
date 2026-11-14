The Handbook of Algorithms, edition 0.29.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.29.0](https://github.com/tamnd/algorithm/releases/tag/v0.29.0)
(`1b4668b1b67228b41adf402d55964388835c05b4`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,542 |
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
| 29 | Games and search | 209 | 1,610 |
| 30 | Quantum | 152 | 1,582 |
| | **All** | **8,112** | **55,730** |

- **New in this edition: Volume 30, Quantum**, in four chapters: *Quantum primitives* (65 entries: qubits, the
  Bloch sphere, tensor products, unitary gates, measurement and the Born rule, the circuit model, universal gate sets
  and the Solovay-Kitaev theorem, reversible computation and uncomputation, entanglement, Bell's theorem and the CHSH
  inequality, the no-cloning theorem, teleportation and superdense coding, the oracle problems of Deutsch and Jozsa,
  Bernstein and Vazirani and Simon, the quantum Fourier transform and phase estimation, density matrices, channels,
  trace distance, fidelity and entropy, the stabilizer formalism and the Gottesman-Knill theorem, and error
  correction with the Shor and Steane codes and the threshold theorem), *Quantum search* (22 entries: Grover's
  algorithm and its optimality in the query model, amplitude amplification, search with an unknown number of
  solutions, fixed-point search, quantum counting, minimum finding and Grover adaptive search, quantum walk and
  spatial search, collision finding, element distinctness and k-distinctness, triangle finding and ordered search),
  *Quantum number theory* (23 entries: order finding, modular exponentiation and continued fractions, Shor's
  algorithm and the reduction of factoring to order finding, discrete logarithms in finite fields and on elliptic
  curves, short discrete logarithms and the Ekerå-Håstad algorithm, Regev's factoring algorithm, resource estimates
  for factoring, Hallgren's algorithm for Pell's equation, unit groups, class groups and the principal ideal
  problem) and *Quantum simulation* (42 entries: Feynman's proposal and Lloyd's universal simulator, Lie-Trotter and
  Trotter-Suzuki product formulas and their commutator bounds, qDRIFT and multi-product formulas, linear combinations
  of unitaries, truncated Taylor series, block encodings, quantum signal processing, qubitization and the quantum
  eigenvalue transformation, optimal and sparse Hamiltonian simulation, the no-fast-forwarding theorem and
  Lieb-Robinson bounds, the Jordan-Wigner and Bravyi-Kitaev mappings, ground-state and Gibbs-state preparation,
  energy estimation, variational eigensolvers and imaginary-time evolution, and simulation in chemistry, many-body
  physics and field theory). Every page uses the same qubit order, and says which results are proved, in the query
  or the gate model, and which costs are only estimated for a hardware model.
- **Volume 0, Guide and Index**, covers the whole set of 8,112 entries and has a new learning path, *Quantum*.
- **Volumes 1 to 29** have the same entries under the same numbers as in 0.28.0. The entries of Volumes 27 and 28
  and of Chapter 29.2 have the corrections that the site made in its release v0.29.0. Cross-references from earlier
  volumes to entries of Volume 30 now give entry numbers. The site has added seven areas before Complexity, which is
  now Volume 38; the learner pages that named it as Volume 31 now say Volume 38.
- Volumes 31 to 38 (CAD, Statistics and inference, Compilers and program analysis, Information retrieval and AI
  reasoning, Control, Robotics, Computer vision, Complexity) are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.29.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
