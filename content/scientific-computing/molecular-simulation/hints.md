1. $\phi(1.5) = 4(1.5^{-12} - 1.5^{-6}) = -0.320337$. The force is $24(2r^{-13} - r^{-7}) = -1.158029$, and the negative sign means attraction. The minimum is at $2^{1/6} = 1.122462$, where the force vanishes.

3. Fixing the three components of the total momentum removes three degrees of freedom, so $N_f = 297$. The mean is $148.5\, k_B T$, the standard deviation $\sqrt{148.5} = 12.186$ in units of $k_B T$, and the relative fluctuation is $\sqrt{2/N_f} = 0.0821$.

5. $\lambda^2 = 1 + 0.1(2/3 - 1) = 0.966667$, so $\lambda = 0.983192$, and $K' = \lambda^2 K = 145$. In general $K' - K_0 = (1 - h/\tau)(K - K_0)$, so $K - K_0 = 50 \cdot 0.9^n$, which falls below 1 after 38 steps.

7. The mean of $e^{-0.5}$, $e^{-1.5}$ and $e^{0.2}$ is 0.683688, so $\beta\Delta A = 0.380254$. The mean of $\beta\Delta U$ is 0.6. The estimate is below it, as Jensen's inequality requires, and the single negative sample carries more than half the weight.

9. One step gives $x = 0.98$ and $v = -0.198$, so $H = 0.499802$ and $\tilde E = 0.495$, as at the start. Since $H = \tilde E + \frac{h^2}{8} x^2$ and $x^2 \le 2\tilde E/(1 - h^2/4)$, $H$ stays between $\tilde E$ and $\frac12$, and $|H - \frac12| \le h^2/8$. The bound is 0.005 at $h = 0.2$. $\tilde E$ is the exact shadow Hamiltonian of this linear problem, and it differs from $H$ by $O(h^2)$.

12. The variance obeys $s = (1 - c)^2 s + 2Dh$, so $s = 2Dh/(1 - (1 - c)^2)$. At $h = 0.005$, $c = 0.5$ and $s = 0.01/0.75 = 0.013333$, a third above the exact 0.01. The scheme is unstable for $|1 - c| \ge 1$, that is $h \ge 0.02$.

15. The unbiased free energy is $F(s) = -\ln P(s) - w(s)$ up to a constant. With $w(0.1) = 0.25$ and $w(0.2) = 1$, $F(0.1) - F(0) = \ln\frac43 - 0.25 = 0.037682$ and $F(0.2) - F(0) = \ln 4 - 1 = 0.386294$.

18. In the perfect lattice each atom has $\bar\rho = z$, so $E_c = \sqrt z$. Removing one atom takes away its $-\sqrt z$ and lowers the density of $z$ neighbours to $z - 1$. Count the change against the $N - 1$ atoms of the perfect lattice to find $E_v = z(\sqrt z - \sqrt{z - 1})$. A pair potential gives $E_v = E_c$.

20. On $(x, v)$ the half kick is the matrix $\begin{pmatrix} 1 & 0 \\ -\kappa h/2 & 1 \end{pmatrix}$, and the trace of $K R K$ equals that of $R K^2$. A linear map with determinant 1 is stable for $|\operatorname{tr}| < 2$. Near $\Omega h = \pi$ the cosine term is close to $-2$ and the sine term pushes the trace below $-2$ on $0.311049 < h < 0.314159$. The slow force is weak, yet the outer step cannot sit at half the fast period.

21. The left side increases with $C$ and the right side decreases, so there is one root. Bisection gives $C = 0.861043$. Forward perturbation gives $-\ln\frac{e^{-1} + e^{-2}}{2} = 1.379885$, and reverse perturbation gives $\ln\frac{e^{0.5} + 1}{2} = 0.280930$. The acceptance ratio lies between them.

22. With $W = \frac32 x^2$ and $x$ standard normal, $\langle e^{-aW} \rangle = (1 + 3a)^{-1/2}$. So the mean is $\frac12$ and the second moment $1/\sqrt7$, which gives the variance 0.127964. The standard error of $\Delta A$ is about $\sigma/(\frac12 \sqrt N)$, which needs $N \ge 5119$. In reverse, $x$ has variance $\frac14$ and the second moment is $\langle e^{3x^2} \rangle$, which is infinite since $2 \cdot 3 \cdot \frac14 \ge 1$.

23. With $\omega = 2\pi/11$ per fs, the periods are 10.847 fs at 1 fs, 10.335 fs at 2 fs and 9.159 fs at 3 fs. The method is unstable for $\omega h > 2$, that is $h > 11/\pi = 3.50$ fs.

24. The velocity at time $t$ equals the velocity at 0 if no collision has happened, with probability $e^{-\nu t}$. Otherwise it is independent of it with mean zero. Then $D = \frac13 \int_0^\infty \langle v(0) \cdot v(t) \rangle\, dt = k_B T/(m\nu) = 2$, and the mean squared displacement is $6D\,(t - (1 - e^{-\nu t})/\nu) = 96.16$ at $t = 10$.
