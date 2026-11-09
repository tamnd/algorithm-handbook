1. ◦ Run the [sieve of Eratosthenes](/sieve-of-eratosthenes/) for $n = 100$, starting each pass at $p^2$. Which primes have passes, how many flags does each pass clear, and how many clear operations are there in all? How many times is the flag of $90$ cleared? Compare the total with the number of composites up to $100$.

2. ◦ Run the [sieve of Sundaram](/sieve-of-sundaram/) for $n = 40$. List the crossed-out values of $x = i + j + 2ij$ and the primes $2x + 1$ that remain.

3. ◦ Run the [linear sieve](/linear-sieve/) for $n = 40$. Which numbers are written while the outer loop is at $i = 15$? At which $i$ is $36$ written? How many writes are there in all?

4. ◦ Follow the [Euler totient sieve](/euler-phi-sieve/) at the entries $m = 36$ and $m = 30$: give the value after each prime that changes it.

5. ◦ Compute $\sum_{m \le 16} d(m)$ with only four divisions, using $\sum_{m \le n} d(m) = \sum_{e \le n} \lfloor n/e \rfloor$ and the symmetry of the pairs $(e, m/e)$, as in the [Dirichlet hyperbola method](/dirichlet-hyperbola-method/).

6. ◦ The number of squarefree integers up to $x$ is $\sum_{d \le \sqrt x} \mu(d) \lfloor x/d^2 \rfloor$. Use it to count the squarefree integers up to $30$, and check the answer by listing the others.

7. ◦ Compute [Legendre's phi function](/legendre-phi-function/) $\phi(50, 4)$ with the recursion $\phi(x, a) = \phi(x, a - 1) - \phi(\lfloor x/p_a \rfloor, a - 1)$, and deduce $\pi(50)$.

8. ◦ For $n = 10^8$, how much memory does a [smallest prime factor table](/smallest-prime-factor-table/) of 32-bit words take? How much does the sieve of Eratosthenes need with one byte per number, with one bit per number, and with one bit per odd number?

9. ◦ The [sieve of Atkin](/sieve-of-atkin/) decides a squarefree $m \equiv 1 \pmod 4$ coprime to $3$ by the parity of the number of solutions of $m = 4x^2 + y^2$ in positive integers. Count the solutions for $m = 221$ and $m = 229$, and say which is prime.

10. • Count the pairs $(i, j)$ that the sieve of Sundaram crosses out, and show that the total is $\Theta(n \log n)$. Show that if the outer loop is restricted to the $i$ for which $2i + 1$ is prime, the sieve becomes the sieve of Eratosthenes on the odd numbers, with $\Theta(n \log \log n)$ steps.

11. • Adapt the linear sieve to compute $\omega(m)$, the number of distinct prime factors, and $\Omega(m)$, the number of prime factors with multiplicity, for all $m \le n$ in $\Theta(n)$. Prove that $\sum_{m \le n} \omega(m) = \sum_{p \le n} \lfloor n/p \rfloor$, and evaluate both sides for $n = 30$.

12. • Show that the number of pairs $(a, b)$ with $1 \le a, b \le n$ and $\gcd(a, b) = 1$ is $\sum_{d \le n} \mu(d) \lfloor n/d \rfloor^2$, and also $2 \sum_{m \le n} \varphi(m) - 1$. Compute it for $n = 10$ both ways.

13. • Write a program that computes $\mu(d)$ for $d \le 100$ with the [Möbius sieve](/mobius-sieve/) and uses Exercise 6 to count the squarefree integers up to $10^4$.

14. • You want the primes in $[10^{12}, 10^{12} + 10^6]$ by the [segmented sieve](/segmented-sieve/). How many base primes are needed? Estimate the number of clear operations, using $\sum_{p \le y} 1/p \approx \ln \ln y + 0.2615$, and the number of primes you will find.

15. • Run the [Lucy_Hedgehog method](/lucy-hedgehog-prime-counting/) for $x = 50$ in its form for sums, with $S(v) = \sum_{2 \le n \le v} n$ at the start and the update $S(v) \leftarrow S(v) - p\,(S(\lfloor v/p \rfloor) - S(p - 1))$. List the values $v$, and give the final $S(50)$.

16. • Apply the [Meissel-Lehmer](/meissel-lehmer-algorithm/) formula $\pi(x) = \phi(x, a) + a - 1 - P_2(x, a)$ to $x = 200$ with $a = \pi(\lfloor x^{1/3} \rfloor)$. Compute $P_2(200, a)$ by the formula $P_2(x, a) = \sum_{p_a < p \le \sqrt x} (\pi(x/p) - \pi(p) + 1)$, and explain why the formula needs no $P_3$ term here.

17. • Let $P = p_1 p_2 \cdots p_a$. Prove that $\phi(x + P, a) = \phi(x, a) + \varphi(P)$, and use it to compute $\phi(1000, 3)$ with almost no work.

18. • A program factors every $m \le n$ with the smallest prime factor table. Show that the total number of divisions is $\sum_{m \le n} \Omega(m) = \sum_{p^k \le n} \lfloor n/p^k \rfloor$, and that this is $n \ln \ln n + O(n)$.

19. • Let $r = \lfloor \sqrt x \rfloor$. Prove that the number of distinct values $\lfloor x/k \rfloor$, $1 \le k \le x$, is $2r$ if $x \ge r(r + 1)$ and $2r - 1$ otherwise. Check it for $x = 50$.

20. ★ Prove that the Lucy_Hedgehog method takes $O(x^{3/4} / \log x)$ updates. Split the primes at $x^{1/4}$: for small $p$, bound the number of values $v \ge p^2$ by $2\sqrt x$; for large $p$, count only the values $\lfloor x/k \rfloor$ with $k \le x/p^2$.

21. ★ Show that an integer $n \le x$ with no prime factor up to $x^{1/3}$ is $1$, a prime, or a product $pq$ of two primes with $x^{1/3} < p \le q$. Use the prime number theorem to show that the number of such $n$ is $(1 + \ln 2 + o(1))\, x / \ln x$, and compare with the [Buchstab function](/buchstab-function/) at $u = 3$.

22. ★ [Brun's sieve](/brun-sieve/) gives $\pi_2(x) = O\big(x (\log \log x)^2 / \log^2 x\big)$ for the number of twin prime pairs up to $x$. Deduce by partial summation that the sum of $1/p$ over the primes $p$ with $p + 2$ prime converges.

23. ★ Prove that a prime $p \equiv 1 \pmod 4$ has exactly one representation $p = 4x^2 + y^2$ in positive integers, so that the sieve of Atkin keeps it. Use the fact that $p$ is a sum of two squares in essentially one way.

24. ★ Use Exercise 12 to prove $\sum_{m \le n} \varphi(m) = 3n^2/\pi^2 + O(n \log n)$, taking $\sum_{d \ge 1} \mu(d)/d^2 = 6/\pi^2$ as known.
