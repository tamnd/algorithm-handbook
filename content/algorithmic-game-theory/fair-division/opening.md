Two children share a cake. One cuts it into two pieces that she values equally, and the other chooses. Neither has reason to complain: the cutter gets half by her own measure whatever happens, and the chooser takes the piece he prefers. Divide and choose is proportional, each child gets at least half by their own valuation, and envy-free, neither prefers the other's piece, though neither knows how the other values the cake.

Fair division asks how far this goes. With three or more agents, envy-free cake cutting is possible but hard: the Selfridge-Conway procedure handles three agents with five cuts, while a bounded protocol for any number of agents was found only in 2016, by Aziz and Mackenzie, and Stromquist proved that no finite protocol can give three or more agents connected envy-free pieces. With indivisible goods, such as heirlooms or offices, envy-freeness may be impossible, and the field relaxes it: envy-free up to one good always exists, while maximin share allocations do not always exist and are approximated. The same questions apply to chores and rent.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Cake cutting.** The cake cutting problem and the Robertson-Webb query model, proportional division, divide and choose, the last diminisher, the Dubins-Spanier moving knife, the Even-Paz algorithm, and the Edmonds-Pruhs lower bound for proportional cake cutting.
2. **Envy-free protocols.** Envy-freeness, the Selfridge-Conway and Brams-Taylor procedures, the Aziz-Mackenzie protocol, the Stromquist moving knife and Stromquist's impossibility theorem, and the adjusted winner procedure for two parties.
3. **Indivisible goods.** Fair allocation of indivisible goods, envy-freeness up to one good and up to any good, round-robin allocation and envy-cycle elimination, the maximin share, the nonexistence of maximin share allocations, approximate maximin share allocations, and the existence of EFX allocations for three agents.
4. **Nash welfare.** The maximum Nash welfare allocation, its unreasonable fairness, and the Barman-Krishnamurthy-Vaish algorithm for allocations that are envy-free up to one good and Pareto optimal.
5. **Chores, rent and splitting.** Chore division, rental harmony and Su's algorithm, consensus halving and the necklace splitting theorem.

## What to read meanwhile

Fairness in computer systems has written entries in Volume 26: [max-min fairness](/max-min-fairness/), [proportional fairness](/proportional-fairness/), which maximizes the sum of logarithms of the rates, as maximum Nash welfare does for goods, and [dominant resource fairness](/dominant-resource-fairness/) for jobs that need several resources. [Pareto optimality](/pareto-optimality/) is in Volume 15.

When each agent gets one item, fair and efficient allocation becomes matching: read the [assignment problem](/assignment-problem/) and the [Hungarian algorithm](/hungarian-algorithm/) in Volume 7. Su's rental harmony algorithm follows a path through a triangulation labelled by Sperner's lemma, the kind of argument behind the class [PPAD](/ppad/) of Volume 39.
