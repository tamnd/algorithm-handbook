1. $\text{rank}_1(B, 7) = 4$, $\text{rank}_0(B, 10) = 5$, $\text{select}_1(B, 5) = 9$ and $\text{select}_0(B, 3) = 5$. $B[9] = \text{rank}_1(B, 10) - \text{rank}_1(B, 9) = 5 - 4 = 1$.

3. $L = 1011011101000011000$, 19 bits. $B$ is node 1: $\text{select}_0(L, 2) = 4$ and $\text{rank}_1(L, 4) = 3$, so its third child is node $3 + 3 - 1 = 5$, which is $F$. $H$ is node 7: $\text{select}_1(L, 8) = 14$ and $\text{rank}_0(L, 14) = 7$, so its parent is node 6, which is $G$.

4. $P = ((()()())((()())))$, 18 symbols. The nodes open at $A{:}0$, $B{:}1$, $D{:}2$, $E{:}4$, $F{:}6$, $C{:}9$, $G{:}10$, $H{:}11$, $I{:}13$. $\text{findclose}$ gives 8 for $B$, 16 for $C$ and 15 for $G$, so the subtrees have $4$, $4$ and $3$ nodes. The excess after position 11 is 4, so $H$ has depth 3.

6. $\ell = 4$, the high parts are $0, 1, 1, 2, 3, 6$ and the low parts $5, 1, 2, 8, 15, 1$. $H = 1011010100010$, 13 bits, so the total is $24 + 13 = 37$ bits, against 42 plain and $\lg \binom{100}{6} \approx 30.15$. $\text{select}_1(H, 4) = 5$, so the high part is $5 - 3 = 2$ and the value is $2 \cdot 16 + 8 = 40$.

7. Root $00110110110$; left node (for $i, m$) $10000$; right node (for $p, s$) $111100$. $\text{access}(6)$: the root bit is 1 and $\text{rank}_1 = 3$ before it; bit 3 of the right node is 1, so $s$. $\text{rank}_s(8)$: $\text{rank}_1(8) = 4$ at the root, then $\text{rank}_1(4) = 4$ in the right node, so 4. $\text{rank}_i(9)$: $\text{rank}_0(9) = 4$, then $\text{rank}_0(4) = 3$ in the left node, so 3.

10. Classes $2, 1, 4, 2$; offsets $2, 0, 0, 4$. The offsets take $\lceil \lg 6 \rceil + \lceil \lg 4 \rceil + 0 + \lceil \lg 6 \rceil = 8$ bits, so the total is $12 + 8 = 20$ bits, against $\lg \binom{16}{8} \approx 13.65$. The six blocks of class 2 in offset order are $1100, 1010, 0110, 1001, 0101, 0011$; so offset 4 is $0101$, offset 5 is $0011$, and class 1 offset 3 is $0001$.

11. For 30: $h = 1$, $p = 2$, index 1; pass $17$ and $18$; the answer is index 3, value 40. For 41: $h = 2$, $p = 5$, index 3; pass $40$; the answer is 63. For 64: $h = 4$, $p = 9$, index 5; the first element there, 97, is the answer.

14. $B_0 = 00110110110$ with $z_0 = 5$. After the stable reorder the sequence is $1, 0, 0, 0, 0, 3, 3, 3, 3, 2, 2$, so $B_1 = 10000111100$ with $z_1 = 6$. For a 1 bit, a position $j$ moves to $z_\ell + \text{rank}_1(B_\ell, j)$; for a 0 bit, to $\text{rank}_0(B_\ell, j)$. $\text{access}(6)$ reads 1 at level 0, moves to $5 + 3 = 8$, reads 1, so the code is $11$, which is $s$. For $\text{rank}_s(8)$ the pair $(0, 8)$ becomes $(5, 9)$ and then $(7, 11)$; the answer is $11 - 7 = 4$.

16. Cycles $(0\ 6\ 8\ 7\ 2)$, $(1\ 9\ 4\ 3\ 11\ 5)$ and $(10)$. Marks $0, 7, 1, 3$, with back pointers $0 \to 7$, $7 \to 0$, $1 \to 3$, $3 \to 1$; the bit vector is $110100010000$. To invert $x$, apply $\pi$ from $x$ until $\pi(y) = x$; the first time you reach a mark, jump along its back pointer once. For $4$: $4, 3$, jump to $1$, then $9$, and $\pi(9) = 4$. For $2$: $2, 0$, jump to $7$, and $\pi(7) = 2$. No query visits more than 4 positions. Space: $48 + 12 + 16$ bits.

19. Use $\binom{2k}{k} = \Theta(4^k / \sqrt{k})$ from Stirling's formula with $k = n - 1$, then divide by $n$.

20. At each node keep the range of positions as in rank; when the node's value range lies inside $[y_1, y_2)$ add the length of the current range and stop, and when it is disjoint stop with 0. At most two root-to-leaf paths are followed. Here the positions $1$ to $5$ hold $2, 7, 1, 4, 6$, and two of them, $2$ and $4$, lie in $[2, 6)$.

21. Induct on $c$. The blocks whose highest one is at position $p$ are exactly those with offsets in $[\binom{p}{c}, \binom{p+1}{c})$, since $\binom{p}{c}$ blocks of class $c$ fit in the positions below $p$ and the rest, by induction, are numbered $0$ to $\binom{p}{c-1} - 1$. Pascal's rule closes the gap.

22. At a node $v$ with $n_v$ symbols, $\lg \binom{n_v}{m_v} \le n_v H(m_v / n_v)$. Write $n_v$ as the sum of the counts of the symbols below $v$ and sum the entropies level by level: the chain rule of entropy makes the levels add up to $\sum_c n_c \lg(n / n_c) = n H_0(S)$.
