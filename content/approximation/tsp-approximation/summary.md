## What to remember

- **Every ratio rests on a lower bound on OPT.** A [minimum spanning tree](/mst-lower-bound-for-tsp/) costs at most $(1 - 1/n)\,\text{OPT}$; a minimum perfect matching on an even set of cities costs at most $\text{OPT}/2$; the [subtour LP](/subtour-elimination-lp/) lies between the tree bound and OPT.
- **The triangle inequality makes shortcuts free.** Without it no ratio is possible unless P = NP. With it, no ratio below $123/122$ is possible unless P = NP.
- **Tree tours give 2 and $3/2$, and both are tight.** The [double tree](/double-tree-algorithm/) pays for every tree edge twice. [Christofides](/christofides-algorithm/) pays once for the tree and once for a matching on its odd vertices. The [Karlin-Klein-Oveis Gharan algorithm](/karlin-klein-oveis-gharan-algorithm/) reaches $3/2 - 10^{-36}$ in expectation.
- **Construction rules differ more in theory than in practice.** [Nearest](/nearest-insertion/) and [cheapest insertion](/cheapest-insertion/) have ratio $2(1 - 1/n)$, tight. [Nearest neighbour](/nearest-neighbor-tsp/) and [greedy edge](/greedy-edge-heuristic/) have ratio $\Theta(\log n)$. [Farthest insertion](/farthest-insertion/) has only the bound $\lceil \lg n \rceil + 1$ and a lower bound of 6.5, yet it gives the shortest tours of the five on random points.
- **Local search has a poor worst case and a good average.** A [2-optimal](/two-opt/) tour is within $O(\sqrt{n})$ of OPT, and the search can take exponentially many moves. On random instances Johnson and McGeoch measured about 5 percent above the Held-Karp bound for 2-opt, 3 percent for 3-opt and 2 percent for [Lin-Kernighan](/lin-kernighan/).
- **The [Held-Karp bound](/held-karp-bound/) equals the subtour LP** and is computed with 1-trees and degree penalties. The integrality gap of the LP is at least $4/3$ and below $3/2$.
- **Points in the plane admit a PTAS.** The schemes of [Arora](/arora-euclidean-tsp-ptas/) and [Mitchell](/mitchell-euclidean-tsp-ptas/) reach $1 + \varepsilon$ for each fixed $\varepsilon > 0$; no FPTAS exists unless P = NP.
- **Direction changes everything.** For the [asymmetric TSP](/asymmetric-tsp/), cycle covers give $\log_2 n$, [thin trees](/asadpour-atsp-algorithm/) give $O(\log n / \log\log n)$, and constant ratios came only in 2018, now $22 + \varepsilon$.
- **For the [bottleneck TSP](/bottleneck-tsp/) the ratio 2 is best possible.** The lower bound is the least threshold at which the cheap edges form a biconnected graph.

## The main algorithms side by side

| Algorithm | Problem | Ratio | Bound on OPT | Time |
|---|---|---|---|---|
| Nearest neighbour | metric | $\frac12(\lceil \lg n \rceil + 1)$ | tours of subsets | $\Theta(n^2)$ |
| Greedy edge | metric | $\frac12(\lceil \lg n \rceil + 1)$ | tours of subsets | $\Theta(n^2 \log n)$ |
| Nearest insertion | metric | $2(1 - 1/n)$ | MST | $\Theta(n^2)$ |
| Cheapest insertion | metric | $2(1 - 1/n)$ | MST | $\Theta(n^3)$ |
| Farthest insertion | metric | $\lceil \lg n \rceil + 1$ | tours of subsets | $\Theta(n^2)$ |
| Double tree, preorder walk | metric | $2(1 - 1/n)$ | MST | $\Theta(n^2)$ |
| Christofides | metric | $3/2$ | MST and matching | $O(n^3)$ |
| Karlin-Klein-Oveis Gharan | metric | $3/2 - 10^{-36}$ | subtour LP | polynomial |
| 2-opt local optimum | metric | $O(\sqrt{n})$ | $i$-th longest edge | $\Theta(n^2)$ per pass |
| Space-filling curve | Euclidean plane | $O(\log n)$ | dyadic squares | $\Theta(n \log n)$ |
| Arora | Euclidean plane | $1 + 1/c$ | structure theorem | $n (\log n)^{O(c)}$ |
| Mitchell | Euclidean plane | $1 + O(1/m)$ | guillotine graphs | $n^{O(m)}$ |
| Repeated cycle cover | asymmetric | $\lfloor \log_2 n \rfloor$ | cycle cover | $O(n^3)$ |
| Asadpour and others | asymmetric | $O(\log n / \log\log n)$ | ATSP LP | polynomial |
| Parker-Rardin | metric bottleneck | 2 | biconnected threshold | $O(n^2 \log n)$ |

: Worst-case ratios on $n$ cities. Karlin-Klein-Oveis Gharan and Arora hold in expectation, Asadpour and others with high probability; $c$ and $m$ are accuracy parameters. Cheapest insertion takes $O(n^2 \log n)$ with a priority queue; 2-opt can need exponentially many passes.

## Choosing a method

- For a tour with a proof of quality, run Christofides and compute the Held-Karp bound; their quotient bounds the error on that input.
- For short tours in practice, build a start tour with greedy edge or farthest insertion and improve it with [Or-opt](/or-opt/) and 2-opt, or better with Lin-Kernighan. For the best tours on large instances, use [LKH](/lin-kernighan-helsgaun/).
- For millions of points in the plane, sort them along a [space-filling curve](/space-filling-curve-tsp/) and start a local search from that order.
- When the costs depend on direction, do not make them symmetric; use a method for the asymmetric problem. When only the longest leg matters, use the [threshold algorithm](/bottleneck-tsp-approximation/).
- Up to about 20 cities, solve exactly with the [Held-Karp dynamic program](/held-karp-algorithm/).
