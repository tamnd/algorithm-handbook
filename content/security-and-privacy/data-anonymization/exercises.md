Exercises 9 to 11 use one table of eight rows, with the quasi-identifier (age, ZIP): row 1 = (23, 13021), row 2 = (27, 13024), row 3 = (25, 13022), row 4 = (34, 13051), row 5 = (38, 13053), row 6 = (31, 13059), row 7 = (45, 14801), row 8 = (29, 13021). Age has the levels exact, decade (such as 20–29) and $*$. ZIP has the levels 5 digits, 4 digits, 3 digits and $*$. A generalization vector $(i, j)$ gives the level of age and the level of ZIP, from $(0, 0)$ to $(2, 3)$. Suppressed rows are removed.

1. ◦ A released table has nine rows in three blocks. Block A, (20–29, 130\*\*, M), has the diseases flu, flu, cancer. Block B, (30–39, 148\*\*, F), has heart disease three times. Block C, (40–49, 130\*\*, \*), has flu, cancer and heart disease. Give the largest $k$ for which the table is [k-anonymous](/k-anonymity/), the number of distinct values in each block, and what a neighbour learns about a woman of 35 with ZIP 14850 who is known to be in the table.

2. ◦ A block of six rows has the sensitive counts $(3, 2, 1)$. Compute its entropy in bits. Decide whether it is entropy 2-diverse and entropy 3-diverse in the sense of [l-diversity](/l-diversity/), using the integer test. Find the values of $c$ for which it is recursive $(c, 2)$-diverse, and those for which it is recursive $(c, 3)$-diverse.

3. ◦ A numeric sensitive attribute takes the values $1, \ldots, 6$, and the whole table holds each value twice. Three blocks of four rows hold the values $\{1, 1, 2, 6\}$, $\{2, 3, 4, 5\}$ and $\{3, 4, 5, 6\}$. Compute the ordered distance and the equal distance of each block to the table, as defined in [t-closeness](/t-closeness/). Give the least $t$ for which the release is $t$-close under the ordered distance.

4. ◦ A file replaces each 9-digit national number by its unkeyed SHA-256 hash, as a form of [pseudonymization](/pseudonymization/). An attacker can compute $10^8$ hashes per second. Find the time it takes to hash every possible number, and so to undo the pseudonyms. Name the change that stops this attack, and the attack that the change does not stop.

5. ◦ In [privacy-preserving record linkage](/privacy-preserving-record-linkage/), each name is padded with one blank on each side and split into bigrams. List the bigram sets of "anna" and "anne", and compute their Dice coefficient and their Jaccard coefficient.

6. ◦ Run quadtree [spatial cloaking](/spatial-cloaking/) with the area $[0, 8)^2$, depth limit $h = 3$ and $k = 3$ for the seven users at $(1, 1)$, $(2, 3)$, $(3, 0)$, $(1, 6)$, $(6, 6)$, $(5, 2)$ and $(7, 7)$. Give the region that each user receives.

7. ◦ Under the p% rule, a cell with total $X$, largest contribution $x_1$ and second largest $x_2$ is sensitive when $X - x_1 - x_2 < (p/100) \, x_1$: the second contributor can then estimate $x_1$ to within $p$ percent. With $p = 20$, decide whether the cells with contributions $(60, 30, 10)$ and $(50, 30, 20)$ are sensitive. These are the cells that the [cell suppression problem](/cell-suppression-problem/) must protect.

8. ◦ A database of baskets is $D = \{a, b\}, \{a, b, c\}, \{a, c\}, \{b, c\}, \{a, b, c\}$. For $m = 1, 2, 3$, give the largest $k$ for which $D$ is $k^m$-anonymous in the sense of [km-anonymity](/km-anonymity/).

9. • Run [Datafly](/datafly/) with $k = 2$ on the eight-row table. Give the vector after each step, the rows in classes of fewer than 2 rows at each step, the rows that are suppressed and the final classes.

10. • For $k = 2$, list the number of suppressed rows for each of the twelve vectors. Then run the [Samarati algorithm](/samarati-algorithm/) with MaxSup = 0 and with MaxSup = 1, and give the heights that the binary search tries and the vector it returns.

11. • Run [Mondrian](/mondrian-anonymization/) on the eight-row table with numeric age and ZIP, for $k = 2$ and for $k = 3$. Choose the attribute with the widest range divided by its range in the whole table, break ties in favour of age, and cut at the median. Give the regions and their ranges. Then compute the discernibility cost (the sum of the squared class sizes, plus $n$ for each suppressed row) of the two Mondrian releases and of the Datafly release of Exercise 9.

12. • Run [MDAV](/mdav/) with $k = 3$ on the nine values $6, 7, 8, 9, 14, 24, 25, 26, 29$, and compute the within-group sum of squares of its partition. Then find an optimal partition into groups of at least 3 by the shortest path method of [microaggregation](/microaggregation/), and compare the two losses with the total sum of squares.

13. • The [post-randomization method](/post-randomization-method/) uses the matrix $P$ with rows $(0.9, 0.1)$ and $(0.2, 0.8)$ on a binary attribute of 1000 records, and the released counts are $T^* = (380, 620)$. Compute the estimate $\hat T$ and the [local privacy](/local-differential-privacy/) parameter $\varepsilon$ of $P$. Then compute the estimate for $T^* = (150, 850)$, and say what it shows about the estimator.

14. • Eight tuples have the sensitive values t1 flu, t2 cold, t3 flu, t4 hiv, t5 cold, t6 flu, t7 hiv, t8 ulcer. Form groups for [anatomy](/anatomy-bucketization/) with $l = 2$: at each step take the oldest remaining tuple from each of the two largest buckets, and break ties between buckets by the first appearance of the value. Give the groups and the two published tables.

15. • In [k-degree anonymization](/k-degree-anonymization/), a degree sequence may only be raised. For $d = (5, 4, 4, 3, 2, 2, 2, 1, 1)$, find the least total increase that makes the sequence 3-anonymous and 2-anonymous, and give an optimal sequence for each. For $k = 3$, give two different optimal sequences.

16. • A table has the inner cells r1 = (8, 14, 20), r2 = (3, 25, 11) and r3 = (16, 6, 9) with row and column totals published. The cell (r2, c1) = 3 is sensitive, values are nonnegative, and the cost of a cell is its value. For each rectangle of four cells that contains (r2, c1), give the interval that an attacker can derive for that cell and the cost of the three other cells. Find the cheapest rectangle that protects the cell when the upper protection level is 10 and there is no lower protection level.

17. • Apply the reduction of [the NP-hardness of k-anonymity](/k-anonymity-np-hardness/) to the 3-uniform hypergraph on the vertices $1, \ldots, 6$ with the edges $e_1 = \{1, 2, 3\}$, $e_2 = \{1, 4, 5\}$, $e_3 = \{4, 5, 6\}$, $e_4 = \{2, 3, 6\}$. Write the table, give $c$, give a 3-anonymous suppression of cost $c$, and give the cost of the suppression that puts all six rows in one class.

18. • Prove that if every transaction of a database occurs at least $k$ times, the database is $k^m$-anonymous for every $m$. Then check that $\{a, b\}, \{a, b\}, \{a\}, \{a, b, c\}, \{a, b, c\}$ is $2^m$-anonymous for every $m$, although one transaction occurs once.

19. ★ Prove that for any two distributions on an ordered domain of $m$ values, the ordered distance of t-closeness is at most the equal distance. Check the inequality on the three blocks of Exercise 3, and show that it is an equality when $m = 2$.

20. ★ Let $P$ be the distribution of a block and $W$ that of the table on the values $1, \ldots, m$, and suppose that the partial sums $\sum_{j \le i} (p_j - w_j)$ never change sign. Prove that the ordered distance equals the difference of the two means divided by $m - 1$. Check this on the third block of Exercise 3, and show that it fails for the first block.

21. ★ Release 1 of a table holds four people of ages 21, 22, 23 and 24 with the sensitive values $a$, $b$, $c$ and $d$, in the groups $[21, 22]$ and $[23, 24]$. Before release 2, the person of age 24 leaves and a person of age 20 with value $e$ arrives. Release 2 has the groups $[20, 21]$ and $[22, 23]$. Both releases are 2-diverse. Show what an attacker who knows that Bob is 22 and is in both releases learns. Then prove that no release of the four people of release 2 in groups of two with distinct values is 2-invariant in the sense of [m-invariance](/m-invariance/), so that the publisher must add a counterfeit tuple.

22. ★ Mondrian stops in a region with no allowable cut, and such a region has at most $2d(k - 1) + m$ rows, where $m$ is the largest number of equal rows. Show that the bound is tight for every $d \ge 1$, $k \ge 2$ and $m \ge 1$ by giving a region with exactly that many rows and no allowable cut.
