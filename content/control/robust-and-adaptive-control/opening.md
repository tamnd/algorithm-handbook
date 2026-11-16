A controller is designed for a model, and the model is wrong. The mass of a vehicle changes with its load, a
motor heats up, and a flexible mode that the model leaves out rings at a frequency nobody measured. Robust
control keeps one fixed controller and proves that it works for every plant in a described set: a disc of
frequency responses around the nominal one, a box of polynomial coefficients, or a block of uncertain
parameters pulled out into a feedback loop. Adaptive control lets the controller change its gains as data come
in, and proves that the loop stays bounded while it learns, for the plant structure it assumes.

The two meet in one example. For the plant $2/(s+1)$ and the reference model $3/(s+3)$, the standard adaptive
law keeps every signal bounded for every bounded command. Multiply the plant by $229/(s^2 + 30s + 229)$, a
factor with gain 1 at low frequency and poles at $-15 \pm 2j$, and apply the command $0.3 + 1.85\sin 16.1t$. The
feedback gain then drifts, passes the stability limit $-17.03$ after about 20 seconds in simulation, and the loop
goes unstable ([the Rohrs counterexample](/rohrs-counterexample/)). A fixed controller with the starting gains
has a wide margin on the same plant. The tools that repair the adaptive law, bounded parameter sets and leakage,
are tools of robust design.

## What the chapter covers

1. **Norms and matrix inequalities.** The [H-infinity norm](/h-infinity-norm/) is the peak gain over frequency
   and the [H2 norm](/h2-norm/) the energy of the impulse response. [H-infinity norm
   computation](/h-infinity-norm-computation/) certifies the first by a Hamiltonian eigenvalue test, and the
   [bounded real lemma](/bounded-real-lemma/) writes it as a [linear matrix inequality](/linear-matrix-inequality/).
   The [S-procedure](/s-procedure/) adds quadratic constraints to such inequalities.
2. **Uncertainty models and parametric robustness.** [Model uncertainty](/model-uncertainty/) gives the
   additive, multiplicative and coprime factor sets and their small-gain tests. The [Kharitonov
   theorem](/kharitonov-theorem/) and the [edge theorem](/edge-theorem/) decide stability of boxes and polytopes
   of polynomials.
3. **Varying parameters.** [Gain scheduling](/gain-scheduling/) interpolates designs made at frozen operating
   points; [quadratic stability](/quadratic-stability/) and [LPV systems](/lpv-system/) give guarantees for
   parameters that move.
4. **Structured uncertainty.** A [linear fractional transformation](/linear-fractional-transformation/) collects
   all uncertain elements into one block-diagonal $\Delta$, the [structured singular
   value](/structured-singular-value/) measures the margin against it, and [mu analysis](/mu-analysis/) applies it
   to robust stability and performance.
5. **H-infinity synthesis.** The [H-infinity control problem](/h-infinity-control-problem/) is solved exactly by
   [two Riccati equations](/dgkf-h-infinity-synthesis/) or by [LMIs](/lmi-h-infinity-synthesis/). [Mixed
   sensitivity design](/mixed-sensitivity-design/) shapes the loop with weights, and [D-K
   iteration](/dk-iteration/) is the usual heuristic for mu-synthesis.
6. **Coprime factors and the gap.** [Coprime factorization](/coprime-factorization/) leads to the [Youla
   parametrization](/youla-parametrization/) of all stabilizing controllers, to [H-infinity loop
   shaping](/h-infinity-loop-shaping/) and to the [nu-gap metric](/nu-gap-metric/).
7. **Model reference adaptive control.** After the [overview of adaptive control](/adaptive-control/), the
   [MIT rule](/mit-rule/) and [model reference adaptive control](/model-reference-adaptive-control/) give the
   gradient and Lyapunov designs. The Rohrs example, [parameter projection](/parameter-projection/), [sigma
   modification](/sigma-modification/) and [L1 adaptive control](/l1-adaptive-control/) deal with what the ideal
   proofs leave out.
8. **Self-tuning control.** [Certainty equivalence](/certainty-equivalence/) underlies the [self-tuning
   regulator](/self-tuning-regulator/) and [adaptive pole placement](/adaptive-pole-placement/).
9. **Learning from probes and repetition.** [Extremum seeking control](/extremum-seeking-control/) finds the
   optimum of an unknown map with a sine dither, and [iterative learning control](/iterative-learning-control/)
   improves a repeated task trial by trial.

## A first reading

Read these in order:

1. [H-infinity norm](/h-infinity-norm/)
2. [Model uncertainty](/model-uncertainty/)
3. [Kharitonov theorem](/kharitonov-theorem/)
4. [Gain scheduling](/gain-scheduling/)
5. [Linear fractional transformation](/linear-fractional-transformation/)
6. [Structured singular value](/structured-singular-value/)
7. [H-infinity control problem](/h-infinity-control-problem/)
8. [Mixed sensitivity design](/mixed-sensitivity-design/)
9. [Coprime factorization](/coprime-factorization/)
10. [Adaptive control](/adaptive-control/)
11. [MIT rule](/mit-rule/)
12. [Model reference adaptive control](/model-reference-adaptive-control/)
13. [Rohrs counterexample](/rohrs-counterexample/)
14. [Self-tuning regulator](/self-tuning-regulator/)

On a first pass you can skip the proofs of the bounded real lemma and the S-procedure, the edge theorem, LPV
systems, LMI synthesis, D-K iteration, the nu-gap metric, L1 adaptive control and the last group. The two
synthesis pages are worth reading for their scalar examples even when the proofs are skipped: both reach the
same optimal level $1 + \sqrt 3$ on the same plant.

## Before you start

The chapter uses the earlier chapters of this volume throughout: the [Nyquist stability
criterion](/nyquist-stability-criterion/), the [sensitivity function](/sensitivity-function/) and
[loop shaping](/loop-shaping/) from classical control; the [small-gain theorem](/small-gain-theorem/), the
[Routh-Hurwitz criterion](/routh-hurwitz-criterion/), the [Lyapunov theorem for linear
systems](/lyapunov-theorem-for-linear-systems/) and the [Kalman-Yakubovich-Popov
lemma](/kalman-yakubovich-popov-lemma/) from stability; and the [continuous algebraic Riccati
equation](/continuous-algebraic-riccati-equation/) and [LQG control](/lqg-control/) from optimal control.
[Persistent excitation](/persistent-excitation/) comes from the chapter on identification.

From other volumes you need [transfer functions](/transfer-function/), the [Kalman filter](/kalman-filter/) and
the [RLS algorithm](/rls-algorithm/) (Volume 28); the [singular value
decomposition](/singular-value-decomposition/), the [spectral radius](/spectral-radius/), [positive definite
matrices](/positive-definite-matrix/), the [Schur complement](/schur-complement/) and the [Lyapunov
equation](/lyapunov-equation/) (Volume 12); and [gradient descent](/gradient-descent/), [projected gradient
descent](/projected-gradient-descent/) and [semidefinite programming](/semidefinite-programming/) with
[interior-point methods](/interior-point-method/) (Volume 15). The hardness of the structured singular value is
stated in terms of [NP-hard](/np-hard/) problems from Volume 39.
