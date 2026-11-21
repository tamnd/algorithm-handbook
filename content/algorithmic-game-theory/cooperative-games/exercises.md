1. ◦ A three-player game has $v(\{1, 2\}) = 6$, $v(\{1, 3\}) = 4$, $v(\{2, 3\}) = 2$, $v(N) = 9$ and $v(\{i\}) = 0$ for each $i$. Is $(3, 2, 4)$ in the [core](/core-of-a-cooperative-game/)? Is $(5, 2, 2)$? Compute the [Shapley value](/shapley-value/) and say whether it is in the core.

2. ◦ On four players let $v = 3 u_{\{1, 2\}} + 6 u_{\{1, 2, 3\}}$, where the unanimity game $u_T$ has $u_T(S) = 1$ if $T \subseteq S$ and $u_T(S) = 0$ otherwise. Give $v(N)$ and the Shapley value, using the Harsanyi dividends. Which player is a null player?

3. ◦ For the [weighted voting game](/weighted-voting-game/) $[6; 4, 2, 1, 1]$, list the minimal winning coalitions and the players with a veto. Compute the [Shapley-Shubik index](/shapley-shubik-index/) and the raw and normalized [Banzhaf index](/banzhaf-index/).

4. ◦ Four planes need runways of lengths 2, 2, 5 and 6, and a runway costs its length. Compute the Shapley value of this [airport game](/airport-game/) by splitting each segment of the runway among the planes that need it.

5. ◦ Three creditors claim $(60, 90, 150)$ from an estate of 120. Compute the awards of the proportional rule, constrained equal awards, constrained equal losses and the [Talmud rule](/talmud-rule/), as defined in the [bankruptcy problem](/bankruptcy-problem/).

6. ◦ Two players split a dollar. Player 1 gets $x$ and has utility $x$; player 2 gets $1 - x$ and has utility $(1 - x)^{1/3}$. Disagreement gives both 0. Find the split of the [Nash bargaining solution](/nash-bargaining-solution/).

7. ◦ In the [Rubinstein bargaining model](/rubinstein-bargaining-model/) with $\delta_1 = 4/5$ and $\delta_2 = 1/2$, what share of the pie does player 1 get in the subgame perfect equilibrium, and in which period do the players agree? What is player 1's share if $\delta_2$ rises to $4/5$?

8. ◦ In a three-player game every pair is worth $3/4$, the grand coalition is worth 1 and each player alone is worth 0. Show that the core is empty. Find the value of the [least core](/least-core/) and every point of the least core.

9. ◦ How many coalition structures does a set of 6 agents have, and a set of 10? Compare each number with $3^n$, the bound on the number of pairs $C \subseteq S$ that the dynamic program of [coalition structure generation](/coalition-structure-generation/) visits.

10. ◦ A game has 20 players, and every marginal contribution lies in $[0, 1]$. You want every Shapley value within $0.02$ of the truth with probability at least $0.95$. How many random orders does the bound of [Shapley value sampling](/shapley-value-sampling/) ask for, and about how many evaluations of $v$ is that?

11. • A [minimum cost spanning tree game](/minimum-cost-spanning-tree-game/) has a source 0 and players 1, 2, 3, with edge costs $c_{01} = 5$, $c_{02} = 6$, $c_{03} = 7$, $c_{12} = 3$, $c_{13} = 6$ and $c_{23} = 2$. Compute the cost of every coalition, the allocation of [Bird's rule](/bird-rule/) and the Shapley value of the cost game. Is each of the two allocations in the core?

12. • A four-player game has $v(S) = 3$ for every $S$ with $|S| = 3$, $v(N) = 39/10$, and $v(S) = 0$ for all smaller coalitions. Give a balanced family with weights that proves the core empty, as in the [Bondareva-Shapley theorem](/bondareva-shapley-theorem/). For which values of $v(N)$ is the core nonempty? What is the least core value when $v(N) = 39/10$?

13. • Compute the Shapley-Shubik index and the raw and normalized Banzhaf index of every player of $[9; 5, 4, 3, 2, 1]$, by hand or with the [dynamic program](/power-index-dynamic-programming/). Do the two indices order the players in the same way?

14. • For the claims $(60, 90, 150)$, compute the Talmud award and the random arrival award for the estate 200, and the Talmud award for the estate 100. Check that both awards for 200 are award vectors, and that the Talmud awards for 100 and 200 are related as self-duality says.

15. • Let $v(S) = |S|^3$ on three players. Show that $v$ is a [convex game](/convex-game/). List the corners of the core, give the Shapley value, and decide whether $(2, 6, 19)$ and $(0, 8, 19)$ are in the core.

16. • A service costs 1 to provide to any nonempty set of players, and the cost-sharing method is equal split. Four players have values $(0.45, 0.40, 0.30, 0.20)$ and bid truthfully. Run the [Moulin mechanism](/moulin-mechanism/). Who is served, and what is lost compared with the set of largest surplus?

17. • Find the [nucleolus](/nucleolus/) of the game with $v(\{1, 2\}) = 4$, $v(\{1, 3\}) = 3$, $v(\{2, 3\}) = 2$, $v(N) = 6$ and $v(\{i\}) = 0$. Give its sorted excess vector, and compare it with the Shapley value.

18. • In an [assignment game](/assignment-game/) two buyers and two sellers have the gains $a_{11} = 5$, $a_{12} = 4$, $a_{21} = 4$, $a_{22} = 2$, where $a_{ij}$ is the gain when buyer $i$ trades with seller $j$. Find $v(N)$, the optimal assignment, and the buyer-optimal and seller-optimal points of the core.

19. • For $[4; 3, 1, 1, 1]$, write the partial derivative of the [multilinear extension](/owen-multilinear-extension/) with respect to player 1 on the diagonal $x = (t, t, t, t)$. Integrate it to get the Shapley-Shubik index of player 1, and evaluate it at $t = 1/2$ to get the raw Banzhaf index. What are the indices of the other players?

20. • A [hedonic game](/hedonic-game/) is symmetric and additively separable with $v(1, 2) = 2$, $v(1, 3) = -2$ and $v(2, 3) = 1$. Check all five partitions for Nash stability, and compute the potential of each.

21. • Take the subset sum instance $(3, 5, 7, 9)$ with target 12. Build the weighted voting game of the reduction in [hardness of power indices](/power-index-hardness/), with a player $x$ of weight 1. Count the swings of $x$, and give its raw Banzhaf index and its Shapley-Shubik index.

22. ★ A cost game on three players has $C(S) = 1$ for every $S$ with one or two players and $C(N) = c$, with $1 \le c \le 3$. Show that a budget balanced [cross-monotonic](/cross-monotonicity/) cost-sharing method exists exactly when $c \le 3/2$.

23. ★ In a weighted voting game, let $w_i \ge w_j$. Prove that player $i$ has at least as many swings as player $j$ of every size. Conclude that $\varphi_i \ge \varphi_j$ and $\beta_i \ge \beta_j$, so that the two indices never order two players of a weighted voting game in opposite ways.

24. ★ A game has $v(\{1, 2\}) = 1$, $v(\{1, 3\}) = 3$, $v(\{2, 3\}) = 5$, $v(N) = 3$ and $v(\{i\}) = 0$. Show that its core is empty, and compute its prenucleolus and its nucleolus.

25. ★ A root $r$ and terminals $a, b, c$ have the metric $d(r, a) = d(r, b) = 6$, $d(r, c) = 3$, $d(a, b) = 2$, $d(a, c) = d(b, c) = 5$, with no other vertices. Compute the [Jain-Vazirani](/jain-vazirani-steiner-cost-sharing/) shares for the sets $\{a\}$, $\{a, b\}$, $\{a, c\}$ and $\{a, b, c\}$. Check that the share of $a$ never rises, and compare each sum with the optimal Steiner tree cost.

26. ★ Compute the nucleolus of the airport cost game with runway needs $(1, 3, 6)$, where the excess of $S$ at a cost allocation $x$ is $x(S) - C(S)$ and each player pays at most its own cost. Compare it with the Shapley value $(1/3, 4/3, 13/3)$.
