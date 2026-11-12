1. ◦ Let $A$ and $B$ be independent fair bits and $C = A \lor B$. Compute $P(A = 1 \mid C = 1)$, $P(A = 1 \mid C = 1, B = 1)$ and $P(A = 1 \mid C = 1, B = 0)$. Which [conditional independence](/conditional-independence/) holds without $C$ and fails with it, and what is this effect called?

2. ◦ A [Bayesian network](/bayesian-network/) has the edges $A \to C$, $B \to C$, $C \to D$ and $B \to E$. Use [d-separation](/d-separation/) to decide each statement: $A \perp B$; $A \perp B \mid D$; $A \perp E$; $A \perp E \mid C$; $A \perp E \mid \{B, C\}$.

3. ◦ In the network of exercise 2, give the [Markov blanket](/markov-blanket/) of $A$, of $B$ and of $C$. Which edge does moralization add?

4. ◦ In the network of exercise 2 every variable is binary. How many free numbers do the [conditional probability tables](/conditional-probability-table/) hold in total? How many does a table of the full joint distribution of the five variables need?

5. ◦ A [hidden Markov model](/hidden-markov-model/) has the states H and L and the symbols a and b. The initial distribution is $\pi = (0.6, 0.4)$, the transitions are $P(\mathrm H \to \mathrm H) = 0.7$ and $P(\mathrm L \to \mathrm L) = 0.6$, and the emissions are $P(\mathrm a \mid \mathrm H) = 0.8$ and $P(\mathrm a \mid \mathrm L) = 0.3$. Run the [forward algorithm](/forward-algorithm/) on $O = (\mathrm a, \mathrm b, \mathrm a)$: give $\alpha_1, \alpha_2, \alpha_3$ and $P(O)$ as an exact fraction.

6. ◦ For the model and the observations of exercise 5, find the most probable state path with the [Viterbi algorithm](/viterbi-algorithm/) and its joint probability with $O$. Then use the [forward-backward algorithm](/forward-backward-algorithm/) to find the most probable state at each time. Do the two answers agree?

7. ◦ Four particles have the normalized weights $1/2, 1/4, 1/8, 1/8$. Compute the effective sample size $1/\sum_i w_i^2$. Then apply systematic [resampling](/resampling/) with the single uniform draw $U = 0.6$, so the points are $(U + j)/4$ for $j = 0, 1, 2, 3$, and give how many copies of each particle survive.

8. ◦ Two spins $x_1, x_2 \in \{-1, +1\}$ have $p(x) \propto \exp(h_1 x_1 + h_2 x_2 + J x_1 x_2)$ with $h_1 = 0.5$, $h_2 = 0$ and $J = 1$. The [mean-field](/mean-field-approximation/) update is $m_i \leftarrow \tanh(h_i + J m_j)$. Starting from $m = (0, 0)$, do one sweep that updates $m_1$ and then $m_2$, to four decimal places.

9. ◦ Two bits have the joint $P(0,0) = 0.4$, $P(0,1) = 0$, $P(1,0) = 0.25$ and $P(1,1) = 0.35$. Compute both [marginals](/marginal-inference/) and the assignment that maximizes each one separately. What is the probability of that assignment, and what is the [MAP](/map-inference/) assignment of the joint?

10. ◦ An HMM state has self-transition probability 0.9. What is the distribution of the number of steps $d$ the chain stays in it once it enters? Give the mean, the most likely value and $P(d \ge 10)$. Which model in this chapter lets you choose this distribution freely?

11. • A latent bit $z$ has the prior $(1/2, 1/2)$, and the observed $x$ has the likelihoods $p(x \mid z = 0) = 1/5$ and $p(x \mid z = 1) = 3/5$. Compute $p(x)$ and the posterior. Compute the [evidence lower bound](/evidence-lower-bound/) for the uniform $q$, and check that the gap to $\log p(x)$ equals $\mathrm{KL}(q \,\|\, p(z \mid x))$. Which $q$ maximizes the bound?

12. • A coin is flipped ten times. Eight flips were recorded, with six heads, and two records were lost. Write the [expectation-maximization](/expectation-maximization/) update for the head probability $\theta$, run three steps from $\theta_0 = 1/2$, and find the fixed point. By what factor does the error shrink at each step?

13. • A pairwise [Markov random field](/markov-random-field/) is the 5-cycle $A - B - C - D - E - A$. Run [variable elimination](/variable-elimination/) symbolically in the order $A, B, C, D, E$. Which fill edges appear, what is the induced width, and is it the treewidth of the cycle? Build the [junction tree](/junction-tree/) from the cliques and give its separators.

14. • Apply the reduction of [Cooper's theorem](/cooper-theorem/) to $\varphi = (x_1 \lor x_2) \land (\lnot x_1 \lor x_3)$: give $P(Y = 1)$ for the output node $Y$, and say what it tells you about $\varphi$.

15. • A zero-mean [Gaussian graphical model](/gaussian-graphical-model/) has the precision matrix with ones on the diagonal, $\Theta_{12} = \Theta_{23} = -0.4$ and $\Theta_{13} = 0$. Which conditional independence does the graph show? Compute the covariance matrix, the correlations of $(X_1, X_3)$ and of $(X_1, X_2)$, and the partial correlation of $X_1$ and $X_2$ given $X_3$.

16. • A scalar random walk $x_t = x_{t-1} + w_t$ with $\operatorname{Var} w_t = 1$ is observed as $y_t = x_t + v_t$ with $\operatorname{Var} v_t = 4$. Find the steady-state predicted variance and the steady-state gain of the Kalman filter, in closed form and to four decimal places.

17. • A causal graph has the edges $Z_1 \to X$, $Z_1 \to Z_2$, $Z_2 \to Y$, $X \to M$, $M \to Y$ and $Y \to W$. List every subset of $\{Z_1, Z_2, M, W\}$ that satisfies the [back-door criterion](/backdoor-criterion/) for the effect of $X$ on $Y$, and say why each other subset fails.

18. • In a model where $Z$ satisfies the back-door criterion, $P(Z = 1) = 0.3$, $P(X = 1 \mid Z = 0) = 0.2$, $P(X = 1 \mid Z = 1) = 0.8$, and $P(Y = 1 \mid x, z)$ is $0.2, 0.4, 0.5, 0.7$ for $(x, z) = (0,0), (1,0), (0,1), (1,1)$. Compute $P(Y = 1 \mid \mathrm{do}(X = x))$ for both $x$, and the observed $P(Y = 1 \mid X = x)$. Compare the two differences.

19. • Show that $\sum_i \alpha_t(i) \beta_t(i) = P(O)$ for every $t$ in an HMM, where $\alpha$ and $\beta$ are the forward and backward variables. Compute $\beta_1$ and $\beta_2$ for exercise 5 and check the identity at $t = 1$ and $t = 2$.

20. • In a Bayesian network all the evidence variables are roots. Show that every sample of [likelihood weighting](/likelihood-weighting/) gets the same weight, and that the samples are then exact draws from the posterior.

21. • A pairwise model lives on the complete bipartite graph $K_{2,3}$. How many spanning trees does it have? Under the uniform distribution over spanning trees, what is the edge appearance probability $\rho_e$ of each edge, as used by [tree-reweighted belief propagation](/tree-reweighted-belief-propagation/)?

22. ★ Let $p = \mathcal N(\mu, \Sigma)$ with precision $\Lambda = \Sigma^{-1}$. The mean-field Gaussian $q$ that minimizes $\mathrm{KL}(q \,\|\, p)$ has the variances $1/\Lambda_{ii}$. Prove that $1/\Lambda_{ii} \le \Sigma_{ii}$, and find when equality holds.

23. ★ The Ising model on a ring of $n$ spins has $p(x) \propto \exp(J \sum_{i} x_i x_{i+1})$ with $x_{n+1} = x_1$ and no field. Prove that its [partition function](/partition-function/) is $Z = (2\cosh J)^n + (2\sinh J)^n$, and check the formula against direct summation for $n = 3$.

24. ★ The forward-backward algorithm stores all $T$ forward vectors, so it uses $\Theta(TN)$ space. Give a variant that uses $O(N\sqrt T)$ space and still runs in $O(TN^2)$ time, with one extra forward pass, and prove both bounds.

25. ★ Prove that eliminating a simplicial vertex, one whose neighbours form a clique, adds no fill edge. Use this to show that a [chordal graph](/chordal-graph/) with largest clique size $\omega$ has an [elimination ordering](/elimination-ordering/) of induced width $\omega - 1$, and that no ordering does better.

26. ★ Let $X$, $Y$ and $Z$ be disjoint sets of nodes in a DAG. Prove that if $Z$ separates $X$ from $Y$ in the moral graph of the ancestral set of $X \cup Y \cup Z$, then $Z$ d-separates $X$ from $Y$.
