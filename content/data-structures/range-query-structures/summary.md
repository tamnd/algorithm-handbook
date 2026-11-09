## What to remember

- The laws of the operation decide the structure. Associativity alone is enough for the [segment tree](/segment-tree/) and the [disjoint sparse table](/disjoint-sparse-table/). An **idempotent** operation, such as the minimum or the gcd, lets two overlapping ranges cover a query, which gives the $O(1)$ query of the [sparse table](/sparse-table/). An **inverse** turns a range into two prefixes, $F(l, r) = P(l)^{-1} \oplus P(r)$, which is what the [Fenwick tree](/fenwick-tree/) uses.
- The **Fenwick tree** stores in cell $i$ the sum of $(i - \mathrm{lowbit}(i), i]$. PREFIX and ADD each take at most $\lfloor \lg n \rfloor + 1$ steps, with $n$ words of space and a $\Theta(n)$ build.
- The **segment tree** has $2n - 1$ nodes and height $\lceil \lg n \rceil$. A query uses at most $4 \lceil \lg n \rceil$ applications of $\oplus$ and a point update at most $\lceil \lg n \rceil$. In the cell-probe model, the update or the query of dynamic partial sums must take $\Omega(\log n)$ time, so both trees are optimal up to a constant factor.
- **Lazy propagation** puts a pending update on the $O(\log n)$ nodes that cover a range. It works when the updates form a monoid of maps that distribute over $\oplus$.
- The **sparse table** stores the answers for all ranges of length $2^k$, $(K + 1)(n + 1) - 2^{K+1} + 1$ cells with $K = \lfloor \lg n \rfloor$, and answers an idempotent query with two of them. None of the static tables supports updates.
- **Square-root decomposition** answers any query with at most $2(b - 1) + n/b$ applications of $\oplus$ for blocks of $b$ items, so $O(\sqrt n)$. [Mo's algorithm](/mo-algorithm/) sorts $q$ offline queries by $(\lfloor l / B \rfloor, r)$ and moves a window $O(n \sqrt q)$ steps in all.
- Some queries do not split into halves. The number of distinct values of $A[l \ldots r]$ is the number of $i$ in the range with $\mathit{prev}[i] < l$, which a sweep with a Fenwick tree answers in $O((n + q) \log n)$ time. The mode of a range has no known linear-space method much faster than about $\sqrt n$ per query.
- The range minimum reduces to the lowest common ancestor in the [Cartesian tree](/cartesian-tree/), and back to a minimum over an Euler tour of $2n - 1$ depths that differ by $\pm 1$. Small blocks then give $O(n)$ preprocessing and $O(1)$ queries, and the [Fischer-Heun](/fischer-heun-rmq/) structure needs only $2n + o(n)$ bits, close to the lower bound of $\lg C_n = 2n - \Theta(\log n)$ bits.

## The main structures side by side

| Structure | Operation | Build | Query | Point update | Space |
|---|---|---|---|---|---|
| [Square-root decomposition](/square-root-decomposition/) | monoid | $O(n)$ | $O(\sqrt n)$ | $O(\sqrt n)$ | $n/b$ summaries |
| [Sparse table](/sparse-table/) | idempotent | $\Theta(n \log n)$ | $O(1)$ | none | $(K+1)(n+1) - 2^{K+1} + 1$ cells |
| [Disjoint sparse table](/disjoint-sparse-table/) | associative | $O(n \log n)$ | $O(1)$ | none | $n \lceil \lg n \rceil$ entries |
| [Sqrt tree](/sqrt-tree/) | associative | $O(n \log \log n)$ | 2 applications of $\oplus$ | $O(\sqrt n)$ | $O(n \log \log n)$ |
| [Fenwick tree](/fenwick-tree/) | group | $\Theta(n)$ | $\Theta(\log n)$ | $\Theta(\log n)$ | $n$ words |
| [Segment tree](/segment-tree/) | monoid | $\Theta(n)$ | $O(\log n)$ | $\Theta(\log n)$ | $2n - 1$ nodes in $4n$ cells |
| [Bender-Farach-Colton](/bender-farach-colton-rmq/) | minimum | $O(n)$ | $O(1)$ | none | $\Theta(n)$ words |
| [Fischer-Heun](/fischer-heun-rmq/) | minimum | $O(n)$ | $O(1)$ | none | $2n + o(n)$ bits |

: Worst-case times for an array of $n$ items. With lazy propagation the segment tree also takes range updates in $O(\log n)$ time. "None" means the structure must be rebuilt after a change.

## Choosing a structure

- For a static array and an invertible operation, use prefix sums from Volume 6. For a static minimum, maximum or gcd, use a sparse table.
- For sums with point updates, use a Fenwick tree. Use a segment tree when the operation has no inverse, when a node must keep more than one number, or when updates cover ranges.
- For a static product that is neither invertible nor idempotent, such as a matrix product, use a disjoint sparse table.
- When all queries are known in advance, sort them first. A sweep often reduces the problem to point updates and prefix queries, and Mo's algorithm handles any query whose answer is cheap to repair when the window gains or loses one item.
- A Chtholly tree is short to write for range assignment on random data, but an adversary can make each operation cost $\Theta(n)$.
