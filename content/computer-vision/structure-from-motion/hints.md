1. Two views have $4n$ measurements and $3n$ point unknowns plus the camera unknowns. Solve $4n \ge 3n + 5$ and $4n \ge 3n + 7$; this gives 5 and 7 points, the counts of the five-point and seven-point solvers.

2. There are $600 + 150000 = 150600$ unknowns. A dense factorization costs about $1.1 \times 10^{15}$ operations; the $600 \times 600$ matrix $S$ costs about $7.2 \times 10^7$ to factor.

3. Here $J = 2x$, so the step is $x_+ = x - (x^2 - 2)/(2x)$, which is Newton's method for $\sqrt 2$. The iterates are 1.5, 1.416667 and 1.414216.

4. The step is $h = -\frac{2}{2 + \mu}(1, 1)$. Its components are $-0.667$ for $\mu = 1$ and $-0.952$ for $\mu = 0.1$, and they tend to $-1$, the step of least norm among all Gauss-Newton steps.

7. Use [union-find](/disjoint-set/) on the matches. The component $\{A_1, B_1, C_2, A_3\}$ holds two features of image $A$, so at least one match in it is wrong.

8. With $J = (1, 2\lambda x + 1)$, expand the step to first order in $x$. For $|\lambda| < 1$ the error shrinks by a factor of about $|\lambda|$ per step, so convergence is only linear; for $\lambda = -2$ the iterates move away from 0 although $f''(0) = 6 > 0$. Gauss-Newton drops the term $r_2 \nabla^2 r_2$, which is large here because the residual at the solution is not small.

9. $b = (-1, -2)$ with $\|b\| = 2.236$; $g = (4, 2)$, $\alpha = 20/68$ and $a = (-1.176, -0.588)$ with $\|a\| = 1.315$. For $\Delta = 1$ scale $-g$ to length 1: $(-0.894, -0.447)$. For $\Delta = 2$ solve $\|a + \beta(b - a)\| = 2$, giving $\beta = 0.795$ and the step $(-1.036, -1.711)$. For $\Delta = 3$ take $b$.

11. The cycle error is $30 + 50 - 75 = 5$ degrees. The normal equations spread it evenly: $\theta_2 = 85/3$, $\theta_3 = 230/3$, and each residual is $-5/3$.

12. Take the edges by inlier count: $(3, 4)$, $(1, 2)$, $(2, 3)$; then $(1, 3)$ and $(2, 4)$ would close cycles. The angles are 0, 40, 65 and 55. The residuals are 3 for $(1, 3)$ and $-5$ for $(2, 4)$.

14. The log scale after 1000 steps has standard deviation $0.005\sqrt{1000} = 0.158$, so the band is $[e^{-1.96 \cdot 0.158}, e^{1.96 \cdot 0.158}] = [0.73, 1.36]$. A simulation with seed 2026 and 4000 runs put 94.7 percent of the runs inside.

15. Each column of the centred matrix is $M$ times a point, with $M$ of size $2F \times 3$. Counting asks for 2 frames, since $L$ has 6 unknowns, but with 2 frames the 6 equations have rank 5 and leave a one-parameter family.

16. All measured directions are $\pm$ the direction of the line, so any positions on the line in the same order fit them. With one camera off the line, the triangle of directions fixes its shape.

17. The gauge is a 3D similarity: 3 for rotation, 3 for translation and 1 for scale. Fixing the first pose removes 6; fixing the distance removes the scale. With only the first pose fixed, scaling all points and all other centres about the first centre leaves every residual unchanged, which gives a null vector of $J$.

18. The conjugate gradient iterate minimizes over a Krylov space, which contains the solution once a polynomial of degree $k$ vanishes at all $k$ eigenvalues. If no two cameras share a point, $S$ is block diagonal, the block Jacobi preconditioner is $S$ itself, and one iteration suffices.

19. The Jacobian in $y$ is $JB$, so the step in $y$ is $-(B^{\mathsf T} J^{\mathsf T} J B)^{-1} B^{\mathsf T} J^{\mathsf T} r = B^{-1} h_x$. The gradient in $y$ is $B^{\mathsf T} g$, and $B B^{\mathsf T} g$ is not a multiple of $g$ in general.

20. Write the normal equations in block form and eliminate the point unknowns with $V^{-1}$. This is block Gaussian elimination, so it changes the system but not its solution; see the [Schur complement](/schur-complement/).
