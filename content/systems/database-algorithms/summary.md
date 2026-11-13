## What to remember

- Join costs count page I/Os, without writing the output. The [block nested-loop join](/block-nested-loop-join/) costs exactly $M + \lceil M/(B-2) \rceil N$ and handles any join condition. The [Grace hash join](/grace-hash-join/) and the combined plan of the [sort-merge join](/sort-merge-join/) cost $3(M + N)$, but only when memory is large enough: about $\sqrt{fM}$ pages for Grace and about $\sqrt{M + N}$ for sort-merge.
- The [hybrid hash join](/hybrid-hash-join/) costs $M + N + 2W$, with $W$ the pages written to disk, and $M + N$ when the smaller input fits in memory. With little memory it can cost more than Grace, and its cost is not monotone in $B$.
- Hash methods have expected CPU bounds, not worst-case ones; a join on one key value does work proportional to the product of the input sizes, and a skewed Grace partition must be split again or joined by nested loops.
- [Cardinality estimates](/cardinality-estimation/) assume uniform values inside each bucket of a [histogram](/histogram/) and independent predicates, and their errors grow with each join. The [System R enumeration](/selinger-join-enumeration/) is exact only for left-deep plans and its own estimates; the best join order is NP-hard to find in general.
- On an acyclic query, the [Yannakakis algorithm](/yannakakis-algorithm/) of $r$ relations removes every dangling tuple with $2(r-1)$ semijoins and evaluates a full join in time linear in input plus output. The [AGM bound](/agm-bound/) caps a join's output at $N^{\rho^*}$, which is $N^{3/2}$ for the triangle. [Generic join](/generic-join/) runs within it; plans of two-way joins can be polynomially slower.
- A schedule is conflict serializable if and only if its [conflict graph](/conflict-graph/) is acyclic. [Two-phase locking](/two-phase-locking/) allows only such schedules, serialized in lock-point order. [Timestamp ordering](/timestamp-ordering/) serializes in timestamp order. [Snapshot isolation](/snapshot-isolation/) is not serializable: it allows write skew. Its [serializable form](/serializable-snapshot-isolation/) aborts on two consecutive read–write edges.
- [Write-ahead logging](/write-ahead-logging/) makes steal and no-force safe. [ARIES](/aries-recovery/) repeats history from the smallest recLSN and then undoes the losers with compensation records that are never undone. Under strict locking, restart is correct after any number of crashes, even during restart.
- The [attribute closure](/attribute-closure-algorithm/) decides in linear time whether a functional dependency is implied. [BCNF decomposition](/bcnf-decomposition/) is always lossless but can lose dependencies. [3NF synthesis](/third-normal-form-synthesis/) keeps them all and stays lossless. Conjunctive-query containment is an NP-complete homomorphism test.

| Method | Page I/Os | Holds when | Join condition | Kind of bound |
|---|---|---|---|---|
| [Block nested loop](/block-nested-loop-join/) | $M + \lceil M/(B-2) \rceil N$ | always | any | exact |
| [Index nested loop](/index-nested-loop-join/) | $M + p_R M C$ | index on $S$ | what the index supports | average $C$ |
| [Sort-merge, combined plan](/sort-merge-join/) | $3(M + N)$ | $\lceil M/B \rceil + \lceil N/B \rceil \le B - 2$ | equality | $M + MN$ merge on one heavy key |
| [Hash join in memory](/hash-join/) | $M + N$ | $fM \le B - 2$ | equality | expected CPU time |
| [Grace hash join](/grace-hash-join/) | $3(M + N)$ | $fM/(B-1) \le B - 2$ | equality | needs even partitions |
| [Hybrid hash join](/hybrid-hash-join/) | $M + N + 2W$ | each disk partition fits | equality | not monotone in $B$ |
| [Bloom join](/bloom-join/) | $M + 2N$ | reduced $R$ fits | equality | exact |

: Two-way join methods in the page model of Ramakrishnan and Gehrke. $R$, the smaller input, has $M$ pages with $p_R$ tuples per page, $S$ has $N$ pages, $B$ is the number of buffer pages, $f$ is the fudge factor of a hash table, and $C$ is the cost of one index probe. Every formula assumes its condition.

## Choosing a method

To join two large tables on equal keys, use a hash join: in memory if the smaller one fits, hybrid if it is a little larger, Grace if it is much larger. Use sort-merge when inputs or output are sorted, and index nested loops when the outer side is small and the inner side is indexed on the key. Keep the block nested-loop join for conditions that are not equalities. For many relations, reduce an acyclic query by semijoins first, and use a worst-case optimal join for cyclic queries whose intermediate results blow up, such as triangles in a graph. Treat every cost the optimizer prints as an estimate.

For transactions, strict two-phase locking with deadlock handling is the safe default. Snapshot isolation never blocks readers but allows write skew, so use its serializable form when constraints span several rows. Pair either with write-ahead logging, steal and no-force, fuzzy checkpoints and group commit, as ARIES does. In schema design, aim for BCNF, and use 3NF synthesis when BCNF would lose a dependency that updates must check.
