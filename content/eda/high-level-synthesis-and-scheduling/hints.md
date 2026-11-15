1. The paths are A D E G, A D F G, B D E G, B D F G, C D E G and C D F G: 6. The first statement has three outcomes and the second two, and the counts multiply. With $k$ two-way branches in sequence there are $2^k$ paths, which is why a scheduler that enumerates paths can take exponential time.

2. The balance equations $3q_A = 2q_B$ and $q_B = 3q_C$ give $q = (2, 3, 1)$. AABBBC holds at most 6 tokens on A→B and 3 on B→C, 9 in total. ABABBC holds at most 4 on A→B and 3 on B→C, 7 in total, so it needs the smaller buffers.

4. The live counts in steps 1 to 6 are 2, 2, 3, 3, 3, 2, so at least 3 registers are needed. Left-edge gives the registers $\{a, e\}$, $\{b, c, f, g\}$ and $\{d\}$. Three registers equal the largest live count, which is optimal for straight-line code.

6. `a * b` lies in $[0, 3969]$, and $3969 < 4096 = 2^{12}$, so it needs 12 bits. `y` lies in $[-255, 3969]$, and two's complement with 13 bits holds $[-4096, 4095]$, so `y` needs 13 bits.

9. $\{s_0, s_1\}$ spans the face $0{-}$, which holds only $s_0$ and $s_1$: met. $\{s_0, s_2\}$ spans the whole cube ${-}{-}$, which also holds $s_1$ and $s_3$: not met. $\{s_1, s_2, s_3\}$ also spans ${-}{-}$, which holds $s_0$: not met.

11. The bound is $\max(4, \lceil 8/2 \rceil) = 4$. Hu's algorithm runs e and a, then b and c, then d and p, then q, then r: 5 steps. Every other operation precedes r, so r runs alone in the last step, and the other seven need at least $\lceil 7/2 \rceil = 4$ steps before it.

12. The rows are $s_1 - s_0 \ge 2$, $s_2 - s_1 \ge 0$, $s_3 - s_1 \ge 0$, $s_4 - s_2 \ge 0$, $s_4 - s_3 \ge 0$ and $s_4 - s_1 \ge \lceil 9/6 \rceil - 1 = 1$. The least solution is $s = (0, 2, 2, 2, 3)$, 4 steps. With one adder the rows $s_2 - s_1 \ge 1$, $s_3 - s_2 \ge 1$ and $s_4 - s_3 \ge 1$ give $(0, 2, 3, 4, 5)$, 6 steps, which is optimal, since four additions on one adder need four steps from step 2 on.

14. In step 2 the only free register is the one that held a, so b goes there. In step 3 it is still busy, so c and d get fresh registers. The cost is $5 + 3 + 3 = 11$. The binding $\{a, d\}$, $\{b\}$, $\{c\}$ costs $3 + 2 + 3 = 8$: a and d share their source and both their ports.

18. The gains $s - h$ are 6, 4, 4, 3 and 4, from 30 for all software. For budget 5 the optimum is $\{P, S\}$ with time 21, while greedy by gain per area takes S, then R, and stops at time 23. For budget 9 the optimum is $\{P, Q, R\}$ with time 16, while greedy takes S, R and P, time 17.

23. No two adjacent vertices have a common neighbour, so the key falls to del, and ab, ac, bd and ef tie at 3. The smallest pair is ab, which leaves $\{a, b\}$ with no neighbour. Then ce wins, and the result is $\{a, b\}$, $\{c, e\}$, $\{d\}$, $\{f\}$: 4 groups. The partition $\{a, c\}$, $\{b, d\}$, $\{e, f\}$ has 3.

24. ASAP puts a, b, c in step 1, d in step 2 and e, f, g in step 3; ALAP puts them in steps 2, 3 and 4. Every window gives at most 2. With 2 units, a, b and c take two steps, so d runs in step 3 or later and e, f, g need steps 4 and 5. The bound looks at each window alone and misses that d joins them.

25. A partition preserved by $s \mapsto s + 1$ is the partition into residues modulo some $m$ dividing 12, so there are 6: $m = 1, 2, 3, 4, 6, 12$. Two such partitions meet in the zero partition when $\mathrm{lcm}(m_1, m_2) = 12$, which leaves the nontrivial pairs $(3, 4)$, with $2 + 2 = 4$ flip-flops, and $(4, 6)$, with $2 + 3 = 5$.

26. $T_\infty = 4/2 = 2$, and a node alone is a path with no delay, so every retiming has period at least $t(A) = 3$. Unfolding gives the cycles $A_0 \to B_1 \to A_0$ and $A_1 \to B_0 \to A_1$, each with time 4 and one delay. The period is 4 for two samples.

27. The total number of tokens stays $d$, and A→B always holds a multiple of $g = \gcd(p, c)$. A deadlock needs at most $c - g$ tokens on A→B and at most $p - 1$ on B→A, so $d \le p + c - g - 1$. For the converse, fire B whenever it can: after $i$ firings of A, A→B holds $pi \bmod c$, and this value reaches $c - g$ for some $i < c/g$, where A then lacks tokens.
