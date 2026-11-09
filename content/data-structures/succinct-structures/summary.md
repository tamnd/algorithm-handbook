## What to remember

- **Space is counted in bits and compared with $\lg N$,** where $N$ is the number of objects in the class. A [succinct](/succinct-data-structures/) structure uses $\lg N + o(\lg N)$ bits; a [compressed](/compressed-data-structure/) one uses space bounded by the entropy of the object at hand.
- **Rank and select are the two basic moves.** $\text{rank}_1(i)$ counts the 1s before position $i$ and $\text{select}_1(j)$ finds the $j$-th 1. On the word RAM both take $O(1)$ time with $n + o(n)$ bits: [Jacobson's rank](/jacobson-rank/) uses superblocks, blocks and a table, and the [rank/select dictionary](/rank-select-dictionary/) adds select by sparse and dense groups.
- **The lower-order term is not small in practice.** For $n = 2^{32}$ Jacobson's parameters give an index of about 63% of $n$, while Vigna's rank9 layout, with word-sized blocks and population count, needs 25%.
- **The extra space has limits.** If the bit vector is kept in plain form, Golynski showed that an index of $\Omega(n \lg \lg n / \lg n)$ bits is needed. In general, [Pătraşcu](/patrascu-succinct-lower-bound/) reached redundancy $n / (w/t)^t$ for query time $O(t)$, and Pătraşcu and Viola showed that $n / w^{O(t)}$ cannot be beaten.
- **Sparse vectors and sorted sets** need only $\lg \binom{n}{m}$ bits, about $m \lg(n/m) + 1.44 m$ when $m$ is much smaller than $n$. The [RRR bit vector](/rrr-bitvector/) reaches this plus $O(n \lg \lg n / \lg n)$; [Elias-Fano](/elias-fano-encoding/) is within about 2 bits per element of it, with no term that grows with $n$.
- **An ordinal tree of $n$ nodes needs $2n - \Theta(\lg n)$ bits.** [LOUDS](/louds-tree/) writes the degrees in level order in $2n + 1$ bits and gives parent and $i$-th child by rank and select, but no subtree size or depth. [Balanced parentheses](/balanced-parentheses-representation/) give every operation, including subtree size, depth and lowest common ancestor, through matching and the excess. [DFUDS](/dfuds/) gives the $i$-th child directly together with preorder and subtree size.
- **A string over $\sigma$ symbols** becomes $\lceil \lg \sigma \rceil$ levels of bit vectors in the [wavelet tree](/wavelet-tree/), which answers access, rank, select and range quantiles in $O(\lg \sigma)$ time. With RRR bit vectors its space drops to $n H_0(S) + o(n \lg \sigma)$. The [wavelet matrix](/wavelet-matrix/) removes the $O(\sigma \lg n)$ bits of the tree shape.
- **Updates cost a logarithm.** The [dynamic bit vector](/dynamic-bit-vector/) takes $O(\lg n)$ time per operation with chunks of $\Theta(\lg^2 n)$ bits in a balanced tree, and the Fredman-Saks bound shows that $\Theta(\lg n / \lg \lg n)$ is the best possible.

## Bit vectors side by side

| Structure | Space in bits | rank | select |
|---|---|---|---|
| Plain [bit vector](/bit-vector/) | $n + O(w)$ | $O(n/w + 1)$ | $O(n/w + w)$ |
| [Jacobson's rank](/jacobson-rank/) | $n + O(n \lg \lg n / \lg n)$ | $O(1)$ | $O(\lg n)$ |
| [Rank/select dictionary](/rank-select-dictionary/), Clark's form | $n + O(n / \lg \lg n)$ | $O(1)$ | $O(1)$ |
| [RRR bit vector](/rrr-bitvector/) | $\lg \binom{n}{m} + O(n \lg \lg n / \lg n)$ | $O(1)$ | $O(\lg n)$, or $O(1)$ with an extra index |
| [SD-array](/sd-array/) | $m \lceil \lg(n/m) \rceil + 2m + o(m)$ | $O(1 + \lg(n/m))$ | $O(1)$ for $\text{select}_1$ |
| [Dynamic bit vector](/dynamic-bit-vector/) | $n + O(n / \lg n)$ | $O(\lg n)$ | $O(\lg n)$ |

: Here $n$ is the length of the vector, $m$ the number of 1s and $w$ the word size. All times are worst case on the word RAM; the dynamic bit vector also inserts and deletes bits in $O(\lg n)$ time.

## Choosing a structure

- For a dense bit vector that must answer rank and select fast, keep it in plain form with a rank/select index.
- For a vector with few 1s, or few 0s, use the RRR bit vector. For a sorted list of integers, such as a posting list, or a very sparse vector, use Elias-Fano encoding or the SD-array.
- For a static trie or any tree navigated mostly between parents and children, use LOUDS. When subtree sizes, depths or lowest common ancestors are needed, use balanced parentheses with a [range min-max tree](/range-min-max-tree/), or DFUDS when the $i$-th child must also be fast.
- For rank and select over a string, use a wavelet tree; for a large alphabet, such as an array of integers, use the wavelet matrix.
- For a bit vector that changes, use a dynamic bit vector, and accept the logarithmic cost of each query.
- For a permutation whose inverse is needed, use the [succinct permutation](/succinct-permutation/) with spacing $t$: $n \lg n + O((n/t) \lg n + n)$ bits and $O(t)$ time for the inverse.
