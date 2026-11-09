1. $P = \langle 0, 2, 1, 4, 4, 8, 6, 11 \rangle$. The sum of $a[2 \ldots 5]$ is $P[6] - P[2] = 6 - 1 = 5$, and the sum of $a[1 \ldots 3]$ is $P[4] - P[1] = 4 - 2 = 2$.

2. $d = \langle 2, -1, 6, -2, 0, 0, -5 \rangle$, and its prefix sums give $\langle 2, 1, 7, 5, 5, 5 \rangle$.

4. After the zero row, the rows of $S$ are $\langle 0, 1, 3, 6 \rangle$, $\langle 0, 5, 12, 21 \rangle$ and $\langle 0, 12, 27, 45 \rangle$. The block is $S[3][3] - S[1][3] - S[3][1] + S[1][1] = 45 - 6 - 12 + 1 = 28 = 5 + 6 + 8 + 9$.

5. The prefix XORs are $\langle 0, 5, 6, 0, 1 \rangle$, and the answer is $P[3] \oplus P[1] = 0 \oplus 5 = 5 = 3 \oplus 6$. Each element is its own inverse under XOR.

7. Addition and XOR always. Multiplication modulo 7 only when no item is a multiple of 7, and multiplication modulo 8 only when every item is odd, since only those residues have inverses. Maximum and gcd never: $\langle 3, 1 \rangle$ and $\langle 3, 2 \rangle$ have the same prefix maxima but different maxima on the range of the second item.

8. Eight entries, one per corner of the box. The entries that use the lower bound in an odd number of coordinates, three of them with one lower bound and one with all three, get a minus sign.

14. Use a difference array over XOR: a toggle of $[l, r)$ flips $d[l]$ and $d[r]$, and lamp $i$ is the XOR of $d[0 \ldots i]$. For the online form, keep $d$ in a Fenwick tree whose operation is XOR.

16. With non-negative items, $P$ is non-decreasing. For $a = \langle 5, -5, 3 \rangle$, $P = \langle 0, 5, 0, 3 \rangle$ and $s = 3$, the answer is $k = 1$, but a binary search over $k \in \{1, 2, 3\}$ looks at $P[2] = 0 < 3$ first and returns $3$.

17. An update costs $O(1)$, plus $O(n)$ for every $B$-th one; a query costs $O(1 + B)$, since it must add the pending updates that fall in its range. The total is $O(n + qB + qn/B)$, and $B = \sqrt{n}$ balances the two terms.

19. Five entries change: $e[l] \mathrel{+}= 1$, $e[l+1] \mathrel{+}= 1$, $e[l+m] \mathrel{-}= (m+1)^2$, $e[l+m+1] \mathrel{+}= 2m^2 + 2m - 1$ and $e[l+m+2] \mathrel{-}= m^2$. Find them by taking the third difference of the values $0, 0, 0, 1, 4, 9, \ldots$ at the start of the range and $\ldots, (m-1)^2, m^2, 0, 0, 0$ at its end.

20. Compute $(k+1)^{\underline{-m}} - k^{\underline{-m}}$ over the common denominator $(k+1) \cdots (k+m+1)$. The sum is $\big[k^{\underline{-3}}/(-3)\big]_0^n$.

21. The condition is $L \le P[r] - P[l] \le U$. Sort the prefix sums by merge sort, and in each merge count, for each $P[r]$ of the right half, the $P[l]$ of the left half that lie in $[P[r] - U, P[r] - L]$ with two pointers that only move forward. Coordinate compression and a Fenwick tree also work.

22. A query walks from the root to a leaf and adds one stored prefix per level. An update changes up to $B$ stored prefixes in each node on the path from the leaf to the root. Take $B = \lceil \log^{\varepsilon} n \rceil$. With $b = \Theta(\log n)$ and $t_u$ polylogarithmic, the lower bound is $\Omega(\log n / \log \log n)$, which these queries meet.
