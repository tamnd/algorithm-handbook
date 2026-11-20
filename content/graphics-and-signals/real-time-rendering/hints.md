1. $F_0 = (0.33/2.33)^2 = 0.0201$. At $60°$, $1 - \cos\theta = 0.5$ and $0.5^5 = 1/32$, so $F = 0.0201 + 0.9799/32 = 0.0507$. The exact Fresnel value is 0.0591.

3. $\lfloor 4x \rfloor$ gives 0, 1, 2 and 4, so the bands are 0, 1, 2 and 3. The value $x = 1$ needs the clamp by $\min$, or it would read a fifth band.

5. $L = 0.18 \cdot 2/0.5 = 0.72$ and $L_d = 0.72/1.72 = 0.4186$. For $L_w = 0.05$, $L = 0.018$ and $L_d = 0.0177$: dark values stay almost linear.

7. BC1: $512^2$ blocks of 8 bytes, 2 097 152 bytes, 4 bits per texel. ASTC $8 \times 8$: $256^2$ blocks of 16 bytes, 1 048 576 bytes, 2 bits per texel. ASTC $6 \times 6$: $\lceil 2048/6 \rceil^2 = 342^2$ blocks, 1 871 424 bytes, $128/36 = 3.56$ bits per texel. Uncompressed RGBA8 takes 16 777 216 bytes.

9. $240 \times 135 = 32\,400$ tiles, all full, since 16 divides both sides. The cull makes $32\,400 \cdot 500 = 16\,200\,000$ sphere tests. At $1920 \times 1080$ the last tile row would be half full.

12. $\Lambda = (-1 + \sqrt{1 + 0.09 \tan^2 70°})/2 = 0.1480$, so $G_1 = 0.8711$. Separable: 0.7588. Height-correlated: $1/(1 + 2\Lambda) = 0.7717$, larger, as it must be. Schlick-GGX with $k = 0.15$ gives 0.7761, too low by 0.095. At $\alpha = 1$, $\sqrt{1 + \tan^2\theta} = 1/c$, so $G_1 = 2c/(c + 1)$, and $c/(c/2 + 1/2)$ is the same.

14. $(1 - 0.5)^5 = 1/32$. The factors are $(1 - 0.5/32)^2 = 0.9690$ for $r = 0$, $(1 - 0.25/32)^2 = 0.9844$ for $r = 0.5$, and exactly 1 for $r = 1$, where $F_{D90} = 1$. At $\theta_d = 0$ and $r = 1$, $F_{D90} = 2.5$ and the factor is $(1 + 1.5/32)^2 = 1.0960$: the rough surface reflects more back toward the light.

16. Logarithmic: 0.5, 3.684, 27.144, 200, with the ratio $400^{1/3} = 7.368$. Uniform: 0.5, 67, 133.5, 200. Practical: the means, 0.5, 35.342, 80.322, 200.

18. $m_1 = 0.4$ and $v = 0.04$, so $p = 0.04/(0.04 + 0.09) = 4/13 = 0.308$, where the truth is 0. The reduction gives $(4/13 - 1/4)/(3/4) = 1/13 = 0.077$.

19. $q = 1 + 2 \cdot 0.57735/17 = 1.0679$. The slices number $\lceil \ln(10^4)/\ln q \rceil = \lceil 140.2 \rceil = 141$. At depth 5, $k = \lfloor \ln 50/\ln q \rfloor = 59$, the slice that starts at 4.83.

23. The samples at $r = 0.375$ ($f = -0.0094$) and $r = 0.5$ ($f = 0.05$) bracket the hit. The secant gives $t = 3/19$ and $\hat r = 0.375 + 0.125 \cdot 3/19 = 15/38 = 0.3947$. The root of $0.6 r^2 - r + 0.3 = 0$ is $r^* = 0.3924$, so the error is 0.0024, and $u = 0.5 + 0.2 \hat r = 0.5789$.

25. With $s + 2 = 2/\alpha^2$, the peak is $1/(\pi\alpha^2)$, which is the GGX peak, 3.5368 for $\alpha = 0.3$ ($s = 20.22$). At $15°$ Blinn-Phong gives 1.7544 and GGX 1.2571; at $30°$, 0.1929 and 0.2842; at $45°$, 0.0032 and 0.0964, thirty times more. GGX is narrower at the core and has the long tail.

26. $A_9(-1) = 1/16$ and $A_9(1) = 17/16$. The error is largest at $t = 0$, where it is $3/32$, the proved bound. The derivative of $A_9(t) - \max(t, 0)$ vanishes at $t = \pm 8/15$, where the value is $3/32 - 2/15 = -19/480$.

27. The density is 1 at the center and $1/3^{3/2}$ at a corner, so the ratio tends to $3\sqrt3 = 5.196$. At 256 texels per side it is already 5.155; at 4 it is 2.47.

28. One wall blocks half of $1 - \delta/\sqrt{\delta^2 + H^2}$ of the cosine-weighted hemisphere, so two walls leave $\delta/\sqrt{\delta^2 + H^2} = 0.6$. For the solid angle, each wall blocks $\arctan(H/\delta)/\pi$, so the visibility is $1 - 2\arctan(4/3)/\pi = 0.4097$. With one wall the values are 0.8 and 0.7048. A seeded Monte Carlo run of 400 000 rays gives 0.601 and 0.410.

30. Ring $k$ has the area $3\pi 4^k d_0^2$ and costs $3\pi\rho d_0^2 T$, independent of $k$. The disc of radius $2d_0$ costs $4\pi\rho d_0^2 T$, and the rings $k = 1, 2, 3$ add $9\pi\rho d_0^2 T$, so the total is $13\pi\rho d_0^2 T$ against $256\pi\rho d_0^2 T$ at full detail, about 1/20. The cost grows with the logarithm of the view distance.
