1. ◦ The tree $T$ has the vertices $1, \ldots, 10$ and the edges $12, 13, 24, 25, 36, 57, 58, 69, 9\,10$. Root it at 1 and order children by increasing label. Give the [preorder](/preorder-traversal/) and [postorder](/postorder-traversal/) of the vertices, the depth of each vertex and the [subtree sizes](/subtree-sizes/).

2. ◦ A binary tree with the labels $1, \ldots, 8$ has the preorder $1, 2, 4, 7, 5, 3, 6, 8$ and the [inorder](/inorder-traversal/) $4, 7, 2, 5, 1, 3, 8, 6$. Rebuild the tree and give its postorder. Why do a preorder and a postorder alone not determine a binary tree?

3. ◦ Compute the [Prüfer code](/pruefer-code/) of the tree $T$ of Exercise 1. Then decode the sequence $4, 4, 1, 6, 6$ into a tree on 7 vertices.

4. ◦ Run the [double sweep](/tree-diameter-double-sweep/) on the tree $T$ of Exercise 1, starting from vertex 1 and breaking ties by the smaller label. Give the vertex found by each sweep, the diameter, and a longest path.

5. ◦ For the tree $T$ of Exercise 1, run [leaf peeling](/tree-center-leaf-peeling/) and give the leaves removed in each round and the [center](/tree-center/). Then find every [centroid](/centroid/) from the subtree sizes of Exercise 1. Are the center and the centroid the same?

6. ◦ Give the vertices of $T$ from Exercise 1 the weights $w(1), \ldots, w(10) = 3, 5, 2, 4, 6, 1, 2, 3, 7, 4$. Compute, for each vertex $v$, the best weight of an [independent set](/independent-set-on-trees/) in the subtree of $v$ that contains $v$ and the best that does not, and give a heaviest independent set of $T$.

7. ◦ Build the [Cartesian tree](/cartesian-tree/), with the minimum at the root, of the array $5, 2, 8, 1, 7, 3, 6, 4$, using the stack method from left to right. Show how the minimum of positions 2 to 6 is the lowest common ancestor of two nodes.

8. ◦ Write the Euler tour of length $2n - 1$ of the tree $T$ of Exercise 1, with children in increasing order, and the depth of each entry. Use it to find the [lowest common ancestor](/euler-tour-lca/) of 7 and 10, and of 8 and 7, as range minima.

9. ◦ For the tree $T$ of Exercise 1, write the [binary lifting](/binary-lifting/) entries $up[k][v]$ for $v = 7$ and $v = 10$ and $k = 0, 1, 2$. Then follow the [LCA query](/lca-binary-lifting/) for 7 and 10 step by step.

10. • Prove that a tree with $n \ge 2$ vertices has $2 + \sum_{v} \max(\deg v - 2, 0)$ leaves. In particular it has at least two leaves, and exactly two only when it is a path.

11. • A [complete binary tree](/complete-binary-tree/) with $n$ nodes is stored in an array with the root at index 1. Show that the children of index $i$ are $2i$ and $2i + 1$, that the height is $\lfloor \log_2 n \rfloor$, and that exactly $\lceil n/2 \rceil$ nodes are leaves.

12. • The graph with the vertices $0, \ldots, 6$ and the edges $01, 02, 13, 14, 23, 25, 36$ is not a tree. Run the double sweep from 0 and show that it returns 3, while the diameter is 4. Which step of the proof for trees fails here?

13. • Prove that the center of a tree lies on every longest path, at its middle, and that the radius is $\lceil d/2 \rceil$ for diameter $d$.

14. • Run [Tarjan's offline LCA algorithm](/tarjan-offline-lca/) on the tree $T$ of Exercise 1 with the queries $(7, 8)$, $(4, 10)$ and $(8, 6)$, visiting children in increasing order. Say at which vertex each query is answered and what the union-find structure returns.

15. • A [virtual tree](/virtual-tree/) on a set $K$ of $k$ vertices adds the lowest common ancestors of pairs of $K$. Show that it is enough to add the LCAs of the pairs that are adjacent when $K$ is sorted by discovery time, and that the virtual tree has at most $2k - 1$ vertices.

16. • A flow graph with start $s$ has the arcs $s \to a$, $s \to b$, $a \to c$, $b \to c$, $b \to f$, $c \to d$, $d \to e$, $d \to f$, $e \to c$, $e \to g$, $f \to g$. Find the dominators of every vertex and draw the [dominator tree](/dominator-tree/).

17. • Show that a forest with at least one edge has [treewidth](/treewidth/) 1, and that the cycle $C_n$ has treewidth 2, with a [tree decomposition](/tree-decomposition/) of width 2 and an argument that width 1 is impossible.

18. • Number the vertices of the $3 \times 3$ grid row by row from 1 to 9. Show that the bags $\{i, i + 1, i + 2, i + 3\}$ for $i = 1, \ldots, 6$ form a [path decomposition](/path-decomposition/) of width 3. Extend the idea to the $k \times k$ grid.

19. • Using unit costs, find the [tree edit distance](/tree-edit-distance/) between the ordered trees $a(b(c, d), e)$ and $a(c, f(d, e))$, written with the children of each node in brackets, and give an edit script that reaches it.

20. • Show that for a minimum vertex cover of a tree, a leaf can always be left out and its neighbour taken. Turn this into a linear-time greedy algorithm, and compare it with the dynamic program for [independent sets](/maximum-independent-set-in-trees/).

21. • Let $a$ and $b$ be the ends of a diameter of a tree. Prove that the [eccentricity](/eccentricity/) of every vertex $v$ is $\max(d(v, a), d(v, b))$, and so compute all eccentricities with three searches. Check it on the tree $T$ of Exercise 1.

22. ★ In the Euler tour, consecutive depths differ by exactly 1. Use this to answer range minimum queries on the tour in constant time after $O(n)$ preprocessing, with blocks of length $\frac12 \log_2 n$ and a table for every possible block pattern.

23. ★ Prove that the number of labeled trees on $\{1, \ldots, n\}$ in which vertex $i$ has degree $d_i$ is $(n - 2)! / \prod_i (d_i - 1)!$, using the [Prüfer code](/pruefer-code/). Sum over all degree sequences to recover $n^{n-2}$.

24. ★ Prove that every graph of treewidth $k$ has a vertex of degree at most $k$. Deduce that such graphs have degeneracy at most $k$ and can be colored with $k + 1$ colors.

25. ★ Show that every spanning tree of the cycle $C_n$ stretches some edge to distance $n - 1$. Then delete one edge of $C_n$ uniformly at random and show that every edge has expected stretch less than 2, the simplest case of a [probabilistic tree embedding](/metric-tree-embedding/).
