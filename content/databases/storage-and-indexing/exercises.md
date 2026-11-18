1. ◦ A table has 1,000,000 rows, 100 to a page, and a B+ tree of height 3 on attribute $A$. A range query on $A$ selects 1% of the rows. Estimate its page I/Os with a [clustered index](/clustered-index/), with an unclustered index, and with a full scan, using the rules $h + k/p$ and $h + k$ of the clustered-index entry. Near what selectivity does the unclustered index stop paying?

2. ◦ Table $T(a, b, c)$ has a [covering index](/covering-index/) candidate with key $(a, b)$. Which of these queries does it cover, and for which can it use its key as a search prefix? (a) `SELECT b FROM T WHERE a = 5`; (b) `SELECT a FROM T WHERE b = 3`; (c) `SELECT c FROM T WHERE a = 5`; (d) `SELECT COUNT(*) FROM T WHERE a > 10`.

3. ◦ An attribute takes the values $0, \ldots, 9$. How many bitmaps does a [bitmap index](/bitmap-index/) keep with equality encoding, and how many with range encoding? How many bitmaps does each read to answer $3 \le A \le 6$? For the column $A = [1, 3, 0, 3, 2, 1]$, write $E^{3}$, $R^{0}$ and $R^{2}$ as bit strings for rows 0 to 5, and compute $1 \le A \le 2$ with each encoding.

4. ◦ A column is stored in four blocks of four rows: $3, 8, 1, 9$; $12, 15, 11, 14$; $20, 17, 22, 18$; $5, 30, 26, 27$. Write its [zone map](/zone-map/). Which blocks does a scan read for $10 \le A \le 16$, and for $A = 25$? What do the two queries return?

5. ◦ [Bulk load](/bulk-loading-b-tree/) the 30 keys $2, 4, 6, \ldots, 60$ into a B+ tree of order $d = 2$ (2 to 4 keys per node) with fill factor $f = 3/4$. Give the leaves, the internal nodes with their separators, the height and the number of nodes.

6. ◦ A [learned index](/learned-index/) on the sorted keys $3, 5, 8, 13, 21, 34, 55, 89$ (positions 0 to 7) uses the single model $f(k) = k/12$ and predicts the position $\lfloor f(k) \rfloor$. Compute the error bounds $e_{lo}$ and $e_{hi}$. Which positions does a lookup of 34 search, and which does a lookup of 40 search?

7. • A zone map keeps the minimum and maximum of each block of 100 rows of a table of 100,000 rows. A range predicate selects 250 rows. How many blocks does a scan read at most if the table is sorted on the attribute? If the values are drawn independently and the predicate selects the 250 smallest values, what is the probability that a given block is skipped, and how many of the 1000 blocks are skipped on average?

8. • A table has 2,000,000 rows, 50 to a page, in an order unrelated to column $a$. A query reads $b$ for the 10,000 rows with $a$ in a range. Compare the page reads of an index-only plan on an index with key $(a, b)$, height 3 and 250 entries per leaf, with a plan on an index on $a$ alone that sorts the record ids and reads each distinct table page once. Use Yao's formula from the clustered-index entry for the second plan, and compare it with the approximation $m(1 - e^{-k/m})$ for $m$ pages.

9. • Under the single-index model of [index selection](/index-selection/), four queries each cost 10 with no index. Index $I_1$ makes queries 1 and 2 cost 0 and queries 3 and 4 cost 5; $I_2$ makes queries 1 and 3 cost 0; $I_3$ makes queries 2 and 4 cost 0. All sizes are 1, there is no maintenance cost, and at most two indexes may be built. Run greedy by benefit, find the optimum, and check the ratio against the guarantee for submodular benefits.

10. • A bit-sliced index stores one bitmap per binary digit of the value. For the column $A = [5, 3, 6, 2]$, write the slices $B_0$, $B_1$ and $B_2$, and compute the sum of $A$ over the rows $F = \{0, 2, 3\}$ from popcounts of $B_i$ AND $F$ only.

11. • Relation $R$ has the join keys $[5, 7, 5, 9, 7]$ with rids 0 to 4, and $S$ has $[7, 5, 8, 7]$ with rids 0 to 3. Build the [join index](/join-index/) of $R \bowtie S$. With two tuples per page in each relation and four pairs per page, how many page I/Os does the join through the index cost, using the bound of the entry?

12. • The column $9, 2, 14, 5, 11, 7, 1, 12, 4, 10$ starts uncracked. Run [database cracking](/database-cracking/) for the queries $5 \le A < 10$, then $3 \le A < 7$, then $8 \le A < 13$. For each, give the pieces it cracks, the number of entries it touches, the pivots of the cracker index after it, and its answer.

13. ★ In the single-index model with no maintenance costs, the benefit of a set $S$ of indexes is $B(S) = \sum_q w_q \max\big(0, \max_{i \in S}(c_q - c_{q,i})\big)$. Prove that $B$ is monotone and submodular: $B(S \cup \{i\}) - B(S) \ge B(T \cup \{i\}) - B(T)$ for $S \subseteq T$.

14. ★ For the knapsack case of index selection, where the benefits of the indexes add up, show that the better of the greedy configuration by benefit per unit of size and the best single index that fits has at least half of the optimal benefit.

15. ★ The PGM-index fits a piecewise linear function such that every key's predicted position is within $\varepsilon$ of its true position. Show that $\lceil n / (2\varepsilon + 1) \rceil$ segments always suffice for $n$ distinct sorted keys and an integer $\varepsilon \ge 0$, even with segments of slope zero.
