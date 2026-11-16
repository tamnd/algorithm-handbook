A cart on a rail is pushed by a motor. Its position $x_1$ and velocity $x_2$ obey $\dot x_1 = x_2$ and $\dot x_2 = u$, where $u$ is the force divided by the mass. These two numbers are the *state*: together with the future input they fix the whole future motion. Left alone, the cart drifts. Set $u = -2x_1 - 2x_2$, and the matrix of the loop has eigenvalues $-1 \pm i$, so every motion dies out like $e^{-t}$. But a position sensor gives $x_1$ only. A second small system, an observer, runs a copy of the model, compares its predicted position with the measured one, and corrects itself. With the gain $L = (5, 6)$ its error decays with eigenvalues $-2$ and $-3$. Feeding back the estimate instead of the true state gives a loop of order four whose eigenvalues are exactly $-1 \pm i$, $-2$ and $-3$.

This chapter is about that way of working. It describes a linear system by matrices, $\dot x = Ax + Bu$ and $y = Cx + Du$, and asks what feedback and estimation can do with them. Most questions turn into linear algebra: the rank of a matrix, the eigenvalues of $A - BK$, a Lyapunov equation, a chain of subspaces. Because the tests are exact rank tests, they say precisely what is possible for a linear time-invariant model. The chapter also shows where exact answers become fragile in floating point, and what the careful methods do instead.

## What the chapter covers

1. **Controllability and observability.** [Controllability](/controllability/) and [observability](/observability/) are decided by the [Kalman rank condition](/kalman-rank-condition/) and by the [Popov-Belevitch-Hautus test](/popov-belevitch-hautus-test/). The [controllability Gramian](/controllability-gramian/) and [observability Gramian](/observability-gramian/) measure them, and [stabilizability](/stabilizability/) and [detectability](/detectability/) weaken them.
2. **Canonical forms and realization.** The [controllable canonical form](/controllable-canonical-form/) and [observable canonical form](/observable-canonical-form/), the [realization problem](/realization-problem/), the [Kalman decomposition](/kalman-decomposition/) and the [minimal realization theorem](/minimal-realization/).
3. **State feedback and pole placement.** [State feedback](/state-feedback/), the [pole placement problem](/pole-placement-problem/) and [theorem](/pole-placement-theorem/), [Ackermann's formula](/ackermann-formula/), [Kautsky-Nichols-Van Dooren pole placement](/robust-pole-placement/), [integral action](/integral-state-feedback/) and [deadbeat control](/deadbeat-control/).
4. **Observers.** The [state observer](/state-observer/), the [Luenberger observer](/luenberger-observer/), the [reduced-order observer](/reduced-order-observer/), the [separation principle](/separation-principle/), the [unknown input observer](/unknown-input-observer/) and the [disturbance observer](/disturbance-observer/).
5. **Geometric control and output regulation.** [Controlled invariant subspaces](/controlled-invariant-subspace/), the [invariant subspace algorithm](/invariant-subspace-algorithm/), the [disturbance decoupling problem](/disturbance-decoupling-problem/), the [output regulation problem](/output-regulation-problem/) and the [regulator equations](/regulator-equations/).
6. **Model order reduction.** The [problem](/model-order-reduction/), [Hankel singular values](/hankel-singular-values/), the [balanced realization](/balanced-realization/), [balanced truncation](/balanced-truncation/) with its [error bound](/balanced-truncation-error-bound/), and the [iterative rational Krylov algorithm](/iterative-rational-krylov/).

## A first reading

A first pass through the chapter can follow one design from start to end: test the model, place the poles, add an observer, and check the loop.

1. [Controllability](/controllability/)
2. [Observability](/observability/)
3. [Kalman rank condition](/kalman-rank-condition/)
4. [Popov-Belevitch-Hautus test](/popov-belevitch-hautus-test/)
5. [Stabilizability](/stabilizability/)
6. [Controllable canonical form](/controllable-canonical-form/)
7. [State feedback](/state-feedback/)
8. [Pole placement theorem](/pole-placement-theorem/)
9. [Ackermann's formula](/ackermann-formula/)
10. [Integral state feedback](/integral-state-feedback/)
11. [Luenberger observer](/luenberger-observer/)
12. [Separation principle](/separation-principle/)
13. [Kalman decomposition](/kalman-decomposition/)

On a first reading skip the Gramians, the realization entries, the geometric group and model order reduction. Come back to the Gramians and the Hankel singular values before reading balanced truncation, and to the minimal realization theorem before the balanced realization. The geometric group can be read on its own after the first group.

## Before you start

The chapter uses linear algebra throughout. You should know [eigenvalues](/eigenvalue/), the [characteristic polynomial](/characteristic-polynomial/) and the [Cayley-Hamilton theorem](/cayley-hamilton-theorem/), and how to find a rank by [Gaussian elimination](/gaussian-elimination/). From this volume you need the [state-space representation](/state-space-representation/), the [matrix exponential](/matrix-exponential/), [Hurwitz matrices](/hurwitz-matrix/) and the [transfer function matrix](/transfer-function-matrix/). The Gramians are solutions of a [Lyapunov equation](/lyapunov-equation/), and balanced truncation uses the [singular value decomposition](/singular-value-decomposition/). The rank tests assume exact arithmetic, as in the [real RAM](/real-ram/) model; the [floating-point model](/floating-point-model/) and the [condition number](/condition-number/) explain why they need care on a computer. The [Kalman filter](/kalman-filter/) is the observer for noisy measurements, and it is treated with signal processing.
