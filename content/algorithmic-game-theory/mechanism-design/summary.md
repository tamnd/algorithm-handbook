## What to remember

- Agents have [quasilinear utility](/quasilinear-utility/) $v_i(o) - p_i$. A direct mechanism is DSIC if truth is a best report for every report of the others, and BIC if it is a best report in expectation when the others are truthful and types follow the prior. DSIC implies BIC for every prior. By the [revelation principle](/revelation-principle/), any equilibrium of any mechanism can be reproduced by a truthful direct one, though the direct one may have other equilibria too.
- [Groves mechanisms](/groves-mechanisms/) choose the outcome of largest reported welfare and charge $p_i = h_i(b_{-i}) - \sum_{j \ne i} b_j(x)$. The [Clarke pivot rule](/clarke-pivot-rule/) $h_i = \max_o \sum_{j \ne i} b_j(o)$ gives [VCG](/vcg-mechanism/), which with nonnegative values is ex post IR and never pays an agent.
- VCG is not budget balanced, and its revenue can be low or zero. With the [Green-Laffont theorem](/green-laffont-theorem/), on unrestricted domains the efficient DSIC mechanisms are exactly the Groves mechanisms, and none of them is strongly budget balanced on every profile.
- In a [single-parameter environment](/single-parameter-environment/), an allocation rule can be made DSIC if and only if it is monotone, and then [Myerson's lemma](/myerson-lemma/) fixes the payment up to $h_i(b_{-i})$: $p_i(b) = h_i(b_{-i}) + b_i x_i(b) - \int_0^{b_i} x_i(z, b_{-i})\, dz$. For a 0/1 rule this is a threshold price.
- With several private numbers, a rule is DSIC with some payments if and only if it is [cycle monotone](/cycle-monotonicity/); the payments are shortest-path distances. On unrestricted domains with at least three outcomes in the range, [Roberts' theorem](/roberts-theorem/) says only affine maximizers are DSIC.
- Giving up dominant strategies buys budget balance: the [AGV mechanism](/agv-mechanism/) is efficient, BIC with independent types and strongly budget balanced, but not IR. The [Myerson-Satterthwaite theorem](/myerson-satterthwaite-theorem/) shows that the gap cannot be closed in bilateral trade: with independent values on overlapping intervals with positive densities, no BIC, interim IR, weakly budget balanced mechanism is efficient. For two uniform values the efficient mechanism needs a subsidy of $1/6$, all the gains from trade.
- Correlation changes the picture. Under the full-rank condition of the [Cremer-McLean theorem](/cremer-mclean-theorem/), side bets on the others' reports extract the whole surplus with interim IR.
- An approximation algorithm with VCG payments is in general not truthful. [Maximal-in-range mechanisms](/maximal-in-range-mechanism/) are, and for makespan on $n$ unrelated machines no deterministic truthful mechanism beats ratio $n$, which VCG reaches ([Nisan-Ronen theorem](/nisan-ronen-conjecture/)).

## The main mechanisms side by side

| Mechanism | Truthful | Outcome | Budget | Participation | Needs |
| --- | --- | --- | --- | --- | --- |
| VCG (Clarke pivot) | DSIC | efficient | runs a surplus, may be 0 | ex post IR for nonnegative values | an exact welfare maximizer, $n + 1$ calls |
| Other Groves | DSIC | efficient | not balanced in general | depends on $h_i$ | the same |
| Affine maximizer | DSIC | best weighted score over a range | depends on $h_i$ | ex post IR with Clarke-style $h_i$ and nonnegative values | a maximizer over the range |
| AGV | BIC | efficient | strongly balanced | not IR in general | independent types, the prior |
| Myerson's lemma payments | DSIC | any monotone single-parameter rule | depends on the rule | ex post IR with $h_i = 0$ | one number per agent |
| Cremer-McLean side bets | DSIC under full rank | efficient | full surplus extraction | interim IR only | correlated types, full rank |
| Automated design (LP) | BIC or DSIC | optimal for the prior | as constrained | as constrained | small finite type sets |

: The main mechanisms of the chapter. Budget terms are those of [budget balance](/budget-balance/).

## Choosing a mechanism

If the welfare-maximizing outcome can be computed, use VCG: on rich domains Groves mechanisms are the only efficient DSIC ones, and the Clarke pivot is the member that is IR and never pays out. If a balanced budget matters more than dominant strategies and types are independent, use AGV, and check participation separately: low types can expect a loss.

If each agent has one private number, design a monotone allocation rule first and let Myerson's lemma give the payments. If the private information is a vector and the exact optimum is out of reach, restrict the range of outcomes and run VCG on it (maximal in range), or randomize and aim for truthfulness in expectation.

If the prior is known and the type sets are small, compute the optimal mechanism with a linear program. Learned mechanisms scale further, with incentive compatibility only approximate and measured on samples. Before relying on any Bayesian mechanism, check how it behaves when the prior is wrong.
