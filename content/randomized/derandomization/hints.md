1. The pairs are $01, 10, 00, 11, 10, 10, 01$, so the output is $01110$. Each pair gives a bit with probability $2pq = 0.32$, so 50 pairs give 16 bits in expectation, and one bit costs $1/(pq) = 6.25$ flips.

3. The vertices go to sides $0, 0, 1, 0, 1, 0$, so the cut is $\{0, 1, 3, 5\}$ against $\{2, 4\}$ and has 6 edges, more than $m/2 = 4.5$. The maximum is 7, for example $\{0, 2, 4\}$ against $\{1, 3, 5\}$; only the edges 04 and 35 are uncut.

5. The powers are $001, 011, 101, 100, 111, 010, 110$, and the output is $1101001$. Every nonempty parity has bias at most $(n - 1)/2^m = 6/8 = 3/4$.

7. The bound is $\frac12 (3/4)^{t-1}$, and $(3/4)^{t-1} \le 2^{-9}$ first holds at $t = 23$. The walk uses $100 + 22 \cdot 4 = 188$ bits. Independent runs need 10 runs and 1000 bits.

9. A clause with two distinct literals fails only when both are false, with probability $1/4$. The start value is $9/2$. For $x_1$ both values give $9/2$, so $x_1$ is true. Then $x_2$ true gives 4 and false gives 5, so $x_2$ is false. Then $x_3$ true gives 6 and false gives 4. The assignment true, false, true satisfies all six clauses.

11. The test accepts $G$ always and a uniform string half the time, so the advantage is $1/2$. The hybrids give $p_0 = p_1 = p_2 = 1/2$ and $p_3 = 1$: all the advantage sits in the last step. The predictor for bit 3 guesses $y_1 \oplus y_2$ and is always right, an advantage of $1/2$, more than the guaranteed $\varepsilon/m = 1/6$.

12. For $y = 000$ the bit is always 0, and for $y = 111$ it is always 1, since every string in the source has odd weight. For the other six seeds the bit is balanced on the four strings. The distance is $\frac18(\frac12 + \frac12) = 1/8$. The family is universal, $k = 2$ and $m = 1$, so the bound is $\frac12\sqrt{1/2} \approx 0.354$.

13. The cycle is 2-regular, so by Hall's condition every set has at least as many neighbours as elements, and the even vertices have only the 4 odd vertices as neighbours. The smallest value is 4, and $\varepsilon = 1/2$. The cycle has even length, so its walk matrix has eigenvalue $-1$, $\lambda = 1$, and the bound is $8/4 = 2$.

16. The condition is $\frac{\varepsilon}{2}\sqrt{1023} \le 0.01$, so $\varepsilon \le 0.02/\sqrt{1023} \approx 6.25 \cdot 10^{-4}$. Then $\log_2(999/\varepsilon) \approx 20.6$ and the seed has 42 bits.

20. For the first test, accept exactly the image of $G$, which has at most $2^d$ elements. For the extractor, take any set $A$ of $2^k$ inputs: the outputs on $A$ and all seeds number at most $2^{k+d}$, and the uniform distribution puts mass at least $1 - 2^{k+d-m}$ outside them, which is $31/32$ for the numbers given. A generator only has to fool tests of bounded size, and deciding membership in the image is in general not such a test.

21. A fixed test is missed by one uniform string with probability at most $1/2$, so by all $T$ with probability at most $2^{-T}$; apply the [union bound](/union-bound/). For $N = 2^{1000}$, $T = 1001$. For the second part, the test that rejects exactly the strings of a set $H$ with $|H| \le 2^{m-1}$ accepts at least half of $\{0,1\}^m$ and is never hit. So a hitting set exists only for a limited class of tests, as for a generator.

22. Let $\chi_i = (-1)^{X_i}$. With the inner product $\mathrm{E}[fg]$ over the sample space, the functions $1, \chi_1, \ldots, \chi_n$ are orthonormal by pairwise independence, and they live in a space whose dimension is the number of points. For 4-wise independence add the products $\chi_i \chi_j$ with $i < j$: every product of two different functions of the list is a product of one to four distinct $\chi$'s. For $n = 8$ the bounds are 9 and 37.

24. Of the $n/2$ pairs, $u$ has one symbol per pair, i.i.d. with $\Pr[1] = 2pq$, and $v$ has about $(p^2 + q^2)n/2$ symbols with $\Pr[1] = p^2/(p^2 + q^2)$. So $r_\nu(p) = pq + \frac12 r_{\nu-1}(2pq) + \frac12 (p^2 + q^2)\, r_{\nu-1}\big(p^2/(p^2 + q^2)\big)$. For $p = 1/3$ this gives $r_2 = 2/9 + 10/81 + 2/45 = 158/405 \approx 0.390$, against $r_1 \approx 0.222$ and $H(1/3) \approx 0.918$.
