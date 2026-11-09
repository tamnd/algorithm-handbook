## What to remember

- A [lattice](/lattice/) $L = \{x B : x \in \mathbb{Z}^n\}$ has many bases, related by unimodular matrices. The [determinant](/lattice-determinant/) $\det(L) = \prod_i \|b_i^*\|$ is the same for all of them, so a basis with short vectors must have nearly orthogonal ones.
- Gram-Schmidt lengths $\|b_i^*\|$ and coefficients $\mu_{ij}$ are the language of reduction. [Size reduction](/size-reduction/) makes $|\mu_{ij}| \le 1/2$; the [Lovász condition](/lovasz-condition/) $\|b_k^*\|^2 \ge (\delta - \mu_{k,k-1}^2) \|b_{k-1}^*\|^2$ forbids a large drop between neighbors. Together they define an [LLL-reduced basis](/lll-reduction/).
- In dimension 2, [Lagrange-Gauss reduction](/lagrange-gauss-reduction/) is Euclid's algorithm on vectors and returns $\lambda_1$ and $\lambda_2$ exactly.
- The [LLL algorithm](/lll-algorithm/) alternates size reduction and swaps, runs in polynomial time, and returns $\|b_1\| \le 2^{(n-1)/2} \lambda_1$ and $\|b_1\| \le 2^{(n-1)/4} \det(L)^{1/n}$ for $\delta = 3/4$. On random lattices it does far better: the [root Hermite factor](/root-hermite-factor/) is about $1.0219$ instead of $2^{1/4}$.
- [Minkowski's theorem](/minkowski-theorem/) gives $\lambda_1 \le \sqrt n \det(L)^{1/n}$ for every lattice; the [Gaussian heuristic](/gaussian-heuristic/) predicts $\lambda_1 \approx \sqrt{n / (2\pi e)} \det(L)^{1/n}$ for a random one. Reduction algorithms are judged against these.
- With a reduced basis, [Babai's nearest plane method](/babai-nearest-plane/) and [rounding](/babai-rounding/) solve CVP within an exponential factor; with a bad basis the same rounding is useless. This difference is the trapdoor of lattice encryption.
- Exact SVP and CVP cost exponential time: [enumeration](/lattice-enumeration/) uses little memory and $n^{O(n)}$ time, [sieving](/lattice-sieving/) uses $2^{O(n)}$ time and memory. [BKZ](/bkz-algorithm/) runs exact SVP on blocks of size $\beta$ and interpolates between LLL and HKZ reduction.
- Exact CVP is NP-hard and exact SVP is NP-hard under randomized reductions, but the factors that LLL and BKZ reach are far outside the known hardness results. [Ajtai's theorem](/ajtai-worst-case-to-average-case-reduction/) ties random instances to the worst case.

## The methods side by side

| Method | Output | Cost |
|---|---|---|
| [Lagrange-Gauss](/lagrange-gauss-reduction/) | exact $\lambda_1, \lambda_2$, rank 2 | $O(\log X)$ steps |
| [LLL](/lll-algorithm/) | $\|b_1\| \le 2^{(n-1)/2} \lambda_1$ | $O(n^5 m \log^3 X)$ bit operations |
| [Deep LLL](/deep-lll/) | shorter than LLL in practice | no polynomial bound known |
| [BKZ](/bkz-algorithm/), block $\beta$ | root Hermite factor $1.0128$ for $\beta = 20$, observed | SVP calls in rank $\beta$, number not bounded |
| [Babai nearest plane](/babai-nearest-plane/) | CVP within $2^{n/2}$ on an LLL basis | $O(n^2 m)$ after Gram-Schmidt |
| [Fincke-Pohst](/fincke-pohst-enumeration/), [Schnorr-Euchner](/schnorr-euchner-enumeration/) | exact SVP or CVP | $2^{O(n^2)}$ on an LLL basis, polynomial memory |
| [Kannan](/kannan-enumeration/) | exact SVP | $n^{n/(2e) + o(n)}$, polynomial memory |
| [Gauss sieve](/gauss-sieve/) | exact SVP, heuristic | $2^{0.415 n}$ time, $2^{0.208 n}$ memory |
| [PSLQ](/pslq-algorithm/) | integer relation | $O(n^2 (n + \log M))$ iterations |

: Lattice algorithms. $n$ is the rank, $m$ the dimension of the vectors, $X$ a bound on the input entries and $M$ the length of the shortest integer relation. The cost of the sieve and the quality of BKZ are heuristic.

## Choosing a method

In dimension 2, use Lagrange-Gauss: it is exact and as fast as Euclid's algorithm. For an application that needs a short vector or a nearly orthogonal basis but not the shortest one, such as Coppersmith's method, integer relations of moderate size or knapsack attacks, run LLL with $\delta$ near $0.99$; the result is usually much better than the worst-case bound. If LLL is not enough, run BKZ with growing block size; a block size of 20 is cheap, and each step up costs more.

For exact SVP or CVP in small rank, enumeration on a BKZ-reduced basis is simple and needs little memory. In high rank, sieving is faster when the memory is there. For CVP with a good basis, Babai's nearest plane method is the standard decoder; with only a bad basis, reduce it first. To estimate whether an attack on a lattice-based system succeeds, compare the root Hermite factor that BKZ reaches at a given block size with what the attack needs, using the Gaussian heuristic for the lattice.
