## What to remember

- **Pages and frames come first.** A slotted page names a record by (page, slot), so compaction moves bytes without changing record ids. LRU fails on a loop over one page more than the buffer pool holds; DBMIN sizes the frames of each file by its reference pattern instead. The five-minute rule $T^* = (K/A)(D/R)$ keeps a page in memory if it is used at least once every $T^*$ seconds.
- **The layout decides what a scan reads.** The N-ary model reads every page of the table for any column; the decomposition model reads only the columns asked for. PAX has the I/O of the first and the cache behavior of the second. An ordered dictionary turns a range on strings into a range of codes, and frame-of-reference stores each block as small offsets from its minimum.
- **Page reads are the cost of an index.** For $k$ matches with $p$ rows per page and a tree of height $h$, a clustered index reads about $h + k/p$ pages and an unclustered one about $h + k$. A table has one physical order; a covering index gives a second cheap path, and a partial index serves queries whose predicate implies its own.
- **B+ trees bend without breaking.** Bulk loading writes each node once after a sort. The prefix B-tree stores the shortest separator that splits two leaves, the GiST reduces a search tree to six key methods, and the Bw-tree replaces latches by delta records installed with one compare-and-swap.
- **Bitmaps trade space for word-parallel logic.** Equality encoding stores $cn$ bits, range encoding $(c - 1)n$ and reads at most two bitmaps for a range. WAH works on 31-bit groups and combines bitmaps of $p$ and $q$ words in $O(p + q)$ without decompressing.
- **Adaptive and learned indexes move work.** Cracking and adaptive merging build the index as a side effect of queries; adaptive merging pays more at first and converges in fewer queries. The PGM-index guarantees an error of at most $\varepsilon$ with at most $\lceil n/(2\varepsilon + 1) \rceil$ segments; ALEX leaves gaps for inserts. Their speed is measured.
- **Indexes must be chosen together.** Index selection under a space budget is NP-hard by a reduction from knapsack. With unit sizes and no maintenance costs the benefit is submodular and greedy reaches a $1 - 1/e$ fraction of the optimum. What-if analysis supplies the costs without building anything.

## The structures side by side

| Structure | Answers | Query cost | Space | Updates |
|---|---|---|---|---|
| [Clustered index](/clustered-index/) | ranges, equality | about $h + k/p$ I/Os | the tree | keep the file in order |
| [Covering index](/covering-index/) | queries on its columns | about $h - 1 + k/e$ I/Os, no table reads | grows with included columns | every covered column |
| [Partial index](/partial-index/) | queries implying its predicate | as the full index | rows satisfying the predicate | only those rows |
| [Bitmap index](/bitmap-index/), range encoding | ranges on few values | $O(n/w)$, at most two bitmaps | $(c - 1) n$ bits | up to $c - 1$ bits per row |
| [WAH bitmap](/word-aligned-hybrid-compression/) | the same, compressed | $O(p + q)$ for inputs of $p$ and $q$ words | at most $2h + 1$ words for $h$ ones | append at the end |
| [Zone map](/zone-map/) | skipping blocks in a scan | $O(n/b)$ bounds plus blocks read | $\Theta(n/b)$ | widen one bound |
| [Join index](/join-index/) | a stored join | $\lceil P/q \rceil$ plus pages touched | $\Theta(P)$ pairs | $O(d)$ pairs per tuple |
| [PGM-index](/pgm-index/) | lookups in a sorted array | $O(\log m + \log \varepsilon)$ | at most $\lceil n/(2\varepsilon+1) \rceil$ segments | rebuild or merge levels |

: Index structures of the chapter. Here $n$ is the number of rows, $k$ the matches, $p$ rows per table page, $e$ entries per index leaf, $c$ the number of values, $w$ the word size, $b$ the rows per block, $P$ the joining pairs with $q$ per page, $d$ the partners of one tuple, $m$ the number of segments and $\varepsilon$ the error bound.

## Choosing a structure

Store tables for transactions as whole records and tables for analysis by column, compressed. Cluster the table on the column most used for ranges, and add covering indexes for frequent queries on other columns when space and updates allow; a partial index fits a predicate that most queries repeat. For a column with few values in combined selections, use a bitmap index. Keep zone maps on any column that the load order already sorts. Treat an adviser's numbers as estimates from the cost model.
