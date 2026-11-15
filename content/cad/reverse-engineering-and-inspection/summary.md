## What to remember

- An [algebraic fit](/algebraic-distance-fitting/) minimizes $\sum_i \varphi(p_i)^2$ under a normalization of the coefficients, so it is a linear problem or an eigenproblem with a closed form. It is exact for that objective but biased for the geometric one: for a circle, a point at distance $\delta$ has algebraic distance $\delta(\delta + 2r)$. On a $60$ degree arc of the unit circle with noise $\sigma = 0.05$, the entry's median Kasa radius is $0.546$, against $1.006$ for the geometric fit.
- [Taubin fitting](/taubin-fitting/) divides by the mean squared gradient and corrects the bias to first order; for a line it is orthogonal regression. The [geometric fit](/geometric-primitive-fitting/) minimizes true distances by Gauss-Newton or Levenberg-Marquardt steps from an algebraic start. A sphere has $4$ parameters, a cylinder $5$, a cone $6$ and a torus $7$, and the iteration finds a local minimum.
- Exact [segmentation](/primitive-segmentation/) into the fewest pieces is NP-hard already for lines in the plane, so practical methods are heuristics, and sampling methods succeed with a stated probability.
- A tolerance is a zone in a [datum frame](/datum-reference-frame/). For a hole at maximum material condition the virtual condition is $V = d_M - t$, and every bit of size away from $d_M$ is added to the position tolerance as bonus.
- [Form error](/form-error-evaluation/) is $E = \min W$, the least width over all placements of the ideal feature, a minimax problem. A [least-squares reference feature](/least-squares-reference-feature/) gives a width $W_{LS} \ge E$: it may reject a good part, never accept a bad one. [Minimum-zone flatness](/minimum-zone-flatness/) is set by a face-vertex or an edge-edge pair of the convex hull, $\Theta(n^2)$ in the worst case.
- [Localization](/inspection-localization/) of matched points is the Kabsch closed form. With unknown matches, iterative closest points never increases the error but stops at a local minimum; on a rectangle outline a start at exactly $90°$ is a fixed point with positive error.
- Worst case $\sum_i \lvert s_i \rvert T_i$ bounds every assembly; root sum of squares $\sqrt{\sum_i s_i^2 T_i^2}$ and [Monte Carlo](/monte-carlo-tolerance-analysis/) estimate how many fail. A Monte Carlo reject rate $p$ from $N$ samples has standard error $\sqrt{p(1-p)/N}$, and zero rejects give an upper $95\%$ limit near $3/N$.
- The [direct linearization method](/direct-linearization-method/) takes sensitivities $-B^{-1}A$ from the loop equations and is exact to first order only: in the clutch example with $T = 0.05$ the true extremes are $-3.03°$ and $+2.07°$, the linear ones $\pm 2.37°$.
- [Tolerance allocation](/tolerance-allocation/) with costs $a_i/T_i$ and an RSS stack has the closed form cost $S^{3/2}/T$ with $S = \sum_j (a_j \lvert s_j \rvert)^{2/3}$. With a discrete choice of processes it is weakly NP-hard and solved by a pseudo-polynomial dynamic program.

| Method | Problem | Time | Guarantee |
|---|---|---|---|
| Kasa circle fit | circle | $\Theta(n)$ | exact for algebraic distance; small radius on short arcs |
| Taubin fit | implicit curve or surface | $\Theta(m n^2 d + s n^3)$ | first-order correction of the bias |
| Geometric fit (Gauss-Newton) | sphere, cylinder, cone, torus | $\Theta(s(m k^2 + k^3))$ | local minimum of the orthogonal distance |
| Kabsch localization | matched points | $\Theta(n)$ | exact least-squares optimum |
| Hull-based flatness | minimum-zone plane | $\Theta(n^2)$ worst case | exact minimum zone |
| Sequential LP cylindricity | minimum-zone cylinder | $O(sn)$ with fixed-dimension LP | local optimum of the minimax |
| Monte Carlo analysis | reject rate | $O(N(n + C_f))$ | standard error $\sqrt{p(1-p)/N}$ |
| Process selection DP | discrete allocation | $O(B \sum_i k_i)$ | exact optimum on the grid of $B$ steps |

: The main methods. $n$ or $m$ counts points (dimensions for Monte Carlo), $d$ the dimension, $k$ the parameters or process options, $s$ the iterations, $N$ the samples, $C_f$ the cost of one assembly solve, and $B$ the budget in grid steps.

## Choosing a method

To fit a primitive, start with an algebraic fit, Taubin's when the arc is short, and finish with the geometric fit. Fit related faces together with [constrained fitting](/constrained-primitive-fitting/) when the design says they are parallel or coaxial. For free-form faces, [squared distance minimization](/squared-distance-minimization/) converges faster than [parameter correction](/parameter-correction/) in the reported tests,

For a verdict on form, compute the minimum zone; a least-squares width is a safe upper bound and a fast first screen. Place the points by Kabsch on known matches first, and start any closest-point iteration from several poses when the part has symmetries.

Use the worst case when every assembly must work, root sum of squares for a quick estimate with many independent parts, and Monte Carlo when the model is nonlinear or the reject rate is wanted. For rare rejects, plan the sample size from the standard error first.
