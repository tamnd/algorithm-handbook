## What to remember

- The microfacet specular term is $D F G / (4 \cos\theta_l \cos\theta_v)$. GGX gives $D = \alpha^2 / \big(\pi ((n \cdot h)^2 (\alpha^2 - 1) + 1)^2\big)$, normalized for every $\alpha$, with a long tail. The Smith function gives $G_1 = 2 / \big(1 + \sqrt{1 + \alpha^2 \tan^2\theta}\big)$, and Schlick gives $F \approx F_0 + (1 - F_0)(1 - v \cdot h)^5$, within 0.036 of the exact value for glass.
- Physically based shading asks for reciprocity and an albedo of at most 1. The Disney model breaks the second rule: its diffuse albedo reaches 1.40.
- Nine spherical harmonic coefficients give the irradiance $E(n) = \tilde n^T M \tilde n$, with an error of at most $3/32$ of the total light, a proved bound reached by a point light. The split sum turns glossy image-based lighting into a prefiltered lookup times $F_0 A + B$, exact for a constant environment.
- Cascades split the view depth at $C_i = \lambda n (f/n)^{i/m} + (1 - \lambda)(n + (f - n) i / m)$, so the shadow texel grows with the pixel. Variance shadow maps use the Cantelli bound $p \le v / (v + (t - m_1)^2)$ on the lit fraction, which leaks light; four moments give a sharp bound that is never weaker.
- Parallax mapping is exact only for constant depth. Parallax occlusion mapping lands within $1/k$ of the first hit when the relief is not thinner than a step. Displacement on a grid of step $\Delta$ has a height error of at most $\tfrac{\Delta^2}{8} \max |f''|$.
- Deferred shading pays $b$ bytes per pixel per pass to shade each pixel once. Tiled and clustered light lists never drop a light that reaches a pixel.
- Screen-space effects see one depth layer. SSAO estimates a volume fraction with variance at most $1/(4s)$ for $s$ samples. GTAO is the exact cosine-weighted occlusion of the height field that the depth buffer describes, not of the scene.
- Weighted blended transparency gets the coverage $1 - \prod_i (1 - \alpha_i)$ exactly. Its color is exact only when the weights are proportional to the transmittances, which depend on the order.

## The main approximations compared

| Method | Cost | What is exact or bounded | Main artefact |
|---|---|---|---|
| [Split sum](/split-sum-approximation/) | two lookups per pixel | exact for a constant environment | glossy lobes lose their stretch |
| [PCF](/percentage-closer-filtering/) | $\Theta(k)$ taps | the mean of the binary tests | fixed penumbra width |
| [PCSS](/percentage-closer-soft-shadows/) | $\Theta(m + k)$ taps | exact width for parallel planes | wrong width with mixed blockers |
| [VSM](/variance-shadow-maps/) | $O(1)$ after filtering | an upper bound, exact for two planes | light bleeding |
| [MSM](/moment-shadow-mapping/) | $O(1)$, four moments | the sharp four-moment bound | smaller leaks, needs precision |
| [POM](/parallax-occlusion-mapping/) | $\Theta(k)$ reads | within $1/k$ of the first hit | thin walls missed, flat outline |
| [Displacement](/displacement-mapping/) | triangles $\propto 1/\Delta^2$ | error at most $\tfrac{\Delta^2}{8} \max \lvert f'' \rvert$ | cracks and popping |
| [SSAO](/screen-space-ambient-occlusion/) | $O(p s)$ | unbiased for its volume fraction | noise, one depth layer |
| [GTAO](/ground-truth-ambient-occlusion/) | $O(p m s)$ | exact for the depth height field | one depth layer |
| [Linked lists](/per-pixel-linked-lists/) | $O(f)$ build, sort per pixel | exact while the pool lasts | memory, dropped fragments |
| [Weighted blended OIT](/weighted-blended-oit/) | $O(f)$, 9 bytes per pixel | exact coverage | wrong order of colors |

: Approximations of the chapter. $k$ and $m$ are tap or direction counts, $s$ samples per pixel, $p$ pixels and $f$ transparent fragments. The artefacts are measured, not bounded.

## Choosing a method

For shading, use GGX with the height-correlated Smith function and Schlick's Fresnel term, with metallic and roughness inputs as in physically based shading. Add Oren-Nayar for rough matte surfaces and linearly transformed cosines for polygonal area lights. Light dynamic objects with a prefiltered cube map and the split sum for specular, and with nine SH coefficients from an [irradiance volume](/irradiance-volume/) for diffuse. Bake light maps for static scenes.

For shadows from the sun, use cascaded shadow maps with a stable fit and PCF. Choose PCSS for contact hardening, and variance or moment maps when the map must be filtered; moment maps leak less where occluders overlap.

For surface detail, a normal map is the default. Add parallax occlusion mapping for deep relief, and displacement where the outline or the shadows must show it. For many lights, use deferred shading with clustered light lists, which beat tiles at depth gaps, or a visibility buffer when bandwidth is the limit. For transparency, weighted blended OIT is cheap and bounded in memory. Use per-pixel linked lists where the order of colors must be exact.
