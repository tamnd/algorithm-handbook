2. The array is $\langle 6, 7, 3, 4, 5 \rangle$ with $h = 2$ and $n = 5$, and GET$(B, 3)$ reads cell $(2 + 3) \bmod 5 = 0$, which holds 6. The two-index form holds at most $N - 1$ items. The difference $(t - h) \bmod N$ takes only $N$ values, but the count can be any of $0, \ldots, N$, so a full buffer and an empty one would look the same. One cell is left unused to tell them apart.

3. The resizes happen at $n = 1, 2, 4, 8, 16$ and copy $1 + 2 + 4 + 8 + 16 = 31$ items, and $cap = 32$. The first shrink comes when $n$ drops to $32/4 = 8$, after 9 pops, and it leaves $cap = 16$.

4. The deletes return $b$, $e$, $a$ and $f$, and $\langle c, d, g \rangle$ is left.

5. $A$: $0 \oplus \text{0x20} = \text{0x20}$. $B$: $\text{0x10} \oplus \text{0x30} = \text{0x20}$. $C$: $\text{0x20} \oplus \text{0x40} = \text{0x60}$. $D$: $\text{0x30} \oplus 0 = \text{0x30}$. Two nodes have the same field, so a field alone does not say where a node is.

7. `a b + c * d e f g ^ ^ / -`. The two `^` stay on the stack together because `^` is right-associative, and both leave before `/`.

8. The answers are $8, 9, 6, 6, 9, 9$ and none for the last two. The scan pops 6 times, and 9 and 5 stay on the stack: they are the items with no greater item after them.

9. The outputs are $1, 1, 2, 2, 2, 3$, and the deque ends with $(6, 3)$ and $(7, 8)$.

10. Move-to-front pays $3 + 1 + 5 + 3 + 2 + 4 = 18$ and ends with $b, e, a, c, d$. Transpose pays $3 + 2 + 5 + 2 + 4 + 4 = 20$ and ends with $a, c, b, e, d$. The fixed list pays 19.

11. The sequence is $0, 2, 6, 12, 3, 11, 6, 12, 3$, so $\mu = 2$ and $\lambda = 4$. They meet after 4 steps, at $x_4 = x_8 = 3$; 4 is the least multiple of $\lambda$ that is at least $\mu$.

12. Five: `a b ∘ c ∘ d ∘`, `a b ∘ c d ∘ ∘`, `a b c ∘ ∘ d ∘`, `a b c ∘ d ∘ ∘` and `a b c d ∘ ∘ ∘`. Each valid string is the postorder of one binary tree with $n$ leaves, so the count is the Catalan number $C_{n-1} = \binom{2n-2}{n-1}/n$.

13. $E_{\mathrm{MTF}} = 1 + 2\,(1/5 + 1/8 + 1/9) = 337/180 \approx 1.872$. $E_{\mathrm{OPT}} = 1/2 + 2/3 + 3/6 = 5/3 \approx 1.667$, and the bound is $7/3$.

17. Floyd's first phase makes 3 evaluations per step, 12 in all; the second phase makes 2 per step for $\mu = 2$ steps, and the third makes $\lambda = 4$, so 20 in total. Brent's first part makes 7 evaluations and finds $\lambda = 4$; lines L8 and L10 add 4 and 4, so 15 in total.

19. MOVE-TO(2) moves C, D, E and F one by one to the right end, so $g = 2$ and $e = 4$. X and Y fill the gap. Z finds $g = e$, and GROW copies the 4 items before the gap and the 4 after it into an array of 16 cells, with $e = 12$. At the end $g = 5$, $e = 12$, $cap = 16$, the text is ABXYZCDEF, and $4 + 8 = 12$ items were moved.

20. $2\,4\,3\,1$ and $1\,3\,2\,4$ can come out. In $4\,1\,2\,3$ and in $3\,1\,2\,4$, once the first item is popped, 1 and 2 are both on the stack with 2 on top, so 1 cannot come out before 2. A permutation can be made if and only if it has no $i < j < k$ with $p_j < p_k < p_i$, and 14 of the 24 permutations pass, the Catalan number $C_4$.

24. Only the four named nodes change. Their new fields are $p.np \oplus a \oplus b$, $a.np \oplus p \oplus q$, $b.np \oplus p \oplus q$ and $q.np \oplus a \oplus b$. A node strictly inside the run keeps its two neighbours, and XOR does not care which one is first, so its field stays right.

25. Keep the front part on stack $L$ and the back part on stack $R$. When a pop finds its stack empty and the other holds $k$ items, use the scratch stack to split those $k$ items into two halves, one on each side, in $O(k)$ steps. With $\Phi = c\,\lvert |L| - |R| \rvert$, each push or pop raises $\Phi$ by at most $c$, and a split lowers it from $ck$ to at most $c$, which pays for the split.

26. COUNT never changes the list, so the requests for $x_i$ cost $i$ each, and the total is $k \sum_i i\,(n - i + 1) = k\,n(n+1)(n+2)/6$. Move-to-front pays $i$ for the first request of each block and 1 for the others, $k\,n(n+1)/2 + n(n-1)/2$ in total. Since OPT is at most the cost of move-to-front, the ratio of COUNT to OPT tends to at least $(n + 2)/3$ as $k$ grows, which exceeds every constant $c$ once $n > 3c - 2$.

27. Block $b$, counting from 0, holds $b + 1$ items and starts at item $b(b+1)/2$. With $k$ blocks in use, $(k-1)k/2 < n$, so $k < \sqrt{2n} + 1$: the last block wastes fewer than $k$ cells and the index holds $k$ pointers. Item $i$ is in block $b = \lfloor (\sqrt{8i + 1} - 1)/2 \rfloor$ at offset $i - b(b+1)/2$. Append writes into the last block or starts a new one; keep the index as a dynamic array, whose copies cost $O(1)$ amortized per append.

29. After $i$ steps the tortoise is at $x_i$ and the hare at $x_{2i}$. They are equal exactly when $x_i$ is on the cycle, that is $i \ge \mu$, and $\lambda$ divides $2i - i = i$. Among the $\lambda$ numbers $\max(\mu, 1), \ldots, \max(\mu, 1) + \lambda - 1$ one is a multiple of $\lambda$, which gives $\nu \le \mu + \lambda$. In the second phase, after $j$ steps the pointers are at $x_j$ and $x_{\nu + j}$; for $j \ge \mu$ these are equal because $\nu$ is a multiple of $\lambda$, and for $j < \mu$ the value $x_j$ is in the tail and never appears again.
