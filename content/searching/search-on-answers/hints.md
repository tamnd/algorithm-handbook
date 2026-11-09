1. (a) is monotone with threshold 8, since $7^2 = 49$. (c) is monotone with threshold 9: the best cut is $\langle 5, 1 \rangle, \langle 4, 2, 3 \rangle$. (b) and (d) are not monotone.

2. The answer is 12, with blocks $\langle 4, 8 \rangle, \langle 1, 6, 3 \rangle, \langle 9, 2 \rangle$. At $t = 11$ the greedy test makes four blocks, $\langle 4 \rangle, \langle 8, 1 \rangle, \langle 6, 3 \rangle, \langle 9, 2 \rangle$, so 11 is infeasible.

3. The answer is 4. At $d = 4$ the greedy test picks 0, 4, 11 and 16. At $d = 5$ it picks only 0, 7 and 12.

5. Ternary search: at most $2\lceil \log_{3/2} 1000 \rceil = 2 \cdot 18 = 36$. Fibonacci search: 15, since $F_{17} - 1 = 1596 \ge 1000 > F_{16} - 1 = 986$. Golden-section search: $1 + \lceil \log_\varphi 1000 \rceil = 16$.

8. Round 1: $\lambda = 10/4 = 2.5$, and $N - 2.5D$ is $0, 2, -3.5, 0.5$, so the minimizer is $(9, 5)$. Round 2: $\lambda = 9/5 = 1.8$, and the minimum of $N - 1.8D$ is 0, at $(9, 5)$, so the minimum ratio is $1.8$.

9. For $k = 1$ the office goes at the median house, 6, with total $5 + 4 + 0 + 1 + 14 = 24$. For $k = 2$ the blocks are $\{1, 2, 6, 7\}$ and $\{20\}$, with offices at 2 (or anywhere in $[2, 6]$) and at 20, and total 10.

10. The test is $\lfloor T/2 \rfloor + \lfloor T/3 \rfloor + \lfloor T/7 \rfloor \ge 10$; each term is non-decreasing in $T$. At $T = 11$ the sum is 9; at $T = 12$ it is 11, so $T = 12$.

11. The number of entries at most $v$ is $\sum_{i=1}^{m} \min(\lfloor v/i \rfloor, n)$, which is non-decreasing in $v$. Search for the least $v$ whose count is at least $k$. For the $3 \times 3$ table the sorted entries are $1, 2, 2, 3, 3, 4, 6, 6, 9$, and the 5th is 3.

13. $F$ is a minimum of finitely many linear functions of $\lambda$, each with slope $-D(x) < 0$. If $\lambda^*$ is the minimum ratio, then $N(x) - \lambda^* D(x) \ge 0$ for every $x$, with equality at the minimizer.

14. A ratio of at least $\lambda$ is reachable exactly when the $k$ largest values of $v_i - \lambda w_i$ have a non-negative sum. Sort and add, then binary search on $\lambda$. Here the best choice is the first two tests, with ratio $5/6$.

15. Count the pairs with $a_i + b_j \le s$ by two pointers in $O(m + n)$ time, and binary search on $s$. The sums are $3, 4, 6, 7, 8, 9, 10, 13, 15$, so the 4th smallest is 7.

17. About $10^5 \cdot 17 \cdot 10^5 \approx 1.7 \times 10^{11}$ updates for separate searches, since $\lceil \lg(10^5 + 1) \rceil = 17$. Parallel binary search makes 17 sweeps of $10^5$ updates, about $1.7 \times 10^6$.

18. The cost of a tour lies in $[0, nC]$. To find a tour, fix the optimal cost $t^*$, then try deleting each edge in turn (by setting its cost to $nC + 1$) and keep the deletion when a tour of cost $t^*$ still exists. The edges that remain form an optimal tour.

19. A cycle has mean less than $\lambda$ exactly when the graph with costs $c_e - \lambda$ has a negative cycle. The minimum mean is a fraction $p/q$ with $1 \le q \le n$, and two different such fractions differ by at least $1/n^2$. So shrink the interval below $1/n^2$, and return the one fraction with denominator at most $n$ inside it.

20. Map each double to its bit pattern, a 63-bit unsigned integer since the sign bit is 0, and run the integer search for the first true pattern. The order is the same, so the predicate is still monotone, and 64 tests are enough.

21. For a threshold $t$, walk the tree from the leaves up and keep the weight of the part of each subtree not yet cut off. Cut a subtree off as soon as that weight reaches $t$. Cutting as low as possible never leaves less weight for the rest, by an exchange argument. The value $t$ is feasible when this makes at least $k + 1$ parts, counting the remainder at the root only if it reaches $t$; extra parts can be merged with a neighbour.

22. Keep an interval of candidate distances. Count the distances in it with two pointers, pick one of them uniformly at random, and use one count to decide on which side the answer lies. Each round takes $O(n)$ time, and as in quickselect the expected number of rounds is $O(\log n^2) = O(\log n)$.
