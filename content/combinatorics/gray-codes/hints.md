1. $45 = 101101_2$ and $\lfloor 45/2 \rfloor = 010110_2$, so $g(45) = 111011$. For $110110$ take the prefix exclusive or from the left: $b = 100100_2 = 36$. Check: $36 \oplus 18 = 54 = 110110_2$.

2. After $s = 1$ the word is $11101110$, after $s = 2$ it is $11010101$, and after $s = 4$ it is $11011000$, so the rank is 216. Check: $216 \oplus 108 = 180 = 10110100_2$.

5. $j = f_0 = 1$, so bit 1 flips and the string becomes $01001$, the string of rank 14. The pointers become $f_0 = 0$, $f_1 = f_2 = 4$, $f_2 = 2$, that is $(0, 4, 2, 3, 4, 5)$.

8. $14 = 112_3$. In the reflected code $\lfloor 14/27 \rfloor = 0$ is even, so the top digit stays 1; $\lfloor 14/9 \rfloor = 1$ is odd, so the middle digit becomes $2 - 1 = 1$; $\lfloor 14/3 \rfloor = 4$ is even, so the last digit stays 2. The string is $112$. The modular code gives $1$, $(1 - 1) \bmod 3 = 0$ and $(2 - 1) \bmod 3 = 1$, so $101$.

9. $C_{22} = B_{22}$, since $n = 4$ is even: $1100, 1001, 1010, 0110, 0101, 0011$. The first step moves a 1 from position 2 to position 0, over a 0. The last string $0011$ differs from $1100$ in four bits, so the list is not cyclic.

11. The shift is linear over $\oplus$, so $g(g(k)) = k \oplus (k \gg 1) \oplus (k \gg 1) \oplus (k \gg 2)$ and the middle terms cancel; $g(g(4)) = 5$. Write $g = 1 + x$ with $x$ the shift; over GF(2), $(1 + x)^{2^m} = 1 + x^{2^m}$. So $g$ applied $2^m$ times is the identity on $n$-bit words exactly when $2^m \ge n$, and the order of $g$ divides that power of 2. The answers are 8 for 8-bit words and 16 for 9-bit words.

12. Use $g(i) \oplus g(j) = g(i \oplus j)$. The strings differ in all six bits exactly when $g(i \oplus j) = 111111$, that is $i \oplus j = 101010_2 = 42$. So $j - i = \pm 32 \pm 8 \pm 2$, and the smallest absolute value is $32 - 8 - 2 = 22$.

14. Color a string by the parity of $d_1 + d_0$. Each step changes the color, and there are five even strings and four odd ones, so a path through all nine starts and ends at an even string. The ends from $00$ are $02$, $11$, $20$ and $22$, and each occurs. A cycle through nine strings would need as many even strings as odd ones.

20. Every bit must change, and an even number of times around a cycle, so the counts are a permutation of $(4, 2, 2)$. The bit that changes four times uses all four edges in its direction. The other four edges of the cycle form a perfect matching on each of the two faces across that direction. Each face has two such matchings, and only the two mixed choices give one cycle of length 8, not two of length 4. That gives $3 \times 2 = 6$.

21. One direction is the parity argument, since $Q_n$ is bipartite by weight. For the other, use induction on $n$. Pick a bit $i$ in which $u$ and $v$ differ and split $Q_n$ into the two halves by bit $i$. In the half of $u$ pick $x$ of weight parity opposite to $u$. Join a path from $u$ to $x$ in that half, the edge from $x$ to $x \oplus e_i$, and a path from $x \oplus e_i$ to $v$ in the other half, which exists because $x \oplus e_i$ and $v$ have opposite parity.

22. From $r$ to $r + 1$ the trailing digits equal to $k - 1$ become 0 and the next digit $b_i$ grows by 1. For every $j < i$ both $b_j$ and $b_{j+1}$ grow by 1 modulo $k$, so their difference does not change. Only digit $i$ changes, by $+1$. The last string is $(k-1)0 \cdots 0$, one step from $0 \cdots 0$. Focus pointers that track the trailing run of digits $k - 1$ find $i$ in $O(1)$ time.

23. The signed count is the coefficient of $x^k$ in $\prod_{i=1}^n (1 + (-1)^i x) = (1 - x)^{\lceil n/2 \rceil} (1 + x)^{\lfloor n/2 \rfloor}$. For $n$ even this is $(1 - x^2)^{n/2}$, and for $n = 2m + 1$ it is $(1 - x)(1 - x^2)^m$. The absolute value is $\binom{n/2}{k/2}$ for $n$ and $k$ even, 0 for $n$ even and $k$ odd, and $\binom{m}{\lfloor k/2 \rfloor}$ for $n = 2m + 1$. It is at least 2 exactly when $2 \le k \le n - 2$ and $k$, $n - k$ are not both odd.

24. The multisets are $\{2, 2, 4, 8\}$, $\{2, 2, 6, 6\}$, $\{2, 4, 4, 6\}$ and $\{4, 4, 4, 4\}$. The missing one is $\{2, 4, 4, 6\}$. Rearrange the second half of $\Gamma_4$: $0000, 0001, 0011, 0010, 0110, 0111, 0101, 0100, 1100, 1101, 1001, 1011, 1111, 1110, 1010, 1000$ has counts $(6, 4, 4, 2)$ from bit 0.
