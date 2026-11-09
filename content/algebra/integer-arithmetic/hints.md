1. Euclid's rule gives $q = -6$, $r = 1$, since $-23 = 4 \cdot (-6) + 1$. C gives $-23 / 4 = -5$ and $-23 \% 4 = -3$. Python gives $-23 // 4 = -6$ and $-23 \% 4 = 1$. For $23$ divided by $-4$, C gives $-5$ and $3$, and Python gives $-6$ and $-1$: in C the remainder takes the sign of the dividend, in Python that of the divisor.

2. $200 = 11001000_2 = 310_8 = \mathrm{C8}_{16}$. In balanced ternary $200 = 243 - 81 + 27 + 9 + 3 - 1$, written $1\mathrm{T}111\mathrm{T}$. Negation swaps 1 and T, so $-200$ is $\mathrm{T}1\mathrm{TTT}1$.

3. $37 = 00100101_2$. Sign-magnitude $10100101$, one's complement $11011010$, two's complement $11011011$. The word $10100101$ means $-37$, $-90$ and $-91$ in the three encodings.

4. $90 + 60$ overflows and gives $-106$. $(-70) + (-70)$ overflows and gives $116$. $120 + (-128) = -8$ does not overflow: operands of opposite signs never do. $64 \cdot 2$ overflows and gives $-128$. Unsigned, $250 + 10$ gives $4$, and the carry out of the top bit signals the overflow.

5. $z_2 = 27 \cdot 31 = 837$, $z_0 = 18 \cdot 41 = 738$, $(27 + 18)(31 + 41) = 45 \cdot 72 = 3240$, $z_1 = 3240 - 837 - 738 = 1665$. The product is $837 \cdot 10^4 + 1665 \cdot 10^2 + 738 = 8537238$.

6. $N = 2000$ has 11 bits, so L2 starts at $2^6 = 64$. The values are $64, 47, 44$, and the step from 44 gives 44 again, so the loop stops: L4 runs 3 times and the answer is 44. From $x = 2000$ the values are $2000, 1000, 501, 252, 129, 72, 49, 44$, and L4 runs 8 times.

7. $20 = 10100_2$. Starting from $(F_0, F_1) = (0, 1)$, the pairs are $(1, 1)$, $(1, 2)$, $(5, 8)$, $(55, 89)$, $(6765, 10946)$. Each of the 5 doubling steps costs 3 multiplications, 15 in all; the steps for a 1 bit add one addition.

8. $59 = 111011_2$, five nonzero digits. With $y_{-1} = 0$, the Booth digits for positions 0 to 7 are $-1, 0, 1, -1, 0, 0, 1, 0$, that is $64 - 8 + 4 - 1$, four nonzero digits. The NAF is $64 - 4 - 1$, three nonzero digits.

9. The Dadda heights are $2, 3, 4, 6, 9, 13, 19, 28, \ldots$, with $d_{j+1} = \lfloor 3d_j/2 \rfloor$. For 16-bit operands the stages reduce to $13, 9, 6, 4, 3, 2$: six stages. For 32-bit operands, eight stages: $28, 19, 13, 9, 6, 4, 3, 2$.

10. By induction on the column: if the carry in is at most $k - 1$, the column sum is at most $k(\beta - 1) + k - 1 = k\beta - 1$. The sum is below $k\beta^n$, so it has at most $n + \lceil \log_\beta k \rceil$ digits.

11. If $r \ne 0$ and $r$ and $b$ have opposite signs, the floored result is $q - 1$ and $r + b$. Otherwise it is $q$ and $r$.

12. Splitting off the carry bits keeps all three subproducts at $h = \lceil n/2 \rceil$ limbs, so $P(n) = 3P(\lceil n/2 \rceil)$ with $P(1) = 1$, and $\lceil \lceil n/2 \rceil / 2 \rceil = \lceil n/4 \rceil$. $P(16) = 81$ and $P(17) = 243$. Since $3^{\lceil \log_2 n \rceil} < 3 \cdot 3^{\log_2 n} = 3n^{\log_2 3}$, the bound holds with a constant 3.

13. $\log_8 15 \approx 1.302$ and $\log_9 17 \approx 1.289$, so $k = 9$. The evaluation and interpolation steps take $\Theta(k^2)$ operations on numbers of $n/k$ limbs, with constants that grow with $k$, so a large $k$ pays off only for very large $n$, where the FFT methods are faster anyway.

15. Write $N = 4M + d$ with $0 \le d \le 3$. From $t^2 \le M < (t+1)^2$ get $(2t)^2 \le N < (2t + 2)^2$. For $N = 2000$: $M = 500$, $t = 22$, and $45^2 = 2025 > 2000$, so $\lfloor \sqrt{2000} \rfloor = 44$.

16. If $N = m^k$ and $p$ is a prime factor of $k$, then $N = (m^{k/p})^p$. And $m \ge 2$ forces $k \le \log_2 N$.

17. For $d = 10$: $s = 3$, $M = \lceil 2048/10 \rceil = 205$, and $205 \cdot 10 - 2048 = 2 \le 2^3$. For $d = 7$, $s = 2$ fails ($147 \cdot 7 - 1024 = 5 > 4$), and $s = 3$ gives $M = 293$, which needs 9 bits. Compilers then multiply by $M - 256$ and add $n$ back in a step that avoids the overflow.

19. By induction $a_i \le 2^i$. The binary method uses 4 squarings and 3 multiplications, 7 in all. A chain of length 6 is $1, 2, 3, 6, 9, 18, 27$. Since 27 has four 1 bits, $\ell(27) \ge \lfloor \log_2 27 \rfloor + 2 = 6$.

20. Kogge-Stone: $n \log_2 n - n + 1 = 49$ cells, 4 levels. Sklansky: $(n/2) \log_2 n = 32$ cells, 4 levels. Brent-Kung: $2n - 2 - \log_2 n = 26$ cells, $2 \log_2 n - 1 = 7$ levels.

22. Precomputation costs $2^k - 2$ multiplications. The exponent has $d = \lceil (\lambda + 1)/k \rceil$ digits; after the top digit, which is a table lookup, come $k(d-1) \le \lambda$ squarings and at most $d - 1 \le (\lambda + 1)/k$ multiplications. Take $k = \lfloor \log_2 \lambda - 2 \log_2 \log_2 \lambda \rfloor$, so that $2^k \le \lambda / (\log_2 \lambda)^2$.

23. Prove the addition law $F_{m+n} = F_{m+1} F_n + F_m F_{n-1}$ from the matrix power. It shows $\gcd(F_{m+n}, F_n) = \gcd(F_m, F_n)$, using that consecutive Fibonacci numbers are coprime. Then run Euclid's algorithm on the indices.

24. A chain of length at least $t$ starting at $i$ has probability at most $\frac14 \cdot 2^{-(t-1)}$, so $P(L \ge t) \le n/2^{t+1}$ by the union bound. Write $E[L] = \sum_{t \ge 1} P(L \ge t)$, bound the first $m = \lfloor \log_2 n \rfloor$ terms by 1 and sum the geometric tail.

25. Read the NAF from the low end. When the remaining number is even, the next digit is 0. When it is odd, the next two digits are $\pm 1$ and 0. For a uniform number the low bits are uniform, so each block is "0" or "$\pm 1\,0$" with probability $\frac12$, independently. The expected block length is $\frac32$ and the expected number of nonzero digits per block is $\frac12$.

26. Multiplication by $d'$ is a bijection modulo $2^w$, and it maps the multiples $0, d, 2d, \ldots$ below $2^w$ to $0, 1, 2, \ldots, \lfloor (2^w - 1)/d \rfloor$. $3 \cdot 171 = 513 \equiv 1 \pmod{256}$. Then $141 \cdot 171 \bmod 256 = 47$, and $47 \cdot 3 = 141$. But $142 \cdot 171 \bmod 256 = 218 > 85$, so 3 does not divide 142.
