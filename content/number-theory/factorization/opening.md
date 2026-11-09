To factor an integer is to write it as a product of primes. The [fundamental theorem of arithmetic](/fundamental-theorem-of-arithmetic/) says the product exists and is unique, and [primality tests](/primality-testing/) can tell in a fraction of a second whether a 1000-digit number is prime. Yet nobody knows how to find the factors of a 600-digit product of two primes, and the RSA cryptosystem depends on that. [Integer factorization](/integer-factorization/) is the clearest example in the book of a problem whose answer is easy to check and, as far as anyone knows, hard to find: the size of the input is the bit length $n$ of $N$, and no classical method runs in time polynomial in $n$.

The methods of this chapter fall into three families. The exponential ones, such as trial division and Pollard's rho, cost a power of $N$ or of its least prime factor $p$; they are simple and they are the right tool for small numbers and small factors. The group methods, Pollard's $p - 1$ and the elliptic curve method, succeed when some group order is a product of small primes. The sieve methods build a congruence $x^2 \equiv y^2 \pmod N$ from many small pieces, and reach subexponential time, written with $L_N[\alpha, c] = \exp\big((c + o(1)) (\ln N)^\alpha (\ln \ln N)^{1 - \alpha}\big)$. The number field sieve, at $L_N[1/3, (64/9)^{1/3}]$, has set every record for general numbers since the mid-1990s, up to the 250-digit RSA-250 in 2020.

## What the chapter covers

1. **The problem and trial division.** The [problem](/integer-factorization/) itself, [trial division](/trial-division/) with its $O(\sqrt N)$ bound, and [wheel factorization](/wheel-factorization/), which skips divisors that share a factor with $30$ or another small primorial.
2. **Differences of squares.** [Fermat's method](/fermat-factorization/) for factors close to $\sqrt N$, and [Lehman's method](/lehman-factorization/) and [Hart's one line algorithm](/hart-one-line-factorization/), which apply it to multiples of $N$ and reach about $N^{1/3}$.
3. **Rho and the square root barrier.** [Pollard's rho](/pollard-rho/) and [Brent's variant](/brent-pollard-rho/), which find $p$ in about $\sqrt p$ steps, and the deterministic [Pollard-Strassen algorithm](/pollard-strassen/).
4. **Smooth numbers and group methods.** [Smooth numbers](/smooth-number/) and the [Dickman function](/dickman-function/) that counts them, [Pollard's $p - 1$ method](/pollard-p-minus-1/), [Williams' $p + 1$ method](/williams-p-plus-1/) and the [elliptic curve method](/elliptic-curve-factorization/).
5. **Congruences of squares.** The [congruence of squares](/congruence-of-squares/), the central idea of every fast method, [relation collection](/relation-collection/), and three ways to get relations: [Dixon's random squares](/dixon-random-squares/), [CFRAC](/continued-fraction-factorization/) and [SQUFOF](/shanks-squfof/).
6. **The sieves.** The [quadratic sieve](/quadratic-sieve/), its [multiple polynomial form](/multiple-polynomial-quadratic-sieve/), the [Knuth-Schroeppel multiplier](/knuth-schroeppel-multiplier/), and the [general](/general-number-field-sieve/) and [special](/special-number-field-sieve/) number field sieves.

## A first reading

1. [Integer factorization](/integer-factorization/)
2. [Trial division](/trial-division/)
3. [Fermat's factorization method](/fermat-factorization/)
4. [Pollard's rho algorithm](/pollard-rho/)
5. [Smooth number](/smooth-number/)
6. [Pollard's p - 1 algorithm](/pollard-p-minus-1/)
7. [Congruence of squares](/congruence-of-squares/)
8. [Relation collection](/relation-collection/)
9. [Dixon's random squares algorithm](/dixon-random-squares/)
10. [Quadratic sieve](/quadratic-sieve/)

These give one method of each kind and the plan behind all the fast ones. On a first pass, skip Lehman, Hart, Pollard-Strassen and SQUFOF, which matter for numbers of a few words or for complexity bounds, and read the elliptic curve method and the number field sieves for their ideas before their details.

## Before you start

You need the [gcd](/greatest-common-divisor/), [modular exponentiation](/modular-exponentiation/), [Fermat's little theorem](/fermat-little-theorem/), the [Chinese remainder theorem](/chinese-remainder-theorem/) and [quadratic residues](/quadratic-residue/) from Chapters 10.1 and 10.2, and [continued fractions](/continued-fraction/) for CFRAC and SQUFOF. From Chapter 10.3, the [prime number theorem](/prime-number-theorem/) explains how many candidates a method meets and a [nontrivial square root of 1](/nontrivial-square-root-of-one/) is the simplest congruence of squares. Pollard's rho uses the [birthday paradox](/birthday-paradox/) and [Floyd's cycle detection](/floyd-cycle-detection/). The sieves use [Gaussian elimination](/gaussian-elimination/) over the field with two elements, the [factor base](/factor-base/) of Chapter 10.6 and the [sieve of Eratosthenes](/sieve-of-eratosthenes/) of Chapter 10.5. Pollard-Strassen uses [fast multipoint evaluation](/fast-multipoint-evaluation/), and the elliptic curve method uses the point arithmetic of elliptic curve cryptography.
