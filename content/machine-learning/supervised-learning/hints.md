1. Accuracy $170/200 = 0.85$. Recall $40/60 = 2/3$ and specificity $130/140 = 13/14$, so the balanced accuracy is $67/84 \approx 0.798$. Precision $40/50 = 0.8$. $F_1 = 2\,TP/(2\,TP + FP + FN) = 80/110 = 8/11 \approx 0.727$.

3. The parent has entropy 1 bit and each child has entropy $H(1/4) \approx 0.811$, so the gain is about $0.189$ bits. The parent's Gini impurity is $1/2$ and each child's is $1 - 9/16 - 1/16 = 3/8$, so the decrease is $1/8$.

4. $\ln(10^9) \approx 20.72$ gives 1037 examples. $2\ln(2 \cdot 10^9) \approx 42.83$, divided by $\varepsilon^2 = 0.0004$, gives 107083: about a hundred times more, because $\varepsilon$ enters squared.

5. Epoch 1 errs on $(2, 1)$, giving $w = (2, 1)$, $b = 1$, and on $(0, 2)$, where $w \cdot x + b = 3$ has the wrong sign, giving $w = (2, -1)$, $b = 0$. The last two examples are then correct, and epoch 2 makes no mistake. The output is $w = (2, -1)$, $b = 0$ after 2 mistakes and 2 epochs.

8. $\varepsilon_1 = 0.2$, $\alpha_1 = \frac12 \ln 4 = \ln 2 \approx 0.693$ and $Z_1 = 2\sqrt{0.2 \cdot 0.8} = 0.8$. A misclassified example gets $0.1 \cdot 2/0.8 = 0.25$ and a correct one $0.1 \cdot \frac12/0.8 = 0.0625$, so the two mistakes now carry half the weight.

10. $w^\ast = 6/5$. The gain is $\frac12(64/3 + 4/3 - 36/5) - 1 = 101/15 \approx 6.73 > 0$, so the split is made, with child weights $8/3$ and $-2/3$.

13. If $(w, b)$ separates the data, the loss of $(tw, tb)$ tends to 0 as $t \to \infty$, but each term is positive, so no point attains the infimum. With the penalty the Hessian is $\tilde X^\top S \tilde X + \lambda\,\mathrm{diag}(0, I)$; it is positive definite (split on whether the $w$ part of a direction is zero), so the objective is strictly convex. It also tends to infinity as $\|w\|$ or $|b|$ grows when both labels occur, so a minimizer exists.

16. At the root $x_1$ and $x_2$ have gain 0, since each of their values leaves two examples of each label, and $x_3$ has gain $1 - H(1/4) \approx 0.189$. ID3 tests $x_3$. In both children $x_1$ has gain $0.311$ and $x_2$ has gain $0.123$, so it tests $x_1$ and then $x_2$ below $x_1 = 0$. The tree has 6 leaves and depth 3. The tree that tests $x_1$ and then $x_2$ is also consistent, with 4 leaves and depth 2.

17. Split $A$: gain $\approx 0.0655$ bits, Gini decrease $1/30 \approx 0.0333$. Split $B$: gain $\approx 0.0623$ bits, Gini decrease $1/24 \approx 0.0417$. Entropy rewards the small pure child of $A$ more than the Gini impurity does.

18. Every classifier has true error exactly $1/2$, because the labels are independent of the features. The selection looked at the labels of the examples that later serve as test folds, so those folds are no longer new data. Select the features again inside each fold, using only its training part.

20. Multiply $\Phi^\top(\Phi\Phi^\top + \lambda I) = (\Phi^\top\Phi + \lambda I)\Phi^\top$ on the left by $(\Phi^\top\Phi + \lambda I)^{-1}$ and on the right by $(\Phi\Phi^\top + \lambda I)^{-1}$; both are invertible for $\lambda > 0$. So $\hat w = \Phi^\top \alpha$ with $\alpha = (K + \lambda I)^{-1} y$, and $\varphi(x) \cdot \hat w = \sum_i \alpha_i k(x_i, x)$.

22. Present $x_t = e_t$ and give it the label opposite to the learner's prediction. Any labels $y_1, \dots, y_m$ are realized by $u = \sum_t y_t e_t/\sqrt m$, a unit vector with margin $1/\sqrt m$, and $R = 1$, so $(R/\gamma)^2 = m$. The perceptron without bias on $e_1, \dots, e_m$, all labeled $+1$, has $w \cdot e_t = 0$ at step $t$, since $w$ lies in the span of the earlier vectors, so it errs every time. The argument needs $m \le d$.

23. Move the boundary of any halfspace, first by translation and then by rotation about a sample point, until it passes through two sample points, without letting it cross any other point. The labeling of the other points does not change, so every labeling a halfspace gives the sample is one of the $O(n^2)$ lines through two points with one of four choices of sides for those two points, or a constant labeling. Each candidate costs $O(n)$ to score. In $\mathbb{R}^d$ use hyperplanes through $d$ points: $O(n^{d+1})$ time for fixed $d$. The hardness results take $d$ as part of the input.

24. The vectors $e_1, \dots, e_d$ are shattered by $w = \sum_i y_i e_i$. Any $d + 1$ vectors satisfy $\sum_i a_i x_i = 0$ with some $a_i \ne 0$; say some $a_i > 0$. If some $a_j < 0$, label $x_i$ by $\mathrm{sign}(a_i)$ where $a_i \ne 0$, and the rest at will: then $0 = \sum_i a_i (w \cdot x_i)$ would be positive. If no $a_j < 0$, label every $x_i$ with $a_i > 0$ by $-1$: then the sum would be negative.

25. Inside the target rectangle, take four strips along its sides, each the thinnest with probability at least $\varepsilon/4$. If the sample hits all four, the learned rectangle contains the target minus the strips, and its error is at most $\varepsilon$. A fixed strip is missed with probability at most $(1 - \varepsilon/4)^n \le e^{-\varepsilon n/4}$; the union bound over four strips gives $4e^{-\varepsilon n/4} \le \delta$. The VC bound for $d = 4$ has an extra factor $\ln(1/\varepsilon)$.

26. If $(w, b)$ has margin $\gamma$, then $w \cdot p + b \ge \gamma$ on the hull of $P$ and $w \cdot q + b \le -\gamma$ on the hull of $N$, so every $p - q$ has length at least $2\gamma$. Conversely, let $p^\ast, q^\ast$ be the closest pair of the two hulls and $w = (p^\ast - q^\ast)/\|p^\ast - q^\ast\|$, with the boundary through the midpoint. The projection property of convex sets gives $w \cdot x \ge w \cdot p^\ast$ on $P$ and $w \cdot x \le w \cdot q^\ast$ on $N$, so the margin is $\|p^\ast - q^\ast\|/2$.
