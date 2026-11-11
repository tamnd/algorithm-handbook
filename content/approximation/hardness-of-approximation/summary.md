## What to remember

- **A gap gives a bound on the ratio.** If it is NP-hard to tell instances with $\mathrm{OPT} \le A$ from those with $\mathrm{OPT} \ge B$, then no polynomial algorithm for the minimization problem has ratio $\rho < B/A$ unless P = NP; for a maximization problem with $\mathrm{OPT} \ge c$ against $\mathrm{OPT} < s$, none has ratio $\alpha > s/c$. This is the [gap problem](/gap-problem/).
- **Some gaps need only an NP-complete problem.** Hamiltonian cycle leaves the [general TSP](/general-tsp-inapproximability/) with no ratio at all, partition gives [bin packing](/bin-packing-inapproximability/) the bound $3/2$, dominating set gives [k-center](/k-center-inapproximability/) the bound 2, and small integer optima give the [makespan bounds](/scheduling-makespan-inapproximability/).
- **Reductions carry hardness.** A [gap-preserving reduction](/gap-preserving-reduction/) carries a gap. An [L-reduction](/l-reduction/) with constants $a$ and $b$ turns a ratio $r$ for the target into $1 + ab(r - 1)$ for a minimization source. [APX-complete](/apx-completeness/) problems, such as MAX 3SAT and max cut, have no PTAS unless P = NP.
- **The PCP theorem is a gap for MAX 3SAT.** For some $\varepsilon_0 > 0$ it is NP-hard to tell satisfiable formulas from those in which every assignment leaves an $\varepsilon_0$ fraction of the clauses false. [Håstad's 3-bit PCP](/hastad-3bit-pcp/) makes the gap tight: $7/8 + \varepsilon$ for MAX E3SAT and $1/2 + \varepsilon$ for Max 3LIN.
- **Products amplify gaps.** Graph products turn a constant gap for [clique](/clique-inapproximability/) and [colouring](/graph-coloring-inapproximability/) into a polynomial one. Zuckerman proved $n^{1-\varepsilon}$ hardness for both under P $\ne$ NP.
- **Label cover is the usual starting point.** It is a [two-prover game](/two-prover-one-round-game/) written as a graph, and the [parallel repetition theorem](/parallel-repetition-theorem/) drives its soundness below any constant. With a set system it gives $(1 - \varepsilon)\ln n$ for [set cover](/set-cover-inapproximability/); with the [long code](/long-code/) and a [dictatorship test](/dictatorship-test/) it gives the tight constants.
- **The Unique Games Conjecture settles two-variable problems.** Under it, ratio $\alpha_{\mathrm{GW}} + \varepsilon$, with $\alpha_{\mathrm{GW}} \approx 0.87856$, is hard for [max cut](/max-cut-ugc-hardness/), $2 - \varepsilon$ is hard for vertex cover, and by [Raghavendra's theorem](/raghavendra-theorem/) the basic SDP is optimal for every CSP. Yet unique games have a [subexponential algorithm](/unique-games-subexponential-algorithm/).
- **Stronger assumptions reach further.** Under [Gap-ETH](/gap-eth/), clique has no FPT algorithm with ratio $o(k)$ and dominating set none with any ratio $g(k)$; see [parameterized inapproximability](/parameterized-inapproximability/).

## Thresholds side by side

| Problem | Best known ratio | Hard within | Assumption |
|---|---|---|---|
| General TSP | none | any $\alpha(n)$ computable in polynomial time | P $\ne$ NP |
| Bin packing (absolute) | $3/2$ | $3/2 - \varepsilon$ | P $\ne$ NP |
| $k$-center | 2 | $2 - \varepsilon$ | P $\ne$ NP |
| MAX E3SAT | $7/8$ | $7/8 + \varepsilon$ | P $\ne$ NP |
| Vertex cover | 2 | $\sqrt 2 - \varepsilon$; $2 - \varepsilon$ | P $\ne$ NP; UGC |
| Max cut | $\alpha_{\mathrm{GW}} \approx 0.87856$ | $16/17 + \varepsilon$; $\alpha_{\mathrm{GW}} + \varepsilon$ | P $\ne$ NP; UGC |
| Metric TSP | $3/2 - 10^{-36}$ | $123/122$ | P $\ne$ NP |
| Steiner tree | $\ln 4 + \varepsilon \approx 1.39$ | $96/95$ | P $\ne$ NP |
| Set cover | $\ln n + 1$ | $(1 - \varepsilon)\ln n$ | P $\ne$ NP |
| Maximum coverage | $1 - 1/e$ | $1 - 1/e + \varepsilon$ | P $\ne$ NP |
| $k$-median | $2.675 + \varepsilon$ | $1 + 2/e - \varepsilon$ | P $\ne$ NP |
| Clique | $\text{polylog}\, n / n$ | $n^{-(1 - \varepsilon)}$ | P $\ne$ NP |
| Chromatic number | $n / \text{polylog}\, n$ | $n^{1 - \varepsilon}$ | P $\ne$ NP |
| Multiway cut, 3 terminals | $12/11$ | $12/11 - \varepsilon$ | UGC |
| Sparsest cut (non-uniform) | $O(\sqrt{\log k}\,\log\log k)$ | every constant | UGC |

: Thresholds as stated in the entries. Minimization ratios are $\rho \ge 1$ and maximization ratios $\alpha \le 1$, and $\varepsilon > 0$ is any constant. Where a row gives two bounds, the first holds under P $\ne$ NP and the second under the Unique Games Conjecture. For sparsest cut, $k$ counts the demand pairs.

## Reading a hardness result

- Find the gap first: the two cases that are hard to tell apart, and the quotient of their optima.
- Check the assumption. P $\ne$ NP, NP $\not\subseteq$ DTIME$(n^{O(\log\log n)})$, the UGC and Gap-ETH are different claims.
- Check the kind of ratio. The bin packing bound is for the absolute ratio and leaves asymptotic schemes open.
- For a new problem, look for a gap-preserving reduction from a problem of the same shape: MAX 3SAT or vertex cover for a constant, label cover or set cover for $\ln n$, clique for $n^{1-\varepsilon}$, and unique games for constraints on two variables.
