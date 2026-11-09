1. ◦ Which of these tests on the integers $t \ge 0$ are [monotone predicates](/monotone-predicate/), false and then true? For each one that is, give the threshold. (a) $t^2 \ge 50$. (b) $t$ is prime. (c) The array $\langle 5, 1, 4, 2, 3 \rangle$ can be cut into at most two contiguous blocks with every block sum at most $t$. (d) $t \bmod 3 = 0$.

2. ◦ Solve the [linear partition](/minimax-partition/) problem for $\langle 4, 8, 1, 6, 3, 9, 2 \rangle$ and $k = 3$ blocks by binary search on the answer. Give the greedy split at the optimal value, and the number of blocks the greedy test uses at the value one less.

3. ◦ Solve [maximin placement](/maximin-placement/) for the positions $0, 3, 4, 7, 11, 12, 16$ and $k = 4$. Which positions does the greedy test pick at the optimal distance, and how many does it pick at the next larger distance?

4. ◦ An answer is an integer in $[1, 10^9]$. How many feasibility tests does [binary search on the answer](/binary-search-on-answer/) make? A real answer lies in $[0, 1000]$ and is wanted to within $10^{-6}$. How many halvings does [binary search on real numbers](/binary-search-on-real-numbers/) make?

5. ◦ A strictly unimodal function is given on 1000 integer points. How many evaluations does [ternary search](/ternary-search/) make at most, by the bound of its entry? How many does [Fibonacci search](/fibonacci-search-unimodal/) need? How many evaluations does [golden-section search](/golden-section-search/) need to shrink a real interval by a factor of 1000?

6. ◦ For the values $1, 3, 4, 8, 13$, list the ten pair distances in order and give the 4th smallest. Then count the distances at most 5 with the two-pointer pass of [k-th smallest pair distance](/kth-smallest-pair-distance/), and check the count against your list.

7. ◦ Which of these functions on the integers is a [unimodal function](/unimodal-function/) in the sense of the chapter (with a minimum)? (a) $f(x) = |x - 3|$. (b) $f(x) = x^2 - 4|x|$. (c) $f(x) = 7$. (d) $f(x) = (x - 2)^2$ for $x \ge 0$ and $f(x) = 4 - x$ for $x < 0$.

8. ◦ A finite set of solutions has the pairs $(N, D)$ equal to $(10, 4)$, $(7, 2)$, $(9, 5)$ and $(3, 1)$. Run [Dinkelbach's algorithm](/dinkelbach-algorithm/) to minimize $N/D$, starting from $(10, 4)$. Give $\lambda$ and the minimizer of $N - \lambda D$ in each round.

9. ◦ Houses stand at $1, 2, 6, 7, 20$ on a line. Solve the [post office problem](/post-office-problem/) for $k = 1$ and for $k = 2$, giving the positions and the total distances.

10. • Three machines make one item every 2, 3 and 7 minutes. Write the feasibility test for "10 items can be made within $T$ minutes", show that it is monotone, and find the least $T$.

11. • The multiplication table of size $m \times n$ has the entry $ij$ in row $i$ and column $j$. Find its $k$-th smallest entry in $O(m \log(mn))$ time without building it. What is the 5th smallest entry of the $3 \times 3$ table?

12. • A strictly unimodal function on $n$ integer points has a maximum. Compare $f(mid)$ with $f(mid + 1)$ instead of using two points at the thirds. How many evaluations does this make, and how does it compare with ternary search?

13. • For a ratio problem with $D(x) > 0$ on a finite set $X$, let $F(\lambda) = \min_{x \in X} (N(x) - \lambda D(x))$. Prove that $F$ is concave and strictly decreasing, and that $F(\lambda) = 0$ exactly when $\lambda$ is the minimum ratio.

14. • Each of $n$ tests has a score $v_i$ and a maximum $w_i > 0$. Choose $k$ tests to maximize $\sum v_i / \sum w_i$. Give the test for "a ratio of at least $\lambda$ is reachable" in $O(n \log n)$ time. Solve it for $v = (5, 0, 2)$, $w = (5, 1, 6)$ and $k = 2$.

15. • For sorted arrays $a$ and $b$ of integers, find the $k$-th smallest of the sums $a_i + b_j$ in $O((m + n) \log U)$ time, where $U$ is the range of the sums. What is it for $a = \langle 1, 4, 6 \rangle$, $b = \langle 2, 3, 9 \rangle$ and $k = 4$?

16. • After $O(n)$ preprocessing with prefix sums, answer the feasibility test of linear partition for a given $t$ in $O(k \log n)$ time instead of $O(n)$. When does this help?

17. • There are $T = 10^5$ updates and $Q = 10^5$ queries. A separate binary search on the answer for each query replays the updates from the start for each test. About how many updates does it apply in all? About how many does [parallel binary search](/parallel-binary-search/) apply?

18. • A decision procedure answers "is there a tour of cost at most $t$?" for a travelling salesman instance with $n$ cities and integer costs at most $C$. Find the cost of the best tour with $O(\log(nC))$ calls. Then find a best tour itself with polynomially many calls.

19. ★ A directed graph has $n$ vertices, $m$ edges and integer costs in $[-W, W]$. Show how to find the exact minimum mean cost of a cycle by a binary search on the answer with $O(\log(nW))$ runs of a negative cycle test. Why can the search stop at a finite precision and still be exact?

20. ★ The non-negative IEEE double numbers are in the same order as their 64-bit patterns read as unsigned integers. Use this to find the exact threshold of a monotone predicate on the non-negative doubles with at most 64 tests.

21. ★ A tree has $n$ vertices with non-negative weights. Cut exactly $k$ edges so that the smallest total weight of a resulting component is as large as possible. Give an $O(n \log S)$ algorithm, where $S$ is the total weight, and prove the greedy test it uses.

22. ★ Find the $k$-th smallest pair distance of $n$ numbers in $O(n \log n)$ expected time, independent of the range of the values.
