1. ◦ A connected plane graph has 10 vertices and 17 edges. How many faces does it have? A convex polyhedron has 12 pentagonal and 20 hexagonal faces, and three faces meet at each corner. Use [Euler's formula](/euler-formula/) to find its numbers of edges and vertices, and check the answer against the degree sum.

2. ◦ Use the [planar edge bound](/planar-edge-bound/) and its version for graphs of girth $g$, $m \le g(n - 2)/(g - 2)$, to show that $K_5$, $K_{3,3}$ and the Heawood graph are not planar. The Heawood graph has the vertices $0, \ldots, 13$, the cycle $i \sim i + 1$ (mod 14), and the chords $i \sim i + 5$ (mod 14) for even $i$; it is 3-regular with girth 6.

3. ◦ A [maximal planar graph](/maximal-planar-graph/) has 12 vertices. How many edges and faces does it have, and what is its average degree? Show that every simple planar graph has a vertex of degree at most 5, and explain why the icosahedron, which is 5-regular and maximal planar, shows that 5 cannot be lowered. What bound on the [chromatic number](/chromatic-number/) follows from the first fact?

4. ◦ The triangular prism has the triangles $1, 2, 3$ and $4, 5, 6$ and the edges $14$, $25$, $36$. Check that it meets the bound $m \le 2n - 3$ for [outerplanar graphs](/outerplanar-graph/) with equality. Show that it is still not outerplanar by finding a $K_4$ [minor](/graph-minor/).

5. ◦ The graph $G$ has the vertices $s, a, b, c, d, t$ and the edges $sa$, $sb$, $ab$, $ac$, $bd$, $cd$, $ct$, $dt$, $st$. Which of the orders $s, c, a, b, d, t$, then $s, b, d, a, c, t$, then $s, a, d, b, c, t$ are [st-numberings](/st-numbering/)? How many st-numberings does $G$ have in all?

6. ◦ Give $K_{3,3}$, with the sides $a, b, c$ and $x, y, z$, the [rotation system](/rotation-system/) in which every vertex lists its neighbours in alphabetical order. [Trace the faces](/planar-face-finding/) with the rule: after arriving at $v$ from $u$, leave along the neighbour that follows $u$ in the rotation at $v$. How many faces are there, and what is the genus of the surface this rotation system describes?

7. ◦ Give a [book embedding](/book-embedding/) of $K_4$ in two pages, with the spine order $1, 2, 3, 4$. Why is one page not enough?

8. ◦ The $k \times k$ grid graph has $n = k^2$ vertices. Find a set of $\sqrt{n}$ vertices whose removal leaves two sides of at most $n/2$ vertices each with no edge between them, as the [planar separator theorem](/planar-separator-theorem/) promises.

9. ◦ Every drawing of a graph can be turned into a planar graph by putting a vertex at each crossing. Use this to show that $\mathrm{cr}(G) \ge m - 3n + 6$ for a simple graph, and $\mathrm{cr}(G) \ge m - 2n + 4$ when $G$ has no triangle. Evaluate both for $K_6$ and $K_{3,3}$, and compare with the [crossing number](/crossing-number/) formula $Z(n)$ of Guy's conjecture for $K_6$.

10. • A simple planar graph has minimum degree 5. Show that it has at least 12 vertices of degree exactly 5.

11. • Prove that a plane graph with $n$ vertices, $m$ edges, $f$ faces and $c$ connected components satisfies $n - m + f = 1 + c$.

12. • Build the [planar dual](/planar-dual-graph/) of the triangular prism of Exercise 4 and identify it. The three edges $14$, $25$, $36$ form a minimal cut of the prism; which cycle of the dual do their dual edges form?

13. • Let $T$ be a spanning tree of a connected plane graph $G$. Show that the dual edges of the edges not in $T$ form a spanning tree of the dual $G^*$. Derive Euler's formula from this.

14. • The Petersen graph has the outer cycle $0, 1, 2, 3, 4$, the spokes $i \sim i + 5$, and the inner edges $i + 5 \sim (i + 2 \bmod 5) + 5$. Find an explicit subdivision of $K_{3,3}$ in it, naming the branch vertices and the paths. Why can it not contain a subdivision of $K_5$, although it has a $K_5$ minor?

15. • Show that a planar graph without triangles has a vertex of degree at most 3, and use this for a linear-time 4-coloring. Show likewise that an outerplanar graph can be 3-colored in linear time.

16. • Take the triangular prism of Exercise 4 and place the outer triangle at $1 = (0, 0)$, $2 = (12, 0)$, $3 = (0, 12)$. Following [Tutte's spring theorem](/tutte-spring-theorem/), put each of $4, 5, 6$ at the average of its neighbours. Compute the positions.

17. • A simple graph has 100 vertices and 1000 edges. Compare the lower bounds on its crossing number given by Exercise 9 and by the [crossing lemma](/crossing-lemma/).

18. • On the orientable surface of [genus](/graph-genus/) $g$, Euler's formula reads $n - m + f = 2 - 2g$ for a cellular embedding. Derive $m \le 3(n - 2 + 2g)$ for simple graphs and $m \le 2(n - 2 + 2g)$ for graphs without triangles. Use them to bound the genus of $K_8$ and of $K_{4,4}$ from below.

19. • In a [doubly connected edge list](/doubly-connected-edge-list/), each half-edge has a twin, a next half-edge on its face, an origin and a face. Explain how to list the half-edges leaving a vertex in clockwise order, and how to insert a diagonal between two vertices of a face in $O(1)$ time once the right half-edges are known.

20. • The wheel $W_5$ is a 5-cycle with a hub joined to all of its vertices. Show that it is planar, contains no $K_4$, and needs 4 colors. What does this say about a [planar graph coloring](/planar-graph-coloring/) algorithm that only looks for a $K_4$?

21. • Suppose that the vertices of a connected graph $G$ have an order with $s$ first and $t$ last in which every other vertex has a neighbour before it and a neighbour after it. Show that $G$ plus the edge $st$ is biconnected. Where does the proof use the edge $st$?

22. ★ The crossing lemma follows from $\mathrm{cr}(G) \ge m - 3n$ by keeping each vertex with probability $p$. Carry out the computation for a general $p$ and choose $p$ to get the largest bound. Show that for $m \ge 9n/2$ the result is $\mathrm{cr}(G) \ge 4m^3/(243 n^2)$.

23. ★ Prove that a connected plane graph is bipartite if and only if every face has a boundary walk of even length. Conclude that a plane graph is bipartite exactly when its dual is Eulerian.

24. ★ A linear forest is a graph each of whose components is a path. Show that linear forests are closed under minors and find the minimal forbidden minors. Then do the same for forests, and compare with the two lists of [Wagner's theorem](/wagner-theorem/).

25. ★ Split a planar graph recursively with separators of at most $c\sqrt{k}$ vertices for a piece of $k$ vertices, with sides of at most $2k/3$, until every piece has at most $r$ vertices. Show that the total number of separator vertices is $O(n/\sqrt{r})$, the bound behind the [r-division](/r-division/).
