1. ◦ Water has the refractive index $\eta = 1.33$. Find its $F_0 = ((\eta - 1)/(\eta + 1))^2$ and the value of the [Schlick approximation](/schlick-fresnel-approximation/) at an incidence of $60°$.

2. ◦ An artist sets the roughness $r = 0.5$, and the engine uses $\alpha = r^2$. What is the peak value of the [GGX distribution](/ggx-distribution/), reached at $n \cdot h = 1$? What is it for $r = 1$?

3. ◦ A [toon shader](/toon-shading/) has $k = 4$ bands and picks the band $i = \min(k - 1, \lfloor k x \rfloor)$ with $x = \max(0, n \cdot l)$. Give the band for $x = 0$, $0.25$, $0.62$ and $1$.

4. ◦ Use [Gooch shading](/gooch-shading/) with $b = y = 0.4$, $\alpha = 0.2$ and $\beta = 0.6$, so $k_{\text{cool}} = (0, 0, b) + \alpha k_d$ and $k_{\text{warm}} = (y, y, 0) + \beta k_d$, and the color is $t\, k_{\text{warm}} + (1 - t) k_{\text{cool}}$ with $t = (1 + n \cdot l)/2$. Find the color of a pure blue object, $k_d = (0, 0, 1)$, at $n \cdot l = 1$, $0$ and $-1$.

5. ◦ An image has the log-average luminance $\bar L = 0.5$. With the key $a = 0.18$ and no white point, the global [Reinhard operator](/reinhard-tone-mapping/) computes $L = a L_w / \bar L$ and $L_d = L/(1 + L)$. Find $L_d$ for the pixels with $L_w = 2$ and $L_w = 0.05$.

6. ◦ The improved [Perlin noise](/perlin-noise/) uses the fade $f(t) = 6t^5 - 15t^4 + 10t^3$. Compute $f(1/2)$ and $f(3/4)$ as exact fractions.

7. ◦ A $2048 \times 2048$ color texture is stored in BC1 of [S3TC](/s3-texture-compression/), and in [ASTC](/adaptive-scalable-texture-compression/) with $8 \times 8$ and with $6 \times 6$ footprints. Give the size in bytes of each, without mipmaps, and the bits per texel of the $6 \times 6$ form. Compare with 4 bytes per texel.

8. ◦ A simplified mesh has the geometric error $\varepsilon = 0.02$ m. The image is 1920 pixels wide with a horizontal field of view of $90°$. Following [level of detail](/level-of-detail/), from what distance is the projected error below 1 pixel? Below 2 pixels?

9. ◦ A frame of $3840 \times 2160$ pixels uses [tiled shading](/tiled-shading/) with $16 \times 16$ tiles and 500 lights. How many tiles are there, and how many sphere tests does the cull make by brute force?

10. ◦ A [variance shadow map](/variance-shadow-maps/) lookup gives the filtered moments $m_1 = 0.4$ and $m_2 = 0.17$. Find the variance and the bound on the lit fraction for the receiver depths $t = 0.5$ and $t = 0.35$.

11. ◦ [Simplex noise](/simplex-noise/) skews by $F = (\sqrt{n + 1} - 1)/n$ and unskews by $G = (1 - 1/\sqrt{n + 1})/n$. Compute $F$ and $G$ for $n = 2$ and $n = 3$.

12. • For GGX with $\alpha = 0.3$ and $\theta = 70°$, compute the exact [Smith](/smith-masking-shadowing-function/) $G_1$. For $l$ and $v$ both at $70°$, compare the separable $G_1 G_1$ with the height-correlated $1/(1 + \Lambda_l + \Lambda_v)$. Then compute the Schlick-GGX form $c/(c(1 - k) + k)$ with $c = \cos\theta$ and $k = \alpha/2$, and show that it equals the exact $G_1$ at every angle when $\alpha = 1$.

13. • In the [Oren-Nayar model](/oren-nayar-reflectance-model/) with $\sigma = 0.3$, find $A = 1 - 0.5\sigma^2/(\sigma^2 + 0.33)$ and $B = 0.45\sigma^2/(\sigma^2 + 0.09)$. Light and view are both at $60°$ from the normal. Give the factor $A + B \max(0, \cos\Delta\phi) \sin\alpha \tan\beta$ that multiplies the Lambert value for $\Delta\phi = 0$ and for $\Delta\phi = 180°$.

14. • The diffuse term of the [Disney principled BRDF](/disney-principled-brdf/) multiplies $\rho/\pi$ by $\big(1 + (F_{D90} - 1)(1 - \cos\theta_l)^5\big)\big(1 + (F_{D90} - 1)(1 - \cos\theta_v)^5\big)$ with $F_{D90} = 0.5 + 2 r \cos^2\theta_d$. Light and view are at $60°$ on opposite sides of the normal, so $\theta_d = 60°$. Compute the factor for $r = 0$, $0.5$ and $1$. Then put light and view at the same $60°$ direction ($\theta_d = 0$) and compute it for $r = 1$.

15. • The Reinhard curve with a white point is $L_d = L(1 + L/W^2)/(1 + L)$. Show that $L = W$ maps to 1. For $W = 4$, which scaled luminance $L$ maps to $L_d = 1/2$?

16. • [Cascaded shadow maps](/cascaded-shadow-maps/) with $n = 0.5$, $f = 200$ and $m = 3$ use the split $C_i = \lambda n (f/n)^{i/m} + (1 - \lambda)(n + (f - n) i/m)$. Give the splits for $\lambda = 1$, $0$ and $0.5$, and the ratio $C_{i+1}/C_i$ of the logarithmic split.

17. • In [percentage-closer soft shadows](/percentage-closer-soft-shadows/), the light has the width $w = 0.5$, the map has the near plane at $n = 1$ and texels of side $h = 0.01$ on it, the blocker is at $d_b = 3$ and the receiver at $d_r = 5$. Find the penumbra width $w_p = w(d_r - d_b)/d_b$, the filter half-width $r_f = n\, w_p/(2 d_r h)$ and the search half-width $r_s = w(d_r - n)/(2 d_r h)$, in texels.

18. • The filter of a variance shadow map holds two occluders, at the depths 0.2 and 0.6 with equal weight, over a receiver at 0.7. Find the variance bound on the lit fraction as an exact fraction, then apply the bleeding reduction $(p - a)/(1 - a)$ with $a = 1/4$. What is the true lit fraction?

19. • [Clustered shading](/clustered-shading/) slices the depth at $n_k = n_0 q^k$ with $q = 1 + 2 \tan\theta / S_y$. Take a vertical field of view of $60°$ ($\tan\theta = \tan 30°$), $S_y = 17$ tile rows, $n_0 = 0.1$ and a far depth of 1000. Find $q$, the number of slices, and the slice index of a pixel at depth 5.

20. • A frame of $2560 \times 1440$ pixels has on average 6 transparent fragments per pixel. [Per-pixel linked lists](/per-pixel-linked-lists/) use 16-byte nodes and a 4-byte head pointer per pixel. How many bytes do they need with a pool sized for the average? Compare with [weighted blended OIT](/weighted-blended-oit/), which needs an RGBA16F target and an R8 target.

21. • ASTC stores 16 weights by integer sequence encoding. With the range $0..4$ (quints, $n = 0$) a stream of $V$ values takes $V n + \lceil 7V/3 \rceil$ bits, and with the range $0..5$ (trits, $n = 1$) it takes $V n + \lceil 8V/5 \rceil$ bits. Compute both, compare with fixed 3-bit fields and with $\log_2$ of the number of possible sequences.

22. • With $M$ the identity, the polygon formula of [linearly transformed cosines](/linearly-transformed-cosines/) gives the cosine-weighted fraction $\frac{1}{2\pi} \sum_i \arccos(\hat a_i \cdot \hat b_i) \big(\mathrm{normalize}(\hat a_i \times \hat b_i)\big)_z$ over the edges. Evaluate it for a square light with the corners $(\pm 1, \pm 1, 1)$ above a point at the origin with the normal $+z$.

23. • Run [parallax occlusion mapping](/parallax-occlusion-mapping/) with $k = 8$ steps on the depth profile $m(r) = 0.3 + 0.6 r^2$ along the ray, with $\Delta = (0.2, 0)$ and $u_0 = 0.5$. Which two samples bracket the hit? Give the secant result $\hat r$, the true $r^*$, and the texture coordinate $u$.

24. • A [geometry clipmap](/geometry-clipmaps/) has $L = 5$ levels of $n = 31$ vertices on a side. Level 0 draws $(n - 1)^2$ cells, and each coarser level draws a ring of $(n - 1)^2 - ((n - 1)/2)^2$ cells. How many triangles does the mesh have, and how many zero-area triangles close the borders between levels (one per coarse edge on each finer window)?

25. ★ The normalized Blinn-Phong distribution $D = \frac{s + 2}{2\pi} (n \cdot h)^s$ is matched to roughness by $s = 2/\alpha^2 - 2$. Show that its peak then equals the GGX peak exactly. For $\alpha = 0.3$, compare the two at $\theta_h = 15°$, $30°$ and $45°$.

26. ★ The [irradiance environment map](/irradiance-environment-map/) replaces the clamped cosine $\max(t, 0)$ by $A_9(t) = 3/32 + t/2 + 15t^2/32$. Find $A_9(-1)$ and $A_9(1)$, the largest error over $t \in [-1, 1]$ and where it occurs, and the most negative value of $A_9(t) - \max(t, 0)$ and where it occurs.

27. ★ A [cube map](/cube-map/) face is the square $[-1, 1]^2$ at distance 1, so a small area $dA$ at $(x, y)$ subtends $dA/(1 + x^2 + y^2)^{3/2}$. As the resolution grows, what does the ratio of the solid angle of a center texel to that of a corner texel tend to?

28. ★ A floor point lies in the middle of a long trench of width 6 whose walls are 4 high, so each wall is at $\delta = 3$ with $H = 4$. Find its cosine-weighted visibility, the value [GTAO](/ground-truth-ambient-occlusion/) computes, and its uniform solid-angle visibility, the value [HBAO](/horizon-based-ambient-occlusion/) computes with no falloff. Compare with a single wall.

29. ★ Two fragments of the same opacity $\alpha$ lie over black: pure red in front and pure blue behind. Weighted blended OIT with equal weights mixes them. Show that the red channel is too low by $\alpha^2/2$ and the blue channel too high by the same amount, and find the weight ratio $w_{\text{front}}/w_{\text{back}}$ that makes the result exact.

30. ★ Objects of $T$ triangles each are spread with density $\rho$ over a plane around the viewer. The full mesh is used up to the distance $2d_0$, and level $k \ge 1$, with $T/4^k$ triangles, is used for distances in $[2^k d_0, 2^{k+1} d_0)$. Show that every ring costs the same number of triangles, and find the total for a view distance of $16 d_0$, compared with drawing every object at full detail.
