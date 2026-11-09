1. PREFIX removes the lowest set bit each step: 13, 12, 8. ADD adds it: 5, 6, 8, 16. Cell 12 has lowest bit 4, so it covers $A[9 \ldots 12]$.

2. The cells are $[2, 9, 1, 18, 2, 10, 1, 37]$ and PREFIX$(6) = 28$. The prefix sums are $2, 9, 10, 18, 20, \ldots$, so the answer is $i = 5$; the search from the top of the tree finds it without computing them all.

3. The nodes are 9 for $[1, 1]$, 5 for $[2, 3]$, 6 for $[4, 5]$ and 14 for $[6, 6]$. The minimum is 2 and the sum is 33. For $n = 6$ the largest index is 13.

4. $K = \lfloor \lg 13 \rfloor = 3$, so there are 4 rows with $13 + 12 + 10 + 6 = 41$ cells. The query uses $k = 3$ and the ranges $[2, 9]$ and $[4, 11]$. Max, and, and lcm give the right answer when an item is counted twice; xor and product do not. With $A = [1, 1, 1]$ the xor of $[0, 2]$ comes out as 0 instead of 1, and with $A = [2, 2, 2]$ the product comes out as 16 instead of 8.

6. Sorted by $(\lfloor l/3 \rfloor, r)$ the order is $Q_1, Q_0, Q_3, Q_4, Q_2$. The answers in input order are $3, 2, 3, 3, 1$, and the window makes 14 moves in all.

7. $\mathit{prev} = [-1, -1, -1, 1, -1, 0, 3, 2]$. A position $i$ in $[l, r]$ is counted when $\mathit{prev}[i] < l$. For $[1, 6]$ these are 1, 2, 4 and 5, so the answer is 4; for $[3, 5]$ all three positions count, so the answer is 3.

8. The root keeps $P$, and $Q$ goes to $[0, 4)$. $R$ ties $P$ at 4 and goes left, where it beats $Q$ at 2, so $Q$ is dropped. $S$ ties $P$ at 4 and is below it at 7, so it goes to $[4, 8)$. QUERY$(3) = 1$ and QUERY$(5) = 0$.

10. The root is 2. Its left child is 0, whose right child is 1; its right child is 6, with children 4 and 7, and 4 has children 3 and 5. The tour is $2, 0, 1, 0, 2, 6, 4, 3, 4, 5, 4, 6, 7, 6, 2$. Between the first visits of 3 and 5 the shallowest node is 4, so the minimum is $A[4] = 4$.

18. A set makes every older tag useless, but an add does not.

20. Count separately the moves within one pair of blocks $(\lfloor l/B \rfloor, \lfloor r/B \rfloor)$ and the moves between pairs. The time pointer can move up to $u$ steps for each of the $(n/B)^2$ pairs.

23. Keep one version of a segment tree for each right end $r$. Version $r$ has a 1 at each position $i \le r$ that is the last occurrence of its value among $A[0 \ldots r]$. Each new version changes at most two leaves.

24. A segment $[a, b)$ splits into $O(\log C)$ nodes, as a range does in a segment tree. Insert the line into each of those subtrees as usual.

25. Two arrays have the same answers to all range minimum queries exactly when their Cartesian trees have the same shape. For $n = 10$, $C_{10} = 16796$, so at least 15 bits are needed.

26. Four trees, over $D$, $iD$, $jD$ and $ijD$. The prefix sum up to $(p, q)$ is $(p + 1)(q + 1)\sum D - (q + 1)\sum iD - (p + 1)\sum jD + \sum ijD$.

27. When the right end moves by one, the inversion count changes by the number of items in the window that are greater than the new item; a Fenwick tree over the values gives it in $O(\log n)$.
