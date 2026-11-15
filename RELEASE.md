The Handbook of Algorithms, edition 0.31.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.31.0](https://github.com/tamnd/algorithm/releases/tag/v0.31.0)
(`2fee836256011b570948813cd7da43bef0d8c42e`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 1,664 |
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
| 33 | Statistics and inference | 276 | 2,168 |
| | **All** | **8,661** | **60,105** |

- **New in this edition: Volume 33, Statistics and inference**, with all eight of its chapters written: *Point
  estimation* (33 entries: bias, variance and mean squared error, one-pass and parallel variance by Welford's method,
  likelihood and Fisher information, sufficiency and the Rao-Blackwell and Lehmann-Scheffé theorems, consistency and
  asymptotic normality of the maximum likelihood estimator, the delta method, estimating equations and the
  generalized method of moments, shrinkage and the James-Stein estimator, and survey sampling with the
  Horvitz-Thompson estimator), *Hypothesis testing and intervals* (45 entries: errors and p-values, confidence sets
  and their duality with tests, tests on normal means, intervals for proportions, the Neyman-Pearson lemma, the
  likelihood ratio test and Wilks' theorem, family-wise error control by Bonferroni, Holm and Hochberg, and the false
  discovery rate, q-values and e-values), *Nonparametric, resampling and robust methods* (44 entries: the empirical
  distribution, the bootstrap and the jackknife, rank and permutation tests, the influence function and the breakdown
  point, M-estimators, trimmed means and the median of absolute deviations, robust regression by least median of
  squares and others, robust multivariate estimation and the Tukey median, kernel smoothing, and conformal
  prediction), *Regression and diagnostics* (31 entries: least squares and the F-test, model selection, leverage and
  influence, tests of the error assumptions such as Breusch-Pagan, heteroskedasticity-consistent errors, correlated
  errors and mixed models, iteratively reweighted least squares, quasi-likelihood and generalized estimating
  equations, and inference after selection), *Bayesian statistics* (29 entries: posterior summaries and credible
  intervals, priors and the Bernstein-von Mises theorem, hierarchical models, Bayes factors and the Lindley paradox,
  sparse priors, marginal likelihoods, approximate Bayesian computation, and posterior predictive checks and
  simulation-based calibration), *Time series and sequential analysis* (35 entries: stationary and ARMA processes,
  fitting by the Yule-Walker equations, the innovations algorithm and the Whittle likelihood, trends and seasons,
  vector autoregressions, unit-root tests and cointegration, the sequential probability ratio test and group
  sequential trials, change-point detection by CUSUM and PELT, and anytime-valid inference with confidence
  sequences), *Causal inference and design of experiments* (41 entries: potential outcomes, randomized experiments,
  factorial and fractional designs, optimal design and the Fedorov exchange algorithm, propensity scores and
  matching, doubly robust and double machine learning estimators, instrumental variables, regression discontinuity
  and synthetic control, and causal graphs and their discovery) and *Survival analysis* (18 entries: censoring, the
  Kaplan-Meier and Nelson-Aalen estimators, the log-rank test, the Cox model, accelerated failure time models, and
  competing risks with the Fine-Gray model). The pages say which guarantees are exact, which are asymptotic, and
  which are only measured by simulation.
- **Volume 0, Guide and Index**, covers the whole set of 8,661 entries. It has a new learning path, *Statistics and
  inference*, in seven stages.
- **Volumes 1 to 32** have the same entries under the same numbers as in 0.30.0. The entries of the written chapters
  of Volumes 31 and 32 have the corrections that the site made in its release v0.31.0. Cross-references from earlier
  volumes to entries of Volume 33 now give entry numbers. In the EPUB of Volume 24, a formula that showed as TeX
  source is now rendered.
- Volumes 34 to 39 (Compilers and program analysis, Information retrieval and AI reasoning, Control, Robotics,
  Computer vision, Complexity) are forthcoming; Volume 0 lists their chapters. The remaining chapters of Volumes 31
  and 32 are still openings only.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.31.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by AI agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
