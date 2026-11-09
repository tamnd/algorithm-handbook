1. In order of weight: $ce$ 3 kept, $be$ 4 kept, $ad$ 5 kept, $df$ 6 kept, $ab$ 7 kept, $bc$ 8 rejected, $bd$ 9 rejected, $ef$ 10 rejected, $fg$ 11 kept. The tree is complete after six edges, so $eg$ and $de$ need not be examined. Its weight is 36.

2. $ad$ 5, $df$ 6, $ab$ 7, $be$ 4, $ec$ 3, $fg$ 11.

3. Round 1: $a$ and $d$ pick $ad$, $b$ picks $be$, $c$ and $e$ pick $ce$, $f$ picks $df$, $g$ picks $fg$. The components are $\{a, d, f, g\}$ and $\{b, c, e\}$. Round 2: both pick $ab$, and the tree is complete.

4. $bc$: $b, e, c$, maximum 4. $bd$: $b, a, d$, maximum 7. $de$: $d, a, b, e$, maximum 7. $ef$: $e, b, a, d, f$, maximum 7. $eg$: $e, b, a, d, f, g$, maximum 11.

5. In decreasing order, $de$ 15, $eg$ 12, $ef$ 10, $bd$ 9 and $bc$ 8 are deleted; $fg$ 11 is kept because, once $eg$ is gone, it is the only edge at $g$.

6. The only edges at $g$ are $eg$ 12 and $fg$ 11, and every spanning tree uses one of them.

7. Eight: of the $\binom{5}{3} = 10$ triples of edges, only the triangles $abc$ and $acd$ fail.

8. The cheapest swap adds $eg$ 12 and removes $fg$ 11, giving weight 37.

9. The cheapest arcs in are $c \to a$ 3, $a \to b$ 2, $b \to c$ 1, a cycle of cost 6. After contraction the arcs from $r$ cost $5 - 3 = 2$, $7 - 2 = 5$ and $8 - 1 = 7$, so $r \to a$ is chosen and $c \to a$ is dropped. The arborescence is $r \to a$, $a \to b$, $b \to c$, of cost 8.

10. A triangle with weights 1, 2, 3 and a pendant edge of weight 10 attached to it: every spanning tree has bottleneck 10, including the tree with the edges 2, 3 and 10.

12. Add $uv$ to $T$. It closes one cycle, of at most $n$ edges; remove its heaviest edge.

14. Sort the edges by counting sort in $O(m + W)$ time.

17. If another clustering is used, two points $p, q$ in one Kruskal cluster lie in different clusters of it. The path between them in the Kruskal forest has a step that crosses between those clusters, and that edge is no longer than the spacing Kruskal achieves.

20. The graph has exactly one cycle. Find it with a traversal and remove its heaviest edge.

21. In the distance graph, consecutive terminals are $2 - \varepsilon$ apart and all other pairs 2 apart, so its minimum spanning tree is the rim path, of cost $(k - 1)(2 - \varepsilon)$, and it uses no spoke. The optimum is the star of spokes, of cost $k$.

23. The cofactor equals $\frac{1}{n}$ times the product of the nonzero eigenvalues, which is $\frac{1}{n} n^{n-1}$.

25. A planar simple graph has $m \le 3n - 6$, and contraction keeps the graph planar. The rounds cost $O(n)$, $O(n/2)$, $O(n/4)$ and so on.
