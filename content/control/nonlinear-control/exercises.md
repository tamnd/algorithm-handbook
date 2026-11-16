1. ◦ Let $f(x) = (x_2, -x_1 - x_2^3)$, $g = (0, 1)$ and $h(x) = x_1^2 + x_2^2$. Compute the
[Lie derivatives](/lie-derivative/) $L_f h$ and $L_g h$. What does $L_f h$ say about $h$ along the
solutions of $\dot x = f(x)$? At which points does the output $y = h(x)$ of $\dot x = f(x) + g u$ have
relative degree 1, and why is the relative degree not defined at the other points?

2. ◦ For $\dot x_1 = -x_1 + x_2^2$, $\dot x_2 = u$, compute the [Lie bracket](/lie-bracket/)
$\mathrm{ad}_f g = [f, g] = (Dg) f - (Df) g$. Near which points is the system feedback linearizable? Is
its Jacobian linearization at the origin controllable?

3. ◦ For the system $\dot x_1 = x_2$, $\dot x_2 = -x_1 + x_3$, $\dot x_3 = -x_3 + (1 + x_1^2) u$, find the
[relative degree](/relative-degree/) of each of the outputs $y = x_1$, $y = x_1 + x_2$ and $y = x_2$.

4. ◦ Apply [backstepping](/backstepping/) with $c_1 = c_2 = 1$ to $\dot x_1 = x_1 + x_2$, $\dot x_2 = u$:
take $z_1 = x_1$, the virtual control $\alpha_1 = -x_1 - c_1 x_1$, $z_2 = x_2 - \alpha_1$ and
$V = \frac12 (z_1^2 + z_2^2)$. Write $u$ as a linear function of $x$ and give the closed-loop eigenvalues.

5. ◦ Apply [Sontag's formula](/sontag-universal-formula/) to $\dot x = x^3 + u$ with $V = x^2 / 2$. Give
$u(x)$, the closed loop and the value $u(1)$.

6. ◦ In [sliding mode control](/sliding-mode-control/) of $\dot x_1 = x_2$, $\dot x_2 = u + d(t)$ with
$|d| \le 0.3$, take $s = x_2 + 2 x_1$ and $u = -2 x_2 - \operatorname{sign}(s)$. Show that
$s \dot s \le -0.7 |s|$, bound the reaching time from $x(0) = (0.5, 0.4)$, and describe the motion of
$x_1$ after reaching. If the input is computed by explicit Euler steps of length $h = 0.001$ and held, how
large can $|s|$ be after reaching?

7. ◦ For the [super-twisting algorithm](/super-twisting-algorithm/) with $\dot s = u + d(t)$ and
$|\dot d| \le L = 2$, what is the smallest $k_2$ that the certificate $k_2 > L + 2L^2 / k_1^2$ allows with
$k_1 = 3$? Does the rule of thumb $k_1 = 1.5 \sqrt L$, $k_2 = 1.1 L$ satisfy the certificate? Can any
$k_1$ work with $k_2 = 1.5$?

8. ◦ Use the [averaging method](/averaging-method/) on $\dot x = \varepsilon (a - \cos^2 t)\, x$ with
$\varepsilon > 0$ small. For which $a$ is the origin of the averaged system exponentially stable? Solve the
original equation exactly and compare.

9. ◦ For $\dot x = u$, $h(x) = 1 - x$, $\alpha(s) = 2 s$ and the nominal input $u_{\text{nom}} = 3$, write
the output of the [safety filter](/cbf-safety-filter/) as a function of $x$, give its value at $x = 0.5$,
and solve the closed loop from $x(0) = 0$. Does the state reach the boundary $x = 1$?

10. ◦ A series circuit has a resistor $r$, an inductor $L$ with flux $\phi$, a capacitor $C$ with charge
$q$, and a voltage source $u$. Write it as a [port-Hamiltonian system](/port-hamiltonian-system/)
$\dot x = (J - R) \nabla H + g u$, $y = g^T \nabla H$ with $x = (q, \phi)$ and
$H = q^2 / (2C) + \phi^2 / (2L)$. What is the output $y$, what is $\dot H$, and what does the feedback
$u = -K y + v$ with $K > 0$ do to the circuit?

11. • For $\dot x_1 = x_2$, $\dot x_2 = -x_1 + x_3$, $\dot x_3 = -x_3 + (1 + x_1^2) u$, find the
[zero dynamics](/zero-dynamics/) for the output $y = x_1 + x_2$ and for the output $y = x_2$. Which output
is minimum phase? Check the answer against the zeros of the linear part.

12. • Show that $\dot x_1 = x_2 + x_2^2$, $\dot x_2 = x_3$, $\dot x_3 = u$ satisfies the
[conditions for feedback linearizability](/feedback-linearizability-conditions/) near the origin. Find
new coordinates $z = T(x)$ and a feedback $u = \alpha(x) + \beta(x) v$ that give
$\dot z_1 = z_2$, $\dot z_2 = z_3$, $\dot z_3 = v$, and the largest region of the form $x_2 > c$ where
they are valid.

13. • Apply backstepping with $c_1 = c_2 = 1$ to $\dot x_1 = \sin x_1 + x_2$, $\dot x_2 = u$. Give the
feedback, the closed-loop equations in $z$, and the value $u(\pi/2, 0)$.

14. • Show that $V = x_1^2 + x_1 x_2 + x_2^2$ is a
[control Lyapunov function](/control-lyapunov-function/) for the double integrator $\dot x_1 = x_2$,
$\dot x_2 = u$. Compute the input of Sontag's formula at $(1, 0)$ and at $(0, 1)$, and $\dot V$ at both
points.

15. • A [high-gain observer](/high-gain-observer/) for $\dot x_1 = x_2$, $\dot x_2 = \phi(x, u)$, $y = x_1$
uses $\dot{\hat x}_1 = \hat x_2 + (2/\varepsilon)(y - \hat x_1)$ and
$\dot{\hat x}_2 = \phi_0(\hat x, u) + (1/\varepsilon^2)(y - \hat x_1)$. Where are the poles of the error
dynamics? If $\phi - \phi_0 = \delta$ is constant, find the steady errors in $x_1$ and $x_2$, and evaluate
them for $\varepsilon = 0.01$ and $\delta = 3$.

16. • Write a program that simulates the sliding mode loop of $\dot x_1 = x_2$, $\dot x_2 = u + d$ with
$d = 0.3 \sin 3t$, $s = x_2 + 2 x_1$, $u = -2 x_2 - \operatorname{sign}(s)$, from $x(0) = (0.5, 0.4)$ by
explicit Euler steps $h = 0.01$ and $h = 0.001$ with the input held over each step. Measure
$\max |s|$ over $3 \le t \le 6$ and compare with $(k + D) h$, where $k = 1$ and $D = 0.3$. Then replace $\operatorname{sign}(s)$ by the
saturation $\operatorname{sat}(s / \varphi)$ with $\varphi = 0.05$ and compare $\max |s|$ with the boundary
layer bound $\varphi D / k$.

17. • An ideal relay $u = -\operatorname{sign}(y)$ closes the loop around $G(s) = 1 / (s (s + 1)(s + 2))$.
Use the [describing function](/describing-function/) $N(A) = 4 / (\pi A)$ to predict the frequency and the
amplitude of the oscillation. Then simulate the loop with a stated step and compare.

18. • For $\dot x = -x + z$, $\varepsilon \dot z = -z + x^2$, write the reduced model and the boundary layer
model of the [singular perturbation method](/singular-perturbation-method/). Find all equilibria of the
full system and their stability for every $\varepsilon > 0$.

19. • In the magnetic levitation example of [IDA-PBC](/ida-pbc/), take $k = 1$, $m = 0.05$, $g_0 = 9.81$,
$r = 2$ and $\theta^\star = 0.6$. Find $\lambda^\star$ and the voltage $u^\star$ at rest. Then show that
with the free function $\Phi \equiv 0$ the energy $H_d$ has no strict minimum at the target.

20. • A point robot $\dot x = u$ in the plane uses the safety filter with
$h(x) = (x_1 - 2)^2 + x_2^2 - 1$, $\alpha(s) = s$ and $u_{\text{nom}} = (4, 0) - x$, from $x(0) = (0, 0)$.
Show that the filter is active on the segment $0 \le x_1 < 1$, $x_2 = 0$, that $x_2$ stays $0$, and that
$\dot x_1 = (1 - x_1)(3 - x_1) / (2 (2 - x_1))$ there. Where does the robot go?

21. • For $\dot x = \theta x^2 + u$ with $\theta$ unknown, use $u = -c x - \hat\theta x^2$ and
$\dot{\hat\theta} = \gamma x^3$ with $c, \gamma > 0$. Show that
$V = \frac12 x^2 + (\theta - \hat\theta)^2 / (2 \gamma)$ has $\dot V = -c x^2$ and that $x \to 0$. If
$\hat\theta(0) = \theta$ and $x(0) \ne 0$, does $\hat\theta$ stay equal to $\theta$?

22. • For the driftless system $\dot x_1 = u_1$, $\dot x_2 = u_2$, $\dot x_3 = x_2 u_1$, compute the
bracket of the two input fields, and use the [Lie algebra rank condition](/lie-algebra-rank-condition/) to
decide controllability. Is the Jacobian linearization at the origin controllable?

23. ★ For the system $\dot x_1 = u_1$, $\dot x_2 = u_2$, $\dot x_3 = x_2 u_1$, show with
[Brockett's condition](/brockett-condition/) that no continuous feedback $u = k(x)$ makes the origin
locally asymptotically stable. Then find a piecewise constant input with values in $\{-1, 0, 1\}^2$ that
steers $(0, 0, 1)$ to the origin in 4 time units.

24. ★ The system $\dot x_1 = -x_1 + x_2^2$, $\dot x_2 = u$ is not feedback linearizable near the origin.
Show that the linear feedback $u = -x_2$ makes the origin globally asymptotically stable, by finding a
Lyapunov function for the closed loop.

25. ★ For $\dot x = \theta x + u$ with $\theta$ unknown, use $u = -c x - \hat\theta x$ and
$\dot{\hat\theta} = \gamma x^2$. Show that $\gamma x^2 / 2 + (\theta - \hat\theta - c)^2 / 2$ is constant
along solutions, and find the limit of $\hat\theta(t)$ in closed form. Evaluate it for $\theta = 1$,
$c = 2$, $\gamma = 1$, $x(0) = 1$, $\hat\theta(0) = 0$. Compare with what
[adaptive backstepping](/adaptive-backstepping/) says about parameter convergence.

26. ★ A first order plant $\dot y = b u$ is controlled by linear
[active disturbance rejection control](/active-disturbance-rejection-control/) with an estimate $b_0$ of
$b$: the observer $\dot z_1 = z_2 + b_0 u + 2 \omega_o (y - z_1)$, $\dot z_2 = \omega_o^2 (y - z_1)$, and
the control $u = (k_p (r - z_1) - z_2) / b_0$ with $k_p, \omega_o > 0$. Find the characteristic polynomial
of the closed loop as a function of $\beta = b / b_0$, show that it factors as
$(s + k_p)(s + \omega_o)^2$ when $\beta = 1$, and find all $\beta$ for which the loop is stable.

27. ★ The safety filter for $\dot x = u$, $h = 1 - x$, $u_{\text{nom}} = 1$ and $\alpha(s) = \gamma s$ is
evaluated at the times $k T$ and its output is held for a time $T$. Prove that every solution that starts
in $\{h \ge 0\}$ stays there if and only if $\gamma T \le 1$. For $\gamma = 10$, $T = 0.15$ and
$x(0) = 0$, find the first unsafe sample and the value of $h$ there.
