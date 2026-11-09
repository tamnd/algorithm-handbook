1. $1000 + 500 + 250 + 125 + 62 + 31 + 15 + 7 + 3 + 1 = 1994$. This is $2n - s_2(n)$, where $s_2(1000) = 6$ is the number of 1 bits of 1000.

2. The powers of 2 up to $n$ cost less than $2n$ together, and the other operations cost at most $n$.

3. The copies happen at appends 2, 3, 5, 9 and 17 and copy $1 + 2 + 4 + 8 + 16 = 31$ items, so the total is $17 + 31 = 48$. The ratio is largest at $n = 2^k + 1$, just after a doubling, where the total is $n + 2^{k+1} - 1 = 3n - 3$.

4. Each increment has amortized cost at most 2 with this potential, and the total is at most $2n + \Phi_0 - \Phi_n \le 2n + b$. Starting at $2^k - 1$, the first increment alone flips $k + 1$ bits.

5. (a) amortized; (b) expected; (c) expected amortized; (d) amortized; (e) worst-case.

6. It copies $2^{20}$ items. The old array of $2^{20}$ items and the new one of $2^{21}$ are both allocated during the copy, $3 \cdot 2^{20}$ items or 24 MiB.

7. Actual costs $1, 1, 1, 2, 1, 2$, total 8; potentials after each operation $1, 2, 3, 1, 2, 0$; amortized costs $2, 2, 2, 0, 2, 0$, total 8. Here $\Phi$ starts and ends at 0, so the totals are equal.

8. Go to $2^{k-1}$, then alternate DECREMENT and INCREMENT. Each step flips all $k$ bits between $1000\cdots0$ and $0111\cdots1$.

10. Bit $i$ flips $\lfloor n/2^i \rfloor$ times at cost $2^i$, which is between $n - 2^i$ and $n$, for each of the $\lfloor \lg n \rfloor + 1$ bits that change.

14. Increment from $0111\cdots1$ to $1000\cdots0$ and undo, again and again. Amortized bounds charge an expensive operation to the cheap ones before it; a structure that can return to an old state lets the expensive operation be repeated without them.

16. Let $x$ be at position $k$ in the move-to-front list and $i$ in $L$, and let $v$ items precede $x$ in both lists. Moving $x$ to the front creates $v$ inversions and removes $k - 1 - v$, so the amortized cost is $k + 2v - k + 1 = 2v + 1 \le 2i - 1$.

17. Take $\Phi$ to be the number of nonzero digits. An increment that carries through $t$ digits equal to 1 turns them into 0 and changes one more digit, so its amortized cost is at most $(t + 1) - t + 1 = 2$. Decrement is the same with $-1$.

18. The $c$ old items are copied after $c/2$ appends, when the new array holds $1.5c$ items. Index $i < c$ is read from the old array if it is not yet copied, and from the new array otherwise. At most $3c$ cells are in use.
