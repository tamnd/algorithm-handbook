1. $(0, 0, a)$, $(0, 0, b)$, $(0, 0, c)$, $(3, 6, d)$. The copy writes positions 3 to 8 from positions 0 to 5, so it reads 3 symbols, those at positions 3, 4 and 5, that it has just written.

3. Seven copies of `a`. The decoder receives an undefined code twice, at 256 and at 257; each time the code is the one it is about to define, and the string is the previous string plus its own first symbol.

4. $\mathrm{LPF} = 0, 1, 0, 4, 3, 2, 2, 1$. The factorization takes $\max(1, \mathrm{LPF}[i])$ symbols at each start $i$: `a`, `a`, `b`, `aaba`, `b`, so $z = 5$.

6. Greedy takes `abc` and then `def`: two copies, 34 bits. Lazy matching sees that the match at `b` (`bcdef`, 5 symbols) is longer than the one at `a` (3), so it writes `a` as a literal and then one copy: 26 bits.

8. $(2 \cdot 5 + 2) \cdot 9 + 0 = 108$, the byte 6C. There are $2^{lc + lp} = 4$ tables of 768 probabilities, 3072 in all.

10. Greedy: `ab`, `c`, `ab`, `c`, `a`, five phrases. $C[7..0] = 0, 1, 2, 1, 2, 3, 2, 3$, read from $i = 7$ down to $i = 0$. An optimal parse is `a`, `bca`, `bca`.

12. Phrase $k$ is an earlier phrase $j < k$ plus one symbol, so by induction its length is at most $k$; so $n \le c(c + 1)/2$. For $a^{100}$ the phrases have lengths $1, 2, \ldots, 13$ and then 9: 14 phrases, and LZW also writes 14 codes, for the strings $a, a^2, \ldots, a^{13}, a^9$.

14. A literal `a` costs 8 bits, the end-of-block code 7, a copy of 258 at distance 1 costs $8 + 5 = 13$ bits, and one of 257 costs $8 + 5 + 5 = 18$. So 259 copies cost $3 + 8 + 13 + 7 = 31$ bits, 517 cost $3 + 8 + 2 \cdot 13 + 7 = 44$ bits, and 516 cost at least $3 + 8 + 13 + 18 + 7 = 49$ bits, since 515 is not a sum of two copies of 258.

15. The lengths of the nonterminals form an [addition chain](/addition-chain/): each is the sum of two earlier ones, starting from 1. The chain $1, 2, 3, 6, 12, 15$ gives 6 rules. With 4 binary rules, 15 must be the sum of two members of a chain $1, a_2, a_3, a_4$ with $a_4 \le 8$. That needs $8 + 7$, but $a_4 = 8$ forces the chain $1, 2, 4, 8$, which has no 7. So 6 is the minimum, one more than the bound $15 \le 2^{m-1}$ requires.

20. All phrases but the last are distinct, and there are at most $\sigma^j$ phrases of length $j$. Take $k$ with $S_k < c \le S_{k+1}$, where $S_k = \sigma + \cdots + \sigma^k$. The total length is at least the length of the $c - 1$ shortest distinct strings, which gives $n \ge (c/2)(\log_\sigma(c/2) - 1)$ up to lower-order terms; solve for $c$.

21. A factorization with $j$ factors is fixed by $j$ descriptions, each a new symbol or a pair of a source position and a length, so at most $2n^2$ choices each. Fewer than $(2n^2)^{k+1}$ strings have at most $k$ factors, and this is below $2^{n-1}$ when $(k + 1)(1 + 2 \log_2 n) < n - 1$, which holds for $k = n / (3 \log_2 n)$ and large $n$. So $z = \Theta(n / \log n)$ for most strings.

22. Take the leftmost occurrence of a substring. If it contains no last position of a factor, it lies inside one factor and avoids that factor's last position, so the factor has length at least 2 and is a copy of an earlier occurrence. Shift the substring back by the copy's distance: an earlier occurrence, a contradiction.

23. Each distinct substring of length $\ell$ has an occurrence that contains a position $p \in \Gamma$, and it is fixed by $p$ and by the offset of $p$ in it, one of $\ell$ values. A string of $n$ distinct symbols has $z = n$ and $n$ distinct symbols.

24. The length of the string of a nonterminal is at most the length of its right-hand side times the longest string among the symbols on it, so $n$ is at most the product of the right-hand side lengths. A product of positive integers with sum $g$ is at most $3^{g/3}$. For $a^{3^k}$ the rules $X_1 \to aaa$ and $X_{i+1} \to X_i X_i X_i$ have size $3k$, and the bound gives $g \ge 3k$, so the smallest size is $3k$.
