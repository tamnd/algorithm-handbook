1. (a) Yes, with 6 edges: join $a$ to $b$, $c$, $d$, join $b$ to $c$ and $d$, and join $e$ to $f$. (b) No: the degree sum 15 is odd. (c) No: each vertex of degree 3 is adjacent to all three others, so the last vertex has degree 3, not 1. (d) Yes: $K_5$, with 10 edges.

3. Compressed sparse row: $\mathit{off} = [0, 2, 4, 5, 6, 7]$ and $\mathit{adj} = [1, 4, 2, 3, 0, 2, 3]$. Compressed sparse column: $\mathit{coff} = [0, 1, 2, 4, 6, 7]$ and $\mathit{src} = [2, 0, 1, 3, 1, 4, 0]$.

4. The candidates are 1, 2, 3, 3. Vertex 3 is the universal sink. The loop makes 4 probes; the check needs 8 entries, of which $A[2, 3]$ and $A[3, 4]$ were already read, so it makes 6 more, 10 in all.

5. The sequence is $(5, 5, 6, 3, 6)$. The decoded tree has the edges $23, 34, 13, 15, 56$.

6. The byte matrix takes $10^{10}$ bytes, 10 GB. The bitset takes $10^5 \cdot \lceil 10^5/64 \rceil = 1.563 \cdot 10^8$ words of 8 bytes, about 1.25 GB. Compressed sparse row stores each edge in both rows: $4(10^5 + 1 + 2 \cdot 10^6) \approx 8.4$ MB.

7. $L(K_4)$ has 6 vertices and $4 \binom{3}{2} = 12$ edges, and it is 4-regular. $L(K_3)$ and $L(K_{1,3})$ are both triangles, so two graphs that are not isomorphic can have the same line graph. This is the exception in Whitney's theorem.

9. $0 \to 1 \to 2 \to 5 \to 6 \to 7 \to 0$ is the only cycle, of length 6, so there is one component. The vertices 3, 4, 8 and 9 lie on no cycle; they point to 0, 7, 5 and 2.

10. The degrees lie in $\{0, \ldots, n - 1\}$, but 0 and $n - 1$ cannot both occur, so $n$ vertices take at most $n - 1$ values. For a multigraph, take the vertices $a, b, c$ with two edges $ab$ and one edge $bc$: the degrees are 2, 3, 1.

15. If $G$ is not connected, take $u$ and $v$. If they are in different components of $G$, they are adjacent in $\overline{G}$. If they are in the same component, pick $w$ in another one: $u w v$ is a path in $\overline{G}$.

18. Repeatedly remove vertices of in-degree 0, as in Kahn's algorithm, updating the in-degree of $f(v)$; the vertices never removed are exactly those on cycles. Then the distances to the cycles are found by a breadth-first search from all cycle vertices at once along the reversed edges, or by processing the removed vertices in reverse order of removal and setting $\mathit{dist}(v) = \mathit{dist}(f(v)) + 1$.

22. Vertex 1 is a leaf exactly when it does not occur in the sequence, and there are $(n - 1)^{n-2}$ sequences over the other labels. So vertex 1 is a leaf with probability $(1 - 1/n)^{n-2}$, and by symmetry and linearity of expectation the expected number of leaves is $n$ times this. The factor tends to $1/e$.

23. Answer "no edge" to each query unless that answer would leave the graph made of the "yes" pairs and the unasked pairs disconnected; then answer "yes". Each "yes" pair is a bridge of that graph when it is answered, and stays a bridge, since the graph only loses pairs later. If some pair $\{x, y\}$ is never asked, the "yes" pairs alone cannot connect $x$ to $y$, or that path and $\{x, y\}$ would put a "yes" pair on a cycle. So the graph of the "yes" pairs is disconnected while the graph with all unasked pairs added is connected, and both agree with every answer.

24. Write "(" when a depth-first walk enters a node and ")" when it leaves it. The number of ordered trees on $n$ nodes is the Catalan number $C_{n-1} = \frac{1}{n}\binom{2n-2}{n-1}$, and its logarithm is $2n - O(\log n)$.

25. Take $u$ and $v$ at distance at least 3 in $G$. They are not adjacent and have no common neighbour. So in $\overline{G}$ they are adjacent, and every other vertex is adjacent to $u$ or to $v$. Any two vertices then meet through $u$ or $v$ in at most three steps.

26. Each class contains at most $n!$ labelled graphs, one for each way to put labels on the vertices, and there are $2^{\binom{n}{2}}$ labelled graphs. Then use $\log_2 n! \le n \log_2 n$.
