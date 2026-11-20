1. $\mathbb{E}[Q] = e^{0.125} \approx 1.1331$, $\mathrm{Var}(Q) = e^{0.25}(e^{0.25} - 1) \approx 0.3647$, so $N \approx 0.3647/10^{-4} \approx 3650$. $P(Q > 2) = \Phi(-\ln 2/0.5) = \Phi(-1.386) \approx 0.0828$, and a 10 % relative error needs $(1-p)/(0.01\,p) \approx 1110$ samples.

3. With $R = 10 + u_1$ and $S = 6 + 1.5u_2$, $G = 4 + u_1 - 1.5u_2$, so $\beta = 4/\sqrt{3.25} \approx 2.2188$ and $P_f = \Phi(-\beta) \approx 0.01325$. The design point is $u^* = -\frac{4}{3.25}(1, -1.5) \approx (-1.231, 1.846)$, where $R = S \approx 8.77$. $G$ is linear in $u$, so the set $G \le 0$ is a half-space and its probability is exactly $\Phi(-\beta)$.

4. $f_0 = \frac52$, $f_1 = 4x_1 - 2$, $f_2 = 3x_2 - \frac32$ and $f_{12} = 4(x_1 - \frac12)(x_2 - \frac12)$, with variances $\frac43$, $\frac34$ and $\frac19$; the total is $\frac{79}{36}$. So $S_1 = \frac{48}{79}$, $S_2 = \frac{27}{79}$, $S_{12} = \frac{4}{79}$, $S_{T1} = \frac{52}{79}$ and $S_{T2} = \frac{31}{79}$.

6. $\xi^4 = He_4 + 6He_2 + 3$, so $c_0 = 3$, $c_2 = 6$, $c_4 = 1$. The rule is exact up to degree 5. It gives $c_0 = 2 \cdot \frac16 \cdot 9 = 3$, which is right. For $c_2$ it needs $\mathbb{E}[\xi^6] - \mathbb{E}[\xi^4]$; the rule gives $\mathbb{E}[\xi^6] \approx 2 \cdot \frac16 \cdot 27 = 9$ instead of 15, so $c_2 = \frac12(9 - 3) = 3$, which is wrong. The integrand $\xi^4He_2$ has degree 6, above the exactness of the rule: this is aliasing.

8. The first index is 2, where $|u_1|$ is largest. Then $c = u_2(2)/u_1(2) = -\frac12$, the residual is $u_2 + \frac12u_1 = (\frac12, 0, 3, \frac32)$, and the second index is 3. Solving $\begin{pmatrix} -2 & 1 \\ 0 & 3 \end{pmatrix}c = (1, 1)$ gives $c = (-\frac13, \frac13)$ and $\hat f = (-\frac13, 1, 1, 0)$, which matches $f$ at the indices 2 and 3.

10. (a) $N(d+2) = 10\,000$ runs, or $N(2d+2) = 18\,000$ with second order indices. (b) $\binom{11}{3} = 165$ terms and 330 to 495 runs. (c) $2M\omega_{\max} + 1 = 233$. (d) Nine levels, since $0.1^9 \le 2 \times 10^{-9} < 0.1^8$, and $N + 8(1 - p_0)N = 16\,400$ evaluations.

13. $\sum_k\sqrt{V_kC_k} = \sum_{k=0}^5 2^{-k/2} \approx 2.987$, so $N_l = 59\,749$, 21 125, 7469, 2641, 934 and 331. The cost is about $1.79 \times 10^5$, against $2 \times 10^4 \cdot 32 = 6.4 \times 10^5$ for plain Monte Carlo on level 5.

14. $r_2 = \sqrt{w_1\rho_2^2/(w_2(1 - \rho_2^2))} \approx 30.42$, $m_1 = \lfloor 100/(1 + 0.3042) \rfloor = 76$, $m_2 = \lfloor 76 \cdot 30.42 \rfloor = 2312$ and $\alpha_2 = \rho_2\sigma_1/\sigma_2 \approx 0.792$. The variance ratio is $(\sqrt{1 - \rho_2^2} + \sqrt{w_2\rho_2^2})^2 \approx 0.166$, about six times smaller.

16. $c = (\frac73, \frac32)$, the diagonal entries $h_{ii}$ of the hat matrix are $\frac56$, $\frac13$, $\frac56$, and the residuals $\frac16$, $-\frac13$, $\frac16$. Dividing by $1 - h_{ii}$ gives the leave-one-out residuals $1$, $-\frac12$, $1$ and the mean square error $\frac34$. Without the first run the line is $2 + 2\xi$, which predicts 0 at $\xi = -1$, a residual of 1.

19. $\mu_1 = 2$ (largest value 3), $x_1 = 1$ and $q_1 = (0, \frac13, 1)$. For $\mu = 1$ the residual is $(0, \frac{1}{12}, 0)$, so $\mu_2 = 1$, $x_2 = \frac12$ and $q_2 = (0, 1, 0)$. For $\mu = 3$, $I_1g$ errs by $\frac{1}{12}$ at $x = \frac12$, and $I_2g$ is exact on the grid, since all the functions lie in a two-dimensional space there.

23. Use a Lagrange multiplier: $C_l = \mu V_l/N_l^2$, so $N_l \propto \sqrt{V_l/C_l}$, and the constraint fixes the constant. With $V_l \le c_22^{-\beta l}$ and $C_l \le c_32^{\gamma l}$, $\sum_l\sqrt{V_lC_l}$ is bounded by a geometric series when $\beta > \gamma$, independent of the finest level. The ceilings add at most $\sum_lC_l = O(\varepsilon^{-\gamma/\alpha})$, and $\alpha \ge \frac12\min(\beta, \gamma) = \frac\gamma2$ makes this $O(\varepsilon^{-2})$.

24. Write $D_u = \mathrm{Var}(f_u)$. Then $S_i = D_{\{i\}}/D$ and $S_{Ti} = \sum_{u \ni i}D_u/D$. Every $D_u$ is counted once in $\sum_u D_u = D$, at most once in $\sum_iS_i$, and $|u|$ times in $\sum_iS_{Ti}$. Both sums equal 1 exactly when $f$ has no interaction terms, that is, when $f$ is additive.

25. Condition on $\xi_{\sim i}$: the two outputs then share every input except $\xi_i$, which is drawn independently for each, so they are independent with the same conditional law and $\mathbb{E}[(Y - Y')^2 \mid \xi_{\sim i}] = 2\mathrm{Var}(Q \mid \xi_{\sim i})$. The ratio is not unbiased: the denominator is an estimate too, and the bias is $O(1/N)$.

26. The weight is $w(u) = e^{-\beta u_1 + \beta^2/2}$. Then $\mathbb{E}_q[\mathbf{1}w^2] = \int_\beta^\infty\phi(u)w(u)\,du$, and $\phi(u)e^{-\beta u} = \phi(u + \beta)e^{\beta^2/2}$. For $\beta = 3$, $p = 1.350 \times 10^{-3}$, the second moment is $8.00 \times 10^{-6}$, the relative variance is 3.39, and about 340 samples give 10 %, against about 74 000 for plain Monte Carlo.

27. The posterior is $N\bigl(y/(1 + \gamma^2), \gamma^2/(1 + \gamma^2)\bigr)$. For two normals with the same variance $s^2$, $d_H^2 = 1 - e^{-(m - m')^2/(8s^2)} \le (m - m')^2/(8s^2)$. For $\gamma = 1$ and $|y - y'| = 0.2$, $d_H \approx 0.04997$ and $L|y - y'| = 0.05$.
