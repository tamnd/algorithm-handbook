## What to remember

- Eigenvalues are computed from the matrix, by [similarity transformations](/similarity-transformation/), and never from the coefficients of the characteristic polynomial. For order 5 and up every method is an iteration.
- Unitary similarities are backward stable: a library returns the exact eigenvalues of $A + E$ with $\|E\|_2$ a modest multiple of $u\|A\|_2$. A simple eigenvalue moves by about $\kappa(\lambda)\|E\|$ with $\kappa(\lambda) = 1/|y^*x|$ for unit left and right eigenvectors; for a symmetric matrix $\kappa = 1$, and [Weyl's inequality](/weyls-inequality/) says no eigenvalue moves by more than $\|E\|_2$.
- Nonnormal matrices can have very sensitive eigenvalues. The $10 \times 10$ Jordan block with eigenvalue $0$, changed by $10^{-10}$ in one corner, has all ten eigenvalues on the circle of radius $0.1$. [Pseudospectra](/pseudospectrum/) show it.
- [Power iteration](/power-iteration/) converges at the rate $|\lambda_2/\lambda_1|$; [inverse iteration](/inverse-iteration/) with shift $\sigma$ converges at the ratio of the distances from $\sigma$ to the nearest and next nearest eigenvalues; the [Rayleigh quotient iteration](/rayleigh-quotient-iteration/) changes the shift every step and converges cubically for symmetric matrices.
- The dense method has two phases: a direct reduction to [Hessenberg](/hessenberg-reduction/) or [tridiagonal](/tridiagonalization/) form, then an iteration on the reduced matrix, with steps of $O(n^2)$ or $O(n)$ flops. Shifts and [deflation](/deflation/) make the [QR algorithm](/qr-algorithm/) find the eigenvalues one or two at a time from the bottom.
- For a symmetric matrix the [Rayleigh quotient](/rayleigh-quotient/) of an approximate eigenvector with error $\epsilon$ has error of order $\epsilon^2$. Eigenvectors are less stable than eigenvalues: by the [Davis-Kahan theorem](/davis-kahan-theorem/) the angle turns by about $\|E\|$ divided by the gap to the rest of the spectrum.
- The [SVD](/singular-value-decomposition/) is computed without forming $A^TA$, which would lose the small singular values. The [Golub-Kahan algorithm](/golub-kahan-svd-algorithm/) reduces to bidiagonal form and iterates on it.
- For large sparse matrices, [Krylov](/krylov-subspace/) methods project onto a small subspace and solve the projected problem. The [Lanczos algorithm](/lanczos-algorithm/) finds extreme eigenvalues of a symmetric matrix with a three-term recurrence, and its vectors lose orthogonality exactly as Ritz values converge.

## Methods side by side

| Method | Finds | Cost | Convergence |
|---|---|---|---|
| [Power iteration](/power-iteration/) | dominant eigenpair | one product with $A$ per step | linear, rate $\lvert\lambda_2/\lambda_1\rvert$ |
| [Inverse iteration](/inverse-iteration/) | eigenpair nearest $\sigma$ | one factorization, then a solve per step | linear, ratio of distances to $\sigma$ |
| [Rayleigh quotient iteration](/rayleigh-quotient-iteration/) | an eigenpair near the start | a factorization per step | cubic if symmetric, else quadratic |
| [Subspace iteration](/subspace-iteration/) | $p$ dominant eigenpairs | $p$ products and $O(np^2)$ per step | linear, rate $\lvert\lambda_{p+1}/\lambda_p\rvert$ |
| Hessenberg and [Francis QR](/francis-double-shift-qr/) | all eigenvalues, general | about $10n^3$; $25n^3$ with Schur vectors | about two steps per eigenvalue in practice |
| Tridiagonalization and QR | all, symmetric | $4n^3/3$ for values; about $9n^3$ with vectors | cubic with the [Wilkinson shift](/wilkinson-shift/) |
| [Jacobi](/jacobi-eigenvalue-algorithm/) | all, symmetric | about $3n^3$ per sweep | quadratic in the last sweeps |
| [Bisection](/bisection-eigenvalue-algorithm/) with Sturm counts | chosen eigenvalues of a tridiagonal $T$ | $O(n)$ per halving | one bit per halving |
| [Divide and conquer](/divide-and-conquer-eigensolver/), [MRRR](/mrrr-algorithm/) | all, tridiagonal | about $O(n^2)$ to $O(n^{2.3})$ typical | direct, after the recursion |
| [Golub-Kahan SVD](/golub-kahan-svd-algorithm/) | singular values | $4mn^2 - 4n^3/3$ | cubic per singular value, typically |
| [Lanczos](/lanczos-algorithm/), [Arnoldi](/arnoldi-iteration/) | a few extreme eigenvalues | $k$ products and $O(kn)$ or $O(k^2n)$ | depends on the gaps |
| [QZ](/qz-algorithm/) | pencil $A - \lambda B$ | about $30n^3$ | as QR |

: Eigenvalue methods for an $n \times n$ matrix, or $m \times n$ with $m \ge n$ for the SVD. Flop counts are leading terms; $k$ is the number of Krylov steps.

## Choosing a method

For a dense matrix that fits in memory, call the library routine for its structure: the symmetric driver if $A$ is symmetric, the general driver otherwise, and an SVD routine for singular values. The symmetric driver is several times cheaper and returns orthonormal eigenvectors; within it, divide and conquer or MRRR are faster than QR when all eigenvectors are wanted, and bisection with inverse iteration is the choice when only a few are.

For a matrix too large to factor, use a restarted Krylov method: Lanczos for symmetric matrices, [implicitly restarted Arnoldi](/implicitly-restarted-arnoldi/) otherwise. Interior eigenvalues need a shift and a factorization. Power iteration is enough when one dominant eigenvalue is well separated, as for [PageRank](/pagerank/).

When the result matters, look at conditioning too. Report eigenvalue condition numbers for nonnormal matrices, check gaps before trusting individual eigenvectors, and plot a pseudospectrum when the matrix is far from normal. For $Ax = \lambda Bx$, reduce by Cholesky when $A$ is symmetric and $B$ is well-conditioned and positive definite, and use QZ in every other case.
