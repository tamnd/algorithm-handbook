A [prime number](/prime-number/) is an integer $p \ge 2$ whose only positive divisors are $1$ and $p$. Deciding whether a given $n$ is prime looks like a question about dividing, and the obvious method, trial division up to $\sqrt n$, answers it. But the input of a primality test is the binary form of $n$, with $\ell \approx \lg n$ bits, and $\sqrt n = 2^{\ell/2}$ divisions is hopeless for the 1024-bit numbers that an RSA key needs. The methods of this chapter never look for a factor. They check a property that every prime has, such as $a^{n-1} \equiv 1 \pmod n$, and cost a few modular exponentiations, $O(\ell^3)$ bit operations each.

The price is a new kind of answer. A failed check proves that $n$ is composite without giving a factor; a passed check only makes $n$ a probable prime. The chapter is about how to make that answer reliable: by choosing a check that no composite passes for many bases, so that a few random bases make an error unlikely; by proving primality with extra data, a certificate; or by using numbers of a special form, for which an exact test is as fast as a probable one. Every key generator in public-key cryptography runs these tests, and the largest known primes were found with them.

## What the chapter covers

1. **Primes and how they are spread.** The definition, [Bertrand's postulate](/bertrands-postulate/), the [prime number theorem](/prime-number-theorem/) and [prime gaps](/prime-gaps/): the facts that make random search for primes fast.
2. **The problem and the Fermat test.** [Primality testing](/primality-testing/) as a problem on $\ell$-bit inputs, [compositeness witnesses](/compositeness-witness/), [probable primes](/probable-prime/) and [pseudoprimes](/pseudoprime/), the [Fermat test](/fermat-primality-test/), and the [Carmichael numbers](/carmichael-number/) that defeat it.
3. **The Euler test and the strong test.** The [Solovay-Strassen test](/solovay-strassen/), the [nontrivial square roots of 1](/nontrivial-square-root-of-one/), [strong pseudoprimes](/strong-pseudoprime/), and the [Miller-Rabin test](/miller-rabin/) with its [error bound](/miller-rabin-error-bound/) of $1/4$ per round and its [deterministic bases](/deterministic-miller-rabin-bases/) below $2^{64}$.
4. **Stronger tests and prime generation.** The [Baillie-PSW test](/baillie-psw/), the [Frobenius test](/frobenius-test/), [random prime generation](/random-prime-generation/), and [safe primes](/safe-prime/) for cryptography.
5. **Certificates from the factors of n - 1.** [Primality certificates](/primality-certificate/) and the tests of [Lucas](/lucas-primality-test/), [Pratt](/pratt-certificate/) and [Pocklington](/pocklington-primality-test/), which prove primality from the factors of $n - 1$.
6. **Primes of special form.** [Mersenne primes](/mersenne-prime/) and the [Lucas-Lehmer test](/lucas-lehmer-test/), [Fermat primes](/fermat-prime/) and [Pépin's test](/pepin-test/), [Proth primes](/proth-prime/) and [Proth's test](/proth-test/).
7. **General primality proofs.** The [AKS test](/aks-primality-test/), which put primality in polynomial time, the [APR-CL test](/apr-cl-primality-test/) and [elliptic curve primality proving](/ecpp/).

## A first reading

Read these in order:

1. [Prime number](/prime-number/)
2. [Primality testing](/primality-testing/)
3. [Compositeness witness](/compositeness-witness/)
4. [Probable prime](/probable-prime/)
5. [Fermat primality test](/fermat-primality-test/)
6. [Carmichael number](/carmichael-number/)
7. [Nontrivial square root of 1](/nontrivial-square-root-of-one/)
8. [Strong pseudoprime](/strong-pseudoprime/)
9. [Miller-Rabin](/miller-rabin/)
10. [Random prime generation](/random-prime-generation/)
11. [Primality certificate](/primality-certificate/)
12. [Lucas-Lehmer test](/lucas-lehmer-test/)

With these you can test and generate primes as real libraries do, and you know what a proof of primality adds. Leave the proof of the Miller-Rabin bound, the Frobenius test and the three general proofs of the last group for a second reading; AKS, APR-CL and ECPP use algebra beyond this volume. The prime number theorem can be taken as a fact at first.

## Before you start

The chapter uses [divisibility and the gcd](/greatest-common-divisor/) from Chapter 10.1 and most of Chapter 10.2: [congruences](/congruence/), [modular exponentiation](/modular-exponentiation/), [Fermat's little theorem](/fermat-little-theorem/), the [Chinese remainder theorem](/chinese-remainder-theorem/), [multiplicative order](/multiplicative-order/), [primitive roots](/primitive-root/), [Euler's criterion](/euler-criterion/) and the [Jacobi symbol](/jacobi-symbol/). The randomized tests are Monte Carlo algorithms with one-sided error, and the results on certificates are stated with the classes P and NP. [Trial division](/trial-division/) is treated with factoring, in Chapter 10.4. The general proofs of the last group need [polynomial rings](/polynomial-ring/) and, for ECPP, elliptic curves as used in elliptic curve cryptography.
