1. ◦ In all the exercises, $\text{rank}_b(B, i)$ counts the bits equal to $b$ in $B[0, i)$, and $\text{select}_b(B, j)$ is the position of the $j$-th bit equal to $b$, with $j$ counted from 1 and positions from 0. Let $B = 1101\,0010\,0111\,0001$, so $n = 16$. Compute $\text{rank}_1(B, 7)$, $\text{rank}_0(B, 10)$, $\text{select}_1(B, 5)$ and $\text{select}_0(B, 3)$. Then read $B[9]$ using only rank, as in the [rank and select problem](/rank-select-problem/).

2. ◦ The number of [ordinal trees](/ordinal-tree/) with $n$ nodes is the Catalan number $C_{n-1}$. For $n = 5$, how many bits does the information-theoretic lower bound give? Compare with [LOUDS](/louds-tree/) (with its two-bit prefix), with [balanced parentheses](/balanced-parentheses-representation/), and with a pointer tree that stores three 32-bit fields per node.

3. ◦ Let $T$ be the tree with root $A$, children $B$ and $C$; $B$ has children $D, E, F$; $C$ has one child $G$; $G$ has children $H$ and $I$. Number the nodes $0$ to $8$ in level order and write the LOUDS string $L$, starting with the prefix $10$. Use $\text{child}(k, i) = \text{rank}_1(L, \text{select}_0(L, k + 1)) + i - 1$ and $\text{parent}(k) = \text{rank}_0(L, \text{select}_1(L, k + 1)) - 1$ to find the third child of $B$ and the parent of $H$.

4. ◦ Write the balanced parentheses string $P$ of the tree $T$ of Exercise 3, with children in the order given. Give the position of each node's opening parenthesis, compute $\text{findclose}$ for $B$, $C$ and $G$, the subtree sizes they give, and the depth of $H$ from the excess (the root has depth 0).

5. ◦ Write the [DFUDS](/dfuds/) string $U$ of $T$: a leading $($, then for each node in preorder as many $($ as it has children, followed by one $)$. Give the position where each node's description starts, and read off the degree of $B$.

6. ◦ Encode $X = 5, 17, 18, 40, 63, 97$ with [Elias-Fano](/elias-fano-encoding/), universe $u = 100$, $n = 6$ and $\ell = \lfloor \lg(u/n) \rfloor$. Give the low parts, the high bit string $H$ (bit $h_i + i$ set), and the total number of bits. Compare with $7$ bits per value and with $\lg \binom{100}{6}$. Then compute $\text{access}(3)$ (indices from 0) with one select.

7. ◦ Map the letters of "mississippi" to $i = 0$, $m = 1$, $p = 2$, $s = 3$. Build the [wavelet tree](/wavelet-tree/) that splits the range $[a, b)$ at $\lfloor (a + b)/2 \rfloor$, with bit 1 for the upper half. Give the bit vectors of the three nodes. Compute $\text{access}(6)$, $\text{rank}_s(8)$ and $\text{rank}_i(9)$ by walking the tree.

8. ◦ An array has $n = 10^6$ slots, of which $m = 10^4$ hold a 32-bit value and the rest are empty. Count the bits of (a) a plain array of 32-bit slots, (b) a bit vector of occupied slots with rank plus the values packed in order, (c) the same with the bit vector replaced by an [SD-array](/sd-array/) with $\ell = \lfloor \lg(n/m) \rfloor$ and a high part of $m + \lfloor (n - 1)/2^\ell \rfloor + 1$ bits. Ignore the $o(\cdot)$ terms.

9. • Build the two-level index of [Jacobson's rank](/jacobson-rank/) for $n = 2^{20}$ bits: superblocks of $200$ bits store an absolute count in 21 bits, blocks of $10$ bits store a count relative to their superblock in 8 bits, and a table gives the rank inside every 10-bit pattern for each of the 11 prefix lengths, in 4 bits per answer. Count the bits of each part. What fraction of $n$ is the index, and why is this still "$o(n)$" only in the limit?

10. • Encode $B = 0110\,1000\,1111\,0101$ as an [RRR bit vector](/rrr-bitvector/) with blocks of $b = 4$ bits. Inside a class $c$, number the blocks by $\sum_i \binom{p_i}{i}$, where $p_1 < p_2 < \cdots$ are the positions of the ones, counted from 0 at the left. Give the class and offset of each block, the number of offset bits, and the total with 3-bit classes. Compare with $\lg \binom{16}{8}$. Then decode class 2 offset 4, class 2 offset 5 and class 1 offset 3.

11. • On the Elias-Fano encoding of Exercise 6, answer $\text{next\_geq}(30)$, $\text{next\_geq}(41)$ and $\text{next\_geq}(64)$. Start at bucket $h = \lfloor y / 2^\ell \rfloor$: the position $p = \text{select}_0(H, h) + 1$ (or $0$ if $h = 0$) holds the first element with high part at least $h$, and its index is $p - h$. For each query give $h$, $p$, the starting index, and the elements passed over.

12. • In the BP string of Exercise 4, the lowest common ancestor of two nodes $x$ and $y$, neither an ancestor of the other, with opening positions $i < j$, is found as follows: take the leftmost position $m$ of minimum excess in $[i, j]$; the answer is the parent of the node that opens at $m + 1$. Compute $\text{lca}(E, H)$, $\text{lca}(D, F)$ and $\text{lca}(F, I)$, giving $m$ each time.

13. • In the DFUDS string of Exercise 5, let $e$ be the position of the $)$ that ends the description of $v$. Then $\text{child}(v, i) = \text{findclose}(e - i) + 1$. For the parent of a node starting at $s$, find $o = \text{findopen}(s - 1)$; the parent starts just after the $k$-th $)$ with $k = \text{rank}_)(U, o)$ (or at 1 if $k = 0$). Compute $\text{child}(B, 2)$, $\text{child}(A, 2)$, $\text{parent}(H)$ and $\text{parent}(C)$.

14. • Build the [wavelet matrix](/wavelet-matrix/) of the sequence of Exercise 7 with 2-bit codes, most significant bit first: at each level write the current bit of every symbol, count the zeros $z_\ell$, and reorder stably with zeros first. Give both levels and $z_0$, $z_1$. Then compute $\text{access}(6)$ and $\text{rank}_s(8)$, giving the pair $(p, i)$ of positions after each level.

15. • On the wavelet tree of Exercise 7, find the 3rd smallest value of $S[2, 9)$ by a single descent, giving the range and $k$ at each node. Then compute $\text{select}_p(2)$ by climbing from the leaf.

16. • Store $\pi = [6, 9, 0, 11, 3, 1, 8, 2, 7, 4, 10, 5]$ as a [succinct permutation](/succinct-permutation/) with $t = 3$: in each cycle of length more than $t$, mark the elements $c_0, c_t, c_{2t}, \ldots$ along the cycle starting from its smallest element, and give each mark a back pointer to the previous mark on the cycle. Find the cycles, the marks, the back pointers and the bit vector of marks. Compute $\pi^{-1}(4)$ and $\pi^{-1}(2)$, listing the positions visited, and give the largest number of positions visited by any inverse query. Count the bits of $\pi$, of the marks and of the back pointers stored as 4-bit indices.

17. • Build a [range min-max tree](/range-min-max-tree/) with blocks of 4 symbols over $P = ((()()())((())))$. Each node stores the total excess $e$ and the minimum $m$ and maximum $M$ of the running excess inside its range, relative to the start of the range. Give the four leaves, the two internal nodes and the root. Then trace $\text{findclose}(1)$ and $\text{findclose}(9)$, saying which nodes are skipped because their excess range cannot contain the target.

18. • Take $n = 2^{30}$ and $m = 2^{16}$ ones. Compute the exact size of the SD-array with $\ell = \lfloor \lg(n/m) \rfloor$, the entropy bound $\lg \binom{n}{m}$ (to a few digits), and the plain bit vector. Then estimate the lower-order term $n \lg \lg n / \lg n$ of an RRR bit vector and explain why a sparse set prefers Elias-Fano.

19. ★ Show that $\lg C_{n-1} = 2n - \tfrac32 \lg n + O(1)$, where $C_{n-1} = \frac{1}{n}\binom{2n-2}{n-1}$. Conclude that both LOUDS and balanced parentheses are within $O(\lg n)$ bits of optimal, before their indexes are added.

20. ★ The points $(i, S[i])$ for $S = [5, 2, 7, 1, 4, 6, 0, 3]$ lie on an $8 \times 8$ grid, one per column. Show how a wavelet tree over $S$ counts the points in $[x_1, x_2) \times [y_1, y_2)$ in $O(\lg \sigma)$ rank operations, and carry it out for $x \in [1, 6)$, $y \in [2, 6)$.

21. ★ Prove that the offset $\sum_{i=1}^{c} \binom{p_i}{i}$ of Exercise 10 is a bijection from the $b$-bit blocks of class $c$ onto $\{0, 1, \ldots, \binom{b}{c} - 1\}$, and that the greedy decoder (take the largest $p$ with $\binom{p}{c} \le$ offset, subtract, and recurse with $c - 1$) inverts it.

22. ★ A wavelet tree stores each node's bit vector as an RRR bit vector of $\lg \binom{n_v}{m_v} + o(n_v)$ bits. Prove that the sum over all nodes of the $\lg \binom{n_v}{m_v}$ terms is at most $n H_0(S)$ plus lower-order terms, where $H_0$ is the empirical zero-order entropy. Use that at each node the count of a symbol only splits, never mixes.

23. ★ The prefix-parity problem keeps $n$ bits under flips and answers the parity of $B[0, i)$. Fredman and Saks showed that it needs $\Omega(\lg n / \lg \lg n)$ time per operation in the cell-probe model with words of $O(\lg n)$ bits. Show that a [dynamic bit vector](/dynamic-bit-vector/) with flip and rank in $O(t)$ time solves prefix parity in $O(t)$ time, and conclude that the bounds of the entry are optimal.
