## What to remember

- **Planar graphs are sparse.** [Euler's formula](/euler-formula/) $n - m + f = 2$ gives $m \le 3n - 6$, and $m \le 2n - 4$ without triangles ([planar edge bound](/planar-edge-bound/)). So there is always a vertex of degree at most 5, and every algorithm that runs in $O(n + m)$ runs in $O(n)$.
- **Two graphs are the only obstructions.** A graph is planar exactly when it has no subdivision of $K_5$ or $K_{3,3}$ ([Kuratowski](/kuratowski-theorem/)), or equivalently no such [minor](/graph-minor/) ([Wagner](/wagner-theorem/)). The two forms differ for a single graph: the Petersen graph has a $K_5$ minor but no $K_5$ subdivision.
- **An embedding is a rotation system.** The cyclic order of edges at each vertex determines the faces by a [face walk](/planar-face-finding/), and the embedding is planar exactly when Euler's formula holds for the faces found. The [doubly connected edge list](/doubly-connected-edge-list/) stores the same thing with explicit pointers, and the [dual](/planar-dual-graph/) swaps faces and vertices, cuts and cycles.
- **Planarity is decided in linear time.** [Hopcroft-Tarjan](/hopcroft-tarjan-planarity-test/) and [Boyer-Myrvold](/boyer-myrvold-planarity-test/) run in $O(n)$ and return either an embedding or a Kuratowski subgraph. First check $m \le 3n - 6$; otherwise the answer is already no.
- **Five colors are easy, four are hard to prove, three are hard to decide.** The [five-color algorithm](/five-color-algorithm/) removes a vertex of degree at most 5 and frees a color with one Kempe swap. The [four color theorem](/four-color-theorem/) needs a computer-checked proof, and deciding 3-colorability stays NP-complete on planar graphs ([planar graph coloring](/planar-graph-coloring/)).
- **Straight lines and small grids suffice.** By [Fáry's theorem](/fary-theorem/) every planar graph has a straight-line drawing, and the [shift method](/de-fraysseix-pach-pollack/) and [Schnyder's drawing](/schnyder-drawing/) place it on an $O(n) \times O(n)$ grid in linear time. For 3-connected graphs, [Tutte's spring theorem](/tutte-spring-theorem/) gives a convex drawing by solving one linear system.
- **Crossings grow cubically.** A dense graph needs many crossings: the [crossing lemma](/crossing-lemma/) gives $\mathrm{cr}(G) \ge m^3/(64 n^2)$ for $m \ge 4n$.
- **Small separators drive divide and conquer.** Every planar graph has a [separator](/planar-separator-theorem/) of $O(\sqrt{n})$ vertices with sides of at most $2n/3$, found in linear time by [Lipton-Tarjan](/lipton-tarjan-separator/). Recursion gives [r-divisions](/r-division/) and [shortest paths](/planar-shortest-paths/) in $O(n)$.

## The algorithms side by side

| Algorithm | Problem | Time | Output |
|---|---|---|---|
| [Face finding](/planar-face-finding/) | faces of a rotation system | $\Theta(n + m)$ | face cycles |
| [Lempel-Even-Cederbaum](/lempel-even-cederbaum-st-numbering/) | st-numbering | $O(n + m)$ | vertex order |
| [Hopcroft-Tarjan](/hopcroft-tarjan-planarity-test/) | planarity | $O(n)$ | yes or no, embedding |
| [Boyer-Myrvold](/boyer-myrvold-planarity-test/) | planarity | $O(n)$ | embedding or Kuratowski subgraph |
| [Five-color algorithm](/five-color-algorithm/) | 5-coloring | $O(n^2)$ | coloring |
| [Shift method](/de-fraysseix-pach-pollack/) | straight-line drawing | $O(n)$ | $(2n - 4) \times (n - 2)$ grid |
| [Schnyder drawing](/schnyder-drawing/) | straight-line drawing | $\Theta(n)$ | $(n - 2) \times (n - 2)$ grid |
| [Planarization](/planarization-heuristic/) | drawing with few crossings | $O(nm + k(n + m + C))$ | planarized graph |
| [Lipton-Tarjan](/lipton-tarjan-separator/) | balanced separator | $\Theta(n)$ | $O(\sqrt{n})$ vertices |
| [Frederickson](/frederickson-planar-shortest-paths/) | shortest paths | $O(n \sqrt{\log n})$ | distances |
| [Genus computation](/graph-genus-computation/) | embedding on $S_g$ | $O(f(g)\, n)$ | embedding or no |

: Bounds from the entries. The five-color algorithm can be made linear, and shortest paths with nonnegative lengths take $O(n)$ with the method of Henzinger, Klein, Rao and Subramanian.

## Choosing an algorithm

- Only a yes or no on a small graph: count edges, then any simple test; for an embedding or a certificate of non-planarity, use Boyer-Myrvold from a library.
- Faces, the dual or any walk around a face: build a rotation system or a doubly connected edge list once and work on it.
- Coloring a planar graph in practice: smallest-last greedy gives six colors at once, the five-color algorithm five; four colors need the quadratic algorithm behind the four color theorem.
- Drawing: a 3-connected graph with a fixed outer face, Tutte's spring layout; a grid with integer coordinates, the shift method or Schnyder's method; a non-planar graph, planarization.
- Divide and conquer on a planar graph, nested dissection or faster shortest paths: a Lipton-Tarjan separator, applied recursively to get an r-division.
