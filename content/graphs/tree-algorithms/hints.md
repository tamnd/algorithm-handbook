1. Preorder $1, 2, 4, 5, 7, 8, 3, 6, 9, 10$; postorder $4, 7, 8, 5, 2, 10, 9, 6, 3, 1$. Depths: 1 is 0; 2 and 3 are 1; 4, 5, 6 are 2; 7, 8, 9 are 3; 10 is 4. Sizes: $s(1) = 10$, $s(2) = 5$, $s(3) = 4$, $s(5) = s(6) = 3$, $s(9) = 2$, and 1 for the leaves 4, 7, 8, 10.

2. The root 1 has the left subtree with preorder $2, 4, 7, 5$ and the right subtree with preorder $3, 6, 8$. Node 4 has the right child 7, node 3 has the right child 6, and 6 has the left child 8. The postorder is $7, 4, 5, 2, 8, 6, 3, 1$. A node with one child gives the same preorder and postorder whether the child is on the left or on the right.

3. The code is $2, 5, 5, 2, 1, 3, 6, 9$. The sequence $4, 4, 1, 6, 6$ decodes to the edges $24, 34, 41, 16, 56$ and finally $67$.

4. From 1 the farthest vertex is 10, at distance 4. From 10 the farthest is 7, at distance 7. The diameter is 7, along $10, 9, 6, 3, 1, 2, 5, 7$.

5. Round 1 removes $4, 7, 8, 10$, round 2 removes $5, 9$, round 3 removes $2, 6$, and $\{1, 3\}$ remains: the center is the edge $13$, both with eccentricity 4. The centroids are 1, with pieces of 5 and 4, and 2, with pieces of 1, 3 and 5. The center and the centroid differ: vertex 3 is central but not a centroid.

6. Bottom up: the leaves 4, 7, 8, 10 have (in, out) $= (w, 0)$. Then $5: (6, 5)$, $9: (7, 4)$, $2: (10, 10)$, $6: (5, 7)$, $3: (9, 7)$, $1: (20, 19)$. A heaviest set is $\{1, 4, 5, 9\}$ with weight 20.

7. The root is 1. Its left subtree has the root 2 with the children 5 and 8; its right subtree has the root 3, with the left child 7 and the right child 4, whose left child is 6. Positions 2 and 6 hold 2 and 3, and their lowest common ancestor is 1, the minimum of the range.

8. The tour is $1, 2, 4, 2, 5, 7, 5, 8, 5, 2, 1, 3, 6, 9, 10, 9, 6, 3, 1$ with the depths $0, 1, 2, 1, 2, 3, 2, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0$. Between the first 7 and the first 10 the least depth is 0, at vertex 1. Between the first 7 and the first 8 it is 2, at vertex 5.

9. For 7: $up[0] = 5$, $up[1] = 2$, $up[2] = $ none. For 10: $up[0] = 9$, $up[1] = 6$, $up[2] = 1$. Lift 10 by one level to 9. With $k = 1$ the ancestors 2 and 3 differ, so move to 2 and 3. With $k = 0$ both parents are 1, so the answer is 1.

12. From 0 the distances are 1 for 1 and 2, 2 for 3, 4 and 5, and 3 for 6. From 6 every vertex is within 3, but $d(4, 5) = 4$. In a tree, the path from the start to the first vertex found meets every longest path; with cycles, a second route can bypass it.

14. Query $(7, 8)$ is answered at 8, where $7$ has been merged into 5, so the answer is 5. Query $(8, 6)$ is answered at 6, after the subtree of 2 has been merged into 1, so the answer is 1. Query $(4, 10)$ is answered at 10 with answer 1.

16. Vertex $s$ dominates everything. The immediate dominators are $s$ for $a$, $b$, $c$, $f$ and $g$, then $c$ for $d$, and $d$ for $e$. Vertex $f$ is reached both through $b$ and through $d$, and $g$ through $e$ and through $f$.

17. For $C_n$ use the bags $\{1, i, i + 1\}$ for $i = 2, \ldots, n - 1$ in a path. A graph of treewidth 1 is a forest.

19. The distance is 2: delete $b$, which gives $a(c, d, e)$, then insert $f$ as the parent of $d$ and $e$. One operation is not enough, since the two trees differ both in the label set and in the shape.

21. Let $v$ be any vertex and $x$ a vertex farthest from it. The path from $v$ to $x$ meets the path from $a$ to $b$, and an exchange argument shows that $a$ or $b$ is at least as far as $x$. On $T$ with $a = 10$, $b = 7$ this gives the eccentricities 4, 5, 4, 6, 6, 5, 7, 7, 6, 7 for the vertices 1 to 10.

24. Remove any bag contained in a neighbouring bag. A leaf bag then has a vertex that no other bag contains, and all its neighbours lie in that bag.

25. Expected stretch of one edge: with probability $1/n$ it is the deleted one and is stretched to $n - 1$, and otherwise it stays 1, which gives $2(n - 1)/n$.
