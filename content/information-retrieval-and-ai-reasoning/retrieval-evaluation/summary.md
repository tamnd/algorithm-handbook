## What to remember

- [Precision at k](/precision-at-k/) divides the number of relevant documents in the top $k$ by $k$, even when the run is shorter. [R-precision](/r-precision/) is precision at rank $R$, which equals recall there. [MRR](/mean-reciprocal-rank/) is the mean over queries of $1/r$ for the first relevant rank $r$, the reciprocal of the harmonic mean of the ranks.
- [Average precision](/mean-average-precision/) is $\frac{1}{R}\sum P@r$ over the ranks $r$ of the relevant documents, with 0 for those not retrieved. It is the area under the step curve of precision against recall. The [interpolated curve](/interpolated-precision-recall-curve/) is the smallest non-increasing curve above the points, so its area is at least AP.
- [nDCG](/normalized-discounted-cumulative-gain/) divides $\sum_i G(g_i)/\log_2(i + 1)$ by the same sum for the ideal ordering of all judged documents. The gains $G(g) = g$ and $2^g - 1$ can rank two runs in opposite orders.
- [RBP](/rank-biased-precision/) is $(1 - p)\sum_i r_i p^{i-1}$ for a user who reads on with probability $p$, and its residual bounds what unjudged documents can add. [ERR](/expected-reciprocal-rank/) is the expected $1/r$ at the rank where a cascade user stops, and sorting by grade maximizes it. The [C/W/L framework](/cwl-framework/) derives weights from continuation probabilities. These are user models, not measurements of users.
- Ties need a stated rule. This area orders by score, then by id ascending; trec_eval uses reverse lexical order. In the opening example the two rules give AP $29/36$ and $53/90$.
- [Pooling](/pooling/) to depth $k$ judges at most $mk$ documents for $m$ runs and counts the rest as not relevant, which can take most of the score of a run outside the pool. [Bpref](/bpref/) ignores unjudged documents. [Inferred AP](/inferred-average-precision/) tends to AP when the whole pool is judged, but it is not unbiased under sampling. A [minimal test collection](/minimal-test-collection/) stops when the sign of $\mathrm{AP}(A) - \mathrm{AP}(B)$ holds for every relevance of the unjudged documents.
- A difference in mean score is not a result until a paired test says so: with the [sign test](/sign-test/), 60 wins against 40 in 100 topics gives $p = 0.0569$.
- [Balanced interleaving](/balanced-interleaving/) can prefer a ranking under random clicks. [Team draft](/team-draft-interleaving/) is fair but can miss a better ranking. [Probabilistic interleaving](/probabilistic-interleaving/) is fair, and its marginalized credit is unbiased when clicks do not see the hidden assignment.

| Metric | Judgments | Weight of rank $i$ | Normalization | Unjudged documents |
|---|---|---|---|---|
| Precision at k | binary | $1/k$ for $i \le k$ | in $[0, 1]$ | not relevant |
| R-precision | binary | $1/R$ for $i \le R$ | in $[0, 1]$ | not relevant |
| Reciprocal rank | binary | first relevant rank only | in $[0, 1]$ | not relevant |
| Average precision | binary | precision at each relevant rank, over $R$ | in $[0, 1]$ | not relevant |
| nDCG | graded | $G(g_i)/\log_2(i + 1)$ | by the ideal ordering | gain 0 |
| RBP | binary or gain in $[0, 1]$ | $(1 - p)p^{i-1}$ | in $[0, 1]$ | residual interval |
| ERR | graded | stop probability times $1/i$ | below 1 | grade 0 |
| Alpha-nDCG | nuggets | $(1 - \alpha)^c$ per nugget, over $\log_2(i + 1)$ | by a greedy ideal, can exceed 1 | no nugget |
| Bpref | binary | judged nonrelevant documents above each relevant one | over $R$ | ignored |
| Inferred AP | sampled | estimated precision at sampled relevant ranks | over $R_S$ | estimated |

: The offline metrics. $R$ is the number of relevant documents, $g_i$ the grade at rank $i$, $c$ the number of earlier documents with the same nugget and $R_S$ the number of sampled relevant documents.

## Choosing a metric

If the user wants one answer, as in question answering, use MRR, or ERR with graded judgments. For a results page with graded judgments, use nDCG or ERR at 10. For recall-oriented search, such as legal or patent search, use MAP and R-precision. Always state the gain, the cutoff, the tie rule and how queries with $R = 0$ count.

With incomplete judgments, report RBP with its residual, or bpref or inferred AP, and count how many of a new run's top documents were never judged. To compare two runs with few judgments, use a minimal test collection. To compare two live rankers, use team-draft or probabilistic interleaving and a sign test over many queries. With many systems, correct for [multiple comparisons](/multiple-comparisons-problem/).
