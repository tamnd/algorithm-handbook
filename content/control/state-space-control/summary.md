## What to remember

- $(A, B)$ is **controllable** exactly when $\operatorname{rank}[B, AB, \dots, A^{n-1}B] = n$, or equally when $\operatorname{rank}[A - \lambda I, B] = n$ at every eigenvalue $\lambda$ of $A$. Observability is the same test for $(A^T, C^T)$. For linear time-invariant models these tests are exact; in floating point the controllability matrix can be badly conditioned, and the PBH form or the distance $\min_\lambda \sigma_{\min}[A - \lambda I, B]$ is the safer measure.
- **Stabilizability** and **detectability** ask only that the modes the input cannot reach, or the output cannot see, are already asymptotically stable. They are what a stabilizing feedback and a converging observer need.
- **Pole placement.** The eigenvalues of $A - BK$ can be put anywhere, in conjugate pairs, exactly when $(A, B)$ is controllable. With one input the gain is unique and [Ackermann's formula](/ackermann-formula/) gives $K = e_n^T W^{-1} p(A)$. With several inputs there are $n(m-1)$ free parameters, and robust methods use them to make the eigenvector matrix well conditioned.
- **Observers** are the dual: $\dot{\hat x} = A\hat x + Bu + L(y - C\hat x)$ has error dynamics $A - LC$. The **separation principle** says that the loop with $u = -K\hat x$ has the eigenvalues of $A - BK$ together with those of $A - LC$. It says nothing about margins: the loop can be much less robust than the state feedback.
- A realization is **minimal** exactly when it is controllable and observable, and then all minimal realizations are similar. Its order is the rank of the Hankel matrix of Markov parameters.
- The largest **controlled invariant subspace** $\mathcal V^\ast$ inside $\ker C$ comes from $\mathcal V_{k+1} = \mathcal K \cap A^{-1}(\mathcal V_k + \operatorname{im} B)$ in at most $\dim \mathcal K + 1$ passes. A disturbance $Ed$ can be hidden from $y$ by state feedback exactly when $\operatorname{im} E \subseteq \mathcal V^\ast$.
- **Output regulation**, with a stabilizable plant and an exosystem with no decaying modes, is solvable exactly when $\Pi S = A\Pi + B\Gamma + P$, $C\Pi + Q = 0$ have a solution.
- **Hankel singular values** $\sigma_i = \sqrt{\lambda_i(W_c W_o)}$ bound every reduction from below: any asymptotically stable model of order $r$ has $\|G - G_r\|_\infty \ge \sigma_{r+1}$. Balanced truncation with $\sigma_r > \sigma_{r+1}$ is asymptotically stable and has $\|G - G_r\|_\infty \le 2\sum$ of the distinct deleted values.

## The main methods side by side

| method | computes | assumes | cost |
|---|---|---|---|
| Kalman rank test | controllability | exact data | $O(n^3 m)$ |
| Ackermann's formula | $K$ for one input | controllable | $O(n^3)$ |
| KNV pole placement | $K$ with well-conditioned eigenvectors | controllable, $m > 1$ | $O(n^4(s+1))$ |
| deadbeat control | $K$ with $A - BK$ nilpotent | uncontrollable eigenvalues at 0 | $O(N n^2(n+m))$ |
| Luenberger observer | $L$ and the estimate | observable, or detectable for convergence only | $O(pn^4)$, then $O(n(n+m+p))$ per step |
| invariant subspace algorithm | $\mathcal V^\ast(\mathcal K)$ | exact data | $O(n^3(n+m))$ |
| balanced truncation | $G_r$ with an $H_\infty$ bound | $A$ Hurwitz, gap $\sigma_r > \sigma_{r+1}$ | $O(n^3 + n^2(m+p))$ |
| iterative rational Krylov | $G_r$ meeting the $H_2$ conditions | $A$ Hurwitz, one input and output | $O(k r n^3)$ dense |

: Costs are the worst-case bounds of the entries, for dense matrices. Here $s$ is the number of sweeps, $N$ the number of steps to reach zero, $k$ the number of iterations and $r$ the reduced order. The iterative rational Krylov algorithm has no a priori error bound and no proof of convergence in general.

## Choosing a method

To check a model, look at the singular values of $[A - \lambda I, B]$ at the eigenvalues of $A$ rather than at the rank of the controllability matrix. For one input and small $n$, up to about 6, Ackermann's formula is fine. For larger $n$ or several inputs, use a robust method such as KNV, or [infinite-horizon LQR](/infinite-horizon-lqr/), which with one input and full state feedback also guarantees a gain margin from 1/2 to infinity and a phase margin of at least 60 degrees. Add integral action when constant references or loads must give zero steady-state error, and use the regulator equations for ramps or sinusoids. Use a full Luenberger observer by default and a reduced-order one when the outputs are clean. When the noise matters, use the [Kalman filter](/kalman-filter/) instead of placing observer poles by hand. To reduce a dense model of up to a few thousand states, use balanced truncation and cut at a gap in the Hankel singular values; for large sparse models, use the iterative rational Krylov algorithm and check the error afterwards.
