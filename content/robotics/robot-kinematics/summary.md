## What to remember

- **Forward kinematics** is a product of one rigid transformation per joint: $T(\theta) = A_1(\theta_1) \cdots A_n(\theta_n)$ with [Denavit-Hartenberg](/denavit-hartenberg-convention/) matrices, or $T(\theta) = e^{[\mathcal S_1]\theta_1} \cdots e^{[\mathcal S_n]\theta_n} M$ with the [product of exponentials](/product-of-exponentials-formula/). Either costs $\Theta(n)$ matrix products.
- **Inverse kinematics** can have no solution, a finite number or infinitely many. An arm with a spherical wrist has at most 8 solutions, by [decoupling](/kinematic-decoupling/). A general 6R arm has at most 16, counted over the complex numbers, and some arms have 16 real ones. The [Pieper criterion](/pieper-criterion/) is sufficient for a closed form, not necessary.
- **Grübler's formula** gives $m(N - 1 - J) + \sum_i f_i$ degrees of freedom, with $m = 3$ in the plane and $m = 6$ in space. The count is right only when the joint constraints are independent; the Bennett linkage counts $-2$ and still moves.
- **The Jacobian** maps joint rates to the end effector twist, $\mathcal V = J(\theta)\dot\theta$, and its transpose maps a wrench to joint torques, $\tau = J^{\mathsf T}F$, with both in the same frame. The [space and body Jacobians](/space-and-body-jacobian/) are related by $J_b = \mathrm{Ad}_{T_{bs}} J_s$.
- **At a singularity** the Jacobian loses rank. Near one, a task velocity along the last singular direction needs joint rates of size $1/\sigma_{\min}$. [Yoshikawa's measure](/yoshikawa-manipulability-measure/) $w = \sqrt{\det JJ^{\mathsf T}} = \sigma_1 \cdots \sigma_m$ is zero exactly at the singularities; for the planar 2R arm, $w = L_1L_2|\sin\theta_2|$.
- **Newton steps converge only locally.** The [pseudoinverse](/jacobian-pseudoinverse-method/) and [Newton-Raphson](/newton-raphson-inverse-kinematics/) methods converge quadratically from a good start near a regular solution. From a far start they can cycle, diverge or find another solution, and they give at most one solution.
- **Damping and the transpose trade speed for safety.** [Damped least squares](/damped-least-squares-inverse-kinematics/) takes $\Delta\theta = J^{\mathsf T}(JJ^{\mathsf T} + \lambda^2 I)^{-1}e$, with $|\Delta\theta| \le |e|/(2\lambda)$ everywhere, and converges linearly. The [transpose](/jacobian-transpose-method/) step $\alpha J^{\mathsf T}e$ is gradient descent on $\tfrac12|e|^2$.
- **Redundancy** gives the rates $\dot\theta = J^{+}v + (I - J^{+}J)z$. The second term changes no task velocity. When $J$ has full row rank $m < n$, the self-motions near a configuration form a manifold of dimension $n - m$.
- **Parallel robots** reverse the difficulty: the inverse kinematics is solved leg by leg, and the forward kinematics is hard. The general [Stewart-Gough platform](/stewart-gough-forward-kinematics/) has at most 40 complex solutions, and examples exist with all 40 real.

## The inverse kinematics methods side by side

| Method | Time | Returns | Convergence | Needs |
|---|---|---|---|---|
| [Paden-Kahan subproblems](/paden-kahan-subproblems/) | $\Theta(n)$ | all solutions | no iteration | axes that meet, or points that joints leave fixed |
| [Raghavan-Roth method](/raghavan-roth-method/) | $\Theta(d^3)$, $d = 16$ | all solutions | no iteration | a polynomial or eigenvalue solver |
| [Pseudoinverse method](/jacobian-pseudoinverse-method/) | $\Theta(k\,mn\min(m, n))$ | one solution | local, quadratic at a regular square solution | an SVD per step |
| [Newton-Raphson](/newton-raphson-inverse-kinematics/) | $\Theta(kn^3)$ | one solution | local, quadratic | an invertible $J_b$ |
| [Damped least squares](/damped-least-squares-inverse-kinematics/) | $\Theta(km^2n)$ | one solution | local, linear, ratio $\lambda^2/(\sigma_{\min}^2 + \lambda^2)$ | a damping $\lambda$ |
| [Jacobian transpose](/jacobian-transpose-method/) | $\Theta(kmn)$ | a stationary point | local, linear | a gain $\alpha$ |
| [Cyclic coordinate descent](/cyclic-coordinate-descent-inverse-kinematics/) | $\Theta(kn)$ | a stationary point | error never increases; no general result | nothing |
| [FABRIK](/fabrik/) | $\Theta(kn)$ | one solution | error never increases; proved for an unconstrained chain with the target in reach | joint positions only |

: Methods for inverse kinematics. Here $n$ is the number of joints, $m$ the dimension of the task and $k$ the number of iterations or sweeps. The rate of damped least squares holds near a solution, with $\sigma_{\min}$ the smallest singular value of the Jacobian there.

## Choosing a method

- If the arm has a spherical wrist, or another geometry that the Paden-Kahan subproblems cover, use the closed form. It returns every solution; pick one by joint limits or by closeness to the present configuration.
- For a general six-joint arm when you need every solution, use the Raghavan-Roth elimination, or [homotopy continuation](/homotopy-continuation/).
- For one solution near a known configuration, as in tracking a path, use Newton steps, and switch to damped least squares when the arm may pass near a singularity. Start each solve from the last solution.
- For a redundant arm, use the pseudoinverse with a null space term for a second goal, or the task-priority method for a strict order of goals.
- For animation and long chains of ball joints, FABRIK or cyclic coordinate descent are cheap and need no matrices; FABRIK gives smoother poses.
- For tasks that need absolute accuracy, [calibrate](/kinematic-calibration/) the arm first: the built arm differs from its drawings.
