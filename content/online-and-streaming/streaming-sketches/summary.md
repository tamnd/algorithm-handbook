## What to remember

- A [streaming algorithm](/streaming-model/) reads the input once and keeps a summary of polylogarithmic size of the [frequency vector](/frequency-vector/) $f$. In the [turnstile model](/turnstile-model/) counts can go down; summaries that store items then fail, and a [linear sketch](/linear-sketch/) $Sf$ still works.
- An estimator with variance $\sigma^2$ gives an [(ε, δ) guarantee](/epsilon-delta-guarantee/) from $\lceil \sigma^2/(\varepsilon^2\delta) \rceil$ averaged copies. The [median trick](/median-trick/) is cheaper: if each copy fails with probability $p < 1/2$, the median of $t$ copies fails with probability at most $(4p(1-p))^{t/2}$, so $t = O(\log(1/\delta))$.
- [Misra-Gries](/misra-gries-summary/) with $k - 1$ counters gives $f_x - m/k \le \hat f_x \le f_x$ for every item, deterministically. [Space-Saving](/space-saving/) with $k$ counters is the same summary shifted up, with $f_x \le \hat f_x \le f_x + m/k$. Both are [mergeable](/mergeable-summaries/).
- The [count-min sketch](/count-min-sketch/) with $w = \lceil e/\varepsilon \rceil$ and $d = \lceil \ln(1/\delta) \rceil$ gives $f_x \le \hat f_x \le f_x + \varepsilon\|f\|_1$ with probability $1 - \delta$ when no count is negative. The [count sketch](/count-sketch/) gives error $\varepsilon\|f\|_2$ in both directions.
- The [AMS sketch](/ams-sketch/) uses $Z = \sum_i s(i) f_i$ with 4-wise independent signs: $\mathbb{E}[Z^2] = F_2$ and $\mathrm{Var}(Z^2) \le 2F_2^2$. [Stable laws](/indyk-p-stable-sketch/) extend this to $F_p$ for $0 < p \le 2$, while $F_p$ for $p > 2$ needs $n^{1 - 2/p}$ space.
- [HyperLogLog](/hyperloglog/) keeps $m$ registers of $O(\log\log n)$ bits and returns $\alpha_m m^2 / \sum_j 2^{-M[j]}$, with a relative error of about $1.04/\sqrt m$. Every $(1 \pm \varepsilon)$ distinct counter needs $\Omega(\varepsilon^{-2} + \log n)$ bits.
- A [quantile summary](/quantile-summary-problem/) answers ranks within $\varepsilon n$. [Greenwald-Khanna](/greenwald-khanna-summary/) uses $O((1/\varepsilon)\log(\varepsilon n))$ words, optimal for deterministic comparison-based summaries, and [KLL](/kll-sketch/) uses $O((1/\varepsilon)\log\log(1/\delta))$ items, optimal for randomized ones.
- The memory of a one-pass algorithm is a one-way message, and by the [INDEX bound](/index-problem-lower-bound/) it needs $(1 - H_2(\delta))\,n$ bits, so the exact median and similar exact answers need $\Omega(n)$ bits.
- [L0 samplers](/l0-sampler/) of $O(\log^2 n\log(1/\delta))$ bits, added over the vertices of a set, return an edge that leaves the set. The [AGM sketch](/agm-graph-sketch/) uses this to find a spanning forest of a dynamic graph in $O(n\log^3 n)$ bits, which is optimal.

## The main summaries

| problem | summary | stream | space | guarantee |
|---|---|---|---|---|
| majority | [Boyer-Moore](/boyer-moore-majority/) | insertions | 2 words | the candidate, checked in a second pass |
| count to $n$ | [Morris counter](/morris-counter/) | insertions | $O(\log\log n)$ bits | variance $n(n-1)/2$ per copy |
| frequent items | Misra-Gries | insertions | $k - 1$ counters | low by at most $m/k$ |
| frequent items | Space-Saving | insertions | $k$ counters | high by at most $m/k$ |
| point counts | count-min | strict turnstile | $\lceil e/\varepsilon \rceil \cdot \lceil \ln(1/\delta) \rceil$ counters | high by at most $\varepsilon\|f\|_1$ |
| point counts | count sketch | turnstile | $O(\varepsilon^{-2}\log(1/\delta))$ counters | within $\varepsilon\|f\|_2$ |
| $F_2$ | AMS | turnstile | $O(\varepsilon^{-2}\log(1/\delta))$ counters | $(1 \pm \varepsilon) F_2$ |
| distinct items | HyperLogLog | insertions | $m$ registers of 5 bits | about $1.04/\sqrt m$ |
| distinct items | [KMV](/kmv-sketch/) | insertions | $k$ hash values | below $1/\sqrt{k-2}$ |
| quantiles | Greenwald-Khanna | insertions | $O((1/\varepsilon)\log(\varepsilon n))$ words | deterministic, $\varepsilon n$ |
| quantiles | [q-digest](/q-digest/) | insertions of integers | at most $4\lceil \log_2 U/\varepsilon \rceil$ nodes | deterministic, $\varepsilon n$ |
| quantiles | KLL | insertions | $O((1/\varepsilon)\log\log(1/\delta))$ items | $\varepsilon n$ with probability $1 - \delta$ |
| spanning forest | AGM | dynamic graph | $O(n\log^3 n)$ bits | correct with high probability |

: The main summaries. Randomized rows fail with probability $\delta$; for HyperLogLog and KMV the error is a relative standard error.

## Choosing a summary

Start from the stream model. With insertions only, the counter summaries are simple and deterministic: Space-Saving for top items and their counts, Misra-Gries when estimates must never be too high. With deletions, use a linear sketch: count-min for counts when no count goes negative, the count sketch when some can, and the AMS or a stable sketch for norms.

For distinct counts, HyperLogLog is the default, with [HyperLogLog++](/hyperloglog-plus-plus/) when many counts are small. Use KMV for intersections and set similarity. For quantiles, KLL is small and mergeable, Greenwald-Khanna is deterministic, and the q-digest suits integer keys spread over many machines. The [t-digest](/t-digest/) is accurate at the tails on most data, but it has no worst-case bound.

If summaries are built on many machines, check that the summary is mergeable and that all machines share the hash seeds. If the answer must be exact, the lower bounds say no small summary exists: store the data.
