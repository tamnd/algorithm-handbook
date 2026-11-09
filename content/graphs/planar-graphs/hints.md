1. The graph has $f = 2 - 10 + 17 = 9$ faces. The polyhedron has $32$ faces and $(12 \cdot 5 + 20 \cdot 6)/2 = 90$ edges, so $n = 2 - 32 + 90 = 60$ vertices. Each vertex has degree 3, and $3 \cdot 60 = 180 = 2 \cdot 90$.

2. $K_5$ has $10 > 3 \cdot 5 - 6 = 9$ edges. $K_{3,3}$ has girth 4 and $9 > 4 \cdot 4/2 = 8$ edges. The Heawood graph has $21$ edges, but girth 6 allows only $6 \cdot 12/4 = 18$.

3. It has $3 \cdot 12 - 6 = 30$ edges and, by Euler's formula, $20$ faces; the average degree is $60/12 = 5$. If every vertex had degree at least 6, the degree sum would be at least $6n > 6n - 12 \ge 2m$. The icosahedron is planar with every degree equal to 5, so no smaller bound holds for all planar graphs. Removing a vertex of degree at most 5 again and again and coloring greedily in the reverse order gives $\chi(G) \le 6$.

4. It has $n = 6$ and $m = 9 = 2 \cdot 6 - 3$. Contract $25$ to a vertex $X$ and $36$ to a vertex $Y$. The edges $12, 23, 31, 45, 56, 64, 14$ become $1X$, $XY$, $1Y$, $4X$, $XY$, $4Y$ and $14$, so $1, 4, X, Y$ form a $K_4$.

5. The first is not one: $c$ has the neighbours $a$, $d$, $t$, all after it. The second is one. The third is not: $d$ has the neighbours $b$, $c$, $t$, all after it. There are six st-numberings: $s, a, b, c, d, t$; $s, a, b, d, c, t$; $s, a, c, b, d, t$; $s, b, a, c, d, t$; $s, b, a, d, c, t$; and $s, b, d, a, c, t$.

6. There are three faces, each a closed walk of 6 edges: $a, x, b, y, c, z$; $a, y, b, z, c, x$; and $a, z, b, x, c, y$. Then $n - m + f = 6 - 9 + 3 = 0 = 2 - 2g$, so $g = 1$: the rotation system describes an embedding on the torus. Changing only the rotation at $z$ to $a, c, b$ leaves a single face, and genus 2.

7. Put $12$, $23$, $34$, $14$ and $13$ on the first page and $24$ on the second. On one page two edges $ac$ and $bd$ with $a < b < c < d$ cross; here $13$ and $24$ interleave. A one-page graph is outerplanar, and $K_4$ has $6 > 2 \cdot 4 - 3$ edges.

8. Remove the column $\lceil k/2 \rceil$. It has $k = \sqrt{n}$ vertices. The columns to its left hold $k(\lceil k/2 \rceil - 1) \le n/2$ vertices, those to its right $k \lfloor k/2 \rfloor \le n/2$, and no edge joins the two sides.

9. Remove one edge per crossing from a drawing with $\mathrm{cr}(G)$ crossings; the rest is a plane graph, so $m - \mathrm{cr}(G) \le 3n - 6$. For $K_6$ the bound is $15 - 18 + 6 = 3$; the triangle-free bound does not apply. For $K_{3,3}$ the first bound is negative and the second is $9 - 12 + 4 = 1$. Guy's formula gives $Z(6) = \tfrac14 \cdot 3 \cdot 2 \cdot 2 \cdot 1 = 3$; drawings with $Z(n)$ crossings exist, so $\mathrm{cr}(K_6) = 3$.

12. The prism has five faces: two triangles $T$, $B$ and three quadrilaterals. Each quadrilateral meets $T$, $B$ and the other two quadrilaterals, and $T$ does not meet $B$, so the dual is $K_5$ minus the edge $TB$. Each vertical edge lies between two quadrilaterals, so the three dual edges form the triangle on the quadrilaterals.

14. Delete vertex 0. The branch vertices are $2, 8, 9$ on one side and $3, 6, 7$ on the other. Six of the nine paths are single edges, $23$, $27$, $83$, $86$, $96$, $97$, and the other three pass through the neighbours of 0: $2, 1, 6$; $9, 4, 3$; and $8, 5, 7$. A subdivision of $K_5$ needs five vertices of degree 4.

16. Each inner vertex satisfies $4p_v = p_{\text{outer neighbour}} + (p_4 + p_5 + p_6)$, and summing the three equations gives $p_4 + p_5 + p_6 = p_1 + p_2 + p_3$.

18. A face of a simple graph has at least 3 edges, so $2m \ge 3f$; substitute in Euler's formula. For $K_8$, $28 \le 3(6 + 2g)$ forces $g \ge 2$. For $K_{4,4}$, $16 \le 2(6 + 2g)$ forces $g \ge 1$.

21. Remove a vertex $v$. A vertex numbered below $v$ reaches $s$ along neighbours with decreasing numbers, which avoids $v$; one above $v$ reaches $t$ along increasing numbers. The edge $st$ joins the two groups.

22. A drawing with $\mathrm{cr}(G)$ crossings keeps each crossing with probability $p^4$, each edge with $p^2$ and each vertex with $p$. Taking expectations of $\mathrm{cr} \ge m - 3n$ gives $\mathrm{cr}(G) \ge m/p^2 - 3n/p^3$, which is largest at $p = 9n/(2m)$.

24. A graph that is not a linear forest has a cycle or a vertex of degree at least 3.
