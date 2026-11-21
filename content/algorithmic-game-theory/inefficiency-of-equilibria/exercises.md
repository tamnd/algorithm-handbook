1. ◦ Two players each choose between two strategies, U or D for the row player and L or R for the column player. The costs (row, column) are $(1, 2)$ at (U, L), $(4, 3)$ at (U, R), $(3, 5)$ at (D, L) and $(2, 2)$ at (D, R). Check with the four-cycle test that this is an exact [potential game](/potential-game/), find a potential with $\Phi(U, L) = 0$, and find the pure equilibria as the local minima of $\Phi$. With the sum of the costs as social cost, give the [price of anarchy](/price-of-anarchy/) and the [price of stability](/price-of-stability/) over pure equilibria.

2. ◦ Two parallel links join $s$ to $t$ with latencies $\ell_1(x) = 2x$ and $\ell_2(x) = x + 1$, and the traffic rate is $r = 2$. Find the [Wardrop equilibrium](/wardrop-equilibrium/) and its cost, the [system optimal flow](/system-optimal-flow/) and its cost, and the price of anarchy of the instance.

3. ◦ For the instance of Exercise 2, compute the [marginal cost tolls](/marginal-cost-tolls/) on the two links, check that the optimal flow is an equilibrium for the tolled latencies, and compute the total toll revenue.

4. ◦ Three parallel links join $s$ to $t$ with latencies $\ell_1(x) = x + 2$, $\ell_2(x) = 2x$ and $\ell_3(x) = 4x$, and $r = 4$. Show that the flow $(1, 2, 1)$ is not a Wardrop equilibrium, and find the equilibrium, its common latency and its cost.

5. ◦ In the network of [Braess's paradox](/braess-paradox/) with edges $s \to v$ of latency $x$, $v \to t$ of latency 1, $s \to w$ of latency 1, $w \to t$ of latency $x$ and the shortcut $v \to w$ of latency 0, find the equilibrium latency with and without the shortcut for $r = 1/2$ and for $r = 3/2$. For which of the two rates does the shortcut hurt?

6. ◦ An [atomic congestion game](/atomic-congestion-game/) has two players and resources $e$, $f$, $g$ with costs $c_e(1) = 1$, $c_e(2) = 3$, $c_f(1) = c_f(2) = 5$ and $c_g(1) = c_g(2) = 1$. Player 1 chooses $\{e\}$ or $\{f, g\}$, and player 2 chooses $\{f\}$ or $\{e, g\}$. Compute [Rosenthal's potential](/rosenthal-potential-theorem/) and the total cost of the four profiles, find every pure equilibrium, and give the price of anarchy and the price of stability.

7. ◦ Three players of a [Shapley network design game](/shapley-network-design-game/) go from $s$ to $t$ over two parallel edges of costs 3 and 2; the players on an edge split its cost equally. Find the pure equilibria, the potential $\sum_e c_e H(x_e)$ of each profile, and the price of anarchy and the price of stability.

8. ◦ In the [load balancing game](/load-balancing-game/) on two identical machines, jobs of weights 3, 3, 2, 2, 2 each choose a machine and pay its load. Find the optimal makespan, every pure equilibrium up to swapping the machines, and the price of anarchy of this instance over pure equilibria. Compare with $2 - 2/(m+1)$.

9. ◦ In the [network creation game](/network-creation-game/) with $n = 5$ players, compute the social cost of the complete graph $K_5$ and of the star for $\alpha = 1/2$ and for $\alpha = 4$, and say which is optimal in each case. At which $\alpha$ do the two costs agree?

10. • For the three links of Exercise 4 at $r = 4$, find the system optimal flow from the marginal cost latencies, its cost and the price of anarchy. Check that the optimal flow is half of the Wardrop equilibrium at rate 8, and explain why this holds for every instance with affine latencies.

11. • In the Braess network of Exercise 5 with rate $r > 0$, find the equilibrium latency with the shortcut as a function of $r$, and the path flows. Show that the shortcut raises the latency exactly when $2/3 < r < 2$, and find the rate at which the ratio of the two latencies is largest. Compare the largest ratio with the bound for affine latencies.

12. • Pigou's network has $\ell_1(x) = x^2$ and $\ell_2(x) = 1$, with rate $r$. For which $r$ is the equilibrium optimal? Give the price of anarchy as a function of $r$ for $r > 1/\sqrt3$, and show that it is largest at $r = 1$, with the value of the [Pigou bound](/pigou-bound/) for quadratics.

13. • Compute the Pigou bound $\alpha(\mathcal C)$ of the class $\mathcal C = \{a\sqrt x + b : a, b \ge 0\}$. Conclude that every nonatomic instance with such latencies, in any network, has price of anarchy at most this value, and give an instance that reaches it.

14. • In the instance of Exercise 2, a leader controls a fraction $\alpha$ of the traffic and uses the LLF strategy of [Stackelberg routing](/stackelberg-routing/): it fills the links in decreasing order of their latency at the optimum, up to their optimal flow. The followers then reach an equilibrium. Find the total cost as a function of $\alpha \in [0, 1]$, and the smallest $\alpha$ for which the outcome is optimal. Check the value at $\alpha = 1/2$ against $4/(3 + \alpha)$.

15. • In an atomic version of Pigou's network, $n$ players each choose link $a$, with cost $k$ when $k$ players use it, or link $b$, with constant cost $n$. Find all pure equilibria, and the price of anarchy and the price of stability for even and for odd $n$. Give the values for $n = 4$ and $n = 5$, and compare with the $5/2$ of the [atomic linear congestion bound](/atomic-linear-congestion-price-of-anarchy/) and the $4/3$ of nonatomic routing.

16. • A symmetric network congestion game has three players from $s$ to $t$ and edges $s \to a$ with cost $k$, $a \to t$ with cost $3k + 5$, $s \to b$ with cost $2k$, $b \to t$ with cost $k + 2$ and $a \to b$ with cost $2k$, where $k$ is the number of players on the edge. Run the [min-cost flow algorithm](/symmetric-network-congestion-min-cost-flow/) with residual costs $c_e(x_e + 1)$ forward and $-c_e(x_e)$ backward, and give the length of the shortest path in each round. Give the resulting equilibrium, its potential and total cost, the optimal total cost, and the price of anarchy.

17. • Take the graph on $a, b, c, d$ with edge weights $w_{ab} = 1$, $w_{bc} = 2$, $w_{cd} = 3$, $w_{da} = 4$, $w_{ac} = 5$, and the congestion game built from it in the proof of [PLS-completeness](/pls-completeness-of-congestion-games/). Start with all players on side 0. Follow improvement dynamics (a) when $b$ moves first and then $d$, (b) when $a$ moves first and then $b$, giving $\Phi$ after each move. Show that both runs end at pure equilibria, and that only one of them is a maximum cut.

18. • On two identical machines, two jobs of weights $w_1 \le w_2$ each choose a machine uniformly at random. Show that this is a mixed Nash equilibrium, find its expected makespan and its ratio to the optimum, and show that the ratio is at most $3/2$. Then find the expected makespan of three unit jobs that choose uniformly, and check that this is an equilibrium too.

19. • Two related machines have speeds 2 and 1, and a job on a machine of speed $s$ with load $L$ pays $L/s$. Jobs of weights 3, 2 and 1 each choose a machine. Find every pure equilibrium, the optimal makespan, and the price of anarchy and the price of stability of the instance.

20. • In the network creation game with $n = 5$, let each player $i$ buy the edge to player $i + 1 \bmod 5$, so the graph is a 5-cycle. List the deviations of a player, and show that the cycle is a pure equilibrium exactly when $1 \le \alpha \le 4$. For $\alpha = 3/2$, compare its social cost with the optimum.

21. ★ Prove that the Pigou bound of the class of nonnegative, nondecreasing, concave latency functions is $4/3$. Conclude that the [Roughgarden-Tardos bound](/roughgarden-tardos-four-thirds-bound/) of $4/3$ holds for concave latencies too.

22. ★ Two parallel links of capacity $u > r$ carry rate $r$; link 1 has the M/M/1 latency $\ell_1(x) = 1/(u - x)$, and link 2 has the constant latency $1/(u - r)$. Show that sending all traffic on link 1 is an equilibrium, find the optimal flow, and prove that the price of anarchy of the instance is $\frac12\left(1 + 1/\sqrt{1 - r/u}\right)$. Evaluate it for $u = 2$, $r = 1$.

23. ★ The Pigou bound for polynomials of degree at most $d$ is $\alpha_d = \left[1 - d(d+1)^{-(d+1)/d}\right]^{-1}$. Prove that $\alpha_d \ln d / d \to 1$ as $d \to \infty$, and explain why the ratio approaches 1 slowly, using the value $\alpha_d \approx 67497$ at $d = 10^6$.

24. ★ In a symmetric singleton congestion game, $n$ players choose among parallel links with nondecreasing costs $c_e(k)$. The greedy algorithm adds the players one at a time, each to a link that minimizes $c_e(x_e + 1)$ for the current loads $x$. (a) Prove that the result is a pure Nash equilibrium. (b) Show that the claim fails for decreasing costs, with two players, link $a$ of costs $c_a(1) = 3$, $c_a(2) = 1$, and link $b$ of costs $c_b(1) = 2$, $c_b(2) = 4$.

25. ★ Write a program that lists all pure equilibria of the network creation game with $n = 4$ players, by trying every strategy of every player in every profile ($8^4$ profiles). For $\alpha = 3/2$, which graphs are equilibria, and what are the price of anarchy and the price of stability? Repeat for $\alpha = 1$.
