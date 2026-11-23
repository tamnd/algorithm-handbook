## What to remember

- A mechanism $M$ is $(\varepsilon, \delta)$-DP if $P[M(x) \in S] \le e^{\varepsilon} P[M(x') \in S] + \delta$ for all neighbors $x, x'$ and all sets $S$. The guarantee is about the mechanism, not one output, and it depends on the neighbor relation: $\varepsilon$ under add/remove gives $2\varepsilon$ under replace. The slack $\delta$ must be much smaller than $1/n$, since releasing each record with probability $\delta$ is $(0, \delta)$-DP.
- Noise is scaled to sensitivity: $\mathrm{Lap}(\Delta_1/\varepsilon)$ gives $\varepsilon$-DP, and the Gaussian mechanism uses $\Delta_2$. The classical $\sigma = \Delta_2\sqrt{2\ln(1.25/\delta)}/\varepsilon$ is proved only for $\varepsilon < 1$; the analytic calibration of Balle and Wang is exact for every $\varepsilon$.
- Post-processing never costs privacy. A group of $k$ records costs $k\varepsilon$ for pure DP, and the slack grows to $\delta(e^{k\varepsilon} - 1)/(e^{\varepsilon} - 1)$, which is exact.
- Basic composition adds the parameters, parallel composition on a partition fixed in advance takes the largest, and advanced composition gives about $\varepsilon\sqrt{2k\ln(1/\delta')}$. All three are upper bounds; the optimal composition theorem gives the exact value for $k$ uses of one mechanism, and computing it in general is #P-complete.
- Rényi DP, zCDP and the moments accountant compose by addition and convert to $(\varepsilon, \delta)$ once, at the end; numerical accounting computes the composed profile with stated error bounds. For 100 Gaussian queries of sensitivity 1 and $\sigma = 10$ at $\delta = 10^{-6}$, zCDP gives $\varepsilon \approx 5.76$ and the exact value is about 4.89.
- The exponential mechanism and report noisy max choose among candidates at the cost of one answer, and the sparse vector technique pays only for the answers above the threshold. Small changes to these algorithms, such as publishing the noisy value, break privacy.
- In the local model each user randomizes alone. Randomized response estimates a fraction with error about $1/(\varepsilon\sqrt n)$, against about $1/(\varepsilon n)$ for a trusted curator. Shuffling and subsampling amplify privacy, but only under their stated hypotheses.
- Lower bounds hold for every private mechanism: answers to about $n$ random subset sums with error $o(\sqrt n)$ rebuild almost all the bits, pure DP pays an error $\Omega(\log|X|/(\varepsilon n))$ by packing, and fingerprinting codes give $\Omega(\sqrt{d\log(1/\delta)}/(\varepsilon n))$ for $d$ attribute means when $\delta$ is in the stated range.

## The mechanisms side by side

| Mechanism | Output | Noise or rule | Guarantee in the entry |
|---|---|---|---|
| [Laplace](/laplace-mechanism/) | real vector | $\mathrm{Lap}(\Delta_1/\varepsilon)$ each coordinate | $\varepsilon$-DP |
| [Geometric](/geometric-mechanism/) | integer | $P(Z = d) \propto e^{-\varepsilon\lvert d\rvert}$ | $\varepsilon$-DP; optimal for one count |
| [Gaussian](/gaussian-mechanism/) | real vector | $N(0, \sigma^2)$ with $\sigma$ from $\Delta_2$ | $(\varepsilon, \delta)$-DP; classical $\sigma$ for $\varepsilon < 1$ |
| [Discrete Gaussian](/discrete-gaussian-mechanism/) | integer vector | exact sampler | $\Delta_2^2/(2\sigma^2)$-zCDP |
| [Randomized response](/randomized-response/) | one bit per user | keep with $e^{\varepsilon}/(1+e^{\varepsilon})$ | $\varepsilon$-local DP |
| [Exponential](/exponential-mechanism/) | one candidate | weight $\exp(\varepsilon u/(2\Delta))$ | $\varepsilon$-DP |
| [Report noisy max](/report-noisy-max/) | one index | $\mathrm{Lap}(\Delta/\varepsilon)$, monotone scores | $\varepsilon$-DP |
| [Sparse vector](/sparse-vector-technique/) | $\bot$ or $\top$ per query | threshold $\mathrm{Lap}(2\Delta/\varepsilon)$, query $\mathrm{Lap}(4\Delta/\varepsilon)$ | $\varepsilon$-DP up to the first $\top$ |
| [Binary tree](/binary-tree-mechanism/) | $T$ running counts | $\mathrm{Lap}(L/\varepsilon)$ per node, $L = \lfloor\log_2 T\rfloor + 1$ | $\varepsilon$-DP, event level |
| [Propose-test-release](/propose-test-release/) | value or $\bot$ | noisy distance to instability | $(2\varepsilon, \delta/2)$-DP |
| [DP-SGD](/dp-sgd/) | model | clip to $C$, add $N(0, \sigma^2C^2)$ | the accountant's $(\varepsilon, \delta)$ for the whole run |

: Mechanisms and guarantees as the entries state them; the symbols are defined in each entry.

## Choosing a method

For one numeric query with small $\ell_1$ sensitivity, use the Laplace mechanism, or the geometric mechanism for an integer count. For many queries, or vector answers whose $\ell_2$ sensitivity is much smaller than the $\ell_1$, use the Gaussian mechanism with the analytic calibration, and track the budget with zCDP, Rényi DP or numerical accounting rather than advanced composition. To choose an item, use the exponential mechanism or report noisy max; to scan many threshold questions, use sparse vector. For running counts, use the binary tree mechanism; for a fixed workload of linear queries, the matrix mechanism; for synthetic data over a small domain, MWEM. For the median and other robust statistics, try propose-test-release or smooth sensitivity, and compare with a clamped Laplace answer. When no curator is trusted, use randomized response for one bit and optimized local hashing for a large domain, and consider a shuffler. To train a model, use DP-SGD with Poisson sampling and an accountant that matches the sampling, or PATE when public unlabeled data exist. Whatever the method, fix the neighbor relation first, use a secure noise sampler, and do not tune on the private data without counting the cost.
