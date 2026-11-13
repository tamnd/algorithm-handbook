1. ◦ Relation $R$ has $M = 1000$ pages and $S$ has $N = 400$ pages, and there are $B = 52$ buffer pages. Count the page I/Os, without writing the output, of the page-at-a-time [nested-loop join](/nested-loop-join/) and of the [block nested-loop join](/block-nested-loop-join/), each with either relation as the outer one. Then decide whether the [Grace hash join](/grace-hash-join/) with $f = 1$ and the combined plan of the [sort-merge join](/sort-merge-join/) run in $3(M + N)$ here, and whether an in-memory [hash join](/hash-join/) is possible.

2. ◦ A table has 1,000,000 rows, 100 to a page, and a B+ tree of height 3 on attribute $A$. A range query on $A$ selects 1% of the rows. Estimate its page I/Os with a [clustered index](/clustered-index/), with an unclustered index, and with a full scan, using the rules of the clustered-index entry. Near what selectivity does the unclustered index stop paying?

3. ◦ An equi-width [histogram](/histogram/) on $\mathit{age}$ over 10,000 rows has the buckets $[0, 20)$ with 1000 rows, $[20, 40)$ with 4000, $[40, 60)$ with 3000 and $[60, 80)$ with 2000. Estimate the number of rows with $30 \le \mathit{age} < 50$, assuming values are spread evenly inside each bucket. Estimate it again for the same predicate combined by AND with a predicate of [selectivity](/selectivity/) $0.1$, and name the assumption you used.

4. ◦ Draw the [conflict graph](/conflict-graph/) of $r_1(x)\, r_2(y)\, w_1(x)\, r_3(x)\, w_2(x)\, w_3(y)$. Is the schedule conflict serializable? Is it view serializable? Remove $r_2(y)$ and give every equivalent serial order of what remains.

5. ◦ Transactions $T_1$, $T_2$, $T_3$ have timestamps 5, 10 and 15, and a smaller timestamp means older. $T_2$ holds an exclusive lock on $x$. First $T_1$ and then $T_3$ ask for a lock on $x$. Say what happens to each of the three transactions under [wait-die and under wound-wait](/wait-die-and-wound-wait/).

6. ◦ Under [snapshot isolation](/snapshot-isolation/), what happens to each of these histories? (a) $r_1(x)\, r_2(x)\, w_1(x)\, w_2(x)\, c_1\, c_2$. (b) $r_1(x)\, r_1(y)\, r_2(x)\, r_2(y)\, w_1(x)\, w_2(y)\, c_1\, c_2$. Which of the two is a serializable outcome, and what does [serializable snapshot isolation](/serializable-snapshot-isolation/) do with the other?

7. ◦ After a crash, the log of an [ARIES](/aries-recovery/) system holds: 10 update $T_1$ on $P_1$; 20 update $T_2$ on $P_2$; 30 begin checkpoint; 40 end checkpoint with transaction table $\{T_1{:}10, T_2{:}20\}$ and dirty page table $\{P_1{:}10\}$; 50 update $T_1$ on $P_3$; 60 commit $T_2$; 70 update $T_3$ on $P_1$; 80 update $T_1$ on $P_2$. Give the transaction table and dirty page table after analysis, the LSN where redo starts, the redo records that are skipped without fetching a page, and the order of the undo pass. How many compensation records does it write?

8. ◦ Relation $R(A, B, C, D, E)$ has the [functional dependencies](/functional-dependency/) $A \to B$, $BC \to D$, $D \to E$, $E \to A$. Find all its keys with the [attribute closure](/attribute-closure-algorithm/). Is $R$ in [3NF](/third-normal-form/)? Is it in [BCNF](/boyce-codd-normal-form/)?

9. ◦ Take $R(A, B) = \{(1,1), (2,1), (3,2)\}$, $S(B, C) = \{(1,5), (2,6), (4,7)\}$ and $T(C, D) = \{(5,8), (7,9)\}$. Run the two semijoin passes of the [Yannakakis algorithm](/yannakakis-algorithm/) on the join tree $R - S - T$. Which tuples are removed, and what is $R \bowtie S \bowtie T$?

10. ◦ Two lists grade six objects, and the score is the sum of the two grades: $a = (1.0, 0.7)$, $b = (0.9, 0.1)$, $c = (0.1, 1.0)$, $d = (0.2, 0.9)$, $e = (0.3, 0.8)$, $f = (0.4, 0.75)$. For $k = 1$, at what depth does the [threshold algorithm](/threshold-algorithm/) stop, and at what depth does [Fagin's algorithm](/fagin-algorithm/) stop? What do both return?

11. ◦ An attribute takes the values $0, \ldots, 9$. How many bitmaps does a [bitmap index](/bitmap-index/) keep with equality encoding, and how many with range encoding? How many bitmaps does each read to answer $3 \le A \le 6$?

12. • A chain query joins $R$ with 1000 tuples, $S$ with 100 and $T$ with 10. The join of $R$ and $S$ has selectivity $1/100$ and that of $S$ and $T$ has selectivity $1/10$, and there is no predicate between $R$ and $T$. Compute $C_{\mathrm{out}}$, the sum of the sizes of the join results, for $(R \bowtie S) \bowtie T$, $(S \bowtie T) \bowtie R$ and $(R \times T) \bowtie S$. Which order does [join ordering](/join-ordering/) under $C_{\mathrm{out}}$ choose?

13. • Let $M = 10{,}000$ and $N = 40{,}000$ pages, with fudge factor $f = 1.2$. Find the smallest $B$ for which the Grace hash join, building on $R$, needs only one partitioning pass, and the smallest $B$ for which the sort-merge join runs its combined plan. Use the conditions of the two entries exactly.

14. • [Hash aggregation](/hash-aggregation/) can combine partial results from several partitions only for some aggregates. Say what partial state is enough to merge COUNT, SUM, MIN, AVG and the variance, and show that no state of bounded size is enough for MEDIAN.

15. • Show that $r_1(x)\, w_2(x)\, r_3(y)\, w_1(y)$ is conflict serializable, but that [two-phase locking](/two-phase-locking/) cannot produce it. Run basic [timestamp ordering](/timestamp-ordering/) on it with timestamps in order of first action. Which [concurrency control](/concurrency-control/) method from the chapter accepts it?

16. • Give a schedule that two-phase locking allows in which the abort of one transaction forces another to abort. Show that [strict two-phase locking](/strict-two-phase-locking/) prevents it.

17. • Decompose the relation of exercise 8 into BCNF with the algorithm of [BCNF decomposition](/bcnf-decomposition/), splitting first on $A \to B$ and then on $D$. Which dependency is lost? Then run [3NF synthesis](/third-normal-form-synthesis/) on the same dependencies, and say which of its schemas is not in BCNF.

18. • For the relation of exercise 8, decide whether each decomposition is a [lossless join decomposition](/lossless-join-decomposition/): (a) $\{A, B\}$ and $\{A, C, D, E\}$; (b) $\{A, B, C\}$ and $\{A, D, E\}$. For the lossy one, give a relation instance that the join of its projections does not reproduce.

19. • Take $R(A, B) = \{(0,0), (1,1)\}$, $S(B, C) = \{(0,1), (1,0)\}$ and $T(C, A) = \{(0,0), (1,1)\}$. Show that no [semijoin](/semijoin/) between two of the relations removes a tuple, yet $R \bowtie S \bowtie T$ is empty. What does this say about semijoin reduction for cyclic queries?

20. • Let $Q_m$ be the Boolean conjunctive query that asks whether a directed graph has a closed walk of length $m$. Using the [Chandra–Merlin theorem](/chandra-merlin-theorem/), decide which of $Q_3 \subseteq Q_6$, $Q_6 \subseteq Q_3$, $Q_3 \subseteq Q_4$ and $Q_4 \subseteq Q_3$ hold.

21. • Run the program $\mathit{path}(x, y) \leftarrow e(x, y)$; $\mathit{path}(x, y) \leftarrow \mathit{path}(x, z), e(z, y)$ on a chain of $n$ nodes. Count the rule instances fired by naive evaluation, which runs until a round adds nothing, and by [semi-naive evaluation](/semi-naive-evaluation/), as closed forms in $n$. Check them against the counts 6 and 20 for $n = 4$ and 190 and 2660 for $n = 20$.

22. • Run the [no-random-access algorithm](/no-random-access-algorithm/) on the data of exercise 10 with $k = 1$. At what depth does it stop, and how do its accesses compare with those of the threshold algorithm?

23. • Show that snapshot isolation and repeatable read are incomparable: give a history that snapshot isolation allows and repeatable read forbids, and one that repeatable read allows and snapshot isolation forbids. Use the phenomena of the [isolation levels](/isolation-levels/) entry.

24. • A [zone map](/zone-map/) keeps the minimum and maximum of each block of 100 rows. A range predicate selects 250 rows. How many blocks are read at most if the table is sorted on the attribute? If the rows are in random order and 50% of the values lie below the range and 49% above it, what is the probability that a given block is skipped?

25. ★ Suppose the Grace hash join splits every partition evenly into $B - 1$ parts, and repartitions until each part of $R$ fits in $B - 2$ pages with fudge factor $f$. Show that $L$ levels of partitioning cost $(2L + 1)(M + N)$ I/Os, and that the least $L$ is the least integer with $fM \le (B - 2)(B - 1)^L$. Find $L$ for $M = 100{,}000$, $B = 11$ and $f = 1$.

26. ★ The [System R enumeration](/selinger-join-enumeration/) keeps, for each set of relations, the cheapest plan for each interesting order. Give three relations and costs for which keeping only the cheapest plan for each set misses the best plan for the whole query.

27. ★ The [AGM bound](/agm-bound/) gives at most $N^{3/2}$ tuples for the triangle query when $R(A, B)$, $S(B, C)$ and $T(C, A)$ each have at most $N$ tuples. Prove the weaker bound $2N^{3/2}$ directly, without fractional covers, by splitting the values of $A$ into heavy ones, with more than $\sqrt{N}$ tuples in $R$, and light ones. Then give an instance with about $N^{3/2}$ triangles, so that the exponent cannot be lowered.

28. ★ Let $R(A, B)$, $S(B, C)$ and $T(C, A)$ each be $\{(0, i) : 0 \le i \le N\} \cup \{(i, 0) : 0 \le i \le N\}$. Count the tuples of the triangle join. Show that every plan made of two-way joins builds an intermediate result with $\Theta(N^2)$ tuples, while [generic join](/generic-join/) does not.

29. ★ The direct serialization graph of a history has an edge for each write–write, write–read and read–write dependency. Prove that if a history allowed by snapshot isolation is not serializable, its graph has a cycle with two consecutive read–write edges, each between transactions that ran at the same time.
