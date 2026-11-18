Two bidders value an item at amounts drawn independently and uniformly from $[0, 1]$. In a second-price auction each bids their value, and the seller's expected revenue is the expected lower value, $1/3$. In a first-price auction each bidder shades their bid to half their value in equilibrium, and the expected revenue is the expected higher value halved, again $1/3$. This is no accident. The revenue equivalence theorem says that, with independent private values and under its conditions, every auction that gives the item to the highest bidder in equilibrium earns the same expected revenue. A reserve price of $1/2$ breaks the tie: it raises the expected revenue to $5/12$, and Myerson's theorem shows that no auction does better in this setting.

Auctions are where mechanism design meets practice: sales of spectrum licences and government bonds, and the billions of small auctions that place advertisements beside search results. When the items are many and bidders want bundles, the winner determination problem becomes NP-hard, and the design of the auction becomes an algorithmic question as well.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Single-item formats.** The English, Dutch, first-price sealed-bid, Vickrey and all-pay auctions, the independent private values model, the equilibrium of the symmetric first-price auction, and the revenue equivalence theorem.
2. **Revenue.** Myerson's optimal auction, virtual valuations, regular distributions and ironing, reserve prices, the Bulow-Klemperer theorem, sequential posted pricing, selling items separately or as a bundle, and the sample complexity of revenue maximization.
3. **Correlated and common values.** Common value auctions and the linkage principle.
4. **Combinatorial auctions.** The winner determination problem, bidding languages and demand queries, the Lehmann-O'Callaghan-Shoham mechanism for single-minded bidders, and the simultaneous ascending auction.
5. **Markets of many auctions.** Position auctions, the generalized second-price auction and its locally envy-free equilibria, pacing equilibria, double auctions with McAfee's trade reduction, uniform price auctions, and the price of anarchy of first-price auctions.

## What to read meanwhile

Equilibrium bidding is a [Nash equilibrium](/nash-equilibrium/) of a game with private information; read Chapter 42.1 for the concept and [expected value](/expected-value/) in Volume 1 for the revenue calculations. Winner determination is a weighted [set packing problem](/set-packing/) (Volume 18), close to the [knapsack problem](/knapsack-problem/) of Volume 15 when there is one kind of item.

Posted prices and online advertising lead to Volume 19: the [prophet inequality](/prophet-inequality/) and the [secretary problem](/secretary-problem/) give the guarantees of sequential pricing, and [online bipartite matching](/online-bipartite-matching/) and the [Balance algorithm](/balance-algorithm/) for b-matching are the simplest models of ads assigned to arriving queries. Bertsekas's [auction algorithm](/auction-algorithm/) in Volume 7 uses rising prices to solve the assignment problem, an optimization method, not a market.
