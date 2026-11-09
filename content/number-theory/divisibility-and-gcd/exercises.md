1. ◦ Run the [Euclidean algorithm](/euclidean-algorithm/) on $(252, 198)$. List the quotients and remainders. What is the gcd, and how many divisions does the algorithm make?

2. ◦ Run the [extended Euclidean algorithm](/extended-euclidean-algorithm/) on $(240, 46)$. Give the gcd and a pair $x, y$ with $240x + 46y = \gcd(240, 46)$, and check that $|x| \le 46/(2g)$ and $|y| \le 240/(2g)$.

3. ◦ Factor $720$ and use the [divisor function](/divisor-function/) to find $d(720)$ and $\sigma(720)$ without listing the divisors.

4. ◦ Use [Legendre's formula](/legendre-formula/) to find the number of zeros at the end of $500!$ and the exponent of $3$ in $200!$.

5. ◦ Find the [continued fraction](/continued-fraction/) of $157/68$ and all its [convergents](/continued-fraction-convergents/). Check that $p_n q_{n-1} - p_{n-1} q_n = \pm 1$ for each pair of consecutive convergents.

6. ◦ Give $\mu(1)$, $\mu(30)$, $\mu(60)$, $\mu(210)$ and $\mu(1001)$, where $\mu$ is the [Möbius function](/mobius-function/). Then check $\sum_{d \mid 12} \mu(d) = 0$ by listing the terms.

7. ◦ Compute $\gcd(12, 18, 30)$ and $\operatorname{lcm}(12, 18, 30)$. Show that their product is not $12 \cdot 18 \cdot 30$, so the [GCD and LCM identity](/gcd-lcm-identity/) does not extend to three numbers.

8. ◦ Write out the [Farey sequence](/farey-sequence/) $F_5$. Check its length against $1 + \sum_{k \le 5} \varphi(k)$, and check $bc - ad = 1$ for the neighbours $2/5$ and $1/2$.

9. ◦ Find the path from the root $1/1$ to $3/7$ in the [Stern-Brocot tree](/stern-brocot-tree/), as a word in $L$ and $R$. Compare the run lengths with the continued fraction of $3/7$.

10. • Find the smallest positive integer with exactly $16$ divisors. Explain how the formula $d(n) = \prod (e_i + 1)$ limits the search to a few candidates.

11. • Prove that $d(n)$ is odd if and only if $n$ is a perfect square. Then prove that $\sigma(n)$ is odd if and only if $n$ is a square or twice a square.

12. • Prove that $\gcd(2^a - 1, 2^b - 1) = 2^{\gcd(a, b)} - 1$ for positive integers $a, b$, by showing that one step of Euclid's algorithm on the left side matches one step on the exponents. Use it to find $\gcd(4095, 262143)$.

13. • How many solutions does $7x + 11y = 1000$ have in non-negative integers? Find them all by the method of [solutions in an interval](/linear-diophantine-solutions-in-interval/), not by trying every $x$.

14. • Use [Möbius inversion](/mobius-inversion-formula/) to show that the number of pairs $(a, b)$ with $1 \le a, b \le n$ and $\gcd(a, b) = 1$ is $\sum_{d=1}^{n} \mu(d) \lfloor n/d \rfloor^2$. Evaluate it for $n = 10$.

15. • Compute $D(100) = \sum_{k \le 100} d(k)$ with the [hyperbola method](/dirichlet-hyperbola-method/). How many divisions does it take?

16. • Prove that $\operatorname{lcm}(1, 2, \ldots, n) = \prod_{p \le n} p^{\lfloor \log_p n \rfloor}$, the product over primes. Use it to compute $\operatorname{lcm}(1, \ldots, 10)$.

17. • The subtractive form of Euclid's algorithm replaces the larger of two positive numbers by their difference until they are equal. Show that on $(a, b)$ with $a/b = [a_0; a_1, \ldots, a_k]$ it makes exactly $a_0 + a_1 + \cdots + a_k - 1$ subtractions. What is the largest number of subtractions it makes on a pair with $1 \le a, b \le 100$, and which pairs reach it?

18. • Use [Bézout's identity](/bezouts-identity/) to prove: if $a \mid c$, $b \mid c$ and $\gcd(a, b) = 1$, then $ab \mid c$. Give an example showing that the condition $\gcd(a, b) = 1$ is needed.

19. • Compute a greatest common divisor of $11 + 3i$ and $1 + 8i$ in the Gaussian integers $\mathbb{Z}[i]$, a [Euclidean domain](/euclidean-domain/) with norm $N(x + yi) = x^2 + y^2$. Round each quotient to the nearest Gaussian integer. What is the norm of the gcd?

20. • Use the [divisor sum of the totient](/totient-divisor-sum/) and Möbius inversion to derive $\varphi(n) = \sum_{d \mid n} \mu(d)\, n/d$. Evaluate both this sum and the product formula for $n = 360$.

21. ★ Prove that $\gcd(F_m, F_n) = F_{\gcd(m, n)}$ for the [Fibonacci numbers](/fibonacci-numbers/), with $F_1 = F_2 = 1$.

22. ★ Let $a, b \ge 2$ be coprime. Prove that every integer greater than $ab - a - b$ is $ax + by$ for some non-negative integers $x, y$, and that $ab - a - b$ is not. How many positive integers are not of this form when $a = 7$ and $b = 11$?

23. ★ Prove that $\sum_{k=1}^{n} \gcd(k, n) = \sum_{d \mid n} d\, \varphi(n/d)$, and evaluate the sum for $n = 12$ both ways.

24. ★ In the ring $\mathbb{Z}[\sqrt{-5}]$, show that $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ are two factorizations into irreducible elements that are not associates of each other. Conclude that $\mathbb{Z}[\sqrt{-5}]$ is not a Euclidean domain for any size function.

25. ★ Let $C(n)$ be the number of pairs $(a, b)$ with $1 \le a, b \le n$ and $\gcd(a, b) = 1$. Assuming $\sum_{d \ge 1} \mu(d)/d^2 = 6/\pi^2$, prove that $C(n)/n^2 \to 6/\pi^2$, so two random integers are coprime with probability about $0.61$.
