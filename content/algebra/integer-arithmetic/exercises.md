1. ◦ Give the quotient and remainder of $-23$ divided by $4$ under three rules: [division with remainder](/division-with-remainder/) ($0 \le r < 4$), the truncated division of C, and the [floor division](/floor-division/) of Python. Then give the C and the Python results for $23$ divided by $-4$.

2. ◦ Write 200 in base 2, base 8 and base 16, and in [balanced ternary](/balanced-ternary/) with the digit $\mathrm{T} = -1$. Then write $-200$ in balanced ternary without doing the conversion again.

3. ◦ Give the 8-bit word for $-37$ in [sign-magnitude](/sign-magnitude-representation/), in [one's complement](/ones-complement/) and in two's complement. Then read the word $10100101$ in each of the three encodings.

4. ◦ In 8-bit two's complement, which of these operations overflow, and which word does the hardware keep for each: $90 + 60$, $(-70) + (-70)$, $120 + (-128)$, $64 \cdot 2$? In 8-bit unsigned arithmetic, what does $250 + 10$ give, and how is the overflow detected?

5. ◦ Multiply $2718 \times 3141$ by one level of [Karatsuba multiplication](/karatsuba-multiplication/) in radix $\beta = 100$. Give $z_2$, $z_0$, the product of the sums, $z_1$ and the result.

6. ◦ Run [Newton's method for integer roots](/newton-integer-root/) with $k = 2$ on $N = 2000$, starting at the value that line L2 gives. List the values of $x$, and say how many times line L4 runs. How many times does it run if you start at $x = 2000$ instead?

7. ◦ Compute $F_{20}$ by [fast doubling](/fibonacci-fast-doubling/). Show the pair $(F_k, F_{k+1})$ after each binary digit of 20, and count the multiplications.

8. ◦ Write 59 in binary. Give its radix-2 [Booth](/booth-multiplication/) digits $y_{i-1} - y_i$ for an 8-bit word, and its [non-adjacent form](/non-adjacent-form/). How many nonzero digits does each of the three forms have?

9. ◦ A [Dadda multiplier](/dadda-multiplier/) for 16-bit operands starts with columns of height up to 16. How many reduction stages does it need, and what are the target heights of the stages? How many stages for 32-bit operands?

10. • Show that when $k \ge 2$ numbers are added column by column in radix $\beta$, the carry out of each column is at most $k - 1$. How many digits can the sum of $k$ numbers of $n$ digits have?

11. • In C, `a / b` truncates toward zero and `a % b` has the sign of `a`. Write the floored quotient and remainder of Python in terms of `q = a / b` and `r = a % b`, using one test and no other division.

12. • Run Karatsuba with threshold $T = 1$, the split $h = \lceil n/2 \rceil$ and the carry bits split off, as in its entry. Show that it makes exactly $3^{\lceil \log_2 n \rceil}$ limb products on $n$-limb operands. How many for $n = 16$ and for $n = 17$? Is the bound $\Theta(n^{\log_2 3})$ still true for every $n$?

13. • [Toom-Cook multiplication](/toom-cook-multiplication/) with $k$ pieces costs $\Theta(n^{\log_k(2k-1)})$. Find the smallest $k$ for which the exponent is below $1.3$, and show that the exponent tends to 1 as $k$ grows. Why do libraries stop at small $k$ anyway?

14. • Let $x$ have $N$ bits, and multiply with the schoolbook method, at cost $\Theta(pq)$ for a $p$-bit by $q$-bit product. Show that computing $x^e$ by $e - 1$ multiplications by $x$ costs $\Theta(e^2N^2)$ bit operations, and that the binary method costs $\Theta(e^2 N^2)$ too.

15. • Let $t = \lfloor \sqrt{\lfloor N/4 \rfloor} \rfloor$. Prove that $\lfloor \sqrt N \rfloor$ is $2t$ or $2t + 1$. Turn this into a recursive [integer square root](/integer-square-root/), and check it on $N = 2000$.

16. • To decide whether $N \ge 2$ is a perfect power $m^k$ with $k \ge 2$, show that it is enough to compute $\lfloor N^{1/k} \rfloor$ for the primes $k \le \log_2 N$ ([integer n-th root](/integer-nth-root/)).

17. • For $w = 8$, find the smallest $s$ and the multiplier $M = \lceil 2^{8+s}/10 \rceil$ for which the rule of [division by a constant](/division-by-constant/) gives $\lfloor n/10 \rfloor = \lfloor Mn/2^{8+s} \rfloor$ for all $0 \le n < 256$. Do the same for $d = 7$, and say why the answer for 7 does not fit the 8-bit multiplier of the machine.

18. • Let $D$ have $n$ limbs and let $R = \lfloor \beta^{2n}/D \rfloor$. Show that for every $0 \le A < \beta^{2n}$, the value $\hat q = \lfloor AR/\beta^{2n} \rfloor$ is $\lfloor A/D \rfloor$ or $\lfloor A/D \rfloor - 1$. How do you tell which, and what does the test cost?

19. • Prove that every [addition chain](/addition-chain/) for $n$ has length at least $\lceil \log_2 n \rceil$. How many multiplications does the binary method use for $x^{27}$? Find an addition chain for 27 of length 6, and use the fact that a number with at least three 1 bits needs at least $\lfloor \log_2 n \rfloor + 2$ steps to show that 6 is optimal.

20. • For $n = 16$, count the prefix cells and the levels of the [Kogge-Stone](/kogge-stone-adder/), [Sklansky](/sklansky-adder/) and [Brent-Kung](/brent-kung-adder/) adders.

21. • Square the matrix $\begin{pmatrix} F_{k+1} & F_k \\ F_k & F_{k-1} \end{pmatrix}$ to get formulas for $F_{2k-1}$ and $F_{2k}$ in terms of $F_{k-1}$ and $F_k$. How many multiplications does this doubling step need?

22. ★ The $2^k$-ary method precomputes $x^2, \ldots, x^{2^k - 1}$, then reads the exponent $n$ in digits of $k$ bits from the top, with $k$ squarings and at most one multiplication per digit. Show that it uses at most $\lambda(n) + (\lambda(n) + 1)/k + 2^k - 2$ multiplications, where $\lambda(n) = \lfloor \log_2 n \rfloor$. Choose $k$ to get $\ell(n) \le \lambda(n) + (1 + o(1))\, \lambda(n)/\log_2 \lambda(n)$.

23. ★ Prove that $\gcd(F_m, F_n) = F_{\gcd(m, n)}$ for all $m, n \ge 1$.

24. ★ Add two random $n$-bit numbers, each bit 0 or 1 with probability $\frac12$ independently. Say that a carry chain of length $t$ starts at position $i$ if position $i$ generates a carry ($a_i = b_i = 1$) and positions $i + 1, \ldots, i + t - 1$ propagate it ($a_j \ne b_j$). Let $L$ be the longest carry chain. Prove that $E[L] \le \log_2 n + 1$. (This is the claim of Burks, Goldstine and von Neumann that the [ripple-carry adder](/ripple-carry-adder/) is fast on average.)

25. ★ Prove that the expected number of nonzero digits in the non-adjacent form of a number chosen uniformly from $0, \ldots, 2^k - 1$ is $k/3 + O(1)$.

26. ★ Let $d$ be odd and let $d'$ be the inverse of $d$ modulo $2^w$. Prove that for $0 \le n < 2^w$, $d$ divides $n$ if and only if $r = n d' \bmod 2^w$ is at most $\lfloor (2^w - 1)/d \rfloor$, and that then $r = n/d$. Find $3^{-1} \bmod 2^8$ and use it to divide 141 by 3, and to show that 3 does not divide 142.
