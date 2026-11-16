1. $\omega_n = 5$ and $2\zeta\omega_n = 4$, so $\zeta = 0.4$. The overshoot is $e^{-0.4\pi/\sqrt{0.84}} = 0.254$, or 25.4 percent, the peak time is $\pi/(5\sqrt{0.84}) = 0.686$ s, and the rule gives $4/(0.4 \cdot 5) = 2$ s. The rule comes from the envelope $e^{-\zeta\omega_n t}/\sqrt{1 - \zeta^2}$, which bounds $|y - 1|$, so the true settling time can only be shorter.

4. The phase is $-3\arctan(\omega/2)$, which is $-180$ degrees at $\omega_{pc} = 2\sqrt 3 = 3.464$ rad/s. There $|s + 2|^2 = 16$, so $L(j\omega_{pc}) = -16/64 = -1/4$, and $g_m = 4$, or 12.04 dB.

10. $|L| = 1$ gives $\omega^4 + 4\omega^2 - 81 = 0$, so $\omega_c^2 = 7.2195$ and $\omega_c = 2.6869$ rad/s. The phase is $-90 - \arctan(\omega_c/2) = -143.34$ degrees, so $\varphi_m = 36.66$ degrees, and the delay margin is $0.6399/2.6869 = 0.238$ s. With $\omega_n = 3$ and $\zeta = 1/3$ the overshoot is 32.9 percent; the rule gives 33 degrees, close to 36.66.

11. Centre $(0 - 3 - 6)/3 = -3$, angles 60, 180 and 300 degrees. The breakaway point solves $3s^2 + 18s + 18 = 0$; the root on the locus is $-3 + \sqrt 3 = -1.268$, with $K = 6\sqrt 3 = 10.39$. The Routh array of $s^3 + 9s^2 + 18s + K$ gives $K = 9 \cdot 18 = 162$ and $\omega = \sqrt{18} = 4.243$ rad/s.

14. The closed-loop polynomial is $(s + 1)(s^2 + 4) + a s^2 + b s + c = s^3 + (1 + a)s^2 + (4 + b)s + (4 + c)$. Matching $(s + 2)^3 = s^3 + 6s^2 + 12s + 8$ gives $a = 5$, $b = 8$, $c = 4$. The factor $s^2 + 4$ sits in the denominator of $C$, so $S$ has zeros at $\pm 2j$ for every plant that keeps the loop stable. With the changed plant the polynomial is $1.1s^3 + 7s^2 + 14s + 8.8$, and $7 \cdot 14 > 1.1 \cdot 8.8$, so it does.

16. While $u = 1$, $y = t$ and the integral state is $I = \int_0^t (4 - \tau)\,d\tau = 4t - t^2/2$. The unsaturated output $(4 - t) + I$ falls to 1 when $t^2 - 6t - 6 = 0$, at $t = 3 + \sqrt{15} = 6.873$ s. Then $y = 6.873$, already 72 percent above the set point, and $I = 3.873$. Since $u = 1 > 0$, $y$ is still rising; a simulation gives the peak 7.01.

17. $L(j\omega) = k(-4\omega + j(4 - \omega^2))/\omega^3$, so the crossing is at $\omega = 2$ and $L = -k$. With the three poles at the origin passed on the right, $P = 0$, and counting encirclements shows that the closed loop is stable exactly when $-k$ lies to the left of $-1$, that is, for $k > 1$. The Routh condition $k \cdot 4k > 4k$ gives the same range. For $k > 1$ the gain can grow without limit but drop only by the factor $k$.

19. The half period is $0.2 + \ln(2 - e^{-0.2}) = 0.3666$ s, so the period is 0.733 s, and $a = 1 - e^{-0.2} = 0.1813$ gives the estimate 7.02. The true ultimate point solves $\arctan\omega + 0.2\omega = \pi$: $\omega_u = 8.443$ rad/s, $T_u = 0.744$ s and $K_u = \sqrt{1 + \omega_u^2} = 8.50$. The estimate is 17 percent low, a little worse than the 15 percent that the relay autotuning entry reports for $\theta = 0.5$ s.

20. The closed-loop polynomial is $s^2 + (1 + K)s + K/T_i$, so $K = 1.8$ and $T_i = 0.45$, and $T(s) = (1.8s + 4)/(s^2 + 2.8s + 4)$. The zero at $-1/T_i = -2.22$ is close to the poles and adds a derivative term to the response; a simulation gives an overshoot of 9.5 percent at 1.47 s. With $b = 0$ the reference enters only through the integral term, $T(s) = 4/(s^2 + 2.8s + 4)$, and the overshoot is the 4.6 percent of the formula.

21. The closed loop is $s^2 + 2s + 5$, with poles $-1 \pm 2j$. $|S(j\omega)|^2 = (\omega^4 + 10\omega^2 + 9)/(\omega^4 - 6\omega^2 + 25)$, which is below 1 exactly when $16\omega^2 < 16$. Setting the derivative to zero in $x = \omega^2$ gives $x^2 - 2x - 19 = 0$, so $\omega^2 = 1 + 2\sqrt 5$, $\omega = 2.339$ and $M_s = 2.058$. The integral is $\pi \cdot 1 = \pi$: with the unstable pole at 1, feedback must make the sensitivity worse on balance.

22. On the ray $s = r e^{j120^\circ}$ the angle condition holds at $r = 2$, so the poles are $-1 \pm j\sqrt 3$ and $K = |s||s + 3||s + 6| = 2 \cdot \sqrt 7 \cdot \sqrt{28} = 28$. Then $s^3 + 9s^2 + 18s + 28 = (s + 7)(s^2 + 2s + 4)$, and the third pole is $-7$. Its real part is 7 times that of the pair, inside the usual range of 5 to 10.

23. With $r = 0$ and a unit step $d$, $E(s) = -P(s)S(s)/s$. The loop is stable and has integral action, so $e \to 0$ and $\int_0^\infty e\,dt = \lim_{s \to 0} E(s)$. Write $P S/s = P T_i/(T_i s + K P (T_i s + 1))$; as $s \to 0$ this tends to $T_i/K$, also when $P$ has an integrator. For the loop shaping example, $4.47205/1.65646 = 2.6998$, which matches the simulated load response.

24. $|L_2| = |L_1|$, so the crossover stays at $\omega_c = 0.78615$ and $L_1$ has 51.83 degrees. The all-pass factor adds the lag $2\arctan(\omega_c/z)$, which is 42.92 degrees for $z = 2$, leaving 8.91 degrees. For 30 degrees, $2\arctan(\omega_c/z) \le 21.83$ degrees, so $z \ge 4.08$, that is, $\omega_c \le 0.19z$. The gain-phase relation does not see the zero, since the gain is the same, and the extra lag is why the rule keeps $\omega_c$ well below $z$.
