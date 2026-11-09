1. The characteristic polynomial is $\lambda^2 - 7\lambda + 10$, so $\lambda = 5$ with $(1, 1)^T$ and $\lambda = 2$ with $(1, -2)^T$.

3. The iterates are proportional to $(2, 1)$, $(5, 4)$ and $(14, 13)$, with Rayleigh quotients $2.8$, $2.9756$ and $2.9973$. The vector error shrinks by $1/3$ per step and the eigenvalue error by $1/9$, because the matrix is symmetric.

5. $S^{-1}AS = \operatorname{diag}(1, 3)$: the columns of $S$ are eigenvectors of $A$.

7. $A^TA = \begin{pmatrix} 25 & 20 \\ 20 & 25 \end{pmatrix}$ has eigenvalues $45$ and $5$, so $\sigma_1 = 3\sqrt 5 \approx 6.708$, $\sigma_2 = \sqrt 5$, and $\kappa_2(A) = 3$.

8. About 8 seconds, 20 seconds and 1 second.

9. Power iteration converges at rate $3/4$ and needs 97 steps. Inverse iteration finds the eigenvector of $3$ at rate $0.1/1.1 = 1/11$ and needs 12 steps.

10. The pivots are $0.5$, $-1.5$, $7/6$ and $-5/14$. Two are negative, and indeed $0.382$ and $1.382$ are the eigenvalues below $1.5$.

12. The vector is $v = (8, 4)^T$ in the last two coordinates, and the result has diagonal $4, 73/25, -23/25$, subdiagonal $-5, 14/25$.

14. $P$ is positive, so $1$ is a simple eigenvalue with a positive left eigenvector. The stationary distribution is $(5/6, 1/6)$, and the other eigenvalue $0.4$ sets the rate.

16. $\alpha_1 = \alpha_2 = 5/2$ and $\beta_1 = \sqrt 5/2$, so the Ritz values are $5/2 \pm \sqrt 5/2$, that is $1.382$ and $3.618$.

18. The equation is $1 + 1/(1 - \lambda) + 1/(2 - \lambda) = 0$. One root lies in $(1, 2)$ and one in $(2, 2 + \|z\|^2) = (2, 4)$.

19. Write $x_k = \cos\theta_k v_1 + \sin\theta_k v_2$. The Rayleigh quotient is $\lambda_1\cos^2\theta_k + \lambda_2\sin^2\theta_k$, and $(A - \rho I)^{-1}$ multiplies the two components by $1/((\lambda_1 - \lambda_2)\sin^2\theta_k)$ and $-1/((\lambda_1 - \lambda_2)\cos^2\theta_k)$.

20. Since $H - \mu I$ is singular and its first $n - 1$ columns are independent, $r_{nn} = 0$. So the last row of $RQ$ is zero.

21. Use $\sin((j-1)\phi) + \sin((j+1)\phi) = 2\cos\phi\sin(j\phi)$ with $\phi = k\pi/(n+1)$; the boundary rows work because $\sin 0 = \sin((n+1)\phi) = 0$.

22. Expand $x$ in the orthonormal eigenvectors, $x = \sum c_i v_i$ with $\|x\| = 1$, and write $\lambda_1 - \rho(x) = \sum_{i \ge 2}(\lambda_1 - \lambda_i)c_i^2$ with $\sum_{i \ge 2} c_i^2 = \sin^2\theta$.
