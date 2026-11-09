1. ◦ An algorithm gets an array of integers and uses the values only in comparisons. For each question, say whether it has the same answer on the array and on its compressed ranks: (a) are two items equal; (b) the length of a longest strictly increasing subsequence; (c) the number of distinct values; (d) the largest difference between two items; (e) the sum of the items.

2. ◦ A duplicate test on $n = 16$ items either compares all pairs, or sorts by merge sort and then compares neighbours. Take the worst case of merge sort to be $n \lceil \lg n \rceil - 2^{\lceil \lg n \rceil} + 1$ comparisons. Give both worst-case counts.

3. ◦ Merge the closed intervals $[5, 7]$, $[1, 2]$, $[6, 9]$, $[2, 4]$, $[11, 13]$ by sorting them on the left end and scanning once. Intervals that touch at one point are merged.

4. ◦ Compute $\operatorname{lcm}(84, 90, 33)$ with two calls to a gcd routine and no factorization. Give both gcds.

5. ◦ Give the canonical form of each object: the fraction $84/(-126)$ in lowest terms with a positive denominator; the multiset $\{3, 1, 3, 2\}$ as a sorted tuple; the undirected edge $\{7, 2\}$ as an ordered pair; the string `baca` under rotation, as its least rotation.

6. ◦ The formula $f_n = (x_1 \land y_1) \lor \cdots \lor (x_n \land y_n)$ needs $2^n$ clauses in any equivalent CNF, and its Tseitin encoding has $3n + 1$ clauses. Find the smallest $n$ for which the Tseitin encoding has fewer clauses, and give both counts there.

7. ◦ Give the number of vertices, the number of edges and the number of connected components of the bipartite double cover of (a) the path $P_4$ on 4 vertices, (b) the complete graph $K_5$, (c) the cycle $C_6$. For (b), name the graph you get.

8. ◦ A directed graph has $n = 6$ vertices and $m = 9$ edges, and all vertices except $s$ and $t$ have a capacity. How many vertices and edges does the split graph have? Answer again for an undirected graph with 6 vertices and 9 edges, where each undirected edge is first replaced by two opposite arcs.

9. ◦ A network has $m = 10$ edges with integer capacities at most $C = 1000$. For capacity scaling, give the first threshold $\Delta_0$, the number of phases and the bound on the number of augmentations. For generic Ford-Fulkerson, give the bound $mC$ on the number of augmentations. For bit scaling with largest length $W = 1000$, give the number of phases $K$.

10. • Suppose $A$ reduces to $B$ by a transform that runs in $O(n)$ time and keeps the size. Which of these follow? (a) An $O(n \log n)$ algorithm for $B$ gives one for $A$. (b) An $\Omega(n \log n)$ lower bound for $B$ gives one for $A$. (c) An $\Omega(n \log n)$ lower bound for $A$ gives one for $B$. (d) An $O(n)$ algorithm for $A$ gives one for $B$. Then apply your answer to the reduction of element distinctness to sorting.

11. • A decision oracle answers "does some subset of the numbers sum to $t$". To find such a subset, go through the items in order and delete item $i$ whenever the instance without it still has a solution. Run this on $a = (4, 7, 9, 2)$ and $t = 13$, starting with one call on the whole instance. Which subset is returned, and how many calls are made in total?

12. • Build the implication graph of $(x_1 \lor x_2) \land (\lnot x_1 \lor x_2) \land (\lnot x_2 \lor x_3) \land (\lnot x_3 \lor \lnot x_2)$, list its 8 arcs, and decide whether the formula is satisfiable by finding a cycle or a strongly connected component.

13. • The h-index of a list of citation counts is the largest $h$ such that at least $h$ counts are at least $h$. Give an algorithm by presorting and its cost, and compute the h-index of $(3, 0, 6, 1, 5)$ and of $(10, 8, 5, 4, 3)$.

14. • Compress $(10^9, 3, 10^6, 3, 7, 10^9 + 1)$ to 1-based ranks. Then give the length of a longest strictly increasing subsequence and of a longest non-decreasing subsequence.

15. • Two subspaces of $\mathbb{Q}^3$ are spanned by $\{(1, 2, 3), (2, 4, 7)\}$ and by $\{(1, 2, 4), (0, 0, 1)\}$. Decide whether they are equal by computing the reduced row echelon form of each pair of rows.

16. • Compute the AHU string codes, with children sorted in the order where "(" comes before ")", of three rooted trees: $T_1$, whose root has children $a$ and $b$, with $a$ having two leaf children and $b$ one; $T_2$, whose root has children $x$ and $y$, with $x$ having one leaf child and $y$ two; and $T_3$, whose root has a leaf child and a child with three leaf children. Which trees are isomorphic?

17. • A graph has the arcs $s \to a$ of length 6, $s \to b$ of length 3, $b \to a$ of length 2, $a \to t$ of length 5 and $b \to t$ of length 7. Run bit scaling: give $K$, then for each phase the reduced lengths $r$, the distances $\delta$ and the new $d$, with vertices in the order $(s, a, b, t)$.

18. • Write a linear program for this problem: given $c_1, \ldots, c_n$, find $x_1 \le x_2 \le \cdots \le x_n$ that minimize $\sum_i |x_i - c_i|$. Solve it for $c = (3, 1, 2)$ and prove the optimum.

19. • $G$ is the cycle $0, 1, \ldots, 6$ with the extra edge $\{0, 3\}$. For each vertex $v$, give the distance from $(v, 0)$ to $(v, 1)$ in the bipartite double cover, and the length of a shortest odd cycle of $G$.

20. • Find a minimum cover of the vertices of the DAG with arcs $1 \to 2$, $1 \to 3$, $2 \to 4$, $3 \to 4$, $4 \to 5$, $4 \to 6$ by vertex-disjoint paths, through a maximum matching in the split bipartite graph. Give the matching, the number of paths and the paths.

21. ★ Define a canonical form of a graph on $n$ labelled vertices as the lexicographically smallest string of upper-triangle adjacency bits $a_{12} a_{13} a_{23} \ldots$ over all $n!$ relabellings. Give the form for each of the four graphs on 3 vertices up to isomorphism, and the cost of the method for $n = 10$ in relabellings.

22. ★ Show that in the comparison model, coordinate compression of $n$ distinct values needs $\Omega(n \log n)$ comparisons in the worst case.

23. ★ Write the linear programming relaxation of minimum vertex cover for $K_n$. Prove that its optimum is $n/2$, give the integer optimum, and find the limit of their ratio as $n \to \infty$.

24. ★ A cycle cover of a directed graph is a set of vertex-disjoint directed cycles that together contain every vertex. Reduce the search for a cycle cover to perfect matching in a bipartite graph, and use the reduction to list all cycle covers of the graph with arcs $1 \to 2$, $2 \to 1$, $2 \to 3$, $3 \to 4$, $4 \to 3$, $4 \to 1$.

25. ★ The bipartite graph with $L = \{1, 2, 3\}$, $R = \{a, b, c\}$ and edges $1a$, $2a$, $3a$, $3b$, $3c$ becomes a flow network with unit capacities. Find a maximum flow, the set $S$ of vertices reachable from $s$ in its residual graph, the arcs of the cut, and the vertex cover $(L \setminus S) \cup (R \cap S)$. Check that the cover has the size of a maximum matching.
