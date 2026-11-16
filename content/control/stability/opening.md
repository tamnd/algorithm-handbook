Put a motor with transfer function $1/(s(s+1)(s+2))$ in a feedback loop with a gain $K$. The closed loop has the characteristic polynomial $s^3 + 3s^2 + 2s + K$, and the loop is stable exactly when $0 < K < 6$. At $K = 6$ two roots reach the imaginary axis at $\pm j\sqrt 2$ and the loop oscillates; above $6$ the oscillation grows. A short table of cross products, the Routh array, gives this range from the coefficients, without computing a single root. Now give the same loop a friction that depends on the speed, or an actuator that saturates. The model is no longer linear, eigenvalues no longer decide anything, and the question becomes whether some measure of energy goes down along every solution. That is Lyapunov's idea, and most of the chapter grows from it.

Stability is the first thing to check about a control system, before any question of speed or accuracy. It decides whether a speed governor hunts, whether a sampled controller with a delay of one sample keeps its loop at rest, whether a relay in a loop starts an oscillation, and whether a robot arm with an unknown load comes to rest at its target. The chapter gives exact tests where they exist, for linear models, and sufficient tests with proofs everywhere else. It says each time which kind of test it is.

## What the chapter covers

1. **Testing a linear model.** A matrix is [Hurwitz](/hurwitz-matrix/) when every eigenvalue has a negative real part. The [Routh array](/routh-array/) counts the roots of a polynomial in the right half plane in $O(n^2)$ operations, and the [Routh-Hurwitz criterion](/routh-hurwitz-criterion/) states the exact conditions. The [Jury test](/jury-stability-test/) does the same for the unit circle.
2. **What stability means.** [Lyapunov stability](/lyapunov-stability/), [asymptotic stability](/asymptotic-stability/) and [exponential stability](/exponential-stability/) are three strengths of one idea. The [region of attraction](/region-of-attraction/) is the set of initial states that converge.
3. **Lyapunov's method.** A [Lyapunov function](/lyapunov-function/) proves stability through [Lyapunov's direct method](/lyapunov-direct-method/) and [LaSalle's invariance principle](/lasalle-invariance-principle/). The [Lyapunov theorem for linear systems](/lyapunov-theorem-for-linear-systems/) and [Lyapunov's indirect method](/lyapunov-indirect-method/) connect the method to eigenvalues. The [converse Lyapunov theorem](/converse-lyapunov-theorem/) and [Barbalat's lemma](/barbalat-lemma/) close the group.
4. **Computing certificates.** [Region of attraction estimation](/region-of-attraction-estimation/), [sum-of-squares programming](/sum-of-squares-programming/) and [contraction analysis](/contraction-analysis/) let a computer find and check the proofs.
5. **Periodic orbits.** A [limit cycle](/limit-cycle/) is an isolated periodic orbit. The [Poincaré-Bendixson theorem](/poincare-bendixson-theorem/) proves that one exists in the plane, and the [describing function](/describing-function/) predicts one in a loop, approximately.
6. **Systems with inputs.** The [small-gain theorem](/small-gain-theorem/), [passivity](/passivity/), [dissipativity](/dissipativity/), the [passivity theorem](/passivity-theorem/), [input-to-state stability](/input-to-state-stability/) and the [ISS small-gain theorem](/iss-small-gain-theorem/) prove a loop stable from properties of its parts.
7. **Absolute stability.** The [Lur'e problem](/lure-problem/) asks for stability with every nonlinearity in a sector. The [KYP lemma](/kalman-yakubovich-popov-lemma/) turns frequency conditions into matrix inequalities, and the [circle criterion](/circle-criterion/) and the [Popov criterion](/popov-criterion/) give sufficient tests.

## A first reading

Read these fifteen entries in order:

1. [Hurwitz matrix](/hurwitz-matrix/)
2. [Routh array](/routh-array/)
3. [Routh-Hurwitz criterion](/routh-hurwitz-criterion/)
4. [Jury stability test](/jury-stability-test/)
5. [Lyapunov stability](/lyapunov-stability/)
6. [Asymptotic stability](/asymptotic-stability/)
7. [Exponential stability](/exponential-stability/)
8. [Lyapunov function](/lyapunov-function/)
9. [Lyapunov's direct method](/lyapunov-direct-method/)
10. [LaSalle's invariance principle](/lasalle-invariance-principle/)
11. [Lyapunov theorem for linear systems](/lyapunov-theorem-for-linear-systems/)
12. [Lyapunov's indirect method](/lyapunov-indirect-method/)
13. [Limit cycle](/limit-cycle/)
14. [Small-gain theorem](/small-gain-theorem/)
15. [Passivity](/passivity/)

The special cases of the Routh array, zero rows and zero leading entries, can wait. Skip at first the converse theorems, Barbalat's lemma, the computational group, and the whole group on absolute stability; they use everything before them. Input-to-state stability and its small-gain theorem are research tools and can come last.

## Before you start

The chapter needs the [eigenvalues](/eigenvalue/) of a matrix, [positive definite matrices](/positive-definite-matrix/), the [Lyapunov equation](/lyapunov-equation/) and [matrix norms](/matrix-norms/), all in Volume 12. From differential equations it needs the [initial value problem](/ode-initial-value-problem/) and the [Lipschitz condition](/lipschitz-condition/), also in Volume 12, which guarantee that solutions exist and are unique. The [characteristic polynomial](/characteristic-polynomial/) is in Volume 11. The [transfer function](/transfer-function/), the [z-transform](/z-transform/) and [BIBO stability](/bibo-stability/) are in Volume 28. The computational group uses [semidefinite programming](/semidefinite-programming/) from Volume 15. From this volume, read the [equilibrium point](/equilibrium-point/) and [Jacobian linearization](/jacobian-linearization/) entries first, and keep the [Nyquist plot](/nyquist-plot/) and the [Nyquist stability criterion](/nyquist-stability-criterion/) at hand for the groups on loops. Calculus in several variables is assumed: gradients, the chain rule along a curve, and compact sets.
