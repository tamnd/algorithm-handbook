## What to remember

- **The magnitude gives the autocorrelation.** $|\hat x|^2$ is the Fourier transform of the autocorrelation
  of $x$, so two signals with the same autocorrelation cannot be told apart. A global phase, a shift and the
  conjugate reversal $\overline{x(-t)}$ always give the same magnitude; for a complex signal the plain
  reversal does not.
- **One dimension is ambiguous, two are not.** In 1D, flipping a zero $a$ of the z-transform to $1/\bar a$
  keeps the autocorrelation, which gives up to $2^{n-2}$ classes of signals of length $n$; $[1,5,6]$ and
  $[2,7,3]$ are an example. In two or more dimensions the z-transform is irreducible for all images outside
  a set of measure zero, and then the image is unique up to the trivial changes (Bruck and Sodin).
- **Sampling.** $M_k \ge 2n_k - 1$ samples of the magnitude along each axis give the whole autocorrelation;
  that is a theorem. The rule that the ratio $\sigma$ of measured intensities to unknown pixels must exceed
  2 is a count of equations and unknowns, not a proof of uniqueness. A crystal gives $\sigma = 1$.
- **General measurements.** For real signals, $|\langle a_i, x\rangle|$ determines $x$ up to sign exactly
  when the vectors have the complement property, so $m \ge 2n - 1$ are needed; for complex signals the
  property is necessary but not sufficient, and $4n - 4$ generic vectors suffice.
- **Projection methods.** Error reduction is alternating projection: its Fourier error never increases,
  $E_F(g_{k+1}) \le E_F(g_k)$, but it can stagnate far from a solution. HIO, the difference map and RAAR
  are not monotone and have no general convergence proof for phase retrieval. Every
  fixed point of HIO, and of the difference map through its read-out, gives a solution.
- **Crystals.** The [Patterson function](/patterson-function/) is the autocorrelation of the density, with
  $N(N-1)$ non-origin peaks for $N$ atoms. Direct methods rest on phase relations, such as the triplet, whose
  strength falls like $1/\sqrt N$. No polynomial-time algorithm is proved; the methods are heuristics.
- **Holography.** An off-axis hologram gives the object wave exactly when the band fits, which along one axis
  needs $B < n_a/8$. An in-line hologram mixes the wave with its twin, and a weak phase object is seen through
  the transfer function $2\sin(\pi\lambda z|f|^2)$, which has zeros.
- **Guarantees are for random models.** PhaseLift recovers $x$ from about $n \log n$ Gaussian measurements
  for a fixed signal, and spectral initialization followed by Wirtinger flow converges linearly from
  $m \ge c_0\, n \log n$. These results do not cover Fourier magnitudes.

| Method | Object-space constraint | What is proved | Time |
|---|---|---|---|
| [Gerchberg-Saxton](/gerchberg-saxton-algorithm/) | a second magnitude | error never increases | $O(Kn\log n)$ |
| [Error reduction](/error-reduction-algorithm/) | support, positivity | error never increases; can stagnate | $O(KN\log N)$ |
| [Hybrid input-output](/hybrid-input-output/) | support | fixed points give solutions | $O(KN\log N)$ |
| [Difference map](/difference-map/) | any with a projection | fixed points give solutions | $O(KN\log N)$ |
| [RAAR](/raar/) | support | convergence only for convex sets | $O(KN\log N)$ |
| [Shrinkwrap](/shrinkwrap/) | support, updated | nothing; a heuristic | $O(KN\log N + (K/T)N^2)$ |
| [Charge flipping](/charge-flipping/) | sign flip below $\delta$ | no convergence proof | $O(KN\log N)$ |
| [ePIE](/epie/) | overlapping scan | bounds for each step, no global proof | $O(KJm^2\log m)$ |
| [PhaseLift](/phaselift/) | none (convex lift) | exact recovery, Gaussian vectors | $O(K(mn^2 + n^3))$ |
| [Wirtinger flow](/wirtinger-flow/) | none | linear rate, Gaussian vectors | $O(Kmn)$ |

: The iterative methods of the chapter. $N$ pixels, $K$ iterations, $T$ steps between support updates,
$J$ scan positions with $m \times m$ windows, and $m$ measurements of a signal of length $n$ for the last
two rows.

## Choosing a method

- **One far-field pattern with a known or estimated support:** run HIO, the difference map or RAAR with
  [shrinkwrap](/shrinkwrap/), refine with a few steps of [error reduction](/error-reduction-algorithm/), and
  repeat from many random starts. Accept the image only if independent runs agree up to the trivial
  ambiguities, as in [coherent diffraction imaging](/coherent-diffraction-imaging/).
- **If you can scan the illumination:** use [ptychography](/ptychography/) with [ePIE](/epie/); the overlap
  removes the need for a support and fixes most ambiguities.
- **A crystal:** start from the [Patterson function](/patterson-function/) for a few heavy atoms, or use
  [direct methods](/direct-methods-crystallography/) or [charge flipping](/charge-flipping/) at atomic
  resolution.
- **A hologram:** use the off-axis geometry when the camera has the bandwidth; otherwise in-line holograms at
  several distances, or the [transport of intensity equation](/transport-of-intensity-equation/) for a
  smooth phase.
- **Designed random measurements:** [spectral initialization](/spectral-initialization/) and
  [Wirtinger flow](/wirtinger-flow/) are cheap; [PhaseLift](/phaselift/) is convex but works on an
  $n \times n$ matrix.
