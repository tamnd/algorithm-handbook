1. Writing a tree as (left, key, right): ((8, 15, (19, 22, 27)), 30, (40, 45, (50, 60, nil))). The height is 3, and the deepest keys are 19, 27 and 50. The search for 25 visits 30, 15, 22 and 27, and stops at the empty left child of 27.

2. The keys in order are 8, 15, 19, 22, 27, 30, 40, 45, 50, 60. The floor and ceiling of 25 are 22 and 27, and of 42 they are 40 and 45. The key 5 has no floor and has ceiling 8. The key 61 has floor 60 and no ceiling.

3. Deleting 15 moves its successor 19 into its place: ((8, 19, (nil, 22, 27)), 30, (40, 45, (50, 60, nil))). Deleting 30 then moves 40 to the root: ((8, 19, (nil, 22, 27)), 40, (nil, 45, (50, 60, nil))). Deleting 30 first gives the same final tree.

4. There are 14 shapes, the Catalan number $C_4$. A path needs each of the first three keys inserted to be the smallest or the largest of the keys still to come, so 8 orders give height 3 and 16 give height 2. The expected height is $7/3$.

5. By $H_i + H_{n-i+1} - 2$: key 1 has expected depth $H_7 - 1 = 223/140 \approx 1.59$, and key 4 has $2H_4 - 2 = 13/6 \approx 2.17$.

6. The path $k_1, k_2, k_3$ costs $1.5$; root $k_1$ with $k_3$ below and $k_2$ below that costs $1.7$; the balanced tree costs $1.7$; root $k_3$ with $k_1$ below and $k_2$ below that costs $2.2$; the path $k_3, k_2, k_1$ costs $2.5$. The best tree is the path from $k_1$, which is as unbalanced as possible.

7. Level 3 holds 10 and 23, level 2 holds 4, 10, 16 and 23, and level 1 holds all eight keys. The search moves from the header to 10 on level 3, to 16 on level 2, and to 20 on level 1; each time the next key, 23, is too large. The node after 20 holds 23, so 21 is not present. Its floor is 20 and its ceiling 23.

8. The tree is (((1, 2, 3), 4, 5), 6, 8). Node 3 is a right child and its parent a left child, so the first step is a zig-zag, which puts 3 in the place of 4; a zig with 6 follows, giving ((1, 2, nil), 3, ((nil, 4, 5), 6, 8)). Splaying 8 is one zig-zig, a rotation at 3 and then at 6: ((((1, 2, nil), 3, (nil, 4, 5)), 6, nil), 8, nil).

9. There are $n + 1 = 11$ threads. The leaves 8, 19, 27, 40 and 50 have two each, and 60 has a right thread. Left threads: 8 to NIL, 19 to 15, 27 to 22, 40 to 30, 50 to 45. Right threads: 8 to 15, 19 to 22, 27 to 30, 40 to 45, 50 to 60, and 60 to NIL. The two NIL threads are the left thread of 8 and the right thread of 60.

10. The positions are $\mathrm{msb}(3 \oplus 6) = 2$, $\mathrm{msb}(6 \oplus 20) = 4$ and $\mathrm{msb}(20 \oplus 22) = 1$, so $D = \{4, 2, 1\}$. The sketches are 001, 011, 110 and 111, that is 1, 3, 6 and 7. The query $2 = 00010$ has sketch 001, the same as the key 3, although $2 < 3$: the bit where 2 and 3 differ, bit 0, is not in $D$. So the sketch rank cannot tell that 2 has no predecessor; the correction step of the entry fixes this.

12. The root must come first, and the orders of the two subtrees can be interleaved in $\binom{n-1}{s(\text{left})}$ ways; induction gives the product formula. The perfect tree on 7 keys has $7!/(7 \cdot 3 \cdot 3) = 80$ orders. The tree of exercise 1 has $10!/(10 \cdot 5 \cdot 4 \cdot 3 \cdot 2) = 3024$.

15. For $1 < i < n$, key $i$ is a leaf exactly when it comes after both $i - 1$ and $i + 1$, which has probability $1/3$. The keys 1 and $n$ have one neighbour each, so probability $1/2$. The sum is $(n - 2)/3 + 1 = (n + 1)/3$.

17. $c(p) = 1/(p \lg(1/p))$, so $c(1/2) = c(1/4) = 2$. The minimum is at $p = 1/e$, with $c = e \ln 2 \approx 1.88$. Choose $p = 1/4$: the search cost is the same as for $p = 1/2$, and a node has $4/3$ pointers on average instead of 2.

23. The 6 orders and 3 keys give 18 equally likely cases. Count them by hand: in 10 of them the larger of the two remaining keys is the root. The method deletes a node with only a right child by moving the child up, and that case breaks the symmetry.

25. Let $s$ be the successor of the deleted key $x$. If $s$ comes after $x$ in the insertion order $\pi$, the new tree is the one built by $\pi$ with $x$ removed and $s$ moved to the place of $x$; otherwise it is the tree built by $\pi$ with $x$ removed. Fix an order $\sigma$ of the remaining keys, renamed $1, \ldots, n - 1$, and count the pairs $(\pi, x)$ that lead to it. The largest key gives $n$ pairs; the key of rank $r < n$ gives $2(n - j)$, where $j$ is the position of $r$ in $\sigma$. The sum is $n + n(n - 1) = n^2$ for every $\sigma$.

26. Each of the $n + 1$ keys must be the root with probability $1/(n + 1)$. The new key is, by the rule. An old key was the root with probability $1/n$ and stays the root with probability $n/(n + 1)$. Given the root, the two subtrees are independent random trees: by the split lemma when $x$ is the root, and by induction otherwise.

27. If some key has a prefix of length $\ell$ in common with the query $q$, so do the shorter prefixes, so the longest common prefix length can be found by binary search over $\ell$, with $O(\log w)$ hash lookups. Let $u$ be that prefix. If the next bit of $q$ is 1, the predecessor is the largest key that starts with $u0$. If it is 0, the smallest key that starts with $u1$ is the successor of $q$, and the list gives its predecessor. The space is $O(nw)$.

28. Cut the sorted keys into groups of between $w/2$ and $2w$ keys, keep each group in a balanced search tree, and put one key of each group into the structure of exercise 27. That structure then has $O(n/w)$ keys and $O(n)$ space. A query finds the right group in $O(\log w)$ time and searches one or two groups of $O(w)$ keys in $O(\log w)$ time.

29. A finger search from the previous key costs $O(1)$. Each split turns a 3-node that has received a third key into two 2-nodes, and an insertion that stops makes at most one new 3-node. So the number of 3-nodes, which is never negative, pays for all the splits but at most one per insertion.
