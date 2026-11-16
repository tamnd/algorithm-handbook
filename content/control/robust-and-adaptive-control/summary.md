## What to remember

- The [H-infinity norm](/h-infinity-norm/) is the peak of $\bar\sigma(G(j\omega))$ over frequency. It is computed to any accuracy by a Hamiltonian eigenvalue test: for stable $A$ and $\gamma > \bar\sigma(D)$, $\gamma$ is above the norm exactly when the Hamiltonian $H_\gamma$ has no eigenvalue on the imaginary axis ([H-infinity norm computation](/h-infinity-norm-computation/)).
- The [small-gain theorem](/small-gain-theorem/) and the norm-bounded [uncertainty models](/model-uncertainty/) give sufficient conditions. For a full complex block the condition is also necessary; for a diagonal or real structure it can be far from tight, and the [structured singular value](/structured-singular-value/) is the exact measure.
- Exact $\mu$ is [NP-hard](/np-hard/) for real and mixed structures and for some complex ones, so [mu analysis](/mu-analysis/) computes a lower bound by power iteration and an upper bound by D-scaling, an LMI. If P differs from NP, no polynomial algorithm gives exact $\mu$ in general.
- Parametric robustness has exact finite tests: four polynomials decide an interval family ([Kharitonov's theorem](/kharitonov-theorem/)), and the edges decide a polytope of polynomials ([edge theorem](/edge-theorem/)). Corners alone do not decide a polytope.
- The [H-infinity control problem](/h-infinity-control-problem/) is solved exactly for a given $\gamma$, by two Riccati equations and a coupling condition $\rho(XY) < \gamma^2$ ([DGKF synthesis](/dgkf-h-infinity-synthesis/)) or by three LMIs ([LMI synthesis](/lmi-h-infinity-synthesis/)). Both give a controller of the plant's order. Adding uncertainty structure, [D-K iteration](/dk-iteration/) alternates the two steps and has no global guarantee.
- Every stabilizing controller is $C = (Y + MQ)(X - NQ)^{-1}$ for a stable proper $Q$ ([Youla parametrization](/youla-parametrization/)), and the closed-loop maps are affine in $Q$. This turns synthesis into a convex problem in $Q$.
- [Model reference adaptive control](/model-reference-adaptive-control/) and the [self-tuning regulator](/self-tuning-regulator/) have stability proofs for their ideal model: bounded signals and a tracking error that tends to zero. The parameters converge only under [persistent excitation](/persistent-excitation/), and unmodelled dynamics can destroy stability ([Rohrs counterexample](/rohrs-counterexample/)). [Parameter projection](/parameter-projection/) and [sigma modification](/sigma-modification/) keep the estimates bounded under bounded disturbances, at the cost of a bias or a known parameter bound.
- [Gain scheduling](/gain-scheduling/) has no general guarantee. [Quadratic stability](/quadratic-stability/) with one Lyapunov matrix for all parameter values is a sufficient condition that holds for arbitrarily fast variation.

| Method | Question it answers | Exact or bound | Cost |
|---|---|---|---|
| Hamiltonian test with bisection | $\|G\|_\infty$ | certified interval | $O((n+m+p)^3)$ per test |
| Kharitonov | stability of an interval polynomial | exact | 4 Hurwitz tests |
| Edge theorem | stability of a polytope of polynomials | exact | one segment test per edge |
| $\mu$ bounds | robust stability with structure | lower and upper bounds | one LMI per frequency |
| DGKF synthesis | is $\gamma$ achievable | exact, needs rank assumptions | two Riccati equations per $\gamma$ |
| LMI synthesis | optimal $\gamma$ | exact up to solver tolerance | SDP with about $n^2$ variables |
| D-K iteration | $\mu$-synthesis | local, no guarantee | repeated synthesis and fits |
| MRAC | tracking with unknown gains | Lyapunov proof, ideal model | $O(n^2)$ per step |
| Self-tuning regulator | regulation with unknown ARX model | convergence under assumptions | $O(d^2)$ per sample |

: The main methods of the chapter, what they decide, and their cost as stated in the entries; $n$ is the state dimension, $m$ and $p$ the input and output sizes, $d$ the number of estimated parameters.

## Choosing a method

To check a fixed design, compute $\|T\|_\infty$ or the H2 norm, then ask what the uncertainty looks like. A disc of frequency responses calls for the small-gain test with a weight. A few real parameters entering the coefficients call for Kharitonov or the edge theorem. Uncertain parameters in several places of a state model call for an [LFT](/linear-fractional-transformation/) and $\mu$ bounds; close bounds settle the question.

To design, start with [mixed sensitivity](/mixed-sensitivity-design/) and DGKF when the plant meets the rank assumptions, and use LMI synthesis when it does not or when extra constraints such as pole regions must be added. [H-infinity loop shaping](/h-infinity-loop-shaping/) is the choice when a classical shaped loop already exists, and its stability margin connects to the [nu-gap metric](/nu-gap-metric/) for comparing plant models. For structured uncertainty, run D-K iteration from several starts and check the result by $\mu$ analysis.

Adapt only when the plant changes too much for one fixed controller. If the parameter moves with a measured variable, schedule instead. When adaptation is used, bound the estimates with projection or leakage, keep the reference model slow compared with the unmodelled dynamics, and treat parameter convergence as a bonus that needs excitation. [Extremum seeking](/extremum-seeking-control/) suits tuning a static optimum with small probes, and [iterative learning control](/iterative-learning-control/) suits tasks repeated from the same start.
