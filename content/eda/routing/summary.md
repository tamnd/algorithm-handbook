## What to remember

- [Lee's algorithm](/lee-maze-routing/) is breadth-first search on the grid: for one two-pin net it finds a shortest path whenever one exists, in $\Theta(MN)$ time on an $M \times N$ grid. [Hadlock's algorithm](/hadlock-algorithm/) is also shortest: a path with detour number $D$ has length $\mathrm{md}(s,t) + 2D$, and minimizing $D$ is a [0-1 BFS](/zero-one-bfs/). Soukup's and the line-probe routers trade the shortest path for speed.
- The [rectilinear minimum spanning tree](/rectilinear-minimum-spanning-tree/) takes $\Theta(n \log n)$ time. The rectilinear Steiner minimal tree is NP-hard, but some optimal tree lies on the Hanan grid of at most $n^2$ points ([Hanan's theorem](/hanan-theorem/)), and $\mathrm{RMST} \le \frac32\,\mathrm{RSMT}$, which is tight ([Hwang's theorem](/hwang-rectilinear-steiner-ratio/)).
- [Iterated 1-Steiner](/iterated-one-steiner/) is never longer than the spanning tree. [FLUTE](/flute/) is optimal for nets of up to 9 pins with its published tables and a heuristic beyond.
- With $R$ the largest source-to-sink distance, the [bounded-radius bounded-cost tree](/bounded-radius-bounded-cost-tree/) has radius at most $(1+\varepsilon)R$ and cost at most $(1 + 2/\varepsilon)\,\mathrm{MST}$. The [Prim-Dijkstra tree](/prim-dijkstra-tradeoff/) has radius at most $R/c$, but no cost bound is proved for $0 < c < 1$.
- [Global routing](/global-routing/) is NP-hard. Wirelength is at least the sum of half-perimeters, and a cut crossed by $k_S$ nets with capacity $c(S)$ forces overflow at least $k_S - c(S)$. [Rip-up and reroute](/rip-up-and-reroute/) and [negotiated congestion](/negotiated-congestion-routing/) have no proof that they reach a legal routing; they are judged on benchmarks.
- [Multicommodity flow](/multicommodity-flow-global-routing/) proves a fractional bound: after $T \ge 2\rho \ln|E| / (\varepsilon^2 \lambda^*)$ rounds the average congestion is at most $(1 + 2\varepsilon)\lambda^*$. The integral optimum can be twice the fractional one.
- In a channel, the [density](/channel-density/) $d$ is a lower bound on the tracks, also with doglegs. Without doglegs a routing exists if and only if the [vertical constraint graph](/vertical-constraint-graph/) is acyclic, and the [left-edge algorithm](/left-edge-algorithm/) uses exactly $d$ tracks when that graph has no edges. The minimum track count is NP-complete without doglegs and with them.
- [River routing](/river-routing/) is exact: width $h$ suffices if and only if $a_{i+h} - b_i \ge h$ and $b_{i+h} - a_i \ge h$ for all $i$. Unordered one-layer [escape routing](/escape-routing/) is a maximum flow problem.

| Method | Problem | Time | Guarantee |
|---|---|---|---|
| Lee | two-pin path | $\Theta(MN)$ | shortest path if one exists |
| Hadlock | two-pin path | $\Theta(MN)$ worst | shortest path if one exists |
| Soukup | two-pin path | $\Theta(MN)$ worst | a path if one exists |
| Rectilinear MST | tree on $n$ pins | $\Theta(n \log n)$ | exact; at most $\frac32$ RSMT |
| Iterated 1-Steiner | Steiner tree | $O(n^3 \log n)$ per round | at most the MST |
| FLUTE | Steiner tree | $O(1)$ lookup, small nets | optimal up to 9 pins |
| BRBC | source tree | $\Theta(n^2)$ | radius $(1+\varepsilon)R$, cost $(1 + 2/\varepsilon)$ MST |
| Prim-Dijkstra | source tree | $\Theta(n^2)$ | radius $R/c$ |
| Negotiated congestion | global routing | $O(I(PE \log V + mE))$ | none; measured |
| Multicommodity flow | fractional global routing | $O(TkE \log V)$ | $(1 + 2\varepsilon)\lambda^*$ |
| Left-edge | channel | $O(n + N \log N + T(N + n))$ | $d$ tracks without vertical constraints |
| Greedy router | channel | $O((n + E)T^2)$ | always completes; tracks measured |
| Yoshimura-Kuh | channel | $O(nN^2(N + n))$ | tracks measured |

: Main methods. For channels $n$ counts columns, $N$ nets, $T$ tracks used and $E$ extension columns; for global routing $I$ and $T$ count iterations and rounds, $m$ and $k$ nets, $P$ pins, $V$ gcells and $E$ grid edges.

## Choosing a method

For one connection on a grid, Lee's algorithm is the reference, and Hadlock's algorithm returns a path of the same length with far fewer labels when the path is nearly straight. For the tree of a net, the spanning tree is a quick estimate, FLUTE serves the many small nets of a placer or router, and iterated 1-Steiner suits a single large net. For a critical net, tune $c$ in the Prim-Dijkstra tree, or use BRBC when a proved bound on radius and cost is wanted.

For global routing, route first with patterns and repair overflow with negotiated congestion, as NTHU-Route 2.0 and other academic routers do, and compare the result with the half-perimeter and cut bounds. For a channel, compute the density and the vertical constraint graph first. Without vertical constraints the left-edge algorithm is optimal; with a cycle, doglegs or the greedy router are needed.
