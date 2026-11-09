1. ◦ Compute $3^{200} \bmod 13$ in two ways: with [Fermat's little theorem](/fermat-little-theorem/), and by noting the order of $3$ modulo $13$. How many squarings and how many extra multiplications does left-to-right [binary exponentiation](/binary-exponentiation/) use for the exponent $200$?

2. ◦ Find the [inverse](/modular-inverse/) of $37$ modulo $101$ with the extended Euclidean algorithm. Check your answer against $37^{99} \bmod 101$.

3. ◦ List all solutions $x \in \{0, \ldots, 99\}$ of $14x \equiv 30 \pmod{100}$. How many does the theory of [linear congruences](/linear-congruence/) predict before you solve?

4. ◦ Find the $x$ with $0 \le x < 900$ such that $x \equiv 1 \pmod 4$, $x \equiv 2 \pmod 9$ and $x \equiv 3 \pmod{25}$, using the [Chinese remainder theorem](/chinese-remainder-theorem/).

5. ◦ Compute $\varphi(1000)$ and $\varphi(720)$ with the product formula for [Euler's totient](/euler-totient/).

6. ◦ Find the [order](/multiplicative-order/) of $2$ modulo $11$. List all [primitive roots](/primitive-root/) modulo $11$ and check that there are $\varphi(\varphi(11))$ of them.

7. ◦ List the [quadratic residues](/quadratic-residue/) modulo $13$. Use [Euler's criterion](/euler-criterion/) to decide whether $5$ is one, and compare with your list.

8. ◦ Use [Lucas's theorem](/lucas-theorem/) to compute $\binom{1000}{300} \bmod 7$. Write $1000$ and $300$ in base $7$ first.

9. ◦ Use [Wilson's theorem](/wilson-theorem/) to find $10! \bmod 11$ and $15! \bmod 17$ without multiplying out the factorials.

10. ◦ Use the [batch modular inverse](/batch-modular-inverse/) method to invert $2, 3, 5, 7$ modulo $11$ with a single inversion. Show the prefix products and the values you peel off.

11. • Take $n = 97$ and $R = 128$ for [Montgomery multiplication](/montgomery-multiplication/). Compute $n' = -n^{-1} \bmod R$ and the Montgomery forms of $5$ and $7$. Run one REDC on the product of these forms and check that the result is the Montgomery form of $35$.

12. • Prove that if $p \equiv 3 \pmod 4$ is prime and $a$ is a quadratic residue modulo $p$, then $a^{(p+1)/4}$ is a square root of $a$. Use it to find both square roots of $5$ modulo $19$.

13. • Run the [Tonelli-Shanks algorithm](/tonelli-shanks/) on $p = 41$, $a = 5$, with the nonresidue $z = 3$. Show $q$, $s$ and the values of the loop variables at each step.

14. • Compute the [Jacobi symbol](/jacobi-symbol/) $\left(\frac{2023}{3001}\right)$ by reciprocity, without factoring. Then show that $\left(\frac{2}{15}\right) = 1$ although $2$ is not a square modulo $15$.

15. • Find the [Pisano periods](/pisano-period/) $\pi(7)$ and $\pi(11)$. Check that $\pi(11)$ divides $11 - 1$ and $\pi(7)$ divides $2(7 + 1)$, as the entry predicts, and find $F_{10^{18}} \bmod 11$.

16. • Solve $x \equiv 3 \pmod 6$, $x \equiv 5 \pmod 8$, whose moduli are not coprime. Then show that $x \equiv 2 \pmod 6$, $x \equiv 5 \pmod 8$ has no solution. State the condition for two congruences to be compatible.

17. • Compute the [Carmichael function](/carmichael-function/) $\lambda(10^6)$ and compare it with $\varphi(10^6)$. What is the largest order of an element modulo $10^6$?

18. • How many solutions does $x^2 \equiv 1 \pmod{105}$ have? List them, and explain the count with the Chinese remainder theorem.

19. • Given that 1 January 2000 has [Julian day number](/julian-day-number/) $2451545$ and was a Saturday, find the Julian day number of 4 July 1776 in the Gregorian calendar and the day of the week it fell on.

20. • Show that the subtractions in [Barrett reduction](/barrett-reduction/) cannot be dropped: for $n = 13$ with $k = 4$, find the smallest $x < 4^k$ whose first estimate $x - \lfloor x \mu / 4^k \rfloor n$ is at least $n$. Here $\mu = \lfloor 4^k / n \rfloor$.

21. • Prove that $n^{13} - n$ is divisible by $2730$ for every integer $n$.

22. ★ Prove that there is no primitive root modulo $2^k$ for $k \ge 3$, by showing that $a^{2^{k-2}} \equiv 1 \pmod{2^k}$ for every odd $a$.

23. ★ Prove that the product of all elements of a finite abelian group equals the product of its elements of order $2$, and that this is the identity unless the group has exactly one element of order $2$. Deduce Wilson's theorem, and find the product of the units modulo $15$.

24. ★ Let $p$ be an odd prime. Prove that $\sum_{a=0}^{p-1} \left(\frac{a(a+1)}{p}\right) = -1$.

25. ★ Prove the supplement $\left(\frac{2}{p}\right) = 1$ if and only if $p \equiv \pm 1 \pmod 8$, using Gauss's lemma: $\left(\frac{a}{p}\right) = (-1)^m$, where $m$ is the number of $a, 2a, \ldots, \frac{p-1}{2}a$ whose least positive residue exceeds $p/2$.

26. ★ Let $n = pq$ with $p, q$ distinct odd primes. Suppose a black box returns some square root modulo $n$ of any square you give it. Show how to factor $n$ with an expected constant number of calls to the box. (This is Rabin's result that [modular square roots](/modular-square-root/) are as hard as factoring.)
