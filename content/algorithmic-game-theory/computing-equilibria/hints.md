1. $\binom31\binom41 + \binom32\binom42 + \binom33\binom43 = 12 + 18 + 4 = 34$, and $\binom73 - 1 = 35 - 1 = 34$. The identity $\sum_k \binom{m}{k}\binom{n}{k} = \binom{m+n}{m}$ counts the term $k = 0$ too, which is the empty pair.

2. There are $4^3 = 64$ profiles, so 64 variables. Each player has $4 \cdot 3 = 12$ ordered pairs (recommended, deviation), so there are 36 incentive inequalities, plus the 64 sign constraints and one equation $\sum_s p(s) = 1$. The normal form has $3 \cdot 64 = 192$ payoff numbers.

3. With $z = 0$, $w = q$ is negative. With only $z_1 > 0$, $z_1 = 5/2$ and $w_2 = -7/2$. With only $z_2 > 0$, $z_2 = 3$ and $w_1 = -2$. With both positive, $w = 0$ gives $2z_1 + z_2 = 5$ and $z_1 + 2z_2 = 6$, so $z = (4/3, 7/3)$, the only solution.

4. Eight sequences: the empty sequence, a, b, three sequences that extend a and two that extend b. There are four equations: the empty sequence has weight 1, and the weights of the children at each of the three information sets sum to the weight of the sequence that leads there. The normal form has $2 \cdot 3 \cdot 2 = 12$ pure strategies, and the reduced form has $3 + 2 = 5$.

5. The stationary distribution $p$ of the matrix with rows $(3/4, 1/4)$ and $(1/2, 1/2)$: $p_1/4 = p_2/2$, so $p = (2/3, 1/3)$.

6. Five pieces: positions 2–3, 3–4, 4–5, 6–7 and 7–8. The number is odd, as the lemma says, because the two ends have different colours.

7. Three solutions: the sinks $011$ and $111$, and the source $100$. The strings $010$ and $101$ lie on a cycle and are not solutions.

8. From row 1: the best response is column 2, and the best row against it is row 1 again, so the output is the pure equilibrium (row 1, column 2), with gains 0 and 0. From row 2: column 3, then row 3; the output is $x = (0, 1/2, 1/2)$, $y = e_3$, and the gains are $1/4$ for the row player and 0 for the column player. From row 3: column 1, then row 2; the output is $x = (0, 1/2, 1/2)$, $y = e_1$, with gains $1/8$ and 0.

9. The positive parts are $(3, 0, 1, 0)$, which sum to 4, so the player plays $(3/4, 0, 1/4, 0)$.

11. Try supports of size 1, then 2, then 3. The three equilibria are the pure one (M, R) with payoffs $(5, 5)$; $x = (1/5, 4/5, 0)$, $y = (0, 3/7, 4/7)$ with payoffs $(20/7, 21/5)$; and the full-support one $x = (1/5, 13/40, 19/40)$, $y = (1/12, 5/12, 1/2)$ with payoffs $(8/3, 111/40)$. Their number is odd, as it must be in a nondegenerate game.

19. Let $M_{ij} = A_{ij} - a_j$. The row player's payoff is $x^{\mathsf T} M y + a^{\mathsf T} y$, and the second term does not depend on $x$. The column player's payoff is $-x^{\mathsf T} M y + b^{\mathsf T} x$, and the second term does not depend on $y$. So both players have the same best responses as in the zero-sum game $M$.

20. For each row $i$, the payoff against $\hat y$ is an average of $k$ independent values in $[0, 1]$ with mean at most $v$. By the Hoeffding inequality it exceeds $v + \varepsilon$ with probability at most $e^{-2k\varepsilon^2}$, and a union bound over the $n$ rows gives total failure probability below 1 when $k > \ln n / (2\varepsilon^2)$. For $n = 1000$ and $\varepsilon = 0.1$ the bound is $345.4$, so $k = 346$.

21. Let $p$ be a CCE with marginals $x$ and $y$, and let $w$ be its expected payoff to the row player. The row player's condition gives $w \ge \max_i (My)_i \ge v$, and the column player's gives $w \le \min_j (x^{\mathsf T} M)_j \le v$. So $w = v$, and $x$ and $y$ guarantee $v$.

22. Take a correlated equilibrium and condition on the column that it recommends. For each recommended column $j$, the conditional distribution $x_j$ of the row makes $j$ a best response of the follower. So the leader could commit to $x_j$ and, with ties broken in its favour, get at least $x_j^{\mathsf T} A e_j$. The CE payoff is an average of these numbers, so it is at most their maximum.
