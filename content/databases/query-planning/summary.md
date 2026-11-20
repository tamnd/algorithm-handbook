## What to remember

- A **query plan** is a tree of operators with an algorithm and an access path for each one. For $n$ relations there are $n!$ left-deep join trees and $(2n-2)!/(n-1)!$ bushy ones. Without cross products the count depends on the query graph: $2^{n-1}$ left-deep trees for a chain, $2(n-1)!$ for a star, $n!$ for a clique.
- **Rewrites** are justified by algebraic equivalences, and the semantics matter. Pushdown is always valid for inner joins and on the preserved side of an outer join. Some laws hold for sets but not for bags, and outer joins do not reassociate freely. Unnesting a COUNT subquery needs an outer join, and NOT IN a null-aware antijoin. Eager aggregation moves a GROUP BY below a join only for decomposable aggregates.
- **Size estimates** come from histograms and selectivities under uniformity, containment and [attribute value independence](/attribute-value-independence/). Independence can underestimate a conjunction by a factor up to $1/\max(s_1, s_2)$. If each of $n$ frequencies is off by at most a factor $c$, a join of $n$ relations can be off by $c^n$, and this is tight; the q-error $\max(\hat c/c, c/\hat c)$ is the usual measure.
- **Better estimates** have their own guarantees. GEE estimates a distinct count from $r$ of $n$ rows with ratio error of order $\sqrt{n/r}$, and no estimator that reads $r$ rows does better on every column. A pessimistic estimate is an upper bound, such as $|R \bowtie S| \le \min(|R| \deg_S, |S| \deg_R)$. Learned estimators have no proved bound.
- **Join ordering** is NP-hard in general, for left-deep trees with cross products under $C_{\mathrm{out}}$ and without cross products under nested-loop costs. IKKBZ solves tree queries under ASI costs in polynomial time.
- **Dynamic programs** are exact for their search space and cost model. System R keeps one plan per set and interesting order. DPccp enumerates only csg-cmp pairs, $(n^3-n)/6$ for a chain and $(3^n - 2^{n+1} + 1)/2$ for a clique, in $O(nc)$ time for $c$ pairs. DPhyp extends it to hyperedges.
- **Volcano and Cascades** search top down over a memo of groups of equivalent expressions, with sort orders as physical properties and branch-and-bound pruning. For a clique of $n$ relations the memo has $2^n - 1$ groups.
- **Adaptive methods** handle wrong estimates. Parametric optimization stores one plan per region of a parameter, mid-query re-optimization checks a validity range at run time, and eddies route each tuple, with the same result for every policy.
- **Choosing views** under a space budget is NP-hard. The HRU greedy algorithm gets at least $1 - (1 - 1/k)^k > 1 - 1/e$ of the best benefit for $k$ views. Multiple-query optimization is NP-hard too.

## The main methods side by side

| Method | Search space or task | Time | Guarantee |
|---|---|---|---|
| [System R enumeration](/selinger-join-enumeration/) | left-deep orders, with interesting orders | $O(k^2 n 2^n)$ | exact for its space and costs |
| [DPccp](/dpccp/) | bushy trees, no cross products | $O(nc)$ | exact for its space and costs |
| [DPhyp](/dphyp/) | bushy trees on a hypergraph | $O(3^n m^2)$ worst case | exact for its space and costs |
| [IKKBZ](/ikkbz-algorithm/) | left-deep, tree queries | $O(n^2)$ | exact for ASI costs |
| [Greedy operator ordering](/greedy-operator-ordering/) | bushy trees | $O(n^3)$ | none, a heuristic |
| [Volcano](/volcano-optimizer-generator/) | memo of rule-equivalent plans | $O(3^n)$ moves on a clique | exact for its rules and costs |
| [GEE](/guaranteed-error-estimator/) | distinct count from a sample | one pass over $r$ rows | never above $\sqrt{n/r}\,D$ |
| [HRU greedy](/hru-greedy-view-selection/) | $k$ views of a cube lattice of $n$ views | $O(kn^2)$ | $\ge 1 - 1/e$ of the best benefit |

: The main methods of the chapter. "Exact" means exact for the model: a better plan under the true costs may lie outside the search space or be priced wrongly by the estimates. In the System R bound, $k$ is the number of interesting orders; for DPccp, $c$ is the number of csg-cmp pairs; for DPhyp, $m$ is the number of hyperedges.

## How to plan a query

Push filters and unnest subqueries first, with the outer join or antijoin that keeps their meaning. Then estimate the size of each subplan, and keep in mind how wrong the estimate can be: a join of correlated columns or a long chain of joins deserves suspicion. Use exact dynamic programming, DPccp or DPhyp, up to about a dozen or a few more relations, and a greedy or randomized search beyond that, as PostgreSQL does with its genetic search from 12 relations on. When a plan is bad, look first at the estimates, not at the search.
