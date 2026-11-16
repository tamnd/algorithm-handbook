A motor turns a load through a gearbox. With the voltage as input and the angle as output, a simple model is $P(s) = 1/(s(s + 1)(s + 2))$: an integrator, because the angle is the integral of the speed, and two lags. Close the loop with a gain $k$, so that the voltage is $k$ times the angle error. With $k = 1$ a unit step of the set point gives an overshoot of 14.5 percent, a peak at 6.1 s and a 2 percent settling time of 12.4 s (a simulation with the Runge-Kutta method of order 4 and the step 0.001 s). The integrator makes the final error zero. With $k = 6$ the closed-loop poles are $\pm j\sqrt 2$ and the linear model oscillates with a constant amplitude. With $k = 10$ the oscillation grows.

This one loop raises most of the questions of the chapter. The [root locus](/root-locus/) shows how the closed-loop poles move as $k$ grows, and it crosses the imaginary axis at $k = 6$. The [Nyquist plot](/nyquist-plot/) of $L = kP$ crosses the negative real axis at $-k/6$, so at $k = 1$ the [gain margin](/gain-margin/) is 6 and the [phase margin](/phase-margin/) is 53.4 degrees. Each margin measures the distance to instability along one direction only. The peak of the [sensitivity function](/sensitivity-function/) is 1.568, so the curve passes within $1/1.568 = 0.638$ of the critical point $-1$, in any direction. What the loop does with a load torque, a ramp of the set point or a saturated amplifier is the subject of [steady-state error](/steady-state-error/), [PID control](/pid-controller/) and [anti-windup](/anti-windup/).

The methods are classical: they work with [transfer functions](/transfer-function/) of one input and one output, and with plots that can be sketched by hand. Some results are exact theorems for linear time-invariant models, such as the [Nyquist stability criterion](/nyquist-stability-criterion/) and the two integral relations of Bode. Others are rules of thumb that a computed response must confirm: the sketching rules of the root locus, the straight-line asymptotes of the [Bode plot](/bode-plot/), the targets for the margins and the [Ziegler-Nichols](/ziegler-nichols-tuning/) tables.

## What the chapter covers

1. **The loop and its responses.** The [feedback control loop](/feedback-control-loop/) and its closed-loop maps, the [second-order system](/second-order-system/) and the [step response specifications](/step-response-specifications/), the [final value theorem](/final-value-theorem/), the steady-state error and the [internal model principle](/internal-model-principle/).
2. **Root locus.** The locus and its angle and magnitude conditions, and the [root locus rules](/root-locus-rules/) for asymptotes, breakaway points, departure angles and imaginary-axis crossings.
3. **Frequency response and stability.** The Bode plot, the Nyquist plot, the Nyquist stability criterion, the gain and phase margins and the [Nichols chart](/nichols-chart/).
4. **Sensitivity and limits of performance.** The sensitivity function, the [complementary sensitivity function](/complementary-sensitivity-function/), the [Bode gain-phase relation](/bode-gain-phase-relation/) and the [Bode sensitivity integral](/bode-sensitivity-integral/).
5. **Compensator design.** The [lead-lag compensator](/lead-lag-compensator/), [loop shaping](/loop-shaping/) and [controller discretization](/controller-discretization/).
6. **PID control and its tuning.** The PID controller, Ziegler-Nichols tuning, [relay autotuning](/relay-autotuning/), [integrator windup](/integrator-windup/), anti-windup and [internal model control](/internal-model-control/).
7. **Control structures.** [Two-degree-of-freedom control](/two-degree-of-freedom-control/), [cascade control](/cascade-control/), [feedforward control](/feedforward-control/), the [Smith predictor](/smith-predictor/) and the [relative gain array](/relative-gain-array/).

## A first reading

Read these in order:

1. feedback control loop, for $S$, $T$ and internal stability;
2. second-order system, for the link between pole positions and the step response;
3. steady-state error, for system type and the error constants;
4. root locus;
5. Bode plot;
6. Nyquist stability criterion, for $Z = N + P$;
7. gain margin and phase margin;
8. sensitivity function, for $M_s$ and its bounds on both margins;
9. lead-lag compensator;
10. PID controller;
11. Ziegler-Nichols tuning;
12. integrator windup.

Skip at first the root locus rules beyond the asymptotes, the two Bode theorems, the internal model principle, controller discretization and the relative gain array. Come back to the Bode theorems before you rely on loop shaping, and to discretization before you put a controller on a computer.

## Before you start

You need the [Laplace transform](/laplace-transform/), [poles and zeros](/poles-and-zeros/) and the [frequency response](/frequency-response/) of a [linear time-invariant system](/linear-time-invariant-system/), with [BIBO stability](/bibo-stability/) and [minimum-phase](/minimum-phase/) systems (Volume 28). Plants with a delay are [time-delay systems](/time-delay-system/), and the step-response tuning rules start from a [process reaction curve](/process-reaction-curve/) (both in chapter 36.1). For the algebraic test of stability, read the [Routh-Hurwitz criterion](/routh-hurwitz-criterion/) in chapter 36.2. The root locus needs [polynomial root finding](/polynomial-root-finding/) (Volume 12), and inverse transforms use [partial fraction decomposition](/partial-fraction-decomposition/) (Volume 11).
