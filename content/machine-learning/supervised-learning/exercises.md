1. ◦ A binary classifier is tested on 200 examples. Its [confusion matrix](/confusion-matrix/) has 40 true positives, 10 false positives, 20 false negatives and 130 true negatives. Compute its accuracy, balanced accuracy, [precision, recall](/precision-and-recall/) and $F_1$ score.

2. ◦ A scoring rule gives the positives the scores $0.9, 0.7, 0.4$ and the negatives the scores $0.8, 0.5, 0.3, 0.2$. Compute the [AUC](/roc-auc/) by counting pairs, and again from the rank sum $R_+$ of the positives.

3. ◦ A node holds 4 positive and 4 negative examples. A split sends 3 positives and 1 negative to the left child and the rest to the right. Compute the [information gain](/information-gain/) in bits and the decrease of the size-weighted [Gini impurity](/gini-impurity/).

4. ◦ A finite class has $|H| = 10^6$ hypotheses. With $\varepsilon = 0.02$ and $\delta = 0.001$, how many examples does the [PAC](/pac-learning/) bound $\lceil \ln(|H|/\delta)/\varepsilon \rceil$ ask for in the realizable case? How many does the [agnostic](/agnostic-pac-learning/) bound $\lceil 2\ln(2|H|/\delta)/\varepsilon^2 \rceil$ ask for?

5. ◦ Run the [perceptron](/perceptron/), with $w = 0$, $b = 0$ and the test $y(w \cdot x + b) \le 0$, on the examples $((2, 1), +1)$, $((0, 2), -1)$, $((1, -1), +1)$, $((-1, 0), -1)$ in this order, epoch after epoch. List the mistakes, and give the final $(w, b)$ and the number of epochs.

6. ◦ Fit the line $y = a + bx$ by [ordinary least squares](/ordinary-least-squares/) to the points $(0, 1)$, $(1, 3)$, $(2, 4)$, $(3, 8)$. Then fit it by [ridge regression](/ridge-regression/) with $\lambda = 5$ on centered data, so that only the slope is penalized. By what factor does the slope shrink?

7. ◦ Run [pool adjacent violators](/pool-adjacent-violators/) on the values $1, 3, 2, 4, 3, 2, 5$ with equal weights. Show the stack of blocks after each value is read, and give the fitted non-decreasing sequence.

8. ◦ In the first round of [AdaBoost](/adaboost/) on 10 examples with equal weights, the chosen stump misclassifies 2 of them. Compute $\varepsilon_1$, $\alpha_1$, the normalizer $Z_1$, and the new weight of a misclassified and of a correctly classified example.

9. ◦ The input $X$ is uniform on three points $a, b, c$, and $\Pr[Y = 1 \mid X]$ is $0.9$, $0.5$ and $0.2$ at them. Give a [Bayes optimal classifier](/bayes-optimal-classifier/) and its risk $R^\ast$. Then compute the limit risk of the 1-nearest neighbor rule, $\mathbb{E}[2\eta(X)(1 - \eta(X))]$, and check it against the [Cover-Hart](/cover-hart-theorem/) bound $2R^\ast(1 - R^\ast)$.

10. ◦ In [XGBoost](/xgboost/) with $\lambda = 1$ and $\gamma = 1$, a leaf has gradient sum $G = -6$ and Hessian sum $H = 4$. What is its weight $w^\ast$? A split would give the children $(G_L, H_L) = (-8, 2)$ and $(G_R, H_R) = (2, 2)$. Compute its gain and the two child weights. Is the split made?

11. • Show that the class of axis-aligned rectangles $[a_1, b_1] \times [a_2, b_2]$ in the plane has [VC dimension](/vc-dimension/) 4: give four points it shatters, and show that it cannot shatter any five points. Then give an $O(n)$ algorithm that, on a sample labeled by some rectangle, returns a rectangle with no training error.

12. • Let $x_1, \dots, x_n$ be independent with mean $\mu$ and variance $\sigma^2$, and estimate $\mu$ by $c\bar x$ for a constant $c$. Write the [mean squared error](/mean-squared-error/) as squared bias plus variance, and find the $c$ that minimizes it. Explain why this is the same tradeoff as in ridge regression, and why the best $c$ cannot be used as it stands.

13. • Show that on linearly separable data the [logistic regression](/logistic-regression/) loss $\sum_i \log(1 + e^{-y_i (w \cdot x_i + b)})$ has infimum 0 and no minimizer. Then show that adding $\lambda\|w\|^2$ with $\lambda > 0$, and leaving $b$ unpenalized, gives a problem with exactly one minimizer when both labels occur in the data.

14. • For labels $y \in \{-1, +1\}$ and $\eta = \Pr[y = 1 \mid x]$, find the $f$ that minimizes the conditional exponential loss $\eta e^{-f} + (1 - \eta) e^{f}$. Evaluate it at $\eta = 0.8$, and compare it with the minimizer of the [logistic loss](/logistic-loss/) at the same $\eta$.

15. • Show that $k(x, z) = \cos(x - z)$ on $\mathbb{R}$ is a positive semidefinite kernel by giving a feature map into $\mathbb{R}^2$. What is the largest possible rank of its Gram matrix? Check this on the points $0, \pi/2, \pi$.

16. • Eight examples with binary features $x_1, x_2, x_3$ have the label $y = x_1 \oplus x_2$. Each pair $(x_1, x_2)$ occurs twice. Set $x_3 = y$ on every example except one copy of $(0, 0)$, where $x_3 = 1$, and one copy of $(0, 1)$, where $x_3 = 0$. Run [ID3](/id3/) on these examples. Which attribute does it test at the root, and how many leaves does its tree have? Compare with the best tree.

17. • A node holds 8 positives and 8 negatives. Split $A$ sends 1 negative to the left and the other 15 examples to the right. Split $B$ sends 1 positive and 3 negatives to the left and the rest to the right. Show that information gain prefers $A$ and the Gini impurity prefers $B$.

18. • A data set has $n = 50$ examples, $10^4$ features of pure noise, and labels drawn by fair coin flips independent of the features. A program picks the 20 features most correlated with the labels on all 50 examples, and then runs 5-fold [cross-validation](/cross-validation/) of a classifier on those 20 features. Its estimate of the error is far below $1/2$. What is the true error of every classifier on this task? What went wrong, and how should the procedure be changed?

19. • In [gradient boosting](/gradient-boosting/) with the absolute loss $|y - F(x)|$, what are the pseudo-residuals of a round? Show that the best constant value of a leaf, for this loss, is a median of the residuals $y_i - F_{t-1}(x_i)$ of the examples in the leaf.

20. • Let $\Phi$ be the $n \times D$ matrix of feature vectors. Prove the identity $(\Phi^\top \Phi + \lambda I_D)^{-1}\Phi^\top = \Phi^\top(\Phi\Phi^\top + \lambda I_n)^{-1}$ for $\lambda > 0$, and use it to show that ridge regression in feature space and [kernel ridge regression](/kernel-ridge-regression/) give the same prediction at every point.

21. • Use the singular value decomposition $X = U\Sigma V^\top$ to show that the ridge solution $(X^\top X + \lambda I)^{-1}X^\top y$ converges, as $\lambda \to 0^+$, to the least squares solution of least norm, $X^+ y$, even when $X$ does not have full column rank.

22. ★ Let $m \le d$. Show that for every deterministic online learner of linear classifiers through the origin there is a sequence of $m$ examples in $\mathbb{R}^d$ with $\|x\| \le 1$ that a unit vector separates with margin at least $1/\sqrt m$, on which the learner errs on every example. Conclude that the bound $(R/\gamma)^2$ of the [perceptron convergence theorem](/perceptron-convergence-theorem/) cannot be improved by any such learner, and give a sequence on which the perceptron without bias makes exactly $m$ mistakes.

23. ★ Give an $O(n^3)$ algorithm for [empirical risk minimization](/empirical-risk-minimization/) under the 0-1 loss over all halfspaces in the plane, for $n$ points in general position, with no assumption that the data are separable. Generalize it to a polynomial algorithm for each fixed dimension $d$. Explain why this does not contradict the NP-hardness of agnostic [halfspace learning](/halfspace-learning/).

24. ★ Show that the class of halfspaces through the origin, $x \mapsto \mathrm{sign}(w \cdot x)$ with $\mathrm{sign}(0) = +1$, has VC dimension exactly $d$ in $\mathbb{R}^d$.

25. ★ For a distribution on the plane labeled by an axis-aligned rectangle, let the learner return the smallest rectangle that contains the positive examples. Prove that it is a PAC learner: with $n \ge \lceil (4/\varepsilon)\ln(4/\delta) \rceil$ examples its error is at most $\varepsilon$ with probability at least $1 - \delta$. Compare this with the bound from the VC dimension.

26. ★ Let $P$ and $N$ be finite sets of points in $\mathbb{R}^d$ whose convex hulls are disjoint. Prove that the margin of the hard-margin [support vector machine](/support-vector-machine/), $\max_{\|w\| = 1,\, b} \min_i y_i(w \cdot x_i + b)$, equals half the distance between the convex hulls of $P$ and $N$.
