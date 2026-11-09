2. The array ends as $\langle 7, 7, 7, 4, 4, 7, 7, 7 \rangle$. The unions change $1 + 2 + 1 + 2 + 1 + 3 = 10$ entries; the last one renames the three members of the set named 6.

3. Quick-union gives $\langle 5, 2, 7, 4, 4, 6, 7, 7 \rangle$, with the path $0 \to 5 \to 6 \to 7$ of height 3. Union by size gives $\langle 5, 2, 2, 4, 4, 2, 5, 2 \rangle$: the last union joins two trees of size 3 and hangs 5 under 2, and the height is 2.

4. Compression gives $\langle 5, 5, 5, 5, 5, 5, 2, 3, 5 \rangle$. Halving gives $\langle 1, 3, 3, 5, 5, 5, 2, 3, 1 \rangle$ and splitting gives $\langle 2, 3, 4, 5, 5, 5, 2, 3, 1 \rangle$. The sum of depths falls from 28 to 10 with compression and to 17 with either of the others.

6. The first eight edges are fine: the path 0, 1, 2, 3, 4, 5 colors the vertices $0, 1, 0, 1, 0, 1$, and each later edge joins two colors. The edge $(0, 4)$ joins two vertices of color 0. It closes the triangle 0, 4, 5, and also the cycle 0, 1, 2, 3, 4.

7. The colors are c c c a b e b d d d. Read the operations backwards: $e$ paints cell 5, $d$ paints 7 to 9, $c$ paints 0 to 2, $b$ paints only 4 and 6, and $a$ paints only 3. That is $1 + 3 + 3 + 2 + 1 = 10$ cells, each once.

9. After the unions the parents of 1 to 9 are $\langle 2, 4, 4, 8, 6, 8, 8, 8, 8 \rangle$ and the ranks are $\langle 0, 1, 0, 2, 0, 1, 0, 3, 0 \rangle$. The find from 1 follows $1 \to 2 \to 4 \to 8$ and points 1 and 2 at 8. The ranks stay; the heights of 2, 4 and 8 drop to 0, 1 and 2.

11. The blocks before the five $E$'s are $\{7, 2\}$, $\{9, 5, 4\}$, $\{\}$, $\{1, 8, 6\}$ and $\{3\}$. Key 1 goes to the fourth extraction, 2 to the first, 3 to the fifth, 4 to the second and 5 to the third. Each block whose extraction is used merges with the next one. The answers are 2, 4, 5, 1, 3, and 6, 7, 8 and 9 stay in the set.

14. Each query $[l, r]$ is answered right after position $r$ is pushed, by a find from $l$.

17. Once a node is on a find path and is not the root or a child of the root, compression makes it a child of the root. With no more links, it stays a child of a root for good, so it is never moved again. Charge each step of a find either to the find itself (the last two nodes) or to a node that moves.

18. Keep the elements apart from the nodes of the forest. Each element has a pointer to its current node, and each root keeps a size. A move lowers the size of the old root by one, gives $x$ a fresh node, and joins that node to the set of $y$. The old node of $x$ stays in its tree as a placeholder, which still serves the finds of the others.

19. Each edge is alive during an interval of time. Build a segment tree over the times of the queries, and store each interval in $O(\log m)$ of its nodes. Walk the tree depth-first: at each node, add its edges with union, recurse, and roll the unions back on the way out. At a leaf, answer the query.

20. When the DFS has finished a child $v$ of $u$, it calls union$(v, u)$ and keeps $u$ as the name of the set. Every set is then a connected piece of the tree whose top node is its name. With Gabow and Tarjan's structure the whole run takes $O(n + m)$ time for $n$ nodes and $m$ queries.
