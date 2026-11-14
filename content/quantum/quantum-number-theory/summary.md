## What to remember

- [Order finding](/order-finding/) prepares $\sum_x |x\rangle|a^x \bmod N\rangle$ over $t$ exponent qubits with $Q = 2^t \ge N^2$ and applies the inverse Fourier transform. The outcome $c$ satisfies $|c/Q - s/r| \le 1/(2Q)$ with constant probability, and then $s/r$ is a [convergent](/continued-fraction-post-processing/) of $c/Q$, the only fraction with denominator below $N$ that close. A run gives $r/\gcd(s, r)$, so a few runs or an lcm give $r$.
- [Miller's reduction](/factoring-to-order-finding/): if $r$ is even and $y = a^{r/2} \not\equiv -1$, then $\gcd(y - 1, N)$ is a proper factor. For odd $N$ with $k \ge 2$ distinct prime factors, a random unit is good with probability at least $1 - 2^{1-k} \ge 1/2$. Prime powers need a separate test.
- [Shor's algorithm](/shor-algorithm/) costs $O(n^3)$ gates per run with schoolbook arithmetic and $O(n^2\log n\log\log n)$ with fast multiplication, fits in about $2n$ logical qubits with Beauregard's circuit, and checks its answer, so it never returns a wrong factor. Factoring is in BQP, but no one has proved that it is outside classical polynomial time.
- Nearly all the gates go into reversible arithmetic: [modular exponentiation](/quantum-modular-exponentiation/) needs about $40n^3$ to $64n^3$ Toffoli gates in the schoolbook circuit of its entry, and [inversion](/quantum-modular-inversion/) runs a fixed $2n - 1$ rounds of the [binary GCD](/quantum-gcd/) because a circuit cannot stop early.
- [Shor's discrete logarithm algorithm](/quantum-discrete-logarithm/) measures pairs $(c, d)$ with $d \equiv -xc \pmod r$ for $h = g^x$ of known order $r$. It is done when the $c_i$ have no common prime factor with $r$, which takes fewer than 2.775 runs on average. On [elliptic curves](/quantum-elliptic-curve-discrete-log/) the group operation is point addition.
- Each [resource estimate](/quantum-resource-estimation-factoring/) holds for its hardware model only. Gidney and Ekerå (2021) estimate 20 million physical qubits and 8 hours for RSA-2048 at a physical error rate of $10^{-3}$ and a 1 µs surface code cycle; Gidney (2025) estimates under a million qubits and under a week.
- The [Ekerå-Håstad algorithm](/ekera-hastad-algorithm/) factors RSA through the short logarithm $d = (p + q - 2)/2$ with $(\frac12 + \frac1s)\log_2 N$ exponent bits per run. [Regev's algorithm](/regev-factoring-algorithm/) uses $\sqrt n + 4$ runs of $O(n^{3/2}\log n)$ gates, under a heuristic assumption.
- [Hallgren's algorithm](/hallgren-pell-algorithm/) finds a period $S = NR$ that is irrational by sampling $f(k) = (I, \lfloor k - N\delta(I)\rfloor)$ on integers, and gives the regulator $R$ of $\mathbb{Q}(\sqrt D)$ in time polynomial in $\log D$. The [class group](/quantum-class-group-algorithm/) and the [principal ideal problem](/quantum-principal-ideal-algorithm/) follow, the first under GRH.
- [Quantum sieving](/quantum-sieving/) lowers the heuristic SVP time from $2^{0.292n}$ to $2^{0.257n}$, counting a QRAM query as one step. It is still exponential.

| Problem | Quantum method | Quantum cost | Best known classical |
|---|---|---|---|
| Factoring, order finding | [Shor](/shor-algorithm/) | $O(n^3)$ gates, $O(1)$ expected runs | [number field sieve](/general-number-field-sieve/), $\exp(O(n^{1/3}(\log n)^{2/3}))$, heuristic |
| Factoring | [Regev](/regev-factoring-algorithm/) | $O(n^{3/2}\log n)$ gates, $\sqrt n + 4$ runs, heuristic | the same |
| RSA via a short logarithm | [Ekerå-Håstad](/ekera-hastad-algorithm/) | $\approx(\frac12 + \frac1s)\log_2 N$ controlled multiplications per run | the same |
| Discrete log in $\mathbb{Z}_p^*$ | [Shor](/quantum-discrete-logarithm/) | $O(n^3)$ gates, under 2.775 expected runs | number field sieve, $L_p[1/3]$, heuristic |
| Elliptic curve discrete log | [Shor with point addition](/quantum-elliptic-curve-discrete-log/) | $O(n^3)$ gates, about $9n$ logical qubits | [Pollard's rho](/pollard-rho-discrete-logarithm/), $\sqrt{\pi r/2}$ |
| Pell, regulator | [Hallgren](/hallgren-pell-algorithm/) | $\mathrm{poly}(\log D)$ | subexponential under GRH |
| Class group, principal ideals | [Hallgren](/quantum-class-group-algorithm/), [Biasse-Song](/quantum-principal-ideal-algorithm/) | polynomial; class group under GRH | subexponential, mostly under GRH |
| Shortest vector | [quantum sieve](/quantum-sieving/) | $2^{0.257n}$ with QRAM, heuristic | [sieve](/lattice-sieving/), $2^{0.292n}$, heuristic |

: The main problems and the best known methods. $n$ is the bit length of the modulus or the group order, or the lattice dimension for the shortest vector. Quantum costs are logical gate counts in the noiseless gate model.

## Choosing a method

To factor on a fault-tolerant machine, use an optimized form of Shor's algorithm with windowed arithmetic. For RSA moduli, the Ekerå-Håstad reduction shortens each run, and the 2021 estimate of Gidney and Ekerå uses it. Regev's algorithm has smaller runs but more of them and more qubits, and it rests on a heuristic, so today it is a research subject rather than a practical choice.

For discrete logarithms, use the two-register algorithm when the group order is known, and the short logarithm version when the exponent is short or the order is unknown. Elliptic curve keys need fewer qubits to attack than RSA keys of the same classical security.

For number fields of small degree, use Hallgren's methods; for large degree, the $S$-unit method of Biasse and Song. On classical machines, use the number field sieve, Pollard's rho and the subexponential relation methods.
