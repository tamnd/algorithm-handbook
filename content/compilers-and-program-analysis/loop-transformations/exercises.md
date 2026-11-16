1. ◦ The loop `for i = 1 to 10` has the body `S1: A[i] = B[i-1] + 1`, `S2: B[i] = A[i] * C[i]`, `S3: C[i] = A[i-2]`. List every [data dependence](/data-dependence/) between the statements, with its kind (flow, anti or output) and its distance in $i$. Which of them are [loop-carried](/loop-carried-dependence/)?

2. ◦ A depth-3 nest has the [distance vectors](/dependence-distance-vector/) $(0, 1, -1)$, $(1, -2, 0)$ and $(1, 0, 3)$. Give the [direction vector](/dependence-direction-vector/) of each, the level of the loop that carries it, and say which of the three loops is a [DOALL loop](/doall-loop/).

3. ◦ The nest `for i, j, k = 1 to 4` has the body `A[i][j][k] = A[i-1][j][k+1] + A[i][j][k-2]`. Find its distance vectors. Which single loop can be reversed without changing the result, by the [legality theorem](/loop-transformation-legality/)?

4. ◦ A double loop with $1 \le i, j \le 5$ writes `A[4i+6j+1]` and reads `A[2i+8j+c]`. Apply the [GCD test](/gcd-test/) for $c = 4$ and for $c = 5$. When the test does not prove independence, give a write iteration and a read iteration that touch the same element.

5. ◦ Write the [chain of recurrences](/chains-of-recurrences/) of $f(i) = 2i^2 - i + 3$ for $i = 0, 1, 2, \dots$ Evaluate it for $i = 0$ to $5$ by additions only, and check the values against $f$.

6. ◦ Before the loop `for i = 0 to 5`, the code sets `j = 2; k = 1; p = 9`. The body first uses `j`, `k` and `p`, then runs `j = j + 3; k = k * 2; p = i`. By [induction variable analysis](/induction-variable-analysis/), give the class of each variable and its value at the use in iteration $i$.

7. ◦ A nest over $1 \le i, j \le 4$ has the distance vectors $(1, -2)$, $(0, 1)$ and $(1, 1)$. Use the [Lamport hyperplane method](/lamport-hyperplane-method/): choose the coefficients of $\pi = (a, b)$ from the inner loop outward, each as small as possible with $\pi \cdot d \ge 1$ for every $d$. How many wavefronts $\pi \cdot (i, j) = t$ does the nest have?

8. ◦ A loop body has five statements S1 to S5, each taking one time unit, run in that order. The only carried dependence goes from S5 in iteration $i$ to S2 in iteration $i + 3$. Under [DOACROSS](/doacross-parallelization/) execution, iteration $i + 1$ starts $\delta$ units after iteration $i$. Find the least $\delta$, the number of processors beyond which there is no gain, and the total time for 100 iterations with 3 processors, with 2 processors and sequentially.

9. • Run the [Allen-Kennedy algorithm](/allen-kennedy-algorithm/) on the loop of exercise 1. Write the result as a sequential loop plus [vector statements](/vectorization/) in array notation, and say why the order of the pieces matters.

10. • A nest with $1 \le i, j \le 10$ writes `A[3i+4j]` and reads `A[3i+4j+2]`. Show that the GCD test on the whole equation cannot prove independence, but the GCD test under the direction "=" for $i$ can. What does this say about the $j$ loop?

11. • A nest with $1 \le i, j \le 4$ writes `A[i+10j]` and reads `A[i+10j+5]`. Show that the GCD test and the [Banerjee test](/banerjee-test/) with direction $(*, *)$ both fail to prove independence, and that the Banerjee test proves it once the direction of $j$ is split into $<$, $=$ and $>$.

12. • Loop 1 is `for i = 1 to 7: A[i] = X[i] + 1`, and loop 2 is `for i = 1 to 7: B[i] = A[8-i] * 2`. Explain why [fusing](/loop-fusion/) them as written changes the result, and which elements of `B` go wrong. Then find a transformation of loop 2 after which fusion is legal.

13. • A nest over $1 \le i \le 12$, $1 \le j \le 8$ has the body `A[i][j] = A[i-2][j+1] + A[i][j-1]`. Unroll-and-jam [unrolls](/loop-unrolling/) the $i$ loop $k$ times and fuses the copies inside the $j$ loop. Find the largest $k$ that keeps the result.

14. • An in-place Gauss-Seidel sweep runs `for t = 0 to 5: for i = 1 to 7: A[i] = A[i-1] + 3*A[i] + 7*A[i+1]`. Find the distance vectors of its direct dependences. Show that rectangular [tiling](/loop-tiling/) of $(t, i)$ is illegal, and that tiling becomes legal after [skewing](/loop-skewing/) $i' = i + t$.

15. • A nest over $1 \le i, j \le N$ has the distance vectors $(1, 1)$ and $(0, 1)$. Find integers $a, b$ such that $\theta(i, j) = ai + bj$ satisfies $\theta(d) \ge 1$ for both distances and takes the fewest distinct values. Which loop order and which parallel loop does the schedule give?

16. • The program `for i = 0 to N: S1: A[i] = B[i]` is followed by `for i = 0 to N: for j = 0 to i: S2: A[j] = A[j] + C[i][j]`. By [array dataflow analysis](/feautrier-array-dataflow/), give the instance that writes the value of `A[j]` read by S2 at $(i, j)$, as a case split on $i$ and $j$.

17. • The nest `for i, j = 1 to 6: A[i][i+j] = A[i-1][i+j+1] + 1` has coupled subscripts. Solve the first subscript, substitute into the second as the delta test of the [subscript-wise tests](/practical-dependence-tests/) does, and give the distance vector. Is the inner loop parallel? Is [interchange](/loop-interchange/) legal?

18. • Loop 1 is `for i = 1 to 9: S1: B[i] = A[i]` and loop 2 is `for i = 1 to 9: S2: C[i] = B[i-2] + 3*B[i+1]`. Fuse them so that S1 runs at time $i$ and S2 at time $i + c$. Find the least shift $c$ that is legal, the order of S1 and S2 in the body that it needs, and the largest dependence distance $w$ in the fused loop, the bound that the [Pluto algorithm](/pluto-algorithm/) minimizes.

19. ★ The depth-2 nest over $1 \le i, j \le N$ has the body `S1: A[i][j] = B[i][j-1] + 1` and `S2: B[i][j] = A[i-1][j] * 2`. Find its dependences, run the Allen-Kennedy algorithm level by level, and write the output with vector statements in $j$.

20. ★ A nest over $1 \le i, j \le 4$ has the distance vectors $(1, -1)$, $(1, -3)$ and $(0, 1)$. Find the least skew factor $f$ such that after $j' = j + fi$ and interchange the inner loop is parallel. Count the wavefronts, compare with the longest chain of dependent iterations, and say how much parallelism the nest has.

21. ★ Matrix multiplication `for i, j, k: C[i][j] = C[i][j] + A[i][k] * B[k][j]` is in row-major order, with $l = 8$ elements per cache line and $s = 100$ iterations per loop. In the [Wolf-Lam model](/wolf-lam-locality-algorithm/), a reference with access matrix $H$ has temporal reuse space $\ker H$ and spatial reuse space $\ker H_S$, with $H_S$ equal to $H$ with its last row set to zero. For a set $L$ of localized loops, its cost is $1/(l^e s^t)$, with $t = \dim(\ker H \cap L)$ and $e = 1$ when $\dim(\ker H_S \cap L) > t$, else $e = 0$. Give the reuse spaces of the three references, the total cost for $L = \{k\}$, $\{j\}$, $\{i\}$, $\{j, k\}$ and $\{i, j, k\}$, and which sets are legal.

22. ★ The loop `for i = 1 to 24` has the body `S1: A[i] = B[i-2] + 1` and `S2: B[i] = A[i-3] * 2`. It is [strip-mined](/strip-mining/) into strips of $VL$ iterations, and each statement runs as one vector operation per strip. Find the largest $VL$ that keeps the result. Then swap the two statements in the body, check that the swap is legal, and find the largest $VL$ after it.

23. ★ The nest `for i, j = 1 to n: A[i][j] = A[j][i]` is meant to transpose `A` in place. Count its flow and anti dependences, give their direction vectors, and say whether the inner loop is parallel and whether interchange is legal. Describe what the nest computes as written and after interchange.
