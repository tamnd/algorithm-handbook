2. Through $\mathit{stack}(A, B)$ the regression is $\{\mathit{on}(B, C), \mathit{holding}(A), \mathit{clear}(B)\}$, which holds when B is on C and A is in the hand. Through $\mathit{stack}(B, C)$ it is $\{\mathit{on}(A, B), \mathit{holding}(B), \mathit{clear}(C)\}$. That set is defined, since the action deletes no goal fact, but it is never reached: a block is picked up only when it is clear, and $\mathit{stack}$ needs a clear target, so nothing lies on a block in the hand. A backward search should prune it.

3. $h^{\max} = 2$, $h^{\mathrm{add}} = 4$, $h^{+} = 3$ and $h^* = 3$, with the plan $a, c, b$. The order matters, because $b$ deletes $q$, which $c$ still needs. $h^{\max}$ and $h^{+}$ are lower bounds on every task; $h^{\mathrm{add}}$ counts $a$ twice and overestimates here.

4. Level 1 has $h_x$ and $h_y$, mutex with each other, since both picks need and delete $\mathit{he}$. Both goals appear at level 2, so $h^{\max} = 2$, but they are mutex at levels 2 and 3. They are first not mutex at level 4, where Graphplan finds the plan.

6. The rounds give $(V(s_1), V(s_2)) = (1, 1)$, $(2, 6/5)$ and $(11/5, 7/5)$. With $a$ and $c$, $V_1 = 1 + V_2$ and $V_2 = 1 + 0.2 V_1$, so $V^* = (5/2, 3/2)$. The other actions cost more: $4 > 5/2$ and $2 > 3/2$. The optimal policy is $a$ in $s_1$ and $c$ in $s_2$.

10. $RRRL$. Three moves right put the robot in cell 4 from every start, and one move left brings it to cell 3. No plan of three actions works; Exercise 25 proves the general bound.

11. For $n = 3$: $h^{\max} = 3$, $h^{\mathrm{add}} = 7$, $h^{+} = 3$ and $h^* = 7$. In general $h^{\max}(\mathit{on}_i) = i$, and $h^{\mathrm{add}}(\mathit{on}_i) = 1 + \sum_{j < i} 2^{j-1} = 2^{i-1}$, so $h^{\max} = n$ and $h^{\mathrm{add}} = 2^n - 1$. The relaxed plan $\mathit{inc}_1, \dots, \mathit{inc}_n$ gives $h^{+} = n$. In the real task exactly one action applies in each state, the one for the lowest bit that is off, so the only plan has $2^n - 1$ actions. Here $h^{\mathrm{add}}$ happens to equal $h^*$, while the admissible $h^{\max}$ is exponentially far below.

12. $V_k = \min(3, 1 + V_{k-1}/2)$ gives $V_k = 2 - 2^{1-k}$, so the gap is $2^{1-k}$. It is $1/64$ at $k = 7$ and $1/128 \le 0.01$ at $k = 8$. Risky is optimal, with $V^* = 1 + V^*/2 = 2 < 3$.

14. The backups are $V(s_1) = \min(1 + 0, 4) = 1$ with $a$; $V(s_2) = \min(1 + 0.2 \cdot 1, 2) = 1.2$ with $c$; $V(s_1) = 1 + 1.2 = 2.2$; and $V(s_2) = 1 + 0.2 \cdot 2.2 = 1.44$. Both values stay below $V^* = (2.5, 1.5)$, as they must from an admissible start.

17. $\Delta = 2$, $-4$ and $0$, so $P(O \mid G) = 1/(1 + e^{-2}) \approx 0.881$, $1/(1 + e^{4}) \approx 0.018$ and $1/2$. Normalizing gives the posterior $0.630$, $0.013$ and $0.357$.

21. $K_3 = \{\mathit{pkgoffice}\}$, $K_2 = \{\mathit{atoffice}, \mathit{holding}\}$, $K_1 = \{\mathit{athome}, \mathit{holding}\}$ and $K_0 = \{\mathit{athome}, \mathit{pkghome}\}$. The monitor runs the suffix after the largest $k$ with $K_k$ true. In $\{\mathit{athome}, \mathit{holding}\}$ that is $K_1$: run *go* and *drop*. In $\{\mathit{atoffice}, \mathit{holding}\}$ it is $K_2$: run *drop*. In $\{\mathit{atoffice}, \mathit{pkghome}\}$ no $K_k$ holds, so the monitor must replan. This domain has no action back home, so the goal can no longer be reached.

23. $V_1(b) = \max(2b - 1,\ 2 - 3b,\ 0.5)$, and $C$ is best for $0.5 \le b \le 0.75$. At $b = 0.1$ the best vector is $B$ (value 1.7), and at $b = 0.9$ it is $A$ (value 0.8). So PBVI drops $C$ and keeps $\max(2b - 1, 2 - 3b)$, a lower bound. The gap is largest where $A$ and $B$ cross, at $b = 0.6$: the PBVI value there is $0.2$ against $0.5$, so the gap is $0.3$.

24. Build the plan backward. Keep a set $R$ of goals not yet settled, with $R = G$ at the start. An action is safe for $R$ when it deletes no fact of $R$. While some safe action adds a fact of $R$, choose one and remove the facts it adds from $R$. Answer yes exactly when the final $R$ is contained in $I$, and run the chosen actions in reverse order of choice. Safety is monotone: an action that is safe for $R$ stays safe for every subset of $R$. Read any plan from its end and it becomes a sequence of such removals. Use this to show that the final $R$ of the greedy procedure is contained in the set that the plan leaves, and that set is contained in $I$.

25. By induction, the belief is always an interval $[l, r]$. A move shrinks the width $r - l$ by one when it pushes against a wall ($L$ with $l = 1$, or $R$ with $r = n$), and otherwise leaves the width unchanged. So $n - 1$ moves are needed before the belief becomes a single cell, and that cell is 1 or $n$. Then $j - 1$ or $n - j$ further moves are needed. The plans $L^{n-1} R^{j-1}$ and $R^{n-1} L^{n-j}$ meet the bound.

26. If $V \le V^*$, then $\min_a [c(s, a) + \sum_t P(t \mid s, a) V(t)] \le \min_a [c(s, a) + \sum_t P(t \mid s, a) V^*(t)] = V^*(s)$. For the second part, let $s_0$ have *go*, which costs 1 and leads to $s_1$, and *safe*, which costs 5 and leads to the goal. Let $s_1$ reach the goal at cost 1, so $V^*(s_0) = 2$. Set $h(s_1) = 10$. The greedy choice at $s_0$ is *safe*, since $5 < 1 + 10$, so no trial ever visits $s_1$ and its value is never corrected.

27. $P(O \mid G)$ tends to 1 when $\Delta > 0$, equals $1/2$ when $\Delta = 0$, and behaves like $e^{\beta \Delta}$ when $\Delta < 0$. So in the first case the posterior tends to weights 1 on the goals with $\Delta > 0$ and $1/2$ on those with $\Delta = 0$, normalized; the goals with $\Delta = 0$ keep some mass. In the second case it becomes uniform over the goals with $\Delta = 0$. In the third it becomes uniform over the goals with the largest $\Delta$.
