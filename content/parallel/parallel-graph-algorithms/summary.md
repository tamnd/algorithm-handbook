## What to remember

- A round of [frontier-based processing](/frontier-based-processing/) on a frontier $U$ costs $O(|U| + m_U)$ work and $O(\log n)$ span, so $R$ rounds have span $S = O(R \log n)$. For a large frontier the dense form is cheaper and needs no atomic writes.
- [Parallel BFS](/parallel-bfs/) has $W = O(n + m)$, but its span $O(D \log n)$ grows with the number of levels.
- [Contraction](/graph-contraction/) by random stars removes each non-isolated vertex with probability at least $1/4$, so $E[N_t] \le (3/4)^t n$ and the expected number of rounds is at most $\log_{4/3} n + 5$.
- Hooking by labels gives [Shiloach-Vishkin](/shiloach-vishkin/), with $O(\log n)$ span, and [parallel Borůvka](/parallel-minimum-spanning-tree/), with at most $\lceil \lg n \rceil$ rounds, since each round at least halves the supervertices.
- Random priorities break symmetry. In [Luby's algorithm](/luby-mis/) $E[m_{t+1}] \le m_t/2$, so at most $\log_2 m + 4$ rounds are expected. [Jones-Plassmann](/jones-plassmann/) takes as many rounds as the longest path of decreasing priority has vertices.
- Symmetry-breaking problems reduce to one another: a maximal matching is a [maximal independent set](/maximal-independent-set/) of the line graph, and a $(\Delta + 1)$-colouring is an MIS of a graph on the pairs $(v, c)$.
- The lexicographically first MIS and the lexicographically first DFS are P-complete. A random order, as in random-order greedy, needs few rounds.
- [Delta-stepping](/delta-stepping/) runs from [Dial's algorithm](/dial-algorithm/), for $\Delta$ below the least weight, to frontier [Bellman-Ford](/bellman-ford/), for $\Delta = \infty$.

| Problem | Method | Work $W$ | Span $S$ | Notes |
|---|---|---|---|---|
| BFS | [parallel BFS](/parallel-bfs/) | $O(n + m)$ | $O(D \log n)$ | CRCW PRAM |
| BFS | [direction-optimizing](/direction-optimizing-bfs/) | $O((n + m) D)$ worst case | $O(D(\log n + k))$ | $k$ largest in-degree |
| Shortest paths | [delta-stepping](/delta-stepping/) | $O((n + m)(l + 1) + k \log n)$ | $O(k(l + 1) \log n)$ | $k$ buckets |
| Connectivity | [random mate](/random-mate-contraction/) | $O(m \log n)$ expected | $O(\log^2 n)$ w.h.p. | not work-efficient |
| Connectivity | [Shiloach-Vishkin](/shiloach-vishkin/) | $O((n + m) \log n)$ | $O(\log n)$ | CRCW PRAM |
| Spanning forest | [parallel Borůvka](/parallel-minimum-spanning-tree/) | $O((n + m) \log n)$ | $O(\log^2 n)$ | deterministic |
| Biconnectivity | [Tarjan-Vishkin](/tarjan-vishkin/) | $O((n + m) \log n)$ | $O(\log n)$ | Euler tour |
| MIS | [Luby](/luby-mis/) | $O(n + m)$ expected | $O(\log^2 n)$ w.h.p. | fresh priorities |
| Colouring | [Jones-Plassmann](/jones-plassmann/) | $O(n + m)$ | $O(R \log n)$ | $\Delta + 1$ colours |
| Maximal matching | [Israeli-Itai](/israeli-itai/) | $O(n + m)$ expected | $O(\log^2 n)$ | proposals |
| Weighted matching | [locally dominant](/locally-dominant-matching/) | $O(n + m \log m)$ | $O(r \log n + \log^2 n)$ | ratio $1/2$ |
| SCC | [forward-backward](/forward-backward-scc/) | $O((n + m) d)$ | $O(n d \log n)$ | $d$ levels |
| SCC | [colouring](/coloring-scc/) | $O((n + m) r)$ | $O(r \log n)$ | $r$ rounds |
| Maximum flow | [parallel push-relabel](/parallel-push-relabel/) | $O(n^2 (n + m))$ | $O(n^2 \log n)$ | $< 4n^2$ pulses |
| Transitive closure | [Ullman-Yannakakis](/ullman-yannakakis/) | $O(n(n + m) + s^3 \log s + n^2 s)$ | $O(t \log n + \log^2 n)$ | Monte Carlo |
| Lexicographic DFS | [label relaxation](/parallel-dfs/) | $O(m h^2 + n h \log n)$ | $O(h \log^2 n)$ | $h$ tree height |

: Proved bounds of the methods of this chapter. The letters $D$, $k$, $l$, $r$, $d$, $s$, $t$ and $h$ are defined in each entry.

## Choosing a method

On a graph with a small diameter, such as a social network, use parallel BFS with the direction switch. With weights, use delta-stepping, with $\Delta = \Theta(1/d)$ for random weights in $[0, 1]$ and $d$ the largest degree, or a $\Delta$ tuned per graph class. On road networks and meshes the span $O(D \log n)$ is the limit, and more processors do not help.

For connectivity, prefer contraction or hooking to a search, since its span does not depend on $D$. Random mate is the simplest to write and to prove, Shiloach-Vishkin has the best span, and Borůvka gives a minimum spanning forest at the same cost.

For independent sets, colourings and matchings, use random priorities. Jones-Plassmann gives the greedy colouring in one random order, and the locally dominant matching the greedy weighted matching; on adversarial weights add a random tie-break, or the rounds can become sequential.

For strongly connected components, trim and then use forward-backward search, which does best with a giant component; colouring helps once it is gone and many components remain. For flow, closure and DFS, expect a large span or a large amount of work.
