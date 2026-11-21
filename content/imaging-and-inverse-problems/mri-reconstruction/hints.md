1. $42.577 \cdot 7 = 298.04$ MHz.

2. $\Delta k = 1/(0.24\ \text{m}) = 4.167$ cycles per meter and $k_{\max} = 96\,\Delta k = 400$ cycles per meter, so the pixels are $1/(2 \cdot 400)$ m $= 1.25$ mm.

3. The reduced field of view is $240/3 = 80$ mm. The positions $10 - 80 = -70$, $10$ and $10 + 80 = 90$ mm fold together.

6. For $c = 8$ the mean is $2.7846$ against $\sqrt 8 = 2.8284$; for $c = 32$ it is $5.6348$ against $5.6569$. The ratio tends to 1, as $\Gamma(c + \frac12)/\Gamma(c) \approx \sqrt c\,(1 - 1/(8c))$.

8. $2^{19} < 10^6 < 2^{20}$, so 20 iterations.

10. Solve $\rho_p + \rho_q/4 = 3/2$ and $\rho_p/2 + \rho_q = 5/2$: $\rho = (1, 2)$. Then $M = \begin{pmatrix} 5/4 & 3/4 \\ 3/4 & 17/16 \end{pmatrix}$ with $\det M = 49/64$. For two pixels both g-factors equal $\sqrt{M_{pp} M_{qq}/\det M} = \sqrt{85}/7 = 1.3171$.

12. $a = (64 + 16 + 1)/128 = 0.6328$. The variance is $\sigma^2 (128 - 17)/128 = 0.8672\,\sigma^2$, against $\sigma^2/2$ for the full line, so the standard deviation grows by $\sqrt{1.7344} = 1.317$.

16. $\cos(u + v) = \cos u \cos v - \sin u \sin v$ writes $X$ as a sum of two outer products of independent vectors, so the rank is 2. The constant adds the outer product of the all-ones vectors, which is independent of the other two, so the rank becomes 3.

17. With $p_1 = 1$, the other three share 2 samples: $p_k = 4\mu_k^2$, so $p = (1, 1, 1/2, 1/2)$ and $K^2 = 1/2$. Uniform sampling has $p_k = 3/4$ and $K^2 = 2/3$. The uncapped value $1/3$ cannot be reached.

18. The proximal gradient bound needs $k \ge 1/(2 \cdot 10^{-4}) = 5000$. FISTA needs $(k + 1)^2 \ge 2 \cdot 10^4$, so $k = 141$ is enough.

20. $M = \begin{pmatrix} 1 + a^2 & 2a \\ 2a & 1 + a^2 \end{pmatrix}$, so $g = (1 + a^2)/(1 - a^2)$. It is 1 at $a = 0$, $5/3$ at $a = 1/2$, and 2 at $a^2 = 1/3$, that is $a = 0.5774$.

22. Expand $\lVert D^{1/2}(E x^\star - y) + D^{1/2}E(x - x^\star)\rVert^2$; the cross term is zero because $E^H D (E x^\star - y) = 0$. Conjugate gradients minimize $\lVert x - x^\star\rVert_A$ over growing Krylov spaces. The plain residual is covered when $D$ is a multiple of $I$.

23. The iterates are $(2/3, 1/2, 2/3)$ and $(8/11, 3/7, 8/11)$. $Cw = \mathbf{1}$ gives $w = (1, 0, 1)$. Near the limit $w_1 \approx 1 - w_2/2$, so $(Cw)_2 \approx 1 + w_2/2$ and $1/w_2$ grows by about $1/2$ per step: $w_2 \approx 2/k$, a slow rate.

24. Put $\cos\alpha = E_1$ in $\sin\alpha (1 - E_1)/(1 - E_1\cos\alpha)$. Then $(1 - E_1)/(1 + E_1) = \tanh(T_R/(2T_1))$. For $T_R/T_1 = 0.01$ the Ernst signal is $0.07071\,M_0$, the approximation $0.07071\,M_0$, and the signal at $90°$ is $1 - E_1 = 0.00995\,M_0$.
