## What to remember

- A **canonical form** maps equal expressions to identical data, so equality becomes a comparison. [Richardson's theorem](/richardson-theorem/) shows that zero-equivalence is undecidable once $\pi$, $\sin$, $\exp$ and $|\cdot|$ are allowed, so each simplifier works within a stated class.
- **Expression swell** is the main practical cost. Over $\mathbb{Z}[x]$ it is controlled by removing contents ([primitive PRS](/primitive-prs/)), by dividing by a factor known in advance ([subresultant PRS](/subresultant-prs/)), or by [modular methods](/modular-methods/): solve modulo primes whose product exceeds twice a bound on the answer, then rebuild it with the Chinese remainder theorem.
- $G \subseteq I$ is a **Gröbner basis** when $\langle \operatorname{LT}(G) \rangle = \langle \operatorname{LT}(I) \rangle$. Then the remainder of [multivariate division](/multivariate-division-algorithm/) by $G$ is unique, and $f \in I$ exactly when it is zero. It is enough that every [S-polynomial](/s-polynomial/) reduces to zero. The [reduced Gröbner basis](/reduced-groebner-basis/) is unique for each ideal and order.
- **The order matters.** Grevlex bases are the cheapest to compute; lex bases give every [elimination ideal](/elimination-ideal/) at once. Compute grevlex, then convert with [FGLM](/fglm-algorithm/) in $O(nD^3)$ field operations. In the worst case any method needs degree $d^{2^{\Omega(n)}}$.
- **Solving.** A system has no common zero over the algebraic closure exactly when its reduced Gröbner basis is $\{1\}$ ([Nullstellensatz](/hilbert-nullstellensatz/)). Over the reals, [cylindrical algebraic decomposition](/cylindrical-algebraic-decomposition/) eliminates quantifiers in doubly exponential time, and no method does better in general.
- **Rational integration** needs no factoring. [Hermite reduction](/hermite-reduction/) finds the rational part with gcds. The logarithmic coefficients are the roots of $\operatorname{res}_x(D, A - zD')$ ([Rothstein-Trager](/rothstein-trager/)). [Liouville's theorem](/liouville-theorem/) fixes the shape of every elementary integral, and the [Risch algorithm](/risch-algorithm/) decides the transcendental case.
- **Summation** follows integration. [Gosper's algorithm](/gosper-algorithm/) decides whether a [hypergeometric term](/hypergeometric-term/) has a hypergeometric antidifference. [Zeilberger's algorithm](/zeilberger-algorithm/) finds a recurrence with a certificate for a definite sum, and [Hyper](/petkovsek-hyper-algorithm/) solves that recurrence.

## The main methods side by side

| Method | Problem | Cost |
|---|---|---|
| [Primitive PRS](/primitive-prs/) | gcd in $\mathbb{Z}[x]$ | $O(m^2)$ ring operations and $O(m^2)$ content gcds |
| [Subresultant PRS](/subresultant-prs/) | gcd, resultant | $O(mn)$ ring operations |
| [Heuristic gcd](/heuristic-gcd/) | gcd in $\mathbb{Z}[x]$ | $O(T d^2 (d + L)^2)$ word operations |
| [Kronecker's method](/kronecker-factorization-method/) | factoring in $\mathbb{Z}[x]$ | $O(d^3 (2k)^{d/2 + 1})$ |
| [Buchberger's algorithm](/buchberger-algorithm/) | Gröbner basis | degree $d^{2^{\Omega(n)}}$ in the worst case |
| [FGLM](/fglm-algorithm/) | change of order | $O(n D^3)$ field operations |
| [CAD](/cylindrical-algebraic-decomposition/) | real quantifier elimination | $(md)^{2^{O(n)}}$ |
| [Hermite reduction](/hermite-reduction/) | rational part of an integral | $O(n^3)$; $O(n^2)$ if $D$ is square-free |
| [Horowitz-Ostrogradsky](/horowitz-ostrogradsky/) | rational part of an integral | $O(d^3)$ |
| [Rothstein-Trager](/rothstein-trager/) | logarithmic part | $O(n^5)$ |
| [Lazard-Rioboo-Trager](/lazard-rioboo-trager/) | logarithmic part, no extensions | $O(n^4)$ |
| [Ben-Or and Tiwari](/ben-or-tiwari-algorithm/) | sparse interpolation | $2T$ values, $O(T^2)$ operations |
| [Zippel's method](/zippel-sparse-interpolation/) | sparse interpolation | at most $(d + 1)(1 + (n - 1)t)$ values |

: Costs as proved in the entries. $m, n, d$ are degrees (for Gröbner bases and CAD, $n$ is the number of variables), $L$ is the coefficient length, $T$ the number of tries or the term bound, $k$ the largest number of divisors of a value, and $D$ the number of solutions with multiplicity.

## Choosing a method

- For a gcd in $\mathbb{Z}[x]$, try the heuristic gcd on small inputs, a modular gcd on large dense ones, and the subresultant PRS when the remainder sequence itself is needed.
- For a Gröbner basis, use F4 or F5 in grevlex. For lex, convert with FGLM, or with the [Gröbner walk](/groebner-walk/) when there are infinitely many solutions.
- To solve a system with finitely many solutions, go from grevlex to a lex basis or a [rational univariate representation](/rational-univariate-representation/), then isolate the roots of one polynomial.
- For inequalities over the reals, use CAD and keep the number of variables small.
- For a rational integral, use Hermite reduction, then Lazard-Rioboo-Trager. For other elementary integrals, try the [Risch-Norman heuristic](/risch-norman-heuristic/) before the Risch algorithm.
- To prove an identity between hypergeometric sums, let Zeilberger's algorithm find the recurrence, then check its certificate by rational function arithmetic.
