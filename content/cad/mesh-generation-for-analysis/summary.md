## What to remember

- In the plane the [radius-edge ratio](/radius-edge-ratio/) is $\rho = R/\ell_{\min} = 1/(2\sin\theta_{\min})$, so a bound on $\rho$ is a bound on the smallest angle. In space it is not: a [sliver](/sliver-tetrahedron/) has $\rho$ near $\sqrt2/2$ and dihedral angles near $0°$ and $180°$.
- The [maximum angle condition](/maximum-angle-condition/) of Babuška and Aziz gives $|u - \Pi u|_1 \le C(\gamma)\, h\, |u|_2$ when every angle is at most $\gamma < 180°$. Small angles alone do not spoil the gradient; angles near $180°$ do.
- [Tetrahedral Delaunay refinement](/tetrahedral-delaunay-refinement/) stops with $\rho \le B$ for every $B \ge 2$ when no two input segments or facets meet at less than $90°$. For $B > 2$ every edge near $v$ is at least $\mathrm{lfs}(v)/(D_S + 1)$ long, with $D_S = (3 + \sqrt2)B/(B - 2)$.
- [Sliver exudation](/sliver-exudation/) proves a dihedral angle bound with a tiny constant; about $5°$ is measured. [Isosurface stuffing](/isosurface-stuffing/) proves dihedral angles in $[10.78°, 164.74°]$, but rounds sharp features off. The [quadtree](/quadtree-mesh-generation/) method proves a smallest angle of $\arcsin(1/4) \approx 14.48°$ in the plane.
- A [sizing function](/mesh-sizing-function/) must be Lipschitz, and the cheapest one is the envelope $h(x) = \inf_y (h_0(y) + L|x - y|)$. The element count is about $\int dA/h^2$ in the plane, so a point refined to size $h_0$ adds only $O(\log(1/h_0))$ elements.
- An [anisotropic](/anisotropic-mesh-adaptation/) mesh is a unit mesh in the metric $M = |H|/(8\varepsilon)$. For a quadratic with Hessian eigenvalues $\lambda_{\min} \le \lambda_{\max}$ it needs $\sqrt{\lambda_{\min}/\lambda_{\max}}$ times the triangles of the isotropic mesh with the same error.
- Counting faces gives $4Q = 2E_{\mathrm{int}} + E_{\mathrm{bnd}}$ for quads and $6H = 2I + B$ for hexes, so the boundary of an all-quad or all-hex mesh has an even count. For a ball the [existence theorem](/hexahedral-mesh-existence-theorem/) says that even is enough, with $O(n)$ hexes by Eppstein's construction, but the hexes come with no quality bound.
- [Optimization-based smoothing](/optimization-based-mesh-smoothing/) and [topological improvement](/topological-tetrahedral-mesh-improvement/) never lower the worst quality they optimize. They give no bound.

| Method | Model | Time | Guarantee |
|---|---|---|---|
| Quadtree (Bern, Eppstein, Gilbert) | point set in the plane | $O(n \log n + k)$ | angles $\ge 14.48°$; size within a constant of optimal |
| Advancing front | boundary mesh, floating point | $O(n^3)$ worst | valid and terminates; quality measured |
| Tetrahedral Delaunay refinement | PLC, no angle below $90°$ | $O(n^2)$ worst | $\rho \le B$ for $B \ge 2$; slivers survive |
| Sliver exudation | Delaunay mesh with bounded $\rho$ | $O(n)$ after the triangulation | tiny proved dihedral bound; about $5°$ measured |
| Isosurface stuffing | signed distance on a BCC lattice | $O(N)$ lattice points | dihedral angles in $[10.78°, 164.74°]$ |
| Delaunay surface meshing | smooth closed surface, 1-Lipschitz $\sigma$ | $O(n^3)$ worst | homeomorphic if $\sigma \le 0.09\,\mathrm{lfs}$; points $\le 27.2 \iint \sigma^{-2}$ |
| DistMesh | implicit domain, forces | $O(k n \log n)$, $k$ unbounded | none; quality measured |
| Blossom-Quad | triangle mesh, matching | $O(n^3)$ | all quads if a perfect matching exists |
| Hexahedral sweeping | one-to-one sweepable volume | $O(Kn)$ | valid for affine layers of convex quads |
| Optimization-based smoothing | one free vertex, max-min quality | $O(s d^3)$ per vertex | worst element never worse, no inversion |

: The main methods. $n$ counts input or output vertices, $k$ output triangles for the quadtree and iterations for DistMesh, $N$ lattice points, $K$ sweep layers, $d$ elements around a vertex and $s$ steps.

## Choosing a method

For a planar domain with triangles, use Delaunay refinement from Volume 13, which has the proved angle bound. For a region given by a distance function, such as a medical scan, use isosurface stuffing, which loses sharp edges.

For a CAD solid with tetrahedra, mesh the surface first, in the [parameter plane](/parametric-surface-meshing/) of each patch or by Delaunay surface meshing, recover the boundary in the [constrained Delaunay tetrahedralization](/constrained-delaunay-tetrahedralization/), refine with a radius-edge bound, then remove slivers by exudation or by smoothing and flips. If two input facets meet at less than $90°$, use [protecting balls](/protecting-balls/).

For flow near a wall, build [boundary layer prisms](/boundary-layer-mesh-generation/) first and fill the rest with tetrahedra. For a method of order above two, curve the boundary elements and check $\det J > 0$ with the Bernstein coefficients of a [high-order mesh](/high-order-mesh-generation/).

For quads, [Blossom-Quad](/blossom-quad/) needs only a triangle mesh and a matching code, and [paving](/paving/) gives rows of quads along the boundary. For hexes, [sweep](/hexahedral-sweeping/) what is sweepable, decompose the rest by hand or by the [medial axis](/medial-axis-decomposition-meshing/), and try [polycube](/polycube-hex-meshing/) or [frame-field](/frame-field-hex-meshing/) methods on organic shapes, checking the scaled Jacobian. If any element is inverted, run [untangling](/mesh-untangling/) before smoothing.
