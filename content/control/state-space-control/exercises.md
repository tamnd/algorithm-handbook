1. ◦ Let $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ and $B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$. Form the controllability matrix of the [Kalman rank condition](/kalman-rank-condition/) and find its rank. Which states can be reached from the origin? Explain the answer from the equations $\dot x_1 = x_2 + u$, $\dot x_2 = 0$.

2. ◦ The discrete-time system $x_{k+1} = A x_k + B u_k$ has $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ and $B = 0$. Show that every initial state reaches the origin in two steps, but that no state other than the origin can be reached from the origin. Which of the two notions in [controllability](/controllability/) does the system have?

3. ◦ Let $A = -I_2$ and $B = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$. Use the [Popov-Belevitch-Hautus test](/popov-belevitch-hautus-test/) to show that $(A, B)$ is not controllable. What is the least number of inputs that makes some $(A, B)$ with this $A$ controllable, and why?

4. ◦ Write $G(s) = (2s + 1)/(s^2 + 3s + 5)$ in [controllable canonical form](/controllable-canonical-form/). Then find the gain $K$ of the state feedback $u = -Kx$ that puts both eigenvalues of $A - BK$ at $-4$, by reading the last row of $A - BK$.

5. ◦ For the scalar system $\dot x = -2x + u$, find the [controllability Gramian](/controllability-gramian/) $W_c(t)$ and its limit as $t \to \infty$. What is the least input energy $\int_0^1 u^2\,dt$ that moves the state from 0 to 1 in time 1?

6. ◦ For the double integrator $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ with $y = x_1$, find the gain $L$ of a [Luenberger observer](/luenberger-observer/) that puts both eigenvalues of $A - LC$ at $-4$.

7. ◦ Let $A = \operatorname{diag}(1, -2)$. Is $(A, B)$ [stabilizable](/stabilizability/) for $B = (1, 0)^T$? For $B = (0, 1)^T$? Is $(C, A)$ [detectable](/detectability/) for $C = [0, 1]$?

8. ◦ Find the [Hankel singular value](/hankel-singular-values/) of $G(s) = 3/(s + 2)$. [Balanced truncation](/balanced-truncation/) to order 0 returns $G_0 = 0$. Compute $\|G - G_0\|_\infty$ and compare it with the bound of the [error bound theorem](/balanced-truncation-error-bound/).

9. ◦ The system $\dot x = Ax + Bu + Ed$, $y = Cx$ has $n = 3$, $C = [1, 0, 0]$ and $E = e_2$. Show that no [unknown input observer](/unknown-input-observer/) of the kind in that entry exists, from its rank condition. Explain in words why the output cannot separate $d$ from the state at once.

10. • Let $A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}$ and $C = [c, 1]$. Find every real $c$ for which $(C, A)$ is not [observable](/observability/). For each such $c$, give the transfer function from $u$ to $y$ with $B = (0, 1)^T$, and explain the result by a cancellation.

11. • Let $A = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ and $B = (b_1, \dots, b_n)^T$. Show that $(A, B)$ is controllable exactly when the $\lambda_i$ are distinct and every $b_i \ne 0$. Compute the determinant of the controllability matrix for $\lambda = (-1, -2, -3)$ and $b = (1, 1, 1)$.

12. • For the double integrator, use the controllability Gramian $W_c(T)$ to find the least energy $\int_0^T u^2\,dt$ that moves the cart from rest at 0 to rest at position $d$ in time $T$. By what factor does the energy grow when $T$ is halved?

13. • The linearized inverted pendulum, in scaled units, is $A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, $B = (0, 1)^T$, $C = [1, 0]$. Find the [state feedback](/state-feedback/) $u = -Kx + Nr$ that places the eigenvalues at $-1$ and $-2$ and gives $y \to r$ for a constant reference $r$.

14. • For $x_{k+1} = A x_k + B u_k$ with $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ and $B = (0, 1)^T$, find the [deadbeat](/deadbeat-control/) gain $K$, with $(A - BK)^2 = 0$. Give the states $x_1$ and $x_2$ of the loop from $x_0 = (1, 0)^T$.

15. • For the double integrator with $y = x_1$, take $K = [2, 2]$ and $L = (4, 4)^T$. Write the observer-based controller as a transfer function from $y$ to $-u$, and check that the closed-loop polynomial factors as the [separation principle](/separation-principle/) says.

16. • The Markov parameters of a single-input single-output system are $h_1, h_2, \dots = 1, 1, 2, 3, 5, 8, \dots$, the Fibonacci numbers. Find the order of a [minimal realization](/minimal-realization/), the transfer function, and one realization $(A, B, C)$.

17. • Let $G(s) = 1/(s+1) + 1/(s+2)$, realized with $A = \operatorname{diag}(-1, -2)$ and $B = C^T = (1, 1)^T$. Show that $W_c = W_o$ and find the two Hankel singular values exactly. What do the two theorems of [model order reduction](/model-order-reduction/) say about the $H_\infty$ error of the best model of order 1?

18. • Let $A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix}$, $B = e_3$ and $C = [1, 1, 0]$. Run the [invariant subspace algorithm](/invariant-subspace-algorithm/) with $\mathcal K = \ker C$. Then decide the [disturbance decoupling problem](/disturbance-decoupling-problem/) for $E = (1, -1, 1)^T$ and for $E = e_3$.

19. • The plant $\dot x = -x + 2u$ must track $w_1 = \sin 2t$, with error $e = x - w_1$. Write the exosystem, solve the [regulator equations](/regulator-equations/) for $\Pi$ and $\Gamma$, and check that $x = \sin 2t$ with $u = \Gamma w$ solves the plant equation.

20. ★ Let $(A, b)$ be controllable with a single input. Show that $\operatorname{rank}(A - bK - \lambda I) \ge n - 1$ for every $K$ and every $\lambda$. Deduce that no single-input feedback gives $A - bK = -I$ when $n \ge 2$, although the [pole placement theorem](/pole-placement-theorem/) allows the eigenvalues $-1, \dots, -1$.

21. ★ Let $A = 0$ and $B = I$, both $2 \times 2$. Describe every $K$ for which $A - BK$ has the eigenvalues $-1$ and $-2$, and count the free parameters. Find the least Frobenius norm of such a $K$, and the gains that attain it. What is the condition number of their eigenvector matrices, the quantity that [robust pole placement](/robust-pole-placement/) tries to make small?

22. ★ Approximate $G(s) = 1/((s+1)(s+2))$ by $G_1(s) = \varphi/(s + \lambda)$ with $\lambda > 0$. Show that $\|G - G_1\|_{H_2}^2 = \|G\|_{H_2}^2 - 2\varphi G(\lambda) + \varphi^2/(2\lambda)$. Find the best $\varphi$ for each $\lambda$, then the best $\lambda$, and check that the result meets the interpolation conditions of the [iterative rational Krylov algorithm](/iterative-rational-krylov/).

23. ★ In exercise 15, put a gain $k > 0$ at the plant input, so that the plant receives $ku$. Find the closed-loop polynomial and the exact range of $k$ for which it is Hurwitz. At the upper end, at which frequency does the loop oscillate? Compare with the full state feedback $u = -Kx$ under the same gain.

24. ★ For the loop of an observer-based controller with reference input, $u = -K\hat x + Nr$, use the coordinates $(x, e)$ with $e = x - \hat x$. Show that the observer error is not controllable from $r$, and find the [Kalman decomposition](/kalman-decomposition/) of the loop. Deduce that the transfer function from $r$ to $y$ is the same as with full state feedback.
