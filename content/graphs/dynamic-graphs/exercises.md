1. ◦ Start with the vertices $1, \ldots, 8$ and no edges, and insert the edges $12$, $34$, $56$, $13$, $24$, $78$, $57$, $26$ one at a time. Using [incremental connectivity](/incremental-connectivity/), give the number of components after each insertion. Which insertion is the first that joins two vertices already connected?

2. ◦ A [temporal graph](/temporal-graph/) has the directed edges $a \to b$ at time 2, $b \to c$ at time 1, $b \to c$ at time 4, $c \to d$ at time 3 and $a \to c$ at time 5. A time-respecting path must use edges at nondecreasing times. Starting at $a$ at time 0, find the earliest arrival time at each vertex. Show that reachability by time-respecting paths is not transitive in this graph.

3. ◦ A union-find structure with union by size and no path compression links the smaller root below the larger, and on a tie links the root of the second argument below the root of the first. Starting from the singletons $1, \ldots, 5$, perform union(1, 2), union(3, 4), union(1, 3), union(5, 1), and then two undo operations. Give the parent pointers and sizes after each step, and the records that the [rollback](/rollback-technique/) stack holds.

4. ◦ In [offline dynamic connectivity](/offline-dynamic-connectivity/) over the time steps $1, \ldots, 8$, the edge $e_1$ is present during the steps $2$ to $7$, $e_2$ during $3$ to $6$, $e_3$ during $1$ to $8$ and $e_4$ only at step $5$. On which nodes of the segment tree over $[1, 8]$ is each edge stored?

5. ◦ Use the [Euler tour tree](/euler-tour-tree/) representation, with a loop node $v$ for each vertex and the arc nodes $uv$ and $vu$ for each edge. Link joins the rotated tours as $S_u\ uv\ S_v\ vu$, and cut splits the tour around the two arcs of the edge. Starting from the singletons $a, \ldots, e$, perform link$(a, b)$, link$(b, c)$, link$(c, d)$, link$(b, e)$, cut$(b, c)$ and link$(d, a)$, and give the sequences after each operation.

6. ◦ Insert the edges $12$, $23$, $34$, $45$, $13$, $56$, $67$, $75$, $41$ one at a time into an empty graph on the vertices $1, \ldots, 7$. How many [bridges](/bridge/) does the graph have after each insertion? Which steps of [online bridge finding](/online-bridge-finding/) collapse a path into one 2-edge-connected component?

7. ◦ Seven vertices are in the topological order $0, 1, \ldots, 6$, and the edges $(0, 1)$, $(1, 2)$, $(4, 5)$, $(5, 6)$ are present. Insert $(6, 1)$, then $(2, 3)$, then $(3, 4)$ with [incremental topological ordering](/incremental-topological-ordering/). For each insertion give the forward set $F$, the backward set $B$ and the order afterwards, or report the cycle.

8. ◦ An undirected graph has the edges $sa$, $sb$, $ab$, $ac$, $bd$, $cd$, $ce$, $de$. Give the breadth-first levels from $s$. An [Even-Shiloach tree](/even-shiloach-tree/) then processes the deletion of $sa$ and afterwards of $bd$. Give the levels after each deletion.

9. ◦ A weighted graph has the edges $ab\,4$, $ac\,2$, $bc\,5$, $bd\,7$, $cd\,3$, $ce\,6$, $de\,8$, $df\,9$, $ef\,1$. Find its minimum spanning tree. Then insert $be\,4$ and delete $cd$, and update the tree each time as a [dynamic minimum spanning tree](/dynamic-minimum-spanning-tree/) would, by one swap per update.

10. • A directed graph has the edges $sa\,2$, $sb\,6$, $ab\,3$, $ac\,7$, $bc\,2$, $bd\,5$, $ce\,4$, $de\,1$, $cd\,4$. Compute the distances from $s$. Which distances change when the length of $sb$ drops to 1? Which change when instead the length of $ab$ rises to 9? Explain why [Ramalingam and Reps](/ramalingam-reps/) touch only these vertices.

11. • A graph has a $K_4$ on the vertices $1, 2, 3, 4$ and the further edges $51$, $52$, $63$, $65$, $76$. Compute the core number of every vertex. Insert $54$, then $64$, and give the [core numbers](/dynamic-k-core-decomposition/) after each insertion. Prove that one insertion raises each core number by at most 1.

12. • For connectivity queries in a forest under link and cut, give one structure with $O(1)$ query time and one with $O(1)$ update time, and state the cost of the other operation in each. Where do [Euler tour trees](/euler-tour-tree/) sit on this [trade-off](/update-query-tradeoff/)?

13. • Show that the deletion of a single edge can remove $\Theta(n^2)$ pairs from the [transitive closure](/dynamic-transitive-closure/) of a directed graph, so no algorithm that keeps the closure as an explicit matrix has a worst-case deletion time below $\Theta(n^2)$.

14. • [Italiano's algorithm](/italiano-dynamic-transitive-closure/) keeps, for each source, a tree of the vertices it reaches. Show that over any sequence of insertions into an initially empty graph, the total work is $O(nm)$, where $m$ is the final number of edges, so the amortized time per insertion is $O(n)$.

15. • Show that an Even-Shiloach tree that keeps levels up to $D$ spends $O(mD + n)$ time over any sequence of deletions. What does this give for the plain decremental breadth-first search, with $D = n$?

16. • In [Holm, de Lichtenberg and Thorup](/holm-de-lichtenberg-thorup/), each edge has a level that only increases, and the spanning trees at level $i$ have at most $n/2^i$ vertices. Show that the levels never exceed $\log_2 n$. If each level increase costs $O(\log n)$, what amortized bound does this give per insertion?

17. • Keep a maximal matching under edge insertions and deletions in a graph of maximum degree $\Delta$. Describe the update after inserting an edge and after deleting a matched edge, with their costs. Show that the matched vertices form a [vertex cover](/dynamic-vertex-cover/) of size at most twice the minimum.

18. • Keep a proper coloring with $\Delta + 1$ colors in a graph whose degrees stay at most $\Delta$. Show that each insertion can be handled by recoloring one vertex in $O(\Delta)$ time, and that deletions need no work. Why does this say nothing about keeping $\chi(G)$ colors, as the entry on [dynamic graph coloring](/dynamic-graph-coloring/) notes?

19. • Use a [link-cut tree](/link-cut-tree/) to keep a minimum spanning forest when edges are only inserted, in $O(\log n)$ amortized time per insertion. How are edge weights stored, given that link-cut trees aggregate values on vertices?

20. • A structure for a dynamic graph rebuilds a static answer from scratch in $O(m)$ time after every $k$ updates, and answers each query by combining the static answer with a scan of the at most $k$ updates since the rebuild, in $O(k)$ time. For a sequence with as many queries as updates, choose $k$ and state the amortized time per operation.

21. • Extend union-find with a parity bit per vertex, the parity of the path to its root, to keep [bipartiteness](/dynamic-bipartiteness/) under insertions. Describe union and the test for an odd cycle, and check it on the insertions $12$, $23$, $34$, $41$, $13$.

22. ★ The bipartite double cover of $G$ has the vertices $(v, 0)$ and $(v, 1)$ for each vertex $v$ and, for each edge $uv$, the edges $(u, 0)(v, 1)$ and $(u, 1)(v, 0)$. Show that $G$ is bipartite exactly when the cover has twice as many components as $G$. Derive a fully dynamic bipartiteness algorithm from any fully dynamic connectivity algorithm.

23. ★ Give a [decremental connectivity](/decremental-connectivity/) algorithm for forests with $O(1)$ query time and $O(n \log n)$ total update time.

24. ★ Show that union-find with path compression but without union by size cannot be combined with rollback: build a sequence of unions, finds and undos on $n$ elements in which every round of a union, a find and an undo costs $\Theta(n)$. Why is the compression itself a problem for undo?

25. ★ Answer an offline sequence of $T$ edge insertions, deletions and connectivity queries on $n$ vertices and at most $m$ edges by splitting the sequence into blocks of $k$ operations. Within a block, contract the edges that are present during the whole block and untouched by it. Choose $k$ and bound the total time.
