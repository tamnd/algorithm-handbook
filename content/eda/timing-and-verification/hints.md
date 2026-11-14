1. The capacitance below $R_1$ is 4, below $R_2$ is 3, below $R_3$ is 2 and below $R_4$ is 1. The Elmore delays are $4$, $4 + 3 = 7$, $7 + 2 = 9$ and $9 + 1 = 10$.

2. The capacitance below $R_1$ is $1 + 1 + 3 = 5$, so node 1 has delay 5, node 2 has $5 + 2 \cdot 1 = 7$ and node 3 has $5 + 1 \cdot 3 = 8$. With the extra 2 at node 2, the capacitance below $R_1$ becomes 7, and node 3 has $7 + 3 = 10$. A load on one branch slows the other branches through their shared resistance.

3. Arrival times: $G_1$ gets $\max(0 + 2, 1 + 3) = 4$ and $y$ gets $\max(4 + 4, 0 + 1) = 8$. Required times: $y$ 8, $G_1$ 4, $c$ 7, $a$ 2, $b$ 1. Slacks: $a$ 2, $b$ 0, $c$ 7, $G_1$ 0, $y$ 0. The critical path is $b \to G_1 \to y$.

4. Setup slack is $(1.5 + 8 - 0.3) - (0 + 8.6) = 0.6$, so the least period is $8 - 0.6 = 7.4$. Hold slack is $(0 + 0.4) - (1.5 + 0.2) = -1.3$, a violation. The hold check does not contain $T$, so no clock period fixes it; the fix is more delay on the short path or less skew.

5. It has $4^3 = 64$ ends. The wire length is $\frac32 \cdot 16 \cdot (2^3 - 1) = 168$ and each path has length $16 (1 - 2^{-3}) = 14$.

6. With $a = 1$ the good circuit gives $z = b$ and the circuit with $a$/0 gives $z = c$, so the tests are the vectors with $a = 1$ and $b \ne c$: 101 and 110. With $a = 0$ the good circuit gives $c$ and the faulty one $b$, so $a$/1 is detected by 001 and 010.

7. $R_1$ and $R_2$ are at distance 3, $R_1$ and $R_3$ at $\sqrt{2^2 + 2^2} = \sqrt 8 \approx 2.83$ (corner to corner), and $R_2$ and $R_3$ at 2. The violations are $R_1R_3$ and $R_2R_3$; the pair at distance exactly 3 is legal. A checker that measures only between edges with overlapping projections finds $R_2R_3$ and misses the corner pair $R_1R_3$.

8. One square gives 4 space tiles: a strip below, a strip above, and one tile on each side. Two squares in one row give 5: the strips below and above, and the three gaps $[0, 1)$, $[2, 3)$ and $[4, 5)$ of the middle row. That is below $3n + 1 = 7$; the bound is reached only by staggered tiles.

9. The standard error after $N$ walks is $4C / \sqrt N$, so $4 / \sqrt N = 0.01$ gives $N = 160\,000$ walks, about $800\,000$ jumps.

14. Zero skew needs $T \ge \max(6, 10) = 10$. With skew, the setup constraints are $c_1 + 6 \le c_2 + T$ and $c_2 + 10 \le c_1 + T$; adding them gives $2T \ge 16$. So $T^* = 8$ with $c_1 - c_2 = 2$. The hold constraints $c_2 - c_1 \le 2$ and $c_1 - c_2 \le 3$ both hold.

19. Controllabilities: $\bar a$ 2/2, $p$ 2/3, $q$ 2/4, $z$ 5/4. Observabilities: $z$ 0, $p$ and $q$ 3, $a_1$, $b$ and $\bar a$ 5, $c$ and $a_2$ 6, and the stem $a$ takes the smaller branch value, 5.

22. For stuck-at-1 at the output, a test is a vector with output 0, so the fault is detectable exactly when the sum of products is not a tautology. A CNF formula is satisfiable exactly when its negation, a DNF by De Morgan, is not a tautology, so this is NP-complete. For stuck-at-0 a test is a vector with output 1, which exists exactly when some product term has no variable together with its complement. So a statement that detection is polynomial for two-level circuits holds for monotone ones or for some faults only.

23. Static timing analysis adds $5 + 1 + 5 + 1 = 12$ along $a \to P \to x \to Q \to y$. That path goes through $P$ only when $s = 1$ and through $Q$ only when $s = 0$, so no vector sensitizes it. With $s = 1$ the delay is $5 + 1 + 1 = 7$, with $s = 0$ it is $1 + 5 + 1 = 7$, and the paths from $s$ are no longer. The true delay is 7.

24. If two pairs had $c < c'$ and $q \ge q'$, the second would be dominated. For the merge, walk both lists from the smallest load; each step pairs the current entries and advances the list whose current required time is the min, since only a larger required time there can raise the min. Each step advances one pointer, so there are at most $a + b - 1$ steps. The lists $(1, 1), (2, 3)$ and $(1, 2), (3, 4)$ give $(2, 1), (3, 2), (5, 3)$.

26. The hold constraint on the path back is now $c_1 - c_2 \le 1$, and setup on that path needs $c_1 - c_2 \ge 10 - T$. Together they give $T \ge 9$, reached with $c_1 - c_2 = 1$; setup from register 1 needs $c_1 - c_2 \le T - 6 = 3$, which holds, and the hold constraint $c_2 - c_1 \le 1/2$ holds too. The loop of the setup edge and the hold edge of the same path sums to $T - 9 \ge 0$.
