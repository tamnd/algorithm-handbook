1. The densities per unit length are $(1/2, 1, 3/2, 1)$ for agent 1. Agent 1 reaches $3/8$ at $1/2$ and needs $1/8$ more at density $3/2$, so it cuts at $7/12$. Agent 2 values $[0, 7/12]$ at $3/8 + 1/8 + 1/24 = 13/24$ and takes it.

3. In round 1 the marks are $7/24$, $7/12$ and $1/6$, so agent 3 takes $[0, 1/6]$. In round 2, from $1/6$, the marks are $3/8$ and $7/12$, so agent 1 takes $[1/6, 3/8]$ and agent 2 gets $[3/8, 1]$. The values to the owners are $1/3$, $7/8$ and $1/3$. Agent 1 values the piece of agent 2 at $1/2$, and so does agent 3, so both envy agent 2; the run made 5 cut queries.

5. The picks are $b, a, c, d, e, f$, so the bundles are $\{b, d\}$, $\{a, e\}$ and $\{c, f\}$. The rows of values are $(14, 7, 6)$, $(10, 13, 3)$ and $(5, 11, 7)$. Agent 3 envies agent 2, so the result is not envy-free, but removing $a$ leaves $4 \le 7$, so it is EF1 (and in fact EFX).

7. Assigning room 1 to $a$ has weight 850, against 750 for the other assignment, so only it can be envy-free. With $p_2 = 800 - p_1$, tenant $a$ needs $p_1 - p_2 \le 200$ and tenant $b$ needs $p_1 - p_2 \ge 100$, so $450 \le p_1 \le 500$. Equal utility, $500 - p_1 = p_1 - 450$, gives $p_1 = 475$ and utility 25 each.

8. With one cut each thief needs 4 beads, so the cut follows bead 4, and R R B R has three red beads. Cut after beads 1 and 5: the middle part R B R B goes to one thief, and R with B R B to the other. Cutting after beads 3 and 7 also works.

12. Agent 1 cuts at $1/3$ and $2/3$. Agent 2 values the pieces at $5/12$, $1/4$ and $1/3$, so it trims $[0, 1/3]$ to $[0, 1/6]$, and the trimmings are $[1/6, 1/3]$. Agent 3 takes $[1/3, 2/3]$, so agent 2 takes the trimmed piece, agent 1 takes $[2/3, 1]$, and agent 3 cuts the trimmings at $2/9$ and $5/18$. The final pieces are $[2/3, 1] \cup [2/9, 5/18]$, $[0, 2/9]$ and $[5/18, 2/3]$, and the rows of the table are $(7/18, 2/9, 7/18)$, $(13/36, 13/36, 5/18)$ and $(5/18, 1/9, 11/18)$.

13. Goods $a$, $b$, $c$ go to agents 1, 2, 3, and $d$ to agent 3, nobody envying it. Before $e$, agents 1 and 2 envy each other and agent 3, while agent 3 envies no one, so every agent is envied and the only cycle is 1, 2; they swap $\{a\}$ and $\{b\}$. Then $e$ goes to agent 1, and the result is $\{b, e\}$, $\{a\}$, $\{c, d\}$ with values 14, 9 and 14 to their owners. Agent 3 values $\{b, e\}$ at 15, but at 8 without $b$.

16. After the first step A has 60 points and B has 70, so B gives up goods in the order of the ratio $p_B/p_A$, which is smallest for the second good, $30/25$. Moving all of it would leave B with fewer points, so A gets the share $(70 - 60)/(25 + 30) = 2/11$ of it. Both end with $710/11 \approx 64.5$ points, and A gives B's share $390/11$.

18. The weights of the six assignments are at most 1450, reached only by tenant $i$ taking room $i$. At equal prices tenant 2 gets 50 from room 2 and 100 from room 1. The utilities always sum to $1450 - 1200 = 250$, so the smallest is at most $250/3$; the prices $(1550/3, 1100/3, 950/3)$ give each tenant exactly $250/3$, and checking the six other comparisons shows that they are envy-free.

21. Draw the recursion tree. Each agent ends in one leaf, and a call on $k \ge 2$ agents asks each of its agents two queries, so $T(n)$ is twice the sum of the depths of the leaves. The balanced split puts every leaf at depth $c = \lceil \lg n \rceil$ or $c - 1$, and counting leaves gives $2^c - n$ of them at depth $c - 1$.

22. Agent $i$ envies agent $j$ exactly when $v(A_j) > v(A_i)$, so an agent of smallest value has no incoming edge and line L4 never runs. For EFX, look at the last good $g$ given to $A_j$: at that time $v(A_i) \ge v(A_j \setminus \{g\})$, and $g$ is the least valuable good of $A_j$, while $A_i$ only grows afterwards.

24. Write the envy-freeness inequality of each tenant for $\sigma$ against $\tau$ and sum them. Both price sums equal $R$ and both assignments have the same weight, so the sum is $0 \ge 0$ with equality, and every inequality is tight.

25. Let $r(i)$ be the number of red beads among beads $i + 1, \dots, i + a + b$, for $0 \le i \le a + b$. The windows at $i = 0$ and $i = a + b$ are complements, so $r(0) + r(a + b) = 2a$, and $r$ changes by at most 1 per step. Some $i$ has $r(i) = a$, and that window also has $b$ blue beads; computing $r$ by a sliding window takes $O(a + b)$ time.
