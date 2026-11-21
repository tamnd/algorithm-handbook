1. The center projects to $c \cdot \omega = 0.3 \cos(\pi/3) = 0.15$, so the support is $-0.35 \le s \le 0.65$. The chord at $s$ has length $2\sqrt{1/4 - (s - 0.15)^2}$, and $\mathcal{R}f(\pi/3, 0.2) = 4\sqrt{0.2475} = 1.98997$.

2. $s(\theta) = 0.4\cos\theta - 0.3\sin\theta = 0.5\cos(\theta + 0.6435)$. So $s(0) = 0.4$, $s = 0$ at $\theta = \pi/2 - 0.6435 = 0.9273$, and the smallest value $-0.5$ is at $\theta = \pi - 0.6435 = 2.4981$.

4. $p = 0.2 \cdot 10 + 0.5 \cdot 2 = 3$ and $I/I_0 = e^{-3} = 0.0498$. The expected count is $4979$, and the standard deviation of $p = -\ln(N/N_0)$ is about $1/\sqrt{4979} = 0.0142$.

5. $\delta = \arcsin(1/4) = 0.25268$, which is $14.478°$. The short scan is $\pi + 2\delta = 3.6470$, or $208.955°$.

7. (a) $\pi \cdot 512/2 = 804.2$, so about 804 angles. (b) $60 \cdot 367 = 22020$ equations for $65536$ unknowns, so the null space has dimension at least $65536 - 22020 = 43516$.

9. The odd terms give $2 \sum_{m \text{ odd}, m \ge 1} 1/(\pi^2 m^2) = (2/\pi^2)(\pi^2/8) = 1/4$. A constant projection filters to 0, as the ramp is zero at zero frequency. The truncated sum is $1/4 - (2/\pi^2)(1 + 1/9 + 1/25) = 0.016736$.

10. The ray is $(-1 + 2\alpha, -3/4 + 3\alpha/2)$ with length $5/2$. The vertical lines give $\alpha = 1/4, 1/2, 3/4$ and the horizontal lines give $\alpha = 1/6, 1/2, 5/6$. The pixels are $(3,0), (2,0), (2,1), (1,2), (1,3), (0,3)$ with lengths $5/12, 5/24, 5/8, 5/8, 5/24, 5/12$, which add to $5/2$.

11. The row sums are $(1, 1, 2)$ and the column sums $(2, 2)$. The first iterate is $(1.5, 2)$. SIRT converges to the minimizer of $\sum_i (Ax - y)_i^2 / r_i$, which is $(5/4, 9/4)$; ordinary least squares gives $(4/3, 7/3)$.

13. The sensitivities are $s = (2, 2)$. One step gives $(2.25, 3.25)$, and $2.25 + 3.25 + 5.5 = 11 = \sum_i y_i$. The KKT conditions with both pixels positive are $2/x_1 + 5/(x_1 + x_2) = 2$ and $4/x_2 + 5/(x_1 + x_2) = 2$, solved by $(11/6, 11/3)$.

16. Use the Gale-Ryser condition: (a) holds, and one matrix has the rows $0111$, $1100$, $1100$, $1000$. (b) fails at $k = 2$, since the two largest column sums give $6$ while $\sum_i \min(r_i, 2) = 5$.

19. With $h(l) = (l + b) - y\log(l + b)$, $c = 2[h(0) - h(4) + 4h'(4)]/16 = 1.0118$, while $h''(4) = 0.4$ and $h''(0) = 10$. The surrogate must touch $h$ at $l$ and stay above it down to $0$, where $h$ is much more curved.

21. The variance is $v\tau^2 \sum_m h(m)^2 = \frac{4v}{\pi^4\tau^2}\bigl(1 + 2\sum_{m \ge 1} (4m^2 - 1)^{-2}\bigr)$. Use $\sum_{m \ge 1} (4m^2 - 1)^{-2} = (\pi^2 - 8)/16$ to get $v/(2\pi^2\tau^2) = 0.05066\,v/\tau^2$, about $0.61$ times the Ram-Lak value.

22. Count the points with each value of $x$, of $y$ and of $x - y$. Adding one set and removing the other is a switching component, so no 0-1 image is determined by these three X-rays when it contains such a pattern.

23. There are 5 matrices: fix where the row with sum 2 puts its ones and count. For $(3, 2, 1)$ the Gale-Ryser inequalities hold with equality at every $k$, which forces the staircase with rows $111$, $110$, $100$.

24. Write $p(s)/s^2$ as $r^4/s^2$ plus a polynomial in $s^2$ and integrate term by term. The result is $G(0) = -1280/(45927\pi) = -0.0088714$. For $r = 1/2$ the integral is $1/112$, so $G(0) = -1/(112\pi) = -0.0028421$.
