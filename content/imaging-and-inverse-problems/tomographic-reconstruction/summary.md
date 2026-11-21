## What to remember

- **The data are line integrals.** After the logarithm of the [Beer-Lambert law](/beer-lambert-law/), each reading is $\mathcal{R}f(\theta, s)$, the integral of the attenuation along one line. With $N$ counts the variance of the log reading is about $1/N$, so the noise differs from ray to ray.
- **The slice theorem gives the inversion.** The 1D Fourier transform of a projection is the 2D transform of the image on a line through the origin. [Filtered back-projection](/filtered-back-projection/) filters each projection with $|\sigma|$ and back-projects, in $O(a d \log d + a n^2)$ time. The rule $a \approx \pi d/2$ keeps the polar samples as dense at the rim as along the rays.
- **Mildly ill-posed.** The ramp makes Radon inversion ill-posed of degree $1/2$. Windows such as Shepp-Logan trade resolution for noise: on white noise of variance $v$ the Ram-Lak kernel gives variance $v/(12\tau^2)$.
- **Cone beams need the Tuy condition.** An exact method exists only if every plane through the object meets the source orbit. A circle fails off the mid-plane, so [FDK](/feldkamp-davis-kress/) is exact only in the mid-plane and for objects that do not vary along the axis. A helix passes, and [Katsevich's algorithm](/katsevich-algorithm/) is exact for it.
- **SIRT is weighted Landweber.** For $0 < \lambda < 2$ it converges to a weighted least squares solution with the weights $1/r_i$, and its filter factors $1 - (1 - \lambda\sigma^2)^k$ show why small singular values take many steps. The iteration count is the regularization.
- **MLEM never lowers the likelihood.** The update $x_j \leftarrow x_j g_j / s_j$ keeps $x$ positive, keeps the total count when there is no background, and converges to a maximizer of the Poisson likelihood. [OSEM](/osem/) is much faster but not monotone, and on inconsistent data it reaches a limit cycle.
- **Penalties change what is proved.** One-step-late has the right fixed points but no monotonicity, and its denominator can reach zero. [SPS](/separable-paraboloidal-surrogates/) is monotone for every penalty weight.
- **Missing data are not alike.** A missing range of angles makes the problem severely ill-posed, with data factors like $e^{-\pi K^2 \sin^2\delta}$. Interior data have an infinite-dimensional null space unless part of the image is known. Sparse views leave a large null space that a prior must fill, and [ASD-POCS](/asd-pocs/) is a heuristic with no convergence proof.

## The methods

| method | data | what is proved |
|---|---|---|
| filtered back-projection | parallel, full angles | exact in the limit of fine sampling; $O(ad \log d + an^2)$ |
| fan-beam FBP | fan, full scan or short scan of $\pi + 2\delta$ | full scan exact in the limit; Parker weights make the two copies of each line add to 1 |
| FDK | cone, circular orbit | exact in the mid-plane and for $z$-invariant objects only |
| Katsevich | cone, helix | exact; Tuy condition holds |
| SIRT, SART | any geometry | convergence to weighted least squares for $0 < \lambda < 2$ (SART: consistent data, common column sums) |
| MLEM | Poisson counts | monotone likelihood; convergence without background |
| OSEM | Poisson counts | convergence only for exact data and balanced subsets |
| SPS | penalized Poisson | monotone for every penalty weight |
| ASD-POCS | sparse view | none; results are measured |

: What the entries prove for each method. "Exact" means exact for continuous data.

## Choosing a method

With complete parallel or fan data and normal dose, filtered back-projection is fast and hard to beat; choose
the window by the noise. On a circular cone-beam scanner FDK is the practical choice when the cone angle is
small, and its errors grow off the mid-plane as the Tuy condition predicts; on a helix an exact method such as
Katsevich removes them. When the counts are low, the geometry is irregular, or a prior is needed, use an
iterative method with a good projector: SIRT or SART for least squares, MLEM or OSEM for emission data, SPS when
a penalty must be monotone. For few views, a total variation prior helps on piecewise constant objects, but
check the result against data with known truth, because no theorem covers the CT case. With a missing angle
range, expect the edges tangent to the missing directions to be lost whatever the method.
