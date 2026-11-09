1. $1$: $1, a$. $2$: $2, a, 1, b$. $3$: $3, c$. $4$: $4, c, 3, d$. $5$: $5, e$. The final matching is $1b, 2a, 3d, 4c, 5e$, which is perfect.

2. Two phases. The first uses paths of length 1 and matches $1a, 3b, 4c, 5e$. The second finds the path $2, a, 1, b, 3, d$ of length 5.

3. A maximum matching is $1a, 2b, 4c$. The set $S = \{1, 2, 3\}$ has $N(S) = \{a, b\}$. A cover of size 3 is $\{a, b, 4\}$.

4. Rows to columns $1 \to 2$, $2 \to 1$, $3 \to 4$, $4 \to 3$ with costs $3 + 5 + 4 + 5 = 17$. The next best assignment costs 19. Row potentials $u = (0, 0, 1, 2)$ and column potentials $v = (5, 3, 3, 3)$ satisfy $u_i + v_j \le c_{ij}$ everywhere, with equality on the chosen cells, and sum to 17.

5. Proposals $Aw$, $Bx$, $Cw$ (accepted, $A$ freed), $Dx$ (rejected), $Ax$ (accepted, $B$ freed), $Bw$ (accepted, $C$ freed), $Dz$, $Cy$. Result $Ax$, $Bw$, $Cy$, $Dz$. With the women proposing, $Ax$, $Bw$, $Cz$, $Dy$.

6. Choose the middle edge $23$. For the bound, every edge of a maximum matching shares an end with an edge of the maximal matching, and each edge of the maximal matching has two ends.

7. The path has a maximum matching of 3 edges, so a minimum edge cover has $7 - 3 = 4$ edges. The cycle also has a maximum matching of 3 and a minimum edge cover of 4.

8. In $K_{1,3}$ take $S$ as the centre: three odd components. The two triangles joined by an edge $uv$ have the perfect matching $uv$ plus one edge in each triangle.

10. There are six perfect matchings. The rest of a cubic graph after a perfect matching is 2-regular, a union of cycles, the Petersen graph has no cycle shorter than 5 and no Hamiltonian cycle, so the rest is two 5-cycles. An odd cycle cannot be coloured with the two colours left.

11. The search reaches $c$ through $b$, goes to $d$ and its mate $e$, and finds no new vertex at $e$; back at $c$, the vertex $e$ is already marked. Contracting $c, d, e$ to one vertex gives the path $a, b, (cde), x$, which expands to $a, b, c, e, d, x$.

12. Whoever is paired with $D$ is the first choice of another of $A$, $B$, $C$, who prefers that person to their own partner.

14. In the first column, either the vertical edge is used, or both horizontal edges to the second column.

17. The answer is 5: the costs at most 5 allow the perfect matching $1 \to 2$, $2 \to 1$, $3 \to 4$, $4 \to 3$, and the costs at most 4 leave row 4 with no cell.

18. There are exactly two stable matchings, those found in Exercise 5.

19. The determinant is $(x_{12} x_{34} + x_{14} x_{23})^2$ up to the signs of the variables in the Pfaffian.

22. The symmetric difference of $M$ and $M^*$ contains $|M^*| - |M|$ vertex-disjoint augmenting paths, each with at least $\ell$ edges. After $\sqrt{n}$ phases $\ell > \sqrt{n}$.

25. Join a centre to three copies of $K_4$ with one edge subdivided, by one bridge each. Removing the centre leaves three components of 5 vertices.
