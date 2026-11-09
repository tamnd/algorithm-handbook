1. $\texttt{GGATCC}$, $\texttt{AAGCTT}$ and $\texttt{ACGCGT}$ are; $\texttt{GATTAC}$ is not, since its reverse complement is $\texttt{GTAATC}$. In odd length the middle base would have to be its own complement, and no base is.

2. The first $\lceil n/2 \rceil$ symbols determine the rest, so there are $\sigma^{\lceil n/2 \rceil}$. For binary strings: 8 of length 6 and 16 of length 7.

3. From left to right: $0, 1, 0, 3, 0, 1, 0, 7, 0, 1, 0, 3, 0, 1, 0, 1, 0$. The largest value is 7, at the center $\texttt{c}$, so the longest palindromic substring is $\texttt{abacaba}$.

4. Nine occurrences: the six single symbols, $\texttt{bcb}$, $\texttt{abcba}$ and $\texttt{bab}$. Six distinct palindromes: $\texttt{a}$, $\texttt{b}$, $\texttt{c}$, $\texttt{bcb}$, $\texttt{abcba}$, $\texttt{bab}$.

5. The longest palindromic prefix is $\texttt{aba}$, so the answer is $\texttt{dcabacd}$, of length $2 \cdot 5 - 3 = 7$. The prefix function at the last position of $\texttt{abacd\#dcaba}$ is 3.

6. The longest palindromic suffix of $\texttt{aabcb}$ is $\texttt{bcb}$, so the closure is $\texttt{aabcbaa}$. For $\texttt{abc}$ it is $\texttt{abcba}$.

7. Three partitions: $\texttt{a|a|b|a}$, $\texttt{aa|b|a}$ and $\texttt{a|aba}$. The palindromic length is 2.

8. Number the centers $0$ to $2n$, with symbol $k$ at center $2k + 1$. The substring $s[i..j]$ has center $i + j + 1$ and is a palindrome exactly when the value there is at least $j - i + 1$. So $s[1..5] = \texttt{bacab}$ is one (value 7 at center 7), $s[2..5] = \texttt{acab}$ is not (value 0 at center 8), and $s[4..6] = \texttt{aba}$ is one (value 3 at center 11).

9. With deletions only it is $n$ minus the longest palindromic subsequence. That subsequence has length 5, for example $\texttt{carac}$, so the answer is 4. With substitutions only, count the mirror pairs that differ: $\texttt{c/r}$, $\texttt{h/e}$, $\texttt{a/t}$, $\texttt{r/c}$, again 4.

10. There are $n(n+1)/2$ occurrences, since every substring is a palindrome, $n$ distinct nonempty palindromes, and $2^{n-1}$ partitions, since each of the $n - 1$ cut points is free. All three reach the largest value possible.

11. Besides the roots of lengths $-1$ and $0$ there are five nodes: $\texttt{a}$ and $\texttt{b}$, children of the root $-1$; $\texttt{aa}$, child of the root $0$ by $\texttt{a}$; $\texttt{aba}$, child of $\texttt{b}$ by $\texttt{a}$; and $\texttt{baab}$, child of $\texttt{aa}$ by $\texttt{b}$. The suffix links go from $\texttt{a}$ and $\texttt{b}$ to the empty root, from $\texttt{aba}$ and $\texttt{aa}$ to $\texttt{a}$, and from $\texttt{baab}$ to $\texttt{b}$. Five distinct nonempty palindromes in length 5 means the string is rich.

12. $\mathrm{PL}(s\,c) \le \mathrm{PL}(s) + 1$ by adding the piece $c$. For the other direction, take a best partition of $s\,c$; its last piece ends in $c$. Remove that $c$: if the piece is $c$ it disappears, if it is $c\,c$ it becomes $c$, and if it is $c\,q\,c$ it becomes the two palindromes $c$ and $q$. So $\mathrm{PL}(s) \le \mathrm{PL}(s\,c) + 1$.

13. At a symbol, the palindrome of radius $t$ exists with probability $\sigma^{-t}$, so a symbol center contributes about $1 + 1/\sigma + 1/\sigma^2 + \cdots = \sigma/(\sigma - 1)$ occurrences. A gap contributes about $1/(\sigma - 1)$. The total is about $n(\sigma + 1)/(\sigma - 1)$: $3n$ for binary strings and $5n/3$ for DNA.

14. Keep $F = \sum_k x_k B^{i-k}$ and $R = \sum_k x_k B^{k-1}$ modulo a prime, where $x_1 \ldots x_i$ is the string read so far. On a new symbol $c$, set $F \gets F B + c$ and $R \gets R + c\,B^{i}$, keeping $B^i$ in a variable. $R$ is the hash of the reversal under the same rule, so answer yes when $F = R$, which is wrong only on a hash collision.

15. Each center gives a maximal palindrome, and a palindrome with that center ends at $j$ exactly when the maximal one reaches $j$. The longest palindrome ending at $j$ uses the leftmost such center. As $j$ grows, the leftmost such center never moves left, so one pointer over the centers suffices. For $\texttt{abacabad}$: $1, 1, 3, 1, 3, 5, 7, 1$.

16. Removing the end symbols of a palindrome of length $L$ leaves one of length $L - 2$, so within one parity the answer "some palindrome of length $L$ exists" is monotone. Across parities it is not: $\texttt{abacaba}$ has palindromes of length 7 but none of length 2, 4 or 6.

17. A palindrome of length at least 2 has one of length 2 or 3 at its center, so the condition is $s[i] \ne s[i-1]$ and $s[i] \ne s[i-2]$ for all $i$. The first two symbols can be chosen in $3 \cdot 2 = 6$ ways and the rest are forced, so the answer is 6 for every $n \ge 2$. Over $\sigma$ symbols it is $\sigma(\sigma - 1)(\sigma - 2)^{n-2}$.

18. Suppose $s$ starts with an even palindrome $p$ of a valid partition, and let $x$ be the shortest even palindromic prefix. Show that if $x \ne p$, then $|x| \le |p|/2$: otherwise $x$ is a border of $p$ of more than half its length, and the period $|p| - |x|$ yields a shorter even palindromic prefix. Then $p = x\,u\,x$ with $u$ an even palindrome, possibly empty, so $p$ can be replaced by the pieces $x$, $u$, $x$, and the greedy step stays inside some valid partition.

19. For each of the $2n + 1$ centers, extend outward by jumps. An LCE query between the suffix of $s$ to the right of the center and the suffix of $s^R$ that starts at the mirror position gives the length of the next run of matching mirror pairs. Each mismatch costs one substitution, so each center needs at most $k + 1$ queries, and the queries take $O(1)$ time after linear preprocessing.

20. A maximal palindrome $s[l..r]$ at one center contains the palindromes $s[l+t..r-t]$, so it covers position $p$ exactly $\min(p - l, r - p) + 1$ times. This is a tent-shaped function of $p$; add it for each center with a second-order difference array, in $O(1)$ per center. For $\texttt{abcbab}$ the counts are $2, 3, 3, 4, 3, 2$.

21. If $s = u\,v$ with $u$, $v$ palindromes, then $s^R = v^R u^R = v\,u$, a rotation. Conversely, if $s = u\,v$ and $s^R = v\,u$, then $s^R = v^R u^R$, and comparing the first $|v|$ symbols gives $v = v^R$, then $u = u^R$. To test, search for $s^R$ in $s\,s$ with any linear-time matcher.
