1. ◦ A data set in the plane has the sample [covariance matrix](/covariance-matrix/) $\begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$. Find its eigenvalues and the first principal direction. What fraction of the variance does the first [principal component](/principal-component-analysis/) keep, and what is the mean squared [reconstruction error](/reconstruction-error/) of the one-dimensional projection?

2. ◦ The correlation matrix of 8 standardized features has the eigenvalues 3.2, 2.0, 1.2, 0.6, 0.4, 0.3, 0.2 and 0.1. How many components does Kaiser's rule $\lambda_j > 1$ keep, and what fraction of the variance do they [explain](/explained-variance/)? What is the least $k$ whose components explain at least 90%?

3. ◦ A point is drawn uniformly from the unit ball in $\mathbb{R}^d$. What is the probability that it lies in the outer shell $0.99 \le \|x\| \le 1$, for $d = 10$, $100$ and $1000$? Relate the answer to the [curse of dimensionality](/curse-of-dimensionality/).

4. ◦ (a) In [SNE](/stochastic-neighbor-embedding/), the conditional distribution of one point over its neighbors is $(1/2, 1/4, 1/4, 0, \ldots, 0)$. What is its perplexity? (b) In [t-SNE](/t-sne/) with $n = 100$ points, $p_{j|i} = 0.3$ and $p_{i|j} = 0.1$. What is $p_{ij}$? (c) In [UMAP](/umap/), the directed weights are $w_{j|i} = 0.6$ and $w_{i|j} = 0.5$. What is the symmetric weight of the edge?

5. ◦ The encoder of a [variational autoencoder](/variational-autoencoder/) outputs $\mu = (1, 0)$ and $\sigma^2 = (1, 0.5)$ for one input. Compute the KL term $\mathrm{KL}(N(\mu, \operatorname{diag}\sigma^2) \,\|\, N(0, I))$ of the ELBO, exactly and to three decimals.

6. ◦ A [factor analysis](/factor-analysis/) model with $k$ factors for $d$ features leaves $((d-k)^2 - (d+k))/2$ degrees of freedom for testing it against the saturated model. Compute this number for $(d, k) = (5, 2)$, $(5, 3)$ and $(10, 3)$, and say what a negative value means.

7. ◦ Use the bound $k \ge 4\ln n/(\varepsilon^2/2 - \varepsilon^3/3)$ of the [Johnson-Lindenstrauss lemma](/johnson-lindenstrauss-lemma/) to find the least target dimension for $n = 10^4$ points with $\varepsilon = 0.25$, and with $\varepsilon = 0.1$. How does the answer change if the points have $d = 10^6$ coordinates instead of $d = 10^5$?

8. ◦ (a) [Randomized PCA](/randomized-pca/) with $k = 10$ and oversampling $p = 5$: what factor does the expected Frobenius error bound put on the optimal error? What is the least $p$ that brings the factor to 1.1 or below? (b) What is the weight $\lambda$ of the sparse term in [robust PCA](/robust-pca/) for a $1000 \times 400$ matrix?

9. ◦ Two classes have means $\mu_0 = (0, 0)$ and $\mu_1 = (2, 1)$ and the within-class scatter $S_W = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$. Find the direction of [linear discriminant analysis](/linear-discriminant-analysis/), and compare it with the direction of the mean difference.

10. ◦ Five points lie on the unit semicircle at the angles $0°, 45°, 90°, 135°$ and $180°$. [Isomap](/isomap/) joins two points when their distance is at most $\varepsilon$. Compute the graph distance between the two ends for $\varepsilon = 1$ and for $\varepsilon = 1.5$, and compare both with the arc length and the straight-line distance.

11. • The sample covariance of data in $\mathbb{R}^4$ has the eigenvalues 10, 4, 1, 1 with eigenvectors $u_1, \ldots, u_4$. Find the maximum likelihood $\sigma^2$ and $W$ of [probabilistic PCA](/probabilistic-pca/) for $q = 1$ and for $q = 2$, and the eigenvalues of the fitted covariance $WW^\top + \sigma^2 I$ in each case. How many free parameters does each model have besides the mean, against a full covariance?

12. • A one-factor model for three standardized features has $S_{12} = 0.48$, $S_{13} = 0.40$ and $S_{23} = 0.30$. Find the loadings and the unique variances of the exact fit. Then do the same for $S_{12} = 0.8$, $S_{13} = 0.9$, $S_{23} = 0.6$, and say what goes wrong.

13. • Four objects have the graph distances of a 4-cycle: 1 between neighbors on the cycle and 2 between opposite objects. Compute $B = -\tfrac12 J D^{(2)} J$ and its eigenvalues. Are the distances Euclidean? What does [classical MDS](/classical-mds/) in two dimensions return, and which distances does it get wrong?

14. • Three objects have all dissimilarities equal to 2. Start [SMACOF](/smacof/) in one dimension from the positions $0, 1, 3$. Center them, form $B(X)$, and apply one Guttman transform. Compute the raw stress before and after the step, and show that the new configuration is the best one in one dimension with this order of the points.

15. • The path graph on three vertices has unit edge weights. Solve $Ly = \lambda Dy$ and give the one-dimensional [Laplacian eigenmap](/laplacian-eigenmaps/) with $y^\top D y = 1$, and the value of the objective.

16. • (a) A point has its four nearest-neighbor distances $1, \sqrt2, \sqrt3, 2$. Compute the local [Levina-Bickel estimate](/intrinsic-dimension-estimation/) with $k = 4$, and its unbiased form $(k-2)/S$. (b) For the points $0, 2, 3, 7, 8, 12$ on a line, compute every TwoNN ratio $\mu_i = T_2/T_1$ and the estimate $(n-1)/\sum_i \ln \mu_i$.

17. • Six points on a line are at $0, 1, 3, 7, 15, 31$. A map sends them to $0, 1, 3, 7, 15, 10$: only the last point moves. Compute [trustworthiness](/trustworthiness-and-continuity/) $T(2)$ and continuity $C(2)$.

18. • Two independent sources are uniform with mean 0 and variance 1, so each has excess kurtosis $-1.2$. Compute the kurtosis of the whitened mixture $0.6 s_1 + 0.8 s_2$. Why does [ICA](/independent-component-analysis/) look for directions of extreme kurtosis, and why can it not separate two Gaussian sources?

19. • Apply one round of the multiplicative updates of [NMF](/nonnegative-matrix-factorization/) with rank 1 to $V = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, starting from $W = (1, 1)^\top$ and $H = (1, 1)$: first $H$, then $W$. Give the squared error after each half-step, and compare with the best rank-one error.

20. • Find the best $k = 2$ [sparse PCA](/sparse-pca/) vector for $A = \begin{pmatrix} 4 & 0 & 1 \\ 0 & 3 & 2 \\ 1 & 2 & 3 \end{pmatrix}$, and its value. What does a greedy method that starts from the largest diagonal entry find? What is the value without the sparsity constraint?

21. • Three points have the kernel $K = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix}$ and $\alpha = 0$. Write the walk $P$ and its stationary law $\pi$ for [diffusion maps](/diffusion-maps/), compute the diffusion distance $D_1(1, 3)^2$ from its definition, and check it against the eigenvectors of $P$ normalized by $\sum_i \pi_i \psi(i)^2 = 1$.

22. • Two points are drawn uniformly and independently from the cube $[0, 1]^d$. Find the mean and the variance of their squared distance, and the ratio of its standard deviation to its mean for $d = 100$ and $d = 10^4$.

23. ★ Show that in the definition of trustworthiness, $\sum_i \sum_{j \in U_k(i)} (r(i,j) - k) \le nk(2n - 3k - 1)/2$ when $k < n/2$, so that $T(k) \ge 0$.

24. ★ Centered data matrices $X$ ($n \times p$) and $Y$ ($n \times q$) have full column rank, and $p + q > n - 1$. Prove that at least $p + q - n + 1$ of the [canonical correlations](/canonical-correlation-analysis/) equal 1. How many must equal 1 for $n = 10$, $p = 6$ and $q = 7$?

25. ★ Prove that a symmetric matrix $A$ has $\operatorname{rank} A \ge (\operatorname{tr} A)^2/\operatorname{tr}(A^2)$. Use it to show that $n$ unit vectors in $\mathbb{R}^k$ with $|\langle v_i, v_j \rangle| \le \varepsilon$ for $i \ne j$ need $k \ge n/(1 + (n-1)\varepsilon^2)$. Evaluate the bound for $n = 10^6$ and $\varepsilon = 0.01$. This is the starting point of [JL optimality](/johnson-lindenstrauss-optimality/).

26. ★ For a graph with symmetric weights $W$, degree matrix $D$ and Laplacian $L = D - W$, prove $y^\top L y = \tfrac12 \sum_{i,j} W_{ij}(y_i - y_j)^2$. Deduce that, when every vertex has positive degree, the multiplicity of the eigenvalue 0 in $Ly = \lambda Dy$ equals the number of connected components. Give a basis of the null space for the graph with the two edges $\{1, 2\}$ and $\{3, 4\}$.

27. ★ A linear map $f$ keeps the squared lengths of $x + y$ and $x - y$ within a factor $1 \pm \varepsilon$, where $x$ and $y$ are unit vectors. Prove $|\langle f(x), f(y) \rangle - \langle x, y \rangle| \le \varepsilon$. Which point set must a [random projection](/random-projection/) be applied to so that this holds for all pairs of $n$ unit vectors, and how does the target dimension change?
