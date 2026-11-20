## What to remember

- Every join reads both inputs, so $M + N$ page reads is the floor. A hash join reaches it when its table on the smaller input fits in memory.
- For equality joins of large inputs, the Grace hash join and the sort-merge join both cost $3(M + N)$ with enough memory, and the hybrid hash join moves from $3(M + N)$ toward $M + N$ as memory grows. The radix hash join partitions in memory with a fan-out per pass that suits the cache and the TLB.
- A semijoin $R \ltimes S$ never has more tuples than $R$. Sending a Bloom filter of the join keys to another site costs little; a false positive costs data but never loses a match.
- Aggregates with mergeable partial states, such as AVG through (SUM, COUNT), are computed by hashing, or by sorting with equal keys combined inside the runs. A data cube on $D$ attributes has $2^D$ group-bys; BUC skips every block with fewer than minsup rows, which is safe because COUNT only shrinks as groups get finer.
- Sorts, hash aggregation and the build side of a hash join are pipeline breakers; selections, projections and the probe side pipeline. An exchange operator parallelizes a plan by repartitioning streams. Compiled, vectorized and morsel-driven engines change how a pipeline runs, not what it computes.
- Plans of two-way joins can build intermediate results much larger than the output; for acyclic queries, the Yannakakis semijoin passes prevent this. Generic join and leapfrog triejoin run within the AGM bound for any query; on the triangle query no two-way plan does. A factorized result has size $O(n^{s})$ with $s \le \rho^*$.
- For top-k queries with a monotone combining function, the threshold algorithm stops no later than Fagin's algorithm and is instance optimal over algorithms without wild guesses; the no-random-access algorithm needs sorted access only. A rank join outputs a pair once its score reaches the corner bound.
- After a presort by a monotone score, the sort-filter skyline outputs each window tuple at once. BBS reads exactly the R-tree nodes whose lower corner no point dominates, which is optimal for algorithms that see only the rectangles.

## The operators side by side

| Operator | Condition | Page I/O or time | Memory |
|---|---|---|---|
| [Block nested-loop join](/block-nested-loop-join/) | any | $M + \lceil M/(B - 2) \rceil N$ | $B$ pages |
| [Index nested-loop join](/index-nested-loop-join/) | index on the inner key | $M + pMC$ | small |
| [Sort-merge join](/sort-merge-join/) | equality | $3(M + N)$ | about $\sqrt{M + N}$ |
| [Hash join](/hash-join/) | equality | $M + N$ | $f M + 2$ pages |
| [Grace hash join](/grace-hash-join/) | equality | $3(M + N)$ | about $\sqrt{f M}$ |
| [Hybrid hash join](/hybrid-hash-join/) | equality | $M + N + 2W$ | between the two above |
| [Radix hash join](/radix-hash-join/) | equality, in memory | $O(P(n + m) + 2^b + T)$ expected time | $O(n + m + 2^b)$ |
| [Sort-based aggregation](/sort-based-aggregation/) | grouping | $2NP - N$ | $B$ pages |
| [Yannakakis algorithm](/yannakakis-algorithm/) | acyclic query | $O(rn + rz)$ expected time | $O(n + z)$ |
| [Threshold algorithm](/threshold-algorithm/) | monotone top-k | $O(m^2 n)$ worst | $O(k + m)$ |
| [Sort-filter skyline](/sort-filter-skyline/) | skyline | $O(n \log n + dn^2)$ worst | window of $w$ tuples |
| [Branch-and-bound skyline](/branch-and-bound-skyline/) | skyline, R-tree | $r$ node reads | heap of at most $rb + 1$ entries |

: The main operators of the chapter. $M$ and $N$ are input pages, $p$ tuples per outer page, $B$ buffer pages, $f$ the hash table fudge factor, $C$ one probe, $W$ pages written to partitions, $P$ passes, $b$ radix bits or node capacity, $n$, $m$ and $T$ input and output tuples, $r$ relations or nodes read, $k$ answers, $z$ output size, $d$ dimensions.

## Choosing an operator

For an equality join, use a hash join when the smaller input fits in memory, a hybrid hash join when it is a few times larger, and Grace or sort-merge beyond that. Prefer sort-merge when the inputs are sorted already or sorted output helps. Use an index nested-loop join for a small outer input and an indexed inner key.

For acyclic queries, the Yannakakis algorithm bounds the work by input plus output; for cyclic queries on skewed data, a worst-case optimal join avoids large intermediate results. For top-k queries, use the threshold algorithm when random access is cheap and the no-random-access algorithm otherwise; for skylines, use BBS when an R-tree exists and the sort-filter skyline otherwise. When an estimate is enough, online aggregation and the ripple join give unbiased running estimates of SUM and COUNT.
