1. ◦ A [Fenwick tree](/fenwick-tree/) has $n = 16$ cells, indexed from 1. Which cells does PREFIX$(13)$ read, and which cells does ADD$(5, x)$ change? Which range of the array does cell 12 cover?

2. ◦ Build the Fenwick tree of $A = [2, 7, 1, 8, 2, 8, 1, 8]$, indexed from 1. Give the eight cells, PREFIX$(6)$, and the smallest $i$ with PREFIX$(i) \ge 20$.

3. ◦ A [segment tree](/segment-tree/) over $A = [6, 3, 8, 2, 7, 4, 9, 1]$ has the root 1 over $[0, 7]$, the children $2v$ and $2v + 1$ of node $v$, and splits $[lo, hi]$ at $mid = \lfloor (lo + hi)/2 \rfloor$. Which nodes lie inside the query range $[1, 6]$ and have a parent that does not? Give their indices, their ranges, and the minimum and the sum of the range. For $n = 6$ in the same layout, what is the largest node index used?

4. ◦ A [sparse table](/sparse-table/) is built for $n = 13$. How many rows and how many cells does it have? Which two stored ranges answer the query $[2, 11]$? Which of max, xor, bitwise and, lcm and product can it answer with two overlapping ranges? For each one that fails, give an array of three items where the answer is wrong.

5. ◦ A [disjoint sparse table](/disjoint-sparse-table/) is built for $n = 16$. For each of the queries $(5, 6)$, $(3, 12)$, $(8, 11)$ and $(6, 9)$, give the level $h$, the block of size $2^h$ and its middle.

6. ◦ Run [Mo's algorithm](/mo-algorithm/) for the number of distinct values of $A = [2, 1, 2, 3, 1, 3, 3, 2]$, with block size $B = 3$, the window starting empty at $[0, 0)$, and the half-open queries $Q_0 = [1, 5)$, $Q_1 = [0, 3)$, $Q_2 = [4, 8)$, $Q_3 = [2, 6)$ and $Q_4 = [5, 7)$. Give the order of the queries, the answers in input order, and the total number of ADD and REMOVE calls.

7. ◦ For $A = [3, 1, 4, 1, 5, 3, 1, 4]$, indexed from 0, write the array $\mathit{prev}$ of [the distinct count query](/range-distinct-count-query/), with $-1$ for a first occurrence. Use it to find the number of distinct values in $A[1 \ldots 6]$ and in $A[3 \ldots 5]$, and name the positions that are counted.

8. ◦ A [Li Chao tree](/li-chao-tree/) for minima over the integer domain $[0, 8)$ keeps at each node the line that is lowest at the middle, and on a tie keeps the line already there. Insert, in this order, $P: y = 6 - x$, $Q: y = 3$, $R: y = x - 2$ and $S: y = 10 - 2x$. Which line does each node hold at the end, and which line is dropped? Give QUERY$(3)$ and QUERY$(5)$.

9. ◦ A [Chtholly tree](/chtholly-tree/) holds $A = [1, 1, 1, 4, 4, 2, 2, 2]$ as runs. Apply ASSIGN$(2, 6, 3)$ and then ADD$(1, 7, 2)$, both on half-open ranges. Give the runs after each operation and the sum of the array at the end.

10. ◦ Build the [Cartesian tree](/cartesian-tree/) of $A = [3, 6, 1, 8, 4, 7, 2, 5]$ with the minimum at the root. Give the root, the left and right child of each node, and the Euler tour of the node indices. Use the tour to answer the minimum of $A[3 \ldots 5]$, as in [the equivalence of RMQ and LCA](/rmq-lca-equivalence/).

11. • A [dynamic segment tree](/dynamic-segment-tree/) over the index range $[0, 32)$ creates the nodes on the path of each updated position. How many nodes exist after updates at positions 5, 6 and 20? How many more does an update at 21 create, and how many nodes would a full tree over $[0, 32)$ have?

12. • In [segment tree beats](/segment-tree-beats/), each node keeps its largest value $mx_1$, the largest value below it $mx_2$ ($-\infty$ if none), the count of $mx_1$ and the sum. CHMIN$(x)$ stops at a node with $mx_1 \le x$, puts a tag on a node with $mx_2 < x < mx_1$, and goes into the children otherwise. For $A = [7, 3, 9, 9, 2, 6, 9, 4]$ and CHMIN$(5)$ on the whole array, which nodes are entered and which get a tag? Give the four fields of the root before and after.

13. • Start from an array of 8 zeros, indexed from 0. Apply "add 3 to $A[1 \ldots 4]$" and "add 1 to $A[3 \ldots 7]$" through the difference array $D$ of [range update and range query](/range-update-range-query/). Give $D$, then compute the sum of $A[2 \ldots 6]$ from the two prefix sums of the form $(p + 1) \sum_{j \le p} D[j] - \sum_{j \le p} j D[j]$.

14. • In a [two-dimensional Fenwick tree](/two-dimensional-fenwick-tree/) on a $16 \times 16$ grid, how many cells does an add at $(3, 5)$ change? On a $1000 \times 1000$ grid, what is the largest number of cells that one prefix query reads, and how does it compare with the bound $(\lfloor \lg n \rfloor + 1)(\lfloor \lg m \rfloor + 1)$?

15. • In a Fenwick tree, let $1 \le j \le i \le n$. Prove that the cells read by PREFIX$(i)$ and the cells changed by ADD$(j, x)$ have exactly one cell in common. Explain why this proves that PREFIX returns the right sum after any sequence of ADD calls.

16. • Give two arrays $X$ and $Y$ of five items each such that the [mode](/range-mode-query/) of $X$ is unique, the mode of $Y$ is unique, and the mode of the concatenation $XY$ is a value that is the mode of neither. Explain what this shows about storing (mode, count) in the nodes of a segment tree.

17. • A [range gcd query](/range-gcd-query/) on $k$ numbers of at most $M$ can be computed as a running gcd, $g \leftarrow \gcd(g, A[i])$. Show that the total number of division steps of [Euclid's algorithm](/euclidean-algorithm/) over the whole run is $O(k + \log M)$, not $O(k \log M)$.

18. • Design the tags of [lazy propagation](/lazy-propagation/) for two kinds of range update, "set every item to $c$" and "add $d$ to every item", with range minimum queries. Give the form of a tag, the rule for composing a new tag with an old one, and the new minimum of a node after a tag.

19. • Show that, without assignments, a sequence of $m$ range adds and range sums on a Chtholly tree can take $\Theta(nm)$ time in total. Which initial array gives this?

20. • In [Mo's algorithm with updates](/mo-algorithm-with-updates/), each query has a time $t$, the number of updates before it, and the queries are sorted by $(\lfloor l/B \rfloor, \lfloor r/B \rfloor, t)$. With $n$ items, $q$ queries and $u$ updates, bound the moves of the left end, the right end and the time. Show that with $q$ and $u$ both $\Theta(n)$, the best $B$ is $\Theta(n^{2/3})$ and the total is $O(n^{5/3})$.

21. • The [Bender-Farach-Colton](/bender-farach-colton-rmq/) structure is built on an Euler tour of $m = 2^{16}$ depths, with blocks of $b = \frac12 \lg m$ entries. How many blocks are there, how many different block tables can there be at most, and how many entries do they hold in all if each table has $b^2$ entries? How many cells does a sparse table over the block minima need, by the cell formula of the sparse table, and how many would a sparse table over all $m$ depths need?

22. • Give an $O(\log n)$ algorithm on a segment tree of maxima that returns the smallest $j \ge l$ with $A[j] \ge x$, or reports that there is none.

23. ★ Design an online structure for the distinct count query: after $O(n \log n)$ preprocessing, it answers the number of distinct values of $A[l \ldots r]$ in $O(\log n)$ time, for queries that arrive one at a time. Bound its space.

24. ★ A Li Chao tree over $[0, C)$ must also accept segments: a line that exists only on an interval $[a, b)$. Show how to insert a segment in $O(\log^2 C)$ time while the query stays $O(\log C)$.

25. ★ Prove that any structure that answers the index of the minimum of every range of an array of $n$ distinct items, without reading the array, must use at least $\lg C_n = 2n - O(\log n)$ bits, where $C_n$ is the $n$-th Catalan number. How many bits does this give for $n = 10$?

26. ★ Support "add $c$ to every cell of the rectangle $[x_1, x_2] \times [y_1, y_2]$" and "sum of the rectangle $[x_1, x_2] \times [y_1, y_2]$" on an $n \times m$ grid in $O(\log n \log m)$ time per operation with Fenwick trees. How many trees do you need, and what does each store?

27. ★ Queries ask for the number of inversions of $A[l \ldots r]$, that is, the pairs $l \le i < j \le r$ with $A[i] > A[j]$. Answer $q$ offline queries in $O(n \sqrt q \log n)$ time with Mo's algorithm and a Fenwick tree.
