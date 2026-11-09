1. ◦ Which of these are the degree sequences of simple undirected graphs: (a) $3, 3, 2, 2, 1, 1$; (b) $3, 3, 3, 3, 3$; (c) $3, 3, 3, 1$; (d) $4, 4, 4, 4, 4$? For each one that is, give the number of edges and draw a graph with that sequence. For each one that is not, say why.

2. ◦ A directed graph on $\{0, 1, 2, 3, 4\}$ has the edges $(0,1), (0,4), (1,2), (1,3), (2,0), (3,2), (4,3)$. Write its [adjacency lists](/adjacency-list/) and those of its [transpose](/transpose-graph/), each list in increasing order. Give the in-degree and the out-degree of each vertex, and check both sums against the [handshake lemma](/handshake-lemma/).

3. ◦ For the graph of Exercise 2, write the two arrays of its [compressed sparse row](/compressed-sparse-row/) form, with sorted rows, and the two arrays of its [compressed sparse column](/compressed-sparse-column/) form.

4. ◦ Run the elimination method of the [universal sink](/universal-sink/) entry on the matrix with rows $01010$, $00111$, $10010$, $00000$, $00110$ (vertices $0$ to $4$). Give the candidate after each probe, the answer, and the number of probes in all if an entry already read is not read again.

5. ◦ Find the [Prüfer sequence](/prufer-sequence/) of the tree on $\{1, \ldots, 7\}$ with the edges $15, 25, 35, 36, 46, 67$. Then find the tree on $\{1, \ldots, 6\}$ whose Prüfer sequence is $(3, 3, 1, 5)$.

6. ◦ An undirected graph has $n = 10^5$ vertices and $m = 10^6$ edges. How many bytes does it take as an [adjacency matrix](/adjacency-matrix/) with one byte per cell, as a [bitset adjacency matrix](/bitset-adjacency-matrix/), and in compressed sparse row form with 32-bit offsets and entries?

7. ◦ How many vertices and edges does the [line graph](/line-graph/) of $K_4$ have, and is it regular? Draw the line graphs of the triangle $K_3$ and of the star $K_{1,3}$. What do they show about recovering $G$ from $L(G)$?

8. ◦ A rooted tree on $\{0, \ldots, 6\}$ with root 0 is given by the [parent array](/parent-pointer-tree/) $[-, 0, 0, 1, 1, 1, 2]$. Write its [left-child right-sibling](/left-child-right-sibling/) links, with the children of each node in increasing order. List the nodes of the tree in preorder, and the nodes of the binary tree given by the two links in preorder.

9. ◦ Draw the [functional graph](/functional-graph/) of $f(x) = (x^2 + 1) \bmod 10$ on $\{0, \ldots, 9\}$. How many weakly connected components does it have, how long is each cycle, and which vertices lie on no cycle?

10. • Prove that every simple graph with at least two vertices has two vertices of the same degree. Give a multigraph without self-loops for which this fails.

11. • Show that a $k$-[regular graph](/regular-graph/) on $n$ vertices has $kn/2$ edges, so that $n$ is even when $k$ is odd. Give a 3-regular graph on six vertices that is [bipartite](/bipartite-graph/) and one that is not.

12. • Show that the [square](/graph-square/) of the cycle $C_n$ is 4-regular for $n \ge 5$. Show that $C_5^2 = K_5$ and that $C_6^2$ is $K_6$ with a perfect matching removed.

13. • Let $A$ be the adjacency matrix of a simple undirected graph. Prove by induction on $k$ that the entry $(u, v)$ of $A^k$ is the number of walks of length $k$ from $u$ to $v$. Deduce that the trace of $A^3$ is six times the number of triangles, and check it on $K_4$ by computing $A^3$.

14. • For the unsigned [incidence matrix](/incidence-matrix/) $B$ of a simple graph, show that $B^T B = 2I + A(L(G))$, where $A(L(G))$ is the adjacency matrix of the line graph. Check it on the path with the vertices $1, 2, 3, 4$ in order.

15. • Prove that for every simple graph $G$, at least one of $G$ and its [complement](/complement-graph/) $\overline{G}$ is connected.

16. • Prove that a forest with $n$ vertices and $c$ components has exactly $n - c$ edges. Deduce that an undirected graph with $m \ge n$ edges has a cycle, and that a [DAG](/directed-acyclic-graph/) can still have $\binom{n}{2}$ edges.

17. • The $d$-dimensional hypercube has the $d$-bit strings as vertices and an edge between two strings that differ in one bit. Treat it as an [implicit graph](/implicit-graph/): give its numbers of vertices and edges, a rule that lists the neighbours of a vertex with word operations, and a proof that it is bipartite. How many vertices of the 10-dimensional cube are at distance exactly 3 from $00 \cdots 0$?

18. • A functional graph is given as an array $f[0 \ldots n-1]$. Give a $\Theta(n)$ algorithm that marks the vertices that lie on a cycle and computes, for every vertex, the number of steps it takes to reach a cycle.

19. • Use a bitset adjacency matrix to count the triangles of a simple graph with $n$ vertices and $m$ edges in $O(m \lceil n/w \rceil)$ word operations. Why must the sum you compute be divided by 3?

20. • An input file lists the $m$ edges of a directed graph on $n$ vertices, possibly with repeated edges and self-loops. Build its compressed sparse row form with sorted rows, no repeated entries and no self-loops in $\Theta(n + m)$ time.

21. • Show that $\binom{N}{m} \ge (N/m)^m$ for $1 \le m \le N$. Deduce that some directed graph with $n = 2^{20}$ vertices and $m = 2^{24}$ edges needs at least 16 bits per edge in any representation, and compare with compressed sparse row using $\lceil \log_2 n \rceil$-bit entries.

22. ★ Using Prüfer sequences, show that the number of labelled trees on $\{1, \ldots, n\}$ in which vertex 1 is a leaf is $(n - 1)^{n-2}$. Deduce that the expected number of leaves of a uniformly random labelled tree on $n$ vertices is $n(1 - 1/n)^{n-2}$, which is about $n/e$.

23. ★ An algorithm decides whether an undirected graph on $n \ge 2$ vertices is connected, and it may only ask [adjacency queries](/adjacency-query/). Prove that it must ask all $\binom{n}{2}$ queries in the worst case.

24. ★ Show that a rooted tree on $n$ nodes whose children are ordered can be stored in $2n$ bits, from which its shape can be rebuilt. Show that every such encoding needs $2n - O(\log n)$ bits for some tree.

25. ★ Prove that if a simple graph $G$ has diameter at least 3, then its complement has diameter at most 3.

26. ★ Show that the number of isomorphism classes of graphs on $n$ vertices is at least $2^{\binom{n}{2}}/n!$. Conclude that a representation of unlabelled graphs, one code word per class, needs at least $\binom{n}{2} - n \log_2 n$ bits for some graph, so forgetting the labels saves at most about $n \log_2 n$ of the $\binom{n}{2}$ bits of the matrix.
