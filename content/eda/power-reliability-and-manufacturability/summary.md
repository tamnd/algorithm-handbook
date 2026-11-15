## What to remember

- Dynamic power is $P = \alpha_{0 \to 1} C V^2 f$, with $\alpha_{0 \to 1}$ the rising transitions per cycle. With zero delay and stationary values the toggle rate is $\alpha = 2p(1-p)(1-\rho)$; glitches can push the true rate above 1.
- Signal probability propagation and transition density are linear time and exact only for independent inputs without reconvergent fanout. On $ab + ac$ with fair inputs the gate-by-gate value is $7/16$ against the true $3/8$, and the error has no fixed sign. Exact signal probability is #P-hard.
- Monte Carlo power estimation stops when $z s / \sqrt N < \varepsilon \bar x$; its coverage is only asymptotic.
- A power grid is $G x = i$ with $G$ a symmetric positive definite M-matrix, so $G^{-1} \ge 0$ and drops grow with every load current. Random walks are unbiased at single nodes, the one-pass multigrid-like solver is an approximation, and vectorless verification is one exact linear program per node.
- Decoupling capacitance only delays a drop and cannot fix a DC drop. The charge rule $c = Q / x_{\max}$ is safe at one node but too large (20 nF against 14.4 nF in the one-node example).
- Devgan's metric $V_i = \sum_k R_{ik} I_k$ is a proved upper bound on the noise peak of an RC tree for aggressor slopes at most $s$, tight for infinitely long ramps.
- Black's equation, the Blech product $(jL)_c$, the reaction-diffusion power law of NBTI and all the yield models are empirical. For mean fault count $\lambda$, Poisson gives $e^{-\lambda}$, Murphy $((1 - e^{-\lambda})/\lambda)^2$ and the negative binomial $(1 + \lambda/\alpha)^{-\alpha}$; at $\lambda = 1$ they give 0.368, 0.400 and 0.5 for $\alpha = 1$. Spread in defect density raises yield above Poisson for the same mean.
- Critical area is a union, not a sum, of per-pair areas; for two parallel wires and square defects it is $(L + 2r)(2r - s)^+$. The Voronoi method finds it for all sizes at once from the $L_\infty$ distance to the second-nearest net.
- The Hopkins cross coefficients form a Hermitian positive semidefinite matrix; keeping its $K$ largest eigenvalues gives the sum of coherent systems, with image error in $[0, \lambda_{K+1} \|u\|^2]$. Inverse lithography optimizes a nonconvex cost through it and finds local optima.

| Method | Problem | Time | Guarantee |
|---|---|---|---|
| Signal probability propagation | node probabilities | $O(G + P)$ | exact without reconvergence |
| BDD activity estimation | exact average switching | $O(P B^2)$ | exact for independent input pairs |
| Monte Carlo power estimation | mean power | $O(NT(G + P))$ | asymptotic confidence interval |
| Clustered voltage scaling | low-supply gates | $O(n(n + m))$ | largest feasible low set, additive delays |
| Multigrid-like grid solver | DC drop | $O(N + M^3)$ | approximate, one pass |
| Random walk grid solver | drop at one node | $O(N + E + W S \log d)$ expected | unbiased estimate |
| Vectorless verification | worst-case drop | one LP per node | exact under the bounds |
| Devgan metric | noise peak on an RC tree | $O(n + m)$ | upper bound |
| Sum of coherent systems | aerial image | $O(K n \log n)$ per image | error at most $\lambda_{K+1}$ per unit mask energy |

: Main methods of the chapter. $G$ gates, $P$ gate pins, $B$ BDD size, $N$ samples of $T$ cycles, $n$ gates or nodes, $m$ pins or coupling capacitors, $M$ coarse nodes, $E$ grid edges, $W$ walks of mean length $S$, $d$ largest degree, $K$ kernels.

## Choosing a method

For activity, use signal probabilities or transition densities for a fast rough number, and expect errors where signals reconverge. Use BDDs when they stay small, and Monte Carlo simulation with a gate-delay model when glitches matter. RTL macromodels serve early estimates, for inputs like their training data.

Clock gating and operand isolation preserve behavior when the enable condition is right. Power gating pays off only for idle periods longer than the break-even time. Threshold and voltage assignment spend timing slack found by timing analysis.

For a grid, solve the full system when it fits, use the multigrid-like method for a fast approximate map, random walks for a few nodes, and vectorless verification when currents are known only by bounds. Screen noise with the Devgan bound and simulate only the nets that fail it.

For yield, compute critical area from the layout and fit the yield model to the fab's data; the negative binomial model with a fitted $\alpha$ is the usual choice when defects cluster. For lithography, a few coherent kernels are the standard fast image model, and inverse lithography is used where model-based correction fails.
