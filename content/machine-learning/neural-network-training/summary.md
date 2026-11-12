## What to remember

- [Backpropagation](/backpropagation/) is the reverse mode of [automatic differentiation](/automatic-differentiation/) on a network. With $\delta_l = (W_{l+1}^\top \delta_{l+1}) \odot f'(z_l)$ and $\partial \ell/\partial W_l = \delta_l a_{l-1}^\top$, it returns every partial derivative in at most $3P + O(N)$ multiply-adds for $P$ weights and $N$ units, on every input; finite differences need $\Theta(P^2)$. A central-difference [check](/gradient-checking/) with $h \approx \varepsilon^{1/3}$ has error about $\varepsilon^{2/3}$.
- Reverse mode keeps the forward values, $\Theta(TH)$ numbers for [backpropagation through time](/backpropagation-through-time/) over $T$ steps with $H$ hidden units. [Checkpointing](/gradient-checkpointing/) with segments of $k = \lceil \sqrt n \rceil$ layers keeps at most $2\lceil \sqrt n \rceil - 1$ states for $n - \lceil n/k \rceil$ extra layer evaluations.
- The gradient at layer $k$ obeys $\|\partial \ell/\partial a_k\| \le \prod_{l > k} \gamma\, \sigma_{\max}(W_l)\, \|\partial \ell/\partial a_L\|$ with $\gamma = \sup |f'|$, $1/4$ for the sigmoid and 1 for tanh. It [vanishes](/vanishing-gradient-problem/) geometrically when every $\sigma_{\max}(W_l) < 1/\gamma$, and it can [explode](/exploding-gradient-problem/) only if some $\sigma_{\max}(W_l) > 1/\gamma$.
- [He initialization](/he-initialization/), $\operatorname{Var}(W) = 2/n_{\mathrm{in}}$, keeps the forward mean square constant through ReLU layers, because $\mathbb{E}[\mathrm{relu}(z)^2] = \tfrac12 \mathbb{E}[z^2]$ for symmetric $z$; the backward pass is then off by $n_L/n_1$. [Xavier initialization](/xavier-initialization/), $2/(n_{\mathrm{in}} + n_{\mathrm{out}})$, balances the two directions and satisfies both only when the widths are equal.
- [Batch](/batch-normalization/) and [layer normalization](/layer-normalization/) with $\epsilon = 0$ give the same output for $W$ and $aW$, $a > 0$, and the gradient at $aW$ is $1/a$ times the gradient at $W$. On such weights, [weight decay](/weight-decay/) changes the effective step size, not the function.
- Weight decay equals an L2 penalty for plain SGD with $\lambda = \alpha\lambda'$, and differs from it under momentum or a non-scalar preconditioner; [AdamW](/adamw/) uses the decoupled form. [AMSGrad](/amsgrad/) has sublinear regret on online convex problems.
- Some regularizers are exact in a model. In expectation over the masks, input [dropout](/dropout/) on linear regression adds the penalty $\frac{1-p}{p} \sum_j w_j^2 \sum_i x_{ij}^2$. [Early stopping](/early-stopping/) of gradient descent from 0 on least squares shrinks each eigendirection within a factor 2 of ridge regression with $\lambda = 1/(\eta t)$, when $\eta s \le 1$ for every eigenvalue $s$. For a deep network neither is an exact penalty.
- At infinite width in the NTK parameterization, gradient flow on squared loss is kernel regression with a fixed kernel ([neural tangent kernel](/neural-tangent-kernel/)). [Double descent](/double-descent/) is exact for minimum-norm least squares with Gaussian features, with a peak at $p = n$.

| Method | What it changes | Extra state | Gradients per step | Guarantee in the entry |
|---|---|---|---|---|
| AdamW | Adam with decoupled decay | $2d$ | 1 | none for convergence |
| AMSGrad | divides by $\max_{s \le t} v_s$ | $3d$ | 1 | sublinear regret, online convex, $\beta_1 < \sqrt{\beta_2}$ |
| [RAdam](/radam/) | Adam step times $r_t \le 1$ | $2d$ | 1 | a variance analysis, no convergence theorem |
| [Adafactor](/adafactor/) | factored second moments | $n + m$ per $n \times m$ matrix | 1 | none |
| [LARS](/layer-wise-adaptive-rate-scaling/) | per-layer rate $\propto \lVert w \rVert/\lVert g \rVert$ | $d$ (momentum) | 1 | stationary point, smooth nonconvex |
| [LAMB](/lamb/) | Adam direction with a per-layer trust ratio | $2d$ | 1 | stationary point, smooth nonconvex, $\beta_1 = 0$, no decay |
| [K-FAC](/kronecker-factored-approximate-curvature/) | approximate natural gradient | $O(d_{\mathrm{in}}^2 + d_{\mathrm{out}}^2)$ per layer | 1, plus a backward pass with sampled targets | none |
| [SAM](/sharpness-aware-minimization/) | gradient taken at $w + \rho g/\lVert g \rVert$ | base optimizer plus $d$ | 2 | a PAC-Bayes bound as motivation, no convergence result |

: Update rules of the chapter for $d$ weights. The extra state counts numbers kept besides the weights. The stationary-point results for LARS and LAMB are Theorems 2 and 3 of the LAMB paper, under its assumptions.

## Choosing a method

Start from a standard loop and change one thing at a time: He initialization for ReLU networks, batch normalization in convolutional networks, layer normalization in transformers, and SGD with momentum or AdamW with a short warmup and a cosine or step decay. Clip the global gradient norm when the loss spikes. Check every new layer against central differences in double precision before training with it.

When memory is the limit, use checkpointing, mixed precision, gradient accumulation, or Adafactor for the optimizer state. For batches in the tens of thousands, LARS and LAMB have the reported results. For overfitting, try data augmentation and early stopping first, then dropout and label smoothing. For a few hard examples among many easy ones, use the focal loss. For a smaller model, use distillation or pruning with fine-tuning. Tune the learning rate first, with random search or Hyperband rather than a grid.
