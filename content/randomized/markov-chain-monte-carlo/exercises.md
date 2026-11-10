1. ◦ Find the [stationary distribution](/stationary-distribution/) of the chain on $\{0, 1, 2\}$ with
$$P = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/4 & 1/2 & 1/4 \\ 0 & 1/2 & 1/2 \end{pmatrix}.$$
Is the chain irreducible? What is its period? What is the period of the chain with the same off-diagonal pattern but no holding, $P(0, 1) = P(2, 1) = 1$ and $P(1, 0) = P(1, 2) = 1/2$?

2. ◦ Which of these chains are [ergodic](/ergodicity/): the simple random walk on a cycle of 6 vertices, the simple random walk on a cycle of 5 vertices, the lazy random walk on a cycle of 6 vertices, and the chain on $\{0, 1\}$ that always switches? Each one has the uniform distribution as a stationary distribution. For which of them does $P^t(x, \cdot)$ converge to it?

3. ◦ Compute the [total variation distance](/total-variation-distance/) between $\mu = (1/2, 1/4, 1/4, 0)$ and the uniform distribution on four points. Name a set $A$ with $\mu(A) - \nu(A)$ equal to the distance. With what probability do the two draws of a maximal coupling agree?

4. ◦ The target on $\{0, 1, 2\}$ is $\tilde\pi = (1, 2, 1)$. The proposal moves to $x - 1$ or $x + 1$ with probability $1/2$ each, and a move off the ends is rejected. Write down the transition matrix of the [Metropolis-Hastings](/metropolis-hastings/) chain. Which matrix of an earlier exercise is it?

5. ◦ On $\{0, 1\}^2$ the target is $\tilde\pi(00, 01, 10, 11) = (3, 1, 1, 3)$. Give the four conditionals $\Pr(x_1 = 1 \mid x_2)$ and $\Pr(x_2 = 1 \mid x_1)$ used by [Gibbs sampling](/gibbs-sampling/). Under random-scan Gibbs, with what probability does the chain leave state $00$ in one step? Can it reach $11$ in one step?

6. ◦ A [random-walk Metropolis](/random-walk-metropolis/) chain targets $\mathcal N(0, 1)$ with steps $\mathcal N(0, \sigma^2)$. Its stationary acceptance rate is $(2/\pi)\arctan(2/\sigma)$. Find the rate for $\sigma = 2$ and for $\sigma = 2\sqrt3$, and the $\sigma$ that gives the rate $2/3$.

7. ◦ A run of 20 000 draws of a quantity with variance 4 has autocorrelations $\rho_k = 0.8^k$. Compute the integrated autocorrelation time $\tau$, the [effective sample size](/effective-sample-size/) and the Monte Carlo standard error of the mean.

8. ◦ Three chains of length 3 give $(1, 2, 3)$, $(2, 3, 4)$ and $(4, 5, 6)$. Compute $W$, $B$, $\widehat{\operatorname{var}}^+$ and $\hat R$ of the [Gelman-Rubin diagnostic](/gelman-rubin-diagnostic/).

9. ◦ The [hard-core model](/hard-core-model/) on the path $0 - 1 - 2$ has $\pi(I) \propto \lambda^{|I|}$ on the independent sets $I$. For $\lambda = 2$, find the partition function $Z$, the expected size of $I$, and the probabilities that vertex 1 and vertex 0 are occupied.

10. ◦ In [parallel tempering](/parallel-tempering/) with $\pi(x) \propto e^{-E(x)}$, the level with $\beta = 1$ holds a state of energy 5 and the level with $\beta = 0.2$ holds a state of energy 1. Find the probability that the swap of the two states is accepted, and the probability for the reverse swap, from the swapped pair.

11. • A two-state chain has $P(1, 2) = a = 1/3$ and $P(2, 1) = b = 1/6$. Find $\pi$, the second eigenvalue, $d(t)$, $t_{mix}$ and $t_{mix}(1/100)$. For the indicator of state 2, find the asymptotic variance and $\tau$.

12. • Show that if $\pi P = \pi$, then the lazy chain $\tfrac12(I + P)$ also keeps $\pi$, is aperiodic when $P$ is irreducible, and has all its eigenvalues in $[0, 1]$ when $P$ is reversible. Find the eigenvalues and the relaxation time of the lazy walk on the cycle of 4 vertices.

13. • Take $\pi = (1/3, 2/3)$ on two states and the proposal that always switches. Write the chains of the Metropolis-Hastings rule and of Barker's rule $r/(1 + r)$. For the indicator of the second state, compute the asymptotic variance of each and compare it with $\operatorname{Var}_\pi f$. Which theorem does the order agree with?

14. • Is the chain
$$P = \begin{pmatrix} 0 & 1/2 & 1/2 \\ 1/3 & 1/3 & 1/3 \\ 1/4 & 1/4 & 1/2 \end{pmatrix}$$
reversible? Use Kolmogorov's criterion on the cycle $0 \to 1 \to 2 \to 0$, then find $\pi$ from [detailed balance](/detailed-balance/).

15. • Two copies of $K_5$ are joined by one edge, and the chain is the lazy random walk on this graph. Find $\Phi(S)$ when $S$ is one copy of $K_5$; a search over all sets shows that this $S$ is the worst, so $\Phi_* = \Phi(S)$ is the [conductance](/conductance/) of the chain. Give the lower bound on $t_{mix}$ and the interval for $\gamma$ that the [Cheeger inequality](/cheeger-inequality/) gives.

16. • For the lazy walk on the cycle of 8 vertices, find $\Phi_*$ and the exact gap $\gamma = (1 - \cos(2\pi/8))/2$. Check the Cheeger inequality. For the lazy walk on the cycle of $n$ vertices, $n$ even, which side of the inequality has the right order in $n$?

17. • The [independence sampler](/independence-sampler/) targets $\pi = (1/4, 1/4, 1/2)$ with the uniform proposal $q$. Write its transition matrix and its eigenvalues. Compare $d(t)$ with the bound $(1 - 1/M)^t$. How many steps does the bound ask for to reach $1/100$?

18. • The lazy walk on the hypercube $\{0, 1\}^3$ has $t_{rel} = 3$ and $\pi_{min} = 1/8$. Compute the upper bound $\lceil t_{rel}(\tfrac12\log(1/\pi_{min}) + \log(1/(2\varepsilon)))\rceil$ and the lower bound $(t_{rel} - 1)\log(1/(2\varepsilon))$ of the [spectral gap](/spectral-gap/) entry for $\varepsilon = 1/4$. The true value is $t_{mix} = 3$.

19. • A run of 12 000 steps of an AR(1) sequence with $\phi = 1/2$ is [thinned](/thinning/) by 3. Find the effective sample size of the full run and of the thinned run, and the fraction of the information lost.

20. • Take the harmonic oscillator $H(q, p) = (q^2 + p^2)/2$ and one leapfrog step of size $\varepsilon = 1$. From $(q, p) = (1, 0)$ and from $(0, 1)$, find the new point, $\Delta H$ and the acceptance probability $\min(1, e^{-\Delta H})$ that [Hamiltonian Monte Carlo](/hamiltonian-monte-carlo/) would use. Check that $p^2/2 + 3q^2/8$ is the same before and after each step.

21. • For a target on $(0, \infty)$, the proposal $y = xe^{\sigma Z}$ with $Z \sim \mathcal N(0, 1)$ has a log-normal density. Show that $Q(y, x)/Q(x, y) = y/x$. For $\pi(x) = e^{-x}$, find the [acceptance probability](/acceptance-probability/) of the move from $x = 1$ to $y = 2$.

22. • Three coins have the energy $E$ equal to their number of heads, so the density of states is $g = (1, 3, 3, 1)$. A walk flips one coin chosen uniformly and accepts with $\min(1, g(E)/g(E'))$, as [Wang-Landau](/wang-landau/) does once $\hat g = g$. Write the chain on the four energy levels and find its stationary distribution.

23. ★ The two-state chain has $P(0, 1) = a$ and $P(1, 0) = b$ with $a + b \le 1$. Drive it with one uniform $u \in [0, 1)$ per step: go to 1 if $u < a$, go to 0 if $u \ge 1 - b$, and stay otherwise. Show that this update is monotone. For [coupling from the past](/coupling-from-the-past/), find $\Pr[T_* > t]$ and show that the output is 1 with probability exactly $\pi(1) = a/(a + b)$.

24. ★ For the lazy walk on $\{0, 1\}^n$, show that $\chi_S(x) = (-1)^{\sum_{i \in S}x_i}$ is an eigenfunction with eigenvalue $1 - |S|/n$ for every $S \subseteq \{1, \ldots, n\}$. Deduce the spectral gap, the relaxation time and the multiplicity of each eigenvalue.

25. ★ Let $Q$ be symmetric and irreducible on a finite set and let $\pi > 0$ be a target that is not constant. Prove that the Metropolis chain is irreducible and aperiodic. Give an example that shows that the condition on $\pi$ is needed.

26. ★ For the Land of Oz chain with $\pi = (2/5, 1/5, 2/5)$, let $f$ be the indicator of a nice day. Find the asymptotic variance of $\frac1t\sum f(X_s)$ and the autocorrelation time $\tau$. How many independent draws is a run of length $t$ worth?

27. ★ Let $\pi = \mathcal N(0, 1)$. The [MALA](/metropolis-adjusted-langevin-algorithm/) proposal with step $\varepsilon$ is $y \sim \mathcal N(x + \tfrac{\varepsilon^2}{2}\nabla\log\pi(x), \varepsilon^2)$. For $\varepsilon = 1$, compute the acceptance probability from $x = 1$ to $y = 0$ and from $x = 0$ to $y = 1$. Then show that the chain that accepts every proposal has the stationary distribution $\mathcal N(0, 1/(1 - \varepsilon^2/4))$.
