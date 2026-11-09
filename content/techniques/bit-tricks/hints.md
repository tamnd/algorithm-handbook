1. $-1 = 11111111_2$, $-37 = 11011011_2$ (invert $00100101_2$ and add 1), $-128 = 10000000_2$. The pattern $10110100_2$ is 180 unsigned and $180 - 256 = -76$ signed.

6. For 37: $y = 00100100_2$, then $00110110_2$, $00111111_2$, $00111111_2$, and the result is 64. For 200: $y = 11000111_2$, then $11100111_2$, $11111111_2$, $11111111_2$, and $y + 1$ wraps to 0. The true answer, 256, does not fit in 8 bits.

8. $\lceil 10000 / 64 \rceil = 157$ words. A field crosses a boundary when its offset $10i \bmod 64$ exceeds 54; among $0, \ldots, 31$ these are $i = 6, 12, 19, 25$, with offsets 60, 56, 62, 58. The offsets repeat with period 32, so the count up to 999 is $31 \cdot 4 + 1 = 125$, the last one being $i = 998$.

10. After the pass for bit 0: $\langle 2, 9, 1, 9, 2, 10, 1, 9 \rangle$. After bit 1: $\langle 2, 9, 3, 18, 2, 10, 3, 19 \rangle$. After bit 2: $\langle 2, 9, 3, 18, 4, 19, 6, 37 \rangle$, and the last entry is the sum of all of $f$.

11. $00111$, $01011$, $01101$, $01110$, $10011$, $10101$, $10110$, $11001$, $11010$, $11100$: ten subsets, $\binom{5}{3}$. One more call returns $100011_2 = 35$, which has a bit outside the 5-bit universe, so the loop must stop when $x \ge 2^5$.

12. If $x$ ends in a 1 followed by $t$ zeros, then $x - 1$ ends in a 0 followed by $t$ ones and agrees with $x$ above, so the XOR is $2^{t+1} - 1$. For $x = 0$ the XOR is all ones and the formula gives 31, while $\nu(\overline{x} \wedge (x - 1))$ gives 32, the usual convention.

13. $y = 11011000_2$. A Gray code word $g$ of the binary number $b$ satisfies $g = b \oplus (b \gg 1)$, so $b_i = g_i \oplus b_{i+1}$, which unrolls to the parity of $g_i, \ldots, g_7$.

17. $c = \langle 0, 1, 1, 1, 1, 0, 1, 0 \rangle$ and $F = \langle 0, 1, 1, 3, 1, 2, 3, 5 \rangle$. The sum $\sum_i F[7 \oplus a_i]$ is 10 and counts each pair twice, so there are 5 pairs. If the array has $z$ zeros, each zero also counts itself, so subtract $z$ before halving.

18. Each pass of the subtraction undoes the matching pass of the addition, because pass $i$ changes only the masks with bit $i$ set and reads only masks without it, which that pass leaves alone; passes for different bits commute. Here $f = \langle 1, 2, 3, 4, 4, 5, 5, 6 \rangle$.

19. Each lane of $x \wedge L$ and $y \wedge L$ is at most 127, so their sum is at most 254 and the carry stops at bit 7 of the lane. The XOR then adds the two top bits modulo 2. The lane sum is `0x0000`; the plain sum is `0x0100`, because the carry out of the low byte enters the high one.

22. 70000 has key 1 and low part 4464; 5 has key 0 and low part 5; 131071 has key 1 and low part 65535; 65536 has key 1 and low part 0. Two array containers: key 0 holds $\{5\}$ and key 1 holds $\{0, 4464, 65535\}$. The first chunk is one run of 4 bytes; the second is a bitmap of 8192 bytes, since an array would take 65536 bytes and runs 131072; the third is an array of 6000 bytes.

24. Write $x = \sum_i b_i 2^i$; then $\lfloor x / 2^k \rfloor = \sum_{i \ge k} b_i 2^{i-k}$, and summing over $k \ge 1$ gives $\sum_i b_i (2^i - 1) = x - \nu(x)$.

25. $F_h[m]$ sums $f[a] g[b]$ over the pairs with $a \vee b \subseteq m$, which are the pairs with $a \subseteq m$ and $b \subseteq m$, so the sum factors. Transform both, multiply pointwise, and invert. Here $F_f = \langle 1, 3, 1, 4 \rangle$, $F_g = \langle 0, 1, 1, 3 \rangle$, the product is $\langle 0, 3, 1, 12 \rangle$, and $h = \langle 0, 3, 1, 8 \rangle$.

26. Count the $k$-subsets that come before: those whose largest element is below $c_k$ number $\binom{c_k}{k}$, and those with largest element $c_k$ that come before are counted by the same rule on $\{c_1, \ldots, c_{k-1}\}$. For $\{1, 2, 4\}$ the position is $\binom{1}{1} + \binom{2}{2} + \binom{4}{3} = 6$.

27. Compare the highest bit $j$ of $a$ with the highest bit of $b$. If $b$ has its highest bit above $j$, both inequalities hold; if the highest bit of $b$ is also $j$, then $a \oplus b$ is below $2^j$ and so smaller than $a$; if $b$ has no bit at or above $j$, then $a > b$. For points, let $d_x = x_1 \oplus x_2$ and $d_y = y_1 \oplus y_2$: when $\operatorname{less}(d_y, d_x)$, the $x$ coordinates decide; otherwise the $y$ coordinates do, because $y$ holds the higher bit of each level.

28. The four constants are `0x17`, `0x1D`, `0x2E` and `0x3A`. The windows of the scan are the windows of the string $D\,0^{\lg w - 1}$ of length $w + \lg w - 1$, so this string must hold each 3-bit word once. A string with that property ends with the same $\lg w - 1$ bits it begins with, so $D$ begins with $\lg w - 1$ zeros, and then the windows are the cyclic windows of $D$. Each de Bruijn cycle has two such rotations, so for $w = 16$ there are $2 \cdot 16 = 32$.
