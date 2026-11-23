1. $89 = 1011001_2$, so the costs are $2, 1, 2, 2, 1, 1, 2$. The total is 11: 7 squarings and 4 multiplications by the base.

2. (a) $31 - 20 = 11$. (b) The top bit is 1, so 10 of the other 19 bits are 1: $\binom{19}{10} = 92378$ exponents. The reading gives away $\log_2(2^{19}/92378) \approx 2.5$ bits.

3. The ladder costs $2$ for each of the 8 bits, 16 in all. Square and multiply does 8 squarings, 1 multiplication for the top bit and $7/2$ on average for the others: 12.5. The ratio is $16/12.5 = 1.28$.

4. $2^{252}/2^{256} = 1/16$ of the signatures, so about $16 \cdot 100 = 1600$ signatures.

5. Each S followed by M is a 1 bit and each S followed by S, or last, is a 0 bit: S M, S, S, S M, S M, S M, S gives $1001110_2 = 78$. The sequence has $k + h$ operations.

6. $8 \cdot 2^6 = 512$ guesses give the round key, and $2^8 = 256$ trials give the other 8 key bits: fewer than 800 tests, against $2^{56} \approx 7.2 \times 10^{16}$.

7. For $12_{16}$ and $16_{16}$: $d = 04_{16}$, $0 - d = \mathrm{FC}_{16}$, $d \mid (0 - d) = \mathrm{FC}_{16}$, its top bit is 1 and $\mathrm{EQ} = 0$. For $x = y$: $d = 0$, the OR is 0 and $\mathrm{EQ} = 1$. If $d \ge 2^7$ its own top bit is set; if $0 < d < 2^7$, then $0 - d = 2^8 - d > 2^7$ has it set; if $d = 0$ both are 0.

8. $20000 \cdot 6.8 \times 10^{-6} \approx 0.136$ expected false alarms, and $1 - (1 - 6.8 \times 10^{-6})^{20000} \approx 0.127$. With two sets, $20000 \cdot 4.6 \times 10^{-11} \approx 9.2 \times 10^{-7}$.

9. (a) $0.0085 / (0.0085 + 0.006 \cdot 0.99) \approx 0.589$. (b) The false positive rate must be $0.85 \cdot 0.001 \cdot (1/0.9 - 1)/0.999 \approx 9.5 \times 10^{-5}$, about 0.0095 percent, more than sixty times below 0.6 percent.

11. (a) $13 \cdot 5 = 65 \equiv 1 \pmod{16}$, so $n' = -5 \bmod 16 = 11$. (b) For $(7, 11)$: $t = 77$, $m = 15$, $u = 272/16 = 17 \ge 13$, so the extra reduction happens and the result is 4. For $(3, 4)$: $t = 12$, $m = 4$, $u = 64/16 = 4$, no extra reduction, result 4. (c) 20 of the 169 pairs.

14. Bit 2 gives the scores $0.5, 1.0, -0.5, 0, -0.5, 0, 0.5, -1.0, 0.5, -1.0, 0, 1.0, 0, 0, -0.5, 0$ for $g = 0, \dots, \mathrm{F}$: the guess 1 ties with B. Bit 3 gives $-0.5, 0.75, 0.75, -0.75, -1.0, 0.5, 0.75, -0.5, 0.75, -0.5, 0, 1.0, 0.25, -0.75, -1.0, 0.25$: B leads the guesses 1, 2, 6 and 8 by 0.25, but by absolute value the guesses 4 and E tie with it.

21. Since $\gcd(e, \varphi(N)) = 1$, the map $r \mapsto r^e$ is a bijection on the units; multiplication by the unit $c$ is another. So $c\, r^e$ is uniform for every $c$. The number of extra reductions is a function of the blinded input and $d$ alone, so its distribution does not depend on $c$.

22. After a wrong bit, the simulated intermediate values are wrong, so the predictions of which inputs make a step slow are unrelated to the device. Both guesses for every following bit then give two sets with equal means. When neither guess shows a difference, the attacker goes back to the last bit and flips it, as Kocher observed.

23. Write $\log \mathcal{N}(x; \mu, \Sigma) = -\frac12 (x - \mu)^{\mathsf T} \Sigma^{-1} (x - \mu) - \frac12 \log\det\Sigma + \text{const}$. With one $\Sigma$, the term $x^{\mathsf T} \Sigma^{-1} x$ and the determinants cancel in the difference, which leaves $(\mu_a - \mu_b)^{\mathsf T} \Sigma^{-1} x$ plus a constant. With $\Sigma_a \ne \Sigma_b$ the term $-\frac12 x^{\mathsf T} (\Sigma_a^{-1} - \Sigma_b^{-1}) x$ stays. Summed over $m$ traces of one class, the pooled difference depends on the traces only through their sum, so averaging them first loses nothing.

25. (a) Every share is uniform and every two shares are uniform and independent of $x$; the noise has mean 0 and is independent of the rest. (b) For a bit, $s - \frac12 = -\frac12 (-1)^s$, so the product of the three is $-\frac18 (-1)^{s_1 \oplus s_2 \oplus s_3} = -\frac18 (-1)^x$; every term with a noise factor has mean 0. (c) $(\ell_i - \frac12)^2 = \frac14 + 2(s_i - \frac12)N_i + N_i^2$, and every term of the product with a single factor $N_i$ has mean 0, so the second moment is $(\frac14 + \sigma^2)^3$. The two means differ by $\frac14$, so the traces needed grow as $(\frac14 + \sigma^2)^3$, about $\sigma^6$; with two shares the same argument gives $\sigma^4$.

26. (a) The pair $(7, \mathrm{E})$ allows $\{2, 7, \mathrm{B}, \mathrm{E}\}$, the pair $(1, 6)$ allows $\{9, \mathrm{B}, \mathrm{C}, \mathrm{E}\}$, and both leave $\{\mathrm{B}, \mathrm{E}\}$. (b) With $g = k \oplus 5$, $S^{-1}(y \oplus g) = f(u)$ and $S^{-1}(y^* \oplus g) = f(u \oplus 1) = f(u) \oplus 1$, and a check of the 16 values of $u$ confirms the identity; so no number of faults on bit 0 separates B from E. (c) The pair $(\mathrm{D}, 4)$ allows $\{2, \mathrm{B}\}$, which leaves B.
