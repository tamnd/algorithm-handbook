1. ◦ The graph $G$ has the vertices $a, \ldots, h$ and the 14 edges $ab, ac, bc, bd, cd, ce, de, df, ef, eg, fg, fh, gh, ah$. List its [maximal cliques](/maximal-clique/). Find the [clique number](/clique-number/), the [independence number](/independence-number/) and the [chromatic number](/chromatic-number/), each with a set or coloring that shows it.

2. ◦ Run [greedy coloring](/greedy-coloring/) on the graph $G$ of Exercise 1 in the order $a, b, c, d, e, f, g, h$, and then in the order $a, b, c, d, f, e, g, h$. Give the colors, numbered from 1, and say how many each order uses.

3. ◦ The crown graph on $2k$ vertices has the vertices $a_1, \ldots, a_k$ and $b_1, \ldots, b_k$, and joins $a_i$ to $b_j$ whenever $i \ne j$. For $k = 4$, run greedy coloring in the order $a_1, b_1, a_2, b_2, a_3, b_3, a_4, b_4$. How many colors does it use, and what is the chromatic number?

4. ◦ Compute a [smallest-last order](/degeneracy-ordering/) of the graph $G$ of Exercise 1, breaking ties alphabetically, and the [degeneracy](/degeneracy/). What bound on the number of colors does the order give, and how many colors does greedy coloring in the reverse order use?

5. ◦ Run [DSATUR](/dsatur/) on the graph $G$ of Exercise 1. Break ties first by the larger degree in $G$ and then alphabetically. Give the vertices in the order they are colored, with their colors.

6. ◦ A graph has the vertices $1, \ldots, 8$ and the edges $12, 13, 24, 35, 45, 46, 57, 68, 78$. Run the [bipartiteness test](/bipartiteness-testing/) by breadth-first search from vertex 1, scanning neighbours in increasing order. Give the layers, the edge that joins two vertices of one layer, and the odd cycle it closes. Then delete that edge and give a 2-coloring of what remains.

7. ◦ The house graph has a square $a, b, c, d$, with the edges $ab, bc, cd, da$, and a roof vertex $e$ joined to $c$ and $d$. Find its [chromatic polynomial](/chromatic-polynomial/) and use it to count the proper colorings with 3 colors and with 4 colors.

8. ◦ A graph has the vertices $a, \ldots, h$ and the edges $ab, ac, ad, bc, bd, cd, ce, de, df, ef, dh, eh, fh, ag$. Find a [perfect elimination ordering](/perfect-elimination-ordering/) by removing a simplicial vertex at each step, choosing the first alphabetically. Then [color the graph](/chordal-graph-coloring/) greedily in the reverse of that order, and give a clique that proves the coloring optimal.

9. ◦ Color the edges of $K_4$ with 3 colors so that edges at a common vertex differ. Then show that $K_5$ needs 5 colors, by counting how many edges one color can take. What is the [chromatic index](/chromatic-index/) of $K_n$ for even and for odd $n$?

10. • Prove that $\omega(G) \le \chi(G)$ and $n \le \alpha(G)\, \chi(G)$ for every graph on $n$ vertices. Deduce that $\chi(G)\, \chi(\overline{G}) \ge n$, where $\overline{G}$ is the complement.

11. • Run the [Welsh-Powell algorithm](/welsh-powell-algorithm/) on the graph $G$ of Exercise 1, breaking degree ties alphabetically. Compute its guarantee $\max_i \min(d_i + 1, i)$, where $d_1 \ge d_2 \ge \cdots$ are the degrees in the order used, and compare it with the number of colors the run uses.

12. • A simple planar graph with $n \ge 3$ vertices has at most $3n - 6$ edges. Use this to show that every planar graph has degeneracy at most 5, and hence that greedy coloring in a [smallest-last order](/degeneracy-ordering/) colors every planar graph with 6 colors in linear time.

13. • Prove that every graph has a vertex order in which greedy coloring uses exactly $\chi(G)$ colors. Explain why this does not give a fast exact algorithm.

14. • The Petersen graph has the outer cycle $0, 1, 2, 3, 4$, the spokes $i, i + 5$, and the inner edges $5\,7, 7\,9, 9\,6, 6\,8, 8\,5$. Find a proper 3-coloring. Then show that $K_n$ and odd cycles need $\Delta + 1$ colors, so that the exceptions in [Brooks' theorem](/brooks-theorem/) are needed.

15. • The [Mycielski construction](/mycielski-graph/) adds a copy $u_i$ of each vertex $v_i$, joined to the neighbours of $v_i$, and a vertex $w$ joined to every $u_i$. Show that $M(G)$ has $2n + 1$ vertices and $3m + n$ edges, and that it has no triangle when $G$ has none. For the Grötzsch graph $M(C_5)$, find the independence number and explain why neither $\omega$ nor $\lceil n / \alpha \rceil$ proves that it needs 4 colors.

16. • What is the largest number of edges in a graph on 7 vertices with no $K_4$? Give the extremal graph from [Turán's theorem](/turan-theorem/) and compare its edge count with the bound $(1 - \frac1r)\frac{n^2}{2}$.

17. • Using $R(3, 3) = 6$ and $R(2, 4) = 4$, show that $R(3, 4) \le 10$. Then improve the bound to 9: in a coloring of the edges of $K_9$ with no red triangle and no blue $K_4$, count the red neighbours of each vertex and reach a contradiction from parity. See [Ramsey's theorem](/ramsey-theorem/).

18. • For the graph $G$ of Exercise 1, evaluate $x^{\mathsf T} A x$ at the uniform vector on all 8 vertices and at the uniform vector on one triangle. Which is the maximum over the simplex, by the [Motzkin-Straus theorem](/motzkin-straus-theorem/)?

19. • Prove that greedy coloring in the reverse of a [perfect elimination ordering](/perfect-elimination-ordering/) uses exactly $\omega(G)$ colors. Conclude that chordal graphs are perfect.

20. • Find the [clique cover](/clique-cover/) number of the 7-cycle $C_7$ and compare it with $\alpha(C_7)$. Which coloring problem on the complement gives the same number?

21. • Give five arcs on a circle such that every point lies in at most two arcs, yet the arcs need 3 colors when overlapping arcs must differ. Explain why this cannot happen with intervals on a line, and what it says about [circular-arc coloring](/circular-arc-coloring/).

22. ★ Using a [smallest-last order](/degeneracy-ordering/) of degeneracy $d$, show how to list all triangles of a graph in $O(m d)$ time, and deduce that a graph with $m$ edges has $O(m^{3/2})$ triangles.

23. ★ In the random graph $G(n, \frac12)$ the expected number of cliques of size $k$ is $\binom{n}{k} 2^{-\binom{k}{2}}$. For $n = 1000$, find the smallest $k$ for which this is below 1, and compare it with $2 \log_2 n$. What does this mean for the [planted clique problem](/planted-clique/) with $k = 30$?

24. ★ The wheel $W_n$ is a cycle $C_n$ with a hub joined to every cycle vertex. Express its chromatic polynomial through that of $C_n$, count the proper 4-colorings of $W_5$ and the proper 3-colorings of $W_6$, and find $\chi(W_n)$ for every $n \ge 3$.

25. ★ Prove that a bipartite graph with maximum degree $\Delta$ has [chromatic index](/chromatic-index/) $\Delta$, by first adding vertices and edges to make it $\Delta$-regular and bipartite and then using [Hall's theorem](/hall-theorem/).

26. ★ Prove that $\chi(G) + \chi(\overline{G}) \le n + 1$ for every graph on $n$ vertices.
