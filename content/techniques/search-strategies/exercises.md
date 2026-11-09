1. ◦ A directed graph has the edges S→A of cost 2, S→B of cost 5, A→B of cost 2, A→C of cost 6, B→C of cost 1, B→G of cost 9 and C→G of cost 3. How many nodes does the [search tree](/search-tree/) rooted at S have? In how many nodes does G appear, and what are the costs of the paths they stand for?

2. ◦ Name the strategy that each [frontier](/search-frontier/) gives: (a) a first-in first-out queue; (b) a stack; (c) a priority queue on the path cost $g$; (d) a priority queue on a heuristic $h$; (e) a priority queue on $g + h$. On an infinite tree with finite branching factor, actions of cost 1 and a goal at some finite depth, which of the five are sure to find a goal, if the heuristic in (d) and (e) is admissible?

3. ◦ On a uniform tree with branching factor 4 and the shallowest goal at depth 5, count the nodes that breadth-first search generates in a full search to depth 5 and the nodes that [iterative deepening](/iterative-deepening-search/) generates in its six runs, without counting the root. Compare the ratio with $b/(b-1)$.

4. ◦ A piece moves on an unbounded square grid like a chess king, to any of its 8 neighbors. How many cells can it reach in at most 5 moves? How many nodes does the search tree have down to depth 5? What do the two numbers say about [graph search and tree search](/graph-search-vs-tree-search/) here?

5. ◦ On a uniform tree with branching factor 10 in both directions and a goal at depth 8, count the nodes, not counting the two roots, that one breadth-first search generates to depth 8, and the nodes that [bidirectional search](/bidirectional-search/) generates when each side goes to depth 4.

6. ◦ A process starts at $x_0 = 4$ and follows $x_{i+1} = (x_i^2 + 1) \bmod 17$. [Simulate](/simulation-technique/) it with a table of the states seen, until a state repeats. Give the tail length $\mu$, the cycle length $\lambda$, and $x_{10^9}$.

7. ◦ Take the cycle on four vertices $a, b, c, d$, with edges $ab$, $bc$, $cd$ and $da$, and the cut $\{a, b\}$ against $\{c, d\}$. As a [local search problem](/local-search-problem/) for Max-Cut with single-vertex flips, is this cut a local optimum? What fraction of the largest cut does it reach, and what does that say about the bound that every local optimum cuts at least half the edges?

8. ◦ A tree has root S with children A and B; A has children C and D; B has the child E; D has the child G, the only goal; C, E and G have no children. Run [depth-limited search](/depth-limited-search/) with limits 0, 1, 2 and 3, children in the order given. For each limit, give the answer (a path, *cutoff* or *failure*) and the number of goal tests. What does iterative deepening return, after how many goal tests? How do the answers change if G is not a goal?

9. • Run [uniform-cost search](/uniform-cost-search/) as graph search on the graph of Exercise 1, with the goal test when a node is selected. Give the order of expansions, the frontier after each one, and the path returned. Which path does it return if the goal test is moved to the moment a node is generated?

10. • On the graph of Exercise 1 take the heuristic $h(S) = 7$, $h(A) = 5$, $h(B) = 3$, $h(C) = 3$, $h(G) = 0$. Check that it is admissible and consistent. Run greedy [best-first search](/best-first-search/) ($f = h$) and A* ($f = g + h$), both as graph search with the goal test at selection. Which paths do they return, and at what cost?

11. • On the graph of Exercise 1 take the heuristic $h(S) = 0$, $h(A) = 6$, $h(B) = 0$, $h(C) = 3$, $h(G) = 0$. Show that it is admissible but not consistent. Run A* as graph search twice: once without reopening states that have already been expanded, and once with reopening. Give the path, its cost and the number of expansions in each run.

12. • Let $S_d = b + b^2 + \cdots + b^d$ be the number of nodes that breadth-first search generates on a uniform tree down to depth $d$, not counting the root. Prove that iterative deepening generates exactly $b(S_d - d)/(b - 1)$ nodes in its runs with limits $1, \ldots, d$, and so fewer than $S_d \cdot b/(b-1)$. Check the formula on Exercise 3.

13. • A chain of $k$ diamonds has states $v_0, v_1, \ldots, v_k$ and, for each $i$, two states $a_i$ and $b_i$ with edges $v_{i-1} \to a_i \to v_i$ and $v_{i-1} \to b_i \to v_i$. Show that the search tree from $v_0$ has $2^{k+2} - 3$ nodes, against $3k + 1$ states. If no state is a goal, how many times does tree-like depth-first search expand $v_{k-1}$, and how many times does it reach $v_k$? How many expansions does graph search make?

14. • A uniform tree has branching factor 3 and depth 2, and its nodes are the sequences over $\{0, 1, 2\}$ of length at most 2, with children in increasing order. Count the goal tests of depth-first search and of [iterative broadening](/iterative-broadening/), which starts with breadth limit 2, when the only goal is the leaf $(1, 1)$, and again when it is the leaf $(2, 0)$.

15. • In Max-Cut without weights, each move flips one vertex to the other side and must increase the number of cut edges. Show that local search stops after at most $|E|$ moves, and so finds a local optimum in polynomial time. Which step of this argument fails when the edges carry weights?

16. • The forward search from a start has branching factor 2 and the backward search from the goal has branching factor 8; the goal is at depth 12. If the forward side searches to depth $k$ and the backward side to depth $12 - k$, how many nodes do they generate together, not counting the two roots? Which $k$ is best, and how does it compare with a forward search alone? Show that the rule "expand the side whose frontier is smaller" reaches the best split.

17. • Iterative lengthening is iterative deepening with a limit on the path cost: each run expands the nodes with $g$ at most the limit, and the next limit is the least $g$ above the old limit. On a chain $v_0 \to v_1 \to \cdots \to v_n$ with positive costs and the goal $v_n$, how many expansions does it make in all? How many does uniform-cost search make? What happens on a tree in which the $N$ nodes with $g \le C^*$ all have different costs?

18. • A graph has the edges S→A and A→S, both of cost 0, and A→G of cost 1. Show that uniform-cost search as tree search, with no check on repeated states, never returns, though a goal of cost 1 exists. Show that graph search returns S-A-G. Which condition in the [completeness](/completeness-and-optimality-of-search/) result for uniform-cost search does this graph break?

19. ★ Iterative broadening with breadth limits $c = 2, 3, \ldots, b$ on a uniform tree of depth $d$ looks at $c^d$ leaves in run $c$. Prove that $\sum_{c=2}^{b} c^d < (1 + b/(d+1))\, b^d$, so the total is less than $1 + b/(d+1)$ times the last run. For which $b$ and $d$ is the factor below 2? Compute the sum and the bound for $b = 10$ and $d = 5$.

20. ★ A bidirectional uniform-cost search runs on the undirected graph with edges S–A of cost 2, A–B of cost 4, B–G of cost 1, S–M of cost 3 and M–G of cost 5. The two sides take turns, forward first, and each turn expands the node with the least $g$ on that side. Show that the rule "stop as soon as a state has been reached by both sides" returns a path of cost 8, though a path of cost 7 exists. Then let $\mu$ be the least cost of a path through a state reached by both sides, and stop when the least $g$ on the forward frontier plus the least $g$ on the backward frontier is at least $\mu$. Prove that this rule returns a cheapest path, and run it on the graph.

21. ★ The spanning trees of a connected weighted graph form a local search problem: a move removes one tree edge and adds one non-tree edge that joins the two parts again. Prove that every local optimum of this neighborhood is a minimum spanning tree, so that local search here returns a global optimum.

22. ★ A heuristic $h$ is consistent if $h(\text{goal}) = 0$ and $h(u) \le c(u, v) + h(v)$ for every edge $u \to v$. Prove that a consistent heuristic is admissible, that $f = g + h$ never decreases along a path, and that A* as graph search with a consistent heuristic has found a cheapest path to each state when it selects that state, so that it never needs to reopen one. Which edge breaks consistency in Exercise 11?
