One unit of traffic travels from $s$ to $t$ over two roads. The first always takes one hour. The second takes $x$ hours when a fraction $x$ of the traffic uses it. Every driver prefers the second road, which never takes longer than an hour, so in equilibrium everybody takes it and the trip takes an hour. If a planner sent half the traffic each way, the average trip would take three quarters of an hour. The ratio $4/3$ of the two costs is the price of anarchy of this example, Pigou's. Braess's paradox goes further: in a network where the equilibrium trip takes $3/2$ hours, adding a road of zero length moves everyone to a new equilibrium where the trip takes 2 hours.

The price of anarchy measures the loss when users choose for themselves instead of following a plan. Its theory gives bounds for whole classes of networks: for selfish routing with linear latency functions, Roughgarden and Tardos proved that the ratio is never worse than $4/3$, the value of Pigou's example. The same questions arise in load balancing and network design.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Selfish routing.** The selfish routing model, the Wardrop equilibrium and the system optimal flow, the Beckmann potential, Pigou's example, Braess's paradox and the hardness of detecting it.
2. **Bounds on the loss.** The price of anarchy and the price of stability, the Pigou bound and the $4/3$ bound for linear latencies, the smoothness framework, and the bounds for atomic linear congestion games and for selfish load balancing.
3. **Congestion and potential games.** Congestion games and Rosenthal's theorem that they have pure equilibria, potential games and the finite improvement property, the PLS-completeness of finding an equilibrium, and the min-cost flow method for symmetric network congestion games.
4. **Designing networks.** The Shapley network design game and its harmonic price of stability, and the network creation game.
5. **Steering selfish users.** Marginal cost tolls, Stackelberg routing and Nash flows over time.

## What to read meanwhile

The solution concept is the [Nash equilibrium](/nash-equilibrium/) of Chapter 42.1, and [Nash equilibrium computation](/nash-equilibrium-computation/) in Chapter 42.2 explains why finding one can be hard. A pure equilibrium of a congestion game is found by local search instead, and the problem lies in the class [PLS](/pls/) of Volume 39 (see [local search problems](/local-search-problem/) in Volume 2).

A system optimal flow minimizes a convex cost over network flows, a generalization of the [min-cost flow problem](/min-cost-flow-problem/) of Volume 7; see also [convex functions](/convex-function/) and the [KKT conditions](/kkt-conditions/) in Volume 15. Load balancing games are selfish versions of [list scheduling](/list-scheduling/) and [makespan scheduling on unrelated machines](/unrelated-machine-scheduling-makespan/) in Volume 18.
