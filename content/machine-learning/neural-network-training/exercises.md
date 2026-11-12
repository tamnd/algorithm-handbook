1. ◦ A network has one input, one ReLU hidden unit and one linear output: $z_1 = w_1 x + b_1$, $a_1 = \mathrm{relu}(z_1)$, $\hat y = w_2 a_1 + b_2$, with the loss $\frac12(\hat y - y)^2$. Take $x = 2$, $y = 1$, $w_1 = 0.5$, $b_1 = -0.5$, $w_2 = 3$ and $b_2 = 0$. Run the forward pass and [backpropagation](/backpropagation/) by hand, and give the loss and its four partial derivatives.

2. ◦ Draw the [computational graph](/computational-graph/) of $f(x_1, x_2) = x_1 x_2 + x_1^2$, with the product, the square and the sum as one node each. Evaluate it at $(3, 2)$, run the reverse sweep of [automatic differentiation](/automatic-differentiation/), and give both partial derivatives. How many contributions does the adjoint of $x_1$ collect?

3. ◦ A fully connected layer has 1024 inputs and 1024 outputs. Give the standard deviation of normal weights, and the bound $a$ of uniform weights on $[-a, a]$, under [Xavier](/xavier-initialization/) and under [He initialization](/he-initialization/). A stack of 20 such ReLU layers is initialized with Xavier weights instead of He weights. By what factor is the mean square of the pre-activations of the last layer smaller?

4. ◦ A cosine [learning rate schedule](/learning-rate-schedule/) runs from $\eta_{\max} = 0.1$ to $\eta_{\min} = 0$ over $T = 100$ steps. Give $\eta_{25}$, $\eta_{50}$ and $\eta_{75}$. The peak 0.1 was tuned for batches of 256 examples; what peak does the linear scaling rule give for batches of 4096?

5. ◦ Inverted [dropout](/dropout/) with keep probability $p = 0.8$ acts on $h = (1, 2, 3, 4, 5)$, and the mask drawn is $(1, 0, 1, 1, 0)$. Give the output. Over random masks, what are the mean and the variance of the sum of the five outputs?

6. ◦ One feature of a [batch normalization](/batch-normalization/) layer takes the values $2, 4, 6, 8$ on a batch of four, with $\gamma = 2$, $\beta = 1$ and $\epsilon = 0$. Give the four outputs in training mode. If the running statistics end at this batch's mean and its unbiased variance, what does the layer output at inference for the input 10?

7. ◦ [Label smoothing](/label-smoothing/) with $\varepsilon = 0.2$ is used with $K = 4$ classes. Write the smoothed target of an example of class 1. At the minimum of the smoothed loss, what is the gap between the logit of the true class and each other logit?

8. ◦ Iterative magnitude pruning, the procedure behind the [lottery ticket hypothesis](/lottery-ticket-hypothesis/), removes 20% of the remaining weights in each round. How many rounds does it take to keep at most 10% of the weights, and what fraction is left after that round?

9. ◦ A chain of 30 sigmoid layers has $\sigma_{\max}(W_l) = 2$ for every weight matrix. Use the bound of the [vanishing gradient problem](/vanishing-gradient-problem/) to bound the ratio of the gradient norm at the bottom of the chain to the one at the top. Then take the scalar recurrence $h_t = \tanh(w h_{t-1})$ with $h_0 = 0$, and give $\partial h_{50}/\partial h_0$ for $w = 0.9$ and for $w = 1.1$; the second case is an instance of the [exploding gradient problem](/exploding-gradient-problem/).

10. • A network has layer widths 784, 512, 256 and 10 and no biases. Count its weights $P$. Bound the multiply-adds of one forward and backward pass of backpropagation by $3P$, ignoring the activations, and compare with gradient estimation by forward differences, which needs $P + 1$ forward passes. Then take a map $F: \mathbb{R}^{1000} \to \mathbb{R}^{10}$: how many forward-mode runs and how many reverse-mode sweeps give its whole Jacobian?

11. • A scalar linear recurrence $h_t = w h_{t-1} + x_t$ starts at $h_0 = 0$, with $w = 0.5$, the inputs $x = (1, 0, 0)$ and the loss $L = \frac12 h_3^2$. Compute $\partial L/\partial w$ by [backpropagation through time](/backpropagation-through-time/) as a sum of one term per step, and check it against the closed form of $h_3$. What does truncation to the last step, $k = 1$, return?

12. • A batch of 30 examples is split for [gradient accumulation](/gradient-accumulation/) into micro-batches of 8, 8, 8 and 6 examples, whose mean gradients for one weight are 1, 2, 3 and 4. Give the gradient of the whole batch, and the value that a loop computes if it averages the four micro-batch means with equal weights. With [gradient clipping](/gradient-clipping/) at $c = 2$, what should the loop pass to the optimizer?

13. • Binomial [checkpointing](/gradient-checkpointing/) with $c$ checkpoints, where each step is recomputed at most $r$ times, can reverse a chain of up to $\binom{c + r}{c}$ steps. For a chain of 1000 steps, find the least $r$ for $c = 5$ and for $c = 10$.

14. • [Adafactor](/adafactor/) replaces the second-moment matrix $V$ of an $n \times m$ weight matrix by $\hat V = R\,C/(\mathbf{1}^\top R)$, with $R$ the column of row sums and $C$ the row of column sums. Compute $\hat V$ for $V = \begin{pmatrix} 1 & 4 \\ 2 & 8 \end{pmatrix}$ and for $V = I_2$. For a $4096 \times 4096$ matrix in 32-bit floats, compare the memory of Adam's two moment buffers with the memory of Adafactor's factored second moment.

15. • Run one step of [sharpness-aware minimization](/sharpness-aware-minimization/) with $\rho = 0.1$ on $L(w) = \frac12(10 w_1^2 + w_2^2)$ at $w = (1, 1)$. Give the perturbation $\hat\epsilon$, the gradient that SAM passes to the base optimizer, and $L(w + \hat\epsilon)$ compared with the first-order estimate $L(w) + \rho\|\nabla L(w)\|$.

16. • Take the [focal loss](/focal-loss/) with $\gamma = 2$ and $\alpha = 1$. Compute it and the cross-entropy for $p_t = 0.9$ and $p_t = 0.1$. An image has 10,000 easy background boxes with $p_t = 0.99$ and 10 hard boxes with $p_t = 0.3$. Give the total of each group under the cross-entropy and under the focal loss.

17. • A teacher has the logits $(3, 1, 0)$. Give its softmax at temperature $T = 1$ and at $T = 4$, as used in [knowledge distillation](/knowledge-distillation/). By what factor does the probability of the second class exceed that of the third at each temperature?

18. • [Weight normalization](/weight-normalization/) writes $w = g\,v/\|v\|$. Take $v = (3, 4)$, $g = 2$ and $\nabla_w L = (1, 0)$. Give $w$, $\partial L/\partial g$ and $\nabla_v L$, and check that $\nabla_v L$ is orthogonal to $v$. After a gradient step on $v$ with $\eta = 1$, what is $\|v\|^2$?

19. • In IEEE 754 half precision, the smallest positive subnormal is $2^{-24}$, the smallest positive normal number is $2^{-14}$ and the largest finite number is 65504. A gradient entry is $10^{-8}$. What does it become in FP16 with round to nearest, and what does it become after a loss scale of $2^{16}$? If the largest gradient entry is 10, what is the largest power-of-two scale that causes no overflow? These are the numbers behind [mixed precision training](/mixed-precision-training/).

20. • A linear classifier has $w = (2, -1, 0.5)$, no bias and the logistic loss $\log(1 + e^{-y w^\top x})$. For $x = (1, 1, 2)$ and $y = +1$, find the worst perturbation in the $\ell_\infty$ ball of radius $\epsilon = 0.1$, the worst margin, and the loss before and after the attack, as in [adversarial training](/adversarial-training/).

21. • Successive halving, a method of [hyperparameter tuning](/hyperparameter-tuning/), starts 27 configurations with a budget of 1 epoch each, keeps the best third, and triples the budget, until one configuration has trained for 27 epochs. Count the total epochs, and compare with training all 27 configurations for 27 epochs.

22. • Compare Adam and [AMSGrad](/amsgrad/) in the form without bias correction, with $\beta_1 = 0$, $\beta_2 = 0.5$ and $\alpha = 0.1$, on one weight that sees the gradients $10, 1, 1, 1$. Give $v_t$, the AMSGrad maximum $\hat v_t$, and the step of each method at each of the four steps.

23. • Fit $y \approx w x$ to the points $(1, 2)$, $(2, 4)$ and $(3, 7)$ with inverted dropout of keep probability $p$ on the input. Show that the minimizer of the expected squared loss is $p$ times the least squares weight, and give both weights for $p = 0.5$.

24. ★ A restricted Boltzmann machine has one binary visible unit $v$ and one binary hidden unit $h$, no biases, and $p(v, h) \propto e^{w v h}$. The data always has $v = 1$, and $w = \ln 3$. Compute the exact gradient of the log-likelihood $\log p(v = 1)$ in $w$. Then compute the expected update of [contrastive divergence](/contrastive-divergence/) with one Gibbs step, using $v_0\, p(h = 1 \mid v_0)$ as the positive statistic and $v_1\, p(h = 1 \mid v_1)$ as the negative one. How large is the bias?

25. ★ (a) A layer of a network has 1023 inputs plus a bias, so the extended input $\bar a$ has length 1024, and 4096 outputs. Count the entries of its exact Fisher block and of the two factors that [K-FAC](/kronecker-factored-approximate-curvature/) keeps. (b) Take $\bar A = \mathrm{diag}(1, 2)$, $G = \mathrm{diag}(4, 1)$ and $\nabla_W h = \begin{pmatrix} 4 & 2 \\ 1 & 6 \end{pmatrix}$. Compute $X = G^{-1} \nabla_W h\, \bar A^{-1}$ and check that $G X \bar A^\top = \nabla_W h$.

26. ★ Let $f(x; w, v) = v\,\mathrm{relu}(w x)$ with $(w, v) = (1, 2)$. Compute the [neural tangent kernel](/neural-tangent-kernel/) values $\Theta(1, 1)$, $\Theta(1, 3)$ and $\Theta(3, 3)$. Take one gradient step with $\eta = 0.01$ on the loss $\frac12 f(1)^2$, the squared loss of the example $(1, 0)$. Compare the true changes of $f(1)$ and $f(3)$ with the kernel prediction $-\eta\, \Theta(x, 1)\, f(1)$.

27. ★ [Early stopping](/early-stopping/) of gradient descent from 0 on least squares applies the filter $g_t(s) = (1 - (1 - \eta s)^t)/s$, and ridge regression applies $r_\lambda(s) = 1/(s + \lambda)$; for $\lambda = 1/(\eta t)$ and $0 \le \eta s \le 1$, $r_\lambda \le g_t \le 2 r_\lambda$. Show that the ratio $g_t/r_\lambda$ equals 2 at $\eta s = 1$ and $t = 1$. Then let $\eta s \to 0$ with $u = t\eta s$ fixed, find the limit of the ratio as a function of $u$, and find its largest value numerically.

28. ★ A weight vector $w$ feeds a batch normalization layer, so the loss is $L(w) = F(w/\|w\|)$ with $\epsilon = 0$. Show that one step $w' = w - \eta \nabla L(w)$ moves $u = w/\|w\|$, to first order, by $-(\eta/\|w\|^2)(I - u u^\top)\nabla F(u)$. With $\eta = 0.1$, give the effective step size on $u$ for $\|w\| = 2$ and for $\|w\| = 1$. Without [weight decay](/weight-decay/), with $\|w\| = 1$ and $\|\nabla L(w)\| = 0.5$, what is $\|w'\|$?
