1. The only nonempty border is $\texttt{abc}$, so the periods are $8 - 3 = 5$ and the trivial period 8. The smallest period is 5.

2. $\texttt{bc} \cdot \texttt{abc} \cdot \texttt{aab}$, and $\texttt{bc} > \texttt{abc} > \texttt{aab}$.

3. The least rotation is $\texttt{abbabc}$, starting at index 1. $\texttt{babcab}$ occurs in $\texttt{cabbabcabbab}$ at index 3, so it is the rotation of $\texttt{cabbab}$ by 3 places.

4. $\texttt{aab}$, $\texttt{abb}$, $\texttt{aabab}$ and $\texttt{aabb}$ are Lyndon words. $\texttt{aba}$ has the smaller rotation $\texttt{aab}$; $\texttt{abab}$ equals its rotation by 2, since it is not primitive; $\texttt{abaab}$ has the smaller rotation $\texttt{aabab}$.

5. $\texttt{aa}$, $\texttt{aba}$, $\texttt{bab}$ and $\texttt{bbb}$. The word $\texttt{aab}$ has the proper factor $\texttt{aa}$, which is already absent.

7. $\texttt{aa}$ at 2, $\texttt{bb}$ at 6, $\texttt{abab}$ at 3 and $\texttt{abaaba}$ at 0; each occurs once.

8. $\texttt{aabababab}$ $= a \cdot \texttt{abababa} \cdot b$, and $\texttt{abababa}$ is a palindrome. Every proper rotation starts with $\texttt{ab}$ or with $b$, so it is larger than the word, which starts with $\texttt{aa}$.

9. $L_4(6) = (4^6 - 4^3 - 4^2 + 4)/6 = 4020/6 = 670$. $N_4(4) = (4^4 + 4^2 + 2 \cdot 4)/4 = 280/4 = 70$.

10. $\texttt{ababaababa}$, or the same word with $a$ and $b$ exchanged. A word of length $11 = 5 + 7 - \gcd(5, 7)$ with both periods has the period 1, so it is one letter repeated.

11. $\lambda = 3, 1, 1, 5, 2, 1, 2, 1$. The first Lyndon factor is the longest Lyndon prefix, of length $\lambda[0] = 3$; the next one starts at 3 and has length $\lambda[3] = 5$. So the factorization is $\texttt{abb} \cdot \texttt{aabab}$.

12. The local periods at the cuts 1, 2, 3, 4 are $1, 5, 2, 2$. Only the cut 2, $\texttt{aa} \cdot \texttt{bab}$, is critical.

13. Greedy first merges $\texttt{abaab}$ and $\texttt{baaba}$ (overlap 4) into $\texttt{abaaba}$, then $\texttt{bbb}$ and $\texttt{bbaa}$ (overlap 2) into $\texttt{bbbaa}$, then these two (overlap 1), giving $\texttt{bbbaabaaba}$ of length 10. The order $\texttt{bbb}$, $\texttt{bbaa}$, $\texttt{baaba}$, $\texttt{abaab}$, with overlaps 2, 3 and 3, gives $\texttt{bbbaabaab}$ of length 9, which is shortest.

14. Four runs, with 0-based ends: $\texttt{bb}$ at $[1, 2]$ and at $[4, 5]$, period 1 and exponent 2; $\texttt{abbabbab}$ at $[0, 7]$, period 3 and exponent $8/3$; $\texttt{babab}$ at $[5, 9]$, period 2 and exponent $5/2$. So 4 runs, fewer than 10, and the exponents sum to $55/6 < 30$.

15. A bordered word has an unbordered border of length $j \le n/2$, its shortest one. For a fixed $j$, at most $k^{n-j}$ words have a border of length $j$, since the last $j$ letters copy the first $j$. So fewer than $k^n \sum_{j \ge 1} k^{-j} = k^n/(k - 1)$ words are bordered. For $k = 3$ more than half the words are unbordered; for $k = 2$ the bound says nothing.

16. From $x$, append the letters of $y$ one at a time; after $m$ steps you are at $y$. A path of $r < m$ edges from $a^m$ ends at a word that starts with $a^{m-r}$, so it does not reach $b^m$, and the diameter is $m$.

18. $\texttt{abbbab}$. Since $\texttt{aa}$, $\texttt{aba}$ and $\texttt{abba}$ are absent and $\texttt{bbbb}$ is absent, two consecutive letters $a$ are separated by exactly $\texttt{bbb}$; since $\texttt{babb}$ and $\texttt{aba}$ are absent, every $\texttt{ba}$ is followed by at most one letter. Of the words of length 6 that obey these rules, only $\texttt{abbbab}$ is left. The minimal absent words fix the set of factors, and the word is its own longest factor, so it is unique.

19. If each half has $i$ letters $a$, there are $\binom{n}{i}^2$ choices, and $\sum_i \binom{n}{i}^2 = \binom{2n}{n}$ by Vandermonde's identity. For $n = 2$: $\texttt{aaaa}$, $\texttt{abab}$, $\texttt{abba}$, $\texttt{baab}$, $\texttt{baba}$, $\texttt{bbbb}$.

21. If $uv = vu$, both are powers of one word $z$, and both sides equal $z^{ij}$ for $u = z^i$, $v = z^j$. Conversely, $x = u^{|v|} = v^{|u|}$ has the periods $|u|$ and $|v|$ and length $|u|\,|v| \ge |u| + |v| - 1$, since $(|u| - 1)(|v| - 1) \ge 0$. By Fine and Wilf it has the period $g = \gcd(|u|, |v|)$, so $u$ and $v$ are both powers of $x[0..g-1]$ and commute.

22. The word $t$ is a sequence of blocks $ab$ and $ba$ at even positions, so $\texttt{aa}$ and $\texttt{bb}$ occur only at odd positions. A factor of length 5 without $\texttt{aa}$ or $\texttt{bb}$ is $\texttt{ababa}$ or $\texttt{babab}$, an overlap, which $t$ does not contain. So if $|u| \ge 5$, the factor $u$ contains $\texttt{aa}$ or $\texttt{bb}$ at some offset $r$, at the positions $i + r$ and $i + |u| + r$ in $uu$, which have different parities when $|u|$ is odd. Examples: $\texttt{bb}$ at position 1 and $\texttt{babbab}$ at position 11, counting from 0.

23. Make the letters vertices and the strings edges of a directed multigraph. In a superstring, the adjacent pairs that belong to $S$ form walks that together use every edge, and $t$ walks with $e$ edges in all need at least $e + t$ letters. Using an edge twice costs a letter and saves at most one walk, so the shortest length is $|S|$ plus the least number of trails that cover every edge once. In each weakly connected component that number is $\max(1, \sum_v \max(0, \mathrm{out}(v) - \mathrm{in}(v)))$. In the example only $a$ has more out-edges than in-edges, by one, so the length is $6 + 1 = 7$, for instance $\texttt{abdbcad}$.

24. Every word with $j$ letters $b$ is $\rho^e$ for a primitive $\rho$ of length $n/e$ with $j/e$ letters $b$, where $e$ divides $\gcd(n, j)$, and each primitive class has $n/e$ rotations. This gives $\binom{n}{j} = \sum_{e \mid \gcd(n, j)} (n/e)\,L(n/e, j/e)$; invert it with the Möbius function. For necklaces, count words fixed by each rotation, as in Burnside's lemma. The values are $(\binom{8}{4} - \binom{4}{2})/8 = 8$ and $(\binom{6}{3} + 2\binom{2}{1})/6 = 4$.
