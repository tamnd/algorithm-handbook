1. The linear convolution is $(1, 1, 1, -3)$. With length 3 the last sample, $-3$, wraps around onto index 0, so the circular result is $(-2, 1, 1)$. The two agree from length $3 + 2 - 1 = 4$ on.

3. The first is not stable, because $\sum 1/(n + 1)$ diverges; the second is, because $\sum 1/(n + 1)^2 = \pi^2/6$. The constant input $x[n] = 1$ gives $y[n] = \sum_{k=0}^{n} 1/(k + 1)$, which grows like $\ln n$.

6. The costs are 14.0, 10.67, 10.29, 10.67 and 11.35 multiplies per output. $N = 256$ is cheapest at about 10.3, against 33 for the direct form.

9. The matched filter is the pulse reversed, $h = (-1, 2, 1)$, and its SNR is $E/\sigma^2 = 6/\sigma^2$. The averaging filter gives $(\sum s)^2 / (3\sigma^2) = 4/(3\sigma^2)$, which is 4.5 times smaller.

12. The samples are $\cos(\pi n + \varphi) = (-1)^n \cos\varphi$, so the amplitude $A$ and the phase enter only through $A\cos\varphi$. For example $\cos(2\pi B t)$ and $2\cos(2\pi B t + \pi/3)$ both give $(-1)^n$, and $\sin(2\pi B t)$ gives zeros.

14. The shifted windows add to a constant when the hop divides the period of the cosine term evenly, that is, when $N/R$ is a whole number of at least 2. So $R = 3$, 4 and 6 work, with constants $N/(2R) = 2$, $1.5$ and $1$. For $R = 5$ the sum moves between about 1.134 and 1.25.

16. The zeros are $2$ and $\tfrac12$. Move the zero at 2 to $\tfrac12$ and scale by 2: $2(1 - \tfrac12 z^{-1})^2 = 2 - 2z^{-1} + \tfrac12 z^{-2}$. The partial energies are $(1, 7.25, 8.25)$ for the original filter and $(4, 8, 8.25)$ for the minimum phase one, which gets its energy out first.

17. The mean error along eigenvector $i$ shrinks by $1 - \mu\lambda_i$ per sample. The eigenvalues are 1.9 and 0.1, so the mean converges for $0 < \mu < 2/1.9 \approx 1.053$. With $\mu = 2/(\lambda_{\max} + \lambda_{\min}) = 1$ both factors have size 0.9. The spread of 19 is what makes this slow.

20. $d = (4, 0, -4, -5)$ and $s = (5, 1, 4, 6)$. The inverse is $x[2i] = s[i] - \lfloor d[i]/2 \rfloor$ and then $x[2i+1] = d[i] + x[2i]$. Each $s[i]$ is the pair average rounded down: the pair $(9, 4)$ has average 6.5 and gives 6.

21. $d = (0, 8, 16, 8, 0)$ and $d' = (1, 1, \tfrac43, \tfrac34, 0)$. The first lag below the threshold is $\tau = 4$, so the pitch is $f_s/4$.

24. A sum of $K$ independent exponentials of mean 1 has the gamma law, so the probability that the average exceeds 3 is $e^{-3K} \sum_{j<K} (3K)^j / j!$. It is 0.0498, 0.0174, 0.0062, 0.0023 and 0.00086 for $K = 1, \ldots, 5$, so $K = 5$ is the least.

25. The Fejér kernel is nonnegative and has mean 1 over a period, so each Cesàro mean is a weighted average of values of the square wave, all in $[-1, 1]$. The price is a wider transition at the jump: the Fejér kernel of order $m$ is a smoother but broader bump than the Dirichlet kernel, and the means converge more slowly.

26. Writing the cosine as two exponentials gives $W(f) = T e^{-i\pi f T}\,[\tfrac12 \operatorname{sinc}(u) + \tfrac14 \operatorname{sinc}(u - 1) + \tfrac14 \operatorname{sinc}(u + 1)]$ with $u = fT$, and the bracket equals $\operatorname{sinc}(u) / (2(1 - u^2))$. The extra factor $1/(1 - u^2)$ turns the $1/f$ fall of the sinc into $1/f^3$: 18 dB per octave, against 6 dB for the rectangular window.

27. In steady state $P^- = P + q$ and $P = P^- r/(P^- + r)$, so $(P^-)^2 - qP^- - qr = 0$ and $P^- = (q + \sqrt{q^2 + 4qr})/2$, with $K = P^-/(P^- + r)$. The update $m_t = (1 - K) m_{t-1} + K y_t$ is an exponential moving average. $K \to 1$ as $r \to 0$, and $K \approx \sqrt{q/r}$ as $q/r \to 0$. For $q = r = 1$, $P^- = (1 + \sqrt 5)/2 \approx 1.618$ and $K = (\sqrt 5 - 1)/2 \approx 0.618$.

28. Substitute $a = (\rho, 0, \ldots, 0)$ in row $i$ of the normal equations: $\rho \cdot \rho^{|i-1|} = \rho^i$ for every $i \ge 1$. The error is $r[0] - \rho\, r[1] = 1 - \rho^2$. So the first reflection coefficient has size $|\rho|$ and all later ones are zero, and the error stops falling after order 1, as it must for a first-order autoregressive signal.
