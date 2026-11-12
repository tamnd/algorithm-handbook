## What to remember

- [PCA](/principal-component-analysis/) keeps the top $k$ eigenvectors of the covariance matrix. For every data set, this subspace has the most variance $\lambda_1 + \cdots + \lambda_k$ and the least mean squared [reconstruction error](/reconstruction-error/) $\sum_{j > k} \lambda_j$ among all $k$-dimensional linear subspaces. The same subspace is the maximum likelihood fit of [probabilistic PCA](/probabilistic-pca/), whose noise variance $\sigma^2$ is the mean of the discarded eigenvalues.
- [Randomized PCA](/randomized-pca/) with oversampling $p$ has, in expectation, a Frobenius error at most $(1 + k/(p-1))^{1/2}$ times the optimum, and is exact with probability 1 when the data have rank at most $k + p$. [Robust PCA](/robust-pca/) recovers a low-rank matrix and sparse corruptions exactly with probability at least $1 - cn^{-10}$, under incoherence and a random support.
- The [Johnson-Lindenstrauss lemma](/johnson-lindenstrauss-lemma/): a random linear map to $k \ge 4\ln n/(\varepsilon^2/2 - \varepsilon^3/3)$ dimensions keeps all $\binom{n}{2}$ distances within $1 \pm \varepsilon$ with probability at least $1/n$, or $1 - n^{-\beta}$ with $4 + 2\beta$ in place of 4. [JL optimality](/johnson-lindenstrauss-optimality/): $k = \Omega(\varepsilon^{-2}\log n)$ is needed by every map, for $\varepsilon$ above $\min(n, d)^{-0.4999}$.
- [Classical MDS](/classical-mds/) recovers points from distances by an eigendecomposition of $B = -\tfrac12 J D^{(2)} J$. The distances are Euclidean exactly when $B \succeq 0$. [SMACOF](/smacof/) never increases the stress but can stop at a local minimum.
- Spectral manifold methods build a neighbor graph and solve one eigenproblem exactly; [Laplacian eigenmaps](/laplacian-eigenmaps/) minimize $\operatorname{tr}(Y^\top L Y)$ subject to $Y^\top D Y = I$. [Isomap](/isomap/) has a recovery theorem: for any $\lambda_1, \lambda_2 \in (0, 1)$, $(1-\lambda_1)d_{\mathcal M} \le D_G \le (1+\lambda_2)d_{\mathcal M}$ with high probability, for a geodesically convex manifold under dense sampling. [LLE](/locally-linear-embedding/) and [LTSA](/local-tangent-space-alignment/) recover coordinates only up to an affine map.
- [SNE](/stochastic-neighbor-embedding/) and [t-SNE](/t-sne/) lower a nonconvex KL divergence by gradient descent; [UMAP](/umap/) runs sampled updates aimed at a cross entropy, which do not follow its gradient. None has a guarantee about the map; check a map with [trustworthiness and continuity](/trustworthiness-and-continuity/).
- [ICA](/independent-component-analysis/) identifies the sources up to order, sign and scale when at most one of them is Gaussian. The updates of [NMF](/nonnegative-matrix-factorization/) never increase its loss, but NMF is NP-hard.

| Method | Model and objective | Guarantee | Time |
|---|---|---|---|
| PCA | linear subspace; most variance | optimal, every input | $O(nd^2 + d^3)$ |
| Randomized PCA | the same, from a sketch | error $\le (1 + \frac{k}{p-1})^{1/2} \times$ optimal, in expectation | $O((q+1)nd(k+p) + (q+1)(n+d)(k+p)^2)$ |
| [Kernel PCA](/kernel-pca/) | linear subspace in feature space | optimal in feature space, every input | $O(n^2 d + n^3)$ |
| Robust PCA | low rank plus sparse | exact, probability $\ge 1 - cn^{-10}$ | $O(T n_1 n_2 \min(n_1, n_2))$ |
| Random projection | none; all pairwise distances | $1 \pm \varepsilon$, probability $\ge 1/n$ | $O(ndk)$ |
| [Fast JL transform](/fast-johnson-lindenstrauss-transform/) | none; all pairwise distances | $1 \pm \varepsilon$, probability $\ge 2/3$ | $O(d \log d + \min(d\varepsilon^{-2}\log n, \varepsilon^{-2}\log^3 n))$ per point |
| Classical MDS | Euclidean distances; strain | optimal for strain, every input | $O(n^3)$ |
| SMACOF | dissimilarities; stress | stress never increases | $O(tn^2 k)$ |
| Isomap | convex manifold; graph distances | near-isometric, with high probability, dense sampling | $O(n^2 d + n^2 k \log n + n^3)$ |
| LLE | locally linear patches; weights | optimal for the weights; affine image | $O(n^2 d + nk^2 d + nk^3 + n^3)$ |
| Laplacian eigenmaps | neighbor graph; $\operatorname{tr}(Y^\top L Y)$ | optimal for the graph | $O(n^2 d + n^3)$ |
| t-SNE | neighbor probabilities; KL divergence | none | $O(n^2 d + n^2 t m)$ |

: Methods and their guarantees. $n$ points in $\mathbb{R}^d$; $k$ is the output dimension, or the number of neighbors for Isomap and LLE; $p$ and $q$ are the oversampling and power steps; robust PCA has an $n_1 \times n_2$ matrix and $T$ iterations; $t$ counts iterations and $m$ is the t-SNE map dimension.

## Choosing a method

Start with PCA; its eigenvalues tell you what you lose. For very large data use randomized PCA, or [incremental PCA](/incremental-pca/) for a stream. When you need a distortion bound for every pair, use a random projection; its $k$ depends on $n$ and $\varepsilon$, not on $d$.

For labeled data use [LDA](/linear-discriminant-analysis/), for mixed signals ICA, and for nonnegative parts such as counts NMF. With only distances, use classical MDS if they are close to Euclidean and SMACOF otherwise. For a curved manifold, try Isomap if it has no holes, and Laplacian eigenmaps or [diffusion maps](/diffusion-maps/) otherwise. For a picture of clusters, use t-SNE or UMAP with more than one setting, and do not read cluster sizes or the distances between clusters from it.
