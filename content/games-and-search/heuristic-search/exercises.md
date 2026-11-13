1. ◦ A graph has the directed edges S→A of cost 2, A→G of cost 2, S→B of cost 1 and B→G of cost 4, and G is the goal. Three heuristics give the values below on S, A, B and G. Which of them are [admissible](/admissible-heuristic/), and which are [consistent](/consistent-heuristic/)?

| | S | A | B | G |
|---|---|---|---|---|
| $h_1$ | 3 | 2 | 1 | 0 |
| $h_2$ | 4 | 3 | 0 | 0 |
| $h_3$ | 2 | 2 | 2 | 0 |

2. ◦ The graph Γ has the directed edges S→A 1, S→B 4, A→B 2, A→C 5, B→C 1, C→G 3 and B→G 6, the start S and the goal G, and the heuristic $h$ = 5, 4, 3, 2, 0 on S, A, B, C, G. Check that $h$ is consistent. Run [A*](/a-star-search/) as a graph search, with the goal test when a state is removed from the open list. List the states in the order they are expanded, with $g$ and $f$, and give the path and its cost.

3. ◦ Run [greedy best-first search](/greedy-best-first-search/) on the graph Γ (edges S→A 1, S→B 4, A→B 2, A→C 5, B→C 1, C→G 3, B→G 6; $h$ = 5, 4, 3, 2, 0 on S, A, B, C, G), ordered by $h$ alone, with the goal test at removal. Which path does it return, and how much more does it cost than the path of A*?

4. ◦ A search finds a solution at depth $d$ after generating $N$ nodes, not counting the root. Compute the [effective branching factor](/effective-branching-factor/) $b^*$ for $N = 39$, $d = 3$ and for $N = 30$, $d = 4$.

5. ◦ [Weighted A*](/weighted-a-star/) with $w = 1.3$ and an admissible heuristic, with reopening, returns a path of cost 52. What lower bound on the optimal cost $C^*$ follows? Which weight guarantees a path within 5 percent of $C^*$?

6. ◦ A* expands a state $n$ with $g(n) = 5$ and $h(n) = 9$, and generates a child $m$ by an action of cost 2, with $h(m) = 3$. Give $f(m)$ without and with the [pathmax](/pathmax/) rule $h(m) \leftarrow \max(h(m), h(n) - c(n, m))$.

7. ◦ A [pattern database](/pattern-database/) for the 15-puzzle stores one entry for each placement of 5 chosen tiles and the blank on the 16 squares. How many entries does it have? How many does it have if the blank is dropped from the key, as for a disjoint additive table?

8. ◦ For the 8-puzzle board 8 1 3 / 4 _ 2 / 7 6 5, with the goal 1 2 3 / 4 5 6 / 7 8 _, compute the misplaced tiles $h_{\text{mis}}$, the Manhattan distance $h_{\text{man}}$ and Gaschnig's heuristic $h_{\text{gas}}$ from the [relaxation](/relaxation-heuristic/) page. The board is 14 moves from the goal. Which of the three heuristics dominate which on all boards?

9. ◦ In [LPA*](/lifelong-planning-a-star/), a vertex $u$ has $g = 7$, $\mathrm{rhs} = 5$ and $h = 3$, a vertex $v$ has $g = 4$, $\mathrm{rhs} = 9$ and $h = 1$, and a vertex $w$ has $g = \mathrm{rhs} = 6$. Classify each as overconsistent, underconsistent or consistent, give the keys $[\min(g, \mathrm{rhs}) + h;\ \min(g, \mathrm{rhs})]$ of those in the queue, and say which one is expanded first.

10. ◦ For each of [jump point search](/jump-point-search/), [HPA*](/hierarchical-pathfinding-a-star/) and [Theta*](/theta-star/), say on which graph its path is guaranteed to be shortest, if any, and what is guaranteed otherwise.

11. • Run [IDA*](/iterative-deepening-a-star/) on the graph Γ (edges S→A 1, S→B 4, A→B 2, A→C 5, B→C 1, C→G 3, B→G 6; $h$ = 5, 4, 3, 2, 0 on S, A, B, C, G), with the successors in the order listed. Give the thresholds of the iterations, the states expanded in each, and the total number of expansions. Compare with A*.

12. • The graph Δ has the directed edges S→A 1, S→B 2, A→C 3, B→C 1 and C→G 3, and $h$ = 0, 0, 4, 0, 0 on S, A, B, C, G. Show that $h$ is admissible but not consistent. Run A* as a graph search with and without the reopening of closed states, and give the path and cost of each.

13. • On the 8-puzzle, take two pattern databases, one for the tiles 1 to 4 and one for the tiles 5 to 8, each with the blank in the key and each counting every move of the blank. Show that the maximum of the two is admissible but the sum is not, with a concrete board. What must change for the sum to be admissible?

14. • Let $h_1$ and $h_2$ be consistent. Show that $\max(h_1, h_2)$ and $\tfrac12(h_1 + h_2)$ are consistent. Then show that $h_1 + h_2$ need not be admissible, using $h_1 = h_2 = h$ on the graph Γ (edges S→A 1, S→B 4, A→B 2, A→C 5, B→C 1, C→G 3, B→G 6; $h$ = 5, 4, 3, 2, 0 on S, A, B, C, G).

15. • A search generates $N = 2000$ nodes and finds a solution at depth $d = 10$. Give the bounds $(N/d)^{1/d} \le b^* \le N^{1/d}$ and compute $b^*$ to three decimals by bisection.

16. • On the graph Γ (edges S→A 1, S→B 4, A→B 2, A→C 5, B→C 1, C→G 3, B→G 6; $h$ = 5, 4, 3, 2, 0 on S, A, B, C, G), which states must every algorithm in the class of the [optimal efficiency](/optimal-efficiency-of-a-star/) theorem expand? Is G among them?

17. • HPA* runs on an open 10 by 10 grid with 4 clusters of 5 by 5 cells and the transitions of its page: $(4, 2)$ and $(5, 2)$, $(4, 7)$ and $(5, 7)$, $(2, 4)$ and $(2, 5)$, $(7, 4)$ and $(7, 5)$. Find the length of its path from $(4, 0)$ to $(5, 0)$ and compare it with the optimum and with the bound $C^* + 2 \cdot \mathrm{gap} \cdot X$, with gap 2.

18. • An undirected graph has the edges S-D, S-X and X-G, each of cost 1, and the goal G. Run [LRTA*](/learning-real-time-a-star/) from S with $h_0$ = 1, 0, 1, 0 on S, D, X, G, until a trial changes no value. Give each walk and the values after each trial. Which value is still below its true distance at the end?

19. • [MM](/bidirectional-heuristic-search/) runs on a problem with $C^* = 12$. Four forward states have $(g_F, h_F)$ = (5, 6), (7, 2), (6, 6) and (4, 9). Compute their priorities $\max(f, 2g)$, and say which of them MM never expands.

20. • A complete binary tree has depth 4, and at each node the heuristic prefers child 0. Name each leaf by its four choices from the root. The only goal is the leaf 1100. Counting a leaf each time it is visited, how many leaf visits do depth-first search in the heuristic order, [limited discrepancy search](/limited-discrepancy-search/) as given by Harvey and Ginsberg, and Korf's ILDS make up to and including the goal?

21. • After a call of [ARA*](/anytime-repairing-a-star/) with $\varepsilon = 2.5$, the goal has $g = 45$, and the states of OPEN and INCONS have $g + h$ = 38, 40, 36 and 41. Give the reported bound $\varepsilon'$, and the interval in which $C^*$ must lie.

22. ★ Run weighted A* with $f = g + w\,h$ on the graph Γ (edges S→A 1, S→B 4, A→B 2, A→C 5, B→C 1, C→G 3, B→G 6; $h$ = 5, 4, 3, 2, 0 on S, A, B, C, G), with ties in $f$ broken toward larger $g$. For which weights $w \ge 1$ does it return the costs 7, 9 and 10? Check each cost against the bound $w C^*$.

23. ★ The optimal efficiency theorem says that an algorithm of its class must expand B on the graph Γ (edges S→A 1, S→B 4, A→B 2, A→C 5, B→C 1, C→G 3, B→G 6; $h$ = 5, 4, 3, 2, 0 on S, A, B, C, G). Build the instance that the proof uses to show this: add one goal state and one action, keep $h$ consistent, and give the new optimal cost. Why must an algorithm that does not expand B on Γ fail on the new instance?

24. ★ The ARA* page suggests setting the next weight just below the last bound $\varepsilon'$. Show that a weight above $\varepsilon'$ can still improve the bound. Use the directed edges s→x of cost 30, x→t of cost 6 and s→t of cost 45, the goal t, the consistent heuristic $h$ = 36, 6, 0 on s, x, t, and the weights 2.5 and then 2.

25. ★ IDA* runs with $h = 0$ and unit costs on a complete $b$-ary tree of depth $d$ whose only goal is the last leaf of the final iteration. Count the nodes it visits over all iterations, compare with one depth-first search of the whole tree, and find the limit of the ratio as $d \to \infty$. Give the numbers for $b = 2$, $d = 10$.

26. ★ A graph has the vertices 1, 2, 3 in a row and a vertex 4 attached to 2. Agent A goes from 1 to 3 and agent B from 3 to 1, under the rules of [multi-agent pathfinding](/multi-agent-pathfinding/): no two agents in one vertex at one time, no swap along an edge. Find the least sum of costs and the least makespan, prove that no plan has a sum of costs of 6, and say whether one plan reaches both optima.
