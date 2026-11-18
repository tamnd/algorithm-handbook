1. $89 = 1011001_2$, so the costs are $2, 1, 2, 2, 1, 1, 2$. The total is 11: 7 squarings and 4 multiplications by the base.

2. (a) $31 - 20 = 11$. (b) The top bit is 1, so 10 of the other 19 bits are 1: $\binom{19}{10} = 92378$ exponents. The reading gives away $\log_2(2^{19}/92378) \approx 2.5$ bits.

6. (a) $13 \cdot 5 = 65 \equiv 1 \pmod{16}$, so $n' = -5 \bmod 16 = 11$. (b) For $(7, 11)$: $t = 77$, $m = 15$, $u = 272/16 = 17 \ge 13$, so the extra reduction happens and the result is 4. For $(3, 4)$: $t = 12$, $m = 4$, $u = 64/16 = 4$, no extra reduction, result 4. (c) 20 of the 169 pairs.

7. (a) For 157 the windows are $10, 01, 11, 01$: costs $3, 3, 3, 3$ and indices $2, 1, 3, 1$. For 135 they are $10, 00, 01, 11$: costs $3, 2, 3, 3$ and indices $2, 0, 1, 3$. (b) The costs show only which windows are zero. The addresses give every window, so the whole exponent.

10. Since $\gcd(e, \varphi(N)) = 1$, the map $r \mapsto r^e$ is a bijection on the units; multiplication by the unit $c$ is another. So $c\, r^e$ is uniform for every $c$. The number of extra reductions is a function of the blinded input and $d$ alone, so its distribution does not depend on $c$.

11. After a wrong bit, the simulated intermediate values are wrong, so the predictions of which inputs make a step slow are unrelated to the device. Both guesses for every following bit then give two sets with equal means. When neither guess shows a difference, the attacker goes back to the last bit and flips it, as Kocher observed.
