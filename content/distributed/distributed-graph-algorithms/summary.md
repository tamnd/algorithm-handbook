## What to remember

- In the [LOCAL model](/local-model/) an $r$-round algorithm is a map from radius-$r$ balls to outputs, so every solvable problem takes at most $D + 1$ rounds. [CONGEST](/congest-model/) allows $O(\log n)$ bits per edge per round.
- [Flooding](/flooding/) sends exactly $2m - n + 1$ messages and reaches a node at distance $d$ in round $d$. The [echo algorithm](/echo-algorithm/) sends exactly $2m$, and the source knows that it is done in round $2e$ or $2e + 1$. In KT0 every deterministic broadcast sends at least $m$ messages.
- [Cole-Vishkin](/cole-vishkin/) 3-colours an oriented ring in exactly $T(N) + 3 \le \log^* N + 3$ rounds. [Linial's bound](/linial-coloring-lower-bound/) says that $\frac12 \log^* n - 1$ rounds are needed, and [Linial's algorithm](/linial-algorithm/) gives $O(\Delta^2)$ colours on any graph in $\log^* N + O(1)$ rounds.
- A $k$-colouring gives an [MIS](/distributed-mis/) in $k$ more rounds. [Luby's algorithm](/luby-mis/) finds one in $O(\log n)$ rounds with high probability. The [KMW bound](/kmw-lower-bound/) shows that MIS, maximal matching and every polylogarithmic approximation of vertex cover need $\Omega(\min(\log\Delta/\log\log\Delta, \sqrt{\log n/\log\log n}))$ rounds.
- On cycles, every [locally checkable problem](/locally-checkable-labeling/) takes $O(1)$, $\Theta(\log^* n)$ or $\Theta(n)$ rounds. [Sinkless orientation](/sinkless-orientation/) takes $\Theta(\log n)$ rounds deterministically and $\Theta(\log\log n)$ with randomness, an exponential gap.
- A [network decomposition](/network-decomposition/) with $C$ colours and cluster diameter $D$ gives an MIS in $O(CD)$ rounds. A $\mathrm{poly}(\log n)$ decomposition makes every polylogarithmic randomized LCL algorithm deterministic with polylogarithmic rounds.
- [MST](/distributed-mst/) in CONGEST takes $\tilde O(D + \sqrt n)$ rounds with $\tilde O(m)$ messages, and the [Peleg-Rubinovich bound](/peleg-rubinovich-lower-bound/) of $\Omega(D + \sqrt n/\log n)$ shows that this is near optimal. SSSP, min cut and max flow meet the same barrier. [GHS](/gallager-humblet-spira/) sends at most $5n\log_2 n + 2m$ messages.
- Unweighted all-pairs distances and the [diameter](/distributed-diameter/) need about $n$ rounds. [Pipelined BFS](/distributed-apsp/) gives $O(n)$, and the [diameter lower bound](/diameter-lower-bound-distributed/) is $\Omega(n/B)$. [Bellman-Ford](/distributed-bellman-ford/) finds single-source distances within $n - 1$ rounds.

## Bounds side by side

| Problem | Model | Upper bound | Lower bound |
|---|---|---|---|
| [Broadcast](/broadcast-problem/) | any timing, KT0 | flooding: $2m - n + 1$ messages, $e$ or $e+1$ rounds | $m$ messages (deterministic), $e$ rounds |
| 3-colouring an oriented ring | LOCAL | $\lceil T(N)/2\rceil + 3$ | $\frac12\log^* n - 1$ |
| [$(\Delta+1)$-colouring](/distributed-vertex-coloring/) | LOCAL | $O(\Delta) + \log^* n$; $\tilde O(\log^2 n)$; randomized $\tilde O(\log^2\log n)$ | $\Omega(\log^* n)$ |
| MIS | LOCAL | randomized $O(\log n)$; $\tilde O(\log^{5/3} n)$ | KMW; deterministic $\Omega(\min(\Delta, \log n/\log\log n))$ |
| [Maximal matching](/distributed-maximal-matching/) | LOCAL | randomized $O(\log n)$; $O(\Delta + \log^* n)$ | KMW |
| Sinkless orientation | LOCAL | $O(\log n)$; randomized $O(\log\log n)$ | the same |
| [Vertex cover](/distributed-minimum-vertex-cover/), ratio $2+\varepsilon$ | LOCAL | $O(\log\Delta/(\varepsilon\log\log\Delta))$ | KMW |
| MST | CONGEST | $\tilde O(D + \sqrt n)$ rounds, $\tilde O(m)$ messages | $\Omega(D + \sqrt n/\log n)$ |
| MST | [congested clique](/congested-clique-model/) | randomized $O(1)$; $O(\log\log n)$ | none above a constant known |
| Exact SSSP | CONGEST | $\tilde O(n^{2/5+o(1)}D^{2/5} + \sqrt n + D)$ | $\Omega(\sqrt n/\log n + D)$, even approximate |
| Exact diameter | CONGEST | $O(n)$ | $\Omega(n/\log n)$ |
| [Exact min cut](/distributed-min-cut/) | CONGEST | $\tilde O(\sqrt n + D)$ | $\tilde\Omega(\sqrt n + D)$ |
| [Triangle listing](/distributed-triangle-enumeration/) | CONGEST, clique | $\tilde O(n^{1/3})$; clique $O(n^{1/3}/\log n)$ | $\Omega(n^{1/3}/\log n)$ |

: Rounds unless stated. $n$ nodes, $m$ edges, diameter $D$, eccentricity $e$ of the source, maximum degree $\Delta$, identifiers below $N$. "KMW" stands for $\Omega(\min(\log\Delta/\log\log\Delta, \sqrt{\log n/\log\log n}))$. Upper bounds are deterministic unless marked randomized.

## Choosing a method

For one broadcast with no structure known, flood. If the source must know when it is done, or must collect a sum or a count, use echo, which costs $n - 1$ messages more. If many broadcasts follow, build a [BFS tree](/breadth-first-search-distributed/) once and send on its $n - 1$ edges. On an asynchronous network, run a synchronous algorithm under [synchronizer](/synchronizer/) α when time matters and under β when messages do.

For symmetry breaking on a ring or a rooted tree, use Cole-Vishkin. On a bounded-degree graph, use Linial's algorithm, then remove one colour class per round, and use the colours to get an MIS or a matching. When $\Delta$ is large, random colour trials or Luby's algorithm take $O(\log n)$ rounds.

For global problems in CONGEST, first compare $D$ with $\sqrt n$. When $D \ge \sqrt n$, Bellman-Ford, BFS and Borůvka-style merging are already near optimal. When $D$ is small, the $\tilde O(D + \sqrt n)$ algorithms for MST, connectivity and min cut win, and on planar graphs [low-congestion shortcuts](/low-congestion-shortcuts/) bring MST down to $\tilde O(D)$. If every pair or the exact diameter is needed, expect about $n$ rounds.
