1. $X = (0, 2, 0, 2)$. Both sides of Parseval's theorem agree: $\sum |X_k|^2 = 8 = 4 \cdot 2 = n \sum |x_j|^2$.

2. The order is $0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15$. The fixed points are $0$, $6$, $9$ and $15$, whose 4-bit codes are palindromes. The other 12 indices form 6 pairs, so 6 swaps.

3. Linear: $(1, 3, 6, 5, 3)$. Cyclic of length 3: add the last two terms onto the first two, giving $(6, 6, 6)$. The linear result has 5 terms, so the length must be at least 5, and the smallest power of two is 8.

5. Length 256, since $3$ is a primitive root modulo 257. Because $2^8 = 256 \equiv -1$, $2^{16} \equiv 1$ and $2^8 \not\equiv 1$, so the order is 16. Multiplying by $2^s$ is a shift, and $2^8 \equiv -1$ turns the reduction into a subtraction: there are no real multiplications at all.

6. After the stages: $(1, 1, 1, 1, 0, 0, 1, -1)$, then $(2, 2, 0, 0, 1, -1, -1, 1)$, then $(3, 1, -1, 1, 1, 3, 1, -1)$. Each stage does 4 butterflies of 2 operations, so $n \lg n = 24$ in all.

7. With $c = 1/2$ the first pass gives $(3, 7, -1, 1)$ and the second gives $(5, -2, -1, 1)$. With $c = 1/\sqrt 2$ the output is $(10, -4, -\sqrt 2, \sqrt 2)$, and both sums of squares are $120$.

8. The FFT makes $\frac{n}{2}\lg n = 5120$ multiplications and $n \lg n = 10240$ additions. The direct sum makes $n(n-1) = 1047552$ of each. There are 5120 butterflies, and 1023 of them have twiddle 1.

12. The stage that joins blocks of size $h$ has $n/(2h)$ blocks, and the first butterfly of each block has twiddle $\omega^0 = 1$. Sum over $h = 1, 2, 4, \ldots, n/2$: the geometric series gives $n - 1$. That leaves $\frac{n}{2}\lg n - n + 1$ nontrivial multiplications.

17. A coefficient of the product can be as large as $10^5 \cdot 999^2 \approx 9.98 \cdot 10^{10}$, which exceeds the prime. Two primes such as $998244353$ and $167772161$ have a product above $10^{17}$, which is enough. The product has up to $2 \cdot 10^5 - 1$ coefficients, so the length is $2^{18}$, and $2^{18}$ divides $p - 1$ for both.

19. The powers $3^q \bmod 7$ for $q = 0, \ldots, 5$ are $1, 3, 2, 6, 4, 5$, so it reads $x_1, x_3, x_2, x_6, x_4, x_5$. The inverse of 3 is 5, whose powers are $1, 5, 4, 6, 2, 3$, so it produces $X_1, X_5, X_4, X_6, X_2, X_3$. What is left is a cyclic convolution of length 6, plus $X_0 = \sum x_j$ and adding $x_0$ to every other output.

21. Compute $\sum_j p_j t_{i+j}(p_j - t_{i+j})^2$ for every $i$. Each term is nonnegative and is zero exactly when one of the two is a wildcard or the letters agree. Expanding the square gives three sums of the form $\sum_j p_j^a t_{i+j}^b$, each a convolution of the reversed pattern with the text.

22. The coefficient at $s$ is $\sum_{v \in V} (-1)^{s \cdot v}$. The map $v \mapsto s \cdot v$ is linear on $V$; if it is zero, every term is $1$, and if not, it takes the values $0$ and $1$ equally often and the terms cancel.

23. If two pairs give the same $j$, reduce modulo $n_1$: $n_2(j_1 - j_1') \equiv 0$, and $n_2$ is invertible modulo $n_1$, so $j_1 = j_1'$; the same for $j_2$. For the product, $\omega_n^{n_2 j_1 k} = \omega_{n_1}^{j_1 k} = \omega_{n_1}^{j_1 k_1}$, and likewise for the second term.

25. Write $f(a z^k) = z^{-\binom{k}{2}} \sum_j \bigl(f_j a^j z^{-\binom{j}{2}}\bigr) z^{\binom{j+k}{2}}$. The sum is a correlation of a sequence of length $n$ with $z^{\binom{r}{2}}$ for $0 \le r < n + m - 1$, which one FFT convolution computes.
