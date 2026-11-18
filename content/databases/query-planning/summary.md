## What to remember

- A **query plan** is a tree of operators with an algorithm and an access path for each one. For $n$ relations there are $n!$ left-deep join trees and $(2n-2)!/(n-1)!$ bushy ones. Without cross products the count depends on the query graph: $2^{n-1}$ left-deep trees for a chain, $2(n-1)!$ for a star, $n!$ for a clique.
- The **selectivity** of a predicate is the fraction of tuples or pairs it keeps. The usual formulas assume uniformity, independence and, for joins, containment of value sets; then $|R \bowtie S| \approx |R|\,|S| / \max(V(R, A), V(S, B))$. Without assumptions, only the Fréchet bounds hold for a conjunction.
- **Predicate pushdown** applies a filter as low in the plan as its columns allow. It is always valid for inner joins, valid on the preserved side of an outer join, and not valid in general on the side that is padded with nulls.
- A **cost model** prices a plan from its size estimates. System R used page fetches plus a weight times the calls to the storage system; PostgreSQL uses units in which a sequential page read costs 1. The measure $C_{\mathrm{out}}$, the sum of intermediate result sizes, is the simplest model that still orders plans sensibly.
- **Join ordering** is NP-hard in general, even for left-deep trees. The dynamic program over subsets is exact for its search space and its cost model, in $O(3^n)$ time for bushy trees; the counts of connected subgraph pairs show how much a sparse query graph saves.
- **System R enumeration** keeps, for each set of relations, the cheapest plan for each interesting order. Keeping only the cheapest plan per set can miss the best plan.
- **Histograms** make selectivities less dependent on uniformity. An equi-depth histogram with $B$ buckets bounds the error of a range count by about $2\lceil N/B \rceil$; the V-optimal histogram minimizes the sum of squared errors and is found by a dynamic program in $O(n^2 B)$ time.
- **Cardinality estimates** are the weak link. Errors multiply along a chain of joins, and measurements on real queries show errors of several orders of magnitude; the q-error $\max(e/t, t/e)$ is the usual measure.
- **View selection** under a space budget is NP-hard in general; the greedy algorithm of Harinarayan, Rajaraman and Ullman on the lattice of a cube gets at least $1 - (1 - 1/k)^k > 1 - 1/e$ of the best benefit for $k$ views.

## The main problems side by side

| Problem | What is chosen | Exact method | Hardness or guarantee |
|---|---|---|---|
| [Join ordering](/join-ordering/) | order and shape of the joins | dynamic program over subsets | NP-hard in general |
| [System R enumeration](/selinger-join-enumeration/) | left-deep order, algorithms, orders | DP, $O(k^2 n 2^n)$ | exact for its space and costs |
| [Query optimization](/query-optimization/) | rewrites, joins, access paths | search over equivalent plans | equivalence undecidable in general |
| [Histogram](/histogram/), V-optimal | bucket boundaries | DP, $O(n^2 B)$ time | minimizes squared error |
| [Cardinality estimation](/cardinality-estimation/) | size of each subplan | none in general | errors measured, q-error |
| [View selection](/view-selection/) | views to materialize | search | greedy $\ge 1 - 1/e$ of the best benefit |

: The problems of the chapter. The exact methods are exact only for the model they use: a better plan under the true costs may lie outside the search space or be priced wrongly by the estimates. In the System R bound, $k$ is the number of interesting orders.

## How to plan a query

Push filters first; the rewrite is always worth doing and needs no estimate. Then estimate the size of each subplan, and keep in mind how wrong the estimate can be: a join of correlated columns or a long chain of joins deserves suspicion. Use exact dynamic programming over join orders up to about a dozen relations, and a greedy or randomized search beyond that, as PostgreSQL does with its genetic search from 12 relations on. Avoid cross products except for small tables, as in a star query with two tiny dimension tables. When a plan is bad, look first at the estimates, not at the search.
