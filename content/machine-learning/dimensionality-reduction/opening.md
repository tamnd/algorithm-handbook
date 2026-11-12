A photograph of a face, with one number per pixel, is a point in a space with thousands of dimensions. Yet a set of 698 such images of one face, taken as the head turns left and right, up and down, and as the light moves, has only three degrees of freedom. Tenenbaum, de Silva and Langford recovered those three coordinates from the pixels alone with [Isomap](/isomap/). Dimensionality reduction is the search for such a small description: a map from $n$ points in $\mathbb{R}^d$ to $n$ points in $\mathbb{R}^k$, with $k$ much smaller than $d$, that keeps the part of the structure you care about.

The methods differ in what they keep and in what they assume. [PCA](/principal-component-analysis/) assumes the data lie near a linear subspace and keeps the most variance; on eight points in $\mathbb{R}^3$ with covariance eigenvalues 81, 36 and 9, two components keep $117/126$ of it, and the mean squared error left is 9, the third eigenvalue. A [random projection](/random-projection/) assumes nothing about the data and keeps every pairwise distance within a factor $1 \pm \varepsilon$, with high probability. Manifold learners assume a curved low-dimensional set and work on a neighbor graph. [t-SNE](/t-sne/) and [UMAP](/umap/) keep neighborhoods only, and promise nothing beyond lowering their own objective. Each entry states its model, its objective and its cost, and you should read every guarantee with the model attached: for all inputs, with high probability over a random matrix, or only in the limit of dense sampling.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **Data in high dimension.** The [covariance matrix](/covariance-matrix/), the [curse of dimensionality](/curse-of-dimensionality/), the [manifold hypothesis](/manifold-hypothesis/), and [intrinsic dimension](/intrinsic-dimension/) and how to [estimate it](/intrinsic-dimension-estimation/).
2. **Principal component analysis.** PCA, its [explained variance](/explained-variance/) and [reconstruction error](/reconstruction-error/), the [scree plot](/scree-plot/), and [whitening](/whitening/).
3. **PCA at scale and beyond.** [Randomized](/randomized-pca/), [incremental](/incremental-pca/), [sparse](/sparse-pca/), [robust](/robust-pca/) and [kernel](/kernel-pca/) PCA.
4. **Latent variable models.** [Factor analysis](/factor-analysis/), [probabilistic PCA](/probabilistic-pca/), the [autoencoder](/autoencoder/) and the [variational autoencoder](/variational-autoencoder/).
5. **Labels, pairs and selected features.** [LDA](/linear-discriminant-analysis/), [CCA](/canonical-correlation-analysis/) and [feature selection](/feature-selection/).
6. **Sources and parts.** [Blind source separation](/blind-source-separation/), [ICA](/independent-component-analysis/), [FastICA](/fastica/), [projection pursuit](/projection-pursuit/), [NMF](/nonnegative-matrix-factorization/) and [LSA](/latent-semantic-analysis/).
7. **Random projections.** The [Johnson-Lindenstrauss lemma](/johnson-lindenstrauss-lemma/), dense, [sparse](/sparse-random-projection/) and [fast](/fast-johnson-lindenstrauss-transform/) projections, and the [lower bound](/johnson-lindenstrauss-optimality/).
8. **Multidimensional scaling.** [MDS](/multidimensional-scaling/), [classical MDS](/classical-mds/), [SMACOF](/smacof/) and [Sammon mapping](/sammon-mapping/).
9. **Manifold learning.** [The framework](/manifold-learning/), Isomap, [LLE](/locally-linear-embedding/), [Laplacian eigenmaps](/laplacian-eigenmaps/), [LPP](/locality-preserving-projections/), [diffusion maps](/diffusion-maps/), [Hessian eigenmaps](/hessian-eigenmaps/), [LTSA](/local-tangent-space-alignment/) and [semidefinite embedding](/semidefinite-embedding/).
10. **Neighbor embeddings and maps.** [SNE](/stochastic-neighbor-embedding/), t-SNE, UMAP, [trustworthiness and continuity](/trustworthiness-and-continuity/), the [self-organizing map](/self-organizing-map/) and [principal curves](/principal-curves/).

The groups go from linear to nonlinear. Most methods in groups 2 to 6 find a linear map, with the eigenproblem or the SVD at their core; group 7 picks a linear map at random. Most methods in groups 8 to 10 place the given points directly and need an extra step to place a new one.

## A first reading

For a short path through the ideas, read these eleven entries in order:

1. the covariance matrix;
2. the curse of dimensionality;
3. principal component analysis;
4. reconstruction error;
5. probabilistic PCA;
6. the Johnson-Lindenstrauss lemma;
7. random projection;
8. classical MDS;
9. Isomap;
10. Laplacian eigenmaps;
11. t-SNE.

They give the linear optimum, its probabilistic reading, the data-blind random alternative, the step from distances to coordinates, and the two main kinds of nonlinear method. On a first pass skip the research-level entries on the [fast JL transform](/fast-johnson-lindenstrauss-transform/) and [JL optimality](/johnson-lindenstrauss-optimality/), and leave Hessian eigenmaps, LTSA, diffusion maps and semidefinite embedding until Isomap and LLE feel familiar. Sparse and robust PCA can wait until you need them.

## Before you start

The linear methods are numerical linear algebra. You need the [symmetric eigenproblem](/symmetric-eigenproblem/), the [singular value decomposition](/singular-value-decomposition/), [positive definite matrices](/positive-definite-matrix/), the [Rayleigh quotient](/rayleigh-quotient/) and the [generalized eigenvalue problem](/generalized-eigenvalue-problem/), all from Volume 12, and [power iteration](/power-iteration/) and the [QR decomposition](/qr-decomposition/) for the large-scale entries. From probability (Volume 1) you need [variance](/variance/) and [expected value](/expected-value/), and for the JL lemma the [union bound](/union-bound/), the [Markov inequality](/markov-inequality/) and [concentration of measure](/concentration-of-measure/). The graph methods use [k-nearest-neighbor graphs](/k-nearest-neighbor-graph/) (Volume 5), [all-pairs shortest paths](/all-pairs-shortest-paths/) and the [Laplacian matrix](/laplacian-matrix/) (Volume 7), and [Markov chains](/markov-chain/) for diffusion maps. The embeddings that are fitted by optimization use [gradient descent](/gradient-descent/) and [stochastic gradient descent](/stochastic-gradient-descent/) from Volume 15. Factor analysis and probabilistic PCA use [maximum likelihood](/maximum-likelihood-estimation/) and [EM](/expectation-maximization/), and the autoencoders use [backpropagation](/backpropagation/), all from other chapters of this volume.
