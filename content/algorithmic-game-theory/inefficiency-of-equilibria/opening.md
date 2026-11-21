One unit of traffic travels from $s$ to $t$ over two roads. The first road takes time $x$ when a fraction $x$ of the traffic uses it; the second always takes time 1. Each driver picks the faster road, so everyone takes the first one, and everyone needs time 1. A planner who sent half of the traffic each way would get an average time of $3/4$. Selfish choice costs a factor $4/3$ here. Now take a network in which two routes of this kind are joined by a free shortcut. The drivers all use the shortcut, and the common travel time rises from $3/2$ to 2. Adding a road made every driver slower. This is Braess's paradox.

This chapter measures such losses. The price of anarchy of a game is the ratio between the cost of its worst equilibrium and the optimal cost; the price of stability uses the best equilibrium instead. The main results bound these ratios for whole classes of games: $4/3$ for nonatomic routing with affine latencies in any network, $5/2$ for atomic congestion games with affine costs, $n$ for the price of anarchy and the harmonic number $H(n)$ for the price of stability of fair cost sharing among $n$ players. Each bound holds for a stated class of latency functions and a stated kind of equilibrium, and the chapter keeps the two together. The same games raise algorithmic questions: when best-response dynamics stops, how long it takes, and how hard it is to compute an equilibrium at all.

## What the chapter covers

1. **Measuring inefficiency.** The [price of anarchy](/price-of-anarchy/) and the [price of stability](/price-of-stability/), with the order pure, mixed, correlated, coarse correlated in which the ratio can only grow.
2. **Selfish routing.** The [selfish routing model](/selfish-routing-model/), the [Wardrop equilibrium](/wardrop-equilibrium/) and the [Beckmann potential](/beckmann-potential/) that it minimizes, the [system optimal flow](/system-optimal-flow/) with its marginal cost characterization, [Pigou's example](/pigou-example/) and [Braess's paradox](/braess-paradox/).
3. **Bounds for nonatomic routing.** The [Roughgarden-Tardos bound](/roughgarden-tardos-four-thirds-bound/) of $4/3$ for affine latencies, the [Pigou bound](/pigou-bound/) for every class of latencies that contains the constants, and the [hardness of detecting Braess's paradox](/braess-paradox-detection-hardness/).
4. **Changing the routing game.** [Marginal cost tolls](/marginal-cost-tolls/) that make the optimum an equilibrium, [Stackelberg routing](/stackelberg-routing/) by a leader who controls part of the traffic, and [Nash flows over time](/nash-flows-over-time/), where queues replace latency functions.
5. **Potential and congestion games.** [Potential games](/potential-game/) and the [finite improvement property](/finite-improvement-property/), [atomic congestion games](/atomic-congestion-game/) and [Rosenthal's potential](/rosenthal-potential-theorem/), the [min-cost flow algorithm for symmetric network games](/symmetric-network-congestion-min-cost-flow/) and the [PLS-completeness of congestion games](/pls-completeness-of-congestion-games/) in general.
6. **Atomic bounds and smoothness.** The [smoothness framework](/smoothness-framework/), the [bound 5/2 for atomic linear congestion games](/atomic-linear-congestion-price-of-anarchy/), the [load balancing game](/load-balancing-game/) and its [price of anarchy](/price-of-anarchy-of-load-balancing/) for pure and mixed equilibria.
7. **Network design and formation.** The [Shapley network design game](/shapley-network-design-game/), its [harmonic price of stability](/harmonic-price-of-stability/), and the [network creation game](/network-creation-game/).

## A first reading

Read these in order:

1. [Price of anarchy](/price-of-anarchy/)
2. [Selfish routing model](/selfish-routing-model/)
3. [Wardrop equilibrium](/wardrop-equilibrium/)
4. [System optimal flow](/system-optimal-flow/)
5. [Pigou's example](/pigou-example/)
6. [Braess's paradox](/braess-paradox/)
7. [Roughgarden-Tardos bound](/roughgarden-tardos-four-thirds-bound/)
8. [Potential game](/potential-game/)
9. [Atomic congestion game](/atomic-congestion-game/)
10. [Rosenthal's potential theorem](/rosenthal-potential-theorem/)
11. [Smoothness framework](/smoothness-framework/)
12. [Load balancing game](/load-balancing-game/)
13. [Price of stability](/price-of-stability/)

They give the two models, the nonatomic bound $4/3$, the potential argument for pure equilibria and the method that turns one inequality into bounds for many kinds of equilibria. The [Beckmann potential](/beckmann-potential/) is worth reading with the system optimal flow, since the two problems differ only in their objective. Leave the hardness results, the tolls and the Stackelberg strategies, the network games and Nash flows over time for a second pass.

## Before you start

You need the [Nash equilibrium](/nash-equilibrium/), the [pure Nash equilibrium](/pure-nash-equilibrium/), the [normal-form game](/normal-form-game/) and the [mixed strategy](/mixed-strategy/) of Chapter 42.1, and the [coarse correlated equilibrium](/coarse-correlated-equilibrium/) for the smoothness framework. [Best-response dynamics](/best-response-dynamics/) and [no-regret dynamics](/no-regret-dynamics/) are in Chapter 42.2.

From Volume 7 you need the [flow network](/flow-network/), the [min-cost flow problem](/min-cost-flow-problem/), [Dijkstra's algorithm](/dijkstra/) and [breadth-first search](/breadth-first-search/); the last entry of the chapter uses the [max-flow problem](/max-flow-problem/). The Beckmann potential is a [convex optimization problem](/convex-optimization-problem/) of Volume 15, and the marginal cost conditions are the [KKT conditions](/kkt-conditions/) of the same volume. The load balancing game uses the [makespan](/makespan/) and [list scheduling](/list-scheduling/) of Volume 18, and its mixed equilibria use [balls into bins](/balls-into-bins/) from Volume 1. The hardness results need [NP-completeness](/np-complete/) and the class [PLS](/pls/) of Volume 39.
