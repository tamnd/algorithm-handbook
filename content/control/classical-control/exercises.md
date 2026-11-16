1. ◦ A closed loop has $T(s) = 25/(s^2 + 4s + 25)$. Read off $\zeta$ and $\omega_n$ of the [second-order system](/second-order-system/), and compute the overshoot, the peak time and the 2 percent settling time by the rule $4/(\zeta\omega_n)$. Compare the rule with the 2 percent settling time of 1.68 s that a simulation gives, and say why the rule errs on the long side (see [step response specifications](/step-response-specifications/)).

2. ◦ For $Y(s) = (s + 3)/(s(s^2 + 3s + 2))$ and for $Y(s) = 1/(s(s - 2))$, decide whether the [final value theorem](/final-value-theorem/) applies, and give $\lim_{t \to \infty} y(t)$ when it exists. What value does the formula $\lim_{s \to 0} sY(s)$ give in the second case, and what does $y(t)$ do?

3. ◦ Let $L(s) = 12(s + 1)/(s(s + 3)(s + 4))$ in a unity [feedback control loop](/feedback-control-loop/). Check with the [Routh-Hurwitz criterion](/routh-hurwitz-criterion/) that the closed loop is stable. Then give the type of the loop, its velocity constant $K_v$, and the [steady-state error](/steady-state-error/) to a unit step and to a unit ramp.

4. ◦ Find the phase crossover frequency and the [gain margin](/gain-margin/) of $L(s) = 16/(s + 2)^3$, as a factor and in dB.

5. ◦ A loop has the peak [sensitivity](/sensitivity-function/) $M_s = 1.5$. Which gain margin and which [phase margin](/phase-margin/) does this guarantee? Does a gain margin of 3 guarantee $M_s \le 1.5$?

6. ◦ A [lead network](/lead-lag-compensator/) $(1 + \alpha T s)/(1 + T s)$ must give a largest phase lead of 40 degrees. Find $\alpha$, the gain of the network at $\omega_m$ in dB, and $\omega_m$ for $T = 0.1$ s.

7. ◦ A plant with two inputs and two outputs has the steady-state gain matrix $G(0) = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$. Compute its [relative gain array](/relative-gain-array/) and say which pairing of inputs and outputs it suggests.

8. ◦ Map the PI controller $C(s) = 2(1 + 1/s)$ to discrete time with the Tustin map and $h = 0.1$ s, and write the difference equation for $u_k$. If the loop crosses over at $\omega_c = 2$ rad/s, about how much phase margin does the hold cost? See [controller discretization](/controller-discretization/).

9. • For $L(s) = 10/(s(1 + s/5))$, find the gain crossover from the straight-line asymptotes of the [Bode plot](/bode-plot/), then the exact crossover and the phase margin.

10. • For $L(s) = 9/(s(s + 2))$, compute the gain crossover, the phase margin and the delay margin. The closed loop is a second-order system; give its $\zeta$ and overshoot, and compare the phase margin with the rule $\varphi_m \approx 100\zeta$ degrees.

11. • For $G(s) = 1/(s(s + 3)(s + 6))$, apply the [root locus rules](/root-locus-rules/): the centre and angles of the asymptotes, the breakaway point and the gain there, and the gain and frequency where the locus crosses the imaginary axis.

12. • Let $L(s) = K(s + 1)/(s(s - 1))$ with $K > 0$. Find where the [Nyquist plot](/nyquist-plot/) crosses the negative real axis, and use the [Nyquist stability criterion](/nyquist-stability-criterion/) to find the gains $K$ that give a stable closed loop. Check the answer with the characteristic polynomial, and give the lower gain margin for $K = 2$.

13. • Compute the ultimate gain and the ultimate period of $P(s) = 1/(s + 2)^3$, and the [Ziegler-Nichols](/ziegler-nichols-tuning/) ultimate cycle PID settings. Explain why the answer follows from the values $K_u = 8$, $T_u = 3.6276$ s of $1/(s + 1)^3$ without a new computation.

14. • The plant $P(s) = 1/(s + 1)$ must follow $r(t) = \sin 2t$ with zero error. Find $C(s) = (a s^2 + b s + c)/(s^2 + 4)$ that puts all closed-loop poles at $-2$. Explain with the [internal model principle](/internal-model-principle/) why the error still tends to zero if the plant becomes $1.2/(1.1 s + 1)$, as long as the closed loop stays stable.

15. • For $P(s) = e^{-0.5 s}/(10 s + 1)$, give the PI settings of [internal model control](/internal-model-control/), $K_c = \tau/(K(\lambda + \theta))$ and $T_i = \tau$, with $\lambda = 0.5$ s, and the SIMC settings $K_c = \tau/(K(\tau_c + \theta))$, $T_i = \min(\tau, 4(\tau_c + \theta))$ with $\tau_c = \theta$. For a unit load step at the plant input, the integral of the error is $-T_i/K_c$ (exercise 23); compare the two tunings by it.

16. • The plant $y' = u$ has a PI controller with $K = 1$, $T_i = 1$, an actuator limit $|u| \le 1$ and no anti-windup. At $t = 0$ the set point steps from 0 to 4. When does the actuator leave the limit, and what are $y$ and the integral state then? Is the output still rising at that time? See [integrator windup](/integrator-windup/).

17. • Let $L(s) = k(s + 2)^2/s^3$ with $k > 0$. Find the frequency and the point where the Nyquist plot crosses the negative real axis, and the range of $k$ for a stable closed loop. Check with the Routh array of $s^3 + k s^2 + 4k s + 4k$.

18. • A disturbance enters through $P_d(s) = 1/((s + 1)(3s + 1))$, and the plant is $P(s) = 2/(s + 1)^2$. Find the ideal [feedforward](/feedforward-control/) $F = -P_d/P$. Is it proper and stable? Give its static gain and its gain at high frequency.

19. • Under [relay autotuning](/relay-autotuning/) with $d = 1$, the plant $e^{-0.2 s}/(s + 1)$ settles into a cycle with the half period $\theta + \ln(2 - e^{-\theta})$ and the amplitude $1 - e^{-\theta}$. Compute the period and the estimate $4d/(\pi a)$, and compare them with the true $T_u$ and $K_u$.

20. ★ For $P(s) = 1/(s + 1)$, choose the PI parameters $K$ and $T_i$ so that the closed-loop poles have $\zeta = 0.7$ and $\omega_n = 2$. Write the closed-loop $T(s)$. The second-order formula predicts an overshoot of 4.6 percent; explain why a simulation shows more, and how a set-point weight $b = 0$ ([two-degree-of-freedom control](/two-degree-of-freedom-control/)) brings the formula back.

21. ★ For $L(s) = 8/((s - 1)(s + 3))$, show that the closed loop is stable, that $|S(j\omega)| < 1$ exactly for $\omega < 1$, and find $M_s$ and the frequency where it occurs. What is $\int_0^\infty \ln|S(j\omega)|\,d\omega$ by the [Bode sensitivity integral](/bode-sensitivity-integral/)?

22. ★ For the root locus of $G(s) = 1/(s(s + 3)(s + 6))$, find the gain $K$ at which the complex closed-loop poles have $\zeta = 0.5$, the poles themselves and the third pole. Is the complex pair dominant by the usual rule of thumb?

23. ★ A loop with a [PID controller](/pid-controller/) reduced to PI, $C(s) = K(1 + 1/(T_i s))$, and a plant with no zero at $s = 0$ is asymptotically stable. Show that after a unit step load disturbance at the plant input, $\int_0^\infty e(t)\,dt = -T_i/K$. Check it against the PI loop of the [loop shaping](/loop-shaping/) entry, $K = 1.65646$, $T_i = 4.47205$.

24. ★ The loops $L_1(s) = 1/(s(s + 1))$ and $L_2(s) = (1 - s/z)/((1 + s/z)s(s + 1))$ have the same gain at every frequency. Find the phase margin of $L_2$ for $z = 2$, and the smallest $z$ that keeps it at 30 degrees or more. Relate the result to the [Bode gain-phase relation](/bode-gain-phase-relation/) and to the rule of thumb $\omega_c < z/2$.
