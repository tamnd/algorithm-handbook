1. $(100, 21, 3)$ and $(64, 13, 7)$ have full period. $(100, 11, 7)$ breaks condition (iii), since $4 \mid 100$ but $a - 1 = 10$ is not divisible by 4, and its period is 50. $(64, 13, 8)$ breaks condition (i), since $\gcd(8, 64) \ne 1$, and its period is 8.

2. Write $65536 = 65 \cdot 1000 + 536$. The values $0, \ldots, 535$ have probability $66/65536$ and the values $536, \ldots, 999$ have $65/65536$. The distance is $536 \cdot 464 / (1000 \cdot 65536) = 1943/512000 \approx 0.0038$. Rejection keeps $W < 65000$ and uses $65536/65000 \approx 1.008$ words per output.

4. The cycles have lengths 6, 6 and 3. The polynomial is $(x^2 + x + 1)^2$, which is not primitive, so no cycle can hold all 15 states.

5. The pairs are 01, 11, 10, 01, 00, 10, 11, and the output is 0, 1, 0, 1. A pair gives a bit with probability $2p(1-p) = 0.18$, so one bit costs $2/0.18 \approx 11.1$ flips. The bound is $h(0.9) \approx 0.469$ bits per flip, against von Neumann's $0.09$.

8. The states are 9, 4, 16, 25 and then 9 again, so the period is 4. The output bits are the parities 1, 0, 0, 1.

10. Here $2^8 \bmod 10 = 6$, so $t = 6$. The rejected words are 0, 26, 77, 128, 154 and 205. Ten words have a low byte below 10 and need the division. The other 250 words split evenly, 25 for each output.

14. The map for $10^6$ steps is $(A, C) = (586742017, 4074525504)$. From the seed 0, the state is $C = 4074525504$.

20. The outputs $x$ run 6, 6, 9, 7, 7, 6, 0, 4, 4, 6, 8, 1, and so on. The period is the order of 10 modulo 59, which is 58. A safe prime gives $(m-1)/2$ only when $b$ is a quadratic residue, and 10 is not a residue modulo 59. The fixed points are $(0, 0)$ and $(9, 5)$, where $6x + c$ is 0 or 59.

21. Write $a^2 = 1 + 8k$ and square repeatedly to get $a^{2^j} \equiv 1 \pmod{2^{j+2}}$. If $a \equiv 3$ or $5 \pmod 8$, then $a^{2^j} - 1$ is $2^{j+2}$ times an odd number, so $a^{2^{w-3}} \not\equiv 1$. If $a \equiv 1$ or $7$, then $a^2 \equiv 1 \pmod{16}$ and the order drops to $2^{w-3}$. At $w = 3$, the multiplier $a = 7$ also has order $2 = 2^{w-2}$, so the "exactly when" fails.

22. The vector $(25, -10, 1)$ comes from exercise 12, and its squared length is 726. Any shorter vector has every $|k_i| \le 26$, and a search of that box finds nothing shorter. The spacing is $1/\sqrt{726} \approx 0.037$. [RANDU](/randu/)'s vector $(9, -6, 1)$ gives $1/\sqrt{118} \approx 0.092$.

23. The period is $2^{16} - 1$ exactly when the matrix $T$ has $T^{65535} = I$ and $T^{65535/p} \ne I$ for each prime $p$ in $65535 = 3 \cdot 5 \cdot 17 \cdot 257$. Exactly 60 triples pass, among them $(7, 9, 8)$. The same program with 8-bit words finds 24 triples, which matches the [xorshift](/xorshift/) entry.

24. Since $-1$ is a non-residue modulo $p$ and modulo $q$, exactly one of the four square roots of a residue is itself a residue. So squaring is a bijection of the residues, and the state sequence is a cycle of a permutation, with no tail. The unique residue root is $x^{(p+1)/4} \bmod p$ and $x^{(q+1)/4} \bmod q$, combined by the Chinese remainder theorem.

25. The classes $j = 0, \ldots, 4$ have sizes 1, 4, 6, 4, 1 and give 0, 2, $5/3$, 2, 0 bits. The size 6 splits as $4 + 2$. The expectation is $8pq(p^2 + q^2) + 10 p^2 q^2$, which is $13/8 = 1.625$ at $p = 1/2$ and $1.4154$ at $p = 0.7$. Per flip that is 0.406 and 0.354, against von Neumann's $pq$, which is 0.25 and 0.21. The bound at $p = 0.7$ is $h(0.7) \approx 0.881$.
