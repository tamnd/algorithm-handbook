A pendulum pushed far from rest, a ball held under an electromagnet, a quadrotor that flips: in each case
the linear model of an earlier chapter holds only near one operating point, and a controller designed from
it may fail once the state moves away. Nonlinear control designs feedback for the nonlinear model itself.
The magnetic levitation example of [IDA-PBC](/ida-pbc/) lifts the ball from height $0.3$ to $0.5$ with an
energy that decreases along every motion in a large set, not just near the target. The double integrator
with a disturbance $0.5 \sin 2t$ in [sliding mode control](/sliding-mode-control/) reaches its sliding
surface within one time unit, whatever the disturbance does, because the switching gain exceeds the
disturbance bound by a margin.

Most methods of the chapter take a control-affine model $\dot x = f(x) + g(x) u$ and answer one of three
questions: can the system be made to look linear, can a Lyapunov function be built for it together with
the feedback, and what does the method cost in robustness, smoothness or knowledge of the model. Each
result holds for the model it was proved for. Feedback linearization cancels terms exactly and gives no
robustness margin. Sliding mode control is robust to matched uncertainty but chatters. Lyapunov's direct
method gives sufficient conditions only.

## What the chapter covers

1. **Derivatives along vector fields.** The [Lie derivative](/lie-derivative/), the
   [Lie bracket](/lie-bracket/), the [relative degree](/relative-degree/) and the
   [zero dynamics](/zero-dynamics/): the language of the rest of the chapter.
2. **Exact linearization by feedback.** [Input-output linearization](/input-output-linearization/) makes
   $y^{(r)} = v$; [feedback linearization](/feedback-linearization/) makes the whole state linear when the
   [conditions for feedback linearizability](/feedback-linearizability-conditions/) hold;
   [differential flatness](/differential-flatness/) turns trajectory planning into the choice of a curve.
3. **Control Lyapunov functions and the limits of stabilization.** A
   [control Lyapunov function](/control-lyapunov-function/) gives a feedback through
   [Sontag's universal formula](/sontag-universal-formula/), and [Artstein's theorem](/artstein-sontag-theorem/)
   says when one exists. The [Lie algebra rank condition](/lie-algebra-rank-condition/) and
   [Brockett's condition](/brockett-condition/) show that reaching a set of states and stabilizing a point
   are different problems.
4. **Backstepping.** [Backstepping](/backstepping/) builds the Lyapunov function and the feedback step by
   step; [adaptive backstepping](/adaptive-backstepping/) handles unknown constant parameters.
5. **Sliding modes.** [Sliding mode control](/sliding-mode-control/), the [chattering](/chattering/) it
   causes, and the [super-twisting algorithm](/super-twisting-algorithm/) that makes the control continuous.
6. **Observers and disturbance estimation.** The [high-gain observer](/high-gain-observer/), the
   [sliding mode observer](/sliding-mode-observer/) and
   [active disturbance rejection control](/active-disturbance-rejection-control/).
7. **Energy and passivity.** [Port-Hamiltonian systems](/port-hamiltonian-system/),
   [passivity-based control](/passivity-based-control/) and [IDA-PBC](/ida-pbc/).
8. **Two time scales.** The [averaging method](/averaging-method/) and the
   [singular perturbation method](/singular-perturbation-method/).
9. **Safety with barrier functions.** The [control barrier function](/control-barrier-function/) and the
   [safety filter](/cbf-safety-filter/) that enforces it with a quadratic program.

## A first reading

Read these entries in order:

1. [Lie derivative](/lie-derivative/)
2. [Relative degree](/relative-degree/)
3. [Zero dynamics](/zero-dynamics/)
4. [Input-output linearization](/input-output-linearization/)
5. [Feedback linearization](/feedback-linearization/)
6. [Control Lyapunov function](/control-lyapunov-function/)
7. [Sontag's universal formula](/sontag-universal-formula/)
8. [Backstepping](/backstepping/)
9. [Sliding mode control](/sliding-mode-control/)
10. [Chattering](/chattering/)
11. [High-gain observer](/high-gain-observer/)
12. [Passivity-based control](/passivity-based-control/)
13. [Control barrier function](/control-barrier-function/)
14. [Safety filter](/cbf-safety-filter/)

The theorems of the third group (Artstein, the rank condition, Brockett), the conditions for feedback
linearizability, flatness, the adaptive and higher order variants, and the two time-scale methods can wait
until a design needs them. [Lie brackets](/lie-bracket/) are needed only for the linearizability
conditions and the rank condition. Read [averaging](/averaging-method/) and
[singular perturbation](/singular-perturbation-method/) before the proofs of the high-gain observer, which
use the same ideas.

## Before you start

The chapter assumes the stability theory of chapter 36.2: [Lyapunov functions](/lyapunov-function/),
[Lyapunov's direct method](/lyapunov-direct-method/), the
[LaSalle invariance principle](/lasalle-invariance-principle/), [passivity](/passivity/) and the
[describing function](/describing-function/). From chapter 36.1 it uses the
[control-affine system](/control-affine-system/) and the [Jacobian linearization](/jacobian-linearization/);
from chapter 36.4, [controllability](/controllability/), the
[controllable canonical form](/controllable-canonical-form/) and the [Luenberger observer](/luenberger-observer/).

From other volumes you need existence and uniqueness of solutions, from the
[Picard-Lindelöf theorem](/picard-lindelof-theorem/) and the [Lipschitz condition](/lipschitz-condition/),
and [Gronwall's inequality](/gronwall-inequality/) for the averaging and perturbation bounds, all in
Volume 12, as are [Hamiltonian systems](/hamiltonian-systems/). The [gradient](/gradient/),
[quadratic programming](/quadratic-programming/) and the [KKT conditions](/kkt-conditions/) of Volume 15
appear in the safety filter. [Transfer functions](/transfer-function/) from Volume 28 help with the linear
special cases of relative degree and zero dynamics.

Some examples come from robotics: computed torque control, the unicycle and differential drive models,
and the flat outputs of a quadrotor. They are robotics topics and are only named here. Many entries report
simulations with a stated method and step size, and their numbers depend on that step.
