1. The core asks for $x_1 + x_2 \ge 6$, $x_1 + x_3 \ge 4$, $x_2 + x_3 \ge 2$ and $x_1 + x_2 + x_3 = 9$. The point $(3, 2, 4)$ fails, because $\{1, 2\}$ gets 5. The point $(5, 2, 2)$ passes all three. The Shapley value is $(4, 3, 2)$, and it is in the core.

3. The minimal winning coalitions are $\{1, 2\}$ and $\{1, 3, 4\}$, so player 1 has a veto. Shapley-Shubik: $(7/12, 1/4, 1/12, 1/12)$. The swings are $(5, 3, 1, 1)$ out of 8 coalitions of the others, so the raw Banzhaf index is $(5/8, 3/8, 1/8, 1/8)$ and the normalized one is $(1/2, 3/10, 1/10, 1/10)$.

5. Proportional: $(24, 36, 60)$. Constrained equal awards: $(40, 40, 40)$. Constrained equal losses: the loss of 180 is split as 60 each, which gives $(0, 30, 90)$. Talmud: $E \le C/2 = 150$, so use equal awards on the half claims $(30, 45, 75)$, which gives $(30, 45, 45)$.

7. The share is $x^* = (1 - \delta_2)/(1 - \delta_1 \delta_2) = (1/2)/(3/5) = 5/6$, and the first offer is accepted. With $\delta_2 = 4/5$ the share is $(1/5)/(9/25) = 5/9$.

8. Adding the three pair constraints gives $2(x_1 + x_2 + x_3) \ge 9/4$, but the sum is 1. In the least core every pair gets at least $3/4 - \varepsilon$, so $2 \ge 9/4 - 3\varepsilon$ and $\varepsilon \ge 1/12$. The value $1/12$ is reached only at $(1/3, 1/3, 1/3)$.

10. With a union bound over the 20 players the Hoeffding bound asks for $m \ge \ln(2n/\delta)/(2\varepsilon^2) = \ln 800 / 0.0008$, so $m = 8356$ orders. Each order costs $n + 1 = 21$ evaluations of $v$ if you walk along it, about 175,000 in all.

11. The coalition costs are $C(1) = 5$, $C(2) = 6$, $C(3) = 7$, $C(12) = 8$, $C(13) = 11$, $C(23) = 8$ and $C(N) = 10$. Prim's algorithm from 0 takes edges 0-1, 1-2, 2-3, so Bird's rule gives $(5, 3, 2)$. The Shapley value is $(10/3, 7/3, 13/3)$. Both allocations are in the core.

14. The estate 200 is above $C/2 = 150$, so each creditor gets half its claim and the losses are shared equally with nobody losing more than half its claim. Talmud: $(30, 55, 115)$. Random arrival: $(115/3, 160/3, 325/3)$. For $E = 100$ the Talmud rule gives $(30, 35, 35)$, which is $c - (30, 55, 115)$, as self-duality says.

17. Look at the pairs of excesses $e(\{3\}) = -x_3$ and $e(\{1, 2\}) = x_3 - 2$: their maximum is at least $-1$, with equality only at $x_3 = 1$. With $x_3 = 1$ the excesses of $\{1, 3\}$ and $\{2, 3\}$ are $x_2 - 3$ and $1 - x_2$, so $x_2 = 2$. The nucleolus is $(3, 2, 1)$, with sorted excesses $(-1, -1, -1, -1, -2, -3)$. The Shapley value is $(5/2, 2, 3/2)$.

21. Player $x$ swings exactly when the others reach weight 12, so the swings are $\{3, 9\}$ and $\{5, 7\}$. The raw Banzhaf index is $2/16 = 1/8$. Each swing has two members among five players and adds $2!\,2!/5! = 1/30$, so the Shapley-Shubik index is $1/15$.

22. Let $\xi$ be such a method. Budget balance on the pairs and cross-monotonicity give $\xi(i, N) \le \xi(i, \{i, j\})$ for both $j \ne i$. Add these six inequalities, two for each player: $2c \le 3$. For $c \le 3/2$, equal split works, with shares $1$, $1/2$ and $c/3$.

23. Let $S$ be a swing of $j$, so $S \cup \{j\}$ wins and $S$ loses. If $i \notin S$, then $S$ is also a swing of $i$, because $w_i \ge w_j$. If $i \in S$, then $S - \{i\} + \{j\}$ is a swing of $i$: adding $i$ gives back $S \cup \{j\}$, and its weight is at most $w(S)$. The map is one to one and keeps the size of $S$, so the swing counts compare size by size, and both indices are sums over sizes with nonnegative weights.

24. The pairs need $2 x(N) \ge 9$, but $x(N) = 3$. The prenucleolus equalizes the three pair excesses at 1, which gives $(-1, 1, 3)$. It is not individually rational, so the nucleolus differs. On the imputations $e(\{2, 3\}) = 2 + x_1 \ge 2$, so $x_1 = 0$; then the excesses $1 - x_2$ and $x_2$ of $\{1, 2\}$ and $\{1, 3\}$ are equal at $x_2 = 1/2$. The nucleolus is $(0, 1/2, 5/2)$.

25. In the threshold form of the entry, two points join when the time reaches their distance, and each terminal outside the root's component pays $1/|K|$ per unit of time. For $\{a, b, c\}$: $a$ and $b$ join at time 2, $c$ joins the root at time 3, and $\{a, b\}$ joins at time 5 through the edge $a$-$c$. So $a$ pays $2 + 1/2 + 1 = 7/2$, and the shares are $(7/2, 7/2, 3)$, with sum 10, the cost of the minimum spanning tree. For $\{a\}$ the share is 6, for $\{a, b\}$ it is $(4, 4)$, and for $\{a, c\}$ it is $(5, 3)$.

26. Pass to the savings game $v(S) = \sum_{i \in S} c_i - C(S)$, whose nucleolus is $(1/2, 7/4, 7/4)$. The cost nucleolus is $c$ minus that, $(1/2, 5/4, 17/4)$. The Shapley value charges the smallest plane less, $1/3$, and the largest more, $13/3$.
