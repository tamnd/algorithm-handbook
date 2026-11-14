Take $N = 15$ and $a = 7$. The powers of 7 modulo 15 are 7, 4, 13, 1, and then they repeat, so the [multiplicative order](/multiplicative-order/) of 7 is $r = 4$. The order is even, so $7^2 \equiv 4$ is a square root of 1, and $\gcd(4 - 1, 15) = 3$ and $\gcd(4 + 1, 15) = 5$ split 15. This step works for any $N$: an even order $r$ with $a^{r/2} \not\equiv -1 \pmod N$ gives a factor. The hard part is $r$ itself. For a 2048-bit $N$ the order can have hundreds of digits, and no classical method is known that finds it in polynomial time. No one has proved that such a method cannot exist either.

A quantum computer finds $r$ by interference. It writes all exponents $x$ at once, computes $a^x \bmod N$ into a second register, and applies an inverse [quantum Fourier transform](/quantum-fourier-transform/) to the exponents. The outcome is an integer $c$ near $sQ/r$ for a random $s$, where $Q = 2^t \ge N^2$, and the continued fraction of $c/Q$ gives $r$ or a divisor of it. Registers hold integers in binary. Qubit 0 is the least significant bit, and it is the rightmost symbol in a ket, so $|0110\rangle$ is the integer 6.

This is [Shor's algorithm](/shor-algorithm/). It factors an $n$-bit integer with $O(n^3)$ gates per run and an expected constant number of runs, in the gate model and with a final classical check, so a wrong answer is never returned. The same Fourier sampling solves discrete logarithms in $\mathbb{Z}_p^*$ and on elliptic curves, and with an irrational period it solves the Pell equation and computes class groups. The chapter keeps three kinds of claims apart. Polynomial gate counts are proved, some of them only under the generalized Riemann hypothesis, and Regev's algorithm rests on a stated heuristic. Classical hardness is conjecture. Physical qubit counts and run times are estimates under a hardware model.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Order finding and its classical steps.** [Order finding](/order-finding/) as phase estimation, the [continued fraction step](/continued-fraction-post-processing/) that reads $r$ from a measured integer, and [Miller's reduction](/factoring-to-order-finding/) from factoring to order finding.
2. **Reversible arithmetic.** Circuits for [modular exponentiation](/quantum-modular-exponentiation/), the [binary GCD](/quantum-gcd/) and [modular inversion](/quantum-modular-inversion/), with their Toffoli and qubit counts.
3. **Shor's factoring algorithm and its cost.** The full algorithm, the proof of [factoring in BQP](/factoring-in-bqp/), and [resource estimation](/quantum-resource-estimation-factoring/) from logical gates to physical qubits.
4. **Discrete logarithms.** [Shor's discrete logarithm algorithm](/quantum-discrete-logarithm/), the [membership proof](/discrete-logarithm-in-bqp/), and the [elliptic curve version](/quantum-elliptic-curve-discrete-log/).
5. **Shorter circuits for factoring.** The [short discrete logarithm problem](/short-discrete-logarithm/), the [Ekerå-Håstad algorithm](/ekera-hastad-algorithm/) and [Regev's algorithm](/regev-factoring-algorithm/).
6. **Problems in number fields.** The [Pell equation](/pell-equation/), the [unit group](/unit-group/), the [class group](/ideal-class-group/) and the [principal ideal problem](/principal-ideal-problem/).
7. **Quantum algorithms for number fields and lattices.** [Hallgren's algorithm for Pell's equation](/hallgren-pell-algorithm/), the [quantum class group algorithm](/quantum-class-group-algorithm/), the [quantum principal ideal algorithm](/quantum-principal-ideal-algorithm/) and [quantum lattice sieving](/quantum-sieving/).

## A first reading

For a short path through the chapter, read these in order.

1. Order finding, the problem and its phase estimation circuit.
2. Continued fraction post-processing, why $Q \ge N^2$ is enough.
3. Factoring to order finding, why at least half the bases work.
4. Quantum modular exponentiation, where the gates go.
5. Shor's algorithm, the whole method on $N = 15$ and $N = 21$.
6. Quantum discrete logarithm, two registers and one linear congruence per run.
7. Quantum elliptic curve discrete logarithm, the attack on elliptic curve keys.
8. Quantum resource estimation for factoring, what a 2048-bit attack would take and under which assumptions.
9. Pell's equation and then Hallgren's algorithm, period finding with an irrational period.
10. Quantum sieving, why lattice problems do not fall the same way.

## Before you start

The quantum side needs [quantum phase estimation](/quantum-phase-estimation/), the quantum Fourier transform, the [Toffoli gate](/toffoli-gate/) and [uncomputation](/uncomputation/) from Chapter 30.1, and [Grover search](/grover-search/) from Chapter 30.2 for the last entry. The number theory is in Volume 10: [modular exponentiation](/modular-exponentiation/), the [Euclidean algorithm](/euclidean-algorithm/) and [binary GCD](/binary-gcd/), [continued fraction convergents](/continued-fraction-convergents/), the [Chinese remainder theorem](/chinese-remainder-theorem/), the [discrete logarithm problem](/discrete-logarithm-problem/), and for the last groups [lattices](/lattice/), the [LLL algorithm](/lll-algorithm/) and the [shortest vector problem](/shortest-vector-problem/). The classical rivals are there too, the [general number field sieve](/general-number-field-sieve/) and [Pollard's rho](/pollard-rho-discrete-logarithm/). The schemes under attack are in Volume 23: [RSA](/rsa-cryptosystem/), [Diffie-Hellman](/diffie-hellman/), [elliptic curve cryptography](/elliptic-curve-cryptography/) and [post-quantum cryptography](/post-quantum-cryptography/). The [Smith normal form](/smith-normal-form/) of Volume 11 appears in the class group algorithm.
