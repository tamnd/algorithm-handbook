## What to remember

- **Ratios and schemes.** A minimization algorithm has ratio $\rho \ge 1$ when $\mathrm{ALG} \le \rho \cdot \mathrm{OPT}$; a maximization algorithm has ratio $\alpha \le 1$ when $\mathrm{ALG} \ge \alpha \cdot \mathrm{OPT}$. A scheme reaches $1 + \varepsilon$, or $1 - \varepsilon$, for every $\varepsilon > 0$, in time $\mathrm{poly}(|I|, 1/\varepsilon)$ for an [FPTAS](/fptas/), $f(1/\varepsilon) \cdot \mathrm{poly}(|I|)$ for an [EPTAS](/eptas/), and polynomial for each fixed $\varepsilon$ for a [PTAS](/ptas/).
- **The chain.** $\mathrm{FPTAS} \subseteq \mathrm{EPTAS} \subseteq \mathrm{PTAS} \subseteq \mathrm{APX} \subseteq \mathrm{NPO}$, where [APX](/apx/) holds the problems with a constant ratio. Each step is strict if P ≠ NP, except EPTAS ⊊ PTAS, which needs FPT ≠ W[1].
- **Rounding.** The [knapsack FPTAS](/knapsack-fptas/) divides the profits by $K = \varepsilon P / n$, with $P$ the largest profit, and rounds down. A set loses less than $nK = \varepsilon P \le \varepsilon \cdot \mathrm{OPT}$, and the [profit-indexed table](/profit-indexed-dynamic-programming/) takes $O(n^3/\varepsilon)$ time.
- **Trimming.** Keep a value of a sorted list only when it exceeds the last kept value by a factor more than $1 + \delta$. With $\delta = \varepsilon/(2n)$ the [subset sum FPTAS](/subset-sum-fptas/) returns at least $\mathrm{OPT}/(1 + \varepsilon)$ in $O(n^2 \log t / \varepsilon)$ time.
- **Where FPTAS stops.** A strongly NP-hard problem whose integer optimum is polynomial in $|I|$ and the largest number has [no FPTAS](/no-fptas-for-strongly-np-hard-problems/) unless P = NP: with $\varepsilon < 1/\mathrm{OPT}$ it would be exact. Even [multiple knapsack](/multiple-knapsack-problem/) with two knapsacks, only weakly NP-hard, has no FPTAS.
- **Large and small items.** Round the large items to a few sizes and pack them exactly; add the small ones greedily. [Dual approximation](/dual-approximation/) guesses $T$ and either returns a solution of value at most $(1 + \varepsilon) T$ or proves $\mathrm{OPT} > T$.
- **Additive terms.** Bin packing has no ratio below $3/2$ unless P = NP, yet its [asymptotic schemes](/asymptotic-ptas/) use at most $(1 + \varepsilon)\,\mathrm{OPT} + 1$ bins.
- **Shifting.** Among $\ell$ shifts of a grid, some shift meets at most a $1/\ell$ part of the optimum. This gives $(1 + 1/\ell)^d$ for covering in $d$ dimensions and, with [Baker's bands](/baker-technique/), $(1 - 1/k)\,\mathrm{OPT}$ for planar independent set in $2^{O(k)} n$ time.
- **Geometry and density.** Any network of length $L$ becomes m-guillotine after adding at most $\frac{\sqrt 2}{m} L$, and portals on a randomly shifted quadtree cost a factor $1 + \varepsilon$ in expectation. With $\delta n^2$ edges the maximum cut is at least $\delta n^2 / 2$, so an additive error of $\varepsilon \delta n^2 / 2$ is relative error $\varepsilon$.

| Scheme | Problem | Guarantee | Time |
|---|---|---|---|
| [Ibarra-Kim](/knapsack-fptas/) | knapsack | $(1 - \varepsilon)\,\mathrm{OPT}$ | $O(n^3/\varepsilon)$ |
| [Trimmed lists](/subset-sum-fptas/) | subset sum | $\mathrm{OPT}/(1 + \varepsilon)$ | $O(n^2 \log t / \varepsilon)$ |
| [Chekuri-Khanna](/chekuri-khanna-ptas/) | multiple knapsack | $(1 - \varepsilon)\,\mathrm{OPT}$ | $n^{O(\log(1/\varepsilon)/\varepsilon^8)}$ |
| [Hochbaum-Shmoys](/hochbaum-shmoys-makespan-ptas/) | makespan | $(1 + \varepsilon)\,\mathrm{OPT}$ | $O(n^{2k^2} \log P)$ |
| [Fernandez de la Vega-Lueker](/fernandez-de-la-vega-lueker-aptas/) | bin packing | $(1 + \varepsilon)\,\mathrm{OPT} + 1$ | $O(n \log n + (1/\varepsilon)^{c/\varepsilon^4})$ |
| [Baker](/baker-planar-ptas/) | planar independent set | $(1 - 1/k)\,\mathrm{OPT}$ | $2^{O(k)} n$ |
| [Borradaile-Klein-Mathieu](/planar-steiner-tree-ptas/) | planar Steiner tree | $(1 + \varepsilon)\,\mathrm{OPT}$ | $O(n \log n + f(\varepsilon)\, n)$ |
| [Mitchell](/mitchell-guillotine-ptas/) | Euclidean TSP in the plane | $(1 + \frac{2\sqrt 2}{m})\,\mathrm{OPT}$ | $n^{O(m)}$ |
| [Arora-Raghavan-Rao](/arora-euclidean-k-median-ptas/) | Euclidean $k$-median in the plane | $(1 + \varepsilon)\,\mathrm{OPT}$, expected | $n^{O(1/\varepsilon)}$ |
| [Arora-Karger-Karpinski](/dense-max-cut-ptas/) | dense max cut | $(1 - \varepsilon)\,\mathrm{OPT}$ | $O(2^{c/(\varepsilon^3 \delta^3)} n^2)$ |

: Main schemes, as stated in the entries. For Hochbaum-Shmoys $k = \lceil 1/\varepsilon \rceil$ and $P$ is the total processing time; for Baker $k$ is the band period; for Mitchell $m = \lceil 2\sqrt 2/\varepsilon \rceil$ gives $1 + \varepsilon$; $c$ is a constant and $f$ depends on $\varepsilon$ only. The last two schemes are randomized.

## Choosing a method

- If the problem has a pseudo-polynomial dynamic program, look for an FPTAS by scaling or trimming. When the numbers are small, the exact table may be cheaper.
- For a strongly NP-hard problem with small integer values, look for an EPTAS or a PTAS.
- For scheduling and packing, split the items by size and use dual approximation. When small optima make the problem hard, as in bin packing, aim for an asymptotic guarantee.
- For local problems on planar graphs, use Baker's bands; for objects of bounded size in the plane, use shifting.
- For network problems among points in the plane, the schemes of Arora and Mitchell settle what is possible; for a tour in practice, use [Christofides' algorithm](/christofides-algorithm/) or local search.
- A scheme with $1/\varepsilon$ in the exponent of $n$ shows that every constant ratio is reachable. It is not a program to run with a small $\varepsilon$.
