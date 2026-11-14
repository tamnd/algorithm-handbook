1. ◦ Registers in this chapter hold integers in binary. Qubit 0 is the least significant bit, and it is the rightmost symbol in a ket. A 4-qubit exponent register is in the state $|1010\rangle$. Which integer does it hold, and which qubits are 1? Write the kets for $x = 3$ and $x = 12$.

2. ◦ Take $N = 33$ and $a = 5$. Find the [order](/order-finding/) $r$ of 5 modulo 33, compute $a^{r/2} \bmod 33$, and use [Miller's reduction](/factoring-to-order-finding/) to split 33.

3. ◦ To factor $N = 2021$ with [Shor's algorithm](/shor-algorithm/), find the bit length $n$ and the least $t$ with $2^t \ge N^2$. The [modular exponentiation](/quantum-modular-exponentiation/) circuit of the chapter uses $t + n$ data qubits and $2n + 4$ ancillas. How many qubits is that in all?

4. ◦ For $N = 35$ and $a = 2$, one run with $Q = 2^{11}$ measures $c = 853$. Check that $Q \ge N^2$. List the [convergents](/continued-fraction-post-processing/) of $853/2048$, find the first one whose denominator $q$ has $2^q \equiv 1 \pmod{35}$, and check that it lies within $1/(2Q)$ of $c/Q$.

5. ◦ In $\mathbb{Z}_{11}^*$ the element $g = 2$ has order $r = 10$. One run of [Shor's discrete logarithm algorithm](/quantum-discrete-logarithm/) for $h = g^x$ returns $(c, d) = (3, 9)$, where $d \equiv -xc \pmod{10}$. Find $x$ and $h$.

6. ◦ The expected number of runs of the discrete logarithm algorithm is $\sum_{t \ge 0}\bigl(1 - \prod_{p \mid r}(1 - p^{-t})\bigr)$ over the primes $p$ that divide $r$. Evaluate it for $r = 11$ and for $r = 16$.

7. ◦ Expand $\sqrt{11}$ as a [continued fraction](/continued-fraction/), find the fundamental solution of [Pell's equation](/pell-equation/) $x^2 - 11y^2 = 1$, and give the regulator $R = \ln(x_1 + y_1\sqrt{11})$ to four decimals.

8. ◦ A [Gauss sieve](/gauss-sieve/) in dimension $n$ keeps a list of about $N = (4/3)^{n/2}$ vectors and makes about $N$ searches through it. Write $N$, the classical time $N^2$, and the time $N^{3/2}$ of [quantum sieving](/quantum-sieving/) with Grover search as powers $2^{cn}$. Give the exponents of 2 for $n = 400$.

9. ◦ An RSA-2048 modulus has two 1024-bit primes, so the [short discrete logarithm](/short-discrete-logarithm/) $d = (p + q - 2)/2$ has $m = 1024$ bits. How many exponent bits does one run of the [Ekerå-Håstad algorithm](/ekera-hastad-algorithm/) with $s = 8$ use? Compare with the exponent register of Shor's algorithm.

10. • Count the units $a$ modulo $N = 35$ for which Miller's reduction succeeds, that is, the order $r$ is even and $a^{r/2} \not\equiv -1$. List the bad units and say why each fails. Compare the fraction with the bound $1 - 2^{1-k}$.

11. • Take $N = 33$ and $a = 5$, so $r = 10$. Suppose each run of order finding returns the reduced fraction $s/r$ for a uniform $s \in \{0, \ldots, 9\}$. What is the probability that one run gives the denominator 10? What is the probability that the lcm of the denominators of two runs is 10?

12. • With $p = 11$, $g = 2$ and $r = 10$ as in Exercise 5, a run for some other $h$ returns $(c, d) = (4, 2)$. Which values of $x$ does it allow? A second run returns $(5, 5)$. Find $x$. What is the probability that a single run fixes $x$?

13. • Evaluate the expected number of runs of Exercise 6 exactly for $r = 10$.

14. • Let $N = 1147 = 31 \cdot 37$ and $g = 2$. Show that $g^{(N-1)/2} \equiv g^d \pmod N$ with $d = (p + q - 2)/2$, and find $d$. Then assume you know only $N$ and $d$, and recover $p$ and $q$.

15. • An RSA key has $N = 1189$ and $e = 3$, and the private exponent is $d = 747$. Factor $N$ from $ed - 1$ by the squaring sequence: write $ed - 1 = 2^s o$ with $o$ odd and square $a^o$ until it reaches 1. Try $a = 2$ and then $a = 3$.

16. • List the reduced forms $(a, b, c)$ of discriminant $\Delta = -56$, with $|b| \le a \le c$. Find the class number and the structure of the [class group](/ideal-class-group/).

17. • In the [quantum class group algorithm](/quantum-class-group-algorithm/) for $\Delta = -56$, take the generators $g_1 = (2, 0, 7)$ of order 2 and $g_2 = (3, 2, 5)$ of order 4, so $G = \mathbb{Z}_2 \times \mathbb{Z}_4$. Find the relation subgroup $H$ and its dual $H^\perp$. What is the probability that one sample generates $H^\perp$, and how many samples are needed on average?

18. • Expand $\sqrt{19}$ as a continued fraction. Find the fundamental solution of $x^2 - 19y^2 = 1$, decide whether $x^2 - 19y^2 = -1$ has a solution, and give the regulator to four decimals.

19. • In $\mathbb{Z}[\sqrt{-5}]$ let $I = (3, 1 + \sqrt{-5})$, an ideal of norm 3. Show that $I$ is not principal and that $I^2$ is, and find a generator of $I^2$. This is a small case of the [principal ideal problem](/principal-ideal-problem/).

20. • Use the model $p_L = (p/p_{\mathrm{th}})^{(d+1)/2}$ for the logical error per surface code patch and round, with $p/p_{\mathrm{th}} = 1/10$ and odd distance $d$, and $2d^2$ physical qubits per patch. Find the least $d$ with $p_L \le 10^{-16}$, the physical qubits per patch, and the physical qubits for 6190 logical qubits without factories or routing. See [resource estimation](/quantum-resource-estimation-factoring/).

21. • Count the points of the curve $y^2 = x^3 + 2x + 2$ over $\mathbb{F}_{17}$, including the point at infinity. Show that $P = (5, 1)$ generates the group, and find $k$ with $kP = (10, 6)$. If the [quantum elliptic curve discrete logarithm](/quantum-elliptic-curve-discrete-log/) algorithm uses transforms over $\mathbb{Z}_r$ for the group order $r$, what is the probability that one run fixes $k$?

22. ★ For $N = pq$ with distinct odd primes, let $v_i$ be the exponent of 2 in the order of $a$ modulo $p_i$. Show that $a$ is bad for Miller's reduction exactly when $v_1 = v_2$. Use this to find the fraction of good units for $N = 77$ and for $N = 65$, and explain why only the first meets the bound $1/2$ with equality.

23. ★ Order finding takes $Q \ge N^2$. Show that this makes the fraction found by continued fractions unique: two distinct fractions with denominators below $N$ cannot both lie within $1/(2Q)$ of $c/Q$. Then take $N = 21$ and the smaller $Q = 256$, and find a $c$ for which two such fractions exist.

24. ★ [Hallgren's algorithm](/hallgren-pell-algorithm/) for $D = 11$ with scale $N = 3$ and $q = 256$ samples integers $c$ near $jq/S$ for integers $j$, where $S = NR$. Two runs give $c_1 = 57$ and $c_2 = 86$. Assume that their $j$ values are coprime and below 5. Find $j_1$ and $j_2$ from the continued fraction of $c_1/c_2$, estimate $R$, and find the unit $x + y\sqrt{11}$ that the estimate points to.

25. ★ Show that the expected number of runs of Exercise 6 is at most $2 + \sum_p \frac{1}{p(p-1)}$ over all primes $p$, for every $r$, and evaluate this bound. Then find the exact supremum over $r$ in terms of the zeta function, and evaluate it.

26. ★ In [Regev's algorithm](/regev-factoring-algorithm/) for $N = 55$ with the bases $b = (2, 3)$ and $a_i = b_i^2$, the lattice is $L = \{z \in \mathbb{Z}^2 : 4^{z_1} 9^{z_2} \equiv 1 \pmod{55}\}$. Find $\det L$ and a basis of $L$ of two vectors of squared length 10. For each basis vector $u$, compute $x = 2^{u_1} 3^{u_2} \bmod 55$ and say whether it splits 55.
