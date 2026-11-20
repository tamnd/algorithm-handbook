2. The optical depth is $-\ln 0.05 = 2.995732$. The first region uses 0.5 of it, so the particle goes $2.495732/3 = 0.831911$ cm into the second region and collides at $x = 1.831911$. It crosses $x = 1$ with probability $e^{-0.5} = 0.606531$.

4. $k_\infty = 0.015/0.012 = 1.25$. With $(\pi/50)^2 = 0.0039478$, $k_{\mathrm{eff}} = 0.015/0.0159478 = 0.940566$. The slab is critical when $D(\pi/L)^2 = \nu\Sigma_f - \Sigma_a = 0.003$, that is $L = \pi/\sqrt{0.003} = 57.357$ cm.

5. Diamond differences give $\psi_{\mathrm{out}} = (\mu/\Delta x - \Sigma_t/2)/(\mu/\Delta x + \Sigma_t/2) = (0.25 - 0.5)/0.75 = -1/3$, and the cell average is $1/3$. The exact value is $e^{-4} = 0.018316$. The outgoing flux is nonnegative when $\Sigma_t\Delta x \le 2|\mu|$, so $\Delta x \le 0.5$ cm.

6. Source iteration needs $\ln 10^{-6}/\ln 0.9 = 131.1$, so 132 sweeps. With the factor $0.2247 \cdot 0.9 = 0.2022$, it needs $\ln 10^{-6}/\ln 0.2022 = 8.6$, so 9 sweeps, each with one diffusion solve.

8. The track length in the cell is $1.2 + 0.5 = 1.7$ cm, so the track-length estimate is $1.7/2 = 0.85$. The collision estimator scores $1/\Sigma_t = 2$ at each of the two collisions, so it gives $4/2 = 2$. Both are unbiased; one history tells nothing about which is closer.

10. The weights are $0.6, 0.36, 0.216, 0.1296$. The first weight below 0.25 is $0.216$, after the third collision. It survives with probability $0.216/0.5 = 0.432$ and then has weight 0.5, so the expected weight is $0.432 \cdot 0.5 = 0.216$. An analog particle survives three collisions with probability $0.6^3 = 0.216$, half as often.

13. The characteristic polynomial is $\lambda^2 - 1.5\lambda + 0.48$, so $k_{\mathrm{eff}} = (1.5 + \sqrt{0.33})/2 = 1.037228$ and $k_2 = 0.462772$. The mode is $(0.686141, 0.313859)$, and the dominance ratio is $0.446162$. In 20 generations the second mode shrinks by $0.446162^{20} \approx 9.8 \times 10^{-8}$.

14. $R = 0.5 \cdot 0.01 + 0.5 \cdot 0.1 = 0.055$. The biased source puts $1/11$ of the particles in cell 1 and $10/11$ in cell 2, with birth weights $R/\phi^+ = 5.5$ and $0.55$. The targets are $5.5, 0.55, 0.06875$, so $w_L = \bar w/3$ gives the windows $[1.8333, 9.1667]$, $[0.18333, 0.91667]$ and $[0.022917, 0.11458]$. The particle of weight 0.55 is split into $\lceil 0.55/0.11458 \rceil = 5$ copies of weight 0.11.

19. The mean of both is $(1 - e^{-0.01})/0.01 = 0.995017$. The collision estimator scores $1/\Sigma_t = 100$ with probability $1 - e^{-0.01} = 0.00995$, so its variance is $98.51$. The track length is 1 unless the particle is absorbed inside, and its variance is about $0.0033$. In a thin gas collisions are rare, so use the track-length estimator.

20. Put the form into the slab equation: $(1 - \kappa\mu)g = c\phi/2$ with $\phi = \int g\,d\mu$. Integrating $c/(2(1 - \kappa\mu))$ gives $c\operatorname{artanh}(\kappa)/\kappa = 1$, which needs $\kappa < 1$. The series $\operatorname{artanh}(\kappa)/\kappa = 1 + \kappa^2/3 + \kappa^4/5 + \cdots$ gives $\kappa^2 = 3(1 - c) + O((1 - c)^2)$. For $c = 0.3$, $\kappa = 0.997414$ in transport and $1.449138$ in diffusion; the diffusion flux would decay faster than the uncollided flux, which is impossible.

21. Let the score of a unit-weight particle born at $x$ be 1 with probability $\phi^+(x)$. Analog: $E[S^2] = \int q\phi^+ = R$. Biased: $E[S^2] = \int (q\phi^+/R)(R/\phi^+)^2\phi^+ = R\int q = R$ for a normalized source. The means agree, so the variances are equal. The gain of CADIS comes from the windows that split and roulette the particles on their way.

22. $k_n = \nu\Sigma_f/(\Sigma_a + Dn^2\pi^2/L^2)$, so $d = (\Sigma_a + b)/(\Sigma_a + 4b)$ with $b = D\pi^2/L^2$, and $1 - d = 3b/(\Sigma_a + 4b)$. For $L = 100$, $d = 0.876361$ and 18 generations give a factor 10; for $L = 200$, $d = 0.964730$ and 65 generations.

23. The distance is a sum of a geometric number of exponential flights with rate $\Sigma_{\max}$; with $q = \Sigma_t/\Sigma_{\max}$ the Laplace transform is $\sum_k q(1 - q)^{k - 1}(\Sigma_{\max}/(\Sigma_{\max} + s))^k = \Sigma_t/(\Sigma_t + s)$. For a varying $\Sigma_t$, the tentative collisions form a Poisson process of rate $\Sigma_{\max}$, and accepting each with probability $\Sigma_t(x)/\Sigma_{\max}$ thins it to a Poisson process of rate $\Sigma_t(x)$. The mean number of tentative collisions per centimetre is $\Sigma_{\max}$.

24. A sweep gives $\psi_\mu = (c\phi/2)/(1 + i\mu\lambda)$, and summing over the two directions with weight 1 gives $c\phi\,\mathrm{Re}(1/(1 + i\lambda/\sqrt3)) = c\phi/(1 + \lambda^2/3)$. At $\lambda = 1$ the factors are $0.75c$ and $0.785398c$. Both tend to $c$ as $\lambda \to 0$: the smooth modes are the slow ones, which is why a diffusion correction works.
