1. The hospital has $x + y = 26 > 15$, so it is late; the latest start was $z - x - y = -11$, eleven years ago. Traffic recorded from year $\max(0, z - x) = 0$ to year $y = 6$, that is everything sent before the migration ends, will be readable. The shop has $x + y = 12 \le 15$ and three years to spare.

2. Category 1 in both cases. The classical cost $2^{150}$ is above $2^{143}$, and the quantum cost $2^{125}$ is above $2^{157-40} = 2^{117}$ and $2^{157-96} = 2^{61}$. Category 2 needs $2^{146}$ in every metric, and the quantum attack costs less. Category 3 needs $2^{207}$ classical gates.

5. $\text{Compress}_4(2000) = 10$ and $\text{Decompress}_4(10) = 2081$, off by 81. $\text{Compress}_{10}(3000) = 923$ and $\text{Decompress}_{10}(923) = 3001$, off by 1. $\text{Compress}_4(3328) = 16 \bmod 16 = 0$, which decompresses to 0; since $3328 \equiv -1 \pmod{3329}$, that is off by only 1.

7. $(1, 0, 1)^\mathsf{T}$ is column 5, so $e$ has its one at position 5. The weight-2 error gives $(0,1,0) + (1,1,1) = (1,0,1)$, the same syndrome as position 5: the Hamming code has minimum distance 3 and corrects only one error.

9. $b = (80, 62, 4, 53)$. The ciphertext is $u = (72, 22)$ and $v = 43$; $\langle u, s \rangle \equiv 92$, so $d = 52$, which lies in $(25, 76)$, and the bit is 1. Decryption is sure to work when $|x^\mathsf{T} e| < \lfloor q/4 \rfloor = 25$, so $m = 24$; with $m = 25$ and all errors $-1$, the bit 1 gives $d = 25$ and decrypts to 0.

11. $3328 = 2^8 \cdot 13$, $8380416 = 2^{13} \cdot 1023$ and $12288 = 2^{12} \cdot 3$. $x^n + 1$ splits into linear factors mod $q$ exactly when $2n$ divides $q - 1$, since its roots are the elements of order $2n$. So it splits for ML-DSA, and $x^{1024} + 1$ splits mod 12289. Mod 3329 there is an element of order 256 (namely 17) but none of order 512, so the factors are $x^2 - \zeta^{2i+1}$; each NTT layer halves the degree, and seven halvings take 256 to 2.

13. Prange: $\binom{40}{4}/\binom{20}{4} = 91390/4845 \approx 18.9$. Lee-Brickell adds the terms $\binom{20}{i}\binom{20}{4-i}$ for $i \le p$ to the denominator: $91390/27645 \approx 3.31$ for $p = 1$ and $91390/63745 \approx 1.43$ for $p = 2$.

16. $b \ge 128/0.292 \approx 438.4$, so 439 classically, and $b \ge 128/0.265 \approx 483.0$, so 484 quantumly. Kyber512 gets $0.292 \cdot 403 \approx 117.7$ and $0.265 \cdot 403 \approx 106.8$. Core-SVP counts one SVP call, drops lower-order terms and treats exponential memory as free; it is a deliberately low estimate, while category 1 compares the full cost of an attack with the $2^{143}$ gates of a key search on AES-128.

18. Lamport: public key $2 \cdot 192 \cdot 24 = 9216$ bytes, signature 4608. Winternitz with $w = 16$: $\ell_1 = 48$, $\ell_2 = \lfloor \lg 720 / 4 \rfloor + 1 = 3$, $\ell = 51$, 1224 bytes. With $w = 256$: $\ell_1 = 24$, $\ell_2 = 2$, $\ell = 26$, 624 bytes.

20. For one coefficient the chance of staying inside is about $1 - \beta/\gamma_1$, and $(1 - \beta/\gamma_1)^{256\ell} \approx e^{-256\ell\beta/\gamma_1}$; the low parts give the factor with $k$ and $\gamma_2$. With $\beta = \tau\eta$ the expected numbers of attempts are about 4.26, 5.09 and 3.85, against 4.25, 5.1 and 3.85 in FIPS 204.

21. $(x^n - 1)(1) = 0$, so evaluation at 1 respects reduction mod $x^n - 1$. Then $b(1) = a(1)s(1) + e(1)$ with $|e(1)| \le 8$. Try all 97 values $g$ of $s(1)$ and accept if some $g$ puts every $b(1) - a(1)g$ in $[-8, 8]$. Real samples always pass; uniform ones pass with probability at most $97 \cdot (17/97)^5 \approx 0.016$. For $x^n + 1$, 1 is not a root mod an odd $q$, and at a root $\alpha$ the value $e(\alpha)$ is not small.

22. $b + rg = \langle a + re_1, s \rangle + e + r(g - s_1)$. If $g \ne s_1$ the term $r(g - s_1)$ is uniform because $q$ is prime, so the new $b$ is uniform and independent of the new $a$. Each coordinate needs at most $q$ guesses, so at most $nq = 852{,}224$ calls.

23. $E[x^\mathsf{T}x] = I/12$, so the covariance is $B^\mathsf{T}B/12 = \frac{1}{12}\begin{pmatrix}17 & 1 \\ 1 & 10\end{pmatrix}$. Averaging many differences estimates $B^\mathsf{T}B$, the shape of the secret parallelepiped. Nguyen and Regev (2006) went on to recover $B$ itself and broke GGH and NTRUSign signatures this way. A discrete Gaussian with $\sigma$ above the smoothing parameter does not depend on which short basis produced it.

24. For these primes both $j = 0$ and $j = 1728$ are supersingular; they come from two and three values of $\lambda$, and every other $j$ from six. For $p = 431$ the program finds 215 roots, 37 values of $j$ and 21 of them in $\mathbb{F}_{431}$, as in the entry. For $p = 419$ it finds 209 roots and 36 values of $j$, 18 of them in $\mathbb{F}_{419}$.
