1. ◦ Classify each algorithm as Las Vegas or Monte Carlo, and for the Monte Carlo ones say whether the error is one-sided: [randomized quicksort](/randomized-quicksort/); Freivalds' check of $AB = C$; the [Miller-Rabin test](/miller-rabin/); [Karger's minimum cut](/karger-min-cut/), run once.

2. ◦ A Monte Carlo algorithm has one-sided error at most $1/2$. How many independent runs bring the error below $10^{-6}$? How many if the error of one run is at most $1/4$?

3. ◦ A Las Vegas algorithm has expected running time 3 seconds on every input. Bound the probability that a run takes 15 seconds or more. If you stop each run at 15 seconds and start again with fresh coins, at most three times, bound the probability that all three runs are stopped.

4. ◦ Run [randomized quickselect](/randomized-quickselect/), with its three-way partition, on $A = [3, 8, 1, 9, 4, 7, 2, 6]$ and $k = 4$ (ranks from 0). Suppose the pivots drawn are the values 2, 7, 4 and 6, in this order. Give the range $[lo, hi)$ before each round, the number of comparisons in each round, and the answer.

5. ◦ In [randomized quicksort](/randomized-quicksort/) on $n$ distinct keys, the keys of ranks $i < j$ are compared with probability $2/(j - i + 1)$. For $n = 10$, what is the probability that the smallest and the largest key are compared? Two keys of adjacent ranks? Two keys whose ranks differ by 2?

6. ◦ A Las Vegas algorithm repeats a round that costs 5 steps and succeeds with probability $1/3$, independently of the other rounds. What is its expected number of steps? What is the probability that it needs more than 10 rounds?

7. • Randomized quickselect looks for the minimum ($k = 0$) of $n$ distinct keys, and a round on $m$ keys makes $m - 1$ two-way comparisons. Write a recurrence for the expected number $C(n)$ of comparisons, solve it, and evaluate it for $n = 10$.

8. • A Las Vegas algorithm stops after exactly $2^i$ steps with probability $2^{-i}$, for $i = 1, 2, \ldots$, so its expected time is infinite. Run it with a budget of $2^j$ steps and restart with fresh coins when the budget runs out. Find the expected total number of steps as a function of $j$, and the best $j$.

9. • A loop runs rounds until one succeeds, each with probability $1/2$, and round $t$ costs $t$ steps, since it handles all earlier work again. The expected number of rounds is 2. Is the expected cost $1 + 2 = 3$? Compute it.

10. • An array holds $n$ distinct numbers, $n$ even. You want any number of the upper half, that is, any of the $n/2$ largest numbers. Give a Las Vegas algorithm with $2(n - 1)$ comparisons in expectation, and a Monte Carlo algorithm with $k - 1$ comparisons and error $2^{-k}$.

11. • A decision algorithm with two-sided error is right with probability $2/3$ on every input. Use the bound $e^{-2\gamma^2 k}$ on the error of a majority vote to find a number $k$ of runs for which the majority is wrong with probability at most $10^{-6}$.

12. • [Karger's algorithm](/karger-min-cut/) finds a given minimum cut of a graph on $n = 20$ vertices with probability at least $2/(n(n - 1))$. How many independent runs, keeping the smallest cut found, make the probability of missing it at most $1/100$? Use the bound $1 - x \le e^{-x}$, then find the exact least number of runs.

13. • Colour each edge of the complete graph $K_n$ red or blue with a fair coin. Show that some colouring has at most $\binom{n}{3}/4$ triangles with all three edges of one colour, and evaluate the bound for $n = 6$ and $n = 10$.

14. • A [treap](/treap/) holds the keys $1, \ldots, n$ with independent random priorities. Key $j$ is an ancestor of key $i$ with probability $1/(|j - i| + 1)$. Find the expected number of proper ancestors of key $i$, and evaluate it for $n = 7$ and $i = 4$.

15. ★ Put the vertices of a graph in a uniformly random order and keep each vertex that comes before all its neighbours. Show that the kept vertices form an [independent set](/independent-set/) of expected size $\sum_v 1/(d(v) + 1)$, where $d(v)$ is the degree. What size does this guarantee for the star with one centre and five leaves, and for the path on five vertices? Compare with the largest independent sets.

16. ★ A hypergraph has $m$ edges, each a set of $k$ vertices. Show that if $m < 2^{k-1}$, the vertices can be coloured red and blue so that no edge has one colour. Then give a Las Vegas algorithm that finds such a colouring when $m \le 2^{k-2}$, with $O(km)$ expected time after reading the input. The seven lines of the Fano plane form a hypergraph with $k = 3$ that has no such colouring; why does this not contradict the first part?

17. ★ An array of $n$ cells holds $k \ge 1$ marked cells. A search probes cells in a uniformly random order without repeating a cell, until it finds a marked one. Show that the expected number of probes is $(n + 1)/(k + 1)$. Compare with the search that may repeat cells, for $n = 10$ and $k = 5$.

18. ★ In the setting of Exercise 7, let $R(n)$ be the expected number of rounds, counting the last one. Show that $R(n) = H_n$, and evaluate $R(7)$ as a fraction.
