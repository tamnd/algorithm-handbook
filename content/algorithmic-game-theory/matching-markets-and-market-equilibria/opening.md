Each year the US residency match assigns tens of thousands of new doctors to hospital programmes. Both sides submit rankings, and an algorithm based on deferred acceptance computes a stable matching, one where no doctor and programme prefer each other to the partners they got. Similar algorithms assign pupils to schools in Boston and New York, and kidney exchanges arrange cycles and chains of transplants among incompatible donor-patient pairs. None of these markets uses money.

Where money is allowed, the classical question is the competitive equilibrium: prices at which every buyer gets a bundle they like best at those prices and the market clears. Arrow and Debreu proved that equilibria exist under general conditions, and the first welfare theorem says that they are Pareto optimal. Computing them is another matter. In Fisher markets with linear utilities the equilibrium solves the Eisenberg-Gale convex program and takes polynomial time, while for richer utilities, such as separable piecewise-linear concave ones in Arrow-Debreu markets, finding one is PPAD-hard. In matching markets with prices, ascending auctions find the smallest equilibrium prices.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Two-sided matching.** The lattice of stable matchings, egalitarian stable matchings, the rural hospitals theorem, the strategyproofness of deferred acceptance for the proposing side and Roth's impossibility theorem, and stable matching with couples.
2. **Allocation without money.** The house allocation problem, serial and random serial dictatorship, probabilistic serial, the Shapley-Scarf housing market with top trading cycles and the Roth-Postlewaite theorem, popular matchings, and the Hylland-Zeckhauser mechanism and competitive equilibrium from equal incomes, with its approximate form.
3. **Schools and kidneys.** The school choice problem and the Boston mechanism, the kidney exchange problem with its cycle formulation, and top trading cycles and chains.
4. **Matching with prices.** The Demange-Gale-Sotomayor auction, the Kelso-Crawford salary adjustment process and gross substitutes.
5. **Market equilibria.** Arrow-Debreu markets and their existence theorem, competitive equilibria and the first welfare theorem, Fisher markets and the Eisenberg-Gale program, the Devanur-Papadimitriou-Saberi-Vazirani algorithm and Orlin's strongly polynomial algorithm, proportional response dynamics, tatonnement, and the PPAD-hardness of market equilibria.

## What to read meanwhile

The matching side is written in Volume 7: [stable matching](/stable-matching/), the [Gale-Shapley algorithm](/gale-shapley/) and [stable matching rotations](/stable-matching-rotations/), with [bipartite matching](/bipartite-matching/) and the [Hopcroft-Karp algorithm](/hopcroft-karp/). With prices and transferable values, matching becomes the [assignment problem](/assignment-problem/), solved by the [Hungarian algorithm](/hungarian-algorithm/) or by Bertsekas's [auction algorithm](/auction-algorithm/), whose prices are the dual variables of [LP duality](/lp-duality/) (Volume 15).

For equilibria, the class [PPAD](/ppad/) is in Volume 39, and the Eisenberg-Gale program is solved with the [KKT conditions](/kkt-conditions/) of Volume 15. [Market-based task allocation](/market-based-task-allocation/) in Volume 37 assigns tasks to robots by prices.
