## What to remember

- A [data dependence](/data-dependence/) joins two accesses to one location, at least one of them a write: flow (write then read), anti (read then write) or output (write then write). In a nest its [distance vector](/dependence-distance-vector/) is $d = i_{\text{sink}} - i_{\text{source}}$, which is lexicographically nonnegative, and the first nonzero entry gives the [loop that carries it](/loop-carried-dependence/). A loop that carries no dependence is a [DOALL loop](/doall-loop/).
- The [legality theorem](/loop-transformation-legality/): a reordering $T$ keeps the meaning if $Td \succ 0$ for every nonzero distance $d$. The condition is sufficient, not necessary. [Interchange](/loop-interchange/) of a depth-2 nest reverses a dependence exactly when its direction is $(<, >)$.
- [Dependence testing](/dependence-testing/) is integer feasibility. The [GCD test](/gcd-test/) checks whether $\gcd(a_1, \dots, a_n)$ divides $c$ in $\sum a_k x_k = c$ and ignores the bounds. The [Banerjee test](/banerjee-test/) checks whether $c$ lies in the real range of the left side and ignores integrality. Both are conservative. The Omega test is exact, with an exponential worst case.
- [Skewing](/loop-skewing/) $j' = j + f i$ maps $(d_1, d_2)$ to $(d_1, d_2 + f d_1)$. A large enough $f$ makes every entry nonnegative, and such a fully permutable band can be [tiled](/loop-tiling/).
- [Distribution](/loop-distribution/) and the [Allen-Kennedy algorithm](/allen-kennedy-algorithm/) split a loop by the strongly connected components of its dependence graph, in topological order, and turn each statement that is on no cycle at the current level into a vector statement. [Fusion](/loop-fusion/) is illegal when it would turn a dependence backward; shifting or reversal can sometimes repair it.
- A [unimodular transformation](/unimodular-transformations/) $T$ with $\det T = \pm 1$ maps the integer points of the iteration space one to one, and the new bounds come from Fourier-Motzkin elimination. The [Lamport hyperplane method](/lamport-hyperplane-method/) picks $\pi$ with $\pi \cdot d \ge 1$ for all $d$. Its wavefronts $\pi \cdot x = t$ then run in parallel.
- [Array dataflow analysis](/feautrier-array-dataflow/) gives the exact last writer of every read as a quast, but only for static control parts with affine bounds and subscripts. [Feautrier's algorithm](/feautrier-scheduling/) and [Pluto](/pluto-algorithm/) solve the [affine scheduling problem](/affine-scheduling-problem/) with Farkas' lemma and linear or integer linear programming. Every schedule they return is legal, and the choice among legal schedules comes from their cost models.
- [Vectorization](/vectorization/) of a loop with a carried dependence from $S_p$ to $S_q$ at distance $d$, with $p \ge q$ in the body, needs vector length at most $d$. Speedups from it, [SLP packing](/slp-vectorization/) and tiling are measurements, not guarantees.

| Method | Problem | Time | Guarantee |
|---|---|---|---|
| GCD test | one subscript equation | $O(mk \log C)$ | conservative; ignores bounds |
| Banerjee test | one subscript, with bounds | $O(mk)$, times $3^k$ to refine directions | conservative; ignores integrality |
| Subscript-wise tests | all subscripts | $O(m^2 k + m \log C + 3^k mk)$ | exact on ZIV and SIV; conservative on MIV |
| Allen-Kennedy | vector code | $O(n(r + e))$ | optimal for level information |
| Lamport hyperplane | uniform distances | $O(Dk + Nk)$ | legal wavefront schedule |
| Wolf-Lam | locality | $O(4^k k!\, kD + 2^k k^3 A^2)$ | legal; reuse by cost model |
| SLP vectorization | one basic block | $O(n^3)$ | legal packs; heuristic choice |
| Array dataflow | exact sources | $O(sd(P + L))$ | exact on static control parts |
| Feautrier scheduling | affine schedule | $O(eL)$ | legal; greedy per dimension |
| Pluto | tiling hyperplanes | $O((sd + e)I)$ | legal; cost model |
| Polyhedral scanning | code generation | $O(smP^{n+1}L)$ | visits each point once, in order |

: Main methods. $k$ is the nest depth, $m$ the subscripts, $C$ the largest coefficient, $r$ and $e$ the statements and dependence edges, $D$ the distance vectors, $N$ the iterations, $A$ the references, $s$ the statements and $d$ the depth; $P$, $L$ and $I$ are the per-call costs or sizes defined in each entry.

## Choosing a method

Test dependences cheaply first: the subscript-wise tests on each subscript, GCD and Banerjee on the coupled ones, and the Omega test only when a precise answer pays.

For vector code, run Allen-Kennedy and strip mine each vector statement to the hardware length; use SLP packing on straight-line code. A loop that stays on a dependence cycle may still run with DOACROSS synchronization when the delay is short, or lose the cycle by [array privatization](/array-privatization/) when it comes from a scratch array.

For cache reuse in a perfect nest, choose interchange, skewing and tiling by hand or with Wolf-Lam. For imperfect nests or fusion across statements, use the polyhedral model with Pluto and generate code by scanning. Measure the result, since the cost models are approximations.
