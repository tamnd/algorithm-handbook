1. $N = 2773$, $\varphi(N) = 2668$, $\lambda(N) = 1334$ and $d = 157$, which is also $17^{-1} \bmod 1334$. The ciphertext is $c = 948$. With the CRT, $d_p = 19$, $d_q = 41$, $q^{-1} \bmod p = 4$, $m_1 = 27$ and $m_2 = 35$; then $h = 4 \cdot (27 - 35) \bmod 47 = 15$ and $m = 35 + 15 \cdot 59 = 920$.

3. $c = 74088 = 42^3$ is a perfect cube over the integers, so $m = 42$. The message is so short that $m^3 < N$, and the reduction modulo $N$ never happens. Padding prevents this.

5. Modulo 7, $100 \equiv 2$ and $2^2 = 4$, so the roots are $\pm 4$; modulo 19, $100 \equiv 5$ and $5^5 \bmod 19 = 9$, so the roots are $\pm 9$. The CRT gives $\{10, 66, 67, 123\}$. Since $66 \ne \pm 10$, $\gcd(66 - 10, 133) = \gcd(56, 133) = 7$, and $N/7 = 19$.

7. $c_1 = 36^4 \cdot 2^{35} \bmod 1225 = 88$ and $c_2 = 712$. Their product is $181$, and $L(181^{12} \bmod 1225) \cdot 3 \bmod 35 = 13 = 4 + 9$.

9. The CRT combination of $3$, $189$ and $370$ modulo $55 \cdot 391 \cdot 1189 = 25569445$ is $74088$. It is less than the product, so it equals $m^3$ over the integers, and $m = 42$.

11. $ed - 1 = 2668 = 2^2 \cdot 667$. Then $2^{667} \bmod 2773 = 471$ and $471^2 \equiv 1$, so 471 is a square root of 1 other than $\pm 1$, and $\gcd(470, 2773) = 47$.

13. $e/N = [0; 1, 3, 1, 24, \ldots]$ with convergents $0/1$, $1/1$, $3/4$, $4/5$. The pair $k = 4$, $d = 5$ gives $\varphi = (5e - 1)/4 = 1020096$, $p + q = N - \varphi + 1 = 2022$ and discriminant $2022^2 - 4N = 16 = 4^2$, so $p, q = 1013, 1009$. The bound is $N^{1/4}/3 \approx 10.6$.

15. The ciphertexts are 18, 50 and 49, and $(c/11) = -1, -1, +1$ gives $1, 1, 0$. The product $18 \cdot 50 \bmod 209 = 64$ is a square modulo 11, so it decrypts to $0 = 1 \oplus 1$. Multiplying by a square keeps the bit: the query $18 \cdot 4 = 72$ decrypts to the challenge bit.

17. $Q = (10, 6)$, $R = (9, 16)$ and $Z = 5Q = 3R = (3, 16)$. From $-R = (9, 1)$ the receiver computes $(3, 1) = -Z$, with the same x-coordinate, so without $R$ in the KDF input two ciphertexts decrypt to the same message.

21. Because $N$ is odd, $2m \bmod N$ is even exactly when $2m < N$. Each further doubling halves the interval that holds $m$. The answers start $0, 1, 0$, twelve queries leave only $m = 920$, and a 2048-bit modulus needs 2048 queries.

22. Draw $x$, ask for a root $y$ of $x^2$. The oracle sees only $x^2$, so each of the four roots is equally likely to be $x$; two of them are $\pm y$, and the other two give $\gcd(x - y, N) \in \{p, q\}$. Forty queries suffice. For the example, $\gcd(10 - 66, 133) = 7$.

23. Expand $(1 + N)^m$ by the binomial theorem; every term after the second is a multiple of $N^2$. By the CRT, $\mathbb{Z}_{N^2}^*$ splits into $\mathbb{Z}_{p^2}^*$ and $\mathbb{Z}_{q^2}^*$, of orders $p(p - 1)$ and $q(q - 1)$, and both divide $N\lambda$. So $c^\lambda \equiv 1 + m\lambda N$, $L = m\lambda \bmod N$, and $\mu = \lambda^{-1} \bmod N$ removes $\lambda$. On the example, $88^{12} \bmod 1225 = 456 = 1 + 13 \cdot 35$, so $L = 13$ and $13 \cdot 3 \bmod 35 = 4$.

24. $c_2 + 2c_1 - 1 = 3m(m^2 + m + 1)$ and $c_2 - c_1 + 2 = 3(m^2 + m + 1)$, so their quotient modulo $N$ is $m$. Here $2184 \cdot 2573^{-1} \bmod 2773 = 100$.

25. Query $y \cdot r^e$ for a fresh uniform $r$; this is uniform because $x \mapsto x r$ is a bijection of $\mathbb{Z}_N^*$. A correct answer $x'$ gives $x = x' r^{-1}$, and the number of calls is geometric with mean 100. In the example $y \cdot 2^{17} \bmod 2773 = 899$, and $1840 \cdot 2^{-1} \bmod 2773 = 920$.
