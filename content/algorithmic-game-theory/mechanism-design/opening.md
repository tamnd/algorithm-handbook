A seller has one item and several buyers, each of whom knows privately what the item is worth to them. Ask for sealed bids, give the item to the highest bidder, and charge the second-highest bid. Then no buyer can gain by bidding anything other than their true value: the bid decides only whether they win, and the price they pay does not depend on it. This is Vickrey's second-price auction, and it is the simplest example of a mechanism that makes honesty a dominant strategy.

Mechanism design runs game theory backwards. Instead of asking what players will do in a given game, it asks which game to set up so that self-interested players, acting on private information, produce an outcome the designer wants: the efficient allocation, high revenue, or a fair decision. Its central results say what can be achieved and what cannot. The Vickrey-Clarke-Groves mechanism makes truth-telling dominant for any welfare-maximizing choice with quasilinear utilities, while the Myerson-Satterthwaite theorem shows that no mechanism for bilateral trade, with overlapping ranges of values, can be efficient, Bayesian incentive compatible, individually rational and budget balanced at once. Algorithmic mechanism design adds computation: a welfare-maximizing rule may be NP-hard, and replacing it by an approximation can destroy the incentives.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The model.** Quasilinear utility, direct revelation mechanisms and the revelation principle, dominant-strategy and Bayesian incentive compatibility, individual rationality and budget balance.
2. **Maximizing welfare.** The Vickrey-Clarke-Groves mechanism, Groves mechanisms and the Clarke pivot rule, the AGV mechanism, the Green-Laffont theorem, affine maximizers and Roberts' theorem.
3. **Characterizations.** Single-parameter environments, monotone allocation rules and Myerson's lemma, Rochet's cycle monotonicity, Border's theorem and Maskin's theorem.
4. **Limits.** The Myerson-Satterthwaite theorem and the Cremer-McLean theorem on full surplus extraction with correlated values.
5. **Algorithmic mechanism design.** Maximal-in-range and truthful-in-expectation mechanisms, truthful scheduling on unrelated machines and the Nisan-Ronen conjecture, strategyproof facility location, automated mechanism design, deep learning for auction design, and Bayesian persuasion.

## What to read meanwhile

The equilibrium concepts come from the [Nash equilibrium](/nash-equilibrium/) of Chapter 42.1. Voting is a mechanism without money, and [Borda count](/borda-count/) in Chapter 42.6 shows a rule that voters can manipulate by strategic lists. Clarke's pivot rule charges each agent the harm it does to the others, a computation that needs the optimal outcome with and without that agent.

The algorithmic side rests on approximation. The scheduling problem behind the Nisan-Ronen question is [makespan minimization on unrelated machines](/unrelated-machine-scheduling-makespan/) in Volume 18, and the facility location setting is the [facility location problem](/facility-location-problem/) of Volume 15. Mechanisms built from linear programs use [linear programming](/linear-programming-problem/) and [LP duality](/lp-duality/) from Volume 15.
