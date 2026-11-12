The Handbook of Algorithms, edition 0.24.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.24.0](https://github.com/tamnd/algorithm/releases/tag/v0.24.0)
(`e372c96a957d135ad6bb300fc11ee50f64e66aa3`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,258 |
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
| 12 | Numerical | 465 | 3,022 |
| 13 | Geometry | 280 | 1,794 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,764 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,311 |
| 19 | Online and streaming | 195 | 1,135 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 390 | 3,136 |
| 24 | Compression and coding | 220 | 1,741 |
| 25 | Machine learning | 419 | 2,978 |
| 26 | Systems | 53 | 409 |
| | **All** | **6,707** | **45,092** |

- **New in this edition: Volume 25, Machine learning**, in six chapters: supervised learning (empirical risk
  minimization, PAC learning and the VC dimension, linear and logistic regression, support vector machines and
  kernels, decision trees, bagging, random forests and boosting), clustering (k-means and k-means++, hierarchical
  and density-based clustering, spectral clustering, mixture models, validity indices and the hardness results),
  dimensionality reduction (principal component analysis and its variants, random projections and the
  Johnson-Lindenstrauss lemma, multidimensional scaling, manifold learning, t-SNE and UMAP), neural network training
  (backpropagation and automatic differentiation, initialization, normalization, regularization and the adaptive
  optimizers), probabilistic inference (Bayesian networks and Markov random fields, variable elimination, belief
  propagation and the junction tree, hidden Markov models, Kalman and particle filters, variational inference) and
  reinforcement learning (bandits, Markov decision processes, dynamic programming, temporal-difference learning,
  Q-learning, policy gradients and actor-critic methods). Each method names its model, and each guarantee says
  whether it holds for all inputs, with high probability or only in the limit.
- **New: Volume 26, Systems**, with its first chapter, *Caching policies* (53 entries: Belady's optimal policy and the
  competitive ratio of LRU, LRU, LFU, ARC, CLOCK, LIRS, S3-FIFO and their relatives, admission by TinyLFU, stack
  algorithms and miss-ratio curves, write policies and the cache patterns of applications). Chapters 26.2 to 26.8
  have an opening only, until the site writes their entries.
- **Volume 0, Guide and Index**, covers the whole set of 6,707 entries and has a new learning path,
  *Machine learning*.
- **Volumes 1 to 24** have the same entries under the same numbers as in 0.23.0; their cross-references to entries
  of Volumes 25 and 26 (logistic regression, belief propagation, the Viterbi algorithm, LRU and others) now give
  entry numbers.
- Volumes 27 to 31 are forthcoming; Volume 0 lists their chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.24.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
