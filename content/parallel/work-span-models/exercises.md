1. ◦ Three processors of a [CRCW PRAM](/crcw-pram/), numbered 1, 2 and 3, write 5, 3 and 7 into the same cell in one step. What does the cell hold afterwards under the common rule, the arbitrary rule, the priority rule (lowest number wins), and the combining rule with addition? Under which rule is the step not allowed at all?

2. ◦ The tree sum of $n = 1024$ numbers on an [EREW PRAM](/erew-pram/) does 512 additions in its first step, 256 in its second, and so on. How many steps and how many additions does it take with unlimited processors? Use the work-time principle of the [PRAM model](/pram-model/) to count the steps on $p = 128$ processors exactly, and compare your count with the bound $\lfloor W/p \rfloor + T$.

3. ◦ A recursive sum splits its input into halves of sizes $\lceil n/2 \rceil$ and $\lfloor n/2 \rfloor$, spawns one half, calls the other, syncs and adds. As in the [work-span model](/work-span-model/), count one strand for each leaf and two strands for each internal call, one before the fork and one after the join. Find the work and the span for $n = 6$ and for $n = 8$.

4. ◦ A [fork-join](/fork-join-model/) procedure runs a serial strand of 4 unit steps, then spawns a task $X$ with work 6 and span 6, then runs a task $Y$ with work 10 and span 3, then syncs and runs 2 more serial steps. Find its work, its span and its [parallelism](/parallelism/). Which task would you try to parallelize further, and why?

5. ◦ A computation has $T_1 = 1000$ and $T_\infty = 40$. For $p = 10, 25, 50$ and 100, give the lower bound $\max(T_1/p, T_\infty)$ from the [work law](/work-law/) and the [span law](/span-law/), and the upper bound $(T_1 - T_\infty)/p + T_\infty$ of a [greedy scheduler](/greedy-scheduling/). Beyond what $p$ is it pointless to add processors?

6. ◦ Under [Amdahl's law](/amdahls-law/), what speedup can a program with parallel fraction $f = 0.8$ reach on 4 processors, and what is its limit as $p \to \infty$? A program is measured at speedup 3 on 4 processors. What serial fraction does the Karp–Flatt metric $e = (1/S_p - 1/p)/(1 - 1/p)$ give?

7. ◦ A run on $p = 32$ processors spends a fraction $s = 0.1$ of its time in serial code. What scaled speedup does [Gustafson's law](/gustafsons-law/) give? What parallel fraction $f$ would a one-processor run of the same scaled problem show, and what does Amdahl's law say about that $f$ on 32 processors?

8. ◦ Starting from $x = 1$, a procedure spawns a child that runs $x = x + 1$, runs $x = 3x$ itself, and then syncs. Each update is a read of $x$ followed by a write. List every value $x$ can hold after the sync. Which values remain possible if each update holds a [mutex](/mutex/)? Does the program still have a [determinacy race](/determinacy-race/)?

9. ◦ With one strand for each split and one for each join, [parallel Fibonacci](/parallel-fibonacci/) has $T_1 = 3F_{n+1} - 2$ and $T_\infty = 2n - 1$. Check that $T_1 = 22$ and $T_\infty = 9$ for $n = 5$. A greedy schedule runs it in 13 steps on 2 processors. Give the [speedup](/speedup/) and the [parallel efficiency](/parallel-efficiency/), and place 13 between the lower and upper bounds of exercise 5.

10. • A [computation DAG](/computation-dag/) has unit strands $1, \dots, 8$ and edges $1 \to 2$, $1 \to 3$, $1 \to 4$, $2 \to 5$, $3 \to 5$, $4 \to 6$, $6 \to 7$, $5 \to 8$ and $7 \to 8$. Find its work, its span and a [critical path](/critical-path/). Run a greedy scheduler on two processors that takes ready strands in the order they became ready, breaking ties by the smaller label. Then run one that always takes the ready strands with the longest path below them. Compare both with the greedy bound and with the best two-processor schedule.

11. • Multiply an $n \times n$ matrix by a vector with a parallel loop over the rows, each row computed by a serial loop. Find the work and the span. Why may the inner loop not simply be made a parallel loop that adds each product into $y_i$? Replace it by a [parallel reduction](/parallel-reduce/) and give the new span and parallelism.

12. • In an $n \times n$ grid, cell $(i, j)$ can be computed once cells $(i-1, j)$ and $(i, j-1)$ are done. Show that this DAG has span $2n - 1$. A fork-join program computes the top-left quadrant, then spawns the top-right and bottom-left quadrants and syncs, then computes the bottom-right quadrant, all recursively. Show that its span is $\Theta(n^{\lg 3})$, compare the two for $n = 1024$, and explain where the fork-join program loses.

13. • [Merge sort](/merge-sort/) with its two recursive calls in parallel and a serial merge has work $\Theta(n \log n)$. Show that its span is $\Theta(n)$ and its parallelism $\Theta(\log n)$. Estimate the parallelism for $n = 2^{20}$ to within a factor of 2, and say how many processors it can use with a [slackness](/parallel-slackness/) of 10.

14. • For $n = 2^{16}$ the [Hillis–Steele scan](/hillis-steele-scan/) has work $n \lg n - n + 1$ and span $\lg n$, the [Blelloch scan](/blelloch-scan/) has work $2(n - 1)$ and span $2 \lg n$, and the serial scan takes $n - 1$ steps. For each parallel scan, find the fewest processors on which some schedule could beat the serial scan, and the fewest on which the greedy bound guarantees it. What does this say about [work efficiency](/work-efficiency/)?

15. • Use the parallel Fibonacci costs of exercise 9. Find the smallest $n$ for which the [parallel slackness](/parallel-slackness/) on $p = 64$ processors is at least 10, and the speedup and efficiency that the greedy bound then guarantees.

16. • Show that under Amdahl's law the speedup reaches half its limit $1/(1 - f)$ exactly when $p = f/(1 - f)$. How many processors does that take for $f = 0.99$, and what is the efficiency there? Give a DAG for which Amdahl's formula is exact on every $p$ that divides its parallel part.

17. • In a [weak-scaling](/weak-scaling/) run of the tree sum, each of $p$ processors holds $m$ numbers, adds them serially, and the $p$ partial sums are then added by a tree. The run takes $m - 1 + \lg p$ steps. How large must $m$ be for the weak-scaling efficiency to stay at least 0.99 on $p = 2^{20}$ processors?

18. • The tree sum of $n$ numbers on $p$ processors takes $n/p - 1 + \lg p$ steps, as in [strong scaling](/strong-scaling/); treat $n/p$ as a whole number. Find the smallest $n$ that keeps the efficiency at least 0.9 on $p = 1024$ processors. Show that, to hold any fixed efficiency below 1, $n$ must grow as $\Theta(p \log p)$.

19. • Give a fork-join program with a data race that prints the same output on every schedule. Does it have a determinacy race? Would the SP-bags algorithm report it? Then explain why removing every data race with locks does not make a program deterministic.

20. • Merge sorted arrays $A$ and $B$ of $n$ items each on a [CREW PRAM](/crew-pram/) by ranking. Each $a_i$ finds $r_i$, the number of $b_j < a_i$, and each $b_j$ finds $s_j$, the number of $a_i \le b_j$, by binary search. Then $a_i$ goes to position $i + r_i$ and $b_j$ to position $j + s_j$. Prove that the positions are distinct even when $A$ and $B$ share values. Why is the algorithm CREW and not EREW? Give its time and its work, and say why it is not work-efficient.

21. • The CRCW maximum of the [CRCW PRAM](/crcw-pram/) entry finds the maximum of $k$ numbers in $O(1)$ steps with $k^2$ processors. Use it to find the maximum of $n$ numbers in $O(\log \log n)$ steps with $n$ processors: split the input into $\sqrt{n}$ groups of $\sqrt{n}$ items each. Write the recurrence for the time and solve it. What is the work, and is the algorithm work-efficient?

22. ★ Show that the factor $2 - 1/p$ of [greedy scheduling](/greedy-scheduling/) is tight for unit strands. For each $p$ and each $k$ divisible by $p$, build a DAG with optimal $p$-processor time $k$ on which some greedy schedule takes $(2 - 1/p)k$ steps.

23. ★ Show that one step of a $p$-processor CRCW PRAM under the priority rule can be simulated in $O(\log p)$ steps on a $p$-processor EREW PRAM, given an EREW sort of $p$ items in $O(\log p)$ steps. Handle the concurrent writes first, then the concurrent reads. How many steps does the simulation take if a [bitonic sort](/bitonic-sort/) is used instead?

24. ★ The SP-bags algorithm of the [determinacy race](/determinacy-race/) entry runs the program serially and keeps an S-bag and a P-bag for each procedure. When $F$ spawns or calls a child $F'$, $S_{F'} = \{F'\}$ and $P_{F'} = \emptyset$. When $F'$ returns to $F$, its S-bag is added to $P_F$ if $F'$ was spawned and to $S_F$ if it was called. At a sync, $P_F$ is emptied into $S_F$. Prove that while a strand of procedure $G$ runs, an earlier procedure instance $E$ is in some P-bag exactly when the strands of $E$ are logically parallel with the current strand, and in some S-bag exactly when they precede it.

25. ★ A parallel loop has $n$ iterations. Each iteration, independently, is a serial chain of $n$ steps with probability $1/n$ and a single step otherwise. Show that the largest expected span of any one iteration is less than 2, but that the expected span of the loop is at least $(1 - 1/e)n$. What is the expected work? Explain why [work-span analysis](/work-span-analysis/) may add expected works but may not take the maximum of expected spans.

26. ★ Generalize the fork-join program of exercise 12. Split the grid into $b \times b$ blocks and process the $2b - 1$ antidiagonals of blocks one after another, the blocks of each antidiagonal in parallel and each block recursively. Show that the span is $\Theta(n^{\log_b (2b-1)})$ for fixed $b$. Compute the exponent for $b = 2, 3, 4$ and 8, and find what happens when $b$ grows with $n$, up to $b = n$.
