Modular exponentiation is fast: $g^x \bmod p$ for a 2048-bit $p$ takes a few thousand multiplications. Going back is a different matter. Given $g$ and $h = g^x$, finding $x$ is the discrete logarithm problem, and for well chosen groups no method is known that runs in time polynomial in the size of the elements. Diffie-Hellman key exchange, ElGamal encryption, DSA and the elliptic curve schemes all rest on this gap, and the algorithms of this chapter are what fixes their key sizes.

The methods fall into two families. Generic methods use only the group operations, so they work in any group, and they need about $\sqrt n$ operations for a group of order $n$; a theorem of Shoup shows that no generic method can do better. Methods of the second family use the representation of the elements. In the multiplicative group of a finite field an element is an integer or a polynomial, it can be factored, and index calculus turns factorizations into linear equations for the logarithms. These methods are subexponential, much like the factoring algorithms of Chapter 10.4, and they explain why a finite field must be far larger than an elliptic curve group for the same security.

## What the chapter covers

1. **The problem and its settings.** The [discrete logarithm problem](/discrete-logarithm-problem/), [discrete roots](/discrete-root/), and the problem in [finite fields](/finite-field-discrete-logarithm-problem/), on [elliptic curves](/elliptic-curve-discrete-logarithm-problem/) and [in a known interval](/interval-discrete-logarithm-problem/).
2. **Square root algorithms.** [Baby-step giant-step](/baby-step-giant-step/), the [Pohlig-Hellman algorithm](/pohlig-hellman/), [Pollard's rho method](/pollard-rho-discrete-logarithm/), [distinguished points](/distinguished-points/), [parallel collision search](/parallel-collision-search/) and [Pollard's kangaroo method](/pollard-kangaroo/).
3. **Lower bounds for generic algorithms.** The [generic group model](/generic-group-model/) and [Shoup's lower bound](/shoup-generic-lower-bound/) of order $\sqrt q$.
4. **Index calculus.** The [factor base](/factor-base/), [index calculus](/index-calculus/) in prime fields, the [number field sieve](/number-field-sieve-discrete-logarithm/), [Coppersmith's algorithm](/coppersmith-discrete-logarithm/) and the [function field sieve](/function-field-sieve/) in small characteristic, and the [quasi-polynomial algorithm](/quasi-polynomial-discrete-logarithm/).
5. **Attacks on special elliptic curves.** The [MOV reduction](/menezes-okamoto-vanstone-reduction/), [summation polynomials](/semaev-summation-polynomial-index-calculus/) and [Weil descent](/weil-descent-attack/).

## A first reading

Read these in order:

1. [Discrete logarithm problem](/discrete-logarithm-problem/)
2. [Baby-step giant-step](/baby-step-giant-step/)
3. [Pohlig-Hellman algorithm](/pohlig-hellman/)
4. [Pollard's rho algorithm for discrete logarithms](/pollard-rho-discrete-logarithm/)
5. [Distinguished points](/distinguished-points/)
6. [Pollard's kangaroo algorithm](/pollard-kangaroo/)
7. [Generic group model](/generic-group-model/)
8. [Factor base](/factor-base/)
9. [Index calculus](/index-calculus/)
10. [Discrete logarithm in finite fields](/finite-field-discrete-logarithm-problem/)
11. [Elliptic curve discrete logarithm problem](/elliptic-curve-discrete-logarithm-problem/)

After these you can solve discrete logarithms in any group of moderate size, and you can say why the groups used in practice have prime order of at least 256 bits on a curve and 2048 bits in a prime field. The sieves, the quasi-polynomial algorithm and the attacks on special curves are research methods; read them when you need to judge a particular group.

## Before you start

The chapter uses [cyclic groups](/cyclic-group/), [Lagrange's theorem](/lagranges-theorem-group-theory/), [multiplicative order](/multiplicative-order/), [primitive roots](/primitive-root/), [modular exponentiation](/modular-exponentiation/), [linear congruences](/linear-congruence/) and the [Chinese remainder theorem](/chinese-remainder-theorem/) from Chapter 10.2. The square root methods need [hash tables](/hash-table/), the [birthday paradox](/birthday-paradox/) and [Floyd's cycle detection](/floyd-cycle-detection/); [Pollard's rho method for factoring](/pollard-rho/) in Chapter 10.4 is the same idea. Index calculus builds on [smooth numbers](/smooth-number/) and on the relation collection of the [quadratic sieve](/quadratic-sieve/); the methods for extension fields use [irreducible polynomials](/irreducible-polynomial/) and polynomial factorization from Volume 11. The elliptic curve entries assume the group law on a curve and its basic facts, such as Hasse's bound on the number of points.
