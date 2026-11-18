## What to remember

- **Page reads are the cost.** For a range with $k$ matches, $p$ rows per page and a tree of height $h$, a clustered index reads about $h + k/p$ pages and an unclustered one about $h + k$. The unclustered index loses to a full scan once $k$ passes about $n/p$, which is a selectivity near $1/p$. Sorting the record ids first helps, but the distinct pages still follow Yao's formula, far above $k/p$.
- **A table has one physical order.** Only one index can be clustered. A covering index gives a second cheap access path by holding the needed columns in its leaves; included columns sit in the leaves only and do not lower the fanout.
- **Bitmaps trade space for word-parallel logic.** With $c$ values and $n$ rows, equality encoding stores $c n$ bits and range encoding $(c - 1) n$; a range predicate reads up to $c$ bitmaps with the first and at most two with the second, each in $O(n/w)$ word operations. Run-length codes such as WAH work directly on the compressed form.
- **Zone maps work only on ordered data.** Two values per block cost almost nothing, and on sorted data a scan reads only the blocks with matches, plus at most one. On random data a block of $b$ rows is skipped with probability $p_{<}^{\,b} + p_{>}^{\,b}$, which is near zero unless the predicate sits at one end of the range.
- **Bulk loading costs a sort.** Sorting the entries and packing them into nodes writes each node once and takes $O(n \log_m n)$ I/Os, against $\Theta(N \log_B N)$ for $N$ separate insertions. It also fixes the fill factor, while random insertions give about 69% full leaves and sorted insertions 50%.
- **Adaptive and learned indexes move work.** Cracking pays $\Theta(n)$ for the first query and less for each later one, as a quicksort spread over the workload. A learned index stores $\Theta(m)$ numbers instead of tree nodes and searches only the window its error bounds allow; how small that window is depends on how well the model fits the data.
- **Indexes must be chosen together.** Index selection under a space budget is NP-hard, already without interactions, by a reduction from knapsack. Greedy by benefit per unit of space can miss the optimum; with unit sizes and no maintenance costs, the benefit is submodular and greedy reaches a $1 - 1/e$ fraction of it.

## The structures side by side

| Structure | Answers | Query cost | Space | Updates |
|---|---|---|---|---|
| [Clustered index](/clustered-index/) | ranges, equality | about $h + k/p$ I/Os | the tree | keep the file in order |
| [Covering index](/covering-index/) | queries on its columns | about $h - 1 + k/e$ I/Os, no table reads | grows with included columns | every covered column |
| [Bitmap index](/bitmap-index/), range encoding | ranges on few values | $O(n/w)$, at most two bitmaps | $(c - 1) n$ bits | up to $c - 1$ bits per row |
| [Zone map](/zone-map/) | skipping blocks in a scan | $O(n/b)$ bounds plus blocks read | $\Theta(n/b)$ | widen one bound |
| [Join index](/join-index/) | a stored join | $\lceil P/q \rceil$ plus pages touched | $\Theta(P)$ pairs | $O(d)$ pairs per tuple |
| [Learned index](/learned-index/) | lookups in a sorted array | $O(1)$ plus $O(\log e)$ | $\Theta(m)$ numbers | rebuild |
| [Cracking](/database-cracking/) | ranges | the pieces cracked, $\Theta(n)$ worst | a copy of the column | merges pending changes |

: The structures of the chapter. Here $n$ is the number of rows, $k$ the matches, $p$ rows per table page, $e$ entries per index leaf in the covering row and the largest error window in the learned row, $c$ the number of values, $w$ the word size, $b$ the rows per block, $P$ the joining pairs with $q$ per page, $d$ the partners of one tuple and $m$ the number of models.

## Choosing a structure

Cluster the table on the column that is most often used for ranges, and add covering indexes for the frequent queries on other columns when the space and the update load allow. For a column with few values that appears in many combined selections, use a bitmap index, with range encoding if the predicates are ranges. Keep zone maps on any column that the load order already sorts, such as the insertion time; they cost almost nothing. Build a large index by bulk loading, not by insertion. Use a join index only for joins that are run often on data that changes rarely. Let an index adviser propose a set, and treat its estimates as estimates: they come from the cost model and inherit its errors.
