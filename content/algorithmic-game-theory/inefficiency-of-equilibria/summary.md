## What to remember

- **The ratio depends on the equilibrium class.** The [price of anarchy](/price-of-anarchy/) is the supremum of $C(\text{equilibrium})/\mathrm{OPT}$ over the equilibria of a class, and the [price of stability](/price-of-stability/) the infimum. Pure equilibria are mixed, mixed are correlated, correlated are coarse correlated, so the price of anarchy can only grow along this chain.
- **Wardrop equilibria minimize a potential.** In the [selfish routing model](/selfish-routing-model/) the equilibria are the minimizers of the [Beckmann potential](/beckmann-potential/) $\sum_e \int_0^{f_e} \ell_e$, so they exist and all have the same cost. The [system optimal flow](/system-optimal-flow/) is the equilibrium for the marginal costs $\ell_e + x\ell_e'$ when each $x\ell_e(x)$ is convex.
- **Affine latencies give 4/3.** For nonatomic routing with affine latencies in any multicommodity network the price of anarchy is at most $4/3$, reached by [Pigou's example](/pigou-example/) ([Roughgarden-Tardos bound](/roughgarden-tardos-four-thirds-bound/)). For any class with the constant functions it is the [Pigou bound](/pigou-bound/) $\alpha(\mathcal C)$, about $1.626$ for quadratics and growing like $d/\ln d$ for degree $d$.
- **Braess's paradox is bounded and hard to undo.** With affine latencies, adding edges raises the equilibrium cost by at most a factor $4/3$; removing nothing is a $4/3$-approximation to the best subnetwork, and no polynomial algorithm does better unless P = NP ([detection hardness](/braess-paradox-detection-hardness/)).
- **Tolls fix routing exactly.** The [marginal cost toll](/marginal-cost-tolls/) $\tau_e = f^*_e\,\ell_e'(f^*_e)$ makes the optimal flow an equilibrium. On parallel links, a [Stackelberg](/stackelberg-routing/) leader with a fraction $\alpha$ of the traffic, using LLF, gets within $1/\alpha$ for any latencies and $4/(3+\alpha)$ for linear ones.
- **Rosenthal's potential gives pure equilibria, not fast ones.** Every [atomic congestion game](/atomic-congestion-game/) is a [potential game](/potential-game/), so improvement paths are finite ([finite improvement property](/finite-improvement-property/)). Finding a pure equilibrium is [PLS-complete](/pls-completeness-of-congestion-games/), also for symmetric games and for network games, and some improvement paths are exponentially long; symmetric network games are solved by [min-cost flow](/symmetric-network-congestion-min-cost-flow/).
- **Smoothness extends one bound to many equilibria.** A $(\lambda, \mu)$-smooth cost game has price of anarchy at most $\lambda/(1 - \mu)$ for pure, mixed, correlated and coarse correlated equilibria, and no-regret play approaches it. Affine atomic congestion games are $(5/3, 1/3)$-smooth, which gives the tight [5/2](/atomic-linear-congestion-price-of-anarchy/).
- **Makespan is not a sum.** In the [load balancing game](/load-balancing-game/) on identical machines, pure equilibria are within $2 - 2/(m+1)$ of the optimum and mixed equilibria within $\Theta(\log m/\log\log m)$, and the price of stability is 1 ([price of anarchy of load balancing](/price-of-anarchy-of-load-balancing/)).
- **Cost sharing has a large anarchy and a small stability.** In the [Shapley network design game](/shapley-network-design-game/) the price of anarchy is $n$ and the price of stability at most $H(n)$, tight in directed networks ([harmonic price of stability](/harmonic-price-of-stability/)).

| Game | Equilibria | Cost | Price of anarchy | Price of stability |
|---|---|---|---|---|
| Nonatomic routing, affine latencies | Wardrop | total latency | $4/3$ | $4/3$ |
| Nonatomic routing, polynomials of degree $\le d$ | Wardrop | total latency | $\alpha_d = \Theta(d/\ln d)$ | $\alpha_d$ |
| Atomic congestion, affine costs | pure to coarse correlated | sum of costs | $5/2$ | $1 + 1/\sqrt3 \approx 1.577$ (pure) |
| Load balancing, identical machines | pure | makespan | $2 - 2/(m+1)$ | 1 |
| Load balancing, identical machines | mixed | expected makespan | $\Theta(\log m/\log\log m)$ | 1 |
| Load balancing, related machines | pure / mixed | makespan | $\Theta(\log m/\log\log m)$ / $\Theta(\log m/\log\log\log m)$ | 1 |
| Load balancing, unrelated machines | pure | makespan | unbounded | 1 |
| Shapley network design | pure | sum of edge costs | $n$ | $\le H(n)$, tight for directed graphs |

: Worst-case ratios of the chapter's games, with the class of equilibria for which the entries state them. In nonatomic routing all equilibria have the same cost, so the two prices coincide.

## Using the results

- **To bound a new routing game,** find its class of latency functions and compute the Pigou bound on two links; with the constants in the class, no network does worse.
- **To bound a game with atomic players,** look for a smoothness inequality first. It covers every equilibrium class and no-regret learning at once.
- **To show that pure equilibria exist,** look for a potential: Rosenthal's for congestion games, $\sum_e c_e H(x_e)$ for fair cost sharing. Comparing the potential with the cost also bounds the price of stability.
- **To compute an equilibrium,** use convex optimization for Wardrop flows and min-cost flow for symmetric network congestion games; in general congestion games, local search can take exponentially many steps.
- **To reduce the loss,** use marginal cost tolls or a Stackelberg leader. With affine latencies, removing edges gains at most $4/3$, and the best removal is hard to find.
