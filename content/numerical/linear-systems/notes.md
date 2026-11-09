## History

Elimination is far older than the computer, and its story belongs to [Gaussian elimination](/gaussian-elimination/) in the volume on algebra. The numerical story starts with geodesy. Gauss described the iteration now named after him and Seidel in an 1823 letter to Gerling, as a way to solve the normal equations of survey data by hand; Seidel published it in 1874, and Jacobi had given his own iteration in 1845. André-Louis Cholesky, a French army officer, factored the symmetric systems of the same surveys. He died in 1918, and Benoit published the method under his name in 1924.

The first computers forced a closer look at rounding. Wilkinson's analysis of elimination in 1961 introduced the growth factor and the bound $2^{n-1}$ for partial pivoting, and his book *Rounding Errors in Algebraic Processes* (1963) taught the backward view of error that the chapter uses throughout. Householder (1958) and Givens (1958) brought orthogonal transformations into the subject, and Golub (1965) used Householder's reflections to solve least squares problems without forming the normal equations. Gram (1883) and Schmidt (1907) had given the orthogonalization that bears their names, for function spaces rather than for floating point.

Iterative methods grew with the size of the problems. Southwell relaxed residuals by hand in the 1940s, and David Young's 1950 thesis turned over-relaxation into SOR, with a formula for the best factor. Hestenes and Stiefel published conjugate gradients in 1952, at first as a direct method; Reid revived it in 1971 as an iteration for large sparse systems, and incomplete Cholesky preconditioning by Meijerink and van der Vorst (1977) made it standard. For nonsymmetric systems came MINRES by Paige and Saunders (1975), BiCG by Fletcher (1976), GMRES by Saad and Schultz (1986) and BiCGSTAB by van der Vorst (1992).

Sparse direct methods are a parallel line. Markowitz (1957) chose pivots to limit fill, Tinney and Walker (1967) brought minimum degree to power networks, Cuthill and McKee (1969) reduced bandwidth, and George reversed their order in 1971. George's nested dissection (1973) was shown optimal for grids by Hoffman, Martin and Rose in the same year, and Lipton and Tarjan's separator theorem (1979) carried it to every planar graph. Multigrid began with Fedorenko (1961) and Bakhvalov (1966) and became practical through Brandt's papers of 1973 and 1977; Ruge and Stüben made it algebraic in the 1980s.

## Further reading

- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, second edition, SIAM, 2002. The reference for rounding error analysis of every factorization in the chapter.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, fourth edition, Johns Hopkins University Press, 2013. The standard handbook of dense and structured algorithms.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, SIAM, 1997. Short lectures that are the best first reading on QR, least squares and Krylov methods.
- Yousef Saad, *Iterative Methods for Sparse Linear Systems*, second edition, SIAM, 2003. Krylov methods and preconditioners in depth.
- Timothy A. Davis, *Direct Methods for Sparse Linear Systems*, SIAM, 2006. Orderings, elimination trees and sparse factorization with working code.
