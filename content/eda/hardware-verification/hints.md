1. Tabulate both functions. They agree on 00, 01 and 10, where both give 0 or both give 1. On 11 the XOR gives 0 and the OR gives 1. The miter is 1 only at $a = b = 1$, and a SAT solver returns that input as the counterexample.

2. Three evaluations: 11, 01 and 10. The pair 11 and 01 changes only $a$ and changes the decision, and the pair 11 and 10 does the same for $b$. Two evaluations cannot do it, because each condition needs its own pair. This is the $k + 1$ bound for $k = 2$.

3. Declared denominator: states $3/4$, arcs $3/6$. Reachable denominator: states $3/3$, arcs $3/4$. The two arcs out of D can never be taken, so the declared figure can never reach 100 percent.

4. $4(1 + \tfrac12 + \tfrac13 + \tfrac14) = 25/3 \approx 8.33$ runs. Waiting for the $i$-th new bin is geometric with success probability $(4 - i + 1)/4$.

5. The MTBF has the factor $e^{t_r/\tau}$, so 1 ns more multiplies it by $e^{1000/20} = e^{50} \approx 5.2 \times 10^{21}$. A factor of 10 needs $\tau \ln 10 \approx 46$ ps.

8. The attempt at cycle 0 looks for `gnt` in cycles 1 to 3, finds none and fails at cycle 3. The attempt at cycle 2 looks in cycles 3 to 5 and passes at cycle 4. The attempts at the other cycles pass vacuously, since `req` is 0 there.

10. The product starts at $(0, 1)$, and every input flips both bits, so the reachable set is $\{(0, 1), (1, 0)\}$. On both states $p = \neg q$, so the outputs agree, and the machines are equivalent. The states $(0, 0)$ and $(1, 1)$, where the outputs differ, are unreachable.

12. There are $4 + 3 + 2 + 1 = 10$ solutions, so the uniform law gives $1/10$, $1/10$ and $4/10 = 2/5$. Under the ordering, $P(a = 3) = 1/4$, $P(a = 0, b = 0) = 1/16$ and $P(b = 3) = \tfrac14(\tfrac14 + \tfrac13 + \tfrac12 + 1) = 25/48$. The ordering spreads $a$ evenly and pushes $b$ up.

16. Constrain by $\neg s_1$ sets $s_1 = 0$ in the functions, which gives $(s_2 \oplus x, 0)$, with range $\{00, 10\}$. From 00 the layers are $\{00\}$, then $\{00, 10\}$, then $\{00, 10, 11\}$, then all four states, since 11 goes to 10 and 01.

18. The remainder is $2a + 2b + 2c - 4ab - 4ac - 4bc + 6abc$. Its least-degree monomial $2a$ gives $a = 1$, $b = c = 0$, where the remainder is 2. Simulation gives carry 1 and sum 1, so $2 \cdot 1 + 1 = 3$ against $a + b + c = 1$.

21. Use inclusion-exclusion over the bins not yet seen: $E = \sum_{S \ne \emptyset} (-1)^{\lvert S \rvert + 1}/p(S)$. The singles give $2 + 4 + 4 = 10$, the pairs $\tfrac43 + \tfrac43 + 2 = \tfrac{14}{3}$ and the triple 1. So $E = 10 - \tfrac{14}{3} + 1 = 19/3 \approx 6.33$, against $3(1 + \tfrac12 + \tfrac13) = 11/2$ for equal bins. The rare bins dominate the wait.

22. The cross is a coupon collector with 12 equal bins: $12 H_{12} = 86021/2310 \approx 37.24$ runs. For the coverpoints, sum over pairs $(s, u) \ne (0, 0)$ of $s$ bins of $A$ and $u$ bins of $B$ the term $(-1)^{s + u + 1} \binom{4}{s}\binom{3}{u}/\bigl(1 - (1 - s/4)(1 - u/3)\bigr)$. The result is $589/66 \approx 8.92$. A simulation with seed 32422 and 200000 runs gave a mean of 8.925. The cross takes more than four times as long.

23. At 111, flipping $x$ flips both $p$ and $q$, and $y$ stays 0. So the observable sites are $b, c, p, q, y$, and the tags agree: at the XOR the tag of $x$ from $p$ is dropped, because $x$ is also in the fanin of $q$. At 110, $q$ is 0 and does not depend on $x$ any more, so flipping $x$ changes $y$, and $x$ is observable. The tag rule still drops $x$, because it looks at the fanin cone of $q$, not at its values. This is the price of soundness: the rule never tags a site that a reconvergent path could cancel.

24. The reachable states are $(0, 100)$, $(1, 010)$ and $(2, 001)$, 3 of 32. Unreachable states where the outputs agree can lead to disagreement, for example A at 3 and B at 010, both with output 0, go to A at 0 and B at 001. The least $k$ is 3, with or without the simple-path constraint. With the enable, a path can stay on one state for any number of steps, so every bad path can be stretched, and plain k-induction fails for every $k$. The simple-path constraint forbids the repeats and gives $k = 3$ again.

25. $x^2 + x = x(x + 1)$ is a product of two consecutive integers, so it is even, and $2^{w-1}$ times an even number is a multiple of $2^w$. The diagram over the rationals stores the nonzero coefficients $2^{w-1}$, so two datapaths that agree modulo $2^w$ can have different diagrams. Comparing diagrams decides equality over the integers, and for words it needs a normal form modulo $2^w$.
