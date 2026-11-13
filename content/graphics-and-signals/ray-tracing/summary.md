## What to remember

- A ray-primitive test costs $\Theta(1)$ and is exact in exact arithmetic. In floating point, [Möller-Trumbore](/moller-trumbore/) can let a ray slip through a shared edge. The [watertight test](/watertight-ray-triangle-intersection/) gets every edge sign exact, so at an inner edge it hits at least one triangle.
- A [BVH traversal](/bvh-traversal/) or [kd-tree traversal](/kd-tree-traversal/) costs $O(n)$ per ray in the worst case, and some scenes reach that bound. The near-logarithmic cost on real scenes is measured, not proved. [Amanatides-Woo traversal](/amanatides-woo-traversal/) visits exactly $1 + |\Delta i| + |\Delta j| + |\Delta k|$ cells.
- The [surface area heuristic](/surface-area-heuristic/) gives the expected cost of a tree for uniform random lines, by Cauchy's formula for convex sets. A greedy build is not always optimal, and real rays are not uniform. The binned SAH [build](/bvh-construction/) takes $O(n \log n)$ for balanced trees and $O(n^2)$ in the worst case.
- The [rendering equation](/rendering-equation/) has a [Neumann series](/neumann-series/) that converges when every albedo is below 1. After $k$ bounces the error is at most $\lVert T \rVert^{k+1} \lVert L \rVert$, so at albedo 0.9 a 1% error takes 43 bounces.
- [Path tracing](/path-tracing/), with [Russian roulette](/russian-roulette/), [next event estimation](/next-event-estimation/) and [MIS](/multiple-importance-sampling/), is unbiased when its densities are positive wherever the integrand is not zero. Its error is a variance, and the standard error falls as $\sigma/\sqrt{N}$. That gives a confidence interval, not a bound.
- A fixed depth limit makes the image too dark. Russian roulette removes that bias, but it never lowers variance.
- [Photon mapping](/photon-mapping/) with a fixed radius is biased and not consistent. [Progressive photon mapping](/progressive-photon-mapping/) shrinks the radius, so it is biased but consistent.
- With a point light and a pinhole camera, light-specular-diffuse-specular-eye paths have probability 0 in path tracing, [light tracing](/light-tracing/) and [bidirectional path tracing](/bidirectional-path-tracing/).

| method | unbiased | consistent | error |
|---|---|---|---|
| path tracing with RR, NEE, MIS | yes | yes | variance |
| path tracing with a depth limit | no, too dark | no | bias plus variance |
| [Metropolis light transport](/metropolis-light-transport/) | only with start-up bias removed | yes | correlated variance |
| photon mapping, fixed radius | no | no | bias plus variance |
| progressive photon mapping | no, bias $O(i^{\alpha-1})$ | yes | variance $O(i^{-\alpha})$ |
| [VCM](/vertex-connection-and-merging/) | no, for a fixed radius | if the radius shrinks | bias plus variance |
| [instant radiosity](/instant-radiosity/) | only without the clamp | if the clamp bound $G_{\max}$ grows with $G_{\max}/N \to 0$ | bias plus variance |
| [irradiance caching](/irradiance-caching/) | no | only as $a \to 0$ and $s \to \infty$ | interpolation error |
| [ReSTIR](/restir/) | with the $1/Z$ or balance merge; the $1/M$ merge is too dark | not shown | variance, correlated over pixels and frames |
| [radiosity](/radiosity/) | deterministic | no | $\rho_{\max}^k$ per sweep plus mesh error |
| [ambient occlusion](/ambient-occlusion/) | yes, for $A(x)$ | yes, for $A(x)$ | sd at most $1/(2\sqrt{N})$ |

: Light transport estimators by bias and consistency. Here consistent means the error goes to zero as the work grows. $i$ is the pass, $\alpha$ the fraction of photons kept, $a$ the error bound of a cache record and $s$ its rays.

## Choosing a method

To find the first hit along a ray, build a [BVH](/bounding-volume-hierarchy/) with the binned SAH and walk it closest child first. An [LBVH](/lbvh-construction/) builds faster and traces slower. [Refit](/bvh-refitting/) the tree when objects move a little. [Spatial splits](/spatial-splits/) help when long thin triangles make boxes overlap. Grids suit evenly spread data such as volumes. A shadow ray needs only an [any-hit query](/any-hit-query/).

Use the watertight test when leaks matter, for example in closed meshes and volumes. For implicit surfaces, use [sphere tracing](/sphere-tracing/) when the function is a true distance bound, and fixed-step [ray marching](/ray-marching/) when it is not.

For light, start with path tracing with NEE and MIS. It is unbiased and estimates its own error. Use bidirectional path tracing when the light enters through small openings. For caustics seen in mirrors, use progressive photon mapping or VCM and accept a bias that shrinks. ReSTIR suits many lights at a few samples per pixel, and Metropolis light transport suits scenes where a few paths carry most of the light. [Whitted ray tracing](/whitted-ray-tracing/) handles only mirrors and glass under point lights, and it leaves out diffuse interreflection.
