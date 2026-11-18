## What to remember

- Every join reads both inputs, so $M + N$ page reads is the floor. A hash join reaches it when its table on the smaller input fits in memory.
- Nested loops work for any condition. Reading the outer relation in blocks of $B - 2$ pages cuts the scans of the inner relation to $\lceil M/(B - 2) \rceil$, and an index on the inner relation replaces them by probes.
- For equality joins of large inputs, the Grace hash join and the sort-merge join both cost $3(M + N)$ with enough memory. The hybrid hash join moves from $3(M + N)$ toward $M + N$ as memory grows.
- A semijoin $R \ltimes S$ never has more tuples than $R$. Sending the join keys, or a Bloom filter of them, to another site often costs far less than sending a relation; a false positive costs data but never loses a match.
- Aggregates with mergeable partial states, such as AVG through (SUM, COUNT), are computed by hashing with one state per group. MEDIAN has no bounded mergeable state.
- In the iterator model, selections and the probe side of a hash join pipeline; sorts, hash aggregation and the build side of a hash join block until their input ends.
- Plans of two-way joins can build intermediate results much larger than the output. For acyclic queries, the semijoin passes of the Yannakakis algorithm prevent this. For any query, the output is at most the AGM bound, and generic join and leapfrog triejoin run within it; on the triangle query, no plan of two-way joins does.
- For top-k queries with a monotone combining function, the threshold algorithm stops no later than Fagin's algorithm and is instance optimal over algorithms without wild guesses. With sorted access only, the no-random-access algorithm is instance optimal with ratio $m$.
- After a presort by a monotone score, no tuple can dominate an earlier one, so the sort-filter skyline outputs each window tuple at once.

## The operators side by side

| Operator | Condition | Page I/O or time | Memory |
|---|---|---|---|
| [Nested-loop join](/nested-loop-join/) | any | $M + pMN$ | 3 pages |
| [Block nested-loop join](/block-nested-loop-join/) | any | $M + \lceil M/(B - 2) \rceil N$ | $B$ pages |
| [Index nested-loop join](/index-nested-loop-join/) | index on the inner key | $M + pMC$ | small |
| [Sort-merge join](/sort-merge-join/) | equality | $3(M + N)$ with enough memory | about $\sqrt{M + N}$ |
| [Hash join](/hash-join/) | equality | $M + N$ | $f M + 2$ pages |
| [Grace hash join](/grace-hash-join/) | equality | $3(M + N)$ | about $\sqrt{f M}$ |
| [Hybrid hash join](/hybrid-hash-join/) | equality | $M + N + 2W$ | between the two above |
| [Bloom join](/bloom-join/) | equality, two sites | $M + 2N$, plus $m$ bits and $\lvert R' \rvert$ tuples sent | $m$ bits |
| [Yannakakis algorithm](/yannakakis-algorithm/) | acyclic query | $O(rn + rz)$ expected time | $O(n + z)$ |
| [Generic join](/generic-join/) | any natural join | within the AGM bound, up to factors of the query size | $O(kn)$ |
| [Threshold algorithm](/threshold-algorithm/) | monotone top-k | $O(m^2 n)$ worst | $O(k + m)$ |
| [Sort-filter skyline](/sort-filter-skyline/) | skyline | $O(n \log n + dn^2)$ worst | window of $w$ tuples |

: The main operators of the chapter. $M$ and $N$ are the pages of the inputs, $p$ the tuples per page of the outer input, $B$ the buffer pages, $f$ the fudge factor of a hash table, $C$ the cost of one probe, $W$ the pages written to disk partitions, $m$ the bits of a Bloom filter or the number of lists, $n$ the input tuples, $r$ the relations, $k$ the attributes or the answers wanted, $z$ the output size and $d$ the dimensions.

## Choosing an operator

For an equality join, use a hash join when the smaller input fits in memory, a hybrid hash join when it is a few times larger, and a Grace hash join or sort-merge join beyond that. Prefer sort-merge when the inputs are sorted already, when sorted output helps, or when keys are heavily skewed. Use an index nested-loop join when the outer input is small and the inner relation has an index on the key, and block nested loops for other conditions.

For three or more relations, check whether the query is acyclic; if it is, the Yannakakis algorithm bounds the work by input plus output. For cyclic queries on skewed data, a worst-case optimal join avoids the large intermediate results of two-way plans. For top-k queries, use the threshold algorithm when random access is cheap, and the no-random-access algorithm otherwise.
