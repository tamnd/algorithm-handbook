## What to remember

- **The model.** Examples are drawn independently from an unknown distribution $D$; a hypothesis $h$ is judged by its risk $L_D(h)$, its expected loss on a new example. Under the 0-1 loss no rule beats the [Bayes optimal classifier](/bayes-optimal-classifier/) $\arg\max_y \Pr[Y = y \mid X = x]$. It needs $D$, so it is only a benchmark.
- **How much data.** For a finite class in the realizable case, every [ERM](/empirical-risk-minimization/) output has risk at most $\varepsilon$ with probability at least $1 - \delta$ once $n \ge \lceil \ln(|H|/\delta)/\varepsilon \rceil$. For an infinite binary class the [VC dimension](/vc-dimension/) $d$ takes the place of $\ln |H|$: the class is PAC learnable exactly when $d$ is finite, and agnostic learning then needs $\Theta((d + \ln(1/\delta))/\varepsilon^2)$ examples. By the [no-free-lunch theorem](/no-free-lunch-theorem-learning/), no learner succeeds on every distribution without some such restriction.
- **Bias and variance.** For squared loss, the expected error at a point is noise plus squared bias plus variance, exactly. That a richer class trades lower bias for higher variance is only a tendency.
- **Linear regression.** [OLS](/ordinary-least-squares/) solves $X^\top X w = X^\top y$, best computed by a QR decomposition in $2nd^2 - 2d^3/3$ flops. [Ridge](/ridge-regression/) has one solution for every $\lambda > 0$ and shrinks the fit along singular direction $i$ by $\sigma_i^2/(\sigma_i^2 + \lambda)$. The [lasso](/lasso-regression/) sets weights exactly to zero.
- **Mistake and margin bounds.** If a unit vector separates the data with margin $\gamma$ and every input has norm at most $R$, the [perceptron](/perceptron/) makes at most $(R/\gamma)^2$ mistakes for every order of the examples (with a bias term, $R$ and $\gamma$ are measured on inputs extended by a constant 1); on data that is not separable it never stops. The [margin bound](/margin-generalization-bound/) holds with high probability and does not depend on the dimension.
- **Surrogate losses.** The [hinge](/hinge-loss/) and [logistic](/logistic-loss/) losses are convex and classification calibrated, so minimizing them does no harm to the 0-1 risk in the limit.
- **Trees.** Finding a tree with the fewest expected tests is NP-hard, so [ID3](/id3/), C4.5 and [CART](/cart/) grow trees greedily, with no general guarantee: on XOR the greedy tree can be no better than chance.
- **Ensembles.** Averaging $m$ predictors of variance $\sigma^2$ and correlation $\rho$ gives variance $\rho\sigma^2 + (1 - \rho)\sigma^2/m$, so [random forests](/random-forest/) make their trees less alike. If round $t$ of [AdaBoost](/adaboost/) has edge $\gamma_t$, the training error is at most $\exp(-2\sum_t \gamma_t^2)$ on every sample; this says nothing by itself about new data.
- **Nearest neighbors.** In the limit of infinite data, the 1-nearest neighbor rule has risk at most $2R^\ast(1 - R^\ast)$ for two classes, where $R^\ast$ is the Bayes risk ([Cover-Hart](/cover-hart-theorem/)). It says nothing for a fixed $n$.

## The main methods side by side

| Method | Output | Training time, worst case |
|---|---|---|
| [OLS](/ordinary-least-squares/), Householder QR | linear | $\Theta(nd^2)$ |
| [Ridge](/ridge-regression/), primal | linear | $\Theta(nd^2 + d^3)$ |
| [Lasso](/lasso-regression/), coordinate descent | sparse linear | $O(knd)$ for $k$ sweeps |
| [Logistic regression](/logistic-regression/), Newton | linear, probabilities | $O(k(nd^2 + d^3))$ for $k$ steps |
| [Perceptron](/perceptron/), separable data | linear | $O((M + 1)nd)$ for $M \le (R'/\gamma)^2$ mistakes |
| [Naive Bayes](/naive-bayes-classifier/) | generative | $\Theta(nd + kd)$ for $k$ classes |
| [$k$-NN](/k-nearest-neighbors/) | the stored data | none; $O(nd + n \log k)$ per query |
| [SVM](/support-vector-machine/), SMO-type solver | kernel expansion | $O(n^2 t + sn)$ |
| [Kernel ridge](/kernel-ridge-regression/) | kernel expansion | $\Theta(n^2 t + n^3)$ |
| [CART](/cart/) | tree | $O(dn^2 \log n)$ |
| [Random forest](/random-forest/) | $B$ trees | $O(Bmn^2 \log n)$ |
| [AdaBoost](/adaboost/), stumps | weighted vote | $O(dn \log n + Tdn)$ |
| [Gradient boosting](/gradient-boosting/) | sum of trees | $O(TDdn \log n)$ |

: Costs on the real RAM for $n$ examples with $d$ features. Here $t$ is the cost of one kernel evaluation, $s$ the number of solver steps, $R'$ the radius of the inputs extended by a constant 1, $m$ the number of features drawn at each node, $T$ the number of rounds and $D$ the depth of each boosted tree.

## Choosing a method

- Start with least squares for numbers and logistic regression for classes. Add a ridge or lasso penalty when $d$ is large next to $n$.
- For a nonlinear boundary, try a kernel SVM or a tree ensemble. A kernel method works with the $n \times n$ kernel matrix, so its cost grows at least like $n^2$.
- Choose $\lambda$, $k$ or the tree size by [cross-validation](/cross-validation/) on the training data, and keep a test set that no choice has seen.
- When one class is rare, judge a classifier by [precision and recall](/precision-and-recall/) or the [ROC curve](/roc-auc/), not by accuracy alone.
