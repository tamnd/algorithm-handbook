1. ◦ Run the [Fermat test](/fermat-primality-test/) on $n = 1387$ with the bases $2$ and $3$. What does each base tell you about $n$?

2. ◦ Use Korselt's criterion to show that $6601 = 7 \cdot 23 \cdot 41$ is a [Carmichael number](/carmichael-number/).

3. ◦ Run one round of the strong test of [Miller-Rabin](/miller-rabin/) on $n = 1387$ with the base $2$. Write $n - 1 = 2^s d$, list the chain of powers, and use the [nontrivial square root of 1](/nontrivial-square-root-of-one/) that appears to split $n$.

4. ◦ Run the [Solovay-Strassen test](/solovay-strassen/) on the Carmichael number $1105$ with the bases $2$ and $3$. You may use $3^{552} \equiv 781 \pmod{1105}$. Which base is a liar and which a witness?

5. ◦ Run the [Lucas-Lehmer test](/lucas-lehmer-test/) on $M_{11} = 2047$: list $s_1, \ldots, s_9$ modulo $2047$ and give the verdict.

6. ◦ Run [Pépin's test](/pepin-test/) on $F_2 = 17$. Then compute $2^{(F_2 - 1)/2} \bmod 17$ and explain why the base $2$ could never prove a Fermat number $F_k$ with $k \ge 2$ prime.

7. ◦ The number $449 = 7 \cdot 2^6 + 1$ is a [Proth number](/proth-prime/). Find the least base $a \ge 2$ with $\left(\frac{a}{449}\right) = -1$, then compute $a^{224} \bmod 449$ by repeated squaring and give the verdict of [Proth's test](/proth-test/).

8. ◦ Write a [Pratt certificate](/pratt-certificate/) for $1009$, using the primitive root $11$. List every entry of the tree, and the powers the checker computes for the top entry.

9. ◦ Find all [strong liars](/strong-liar/) for $n = 25$ and compare their number with the bound $\varphi(n)/4$.

10. ◦ Compute $x / \ln x$ for $x = 10^6$ and compare it with $\pi(10^6) = 78498$. By the [prime number theorem](/prime-number-theorem/), about how many odd integers near $2^{1024}$ must you draw, on average, before one is prime?

11. • Let $n = pq$ with $p \ne q$ odd primes. Prove that the number of Fermat liars for $n$ among the units is $\gcd(n - 1, p - 1) \cdot \gcd(n - 1, q - 1)$, and evaluate it for $n = 1387$.

12. • Prove that a Carmichael number is odd. (Use a single well-chosen base.)

13. • Let $p$ be an odd prime. Prove that if $M_p = 2^p - 1$ is composite, it is a [Fermat pseudoprime](/fermat-pseudoprime/) to the base $2$. Prove the same for every composite Fermat number $F_k = 2^{2^k} + 1$.

14. • The number $x = 2135$ satisfies $x^2 \equiv 1 \pmod{8633}$. Factor $8633$, and explain why, for odd $n$, both $\gcd(x - 1, n)$ and $\gcd(x + 1, n)$ are proper factors whenever $x$ is a nontrivial square root of 1.

15. • In Proth's test the base is the least $a \ge 2$ with $\left(\frac{a}{n}\right) = -1$. Prove that this $a$ is always prime.

16. • Let $p$ be an odd prime and $q$ a prime factor of $M_p = 2^p - 1$. Prove that $q \equiv 1 \pmod{2p}$ and $q \equiv \pm 1 \pmod 8$. Use this to find the least prime factor of $M_{23}$ with a few trial divisions.

17. • Prove that every prime factor of $F_k = 2^{2^k} + 1$ is $\equiv 1 \pmod{2^{k+1}}$. List the primes below $700$ that this allows as factors of $F_5$, and say which one divides it.

18. • Let $p = 2q + 1$ be a [safe prime](/safe-prime/) with $q$ an odd prime. Prove that $g \not\equiv \pm 1$ is a [primitive root](/primitive-root/) modulo $p$ exactly when $\left(\frac{g}{p}\right) = -1$. Find the least primitive root modulo $23$ this way.

19. • A [random prime generator](/random-prime-generation/) for 1024-bit primes draws odd candidates and first removes those with an odd prime factor up to $100$. About what fraction of odd candidates survive, and about how many Miller-Rabin tests does one prime cost on average? Use $\prod_{3 \le p \le 100} (1 - 1/p) \approx 0.241$.

20. • Write a program that counts the Fermat liars, the Euler liars and the strong liars of the Carmichael number $2465 = 5 \cdot 17 \cdot 29$, and compare each count with $\varphi(2465)$.

21. • Use [Bertrand's postulate](/bertrands-postulate/) to prove that $n!$ is not a perfect square for any $n \ge 2$.

22. • Find the least $m$ such that the five integers $m, m + 1, \ldots, m + 4$ are all composite, and give a run of five consecutive composites built from $6!$. What does this say about [prime gaps](/prime-gaps/)?

23. ★ Prove that if $n$ is a Carmichael number and $p$ is a prime factor of $n$, then $p - 1$ divides $n/p - 1$. Deduce that $p < \sqrt n$.

24. ★ Prove that every [strong pseudoprime](/strong-pseudoprime/) to the base $a$ is an [Euler-Jacobi pseudoprime](/euler-jacobi-pseudoprime/) to the base $a$.

25. ★ Let $n \ge 2$ and $\gcd(a, n) = 1$. Prove that $n$ is prime if and only if $(X + a)^n \equiv X^n + a$ in $\mathbb{Z}_n[X]$, the identity behind the [AKS test](/aks-primality-test/).

26. ★ Prove the form of the [Lucas test](/lucas-primality-test/) with a separate base for each prime: if for every prime $q \mid n - 1$ there is an $a_q$ with $a_q^{n-1} \equiv 1$ and $a_q^{(n-1)/q} \not\equiv 1 \pmod n$, then $n$ is prime.
