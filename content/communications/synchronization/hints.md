1. $K_p = 0.026667$ and $K_i = 3.5556\times10^{-4}$, and $2K_p + K_i = 0.0537 < 4$, so the loop is stable. The
integrator absorbs a constant frequency offset, so the steady phase error is $0$. A ramp of $\alpha$ rad per
symbol squared leaves $\alpha/K_i = 0.0028125$ rad. The first-order loop settles where
$K_p\sin e = 0.002$, so $e = \arcsin(0.075) = 0.0751$ rad.

3. $\mathrm{SNR} = 10^{0.8} = 6.3096$, so the bound is $1/(2\cdot64\cdot6.3096) = 1.238\times10^{-3}$ rad$^2$,
a standard deviation of $0.0352$ rad or $2.02°$. One degree is $0.017453$ rad, so
$N \ge 1/(2\,\mathrm{SNR}\,(0.017453)^2) = 260.1$, which means 261 symbols.

5. Solve $(1 - \lambda)^{30} = 10^{-4}$: $\lambda = 1 - 10^{-4/30} = 0.2644$. An exact match of 31 random bits
has the probability $2^{-31} = 4.66\times10^{-10}$, far below the soft detector's rate, but the hard rule
also misses the word whenever a single bit of it is wrong.

8. $c_0 = x_0 = -1$, $c_1 = -x_{-1}/3 - x_0/2 + x_1 - x_2/6 = -2/3$, $c_2 = x_{-1}/2 - x_0 + x_1/2 = 2$, and
$c_3 = -x_{-1}/6 + x_0/2 - x_1/2 + x_2/6 = -1/3$. Horner's rule gives
$y(0.25) = -1 + 0.25(-2/3 + 0.25(2 + 0.25(-1/3))) = -67/64 = -1.046875$. The curve passes through all four
samples, which is a quick check of the coefficients.

11. The weights are $0.2, 0.3, 0.3, 0.2$ and sum to 1. The differences are $0.9273, 0.9653, 1.0304, 0.9273$ rad,
so the estimate is $0.9696$ rad per sample, or $0.1543$ cycles. The plain mean is $0.9626$: neighbouring differences
share one noisy sample, so their errors are correlated, and the parabolic weights are the best linear
combination for that noise.

12. The estimator takes $\arg\sum_{m=1}^{L} R(m)$, which equals $\pi\nu(L + 1)$ for a clean tone. With
$\nu(L + 1) = 1.08 > 1$ the angle wraps to $-0.92\pi$ and the estimate becomes $\nu - 2/(L + 1) = -0.1022$. It
stays right while $\nu(L + 1) < 1$, that is for $L \le 7$.

13. The key idea is that both gains are slopes of the S-curve at zero error, so the same loop design formula
applies once the slope is known. The numbers are $e = 0.4$, $A = 0.17157$, $K_D = 1.0780$ and $K_p = 0.03638$
for Gardner, and $K_D = 1.7804$ with $K_p = 0.02203$ for Mueller and Müller.

15. The correlations for $\mu = 0, \ldots, 5$ are $-0.4, 0.1, 2.9, -2.8, -0.3, 4.9$, and the metrics are
$-1.765, -1.172, 1.005, -6.189, -4.770, 0.948$. Correlation picks $\mu = 5$, Massey picks $\mu = 2$. The
window at $\mu = 5$ holds large samples, which random data around the word also produces; the
$\ln\cosh$ term subtracts what such data would score on its own.

17. $\xi = 0.089135$, and the bound is $1/(8\pi^2\cdot0.089135\cdot200\cdot15.849) = 4.48\times10^{-5}$, a
standard deviation of $0.0067T$. A loop averages over about $1/(2B_LT)$ symbols, so a block of 200 matches
$B_LT = 0.0025$.

19. For $z^2 + a_1z + a_0$ the Jury test asks $|a_0| < 1$, $1 + a_1 + a_0 > 0$ and $1 - a_1 + a_0 > 0$. These give
$0 < K_p < 2$, $K_i > 0$ and $2K_p + K_i < 4$. Both poles sit at $0$ when $K_p = K_i = 1$; then the error
transfer is $(z - 1)^2/z^2$, and the errors are $0.5$, $-0.4$, then $0$ from the third step on. The impulse
response of $\psi$ is $0, 2, -1$, so $B_LT = 2.5$: the loop passes far more noise than it removes.

20. The sum telescopes, so the estimator uses only the two end samples. Its variance is
$2\cdot\tfrac1{2\,\mathrm{SNR}}/(N - 1)^2$, and the ratio to the bound is $N(N + 1)/(6(N - 1))$, which is
$5.68$ for $N = 32$ and grows linearly with $N$.

21. The key idea is that a circular Gaussian vector has a direction uniform on the unit sphere of
$\mathbb{C}^L$, independent of its length, and $\rho$ depends only on that direction. Rotate so that $c$ is the
first basis vector; then $\rho = |g_1|^2/\sum_i|g_i|^2$ for independent exponential $|g_i|^2$, which is
Beta$(1, L - 1)$. For $L = 63$, $\lambda = 1 - 10^{-5/62} = 0.1695$.

22. A point at radius $r$ and angle $\phi$ fails when its rotated coordinate crosses the nearest boundary. For the
corner $(7, 7)$ the inner boundary $x = 6$ is reached when $7\sqrt2\cos(\pi/4 + \delta) = 6$, so
$\delta = \arccos(6/(7\sqrt2)) - \pi/4 = 0.1343$ rad, or $7.69°$. The next smallest tolerance is $0.1366$ rad, for
the eight neighbours of the corners, such as $(7, 5)$; the 16-QAM corner, by the same rule, gives $0.2945$ rad.
