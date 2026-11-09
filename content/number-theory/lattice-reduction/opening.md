A lattice is the set of all integer combinations of a few independent vectors in $\mathbb{R}^m$: a regular grid, possibly slanted. The same lattice has many bases, and most of them are bad. The vectors $(43, 19)$ and $(66, 29)$ span the same lattice as $(1, -2)$ and $(3, 1)$, but from the first pair nobody can see that the lattice contains a vector of length $\sqrt 5$, or which lattice point lies nearest to a given point. Lattice reduction turns a bad basis into a good one, made of short vectors that are nearly orthogonal. In two dimensions this is a form of Euclid's algorithm, known since Lagrange and Gauss. In higher dimension the exact problems are hard, and the LLL algorithm of 1982 gives a reduced basis in polynomial time at the cost of an approximation factor exponential in the dimension.

That factor sounds weak, but it is enough for a long list of problems that do not look like lattice problems at all: factoring polynomials with rational coefficients, finding an integer relation among real numbers, approximating several numbers by fractions with one denominator, finding small roots of a polynomial modulo $N$, and breaking knapsack and some RSA systems. The hardness of the exact problems has become useful too. Lattice problems are believed hard even for quantum computers, and the public-key systems built on them rest on the algorithms of this chapter: their key sizes are chosen so that BKZ and sieving fail.

## What the chapter covers

1. **Lattices and bases.** The [lattice](/lattice/), its [bases](/lattice-basis/), the [determinant](/lattice-determinant/), [Gram-Schmidt orthogonalization](/gram-schmidt-orthogonalization/) and the [dual lattice](/dual-lattice/).
2. **Shortest and closest vectors.** The [shortest vector problem](/shortest-vector-problem/), the [closest vector problem](/closest-vector-problem/), the [successive minima](/successive-minima/) and the [covering radius](/covering-radius/).
3. **Bounds from the geometry of numbers.** The [Hermite constant](/hermite-constant/), [Minkowski's first](/minkowski-theorem/) and [second](/minkowski-second-theorem/) theorems, and the [Gaussian heuristic](/gaussian-heuristic/).
4. **Approximate and promise problems.** [Approximate SVP](/approximate-svp/), [GapSVP](/gap-svp/), [unique SVP](/unique-svp/), [bounded distance decoding](/bounded-distance-decoding/) and the [shortest independent vectors problem](/shortest-independent-vectors-problem/).
5. **What a reduced basis is.** [Lattice basis reduction](/lattice-basis-reduction/) as a problem, [Lagrange-Gauss reduction](/lagrange-gauss-reduction/) in dimension 2, [size reduction](/size-reduction/), the [Lovász condition](/lovasz-condition/), [LLL-reduced bases](/lll-reduction/), and the stronger [HKZ](/hkz-reduction/) and [Minkowski](/minkowski-reduced-basis/) reductions.
6. **The LLL algorithm and its uses.** The [LLL algorithm](/lll-algorithm/), its [approximation guarantee](/lll-approximation-guarantee/), the [root Hermite factor](/root-hermite-factor/), [deep LLL](/deep-lll/), [Seysen reduction](/seysen-reduction/), and Babai's [rounding](/babai-rounding/) and [nearest plane](/babai-nearest-plane/) methods for CVP.
7. **Enumeration, block reduction and sieving.** [Lattice enumeration](/lattice-enumeration/) in the versions of [Fincke and Pohst](/fincke-pohst-enumeration/), [Schnorr and Euchner](/schnorr-euchner-enumeration/) and [Kannan](/kannan-enumeration/), the [BKZ algorithm](/bkz-algorithm/), [lattice sieving](/lattice-sieving/) and the [Gauss sieve](/gauss-sieve/).
8. **Applications to numbers and polynomials.** The [integer relation problem](/integer-relation-problem/) and the [PSLQ algorithm](/pslq-algorithm/), [simultaneous Diophantine approximation](/simultaneous-diophantine-approximation/) and [Coppersmith's method](/coppersmith-method/).
9. **How hard lattice problems are.** The [NP-hardness of CVP](/cvp-np-hardness/), the [randomized NP-hardness of SVP](/svp-randomized-np-hardness/) and [Ajtai's worst-case to average-case reduction](/ajtai-worst-case-to-average-case-reduction/).

## A first reading

Read these in order:

1. [Lattice](/lattice/)
2. [Lattice basis](/lattice-basis/)
3. [Lattice determinant](/lattice-determinant/)
4. [Gram-Schmidt orthogonalization](/gram-schmidt-orthogonalization/)
5. [Shortest vector problem](/shortest-vector-problem/)
6. [Closest vector problem](/closest-vector-problem/)
7. [Lagrange-Gauss reduction](/lagrange-gauss-reduction/)
8. [Size reduction](/size-reduction/)
9. [Lovász condition](/lovasz-condition/)
10. [LLL algorithm](/lll-algorithm/)
11. [LLL approximation guarantee](/lll-approximation-guarantee/)
12. [Babai nearest plane algorithm](/babai-nearest-plane/)
13. [Coppersmith's method](/coppersmith-method/)

With these you can reduce a basis by hand in small dimension, say what LLL guarantees and why, and use it for approximate CVP and for small roots. The geometry of numbers, the enumeration and sieving algorithms and the hardness results are for a second reading, when you need exact SVP or the cost of an attack on a lattice-based system.

## Before you start

The chapter is linear algebra over the integers. You need [linear independence](/linear-independence/), [determinants](/determinant/) and [unimodular matrices](/unimodular-matrix/) from Volume 11, and the [Euclidean algorithm](/euclidean-algorithm/) and [continued fractions](/continued-fraction/) from Chapter 10.1; Lagrange-Gauss reduction is Euclid's algorithm on vectors, and continued fractions are the one-dimensional case of Diophantine approximation. Enumeration is a [depth-first search](/depth-first-search/). Minkowski's theorem uses [convex sets](/convex-set/). The hardness results reduce from subset sum and use the classes NP and RP, and Ajtai's theorem is stated for the short integer solution problem, defined in that entry; for this group it is enough to know what an NP-hardness proof is.
