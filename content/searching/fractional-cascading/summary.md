## What to remember

- **The problem is one key and many lists.** Finding the successor of $x$ in each of $k$ sorted lists of total size $n$ needs $\Omega(\log n + k)$ comparisons, and separate binary searches spend $O(k \log n)$.
- **Copy every second element back.** Each augmented list holds its own catalog and every second element of the next augmented list, with pointers. On a path the total size is at most $2n + k + 1$.
- **The query does one binary search.** After it, each move to the next list follows a down pointer and tests one position before it. The cost is $O(\log n + k)$, which matches the lower bound.
- **The next list may be chosen on the fly.** A query on a catalog graph walks a connected subgraph, and each step needs only the position in the current list. This is what makes the method fit tree walks such as segment trees and range trees, where it removes a factor of $\log n$.
- **The degree matters.** On a graph of degree $d$ the gaps between bridges have $O(d)$ elements and a step costs $O(\log d)$. Ranges on the edges keep the useful degree small even at nodes of high fan-out.
- **Updates cost a $\log \log n$ factor.** Gaps that grow too long are split by copying their middle element, as B-tree nodes split, and the pointers become a union-split-find structure.
- **Planar maps are different.** Replacing the lists by planar subdivisions breaks the method: by the Chazelle–Liu bound, a query time of $O(k + \operatorname{polylog} n)$ needs nearly quadratic space.

## The methods side by side

| Method | Query time | Space | Updates |
|---|---|---|---|
| $k$ separate binary searches | $O(k \log n)$ | $O(n)$ | as for sorted lists |
| One merged list with all successors stored | $O(\log n + k)$ | $O(nk)$ | rebuild |
| [Fractional cascading](/fractional-cascading-bridge/) on a path | $O(\log n + k)$ | $O(n + k)$ | rebuild |
| Fractional cascading on a [catalog graph](/catalog-graph/) of degree $d$ | $O(\log n + k \log d)$ | $O(n)$ | rebuild |
| [Dynamic fractional cascading](/dynamic-fractional-cascading/) | $O(\log n + k \log \log n)$ | $O(n)$ | $O(\log \log n)$ amortized |
| Planar catalogs, [any pointer structure](/fractional-cascading-lower-bound/) with query $O(k + \operatorname{polylog} n)$ | — | $\Omega(n^2/\operatorname{polylog} n)$ | — |

: Multiple list search. The first five rows are for sorted lists, with $n$ the total size and $k$ the number of lists a query visits. The dynamic bound is that of Mehlhorn and Näher. The last row is a lower bound on a pointer machine, not a method.

## When to use it

- Use fractional cascading when one key is searched in many lists, the queries come one at a time, and the lists change rarely. The classic cases are layered range trees, segment trees with sorted lists, and point location by separating chains.
- If every list on the path is a subset of the one before it, as in a merge sort tree, store the successor pointers directly. The copies are already there and no sampling is needed.
- If all the queries are known in advance, sort them and merge them with each list. This costs $O(n + qk)$ for $q$ queries with no extra structure.
- With few lists, or lists of very different lengths, separate binary searches are simpler and often as fast; the gain grows with $k$.
- When the lists change often, weigh the extra $\log \log n$ per list and the more complex code of the dynamic version against a balanced search tree at each node.
- Do not look for a planar version for general maps. The lower bound rules it out; special settings, such as the hive graph for one segment problem, need their own structure.
