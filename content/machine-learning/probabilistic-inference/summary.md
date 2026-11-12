## What to remember

- A [Bayesian network](/bayesian-network/) has the joint $\prod_i P(x_i \mid \mathrm{pa}_i)$, and [d-separation](/d-separation/) reads off independences that hold in every distribution that factorizes over the DAG. A [Markov random field](/markov-random-field/) has $p(x) = \frac{1}{Z} \prod_C \psi_C(x_C)$, and graph separation plays the same role.
- Inference is hard in general. [Marginal inference](/marginal-inference/) is #P-complete, deciding $P(X = x) > 0$ is NP-complete ([Cooper](/cooper-theorem/)), and with evidence even an absolute error below $1/2$ is NP-hard ([Dagum and Luby](/dagum-luby-theorem/)).
- [Variable elimination](/variable-elimination/) takes $O((n + m) d^{w+1})$ time for an order of induced width $w$, and the least $w$ over all orders is the treewidth. On a tree, [belief propagation](/belief-propagation/) gives every marginal with two messages per edge.
- On an [HMM](/hidden-markov-model/) with $T$ steps and $N$ states, the [forward](/forward-algorithm/), [Viterbi](/viterbi-algorithm/) and [forward-backward](/forward-backward-algorithm/) algorithms take $\Theta(TN^2)$ time. [EM](/expectation-maximization/) never lowers the likelihood, and at best it reaches a local maximum.
- For every $q$, $\log p(x) = \mathrm{ELBO}(q) + \mathrm{KL}(q \,\|\, p(z \mid x))$. So [mean field](/mean-field-approximation/) gives a lower bound on $\log Z$, and [tree-reweighted belief propagation](/tree-reweighted-belief-propagation/) gives an upper bound at its optimum.
- [Loopy belief propagation](/loopy-belief-propagation/) and [expectation propagation](/expectation-propagation/) have no convergence guarantee, and their answers are not bounds.
- The [particle filter](/particle-filter/) works for any state-space model. At a fixed time its error is of order $c_t/\sqrt N$, and $c_t$ can grow with $t$ unless the model forgets its past. [Annealed importance sampling](/annealed-importance-sampling/) gives an unbiased estimate of $Z$, so the log of the estimate is biased low.
- Conditioning is not intervening. If $Z$ satisfies the [back-door criterion](/backdoor-criterion/), then $P(y \mid \mathrm{do}(x)) = \sum_z P(y \mid x, z) P(z)$.

| Method | Guarantee | Time |
|---|---|---|
| Variable elimination | exact | $O((n + m) d^{w+1})$ |
| [Junction tree algorithm](/junction-tree-algorithm/) | exact | $O(n^3 + (n + m) d^{w+1})$ |
| Loopy belief propagation | none | $O(t m r k^r)$ |
| Mean field | lower bound on $\log Z$ | $O(t(n + e))$ |
| Tree-reweighted BP | upper bound on $\log Z$ at the optimum | $O(n^3 + t m k(k + d))$ |
| Forward, Viterbi, forward-backward | exact | $\Theta(TN^2)$ |
| [RTS smoother](/rauch-tung-striebel-smoother/) | exact for linear Gaussian models | $O(T(n^3 + n^2 m + n m^2 + m^3))$ |
| [Extended](/extended-kalman-filter/) or [unscented](/unscented-kalman-filter/) filter | approximate | $O(T(n^3 + n^2 m + n m^2 + m^3))$ |
| Particle filter | converges as $N \to \infty$ | $O(TN \log N)$ |
| [Likelihood weighting](/likelihood-weighting/) | converges as $s \to \infty$ | $O(s m (p + c))$ |
| Annealed importance sampling | unbiased for $Z$ | $O(s t c)$ |

: The main methods, the kind of guarantee each gives, and the cost stated in its entry. The letters follow the entries: $n$ variables or state dimension, $m$ factors or observation dimension, $d$ or $k$ states, $w$ the induced width, $t$ iterations or annealing steps, $s$ samples, $T$ time steps, $N$ states or particles.

## Choosing a method

Start with the width. If the graph is a tree, or an [elimination ordering](/elimination-ordering/) from the min-fill rule has small induced width, use exact inference: belief propagation on a tree, variable elimination for one query, the junction tree for many. A chain has width one, and the HMM algorithms are variable elimination on a chain. For a linear Gaussian model the Kalman filter and the RTS smoother are exact. For a nonlinear model use the extended or unscented filter when the posterior has one mode, and a particle filter when it may have several, watching the effective sample size.

When the width is large, choose by the guarantee you need. Loopy belief propagation is cheap and often accurate, but check that it converged, and try a [residual schedule](/residual-belief-propagation/) or damping when it does not. To know how far off $\log Z$ can be, run mean field and tree-reweighted messages and report both bounds. For a posterior over parameters, use the closed form when the prior is [conjugate](/conjugate-prior/), [stochastic variational inference](/stochastic-variational-inference/) for large conditionally conjugate models, and [black-box gradients](/black-box-variational-inference/) when nothing has a closed form; each returns a local optimum, and mean field tends to understate the spread. For a question about what an action would do, a better conditional probability does not help: check the back-door criterion, and the [do-calculus](/do-calculus/) when it fails.
