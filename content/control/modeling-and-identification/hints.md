1. The transform gives $sY - 1 + 2Y = 1/s$, so $Y(s) = (s + 1)/(s(s + 2)) = \frac{1/2}{s} + \frac{1/2}{s + 2}$. Then $y(t) = \tfrac12 + \tfrac12 e^{-2t}$, which tends to $\tfrac12$.

2. Poles $-1$ and $-3$, zero $2$, static gain $G(0) = -2/3$. Partial fractions of $G(s)/s$ give $y(t) = -\tfrac23 + \tfrac32 e^{-t} - \tfrac56 e^{-3t}$. The slope at $0^+$ is $\lim_{s \to \infty} sG(s) = 1$, so the output first rises and then settles at $-2/3$. The zero in the right half plane causes this wrong-way start; see [minimum phase](/minimum-phase/).

3. The equilibria are $0$ and $\pm 1$. The derivative $1 - 3x^2$ is $1$ at $0$, which is unstable, and $-2$ at $\pm 1$, which are locally asymptotically stable. For $\pm x^3$ the linearization at $0$ is $\dot x = 0$. The equilibrium is not hyperbolic, so the linearization decides nothing. In fact $\dot x = -x^3$ is asymptotically stable, though not exponentially, and $\dot x = x^3$ is unstable.

4. $A = -I + N$ with $N^2 = 0$, and $-I$ commutes with $N$, so $e^{At} = e^{-t}(I + tN) = e^{-t}\begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$. Then $x(t) = (te^{-t}, e^{-t})$. The first component peaks at $t = 1$ with the value $1/e \approx 0.368$.

5. $h_k = CA^{k-1}B = 0.5^{k-1}$: $1$, $0.5$, $0.25$, $0.125$. The Hankel matrix $\begin{pmatrix} 1 & 0.5 \\ 0.5 & 0.25 \end{pmatrix}$ has rank $1$. The mode $0.2$ is missing because $C$ does not see the second state, so it is unobservable. A minimal realization is $(0.5, 1, 1, 0)$.

6. $A_d = e^{-\ln 2} = 1/2$ and $B_d = 2(1 - e^{-\ln 2}) = 1$, so $x_{k+1} = x_k/2 + u_k$. The step response is $x_k = 2(1 - 2^{-k})$, which is $2(1 - e^{-t})$ at $t = k\ln 2$. Forward Euler gives $x_{k+1} = (1 - \ln 2)x_k + 2\ln 2\, u_k$, so its first step is $2\ln 2 \approx 1.386$ instead of $1$.

7. $r_u(0) = 1$ and $r_u(1) = -1$, so the matrix is $\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$. It is singular, so the input is persistently exciting of order $1$ only. Since $u(k-2) = -u(k-1)$, the output is $(b_1 - b_2)u(k-1)$, and only $b_1 - b_2$ is determined.

8. $K = (16 - 10)/2 = 3$. Then $T = 1.5(t_{63} - t_{28}) = 3$ and $L = t_{63} - T = 2$. The model is $G(s) = 3e^{-2s}/(3s + 1)$. As a check, an FOPDT response reaches $1 - e^{-1/3} \approx 28.3$ percent at $L + T/3 = 3$ and $1 - e^{-1}$ at $L + T = 5$.

12. The exponential of the block matrix gives $A_d = \begin{pmatrix} 1 & 1/2 \\ 0 & 1/2 \end{pmatrix}$ and $B_d = (\ln 2 - \tfrac12, \tfrac12)^T$. Then $H(z) = \dfrac{(\ln 2 - \frac12)z + \frac12(1 - \ln 2)}{(z - 1)(z - \frac12)}$, with poles $e^{0} = 1$ and $e^{-h} = 1/2$ and a zero at $-(1 - \ln 2)/(2\ln 2 - 1) \approx -0.7943$, which the continuous system does not have. The step response starts $0.1931$ and $0.6363$, the values of $t - 1 + e^{-t}$ at $t = \ln 2$ and $t = 2\ln 2$.

16. The regressors are $\varphi(k) = (-y(k-1), u(k-1))$ for $k = 1, \ldots, 4$. Then $R = \begin{pmatrix} 53/16 & 1/4 \\ 1/4 & 4 \end{pmatrix}$ and $f = (-11/8, 15/4)$, and $\det R = 211/16$. The estimate is $\hat a = -103/211 \approx -0.4882$ and $\hat b = 817/844 \approx 0.9680$. The residual sum of squares is $19/1688 \approx 0.0113$.

20. Since $y(k-1)$ depends on inputs up to $u(k-2)$ only, $\mathbb{E}\,y(k-1)u(k-1) = 0$, and the normal equations separate: $\hat b \to \mathbb{E}\,y(k)u(k-1) = 1$ and $\hat a \to -r_y(1)/r_y(0)$. Split $y$ into the input part, an AR(1) with $r(0) = 4/3$ and $r(1) = 2/3$, and the noise part $(1 + 0.5q^{-1})/(1 - 0.5q^{-1})\,e$, with $r(0) = 7/3$ and $r(1) = 5/3$. So $r_y(0) = 11/3$, $r_y(1) = 7/3$, and the limit is $(-7/11, 1)$: the pole is estimated as $0.636$ instead of $0.5$. The instruments are independent of $e(k) + 0.5e(k-1)$, and $\mathbb{E}\,\zeta\varphi^T = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ is nonsingular, so the IV limit is the true $(-0.5, 1)$. A simulation with $N = 100000$ and seeds 1 to 3 gave least squares estimates of $a$ between $-0.6365$ and $-0.6354$, and IV estimates between $-0.5027$ and $-0.5024$ (measurement).

21. The regressor is $(-y(k-1), u(k-1))$ with $u(k-1) = -c_1 y(k-1) - c_2 y(k-2)$. If $c_2 = 0$, the second component is a multiple of the first, the normal matrix is singular, and only $a + bc_1$ is determined. If $c_2 \ne 0$ and the closed loop is stable, $y(k-2)$ is not a linear function of $y(k-1)$, and the matrix is nonsingular. Substituting the control law gives $y(k) + (a + bc_1)y(k-1) + bc_2\, y(k-2) = e(k)$, here $y(k) - 0.3y(k-1) + 0.2y(k-2) = e(k)$, with poles of modulus $\sqrt{0.2} \approx 0.447$. Then $b = 0.2/c_2 = 1$ and $a = -0.3 - bc_1 = -0.8$.

22. Scalar DMD fits one number, $\lambda = \sum x_{k+1}x_k / \sum x_k^2 = 125233/175010 \approx 0.7156$ over the pairs $k = 0, 1, 2$; it is neither $0.8$ nor $0.5$. With $X = (z_0\ z_1)$ and $X' = (z_1\ z_2)$, the map $A = X'X^{-1} = \begin{pmatrix} 0 & 1 \\ -0.4 & 1.3 \end{pmatrix}$ has the characteristic polynomial $\mu^2 - 1.3\mu + 0.4$, whose roots are $0.8$ and $0.5$.

23. For $u \in \{-1, 1\}$, $u^2 = 1$, so $f(u) = u + \beta$, and by linearity the output is $Gu + \beta\, G\mathbf{1}$, where $G\mathbf{1}$ is the step response $1 - 0.5^k$ of $G$. The data reveal $\beta$ only through the offset $\beta G(1) = \beta$. If the model also allows an unknown constant offset, $\beta$ cannot be found at all. To see the curvature of $f$ the input needs at least three distinct levels.
