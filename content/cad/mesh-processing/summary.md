## What to remember

- A closed [manifold mesh](/manifold-mesh/) has $\chi = V - E + F = 2 - 2g$, and with $b$ border loops $\chi = 2 - 2g - b$. A closed triangle mesh has $3F = 2E$ and $\sum_i (6 - d_i) = 6\chi$.
- [Vertex welding](/vertex-welding/) and [consistent orientation](/consistent-mesh-orientation/) take near linear expected time; welding chains, so a class can be wider than $\varepsilon$. Filling a hole of $n$ border vertices by the [triangulation dynamic program](/polygon-triangulation-dp/) takes $\Theta(n^3)$ time and $\Theta(n^2)$ space over $C_{n-2}$ patches; whether a loop in space has a triangulation that does not cross itself is NP-complete.
- [Laplacian smoothing](/laplacian-smoothing/) multiplies an eigenmode of frequency $k$ by $1 - \lambda k$ and shrinks every closed mesh toward a point. [Taubin smoothing](/taubin-smoothing/) multiplies it by $(1 - \lambda k)(1 - \mu k)$ with $\mu < -\lambda < 0$, has pass band $k_{PB} = 1/\lambda + 1/\mu$, and its largest gain below $k_{PB}$ is $1 + (\lambda + \mu)^2 / (-4\lambda\mu)$. [Implicit fairing](/implicit-fairing/) uses $1/(1 + \Delta t\, k)$, stable for all $\Delta t > 0$.
- The [cotangent Laplacian](/cotangent-laplacian/) has edge weights $\frac12(\cot\alpha + \cot\beta)$. It reproduces linear functions on a flat mesh, and a weight is negative when $\alpha + \beta > \pi$.
- The [angle defect](/discrete-gaussian-curvature/) $K_i = 2\pi - \Theta_i$ sums to $2\pi\chi$ on a closed mesh, exactly ([discrete Gauss-Bonnet](/discrete-gauss-bonnet-theorem/)). With a border, add $\pi - \Theta_i$ at each border vertex.
- Exact geodesics take $O(n^2 \log n)$ time and $O(n^2)$ space by [MMP](/mmp-geodesic-algorithm/), $O(n^2)$ time and $O(n)$ space by Chen and Han, $O(n \log n)$ on convex polytopes. The [heat method](/heat-method/) is approximate: $t = h^2$, two sparse solves, an error that goes to 0 under refinement.
- A [Tutte embedding](/tutte-embedding/) with a strictly convex boundary and positive weights is one to one in exact arithmetic; in doubles tiny triangles can flip. [LSCM](/least-squares-conformal-maps/) needs two pins and may fold. [ABF](/angle-based-flattening/) is locally injective when its angle constraints hold exactly.
- [Triangle-triangle intersection](/triangle-triangle-intersection/) takes $\Theta(1)$ signs of ORIENT3D. A mesh of $m$ triangles can have $\Theta(m^2)$ crossing pairs, and deciding whether it has any needs $\Omega(m \log m)$ in the algebraic decision tree model. [Mesh Booleans](/mesh-boolean-operations/) can have $\Theta(nm)$ output triangles.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Vertex welding (grid) | exact distances | $O(n)$ expected, sparse cells | finds every pair within $\varepsilon$; classes chain |
| Liepa hole filling | real RAM, floats for angles | $\Theta(n^3)$, $\Theta(n^2)$ space | patch closes the hole; shape measured |
| Volumetric repair (Ju) | exact or perturbed crossings | $O(s + k + b g)$ | always closed; resampled at cell size |
| Mesh arrangements | exact rationals | output can be $\Theta(n^2)$ | exact Booleans for closed input |
| Generalized winding number | floating point | $O(F)$ per query | integer for closed meshes in exact arithmetic |
| Laplacian, Taubin | floating point | $\Theta(Kn)$ | gains $1 - \lambda k$, $(1 - \lambda k)(1 - \mu k)$ |
| Implicit fairing | floating point, CG | $\Theta(Ksn)$ | stable for every $\Delta t$ |
| MMP geodesics | real RAM | $O(n^2 \log n)$, $O(n^2)$ space | exact distances |
| Heat method | floating point | $\Theta(sn)$ with CG | approximate; converges under refinement |
| Tutte, LSCM | exact or floats | $O(n^{3/2})$ with nested dissection | Tutte one to one; LSCM may fold |
| Isotropic remeshing | floating point | $O(k n^2 \log n)$ worst | topology kept; quality measured |
| Metro | exact distances | $O(SF)$ worst | lower bound, low by at most the sample spacing |

: The main methods. $n$ counts vertices (border vertices for Liepa), $F$ triangles, $K$ steps, $s$ solver iterations, $S$ samples, $k$ rounds; for Ju, $s$ polygons, $k$ crossings, $b$ odd cells, $g$ cells.

## Choosing a method

For a soup, weld with a tolerance below the smallest feature, orient, and check the manifold conditions. Fill a few small holes with Liepa's method, which keeps every input face. When the model has many defects, use volumetric repair and measure the change with Metro in both directions.

For Booleans on meshes that may touch, overlap or cut themselves, use exact arrangements; tolerance-based Booleans fail on coincident faces. For broken input, label the inside with the generalized winding number.

To remove noise, use Taubin smoothing, or implicit fairing with cotangent weights for large steps; plain Laplacian smoothing shrinks. For distances, use the heat method for speed and MMP when the distance must be exact. To flatten a disk, use Tutte with mean value weights when the map must be one to one, LSCM for a fast conformal chart, and ABF when angles matter most. Remesh first: cotangent weights assume triangles of good shape.
