1. There are four dependences. S1 → S2 is a flow dependence on `A[i]` with distance 0, and S2 → S3 is an anti dependence on `C[i]` with distance 0; both are loop-independent. S2 → S1 is a flow dependence on `B` with distance 1, and S1 → S3 is a flow dependence on `A` with distance 2; both are carried by the $i$ loop.

3. The read `A[i-1][j][k+1]` gives the flow distance $(1, 0, -1)$, and `A[i][j][k-2]` gives $(0, 0, 2)$. Only loop 2 can be reversed. Reversing loop 1 turns the first vector into $(-1, 0, -1)$, and reversing loop 3 turns the second into $(0, 0, -2)$, both lexicographically negative. Loop 2 carries no dependence, and a script that ran all three reversed nests found that only the reversal of loop 2 kept the result.

4. The equation is $4i + 6j - 2i' - 8j' = c - 1$, and the gcd of the coefficients is 2. For $c = 4$ the constant 3 is odd, so there is no dependence. For $c = 5$ the constant 4 is even and the test says "maybe". Indeed there is a dependence: the write at $(1, 2)$ and the read at $(2, 1)$ both touch `A[17]`, a flow dependence with distance $(1, -1)$. Within the bounds there are 30 such pairs.

7. $b = 1$ comes from $(0, 1)$. Then $(1, -2)$ needs $a - 2 \ge 1$, so $a = 3$, and $(1, 1)$ needs only $a + 1 \ge 1$. With $\pi = (3, 1)$, $3i + j$ runs from 4 to 16: 13 wavefronts. No $\pi$ with entries up to 6 in absolute value does better.

8. $\delta = \lceil (5 - 1)/3 \rceil = 2$: S2 of iteration $i + 3$ may start once S5 of iteration $i$ has ended. A body takes 5 units and a new iteration starts every 2, so 3 processors are enough. The times are $2 \cdot 99 + 5 = 203$ with 3 processors, 252 with 2 processors and 500 sequentially.

10. On the whole equation $3i + 4j - 3i' - 4j' = 2$ the gcd is 1, so the test cannot decide, and in fact there are 180 dependent pairs. With $i = i'$ the equation becomes $4(j - j') = 2$, and 4 does not divide 2. So every dependence has a nonzero $i$ distance, which means that the $i$ loop carries all of them and the $j$ loop is parallel.

11. The gcd is 1. For Banerjee, write $h = (i - i') + 10(j - j')$. Over the box it ranges over $[-33, 33]$, which contains 5. Split by the direction of $j$: for $<$, $j - j' \in [-3, -1]$ gives $[-33, -7]$; for $=$ it gives $[-3, 3]$; for $>$ it gives $[7, 33]$. No range contains 5.

14. Look at the read of `A[i+1]` at $(t, i)$: its value comes from $(t - 1, i + 1)$, a distance $(1, -1)$. A rectangular tile that holds $(t - 1, i + 1)$ to the right of $(t, i)$ runs it too late. Skewing maps $(d_1, d_2)$ to $(d_1, d_2 + d_1)$, which makes every component nonnegative.

19. Allen-Kennedy first finds the strongly connected components at level 1, then drops the edges carried there and recurses at level 2. Check which of the two edges disappears, and which statement must come first in the $i$ body.

20. After skewing, $(d_1, d_2)$ becomes $(d_1, d_2 + f d_1)$, and after interchange it becomes $(d_2 + f d_1, d_1)$. The inner loop is parallel when every first component is positive. For the comparison, find a path through all 16 points that uses only the steps $(1, -1)$, $(1, -3)$ and $(0, 1)$.

21. Work with $k$ innermost first. `A[i][k]` moves along a row, so spatial reuse gives $1/l$; `B[k][j]` touches a new line each time, so the cost is 1; `C[i][j]` does not change, so $1/s$. Do the same for each set. The only dependence is $(0, 0, 1)$ on `C`, and it stays nonnegative under every permutation.

22. Inside a strip, a vector statement reads all its lanes before it writes any. A carried dependence from $S_p$ to $S_q$ with $p \ge q$ in the body breaks once $VL$ exceeds its distance; one with $p < q$ never does. The swap is legal because no dependence has distance 0.

23. Pair iteration $(a, b)$ with $(b, a)$ for $a < b$. The first reads `A[b][a]` and writes `A[a][b]`, and the second reads `A[a][b]` and writes `A[b][a]`. That gives one flow and one anti dependence per pair, both with direction $(<, >)$.
