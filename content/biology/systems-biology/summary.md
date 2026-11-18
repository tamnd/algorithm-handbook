## What to remember

- **One network, three models.** The [stoichiometric matrix](/stoichiometric-matrix/) $S$ gives $dx/dt = S\,v(x)$ under [mass action](/mass-action-kinetics/), the [chemical master equation](/chemical-master-equation/) for counts, and the flux constraint $Sv = 0$ for metabolism.
- **Structure can decide dynamics.** A weakly reversible network of deficiency $\delta = c - l - s = 0$ has, for every choice of positive rate constants, exactly one positive equilibrium in each positive compatibility class, and it is locally asymptotically stable in its class.
- **Steep responses come from cooperativity.** The [Hill function](/hill-equation/) $x^n/(K^n + x^n)$ goes from 10% to 90% over a factor $81^{1/n}$ in $x$. Steep repression makes the [toggle switch](/genetic-toggle-switch/) bistable and the [repressilator](/repressilator/) oscillate; in both, the threshold is where the slope at the symmetric equilibrium crosses a critical value.
- **Boolean models are finite but hard.** A synchronous network on $N$ genes has $2^N$ states, and every trajectory ends in a fixed point or a cycle. Deciding whether a fixed point exists is NP-complete.
- **Exact stochastic simulation.** The [Gillespie algorithm](/gillespie-algorithm/), the [first reaction method](/first-reaction-method/) and the [next reaction method](/next-reaction-method/) sample the same law, the master equation, exactly. They differ in cost per event: $\Theta(m + n)$ with two random numbers, $\Theta(m + n)$ with up to $m$ numbers, and $O(n + d \log m)$ with about one number.
- **Approximations trade exactness for speed.** [Tau-leaping](/tau-leaping/) fires Poisson numbers of reactions per step and can drive counts negative without safeguards. The [chemical Langevin equation](/chemical-langevin-equation/) and the [linear noise approximation](/linear-noise-approximation/) hold for large counts; [moment closure](/moment-closure/) has no error control. The [finite state projection](/finite-state-projection/) bounds its error by the probability that leaves the projected set.
- **Metabolism is optimization.** [FBA](/flux-balance-analysis/) is one LP with a unique optimal value but often many optimal flux vectors; [FVA](/flux-variability-analysis/) measures that spread with $2m + 1$ LPs. [MOMA](/minimization-of-metabolic-adjustment/) is a strictly convex QP with a unique solution. [OptKnock](/optknock/) and [gap filling](/metabolic-network-gap-filling/) are MILPs, and gap filling is NP-hard.
- **Pathways can be exponentially many.** [Elementary flux modes](/elementary-flux-mode/) are the minimal steady pathways; counting them is #P-complete.
- **Inferred networks are hypotheses.** [ARACNE](/aracne/) is exact for tree networks given exact mutual information, [GENIE3](/genie3/) ranks links by random forest importance, and both are judged on benchmarks. [IsoRank](/isorank/) is a heuristic for an NP-hard alignment problem.

## The main methods side by side

| Method | Model | Guarantee | Cost |
|---|---|---|---|
| [Gillespie direct method](/gillespie-algorithm/) | master equation | exact sample paths | $\Theta(m + n)$ per event |
| [Next reaction method](/next-reaction-method/) | master equation | exact sample paths | $O(n + d \log m)$ per event |
| [Tau-leaping](/tau-leaping/) | master equation | approximate; leap condition with $\epsilon$ | $O(mn)$ per leap |
| [Finite state projection](/finite-state-projection/) | master equation | $L^1$ error equals the lost mass | grows as $w^n$ states |
| [Linear noise approximation](/linear-noise-approximation/) | master equation, large volume | Gaussian fluctuations of order $\Omega^{-1/2}$ | a Lyapunov equation |
| [FBA](/flux-balance-analysis/) | steady fluxes, bounds | optimal value exact | one LP |
| [FVA](/flux-variability-analysis/) | steady fluxes, bounds | exact flux ranges | $2m + 1$ LPs |
| [MOMA](/minimization-of-metabolic-adjustment/) | knockout fluxes | unique solution | one QP |
| [OptKnock](/optknock/) | bilevel design | exact for the MILP | one MILP, NP-hard in general |
| [EFM enumeration](/elementary-flux-mode-enumeration/) | flux cone | all modes | output can be exponential |
| [Attractor detection](/boolean-network-attractor-detection/) | Boolean network | all attractors | exponential in the worst case |
| [ARACNE](/aracne/) | mutual information | exact on trees with exact MI | $O(m^2(n + b^2) + m^3)$ |

: Main methods of the chapter. For the simulation methods, $m$ is the number of reactions, $n$ the number of species and $d$ the most reactions that one firing affects; $w$ is the range of each count. For FBA and FVA, $m$ is the number of reactions. For ARACNE, $m$ is the number of genes, $n$ the number of samples and $b$ the number of bins.

## Choosing a method

- For a well-mixed system with large counts, integrate the mass action ODE. When counts are small or noise matters, simulate with the Gillespie algorithm; switch to the next reaction method for large sparse networks, and to tau-leaping when the counts are large but noise still matters.
- For the distribution of a small system, use the finite state projection, which bounds its own error.
- For a genome-scale metabolic model, start with FBA, then run FVA before reading any single flux. Use MOMA for fresh knockouts and OptKnock for strain design.
- Reduce models by quasi-steady state only when the fast and slow timescales are well separated.
- Treat each inferred link as a hypothesis to test.
