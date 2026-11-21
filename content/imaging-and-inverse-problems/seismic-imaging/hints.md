1. The impedances are $4.2$, $5.75$ and $4.95 \times 10^6$ kg/(m²s). The coefficients are $1.55/9.95 = 0.156$ at $t = 2 \cdot 300/2000 = 0.3$ s and $-0.80/10.70 = -0.075$ at $t = 0.3 + 2 \cdot 500/2500 = 0.7$ s.

2. $t = \sqrt{0.64 + 0.36} = 1.0$ s, so the correction is $0.2$ s. The stretch factor is $t/t_0 = 1.25$, and the 40 Hz wavelet becomes 32 Hz.

5. $v^2 = (2600^2 \cdot 1.4 - 2200^2 \cdot 0.8)/0.6 = 9.32 \times 10^6$, so $v = 3053$ m/s.

6. $\tan\alpha_s = \sin 40° = 0.643$, so the event appears at $32.7°$. Migration has to steepen it back to 40°.

8. The values $T_i - D_i/v$ are $0.5$, $0.6$ and $0.45$ s, with mean $t_0 = 0.517$ s. The residuals are $-0.017$, $+0.083$ and $-0.067$ s; they add to zero, as they must for the best $t_0$.

10. $t_0 = 0.5 + 0.2 = 0.7$ s and $V^2 = (2000^2 \cdot 0.5 + 3000^2 \cdot 0.2)/0.7$, so $V = 2329.9$ m/s. The hyperbola gives $0.8211$ s at 1000 m and $1.1076$ s at 2000 m. Tracing rays with a common ray parameter $p$ (solve for $p$ by bisection) gives $0.8193$ s and $1.0872$ s. The hyperbola is late by $1.8$ ms and $20.4$ ms, because the fourth-order term of the exact moveout is negative.

12. $r_0 = 1.36$ and $r_1 = 0.6$, so the coefficient is $r_1/r_0 = 0.441$. The prediction error filter $(1, -0.441)$ turns $w$ into $(1, 0.159, -0.265)$. The perfect filter is the inverse $(1, -0.6, 0.36, -0.216, \ldots)$, which decays because $w$ is minimum phase.

13. Both give $(1 + 0.0625)/1.25^2 = 0.68$. The norm does not change under time reversal or sign change, so it cannot tell a minimum-phase wavelet from its maximum-phase mirror; a spike gives $1$.

16. At 30°, $(1 - 0.125)/0.866 - 1 = 0.0104$. The error reaches 1% at $29.7°$, found by bisection.

20. The arrival time at velocity $v$ is $2000/v$ s. The half-period rule allows $|2000/v - 0.8| < 1/16$ s, so $2319 < v < 2712$ m/s. The Ricker basin $0.4315/8 = 0.0539$ s gives $2342 < v < 2681$ m/s, slightly narrower.

22. Forward substitution gives $u = (1, 1, 0.5)$ and $J = 0.125$. The adjoint system $A^{\mathsf T}\lambda = (0, 0, u_3)$ is solved backward: $\lambda_3 = 0.25$, $\lambda_2 = 0.25$, $\lambda_1 = 0.25$. Since $\partial(Au)/\partial m_i = u_i e_i$, the gradient is $g_i = -\lambda_i u_i = (-0.25, -0.25, -0.125)$. In closed form $J = 1/(2(m_1m_2m_3)^2)$, and $\partial J/\partial m_i = -2J/m_i$ gives the same vector. One forward and one adjoint solve serve all three parameters.

23. All four ray times are $100(0.4 + 0.5) = 90$ ms. The checkerboard $(1, -1, -1, 1)$ is in the null space, so the minimum-norm model is the uniform $0.45$ ms/m, or 2222 m/s. The diagonal ray takes $100\sqrt2 \cdot 0.8 = 113.1$ ms, so $s_{11} + s_{22} = 0.8$. Writing the model as $0.45 + c(1, -1, -1, 1)$ gives $0.9 + 2c = 0.8$, so $c = -0.05$ and the true model.

24. With $a = -1$, the iteration gives $P_0^{(k)} = P + P^2 + \cdots + P^{k+1}$, while the primary is $P/(1 - P) = rz$ in units of $\tau$. The error after $k$ steps is $-(rz)^{k+2}/(1 + rz)^{k+1}$. After two steps the output is $0.5, 0, 0, -0.0625, 0.09375, -0.09375$ at $\tau$ to $6\tau$. The first two multiples are gone; later orders remain.

25. The arrival times are $1$, $1.6125$ and $1.3416$ s. Each row of the Jacobian is the unit vector from the station to the source divided by $v$, followed by $1$. The errors after three steps are $0.145$, $5.0 \times 10^{-4}$ and $1.8 \times 10^{-8}$ km. The ratios $e_{k+1}/e_k^2$ stay near $0.02$ to $0.07$, which is quadratic convergence; the three data fit the three unknowns exactly.

26. $L^{\mathsf T}d = (2, 3)$, against the model $(1, 1)$. The first CGLS step goes along $s_0 = (2, 3)$ with $\alpha = 13/34$, giving $(13/17, 39/34) = (0.765, 1.147)$ with a residual norm of $0.171$. The second step gives $(1, 1)$ exactly, as CGLS must for a $2 \times 2$ system.
