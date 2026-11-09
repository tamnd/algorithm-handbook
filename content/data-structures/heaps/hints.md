1. (a) and (c) are min-heaps; equal keys are allowed. (b) is not: position 5 holds 2, and its parent at position 2 holds 3.

3. The 4 goes in at position 10, swaps with 10 and then with 8, and stops below 3: $\langle 3, 4, 5, 12, 8, 7, 9, 15, 14, 10 \rangle$, after 2 swaps. Extract-min moves 10 to the root, which sinks past 4 and 8: $\langle 4, 8, 5, 12, 10, 7, 9, 15, 14 \rangle$.

4. Floyd's method gives $\langle 1, 2, 5, 3, 6, 9, 8, 7, 4 \rangle$ with 6 swaps, and $n - s_2(n) = 9 - 2 = 7$. Insertion gives $\langle 1, 2, 3, 4, 7, 8, 5, 9, 6 \rangle$ with 10 swaps, a different heap of the same keys.

7. The heap holds $\{12\}$, $\{7, 12\}$, $\{7, 12, 25\}$; 3 is skipped; then $\{12, 18, 25\}$, $\{18, 25, 30\}$; 9 is skipped; then $\{22, 25, 30\}$, $\{25, 30, 41\}$; 15 is skipped. The answer is 41, 30, 25, and the heap changed 7 times: 3 inserts and 4 replacements.

8. $13 = 1101_2$, so the trees are $B_3$, $B_2$ and $B_0$. The next insert makes 1 link, giving $B_3, B_2, B_1$; the one after makes none. A heap of $15 = 1111_2$ keys has four trees, so the insert makes 4 links and leaves one $B_4$.

9. At first $B[2] = \{2, 3\}$ and $B[4] = \{9, 12\}$. The first call sets $last = 2$ and moves 3 to $B[1]$; the second sets $last = 3$; the third empties $B[4]$, sets $last = 9$ and moves 12 to $B[3]$, since $12 \oplus 9 = 0101_2$. The refills move items 5 times.

11. For $n = 6$ the subtree sizes multiply to $6 \cdot 3 \cdot 2 = 36$, so there are $720/36 = 20$ heaps; for $n = 7$ the product is $7 \cdot 3 \cdot 3 = 63$ and there are 80 heaps. A comparison tree that builds a heap must tell apart the $n!$ inputs up to the $n!/\prod s(v)$ that lead to the same heap, so it needs $\lceil \lg \prod s(v) \rceil$ comparisons: 6 in both cases.

16. Each insert adds one tree, and each link removes one. After $n$ inserts there are $s_2(n)$ trees, so there were $n - s_2(n)$ links: 994 for $n = 1000$. In the alternating run each insert makes $k$ links, and the extract-min that follows breaks the $B_k$ back into $B_0, \ldots, B_{k-1}$, raising the number of trees by $k - 1$. With the number of trees as the potential, it is the extract-min that pays.

20. A key inserted at position $i$ can rise at most to the root, $\lfloor \lg i \rfloor$ levels. A new smallest key rises all the way. For $n = 10$ the sum is $0 + 1 + 1 + 2 + 2 + 2 + 2 + 3 + 3 + 3 = 19$.

21. Use a second heap of candidates, ordered by key, that holds positions of the first heap. Start it with the root. Each time you take a position out, output its key and put in its two children. Every key output is the smallest key not yet output, because the parent of each node comes out before the node. The candidate heap never holds more than $k + 1$ positions.

22. The tree is 1(7, 2(6, 3(5, 4))): its right path is 1, 2, 3, 4. In general insert $k, k + 1, k + 2$, then $k - 1, k + 3$, then $k - 2, k + 4$, and so on down to $1, 2k + 1$. The right path is then $1, 2, \ldots, k + 1$. The long insert swaps the children of every node on its path, so the path does not stay long.

23. Build a binomial tree $B_k$, for example by inserting $2^k + 1$ keys and calling extract-min. Then lower each grandchild of the root to a key that is still above the root's key but below its parent's key; each such decrease-key cuts the grandchild, with its subtree, to the root list. The root keeps its $k$ children, and each has lost all of its own. The proof that a node of degree $k$ has at least $F_{k+2}$ descendants used the rule that a node loses at most one child before it is cut; without it, $D(n)$ can be $n - 1$.

24. A key never corrupted is never smaller than any item returned before it, since current keys only go up. At most $n/3$ of the items left are corrupted, so at least $n - \lceil n/3 \rceil - n/3$ of them are uncorrupted, and each is larger than $x$. For selection, compare every key with $x$, throw away the side that cannot hold the answer, and recurse on at most $2n/3 + 1$ keys.

25. One input is $\langle 3, 2, 4, 1, 5, 6, 7, 8 \rangle$. Sift-down at position 4 makes 1 comparison (one child), at 3 makes 2, at 2 makes 2 and then 1, and at 1 makes 2, 2 and 1: in all 11. The formula gives $16 - 2 - 3 = 11$.
