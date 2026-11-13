1. ◦ A unit sphere has its center at $(0.6, 0, 0)$. A ray starts at $o = (0, 0, 5)$ with $d = (0, 0, -1)$. Use [ray-sphere intersection](/ray-sphere-intersection/) to find both roots $t$, the first hit point and the unit normal there.

2. ◦ Take the box $[1, 3] \times [0, 2] \times [0, 2]$ and the direction $d = (2, 1, 0)$. Run the [slab method](/slab-method/) for the origins $(0, 0.5, 1)$, $(0, 1.5, 1)$ and $(0, 1.6, 1)$. Give the interval $[t_0, t_1]$ or say that the ray misses. Say what the second ray does geometrically, and why the test counts it as a hit.

3. ◦ The triangle has $v_0 = (1, 0, 0)$, $v_1 = (0, 1, 0)$ and $v_2 = (0, 0, 1)$. The ray starts at the origin with $d = (1, 2, 3)$. Run [Möller-Trumbore](/moller-trumbore/) and give $\det$, $u$, $v$ and $t$. Say whether the ray meets the front or the back of the triangle, and what the culling version returns.

4. ◦ Water has the index 1.333. Use [Snell's law](/snells-law/) and the [Fresnel equations](/fresnel-equations/) for unpolarized light. Find $R_0$ at normal incidence. For light from air at $60°$, find the refraction angle, the exact $R$ and Schlick's value. For light inside the water, find the transmitted angle and $R$ at $45°$, and say what happens at $50°$.

5. ◦ A camera has an image of $W = 8$ by $H = 6$ pixels and a vertical field of view $\theta = 60°$. Its axes are $u = (1, 0, 0)$, $v = (0, 1, 0)$ and $w = (0, 0, 1)$. Use [primary ray generation](/primary-ray-generation/) to give the direction through the center of pixel $(5, 1)$. Then add a [thin lens](/thin-lens-camera/) with radius $R = 0.05$, focused at $z_f = 5$. Find the diameter of the blur disk for a point at depth 10.

6. ◦ A 50 mm lens at f/8 is focused at 5 m, with an acceptable circle of confusion of 0.03 mm. Use the formulas of [depth of field](/depth-of-field/) to find the hyperfocal distance and the near and far limits of sharpness. Find the distance from the lens to the film as well.

7. ◦ A 2D grid has unit cells. A ray starts at $(0.5, 0.2)$ with $d = (1, 0.5)$ and stops at $x = 4$. List the cells that [Amanatides-Woo traversal](/amanatides-woo-traversal/) visits, in order, and check the count against $1 + |\Delta i| + |\Delta j|$.

8. ◦ A [Whitted ray tracer](/whitted-ray-tracing/) has the depth limit $D = 3$, so rays at depth 3 spawn no children, and every surface reflects and refracts. The scene has $m = 2$ point lights. Find the largest number of rays per pixel, the number of shadow rays, and the total number of ray queries.

9. ◦ Every surface of a closed furnace emits $L_e$ and has albedo $\rho = 0.8$. Use the Neumann series of the [rendering equation](/rendering-equation/) to find the radiance. Find how many bounces keep the truncation error below 1%. Find what fraction of the true radiance a [path tracer](/path-tracing/) with a depth limit of 5 bounces converges to.

10. ◦ A path tracer shows a standard error of 0.08 in a pixel at 16 samples per pixel. Find the number of samples that brings it to 0.01. Say why this number gives a confidence interval and not a bound on the error.

11. ◦ Classify each estimator as unbiased or biased, and as consistent or not: (a) path tracing with [Russian roulette](/russian-roulette/), (b) path tracing with a fixed depth limit, (c) [photon mapping](/photon-mapping/) with a fixed radius, (d) [progressive photon mapping](/progressive-photon-mapping/), (e) [instant radiosity](/instant-radiosity/) with a fixed clamp, (f) [irradiance caching](/irradiance-caching/) with a fixed error bound $a$ and a fixed number of rays $s$ per record, (g) [ReSTIR](/restir/) with the $1/M$ merge, (h) [Metropolis light transport](/metropolis-light-transport/) from a fixed start path, and (i) [ambient occlusion](/ambient-occlusion/), as an estimate of $A(x)$ and as an estimate of the real light.

12. • Four unit cubes $[c, c+1] \times [0, 1] \times [0, 1]$ sit at $c = 0, 1, 8, 9$. Take $c_t = c_i = 1$. Compute the [surface area heuristic](/surface-area-heuristic/) cost of the three splits along $x$ and of a leaf. Find the ratio $c_t / c_i$ above which a leaf beats the best split.

13. • Two candidate [BRDFs](/brdf/) are $f_1 = c \cos\theta_o$ and $f_2 = c(\cos\theta_i + \cos\theta_o)$. For each one, say whether it obeys [Helmholtz reciprocity](/helmholtz-reciprocity/). Find its [albedo](/albedo/) as a function of the incident angle, and the largest $c$ that conserves energy.

14. • Five points have 2-bit coordinates: $A = (0,0,0)$, $B = (1,0,0)$, $C = (3,3,3)$, $D = (2,3,1)$ and $E = (1,1,0)$. Compute their 6-bit [Morton codes](/morton-encoding/), with the bit of $x$ lowest in each group of three. Sort them, and build the hierarchy of [LBVH construction](/lbvh-construction/) by splitting each range at its highest differing bit.

15. • Estimate $\int_0^1 3x^2\,dx$ with the densities $p_1 = 1$ and $p_2 = 2x$. Find the variance of one sample from each density alone. Use [multiple importance sampling](/multiple-importance-sampling/) with one sample from each density, and find the variance with the balance heuristic and with the power heuristic ($\beta = 2$). Compare both with two samples from $p_2$, and with the plain average of one sample from each. Give the two weights of $p_1$ at $x = 0.25$.

16. • A light of radiance $L$ fills a cone of half-angle $\alpha$ around the normal of a diffuse point. Cosine sampling of the BSDF hits the light with probability $\sin^2\alpha$. Find the relative standard deviation of one BSDF sample, and the number of samples for a 1% relative error, for $\alpha = 1°$ and $\alpha = 5°$. Show that [next event estimation](/next-event-estimation/), sampling the cone uniformly in solid angle, has a relative error of at most $1 - \cos\alpha$ from one sample.

17. • A medium has $\sigma_t = 1$ on $[0, 1)$ and $\sigma_t = 3$ on $[1, 2)$. [Delta tracking](/delta-tracking/) uses the majorant 3 on $[0, 2]$. Find the probability that the first real collision lies in $[0, 1)$, the transmittance of the whole segment, and the expected number of tentative points before the walk stops. Compare with ratio tracking, which never stops early.

18. • A hit point of [progressive photon mapping](/progressive-photon-mapping/) starts with $N = 0$ and $R^2 = 1$, and uses $\alpha = 0.7$. In pass 1 it finds $M = 20$ photons, and in pass 2 it finds $M = 15$. Give $N$ and $R^2$ after each pass, and check that the photon density $N / R^2$ grows.

19. • The irradiance near a point of a [photon map](/photon-map/) is $E(x) = E_0 + g \cdot x + a\lvert x \rvert^2$ in local coordinates. A density estimate averages $E$ over a disk of radius $r$. Find its bias, and say which term causes it.

20. • A ray descends at an angle of $1°$ toward the plane $z = 0$, starting at height 1, and the distance function is $z$. Show that each step of [sphere tracing](/sphere-tracing/) multiplies the height by $1 - \sin 1°$. Find the number of steps until the height falls below $10^{-3}$.

21. • A point lies on a floor, in the corner where two perpendicular walls meet it, and $d_{\max} = \infty$. Find its [ambient occlusion](/ambient-occlusion/) $A(x)$. Find the number of rays that keeps the standard deviation below 0.01, both from the bound $1/(2\sqrt{N})$ and from the exact variance.

22. • Two patches of [radiosity](/radiosity/) see each other with $F_{12} = F_{21} = 0.2$, and both have $\rho = 0.5$. Patch 1 emits $E_1 = 1$ and patch 2 emits nothing. Solve for $B_1$ and $B_2$. Run three Jacobi sweeps from $B = E$, and give the factor by which the largest error falls per sweep.

23. • Take a point light and a pinhole camera. For each of the paths $LDE$, $LSDE$, $LDSE$ and $LSDSE$ in the notation of the [path integral formulation](/path-integral-formulation/), say which of path tracing with NEE, [light tracing](/light-tracing/) and [bidirectional path tracing](/bidirectional-path-tracing/) can produce it with positive probability.

24. • A scene has two lights with contributions $f = (3, 1)$. Resampled importance sampling, as in [ReSTIR](/restir/), draws $M$ candidates uniformly, uses the target $\hat p = f$, and keeps one candidate $y$ with probability proportional to $\hat p / p$. Show that the estimate does not depend on which $y$ is kept. Give its mean and variance.

25. ★ Every surface of a closed furnace emits $L_e$ and has albedo $\rho$. The BSDF is sampled by its cosine, and [Russian roulette](/russian-roulette/) continues with a constant probability $q$. Show that the variance of one path is $L_e^2 \rho^2 (1 - q) / ((1 - \rho)^2 (q - \rho^2))$, finite exactly when $q > \rho^2$. Give its value at $q = \rho = 0.5$. Then show that the variance times the expected number of vertices decreases in $q$.

26. ★ Show that a greedy top-down SAH build is not always optimal. Use four unit cubes $[c, c+1] \times [0, 1] \times [0, 1]$ at $c = 0, 2, 3, 5$, with $c_t = c_i = 1$ and the cost of a leaf $c_i$ times its count. Find the greedy tree and its cost, and a tree of lower cost.

27. ★ The SAH rests on Cauchy's formula: a uniform random line that meets a convex body $K$ meets a convex body $K' \subseteq K$ with probability $S(K')/S(K)$. Use this, together with Crofton's formula for the integral of chord lengths, to show that the mean chord of a uniform random line through a convex body is $4V/S$. Give it for the unit cube and for a ball of radius $r$.

28. ★ A plane holds $n$ long, thin horizontal triangles and $n$ long, thin vertical ones, and each horizontal one crosses each vertical one. Show that every [kd-tree](/kd-tree-traversal/) whose leaves hold at most $c$ references has $\Omega(n^2/c^2)$ leaves, while a [BVH](/bounding-volume-hierarchy/) over the same $2n$ triangles has at most $4n - 1$ nodes.

29. ★ Unit cubes sit at $x = 2^k$ for $k = 0, \ldots, n-1$. A binned SAH [BVH construction](/bvh-construction/) uses $K = 4$ equal bins over the range of centroids. Show that bin 0 holds all but the last two cubes, so every split leaves at least $m - 2$ of the $m$ cubes on its left side. Conclude that a build down to single cubes bins at least $n + (n - 2) + (n - 4) + \cdots \ge n^2/4$ primitives, so it does $\Theta(n^2)$ work.
