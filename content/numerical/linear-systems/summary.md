## What to remember

- Never form $A^{-1}$ to solve $Ax = b$. Factor $A$ once, in $O(n^3)$ operations, and solve each right-hand side with two triangular solves in $O(n^2)$.
- Gaussian elimination with [partial pivoting](/partial-pivoting/) computes the exact factors of $A + \Delta A$ with $|\Delta A| \lesssim \gamma_n |\hat L||\hat U|$. The [growth factor](/growth-factor/) can reach $2^{n-1}$, but in practice it stays small, and the method is backward stable for all but contrived matrices.
- The relative forward error is about the [condition number](/condition-number/) $\kappa(A)$ times the backward error. A small [residual](/residual/) proves a small backward error, not a small error: with $\kappa(A) = 10^{12}$, expect about four correct digits in binary64.
- A symmetric positive definite matrix needs no pivoting. [Cholesky](/cholesky-decomposition/) factors it in $n^3/3$ flops, half the cost of LU.
- For least squares, the [normal equations](/normal-equations/) square the condition number. [Householder QR](/qr-decomposition/) is backward stable at about twice the cost when $m \gg n$, and the SVD handles rank deficiency.
- Sparse direct solvers live or die by the ordering. On a $k \times k$ grid, [nested dissection](/nested-dissection/) gives $O(n \log n)$ fill and $O(n^{3/2})$ work for $n = k^2$ unknowns, and both orders are optimal.
- A stationary iteration $x_{k+1} = M^{-1}(Nx_k + b)$ converges for every start exactly when the [spectral radius](/spectral-radius/) of $M^{-1}N$ is below 1, and each digit costs about $-1/\log_{10}\rho$ sweeps.
- [Conjugate gradients](/conjugate-gradient-method/) reduce the $A$-norm error by $\varepsilon$ in at most $\lceil \frac12\sqrt\kappa \ln(2/\varepsilon) \rceil$ steps, so [preconditioning](/preconditioning/) pays when it lowers $\kappa$. [Multigrid](/multigrid-method/) solves model elliptic problems in $O(n)$ work.

## Costs side by side

| Method | Matrix | Cost | Notes |
|---|---|---|---|
| [Back substitution](/back-substitution/) | triangular | $n^2$ flops | backward stable |
| [LUP](/lup-decomposition/) | general | $2n^3/3$ flops | then $2n^2$ per right-hand side |
| [Cholesky](/cholesky-decomposition/) | SPD | $n^3/3$ flops | no pivoting |
| [Thomas algorithm](/thomas-algorithm/) | tridiagonal | $8n - 7$ flops | stable if diagonally dominant |
| [Levinson-Durbin](/levinson-durbin-recursion/) | SPD Toeplitz | $4n^2 - 3n - 2$ flops | |
| [Normal equations](/normal-equations/) | $m \times n$ | $mn^2 + n^3/3$ flops | error $\propto \kappa_2(A)^2$ |
| [Householder QR](/qr-decomposition/) | $m \times n$ | $2mn^2 - 2n^3/3$ flops | backward stable |
| [Jacobi](/jacobi-method/), [Gauss-Seidel](/gauss-seidel-method/) | sparse | $O(z)$ per sweep | sweeps $\approx \ln(1/\varepsilon)/\ln(1/\rho)$ |
| [Conjugate gradients](/conjugate-gradient-method/) | sparse SPD | $O(z + n)$ per step | $\lceil \tfrac12\sqrt\kappa\ln(2/\varepsilon)\rceil$ steps |
| [GMRES](/gmres/) | sparse general | $O(z + kn)$ at step $k$ | $\Theta(kn)$ memory; restarted in practice |

: Costs for an $n \times n$ system, or an $m \times n$ least squares problem, with $z$ nonzeros in a sparse matrix. A flop is one floating-point addition or multiplication; the counts are those of the entries.

## Choosing a method

- Dense and $n$ up to a few thousand: LUP with partial pivoting, or Cholesky if the matrix is symmetric positive definite. Ask the library for a condition estimate and check it.
- Several right-hand sides: factor once and reuse the factors. A rank-$k$ change in $A$: update the solution with the [Woodbury identity](/woodbury-identity/) instead of refactoring.
- Least squares: Householder QR; the normal equations only when $A$ is well conditioned and $m \gg n$; the SVD or a [rank-revealing factorization](/rank-revealing-factorization/) when $A$ may be rank deficient; [Tikhonov regularization](/tikhonov-regularization/) when the problem is ill posed.
- Banded or tridiagonal: the band solver or the Thomas algorithm, in linear time.
- Sparse and of moderate size: a sparse direct solver with a fill-reducing ordering, such as [minimum degree](/minimum-degree-ordering/) or nested dissection.
- Sparse and very large: conjugate gradients with an [incomplete Cholesky](/incomplete-cholesky-factorization/) or multigrid preconditioner when $A$ is SPD, [MINRES](/minres/) when it is symmetric indefinite, and GMRES or [BiCGSTAB](/bicgstab/) with an [incomplete LU](/incomplete-lu-factorization/) preconditioner otherwise.
- An answer needed to more digits than the conditioning allows: [iterative refinement](/iterative-refinement/) with residuals computed in higher precision.
