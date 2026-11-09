1. ◦ Find the [eigenvalues](/eigenvalue/) and [eigenvectors](/eigenvector/) of $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ from the characteristic polynomial, and check each pair by multiplying.

2. ◦ Draw the [Gershgorin discs](/gershgorin-circle-theorem/) of $\begin{pmatrix} 4 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & -4 \end{pmatrix}$. How many eigenvalues lie in each disc, and why are they real?

3. ◦ Run three steps of [power iteration](/power-iteration/) on $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ from $x_0 = (1, 0)^T$, normalizing each iterate, and compute the [Rayleigh quotient](/rayleigh-quotient/) of each. At what rate does the vector converge, and at what rate does the eigenvalue estimate converge?

4. ◦ For the same matrix and $x = (1, 0.9)^T$, compute the Rayleigh quotient and its error. Compare the error with the angle $\theta$ between $x$ and the eigenvector $(1, 1)^T$.

5. ◦ With $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ and $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, compute the [similarity transformation](/similarity-transformation/) $S^{-1}AS$. What has it done to $A$, and what are the columns of $S$?

6. ◦ Show that $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ has only one independent eigenvector, so that no [diagonalization](/diagonalization/) exists. Then put $10^{-10}$ in position $(2, 1)$ and find the eigenvalues. How far have they moved?

7. ◦ Compute the singular values of $\begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$ from the eigenvalues of $A^TA$, and give $\|A\|_2$ and $\kappa_2(A)$.

8. ◦ A computer runs dense eigenvalue codes at $10^{10}$ flops per second. Using the counts of the [nonsymmetric](/nonsymmetric-eigenproblem/) and [symmetric](/symmetric-eigenproblem/) problems, estimate the time for $n = 2000$ to find all eigenvalues of a general matrix, a Schur form with Schur vectors, and all eigenvalues of a symmetric matrix.

9. • A symmetric matrix has eigenvalues $1$, $3$ and $4$. How many steps of power iteration reduce the eigenvector error by $10^{-12}$? Which eigenvector does [inverse iteration](/inverse-iteration/) with shift $\sigma = 2.9$ find, and how many steps does it need for the same reduction?

10. • Let $T$ be the tridiagonal matrix of order 4 with $2$ on the diagonal and $-1$ beside it. Compute the pivots of the $LDL^T$ factorization of $T - 1.5I$ and use the [Sturm count](/sturm-sequence-eigenvalue-count/) to say how many eigenvalues of $T$ are below $1.5$. Check against $2 - 2\cos(k\pi/5)$.

11. • The trailing $2 \times 2$ block of a symmetric tridiagonal matrix is $\begin{pmatrix} 2 & 0.5 \\ 0.5 & 3 \end{pmatrix}$. Compute the Rayleigh shift and the [Wilkinson shift](/wilkinson-shift/), and say which eigenvalue of the block the Wilkinson shift is.

12. • Reduce $A = \begin{pmatrix} 4 & 3 & 4 \\ 3 & 1 & 2 \\ 4 & 2 & 1 \end{pmatrix}$ to tridiagonal form with one Householder reflector, as in [tridiagonalization](/tridiagonalization/). Give the reflector vector and the tridiagonal matrix, and check that the trace is unchanged.

13. • Find the rotation of the [Jacobi algorithm](/jacobi-eigenvalue-algorithm/) that zeros the off-diagonal entries of $\begin{pmatrix} 3 & 2 \\ 2 & 0 \end{pmatrix}$: give $c$, $s$ and the resulting diagonal matrix.

14. • A two-state Markov chain has transition matrix $P = \begin{pmatrix} 0.9 & 0.1 \\ 0.5 & 0.5 \end{pmatrix}$, with rows summing to 1. Use the [Perron-Frobenius theorem](/perron-frobenius-theorem/) to justify a unique stationary distribution, find it, and give the rate at which power iteration on $P^T$ converges to it.

15. • The matrix $A = \begin{pmatrix} 1 & 10 \\ 0 & 2 \end{pmatrix}$ has eigenvector matrix $V = \begin{pmatrix} 1 & 10 \\ 0 & 1 \end{pmatrix}$. Compute $\kappa_2(V)$ and the [Bauer-Fike](/bauer-fike-theorem/) bound for a perturbation with $\|E\|_2 = 10^{-6}$. Compare with the first-order estimate from the [eigenvalue condition number](/eigenvalue-condition-number/).

16. • Run two steps of the [Lanczos algorithm](/lanczos-algorithm/) on $A = \operatorname{diag}(1, 2, 3, 4)$ with $q_1 = (1, 1, 1, 1)^T/2$. Give $\alpha_1$, $\beta_1$, $\alpha_2$ and the two Ritz values, and compare them with the extreme eigenvalues of $A$.

17. • Using the [singular value decomposition](/singular-value-decomposition/) of the matrix of exercise 7, find its best rank-one approximation and the 2-norm of the error.

18. • Write the [secular equation](/secular-equation/) for the eigenvalues of $\operatorname{diag}(1, 2) + zz^T$ with $z = (1, 1)^T$, and solve it. In which intervals does the theory place the two roots?

19. ★ For a real symmetric $2 \times 2$ matrix, let $\theta_k$ be the angle between the iterate $x_k$ of the [Rayleigh quotient iteration](/rayleigh-quotient-iteration/) and an eigenvector. Prove that $\tan\theta_{k+1} = -\tan^3\theta_k$. Check it on $\begin{pmatrix} 4 & 1 \\ 1 & 1 \end{pmatrix}$ from $x_0 = (1, 0)^T$.

20. ★ Let $H$ be an unreduced upper Hessenberg matrix and $\mu$ an exact eigenvalue. Show that one step of the [QR algorithm](/qr-algorithm/) with shift $\mu$ produces a matrix whose last row is $\mu e_n^T$, so that $\mu$ is [deflated](/deflation/) in one step. Check it on $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ with $\mu = 3$.

21. ★ Show that the tridiagonal matrix of order $n$ with $2$ on the diagonal and $-1$ beside it has eigenvalues $2 - 2\cos(k\pi/(n+1))$ with eigenvectors $(\sin(jk\pi/(n+1)))_{j=1}^n$. Then check the [Cauchy interlacing theorem](/cauchy-interlacing-theorem/) for $n = 3$ and $n = 4$.

22. ★ Let $A$ be real symmetric with eigenvalues $\lambda_1 \ge \dots \ge \lambda_n$, and let $\theta$ be the angle between $x$ and the eigenvector of $\lambda_1$. Prove that $0 \le \lambda_1 - \rho(x) \le (\lambda_1 - \lambda_n)\sin^2\theta$, and that equality holds for $n = 2$.
