## What to remember

- In the [feedback control loop](/feedback-control-loop/) with $L = PC$, the output is $y = T r + P S d - T n$ with $S = 1/(1 + L)$, $T = L/(1 + L)$ and $S + T = 1$. With $P = b/a$ and $C = n_c/d_c$, internal stability needs $a\,d_c + b\,n_c$ Hurwitz, so an unstable cancellation in $PC$ is never allowed.
- A [second-order system](/second-order-system/) with $0 < \zeta < 1$ has the overshoot $M_p = e^{-\zeta\pi/\sqrt{1 - \zeta^2}}$ and the peak time $\pi/(\omega_n\sqrt{1 - \zeta^2})$. The settling time $4/(\zeta\omega_n)$ and dominant poles are rules of thumb.
- A stable loop of type 0 has the step error $1/(1 + K_p)$, and one of type 1 the ramp error $1/K_v$; the [final value theorem](/final-value-theorem/) gives these values only for a stable closed loop. The error is zero for every nearby plant exactly when the controller contains the model of the signal ([internal model principle](/internal-model-principle/)).
- The [Nyquist stability criterion](/nyquist-stability-criterion/) $Z = N + P$ is exact for linear time-invariant models. The gain margin $1/|L(j\omega_{pc})|$, the phase margin $180 + \arg L(j\omega_c)$ degrees and the delay margin $\varphi_m/\omega_c$ each measure the distance to instability along one direction only.
- The peak sensitivity $M_s$ is the inverse of the smallest distance from $L(j\omega)$ to $-1$, and it bounds both margins: $g_m \ge M_s/(M_s - 1)$ and $\varphi_m \ge 2\arcsin(1/(2M_s))$.
- For a minimum-phase loop the gain curve fixes the phase ([Bode gain-phase relation](/bode-gain-phase-relation/)). A slope of $-20n$ dB per decade over a wide band gives about $-90n$ degrees, so the gain should fall at about $-20$ dB per decade near crossover.
- For a stable closed loop whose $L$ has relative degree at least 2, $\int_0^\infty \ln|S(j\omega)|\,d\omega = \pi\sum_i \operatorname{Re} p_i$ over the unstable poles of $L$ ([Bode sensitivity integral](/bode-sensitivity-integral/)). Pushing $|S|$ down in one band pushes it up in another.
- A lead network $(1 + \alpha T s)/(1 + T s)$ gives at most $\sin\varphi_{\max} = (\alpha - 1)/(\alpha + 1)$ at $\omega_m = 1/(T\sqrt\alpha)$, where its gain is $\sqrt\alpha$. A sampled controller loses about $\omega_c h/2$ radians of phase margin to the hold.
- The Ziegler-Nichols ultimate cycle PID is $K = 0.6K_u$, $T_i = T_u/2$, $T_d = T_u/8$, a heuristic aimed at a decay ratio of one quarter. A relay experiment estimates $K_u$ by $4d/(\pi a)$, an approximation.

| method | output | cost | kind of result |
|---|---|---|---|
| [Root locus rules](/root-locus-rules/) | asymptotes, breakaway points, angles, crossings | $O((n + m)^3 + t(n + m)^2)$ | rules for a sketch; computed points exact up to root finding |
| [Root locus](/root-locus/) on a grid of gains | closed-loop poles | $O(t n^2)$ per gain | exact up to root finding |
| Nyquist criterion | number of unstable closed-loop poles | one frequency sweep | exact for linear time-invariant models |
| Margins and $M_s$ | $g_m$, $\varphi_m$, $M_s$ | one frequency sweep and a search | $g_m$, $\varphi_m$ one direction each; $M_s$ the closest point |
| [Ziegler-Nichols tuning](/ziegler-nichols-tuning/) from a model | $K$, $T_i$, $T_d$ | $O(g n)$ for the phase search | tables are rules of thumb |
| [Relay autotuning](/relay-autotuning/) | estimates of $K_u$ and $T_u$ | $O(k n^2)$ to simulate; 2 to 4 periods on a plant | describing-function approximation |
| [PID controller](/pid-controller/) step | $u_k$ | $O(1)$ per sample, three stored numbers | fixed work per sample |
| [Smith predictor](/smith-predictor/) step | $u_k$ | $O(n^2)$ per sample | with an exact model, $y = T_0 e^{-\theta s} r$ |

: Main methods of the chapter. $n$, $m$: poles and zeros of the loop, or the order of the plant model; $t$: iterations of the polynomial root finder; $g$: frequency grid points; $k$: simulation steps.

## Choosing a method

For a rational loop, test stability by the closed-loop poles or the [Routh-Hurwitz criterion](/routh-hurwitz-criterion/); with a delay or a measured frequency response, use the Nyquist criterion.

To judge robustness, compute $M_s$ first, then the margins.

For a process loop, start with a PID controller tuned by a relay experiment or the Ziegler-Nichols tables; [internal model control](/internal-model-control/) gives a calmer one from a model with a delay, and [loop shaping](/loop-shaping/) one from a target crossover and margin. Add a [lead-lag compensator](/lead-lag-compensator/) when the phase at the wanted crossover is short, and check every design by its margins, $M_s$ and step responses.

A long delay calls for a Smith predictor, a measured disturbance for [feedforward control](/feedforward-control/), a fast disturbance near the actuator for [cascade control](/cascade-control/), set-point overshoot for a set-point weight ([two-degree-of-freedom control](/two-degree-of-freedom-control/)), and several loops on one plant for the [relative gain array](/relative-gain-array/). On a computer, discretize with the Tustin map with $\omega_c h/2$ a few degrees, and add [anti-windup](/anti-windup/) whenever the actuator can saturate.
