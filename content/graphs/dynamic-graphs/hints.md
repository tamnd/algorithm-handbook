1. The counts are $7, 6, 5, 4, 4, 3, 2, 1$. The insertion $24$ is the first redundant one: $1, 2, 3, 4$ are already connected through $12$, $34$ and $13$.

2. The earliest arrivals are $a$ at 0, $b$ at 2 and $c$ at 4, through $b \to c$ at time 4; the edge $a \to c$ at time 5 is later. Vertex $d$ is unreachable, because $c \to d$ leaves at time 3. Yet $a$ reaches $b$, and $b$ reaches $d$ by $b \to c$ at 1 and $c \to d$ at 3.

3. After the four unions: $p(2) = 1$, $p(4) = 3$, $p(3) = 1$, $p(5) = 1$, and size$(1) = 5$. The stack holds $(2, 1)$, $(4, 1)$, $(3, 2)$, $(5, 4)$: the vertex that was linked and the old size of its new parent. The first undo sets $p(5) = 5$ and size$(1) = 4$; the second sets $p(3) = 3$ and size$(1) = 2$, leaving $\{1, 2\}$, $\{3, 4\}$, $\{5\}$.

4. $e_1$ goes to $[2, 2]$, $[3, 4]$, $[5, 6]$, $[7, 7]$; $e_2$ to $[3, 4]$ and $[5, 6]$; $e_3$ to the root $[1, 8]$; and $e_4$ to the leaf $[5, 5]$.

5. The sequences are: $a\ ab\ b\ ba$; then $b\ ba\ a\ ab\ bc\ c\ cb$; then $c\ cb\ b\ ba\ a\ ab\ bc\ cd\ d\ dc$; then $b\ ba\ a\ ab\ bc\ cd\ d\ dc\ c\ cb\ be\ e\ eb$. The cut leaves $cd\ d\ dc\ c$ and $b\ ba\ a\ ab\ be\ e\ eb$. The last link gives $d\ dc\ c\ cd\ da\ a\ ab\ be\ e\ eb\ b\ ba\ ad$.

6. The counts are $1, 2, 3, 4, 2, 3, 4, 2, 1$. The edge $13$ closes the cycle $1, 2, 3$, the edge $75$ the cycle $5, 6, 7$, and the edge $41$ the cycle $1, 3, 4$; each merges the components along the tree path. Only $45$ is a bridge at the end.

7. For $(6, 1)$: $F = \{1, 2\}$, $B = \{4, 5, 6\}$, and the order becomes $0, 4, 5, 3, 6, 1, 2$; vertex 3 keeps its place. For $(2, 3)$: $F = \{3\}$, $B = \{6, 1, 2\}$, and the order becomes $0, 4, 5, 6, 1, 2, 3$. For $(3, 4)$ the forward search from 4 goes through 5, 6, 1, 2 and reaches 3, so the edge closes a cycle.

8. Initially $s$ 0, $a$ and $b$ 1, $c$ and $d$ 2, $e$ 3. After deleting $sa$: $a$ 2, $d$ 2, $c$ 3, $e$ 3. After deleting $bd$: $d$ 4 and $e$ 4, both through $c$.

9. The tree is $ef$, $ac$, $cd$, $ab$, $ce$, of weight 16. Inserting $be\,4$ closes the cycle $b, a, c, e$, whose heaviest edge is $ce\,6$; swapping gives weight 14. Deleting $cd$ isolates $d$ in the tree, and the lightest edge back is $bd\,7$, giving weight 18.

11. Before: 3 for $1, 2, 3, 4$; 2 for 5 and 6; 1 for 7. After $54$, vertex 5 has core number 3; after $64$, vertex 6 also has 3. For the bound, remove the new edge from the $(k + 2)$-core of $G + e$; every vertex keeps degree at least $k + 1$.

13. Let $k$ vertices point to $u$, let $v$ point to $k$ other vertices, and add the edge $uv$.

16. An edge rises to level $i$ only inside a tree of at most $n/2^i$ vertices, which must have at least 2 vertices.

19. Represent each edge by a node of its own between its two ends, carrying the weight; vertices carry $-\infty$.

22. A connected graph lifts to one component when it has an odd cycle and to two when it is bipartite.

23. Run two searches from $u$ and from $v$ alternately, one step each. A vertex gets a new label only when its component at least halves.

25. Each query runs a search on the contracted graph, which has at most $k$ extra edges. The total time is $O((T/k)(n + m) + Tk)$.
