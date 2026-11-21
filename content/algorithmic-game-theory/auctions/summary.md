## What to remember

- **The second-price idea.** In the [Vickrey auction](/vickrey-auction/) the winner pays $\max(r, \text{highest other bid})$, so bidding your value is a dominant strategy. The [English auction](/english-auction/) has essentially the same outcome with private values.
- **First-price bidding.** In the symmetric model with independent private values, the equilibrium bid is $\beta(v) = \mathbb{E}[Y_1 \mid Y_1 < v]$, where $Y_1$ is the highest of the other values. For $n$ uniform values this is $(n-1)v/n$. The [Dutch auction](/dutch-auction/) is the same game.
- **Revenue equivalence.** With risk-neutral bidders and independent private values, two auctions that give the same allocation and the same payment to the lowest type earn the same expected revenue. This [revenue equivalence theorem](/revenue-equivalence-theorem/) is why the Vickrey, first-price and [all-pay](/all-pay-auction/) auctions tie in the symmetric model.
- **Virtual values.** For a bidder with distribution $F$ and density $f$, $\varphi(v) = v - (1 - F(v))/f(v)$, and a truthful auction earns its expected virtual surplus. With independent private values, [Myerson's optimal auction](/myerson-optimal-auction/) gives the item to the highest nonnegative virtual value. For i.i.d. [regular](/regular-distribution/) values it is a Vickrey auction with reserve $\varphi^{-1}(0)$, and for irregular values it uses [ironed](/ironing/) virtual values.
- **Competition beats optimization.** By the [Bulow-Klemperer theorem](/bulow-klemperer-theorem/), for i.i.d. regular values a Vickrey auction with $n + 1$ bidders earns at least as much as the optimal auction with $n$.
- **Common values.** With a shared value and noisy signals, the winner tends to be the bidder who overestimated most: the winner's curse. Under affiliation the [linkage principle](/linkage-principle/) puts the expected revenue of the English auction at or above that of the second-price auction, and that at or above the first-price auction.
- **Two-sided trade loses something.** No mechanism for one buyer and one seller is Bayesian incentive compatible, interim individually rational, weakly budget balanced and efficient at once. [McAfee's mechanism](/mcafee-trade-reduction/) is truthful in dominant strategies and runs no deficit by giving up at most one of the $k$ efficient trades.
- **Packages are hard.** The [winner determination problem](/winner-determination-problem/) of a [combinatorial auction](/combinatorial-auction/) is weighted set packing. It is NP-hard, and no polynomial algorithm approximates it within $m^{1/2-\epsilon}$ unless P = NP. For single-minded bidders, the [LOS mechanism](/single-minded-bidder-mechanism/) is truthful and within a factor $\sqrt{m}$.
- **Search advertising.** The [generalized second-price auction](/generalized-second-price-auction/) is not truthful. Its [envy-free equilibria](/gsp-envy-free-equilibrium/) are efficient and pay at least the VCG prices, and the cheapest of them gives exactly the VCG outcome.

## The main mechanisms side by side

| Mechanism | Winner pays | Truthful | Outcome |
|---|---|---|---|
| [Vickrey](/vickrey-auction/), English | highest other bid, or the reserve | yes, dominant strategy | efficient with no reserve |
| [First-price](/first-price-auction/), Dutch | its own bid | no | efficient in the symmetric equilibrium; welfare at least $1 - 1/e^2$ of the optimum in every Bayes-Nash equilibrium with independent values |
| [All-pay](/all-pay-auction/) | every bidder pays its bid | no | same revenue as Vickrey in the symmetric model |
| [Myerson](/myerson-optimal-auction/) | smallest bid that still wins | yes, dominant strategy | maximum expected revenue; not efficient |
| [VCG](/vcg-mechanism/) for packages | the harm it does to the others | yes, dominant strategy | efficient, but needs an exact NP-hard optimum |
| [LOS](/single-minded-bidder-mechanism/) | its critical value | yes, for single-minded bidders | $\sqrt{m}$-approximate welfare in $O(n^2 m)$ time |
| [Uniform price](/uniform-price-auction/), highest losing bid | one price for all units | only with unit demand | demand reduction otherwise |
| [McAfee](/mcafee-trade-reduction/) | buyers and sellers face separate prices | yes, dominant strategy | at least $1 - 1/k$ of the gains from trade, no deficit |
| [GSP](/generalized-second-price-auction/) | next bid down, per click | no | VCG outcome in the cheapest envy-free equilibrium |

: The mechanisms of the chapter. The bound for first-price auctions is the price of anarchy of [first-price auctions](/first-price-auction-price-of-anarchy/); with correlated values the known bound is $1 - 1/e$.

## Choosing a mechanism

- To give one item to the bidder who values it most, use a second-price or English auction.
- To earn the most from bidders whose distributions you know, set a reserve from the virtual value, or run Myerson's auction when the bidders are not symmetric. With i.i.d. regular bidders, one more bidder is worth at least as much.
- When the distributions are known only through samples, see the [sample complexity of revenue maximization](/sample-complexity-of-revenue-maximization/); [sequential posted prices](/sequential-posted-pricing/) are a simple alternative to an auction.
- When bidders want bundles, first check whether the bundles have structure (two items at most, intervals, a laminar family) that makes winner determination polynomial. Otherwise solve an integer program for VCG, or use LOS.
- When the value is common, prefer an open ascending format, which reveals information as the price rises.
