## What to remember

- A **combinatorial optimization problem** has a finite but huge set of solutions. A symmetric TSP on $n$ cities has $(n-1)!/2$ tours, so enumeration fails at about 20 cities; the [Held-Karp](/held-karp-algorithm/) dynamic program over subsets needs only $O(n^2 2^n)$ time.
- The **0-1 knapsack problem** is NP-hard only in the weak sense: [dynamic programming](/knapsack-dynamic-programming/) solves it in pseudo-polynomial $\Theta(nW)$ time. The [ratio greedy](/greedy-fractional-knapsack/) solves the fractional relaxation in $\Theta(n \log n)$ time, with $f_{LP} < 2 f^*$ once every item fits alone, and the better of the greedy prefix and the best single item has value at least $f^*/2$.
- The **traveling salesman problem** has no polynomial-time approximation ratio for general costs unless P = NP. For metric costs, Christofides' algorithm has ratio $3/2$, and no ratio below $123/122$ is possible unless P = NP. The [nearest neighbor heuristic](/nearest-neighbor-heuristic/) runs in $\Theta(n^2)$ time, and its ratio on metric instances is $\Theta(\log n)$.
- The **vehicle routing problem** combines the TSP with bin packing. [Clarke-Wright savings](/clarke-wright-savings/) merges routes in the order of the savings $s(i, j) = c(0, i) + c(0, j) - c(i, j)$, and each merge lowers the cost by exactly $s(i, j)$; it has no proved ratio.
- **Minimum bisection** is NP-hard. For a graph with $n$ vertices, $n$ even, every bisection cuts at least $n \lambda_2 / 4$ edges, where $\lambda_2$ is the second smallest eigenvalue of the Laplacian. [Kernighan-Lin](/kernighan-lin/) swaps pairs with gain $D(a) + D(b) - 2w(a, b)$; [Fiduccia-Mattheyses](/fiduccia-mattheyses/) moves single vertices and does a pass in $\Theta(n + P)$ time.
- **Facility location** with metric costs has ratio 1.488, and no ratio below about 1.463 is possible under a complexity assumption. The **quadratic assignment problem** has no constant ratio unless P = NP, and exact methods reach only about $n = 30$.
- **Greedy is optimal for every weight function exactly on matroids** ([Rado-Edmonds](/rado-edmonds-theorem/)). Two matroids can be intersected in polynomial time, with $\max |I| = \min_U \bigl( r_1(U) + r_2(E \setminus U) \bigr)$; three matroids give an NP-hard problem.
- **Submodular functions** have diminishing returns. They can be minimized with polynomially many oracle calls, while maximizing them is NP-hard; for monotone $f$ under $|S| \le k$, greedy reaches $1 - 1/e$ of the optimum.
- **Lagrangian relaxation** gives the bound $\min \{ c^\top x : Ax \le b, \ x \in \operatorname{conv}(X) \}$ (Geoffrion), which is never weaker than the LP bound and equals it when $X$ has the integrality property.

## The main methods side by side

| Method | Problem | Time | Result |
|---|---|---|---|
| [Greedy fractional knapsack](/greedy-fractional-knapsack/) | fractional knapsack | $\Theta(n \log n)$ | optimal |
| [Knapsack dynamic programming](/knapsack-dynamic-programming/) | 0-1 knapsack | $\Theta(nW)$ | optimal |
| [Nearest neighbor](/nearest-neighbor-heuristic/) | metric TSP | $\Theta(n^2)$ | ratio $\Theta(\log n)$ |
| [Clarke-Wright savings](/clarke-wright-savings/) | capacitated VRP | $\Theta(n^2 \log n)$ | no proved ratio |
| [Kernighan-Lin](/kernighan-lin/) | bisection | $\Theta(n^3)$ per pass | local optimum, no ratio |
| [Fiduccia-Mattheyses](/fiduccia-mattheyses/) | bisection of hypergraphs | $\Theta(n + P)$ per pass | local optimum, no ratio |
| [Matroid intersection algorithm](/matroid-intersection-algorithm/) | two matroids | $O(n r^2 Q)$ | optimal, with certificate |
| [Lagrangian relaxation](/lagrangian-relaxation/) | integer programs with an easy core | one easy subproblem per step | lower bound |
| [Large neighborhood search](/large-neighborhood-search/) | any, with a repair method | set by a time limit | heuristic |

: The main methods of the chapter. For Fiduccia-Mattheyses, $P$ is the number of pins, the total size of the nets. For the matroid intersection algorithm, $r$ is the size of a largest common independent set and $Q$ the time of one independence test. Kernighan-Lin and Fiduccia-Mattheyses may need several passes; each applied pass lowers the cut.

## Choosing a method

- When the problem has matroid structure, use greedy; with two matroids, use the matroid intersection algorithm. Check the exchange property before you trust greedy.
- For knapsack, use dynamic programming when $W$ is small, and the fractional bound inside branch and bound when it is not.
- For tours and routes, start from nearest neighbor or savings, improve by local search or large neighborhood search, and compare with a lower bound, such as one from Lagrangian relaxation.
- For partitioning large sparse graphs and circuits, use Fiduccia-Mattheyses, inside a multilevel scheme for very large inputs. Use Kernighan-Lin for small graphs that need exactly equal halves.
- When you need a proof of optimality, combine a bound (LP, Lagrangian, or a matroid certificate) with branch and bound. A heuristic alone proves nothing about how far it is from the optimum.
