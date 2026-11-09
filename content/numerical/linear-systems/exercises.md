1. ◦ For $A = \begin{pmatrix} 1 & -2 \\ 3 & 4 \end{pmatrix}$, compute the [matrix norms](/matrix-norms/) $\|A\|_1$, $\|A\|_\infty$ and $\|A\|_F$. Which of them bounds $\|A\|_2$ from above, and is $\|A\|_2$ closer to $\|A\|_F$ or to $\sqrt{\|A\|_1\|A\|_\infty}$?

2. ◦ Solve $\begin{pmatrix} 2 & 1 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 4 \end{pmatrix} x = \begin{pmatrix} 3 \\ 13 \\ 8 \end{pmatrix}$ by [back substitution](/back-substitution/), and count the multiplications, divisions and additions it makes.

3. ◦ Which of $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$ and $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ is [positive definite](/positive-definite-matrix/)? For the one that is not, give a vector $x$ with $x^T A x < 0$.

4. ◦ For $n = 1000$, give the flop counts of the LUP decomposition, the Cholesky decomposition, one LUP-SOLVE, and the Thomas algorithm on a tridiagonal matrix of the same order.

5. ◦ Write down the [Hilbert matrix](/hilbert-matrix/) $H_3$ and compute its determinant exactly. What does the size of the determinant say, and not say, about conditioning?

6. ◦ Let $A = \begin{pmatrix} 1 & 1 \\ 1 & 1.0001 \end{pmatrix}$, $b = (2, 2.0001)^T$, with exact solution $x = (1, 1)^T$. For the guess $\hat x = (2, 0)^T$, compute the [residual](/residual/) and the error in the $\infty$-norm.

7. ◦ For $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, write the iteration matrices of the [Jacobi](/jacobi-method/) and [Gauss-Seidel](/gauss-seidel-method/) methods and give their spectral radii. How many sweeps of each reduce the error by about $10^{-6}$?

8. ◦ Use the [Neumann series](/neumann-series/) to compute $(I - B)^{-1}$ for $B = \begin{pmatrix} 0 & 1/2 \\ 1/2 & 0 \end{pmatrix}$, and compare $\|(I - B)^{-1}\|_\infty$ with the bound $1/(1 - \|B\|_\infty)$.

9. • Use the [Sherman-Morrison formula](/sherman-morrison-formula/) to invert $I + \mathbf{1}\mathbf{1}^T$, where $I$ is the $3 \times 3$ identity and $\mathbf{1}$ the vector of ones. Generalize to order $n$.

10. • Compute the [LUP decomposition](/lup-decomposition/) of $A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$ with partial pivoting. Give the row order, $L$ and $U$, and check that every multiplier has modulus at most 1.

11. • Run the [Thomas algorithm](/thomas-algorithm/) on the tridiagonal matrix with $2$ on the diagonal and $-1$ beside it, of order 4, with right side $(1, 0, 0, 1)^T$. Give the modified superdiagonal coefficients and the solution.

12. • Fit a line $y = c_0 + c_1 t$ to the points $(0, 1)$, $(1, 2)$, $(2, 2)$ by [least squares](/least-squares-problem/). Give $A^T A$, $A^T b$, the coefficients and the minimum value of $\|Ax - b\|_2^2$.

13. • For the model Poisson problem in one dimension with $h = 1/100$, the Jacobi iteration has spectral radius $\cos(\pi h)$. Estimate the number of sweeps that reduce the error by $10^{-6}$ for Jacobi, for Gauss-Seidel, and for [SOR](/successive-over-relaxation/) with $\omega = 2/(1 + \sin \pi h)$ and spectral radius $\omega - 1$.

14. • A symmetric positive definite system has $\kappa_2(A) = 10^4$. Use the bound for [conjugate gradients](/conjugate-gradient-method/) to find the number of steps that reduce the $A$-norm error by $10^{-6}$. What does a preconditioner that brings $\kappa$ down to $100$ save?

15. • Zero the second component of $x = (3, 4)^T$ in two ways: by a [Givens rotation](/givens-rotations/), giving $c$, $s$ and the result, and by a [Householder reflection](/householder-reflections/) with the sign chosen to avoid cancellation, giving $v$ and the result.

16. • For the $3 \times 3$ tridiagonal matrix with $2$ on the diagonal and $-1$ beside it, eliminate the first unknown and write down the [Schur complement](/schur-complement/). Check that it is again symmetric positive definite.

17. • Run the cyclic [Kaczmarz method](/kaczmarz-method/) on the equations $x = 0$ and $x + y = 0$ from $(1, 1)$. Give the iterates after each full sweep and the factor by which the distance to the solution shrinks per sweep. Relate the factor to the angle between the two lines.

18. • Solve the [Lyapunov equation](/lyapunov-equation/) $AX + XA^T = -I$ for $A = \begin{pmatrix} -1 & 1 \\ 0 & -2 \end{pmatrix}$, with $X$ symmetric. Is $X$ positive definite?

19. • An arrowhead matrix of order $n$ has nonzeros on the diagonal, in the first row and in the first column. Count the [fill-in](/fill-in/) when elimination takes the unknowns in the given order, and when it takes the first unknown last.

20. ★ Prove that the Cholesky factor of the tridiagonal matrix with $2$ on the diagonal and $-1$ beside it has $l_{kk} = \sqrt{(k+1)/k}$ and $l_{k+1,k} = -\sqrt{k/(k+1)}$.

21. ★ Run conjugate gradients from $x_0 = 0$ on $A = \operatorname{diag}(1, 1, 1, 4, 4, 4, 4)$ with $b = \mathbf{1}$. After how many steps is the residual zero in exact arithmetic? Explain the count with the [Krylov subspace](/krylov-subspace/) and a polynomial argument.

22. ★ Find the [pseudoinverse](/pseudoinverse/) of the rank-one matrix $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, and give a general formula for $(uv^T)^+$. What is the minimum-norm least squares solution of $Ax = (1, 0)^T$?

23. ★ Orthogonalize the columns of $\begin{pmatrix} 1 & 1 & 1 \\ \epsilon & 0 & 0 \\ 0 & \epsilon & 0 \\ 0 & 0 & \epsilon \end{pmatrix}$ with $\epsilon = 10^{-8}$ in binary64, by classical and by modified [Gram-Schmidt](/gram-schmidt-process/). Compute $q_2^T q_3$ for each, and explain the difference.

24. ★ The matrix $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ is consistently ordered. Use Young's formula to find the optimal SOR factor and the spectral radius at that factor, and compare with Gauss-Seidel.
