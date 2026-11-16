1. ◦ Build the [Routh array](/routh-array/) of $s^4 + 2s^3 + 3s^2 + 4s + 5$. How many roots lie in the right half plane?

2. ◦ Use the trace and the determinant to decide which of these matrices are [Hurwitz](/hurwitz-matrix/): $\begin{bmatrix} 1 & -3 \\ 2 & -2 \end{bmatrix}$, $\begin{bmatrix} -1 & 2 \\ 3 & -1 \end{bmatrix}$ and $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$. For each one that is not, say whether the origin of $\dot x = Ax$ is still Lyapunov stable.

3. ◦ Run the [Jury test](/jury-stability-test/) on $z^2 - \tfrac65 z + \tfrac12$, with exact fractions, and give the first column of the table. Then use the stability triangle to decide whether $z^2 + \tfrac85 z + \tfrac12$ has all its roots inside the unit circle.

4. ◦ For each scalar system, say whether the origin is unstable, Lyapunov stable, asymptotically stable or exponentially stable, and whether the property is global: (a) $\dot x = -x + x^3$; (b) $\dot x = -x^5$; (c) $\dot x = 0$; (d) $\dot x = x^2 - x^4$.

5. ◦ Solve $A^T P + PA = -I$ by hand for $A = \begin{bmatrix} -1 & 1 \\ 0 & -2 \end{bmatrix}$, and check that $P > 0$, as the [Lyapunov theorem for linear systems](/lyapunov-theorem-for-linear-systems/) says it must be.

6. ◦ Find the equilibria of $\dot x_1 = x_2$, $\dot x_2 = -x_1 + x_1^3 - x_2$ and classify each one with [Lyapunov's indirect method](/lyapunov-indirect-method/). What does the method say about the origin of $\dot x_1 = x_2$, $\dot x_2 = -x_1^3 - x_2$?

7. ◦ In polar coordinates, $\dot r = r(1 - r^2)(4 - r^2)$ and $\dot\theta = 1$. Find the [limit cycles](/limit-cycle/), say which ones attract nearby solutions, and give the nontrivial Floquet multiplier of each.

8. ◦ Which of these transfer functions are positive real: $(s+2)/(s+1)$, $1/(s(s+1))$ and $s/(s+1)$? Use the definition on the [passivity](/passivity/) page.

9. ◦ For $J = \begin{bmatrix} -3 & 1 \\ 2 & -4 \end{bmatrix}$, compute the matrix measures $\mu_1(J)$, $\mu_2(J)$ and $\mu_\infty(J)$. What contraction rate does each one give for $\dot x = Jx + u(t)$, in the sense of [contraction analysis](/contraction-analysis/)?

10. ◦ Write $p(x) = x^4 + 4x^3 + 6x^2 + 4x + 5$ as a sum of two squares of polynomials. What is the largest $\gamma$ such that $p - \gamma$ is a sum of squares?

11. • A plant $1/((s+1)^2(s+2))$ is in a unity feedback loop with a gain $K$. Use the Routh array to find every $K$ for which the loop is stable, and the frequency of the oscillation at the upper limit.

12. • Build the Routh array of $s^4 + s^3 + 2s^2 + 2s + 1$. A zero appears in the first column; replace it by $\varepsilon > 0$, count the sign changes, and explain why the count is the true number of roots in the right half plane here.

13. • A plant $1/s$ is sampled with a zero-order hold of period $h$, and the controller applies $u_k = -K y_{k-1}$, one sample late. Find the closed loop polynomial and the range of $K$ for which the loop is stable. Compare with the range without the delay, $u_k = -K y_k$, and with continuous feedback.

14. • Substitute $z = (1+w)/(1-w)$, the [bilinear transform](/bilinear-transform/), into $z^2 + \tfrac25 z - \tfrac{9}{20}$ and clear the denominators. Use the resulting polynomial in $w$ to decide whether the roots in $z$ lie inside the unit circle, and check by factoring.

15. • Show with [Lyapunov's direct method](/lyapunov-direct-method/) that the origin of $\dot x_1 = -x_1 + x_2$, $\dot x_2 = -x_1 - x_2^3$ is globally asymptotically stable. Is it also locally exponentially stable?

16. • Show that the origin of $\ddot x + \dot x^3 + x = 0$ is globally asymptotically stable, using the energy and [LaSalle's invariance principle](/lasalle-invariance-principle/). Then show that it is not exponentially stable.

17. • For $\dot x_1 = -2x_1 + x_1 x_2$, $\dot x_2 = -x_2 + x_1^2$, take $V = x_1^2 + x_2^2$. Find the largest $c$ such that $\dot V < 0$ on $\{0 < V < c\}$, and so a disc that lies in the [region of attraction](/region-of-attraction/). Compare its radius with the distance from the origin to the other equilibria.

18. • Show that $\dot x = -x - x^3 + u$ is [input-to-state stable](/input-to-state-stability/), with the asymptotic gain $\rho(r)$ equal to the positive root of $x + x^3 = r$. What is $\rho(10)$?

19. • Let $G(s) = 1/(s^2 + s + 1)$ be in negative feedback with a nonlinearity that satisfies $|\varphi(y)| \le k |y|$. Find the largest $k$ that the [small-gain theorem](/small-gain-theorem/) certifies, and the range of constant gains $\varphi(y) = ky$ for which the loop is stable.

20. • For $\dot x = -2x + u$, $y = x$, find every $p$ for which $V = p x^2$ is a storage function for the supply rate $u^2 - y^2$, in the sense of [dissipativity](/dissipativity/). What does the existence of one such $p$ say about the $L_2$ gain?

21. • Use the [passivity theorem](/passivity-theorem/) to show that the negative feedback loop of $G_1 = 1/s$ and $G_2 = (s+2)/(s+1)$ is stable, and check the answer by computing the closed loop poles.

22. • For $G(s) = 1/((s+1)(s+2))$ and a time-invariant nonlinearity in the sector $[0, k]$, find the largest $k$ that the [circle criterion](/circle-criterion/) certifies, in closed form. Then show that the [Popov criterion](/popov-criterion/) with $\eta = 1/3$ certifies every $k > 0$.

23. • The cubic $y = e^3$ has the describing function $N(a) = 3a^2/4$. Put it in a loop with $G(s) = 1/(s(s+1)^2)$ and use the [describing function](/describing-function/) to predict the amplitude and the period of a limit cycle. Does the predicted cycle attract or repel nearby solutions?

24. ★ Let $A$ be Hurwitz and $A^T P + PA = -I$. Show that $A + \Delta$ is Hurwitz whenever $\|\Delta\|_2 < 1/(2\lambda_{\max}(P))$. For the matrix of exercise 5, compute this bound, and compare it with the smallest $\|\Delta\|_2$ that makes $A + \Delta$ singular.

25. ★ The cascade $\dot x_1 = -x_1 + x_1^2 x_2$, $\dot x_2 = -x_2$ is made of two systems whose origins are globally asymptotically stable when their inputs are zero. Find every initial state from which $x_1$ escapes to infinity in finite time, and the escape time. What does this say about the first system as a system with input $x_2$?

26. ★ Show that $\dot x_1 = x_1 - x_2 - x_1^3$, $\dot x_2 = x_1 + x_2 - x_2^3$ has the origin as its only equilibrium, that the annulus $0.9 \le |x| \le 1.5$ is positively invariant, and so that it contains a periodic orbit by the [Poincaré-Bendixson theorem](/poincare-bendixson-theorem/). Use Bendixson's criterion to find a disc around the origin that no periodic orbit fits in.

27. ★ A relay with dead zone gives the output $\operatorname{sign}(e)$ when $|e| > \tfrac12$ and $0$ otherwise. Derive its describing function, find the amplitude at which it is largest, and find the values of $K$ for which the loop with $G(s) = K/(s(s+1)(s+2))$ is predicted to oscillate. For $K = 10$, find the predicted amplitudes and say which cycle attracts.

28. ★ Exercise 19 found the largest $k$ that the small-gain theorem certifies for $G(s) = 1/(s^2 + s + 1)$. Show that this $k$ cannot be raised for dynamic perturbations: find a stable transfer function $\Delta(s) = c\,(a - s)/(a + s)$ with $\|\Delta\|_\infty$ equal to that $k$ such that the loop of $G$ and $\Delta$ has a pole on the imaginary axis.
