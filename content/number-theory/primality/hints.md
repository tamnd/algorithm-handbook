1. $2^{1386} \equiv 1 \pmod{1387}$, so the base $2$ is a liar and says nothing; $3^{1386} \equiv 875$, so the base $3$ is a witness and $1387 = 19 \cdot 73$ is composite.

3. $1386 = 2 \cdot 693$, so $s = 1$, $d = 693$. Then $2^{693} \equiv 512$, which is not $\pm 1$, and $512^2 \equiv 1$. So $512$ is a nontrivial square root of 1, $\gcd(511, 1387) = 73$ and $\gcd(513, 1387) = 19$.

4. $1105 \equiv 1 \pmod 8$, so $\left(\frac{2}{1105}\right) = 1$, and $2^{552} \equiv 1$: the base $2$ is an Euler liar. $\left(\frac{3}{1105}\right) = \left(\frac{1105}{3}\right) = \left(\frac{1}{3}\right) = 1$, but $3^{552} \equiv 781 \not\equiv 1$: the base $3$ is a witness.

6. $3^8 \equiv 16 \equiv -1 \pmod{17}$, so $17$ is prime. But $2^8 \equiv 1$. In general $2^{2^k} \equiv -1 \pmod{F_k}$, so $2$ has order $2^{k+1}$, and for $k \ge 2$ this divides $(F_k - 1)/2 = 2^{2^k - 1}$; so $2^{(F_k - 1)/2} \equiv 1$ for every such $F_k$, prime or not.

8. $1008 = 2^4 \cdot 3^2 \cdot 7$. The entries, children first: $(3, 2, \{2{:}1\})$, $(7, 3, \{2{:}1, 3{:}1\})$, $(1009, 11, \{2{:}4, 3{:}2, 7{:}1\})$. For the top entry the checker verifies $11^{1008} \equiv 1$ and $11^{504} \equiv 1008$, $11^{336} \equiv 374$, $11^{144} \equiv 935$, none of them $1$.

11. The Fermat liars are the solutions of $a^{n-1} \equiv 1$ in the units. By the Chinese remainder theorem they are pairs of solutions modulo $p$ and modulo $q$, and in the cyclic group of units modulo $p$ the equation $x^{n-1} = 1$ has $\gcd(n - 1, p - 1)$ solutions. For $1387$: $\gcd(1386, 18) \cdot \gcd(1386, 72) = 18 \cdot 18 = 324$ of the $1296$ units.

14. $\gcd(2134, 8633) = 97$ and $8633 = 89 \cdot 97$. Since $n \mid (x - 1)(x + 1)$ and $\gcd(x - 1, x + 1) \mid 2$, each prime power of the odd $n$ divides exactly one factor; they cannot all go to the same one, since $n$ divides neither.

16. The order of $2$ modulo $q$ divides the prime $p$ and is not $1$, so it is $p$, and $p \mid q - 1$; as $q$ is odd, $2p \mid q - 1$. Also $2 \equiv 2^{p+1} = (2^{(p+1)/2})^2$ is a square modulo $q$, so $q \equiv \pm 1 \pmod 8$. For $p = 23$ the first candidate is $47 \equiv 7 \pmod 8$, and $2^{23} - 1 = 47 \cdot 178481$.

17. The order of $2$ modulo $q$ divides $2^{k+1}$ but not $2^k$, since $2^{2^k} \equiv -1$. So it is $2^{k+1}$, which divides $q - 1$. For $k = 5$ the primes $\equiv 1 \pmod{64}$ below $700$ are $193, 257, 449, 577, 641$, and $641$ divides $F_5$.

18. The order of $g$ divides $2q$; it is $1$ or $2$ only for $g \equiv \pm 1$, and it divides $q$ exactly when $g^q = g^{(p-1)/2} \equiv 1$, that is when $\left(\frac{g}{p}\right) = 1$ by Euler's criterion. Modulo $23$: $\left(\frac{2}{23}\right) = \left(\frac{3}{23}\right) = \left(\frac{4}{23}\right) = 1$ and $\left(\frac{5}{23}\right) = -1$, so the answer is $5$.

23. Write $n = pm$. Then $n - 1 = (p - 1)m + (m - 1)$, and $p - 1 \mid n - 1$ gives $p - 1 \mid m - 1$. Since $m > 1$, $m \ge p$, and $m \ne p$ as $n$ is squarefree.

24. Write $n - 1 = 2^s t$. If $a^t \equiv 1$, both sides are $1$, because $\left(\frac{a}{n}\right) = \left(\frac{a}{n}\right)^t = \left(\frac{a^t}{n}\right)$. If $a^{2^r t} \equiv -1$, the order of $a$ modulo each prime $p \mid n$ has $2$-part exactly $2^{r+1}$; so $\left(\frac{a}{p}\right) = -1$ exactly when $2^{r+1} \parallel p - 1$. Count these primes with multiplicity, call the count $N$, and compute $n$ modulo $2^{r+2}$: $N$ is odd exactly when $r = s - 1$, which is when $a^{(n-1)/2} \equiv -1$.

25. For prime $n$ the middle binomial coefficients vanish modulo $n$ and $a^n \equiv a$. For composite $n$, take a prime $q$ with $q^k \parallel n$: then $q^k \nmid \binom{n}{q}$, so the coefficient $\binom{n}{q} a^{n-q}$ of $X^q$ is not $0$ modulo $n$.

26. The order of $a_q$ modulo $n$ divides $n - 1$ but not $(n-1)/q$, so it is divisible by the full power $q^e \parallel n - 1$. All these orders divide $\varphi(n)$, so $n - 1 \mid \varphi(n)$; as $\varphi(n) \le n - 1$, $\varphi(n) = n - 1$ and $n$ is prime.
