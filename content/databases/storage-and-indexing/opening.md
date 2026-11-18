A table of a million orders fills ten thousand disk pages. A query for one day's orders can read all ten thousand, or it can read the hundred or so that hold that day, if the rows are stored in date order and an index says where the day begins. The difference between the two is the subject of this chapter: how the rows are placed and which auxiliary structures the system keeps, so that each query reads as little as it can.

The cost here is counted in page reads, as in the [external memory model](/external-memory-model/), and the main tool is the [B+ tree](/b-plus-tree/) of Volume 3. The entries of the chapter are about how a database uses such structures: the order of the file under an index, the columns stored in the index, the summaries that let a scan skip data, and the choice of which indexes to build at all. The same table can be cheap or ruinous to query depending on these choices, and none of them is free, since every index must be updated with the table.

## What the chapter covers

1. **Access paths and their order.** A [clustered index](/clustered-index/) reads about $h + k/p$ pages for $k$ matches with $p$ rows per page, against about $h + k$ for an unclustered one. A [covering index](/covering-index/) answers a query from its own leaves. [Bulk loading](/bulk-loading-b-tree/) builds a B+ tree from sorted entries and writes each node once.
2. **Indexes for analytic scans.** A [bitmap index](/bitmap-index/) keeps one bit vector per value and answers selections with bitwise operations. A [zone map](/zone-map/) keeps the minimum and maximum of each block. A [join index](/join-index/) stores the pairs of row ids that join.
3. **Adaptive and learned indexes.** [Database cracking](/database-cracking/) partitions a copy of a column a little more with each range query. A [learned index](/learned-index/) predicts the position of a key with a model and corrects the guess with a short search.
4. **Choosing indexes.** [Index selection](/index-selection/) picks indexes for a workload under a space budget; it is NP-hard, and greedy search over optimizer estimates is the practice.

## A first reading

Read the clustered index, the covering index, the bitmap index and the zone map first, in that order. Together they explain most of the plans an optimizer chooses for selections. Then read index selection, which shows why indexes must be chosen together and not one at a time. Bulk loading and the join index are short and can follow. Database cracking and learned indexes are research topics and can wait until the rest is familiar.

## Before you start

You need the [B+ tree](/b-plus-tree/) and the [bit vector](/bit-vector/) from Volume 3, and [bitwise operations](/bitwise-operations/) from Volume 2. Bulk loading starts with an [external merge sort](/external-merge-sort/) from Volume 4, and cracking reuses the [partition step](/partition-around-pivot/) of [quicksort](/quicksort/). A learned index uses [binary search](/binary-search/) from Volume 5 and [least squares](/ordinary-least-squares/) from Volume 25. Index selection reduces from the [knapsack problem](/knapsack-problem/) of Volume 15 and is [NP-hard](/np-hard/) in the sense of Volume 39; its costs come from the [cost model](/cost-model/) of the query planning chapter. The join index assumes the [relational join](/relational-join/) of the query processing chapter.

The chapter is partly written. Entries still to come cover the buffer pool and its replacement policies, page and file layouts (heap files, slotted pages, row, column and hybrid storage), column compression, further index structures (dense and sparse, partial and prefix indexes, latch-free and generalized search trees, newer learned indexes), adaptive merging, late materialization, the five-minute rule, and the what-if analysis behind index advisers. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
