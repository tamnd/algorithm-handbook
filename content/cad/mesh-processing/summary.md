## What to remember

- A closed [manifold mesh](/manifold-mesh/) has $\chi = V - E + F = 2 - 2g$, minus $b$ for $b$ border loops; a closed triangle mesh has $3F = 2E$ and $\sum_i (6 - d_i) = 6\chi$. A [progressive mesh](/progressive-mesh/) vertex split adds one vertex, two faces and three edges, and [Edgebreaker](/edgebreaker/) codes a genus 0 mesh of $t$ triangles in exactly $2t - 1$ bits.
- [Vertex welding](/vertex-welding/) and [consistent orientation](/consistent-mesh-orientation/) take near linear expected time, and welding chains. Filling a hole of $n$ border vertices by the [triangulation dynamic program](/polygon-triangulation-dp/) takes $\Theta(n^3)$ time; a patch that must not cross itself is NP-complete to find. [Triangle-triangle tests](/triangle-triangle-intersection/) are $\Theta(1)$ signs of ORIENT3D, and [mesh Booleans](/mesh-boolean-operations/) can have $\Theta(nm)$ output triangles.
- [Laplacian smoothing](/laplacian-smoothing/) multiplies a mode of frequency $k$ by $1 - \lambda k$ and shrinks. [Taubin smoothing](/taubin-smoothing/) uses $(1 - \lambda k)(1 - \mu k)$ with $\mu < -\lambda < 0$ and pass band $k_{PB} = 1/\lambda + 1/\mu$; [implicit fairing](/implicit-fairing/) uses $1/(1 + \Delta t\, k)$, stable for all $\Delta t > 0$. [Manifold harmonics](/manifold-harmonics/) are the modes themselves, $C\phi = \lambda M\phi$.
- The [cotangent Laplacian](/cotangent-laplacian/) weight $\frac12(\cot\alpha + \cot\beta)$ is negative when $\alpha + \beta > \pi$. Applied to the positions it is the area gradient, so divided by the mixed area it is the [mean curvature normal](/discrete-mean-curvature/), an estimate of $2Hn$. [Curvature tensors](/curvature-tensor-estimation/) are exact for balanced directions and exact samples, and can keep a bias under refinement.
- The [angle defect](/discrete-gaussian-curvature/) $2\pi - \Theta_i$ sums to exactly $2\pi\chi$ ([discrete Gauss-Bonnet](/discrete-gauss-bonnet-theorem/)).
- [Laplacian surface editing](/laplacian-surface-editing/) is one sparse solve whose details turn correctly only for small angles. [ARAP deformation](/as-rigid-as-possible-deformation/) alternates rotations and a fixed solve; the energy never rises, but the minimum is local.
- Exact geodesics take $O(n^2 \log n)$ time and $O(n^2)$ space by [MMP](/mmp-geodesic-algorithm/); the [heat method](/heat-method/) costs two sparse solves and converges only under refinement.
- A closed surface is opened by a [cut graph](/cut-graph/) whose cycle rank is $2g$; the shortest one is NP-hard. [Tutte](/tutte-embedding/) with a convex boundary is one to one in exact arithmetic; [LSCM](/least-squares-conformal-maps/) and [ARAP parameterization](/arap-parameterization/) may fold. [Discrete conformal equivalence](/discrete-conformal-equivalence/) is convex, unique when it exists, and can fail on a fixed triangulation; [BFF](/boundary-first-flattening/) gets the boundary angles exactly with linear solves but is only approximately conformal.
- [Cross field](/cross-field/) indices are multiples of $\frac14$ that sum to $\chi$. The [globally optimal field](/globally-optimal-direction-fields/) is optimal only for the relaxed problem.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Edgebreaker | genus 0, exact counts | $O(t)$ expected encode | exactly $2t - 1$ bits |
| Liepa hole filling | floats for angles | $\Theta(n^3)$ | closes the hole; shape measured |
| Mesh arrangements | exact rationals | output $\Theta(n^2)$ | exact Booleans for closed input |
| ARAP (deform, flatten) | floating point | one factorization, a solve per round | energy decreases; local minimum |
| Discrete conformal | Newton, line search | per step a sparse solve | unique if it exists |
| Optimal direction field | inverse iteration | one factorization | optimal for the relaxation |
| Isotropic remeshing | floating point | $O(k n^2 \log n)$ worst | topology kept; quality measured |
| VSA | real RAM | $O(k s n \log n)$ | energy decreases; local minimum |
| Metro | exact distances | $O(SF)$ worst | lower bound, low by the sample spacing |

: The main methods. $n$ counts vertices (border vertices for Liepa, faces for VSA), $t$ and $F$ triangles, $s$ solver iterations or rounds, $S$ samples, $k$ rounds or proxies.

## Choosing a method

For a soup, weld below the smallest feature, orient, and check manifoldness. Fill a few holes with Liepa's method; with many defects, use volumetric repair and compare with Metro both ways. For Booleans on meshes that touch or overlap, use exact arrangements; label the inside of broken input by the generalized winding number.

To remove noise, use Taubin smoothing, or implicit fairing with cotangent weights for large steps; to filter by frequency, use manifold harmonics. To edit with handles, use Laplacian editing for small changes and ARAP for large bends. For distances, use the heat method for speed and MMP for exact values.

Cut to a disk before flattening. Use Tutte with mean value weights when the map must be one to one, LSCM for a fast conformal chart, BFF when the outline is given, discrete conformal equivalence for exact target angles, and ARAP when lengths matter; check for flips with exact orientation tests. For quads, design a smooth cross field, then quadrangulate. Remesh first: cotangent weights assume triangles of good shape. Segment by the SDF for parts of different thickness and by VSA for flat patches.
