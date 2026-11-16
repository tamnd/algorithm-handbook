## What to remember

- The output $y = h(x)$ has [relative degree](/relative-degree/) $r$ at $x_0$ if
  $L_g L_f^k h = 0$ near $x_0$ for $k < r - 1$ and $L_g L_f^{r-1} h(x_0) \ne 0$. Then
  $u = (v - L_f^r h) / (L_g L_f^{r-1} h)$ gives $y^{(r)} = v$, and the other $n - r$ states follow the
  [zero dynamics](/zero-dynamics/), which must be checked apart.
- A single-input system is [feedback linearizable](/feedback-linearizability-conditions/) near $x_0$ if
  and only if $g, \mathrm{ad}_f g, \dots, \mathrm{ad}_f^{n-1} g$ are independent at $x_0$ and the span of
  the first $n - 1$ is involutive. The result is local, and the exact cancellation gives no robustness
  guarantee.
- $V$ is a [control Lyapunov function](/control-lyapunov-function/) for $\dot x = f + g u$ when
  $L_g V(x) = 0$ implies $L_f V(x) < 0$ for $x \ne 0$. With the small control property,
  [Artstein's theorem](/artstein-sontag-theorem/) makes this equivalent to stabilization by a feedback
  that is smooth away from $0$ and continuous at $0$, and
  [Sontag's formula](/sontag-universal-formula/) gives one.
- The [Lie algebra rank condition](/lie-algebra-rank-condition/) gives accessibility, not
  controllability. By [Brockett's condition](/brockett-condition/), a continuous stabilizing feedback needs
  $(x, u) \mapsto f(x, u)$ to map every neighborhood of $(0, 0)$ onto a neighborhood of $0$; controllable
  driftless systems with fewer inputs than states fail it.
- [Backstepping](/backstepping/) gives $V = \frac12 \sum z_i^2$ with $\dot V = -\sum c_i z_i^2$.
  [Adaptive backstepping](/adaptive-backstepping/) keeps this $\dot V$ with unknown parameters, so
  $x \to 0$, but the estimates need not converge to the true values.
- [Sliding mode control](/sliding-mode-control/) with $s \dot s \le -\eta |s|$ reaches $s = 0$ within
  $|s(0)| / \eta$ and rejects matched disturbances with $|d| \le D$ when the gain is at least
  $D + \eta$. With sampling period $h$ the sliding variable stays within $(k + D) h$, which is
  [chattering](/chattering/); the [super-twisting algorithm](/super-twisting-algorithm/) improves this to
  order $h^2$.
- For two states, a [high-gain observer](/high-gain-observer/) with parameter $\varepsilon$ has errors
  of order $\varepsilon^2$ in $x_1$ and $\varepsilon$ in $x_2$, but a transient of order $1/\varepsilon$
  in $x_2$ (peaking); saturate the control.
- In [passivity-based control](/passivity-based-control/) and [IDA-PBC](/ida-pbc/) the closed-loop energy
  satisfies $\dot H_d = -\nabla H_d^T R_d \nabla H_d \le 0$. That gives stability; convergence needs the
  [LaSalle invariance principle](/lasalle-invariance-principle/) and a detectability check.
- A [control barrier function](/control-barrier-function/) asks for
  $L_f h + L_g h\, u + \alpha(h) \ge 0$. Without input limits the [safety filter](/cbf-safety-filter/) is
  $u = u_{\text{nom}} + \max(0, -(a \cdot u_{\text{nom}} + b))\, a^T / |a|^2$ with $a = L_g h$ and
  $b = L_f h + \alpha(h)$, valid for a continuously updated input.

| Method | Needs | Guarantee | Weakness | Cost |
|---|---|---|---|---|
| Input-output linearization | relative degree $r$, exact model | $y^{(r)} = v$ locally | zero dynamics, no robustness | $O(n^3 p q)$ design |
| Backstepping | strict feedback form | global asymptotic stability | formulas grow with $n$ | $O(3^n q)$ |
| Adaptive backstepping | linear unknown parameters | $x \to 0$ | estimates need not converge | $O((3(n+p))^n (q + np + p^2))$ |
| Sontag's formula | a CLF | asymptotic stability | needs the CLF | $O(nm)$ |
| Sliding mode control | matched uncertainty, bound $D$ | reaching in finite time | chattering | $O(n + q)$ |
| High-gain observer | observable form | error $O(\varepsilon)$ | peaking | $O(n + q)$ |
| IDA-PBC | energy, solved matching PDE | $\dot H_d \le 0$ | the PDE | $O(n^2 m + m^3)$ |
| Safety filter | a CBF valid with the input limits | forward invariance | pointwise, no look-ahead | $O(m \log m)$ |

: Main design methods; costs per evaluation. $n$ is the number of states, $m$ the number of inputs, $p$ the
number of unknown parameters (for adaptive backstepping) or of terms (for input-output linearization),
$q$ the cost of evaluating the model once.

## Choosing a method

With a well-defined relative degree and stable zero dynamics,
input-output linearization is quickest, but it cancels terms exactly. In strict feedback form,
[backstepping](/backstepping/) is global and can keep helpful nonlinear terms.
Given a control Lyapunov function, use Sontag's formula.

For bounded matched uncertainty, sliding mode control rejects it in the ideal model; use a boundary layer or super-twisting when the actuator cannot switch fast. If the
uncertainty is large and poorly modeled, [active disturbance rejection control](/active-disturbance-rejection-control/)
needs only the order and a rough input gain. For plants with a clear energy,
passivity-based designs keep the physics and give a Lyapunov function. To add a state constraint
to a working controller, wrap it in a safety filter.

Before designing a stabilizer, check [Brockett's condition](/brockett-condition/): if it fails, no
continuous static feedback works, and time-varying or discontinuous feedback is needed.
