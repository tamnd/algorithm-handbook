1. In order: a trail, since vertex 1 repeats but no edge does; a walk, since the edge $13$ is used twice; a simple path; a simple cycle; none, since $24$ is not an edge; a closed walk that is not a trail, since $13$ is used twice.

2. Row $a$ of $A^3$ is $(2, 5, 5, 2)$, so there are 2 walks of length 3 from $a$ to $d$ and 5 from $a$ to $b$. The two to $d$ are $a, b, c, d$ and $a, c, b, d$.

3. The arcs $1 \to 2$, $2 \to 4$, $1 \to 3$, $5 \to 6$, $6 \to 7$ are tree arcs. $3 \to 4$, $5 \to 1$ and $7 \to 3$ are cross arcs, since their heads are already black. $7 \to 5$ is a back arc and closes the cycle $5, 6, 7, 5$.

4. All degrees are even (2, 4, 4, 4, 4, 2) and the graph is connected, so a circuit exists. Without $23$ the vertices 2 and 3 have odd degree, so an Eulerian path exists and must run between 2 and 3.

5. The first tour is $1, 2, 3, 1$, which is stuck at 1 because both its edges are used. Back at 3 a second tour $3, 4, 2, 5, 4, 6, 5, 3$ is spliced in, which gives the circuit $1, 2, 3, 4, 2, 5, 4, 6, 5, 3, 1$.

6. All four vertices are odd. The distances are $ab = 3$, $ac = 5$, $ad = 1$, $bc = 2$, $bd = 4$, $cd = 4$. The pairings cost $3 + 4 = 7$, $5 + 4 = 9$ and $1 + 2 = 3$, so $ad$ and $bc$ are doubled, and the walk has length $21 + 3 = 24$.

7. $a = 3$, $b = 2$, $c = \max(3 + 4, 2 + 6) = 8$, $d = \max(3 + 2, 8 + 1) = 9$, $t = \max(8 + 3, 9 + 5) = 14$. A longest path is $s, b, c, d, t$.

8. The matching $1 \to 2$, $2 \to 4$, $4 \to 5$, $3 \to 6$ has size 4, so $6 - 4 = 2$ paths suffice: $1, 2, 4, 5$ and $3, 6$. One path is impossible, since 2 and 3 are incomparable.

9. The layers are $\{0\}$, $\{1, 4, 5\}$ and $\{2, 3, 6, 7, 8, 9\}$. Each vertex of the last layer has one neighbour in the layer before, so the six non-tree edges $23, 27, 38, 68, 69, 79$ all lie inside layer 2 and each gives the bound $2 + 2 + 1 = 5$. No edge lies inside layer 1, so no cycle through 0 is shorter, and since the graph looks the same from every vertex the girth is 5.

11. Every vertex must have in-degree equal to out-degree, and the arcs must lie in one strongly connected component. The circuit $00, 00, 01, 10, 01, 11, 11, 10, 00$ uses the arcs $000, 001, 010, 101, 011, 111, 110, 100$ and gives the string $00010111$.

13. If every degree is at least $n/2$, every pair has degree sum at least $n$. In $K_{k, k+1}$ a Hamiltonian cycle would alternate sides and so need equal sides.

16. A basis has $10 - 6 + 1 = 5$ cycles, one for each non-tree edge $23, 34, 35, 45, 56$. The cycle $3, 4, 5$ is the sum of the fundamental cycles of $34$, $35$ and $45$: the tree edges $12, 13, 24, 25$ cancel in pairs.

19. $K_n$ needs $n - 2$, since any three remaining vertices form a triangle. The wheel needs 2, the hub and one rim vertex, since removing one vertex leaves a cycle or a triangle. The Petersen graph needs 3, for example $\{0, 2, 8\}$: removing $k$ vertices of a cubic graph deletes at most $3k$ of the 15 edges, and a forest on $10 - k$ vertices has at most $9 - k$ edges, so $15 - 3k \le 9 - k$.

21. A closed walk of length 3 in a simple graph is a triangle with a chosen start (3 ways) and direction (2 ways). The diamond has 2 triangles and trace 12. The trace of $A^4$ counts the 4-cycles 8 times each, plus the walks that go back and forth along one edge or along two edges at a vertex.

22. Each 4-cycle offers two ways across, so there are $2^k$ paths. For the bad case, hang a large graph that does not reach $t$ near $s$ and let the search enter it first.

24. Paths that share vertices in the DAG are disjoint paths in the closure, since a repeated vertex can be skipped. By Dilworth's theorem, the closure is a partial order whose smallest chain cover equals its largest antichain.
