In these exercises $\omega(\theta) = (\cos\theta, \sin\theta)$, $\omega^\perp(\theta) = (-\sin\theta, \cos\theta)$ and $\mathcal{R}f(\theta, s) = \int f(s\,\omega + t\,\omega^\perp)\,dt$ for $\theta \in [0, \pi)$, as in the [Radon transform](/radon-transform/) entry. Fourier transforms use the ordinary frequency, $\hat g(\sigma) = \int g(s) e^{-2\pi i \sigma s}\,ds$. Angles are in radians unless degrees are given.

1. ◦ A disk of radius $1/2$ with constant density 2 has its center at $(0.3, 0)$. Give the range of $s$ where $\mathcal{R}f(\pi/3, s) \ne 0$, and compute $\mathcal{R}f(\pi/3, 0.2)$.

2. ◦ The point $(0.4, -0.3)$ traces a curve $s(\theta)$ in the [sinogram](/sinogram/). Write it as $A\cos(\theta + \phi)$ and find $s(0)$, the angle in $[0, \pi)$ where $s = 0$, and the smallest value of $s$ with the angle where it occurs.

3. ◦ For $f(x) = e^{-|x|^2}$, compute $\mathcal{R}f(\theta, s)$, its 1D transform in $s$, and the 2D transform $\hat f(\xi)$. Check that they agree on the line $\xi = \sigma\,\omega(\theta)$, as the [Fourier slice theorem](/fourier-slice-theorem/) says.

4. ◦ A ray crosses 10 cm of water ($\mu = 0.2$ per cm) and 2 cm of bone ($\mu = 0.5$ per cm). Compute the line integral $p$ and the fraction $I/I_0$ that gets through. With $N_0 = 10^5$ photons sent, give the expected count and the standard deviation of the measured $p$.

5. ◦ A fan-beam scanner has its source at distance $D = 4$ from the center, and the object fits in the disk of radius 1. Find the half fan angle $\delta$ in degrees and the length of the short scan $\pi + 2\delta$ in radians and in degrees.

6. ◦ In SPECT, a uniform disk of radius 10 cm has $\mu = 0.15$ per cm, and a point source sits at $(5, 0)$. Compute the attenuation factor of the [attenuated Radon transform](/attenuated-radon-transform/) for the photons that leave along the positive $x$ direction and for those along the negative $x$ direction, and the ratio of the two.

7. ◦ (a) A parallel-beam scan has $d = 512$ detector bins. How many angles does the rule $a \approx \pi d/2$ ask for? (b) A sparse-view scan of a $256 \times 256$ image uses $a = 60$ angles and $d = 367$ bins. How many equations are there, and what is the least possible dimension of the null space of the system matrix?

8. ◦ One pixel is seen by three bins with weights $a = (1, 2, 3)$, no background, and counts $y = (4, 5, 9)$. Show that one [MLEM](/mlem-reconstruction/) step from any $x_0 > 0$ gives the maximum likelihood estimate, compute it, and compute the Cramér-Rao bound for its variance at that value.

9. ◦ The Ram-Lak kernel with $\tau = 1$ has the samples $h(0) = 1/4$, $h(m) = 0$ for even $m \ne 0$ and $h(m) = -1/(\pi^2 m^2)$ for odd $m$. Show that $\sum_m h(m) = 0$ and say what this means for the filtered projection of a constant. Compute the truncated sum over $|m| \le 5$.

10. • The square $[-1, 1]^2$ is cut into $4 \times 4$ pixels of side $1/2$. Pixel $(i, j)$ is in row $i$ counted from the top and column $j$ counted from the left, both from 0. Run [Siddon's algorithm](/siddon-algorithm/) by hand on the ray from $(-1, -3/4)$ to $(1, 3/4)$: list the crossing parameters $\alpha$ in $[0, 1]$, the pixels in order, and the length in each. Check the total.

11. • Let $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}$ and $y = (1, 2, 4)$. Run one step of [SIRT](/sirt/) with $\lambda = 1$ from $x = 0$, using the row sums and column sums of $A$. Find the limit of SIRT and compare it with the ordinary least squares solution.

12. • In the scaled form of SIRT, a singular value $\sigma$ of $B$ has the filter factor $1 - (1 - \lambda\sigma^2)^k$ after $k$ steps. For $\sigma = 0.01$, how many steps does it take for the factor to reach $1/2$ with $\lambda = 1$, and with $\lambda = 1.9$?

13. • With the matrix $A$ of exercise 11, no background, counts $y = (2, 4, 5)$ and the start $x = (1, 1)$, run one MLEM step. Check that the total count is kept. Then find the maximum likelihood estimate from the KKT conditions.

14. • One pixel is seen by two bins, each with weight 1, with counts $y = (1, 3)$. Run [OSEM](/osem/) with each bin as its own subset, from $x_0 = 1/2$. Describe the iterates and compare them with the maximum likelihood estimate.

15. • A beam is half photons with $\mu = 0.3$ per cm and half with $\mu = 0.2$ per cm in some material. Compute $p(L) = -\ln(\tfrac12 e^{-0.3L} + \tfrac12 e^{-0.2L})$ at $L = 20$ cm and compare it with the linear value $\bar\mu L$. Compute $p'(0)$ and $p''(0)$, and the slope $p'(20)$.

16. • For each pair, decide whether a $4 \times 4$ 0-1 matrix exists with the given row sums and column sums, and give one when it does: (a) rows $(3, 2, 2, 1)$, columns $(3, 3, 1, 1)$; (b) rows $(3, 1, 1, 1)$, columns $(3, 3, 0, 0)$.

17. • In [limited-angle tomography](/limited-angle-tomography/), the stripe functions $f_K$ have data at most $e^{-\pi K^2 \sin^2\delta}$ on the measured angles when the missing range is $|\theta - \varphi| < \delta$. For $\delta = 10°$, how large must $K$ be for the data to fall below $10^{-6}$? What is the bound for $\delta = 15°$ and $K = 10$?

18. • Two pixels, $A = I$, $b = 0$, and the penalty $R(x) = \tfrac12 (x_1 - x_2)^2$. The [one-step-late](/one-step-late-algorithm/) denominator of pixel 1 is $1 + \beta (x_1 - x_2)$. For the current image $x = (0.1, 5)$, find the values of $\beta$ for which the update fails.

19. • For one bin of the [SPS](/separable-paraboloidal-surrogates/) method with $y = 10$, $b = 1$ and the current line sum $l = 4$, compute the optimal curvature $c$. Compare it with $h''(4)$ and $h''(0)$, and explain why $c$ lies between them.

20. • A circular cone-beam orbit has radius $R = 5$. For a point at height $z = 1$ above the orbit plane, compute the fraction of plane normals that the [Tuy condition](/tuy-condition/) misses, and compare it with the small-height value $z^2/(2R^2)$.

21. ★ Filter white noise of variance $v$ with the Shepp-Logan kernel $h(m) = -2/(\pi^2\tau^2(4m^2 - 1))$, as $q_k = \tau \sum_m h(m) p_{k - m}$. Find the variance of $q_k$ in closed form and compare it with $v/(12\tau^2)$ for Ram-Lak.

22. ★ Show that the sets $\{(0, 0), (2, 1), (1, 2)\}$ and $\{(1, 0), (0, 1), (2, 2)\}$ of lattice points have the same X-rays in the three directions $(1, 0)$, $(0, 1)$ and $(1, 1)$, that is, the same number of points on every lattice line in those directions. What does this say about [discrete tomography](/discrete-tomography/) with these three directions?

23. ★ Count the $3 \times 3$ 0-1 matrices with row sums $(2, 1, 1)$ and column sums $(2, 1, 1)$. Then show that row sums $(3, 2, 1)$ and column sums $(3, 2, 1)$ determine the matrix uniquely.

24. ★ In [interior tomography](/interior-tomography/) with $r = 1/3$, take $p(s) = (s^2 - r^2)^2 (1 - s^2)^2$ for $r < |s| < 1$ and zero elsewhere. Compute the value $G(0) = -\frac{1}{\pi}\int_r^1 p(s)/s^2\,ds$ of the null function at the center exactly. Check your method on $r = 1/2$, where the entry gives $-0.002842$.

25. ★ Three projections of a particle in cryo-EM have the beam directions $d_1, d_2, d_3$. In image $i$ the common line with image $j$ points along $d_i \times d_j$. In each image the two common lines make the angle $120°$. Find the angle between any two beam directions.
