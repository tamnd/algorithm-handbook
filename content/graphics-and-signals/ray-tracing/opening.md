A ray tracer makes an image by following lines of sight. For each pixel it sends a ray from the camera into the scene, finds the first surface the ray hits, and asks how much light leaves that point towards the camera. Shadows, mirrors and glass come from tracing more rays from the hit point. Light that bounces between surfaces is natural in a ray tracer and hard for the rasterizer of Chapter 28.1. Most film rendering now traces rays, and graphics processors since 2018 have hardware for ray queries.

Two problems make up the subject. The first is to answer billions of ray queries against millions of triangles. A bounding volume hierarchy or a kd-tree, built with the surface area heuristic, brings the cost of one ray from linear in the number of triangles to close to logarithmic on typical scenes. The second is an integral. Kajiya's rendering equation of 1986 writes the light leaving a point as an integral over incoming directions of light that is itself unknown, and path tracing estimates it by Monte Carlo with random paths. The noise falls as $1/\sqrt{N}$ in the number $N$ of paths per pixel, so much of the field is about variance reduction.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Rays and cameras.** Primary rays, pinhole and thin-lens cameras, ray casting and Whitted's recursive ray tracing.
2. **Intersection tests.** Rays against planes, spheres, boxes by the slab method and triangles by the Möller-Trumbore, Plücker and watertight tests; closest-hit and any-hit queries; ray marching and sphere tracing of signed distance functions.
3. **Acceleration structures.** Bounding volume hierarchies built by the surface area heuristic or by Morton codes, refitting, kd-tree and grid traversal, instancing, and ray packets.
4. **Materials.** The BRDF, BSDF and BSSRDF, Lambertian and microfacet models, Fresnel's equations and Snell's law.
5. **Light transport.** The rendering equation and the path integral, path tracing with next-event estimation and multiple importance sampling, bidirectional and Metropolis methods, photon mapping, radiosity, ReSTIR, and participating media.

## What to read meanwhile

Volume 3 has the spatial structures: the [kd-tree](/kd-tree/), the [BSP tree](/bsp-tree/), the [octree](/octree/), the [uniform grid](/uniform-grid/) and the [R-tree](/r-tree/), whose boxes are the [minimum bounding rectangles](/minimum-bounding-rectangle/) that graphics calls axis-aligned bounding boxes. Linear BVH construction sorts primitives by [Morton encoding](/morton-encoding/). The ray-sphere test solves the quadratic of [circle-line intersection](/circle-line-intersection/).

For the integral, read [Monte Carlo integration](/monte-carlo-integration/), [importance sampling](/importance-sampling/), [stratified sampling](/stratified-sampling/) and [quasi-Monte Carlo integration](/quasi-monte-carlo-integration/) with the [Halton](/halton-sequence/) and [Sobol](/sobol-sequence/) sequences. Metropolis light transport is [Metropolis-Hastings](/metropolis-hastings/) over paths, and ReSTIR builds on [weighted reservoir sampling](/weighted-reservoir-sampling/). Chapter 28.3 treats [hidden surface removal](/hidden-surface-removal/) and [shadow mapping](/shadow-mapping/), the rasterizer's answers to the same questions.
