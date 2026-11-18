## What to remember

- A **materialized view** stores the result of a query. A query can read it in place of the base tables when the view keeps every column and row the query needs; aggregate views are the most useful because they are much smaller than their input. An average can be rolled up only from stored sums and counts, never from averages.
- **View maintenance** keeps the stored result equal to its query. Recompute when the change is large compared with the tables; otherwise apply a delta. Immediate maintenance updates the view in the same transaction as the base tables; deferred maintenance waits and must compute the delta from a log, or correct for the fact that it sees only the new states.
- **Delta rules** come from the algebra. Selection and projection are linear, so their delta is the operator applied to the delta. Join is bilinear: $\Delta(R \bowtie S) = \Delta R \bowtie S + R \bowtie \Delta S + \Delta R \bowtie \Delta S$ with the old $R$ and $S$. A join of $k$ changed relations has $2^k - 1$ terms.
- Under set semantics a tuple of a view can have several derivations. The **counting algorithm** stores the number of derivations of each tuple and removes the tuple only when the count reaches 0. Insertions into MIN and MAX views are easy; deletions may need the base data or a larger state.
- In a recursive view, facts derive each other in cycles and counts never fall to 0. **DRed** overdeletes every fact with a derivation through a deleted fact, rederives those that still have a derivation from the remaining facts, and inserts the consequences. It is correct for Datalog without negation, but its overdeletion can be far larger than the change: deleting one edge of a cycle overdeletes every path fact.

## The methods side by side

| Method | Views | Handles deletions by | Cost of a change |
|---|---|---|---|
| Recomputation | any | rebuilding the view | a full evaluation |
| [Delta rules](/incremental-view-maintenance/) | select, project, join and union on bags | negative multiplicities | the delta query |
| [Counting](/incremental-view-maintenance/) | nonrecursive, sets | counts of derivations | the delta query |
| [DRed](/dred-algorithm/) | recursive Datalog, no negation | overdelete and rederive | grows with the overdeleted facts |

: The ways to maintain a view in the chapter. The cost of incremental maintenance depends on the delta query and on the indexes it can use, not on the size of the view.

## How to choose

Store a view when many queries read it and the base tables change slowly compared with the reads. Keep counts, sums and counts of rows, not averages, so that every aggregate can be maintained. Maintain incrementally when changes are small, and recompute after a bulk load. For recursive views, use DRed when deletions are rare or local, and expect a deletion near the start of a long chain or on a cycle to cost almost as much as a recomputation.
