## What to remember

- **Every ratio proof compares the answer with a computable bound on OPT**, a lower bound when minimizing and an upper bound when maximizing. For [bin packing](/bin-packing/) it is the total size; for covering problems, the [LP relaxation](/lp-relaxation/) or any feasible dual, by [weak duality](/weak-duality/); for [k-center](/k-center-problem/), $k + 1$ points that are far apart.
- **Bin packing has absolute and asymptotic ratios.** No algorithm has absolute ratio below $3/2$ unless P = NP, yet the [asymptotic scheme](/bin-packing-aptas/) uses at most $(1 + \varepsilon)\text{OPT} + 1$ bins.
- **Set cover: greedy gives $H_d$, primal-dual gives $f$.** [Greedy](/greedy-set-cover/) costs at most $H_d \cdot \text{OPT}$, where $d$ is the largest set size, and $(1 - \varepsilon)\ln n$ is NP-hard. The [primal-dual algorithm](/set-cover-primal-dual/) costs at most $f \cdot \text{OPT}$, where $f$ is the largest [element frequency](/element-frequency/).
- **Greedy coverage reaches $1 - (1 - 1/k)^k > 1 - 1/e$ of OPT**, and nothing better is possible for [maximum coverage](/max-coverage/) unless P = NP. The [Nemhauser-Wolsey-Fisher theorem](/nemhauser-wolsey-fisher-theorem/) gives the same bound for every monotone submodular function.
- **Vertex cover has ratio 2 by four routes**: a [maximal matching](/vertex-cover-2-approximation/), LP rounding at $1/2$, the [primal-dual algorithm](/primal-dual-weighted-vertex-cover/) and local ratio; the last three allow weights. Ratio $\sqrt 2 - \varepsilon$ is NP-hard, and $2 - \varepsilon$ is hard under the Unique Games Conjecture.
- **Primal-dual in one line.** If every bought item is tight and every raised dual variable meets at most $\beta$ bought items, then $c(A) \le \beta \sum y \le \beta \cdot \text{OPT}$. The [local ratio technique](/local-ratio-technique/) gives the same algorithms by splitting the weights.
- **Independent set and cut.** The [minimum-degree greedy](/greedy-independent-set/) finds an independent set of at least the [Caro-Wei](/caro-wei-theorem/) size $\sum_v 1/(\deg v + 1)$. A random cut, greedy placement and local search each cut at least half of the edge weight, so each is a $1/2$-approximation for [maximum cut](/maximum-cut/).
- **k-center has ratio 2, and no better** unless P = NP, by a reduction from [dominating set](/dominating-set/).
- **Integer programs.** Randomized rounding gives $O(\log m)$ for a [covering integer program](/covering-integer-program/) and $O(m^{1/B})$ for a [packing integer program](/packing-integer-program/), with $m$ constraints and least right side $B$.

## The main algorithms side by side

| Algorithm | Problem | Ratio | Bound on OPT | Time |
|---|---|---|---|---|
| Next fit | bin packing | $2\,\text{OPT} - 1$ | $\lceil S \rceil$ | $\Theta(n)$ |
| First fit, best fit | bin packing | $\lfloor 1.7\,\text{OPT} \rfloor$ | weight function | $\Theta(n \log n)$ |
| First fit decreasing | bin packing | $\frac{11}{9}\text{OPT} + \frac69$, and $\frac32\text{OPT}$ | sizes, large items | $\Theta(n \log n)$ |
| Greedy set cover | set cover | $H_d$ | dual fitting | $O(n + s \log m)$ |
| Primal-dual set cover | set cover | $f$ | feasible dual | $\Theta(n + m + s)$ |
| Greedy maximum coverage | maximum coverage | $1 - (1 - 1/k)^k$ of OPT | gains of an optimal family | $O(k(m + s))$ |
| Maximal matching | vertex cover | 2 | matching size | $\Theta(n + m)$ |
| Primal-dual vertex cover | weighted vertex cover | 2 | feasible dual | $\Theta(n + m)$ |
| Minimum-degree greedy | independent set | $(\Delta + 2)/3$ | counting | $O((n + m) \log n)$ |
| Random cut, greedy placement | maximum cut | $1/2$ of OPT | total weight | $O(n + m)$ |
| Farthest-first traversal | k-center | 2 | $k + 1$ far-apart points | $\Theta(nk)$ |

: Worst-case ratios. Bin packing has $n$ items; set cover and coverage have $n$ elements, $m$ sets and total size $s$; graphs have $n$ vertices and $m$ edges. The random cut reaches $1/2$ in expectation.

## Choosing a method

- For bin packing with the whole list known, use first fit decreasing. Online, use first fit or best fit, or next fit when only one bin may stay open. For many copies of a few sizes, use the [cutting stock](/cutting-stock-problem/) model.
- For set cover, compute $d$ and $f$. When each element lies in few sets, use primal-dual with a reverse delete pass; otherwise use greedy.
- To choose $k$ items under a coverage or diminishing-returns objective, use lazy greedy. One run serves every budget up to $k$.
- For weighted vertex cover, primal-dual runs in linear time and returns a lower bound with its answer. On a bipartite graph, a minimum cut solves the problem exactly.
- For $k$-center, use farthest-first traversal, but watch for outliers: the farthest point always becomes a centre.
- When a covering or packing LP has large right sides, round it at random; when they are 1, expect large losses.
