One player owns a left glove and two others each own a right glove. A matched pair sells for 1, a single glove for nothing. The question is how the three should share the 1 they can earn together. The core, the divisions that no group can improve on by leaving, gives everything to the owner of the left glove: if a right-glove owner received anything, the left-glove owner and the other right-glove owner could earn 1 on their own and split it. The Shapley value, which averages each player's marginal contribution over all orders of arrival, gives the left-glove owner $2/3$ and each right-glove owner $1/6$. One answer measures stability, the other fairness.

In a cooperative game the players can make binding agreements, so the question is how coalitions form and share what they earn. The same mathematics shares the cost of a runway, a network or a cloud service among its users and measures the voting power of council members with unequal weights. A game on $n$ players has $2^n$ coalitions, so the algorithms work with compact descriptions, linear programs and sampling.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The core.** Transferable utility games, the core and the Bondareva-Shapley theorem, convex games and Shapley's theorem on them, the least core, and the nucleolus, computed by a sequence of linear programs.
2. **The Shapley value.** Its definition and Shapley's uniqueness theorem, Owen's multilinear extension, and Monte Carlo estimation.
3. **Voting power.** Weighted voting games, the Shapley-Shubik and Banzhaf indices, the hardness of computing them and their computation by dynamic programming.
4. **Cost sharing.** The airport game, the minimum cost spanning tree game and Bird's rule, cost-sharing mechanisms, cross-monotonicity and the Moulin mechanism, the Jain-Vazirani mechanism for Steiner trees, bankruptcy problems and the Talmud rule, and the Shapley-Shubik assignment game.
5. **Bargaining and coalitions.** The Nash bargaining solution and Rubinstein's bargaining model, hedonic games, coalition structure generation and marginal contribution nets.

## What to read meanwhile

The Bondareva-Shapley theorem is an application of [LP duality](/lp-duality/) (Volume 15), and the core of the assignment game is the set of dual solutions of the [assignment problem](/assignment-problem/) of Volume 7. Cost sharing on networks uses the [minimum spanning tree](/minimum-spanning-tree/) and the [Steiner tree problem](/steiner-tree-problem/) of Volume 7 and the [Steiner forest](/steiner-forest/) of Volume 18.

Power indices of weighted voting games are counted by a dynamic program like the one for the [subset sum problem](/subset-sum-problem/) of Volume 39, pseudo-polynomial in the weights. Estimating the Shapley value from random orders is [Monte Carlo integration](/monte-carlo-integration/) (Volume 12). The Nash bargaining solution maximizes a product of gains, the rule behind [proportional fairness](/proportional-fairness/) in Volume 26.
