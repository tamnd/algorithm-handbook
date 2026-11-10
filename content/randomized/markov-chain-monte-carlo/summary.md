## What to remember

- A finite chain that is irreducible and aperiodic has a unique [stationary distribution](/stationary-distribution/) $\pi$, and $\|P^t(x, \cdot) - \pi\|_{TV} \to 0$ from every start, geometrically fast. Time averages converge to $E_\pi f$ with irreducibility alone; that is the [ergodic theorem](/ergodic-theorem/).
- [Detailed balance](/detailed-balance/), $\pi(x)P(x, y) = \pi(y)P(y, x)$, implies $\pi P = \pi$. It is the usual way to prove a sampler correct, one pair of states at a time.
- [Metropolis-Hastings](/metropolis-hastings/) proposes $y$ from $Q(x, \cdot)$ and accepts with probability $\min(1, r)$, where $r = \pi(y)Q(y, x)/(\pi(x)Q(x, y))$. Only ratios of $\pi$ enter, so the normalizing constant is never needed. A rejected step repeats the old state, and that repeat must be counted.
- The [mixing time](/mixing-time/) $t_{mix}$ is the first $t$ with $\max_x\|P^t(x, \cdot) - \pi\|_{TV} \le 1/4$, and $t_{mix}(\varepsilon) \le \lceil\log_2(1/\varepsilon)\rceil\,t_{mix}$. A chain is [rapidly mixing](/rapid-mixing/) when $t_{mix}$ is polynomial in $\log|\Omega|$.
- Bounds on $t_{mix}$ come from coupling, $d(t) \le \Pr[\tau_{couple} > t]$, and from the [spectral gap](/spectral-gap/) $\gamma$, with $t_{rel} = 1/\gamma_*$. The [Cheeger inequality](/cheeger-inequality/) $\Phi_*^2/2 \le \gamma \le 2\Phi_*$ ties the gap to the worst bottleneck, and $t_{mix} \ge 1/(4\Phi_*)$.
- Correlated draws are worth fewer independent ones: $\mathrm{ESS} = n/\tau$ with $\tau = 1 + 2\sum_{k \ge 1}\rho_k$. Thinning a finished run never lowers the variance of its mean.
- No diagnostic computed from a finite run can prove convergence. A chain that never found a mode gives output that passes every test. Only proven mixing bounds, or exact samplers such as [coupling from the past](/coupling-from-the-past/), give guarantees.
- With a gradient, [Hamiltonian Monte Carlo](/hamiltonian-monte-carlo/) makes long moves that are still accepted, because the leapfrog method keeps volume, is reversible and nearly keeps energy. The acceptance is $\min(1, e^{-\Delta H})$.

## The samplers side by side

| Sampler | Needs | Tuning | Main strength | Main weakness |
|---|---|---|---|---|
| [Random-walk Metropolis](/random-walk-metropolis/) | $\tilde\pi(x)$ | step size, aim at acceptance $0.234$ ($0.44$ in one dimension) | works for any target | $O(d)$ steps per independent draw |
| [Independence sampler](/independence-sampler/) | $\tilde\pi(x)$, a proposal $q$ to draw from | the choice of $q$ | $d(t) \le (1 - 1/M)^t$ when $\pi/q \le M$ | not geometrically ergodic when $\pi/q$ is unbounded |
| [Gibbs sampling](/gibbs-sampling/) | the full conditionals | none | no rejections | slow for strongly correlated coordinates |
| [Slice sampling](/slice-sampling/) | $\tilde\pi(x)$ | initial width $w$ | adapts its step to the target | one coordinate or direction at a time |
| [MALA](/metropolis-adjusted-langevin-algorithm/) | $\nabla\log\pi$ | step $h \propto d^{-1/3}$, acceptance $0.574$ | better scaling than a random walk | sensitive to the step size |
| [HMC](/hamiltonian-monte-carlo/) | $\nabla\log\pi$ | step $\varepsilon$, number of steps $L$ | long moves in high dimension | $L$ is hard to choose |
| [NUTS](/no-u-turn-sampler/) | $\nabla\log\pi$ | step $\varepsilon$ only | chooses $L$ by itself | up to $2^D$ gradients per draw |
| [Swendsen-Wang](/swendsen-wang/) | a ferromagnetic Ising or Potts model | none | small $\tau$ near the critical point | only for this class of models |
| [Parallel tempering](/parallel-tempering/) | $\tilde\pi(x)$ | the ladder of temperatures | crosses barriers between modes | runs many copies |
| [Coupling from the past](/coupling-from-the-past/) | a monotone coupling | none | exact draws from $\pi$ | random running time, not interruptible |

: The main samplers of the chapter. $\tilde\pi$ is the target up to a constant, $d$ is the dimension, and $D$ is the depth of the doubling tree of NUTS. The scaling results for random-walk Metropolis and MALA hold for product targets in the limit of high dimension.

## Choosing a method

For a discrete target with easy conditionals, use Gibbs sampling, or [Glauber dynamics](/glauber-dynamics/) on a graph. For a smooth density on $\mathbb R^d$ with a gradient, use HMC or NUTS. Random-walk Metropolis is the fallback when no gradient is available, and it is fine in low dimension. Check the [acceptance rate](/acceptance-probability/) against the scaling results above, but tune for effective samples per unit of work, not for acceptance.

When the coordinates are strongly correlated, change the parametrization or update blocks; a better sampler helps more than a longer run. When the target has well-separated modes, a single local chain can look converged and be wrong. Run several chains from spread-out starts, compare them with the [Gelman-Rubin diagnostic](/gelman-rubin-diagnostic/), and use parallel tempering if they disagree.

Report the [effective sample size](/effective-sample-size/) and the Monte Carlo standard error with every estimate. Discard a [burn-in](/burn-in/) that covers any adaptation of the sampler, and do not [thin](/thinning/) unless storage or the cost of evaluating $f$ forces it. When an exact sample matters and the chain is monotone, use coupling from the past.
