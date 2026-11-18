1. ◦ Relation $R$ has $M = 1000$ pages and $S$ has $N = 400$ pages, and there are $B = 52$ buffer pages. Count the page I/Os, without writing the output, of the page-at-a-time [nested-loop join](/nested-loop-join/) and of the [block nested-loop join](/block-nested-loop-join/), each with either relation as the outer one. Then decide whether the [Grace hash join](/grace-hash-join/) with $f = 1$, building on $S$, and the combined plan of the [sort-merge join](/sort-merge-join/) run in $3(M + N)$ here, and whether an in-memory [hash join](/hash-join/) is possible.

2. ◦ Relation $R$ has $M = 500$ pages of 80 tuples, and $S$ has $N = 2000$ pages with an unclustered B+ tree on the join key. A probe reads 2 inner pages and 1 leaf, and each tuple of $R$ has 3 matches on different pages of $S$. With $B = 102$, compare the [index nested-loop join](/index-nested-loop-join/) and the block nested-loop join with $R$ outer. Then let a selection on $R$, applied as $R$ is read, keep only $t$ tuples, which the block nested-loop join packs into its blocks. For which $t$ is the index nested-loop join cheaper?

3. ◦ Run the [Yannakakis algorithm](/yannakakis-algorithm/) on the path $R(A, B)$, $S(B, C)$, $T(C, D)$, $U(D, E)$ with the root $R$, for $R = \{(1,1), (2,2), (3,2), (4,9)\}$, $S = \{(1,3), (2,4), (2,5)\}$, $T = \{(3,6), (4,7), (5,6)\}$ and $U = \{(6,8), (9,9)\}$. Which tuples does each [semijoin](/semijoin/) pass remove, and what is the output? How many intermediate tuples does the plan $((R \bowtie S) \bowtie T) \bowtie U$ build on the original relations?

4. ◦ Two lists grade six objects, and the score is the sum of the two grades: $a = (1.0, 0.7)$, $b = (0.9, 0.1)$, $c = (0.1, 1.0)$, $d = (0.2, 0.9)$, $e = (0.3, 0.8)$, $f = (0.4, 0.75)$. For $k = 1$, at what depth does the [threshold algorithm](/threshold-algorithm/) stop, and at what depth does [Fagin's algorithm](/fagin-algorithm/) stop? What do both return, and how many sorted and random accesses does the threshold algorithm make?

5. ◦ [Hash aggregation](/hash-aggregation/) with room for $m = 2$ groups reads the records $(a, 4)$, $(b, 2)$, $(c, 6)$, $(a, 1)$, $(d, 3)$, $(b, 5)$, $(c, 2)$ and computes COUNT, SUM and AVG per key. Which records are spilled, what does level 0 output, and what does level 1 output if all its groups fit?

6. ◦ In the [iterator model](/iterator-model/), the plan is LIMIT 1 over a hash join whose build input is a selection on a scan of $R$ and whose probe input is a scan of $S$. $R$ has 1000 tuples, of which the selection keeps 100, and the first tuple of $S$ with a partner among them is the seventh. How many tuples have the scans of $R$ and $S$ returned when the root receives its tuple? What changes if the plan has a sort above the join instead of the LIMIT?

7. ◦ A [Bloom join](/bloom-join/) puts the $n = 1000$ distinct keys of $S$ into a filter of $m = 8000$ bits with $k = 4$ hash functions. $R$ has 100,000 tuples, of which 2000 have a partner in $S$, and its other keys are chosen independently of the hash functions. Estimate the false positive rate and the number of tuples of $R$ sent to the site of $S$.

8. ◦ Points $(x, y)$, both to be minimized, are $a = (1, 9)$, $b = (2, 7)$, $c = (3, 8)$, $d = (4, 4)$, $e = (5, 5)$, $f = (6, 2)$, $g = (7, 3)$, $h = (8, 1)$, $i = (9, 6)$. Find the skyline. Sort the points by $x + y$, ties by the tuple, and run the [sort-filter skyline](/sort-filter-skyline/) with a window of $w = 2$. In which order and in which passes are the skyline points output?

9. ◦ Run the leapfrog join of [leapfrog triejoin](/leapfrog-triejoin/) on the sorted lists $A = \{1, 3, 4, 7, 10, 12, 15\}$, $B = \{2, 4, 6, 10, 15, 20\}$ and $C = \{4, 5, 10, 11, 15\}$. List the moves, count them, and compare the count with the bound $m(n_{\min} + 1)$ of the entry.

10. • Let $M = 10{,}000$ and $N = 40{,}000$ pages, with fudge factor $f = 1.2$. Find the smallest $B$ for which the Grace hash join, building on $R$, needs only one partitioning pass, and the smallest $B$ for which the sort-merge join runs its combined plan. Use the conditions of the two entries exactly.

11. • A [hybrid hash join](/hybrid-hash-join/) has $M = 1000$, $N = 3000$, $B = 400$ and $f = 1$. Use the memory plan of the entry to find the number $k$ of disk partitions, the frames $c$ for $R_0$ and the slots $d$ per disk partition. Estimate the share $\rho$ joined in memory, the pages $W$ written and the cost $M + N + 2W$, and compare with the Grace hash join.

12. • [Group-by aggregation](/group-by-aggregation/) splits the east rows $10, 7, 1$ into the parts $\{10, 7\}$ and $\{1\}$. Give a partial state of bounded size for the population variance, its merge, and its final step, and check that the merged state gives the variance of $10, 7, 1$. Which state does COUNT DISTINCT need, and why does it not have bounded size?

13. • Take $R(A, B) = \{(0,0), (1,1)\}$, $S(B, C) = \{(0,1), (1,0)\}$ and $T(C, A) = \{(0,0), (1,1)\}$. Show that no semijoin between two of the relations removes a tuple, yet $R \bowtie S \bowtie T$ is empty. What does this say about semijoin reduction for [cyclic queries](/acyclic-join-evaluation/)?

14. • Run the [no-random-access algorithm](/no-random-access-algorithm/) on the data of exercise 4 with $k = 1$. At what depth does it stop, and how do its accesses compare with those of the threshold algorithm?

15. • Prove that on every database the threshold algorithm stops at a depth no greater than the depth at which Fagin's algorithm ends its sorted phase.

16. • Compute the fractional edge cover number $\rho^*$ and the [AGM bound](/agm-bound/) with $N$ tuples per relation for (a) the 4-clique query with the six edges $AB, AC, AD, BC, BD, CD$; (b) the 5-cycle; (c) the triangle $AB, BC, CA$ with the pendant edge $CD$; (d) the bowtie $AB, BC, CA, CD, DE, EC$. Prove each value with a cover and a fractional vertex packing of the same weight.

17. • In the 4-cycle query $R(A, B) \bowtie S(B, C) \bowtie T(C, D) \bowtie U(D, A)$, let each relation be $\{(0, i), (i, 0) : 1 \le i \le m\}$, so $N = 2m$. Count the output and the tuples of $R \bowtie S$. Compare both with the AGM bound, and explain why the [multiway join](/multiway-join/) argument against two-way plans on the triangle does not carry over to this instance.

18. • In the setting of exercise 7, each tuple of $R$ takes 800 bits on the network. For filters of $m = 4000$, $8000$ and $16{,}000$ bits, with $k$ the integer nearest to $(m/n) \ln 2$, estimate the total bits sent: the filter plus the tuples that pass. Compare with sending the exact set of 1000 keys of 32 bits each, and with sending all of $R$.

19. • Show that in the sort-filter skyline every tuple that enters the window is in the skyline, and that with a window of $w$ tuples and a skyline of $s$ tuples it makes exactly $\lceil s/w \rceil$ passes. Check this on exercise 8 for $w = 1, 2, 3$.

20. • Write open, next and close for a hash semijoin operator $R \ltimes S$ in the iterator model, with a hash table on the keys of $S$. Which input blocks? Change it into the antijoin, the tuples of $R$ with no partner in $S$, and say why the antijoin cannot return its first tuple before $S$ has been read in full, while the semijoin could if the table were built on $R$ instead.

21. ★ Suppose the Grace hash join splits every partition evenly into $B - 1$ parts, and repartitions until each part of $R$ fits in $B - 2$ pages with fudge factor $f$. Show that $L$ levels of partitioning cost $(2L + 1)(M + N)$ I/Os, and that the least $L$ is the least integer with $fM \le (B - 2)(B - 1)^L$. Find $L$ for $M = 100{,}000$, $B = 11$ and $f = 1$.

22. ★ Run [generic join](/generic-join/) on the triangle query $R(A, B) \bowtie S(B, C) \bowtie T(C, A)$, each relation with at most $N$ tuples, with the order $A, B, C$ and intersections that cost the size of the smaller set. Prove without fractional covers that the work at level $C$ is at most $2N^{3/2}$, by splitting the values of $A$ into heavy ones, with more than $\sqrt{N}$ tuples in $T$, and light ones.

23. ★ For the 4-cycle query of exercise 17 with arbitrary relations of at most $N$ tuples, show that the plan $(R \bowtie S) \bowtie (T \bowtie U)$ with hash joins runs in $O(N^2)$ time, which matches the AGM bound. Then give an instance where this plan builds $\Theta(N^2)$ intermediate tuples while the output is empty and generic join, with a suitable order of the attributes, does $O(N)$ work.

24. ★ Two lists rank the same $N$ objects in independent uniformly random orders. Show that the depth $D$ at which Fagin's algorithm with $k = 1$ ends its sorted phase satisfies $\Pr[D > d] = \binom{N - d}{d} / \binom{N}{d}$, and deduce that $E[D]$ is $\Theta(\sqrt{N})$. Compute $E[D]$ for $N = 10{,}000$ and compare it with $\sqrt{\pi N}/2$.

25. ★ For two lists, the sum as score and $k = 1$, build a database of $N$ objects in which an algorithm with sorted access only can name the top object after reading depth 2 in both lists, yet must read to depth $N$ in one list to learn the exact score of that object.
