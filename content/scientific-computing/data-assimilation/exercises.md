1. ◦ A background value $x^b = 4$ has error variance 2, and an observation $y = 7$ of the same quantity has
error variance 1. Compute the gain, the analysis $x^a$ and the analysis error variance, as in
[the data assimilation problem](/data-assimilation-problem/).

2. ◦ A station sits at position 3.6 on a line of grid points $1, 2, 3, \ldots$, and the
[observation operator](/observation-operator/) interpolates linearly between neighbours. With $x_3 = 12$ and
$x_4 = 7$, give the row of $H$ and the value $Hx$. Then give the tangent linear row of the wind speed
$\sqrt{u^2 + v^2}$ at $(u, v) = (5, 12)$, and use it to predict the speed at $(5.1, 12.2)$.

3. ◦ Five grid values have the [background error covariance](/background-error-covariance/)
$B_{ij} = 2 \cdot (1/2)^{|i - j|}$. Value 3 is observed with error variance $r = 1$ and innovation $d = 3$.
Compute the analysis increment at all five points and the analysis error variance at point 3.

4. ◦ For the [Lorenz-96 model](/lorenz-96-model/) with $n = 5$ and the state $x = (1, 2, 3, 4, 5)$ (indices
$0$ to $4$, taken modulo 5), compute the quadratic part $N_j(x) = (x_{j+1} - x_{j-2})x_{j-1}$ for every $j$,
check that $\sum_j x_jN_j(x) = 0$, and give the tendency $dx/dt$ for $F = 8$.

5. ◦ The scalar model $\dot x = -x$ is [nudged](/nudging/) towards a constant observation $y = 4$ with gain
$g$. What is the smallest $g$ for which the equilibrium is within $0.1$ of $y$? With that gain, how small must
the time step of the classical Runge-Kutta method be for the nudged equation to be stable?

6. ◦ Evaluate the [Gaspari-Cohn function](/gaspari-cohn-function/) with half-width $c = 3$ at the distances
$r = 1$ and $r = 4$, as exact fractions. Beyond which distance is it zero?

7. ◦ Take the model $x_1 = 3x_0$, the background $x^b = 1$ with $B = 1$ and one observation $y_1 = 6$ of
$x_1$ with $R = 1$. Minimize the strong-constraint [4D-Var](/four-dimensional-variational-assimilation/)
cost by hand to find $x^a_0$ and $x^a_1$. Then run one forecast and one analysis step of the
[Kalman filter](/kalman-filter/) from $x^b$ and compare the mean and variance at time 1.

8. ◦ Two variables are independent, and their correlation is estimated from an ensemble of $N$ members. How
large must $N$ be for the standard deviation of the sample correlation to be at most $0.05$, using the mean
squared sample correlation $1/(N - 1)$ from [covariance localization](/covariance-localization/)?

9. ◦ Compute the variance $\tau^2$ of the log likelihood in the
[particle filter collapse](/particle-filter-weight-collapse/) theorem for (a) $B = H = R = I$ in 40
dimensions and (b) a single observation with $HBH^\top/R = 4$.

10. • An [ensemble square root filter](/ensemble-square-root-filter/) has the scalar members $1, 3, 5$ and
observes the value directly: $y = 4.5$ with $r = 1/2$. Compute the gain, the factor $\alpha$, the new
members, and check that their sample variance equals the Kalman value $(1 - K)s$.

11. • In Exercise 10, apply relaxation to prior perturbations (RTPP) and relaxation to prior spread (RTPS),
both with $\alpha = 1/2$, as defined in [covariance inflation](/covariance-inflation/). Show that the two
give the same members here, and explain why they always agree for a scalar state with a deterministic
filter.

12. • An ensemble of two members on three grid points has the perturbation $v = (1, 1, 1)$, so the sample
covariance is $vv^\top$. What is its rank? Localize it with the tridiagonal matrix $L$ that has 1 on the
diagonal and $1/2$ next to it. Give the eigenvalues of $L \circ vv^\top$ and its rank.

13. • On a ring of 6 points, the cut-off taper $\rho(d) = 1$ for ring distance $d \le 1$ and $0$ otherwise
gives a circulant matrix. Compute its eigenvalues and show that it is not a valid localization matrix.

14. • The model $x_k = x_{k-1} + h\,x_{k-1}(1 - x_{k-1})$ with $h = 1/2$ starts at $x_0 = 0.2$, and
$J = \tfrac12(x_2 - 0.5)^2$. Run the [adjoint model](/adjoint-model/) by hand to get $dJ/dx_0$, and check it
with a centred finite difference.

15. • Write the tangent linear model of the Lorenz-96 tendency $f(x)$ at a state $x$, as a function
$\delta x \mapsto f'(x)\delta x$, and its adjoint $\lambda \mapsto f'(x)^\top\lambda$ without forming the
matrix. Check them with the dot product test for $n = 40$ and random vectors.

16. • The rotation $\dot x_1 = x_2$, $\dot x_2 = -x_1$ is nudged with gain $g$ on $x_1$ only:
$\dot x_1 = x_2 + g(y - x_1)$. With exact observations of a true trajectory, find the eigenvalues of the
error equation as functions of $g$, and the gain that makes the slowest error decay fastest. What is that
rate?

17. • In [weak-constraint 4D-Var](/weak-constraint-4d-var/), take $x_1 = x_0 + \eta$ with $x^b = 0$, $B = 1$,
$Q = 2$ and one observation $y = 3$ of $x_1$ with $R = 1$. Solve it with the
[representer method](/representer-method/): give $P$, $\beta$, $x_0$, $\eta$ and $x_1$. Compare $x_1$ with
the strong-constraint answer.

18. • Do one step of [ensemble Kalman inversion](/ensemble-kalman-inversion/) in mode "none" with the
members $u = (0, 2)$, $G(u) = 2u$, $y = 3$, $\Gamma = 1$ and $h = 1$. Give $C^{ug}$, $C^{gg}$, the gain, the
new members, their mean and variance. Compare with the posterior for the prior $N(1, 2)$, and check the
size of the missing variance.

19. • In the scalar case of the [Desroziers diagnostics](/desroziers-diagnostics/), the true values are
$HBH^\top = 2$ and $R = 1$, but the system assumes $H\tilde BH^\top = 1$. Starting from $\tilde R_0 = 3$, the
update is $\tilde R_{j+1} = \tilde R_j S/(H\tilde BH^\top + \tilde R_j)$ with the true innovation variance
$S$. Compute $\tilde R_1$ and $\tilde R_2$, find the limit, and say where the error of $\tilde B$ has gone.

20. • A filter has the forecast spread $\mathrm{tr}(HP^fH^\top) = 2$ and $\mathrm{tr}\,R = 2$, and the mean
of $d^\top d$ over many cycles is 6. What multiplicative inflation does the innovation estimate of
[covariance inflation](/covariance-inflation/) give, and by what factor are the perturbations multiplied?

21. ★ Take a linear model $x_1 = Mx_0$ in $n$ dimensions with the background $x^b$, covariance $B$, and
observations $y = Hx_1 + \epsilon$ with $\epsilon \sim N(0, R)$ at time 1 only. Prove that $Mx^a_0$, where
$x^a_0$ minimizes the strong-constraint [4D-Var](/four-dimensional-variational-assimilation/) cost, is the
Kalman filter analysis at time 1 with $P^f = MBM^\top$, and that $M\,\mathrm{Cov}(x^a_0)\,M^\top$ is its
analysis covariance $(I - KH)P^f$. Do not assume that $M$ is invertible.

22. ★ Let $L$ be positive definite and $P$ positive semidefinite with all diagonal entries positive. Prove
that $L \circ P$ is positive definite. Conclude that localizing a sample covariance of rank $N - 1$ with a
positive definite $L$ gives a full rank covariance when no variable has zero spread.

23. ★ On the ring of 40 points, build the matrix of the Gaspari-Cohn function of the ring distance
$\min(|i - j|, 40 - |i - j|)$ with half-width $c$. It is circulant, so its eigenvalues are the discrete
Fourier transform of its first row. Find the smallest integer $c$ for which an eigenvalue is negative, and
show that the chordal distance $\tfrac{40}{\pi}\sin(\pi|i - j|/40)$ gives no negative eigenvalue for that $c$.

24. ★ The scalar state obeys $dx = -x\,dt + dw$ with $\mathrm{Var}(dw) = 3\,dt$, and is observed continuously
with noise of intensity $r = 1$. A nudged estimate uses $d\hat x = -\hat x\,dt + g(dy - \hat x\,dt)$. Find
the stationary error variance as a function of $g$, the gain that minimizes it, and show that this gain is
the steady gain of the [Kalman-Bucy filter](/kalman-bucy-filter/).

25. ★ Estimate the largest Lyapunov exponent of the Lorenz-96 model with $n = 40$, $F = 8$ and RK4 with
step $0.01$: run two nearby trajectories, measure their separation every $0.1$ time units, rescale it to a
fixed small size, and average the logarithms of the growth. Give the exponent and the error doubling time.
