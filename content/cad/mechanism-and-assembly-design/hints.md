1. (a) The shortest link is 3 and the longest 8, and $3 + 8 = 11 \le 6 + 7 = 13$, so the chain is Grashof. The shortest link is the input, next to the ground, so it is a crank-rocker. (b) With the shortest link grounded, both its neighbors turn fully: a double crank, or drag link. (c) $4 + 9 = 13 > 5 + 7 = 12$, so no link turns fully in any inversion: a triple rocker.

2. The stroke is $\sqrt{(b + a)^2 - e^2} - \sqrt{(b - a)^2 - e^2} = \sqrt{165} - \sqrt{45} \approx 12.845 - 6.708 = 6.137$. The crank turns fully because $b = 10 \ge a + |e| = 5$.

3. $K_1 = d/a = 9/4$, $K_2 = d/c = 9/7$ and $K_3 = (a^2 - b^2 + c^2 + d^2)/(2ac) = 46/56 = 23/28$. Since $4 + 10 \le 7 + 9$ and the shortest link is the input, it is a crank-rocker. At $\varphi = 0$ the equation becomes $(K_1 - 1)\cos\psi = K_2 - K_3 = 13/28$, so $\cos\psi = 13/35$ and $\psi = 68.20°$ or $291.80°$, one value for each circuit.

5. The points are $x_k = 5 + 5\cos\big((2k - 1)\pi/8\big)$, which gives $0.3806$, $3.0866$, $6.9134$ and $9.6194$. The product equals $(5^4/2^3)\, T_4\big((x - 5)/5\big)$, so its largest absolute value is $625/8 = 78.125$.

8. The pitch radii are $mz/2 = 27$ and $67.5$ mm, so $c = 94.5$ mm. The speed ratio is $\omega_2/\omega_1 = -18/45 = -2/5$, the minus sign for external gears. The base radii are $r\cos 20° = 25.372$ and $63.429$ mm, and the base pitch is $\pi m \cos 20° = 8.856$ mm.

9. The limit is $z \ge 2/\sin^2\varphi$, which is $17.10$ at $20°$ and $11.20$ at $25°$, so 18 and 12 teeth. An 11-tooth gear undercuts at $25°$. A shift removes the undercut when $x \ge 1 - z\sin^2\varphi/2$, which is $x \ge 0.415$ for 10 teeth at $20°$.

10. The numbers fit because $30 + 2 \cdot 20 = 70$. From sun to ring through the planet, $e = (-30/20)(+20/70) = -3/7$. With the ring held, $-\omega_A = -\tfrac37(\omega_S - \omega_A)$, so $\omega_A = 0.3\,\omega_S = 300$ rpm and the reduction is $10/3$. For the planet, $\omega_P - \omega_A = -\tfrac{30}{20}(\omega_S - \omega_A)$, which gives $\omega_P = -750$ rpm. Equal spacing needs $(z_S + z_R)/N = 100/N$ to be an integer, so 3 planets fail and 4 fit.

11. For $b \ge 2$ the input is shortest. With 6 as the longest, Grashof needs $2 + 6 \le 5 + b$, so $b \ge 3$. With $b$ as the longest, it needs $2 + b \le 11$, so $b \le 9$. So the linkage is a crank-rocker for $3 \le b \le 9$. For $b < 2$ the coupler is shortest, and $b + 6 \le 7$ gives a Grashof double rocker for $b \le 1$. It is a triple rocker for $1 < b < 3$ and for $b > 9$. The change points are $b = 1$, $3$ and $9$.

16. The crank pin is $A = (0, 4)$. Intersect the circle of radius 10 about $A$ with the circle of radius 7 about $O_4$ to get $B \approx (9.545, 6.979)$, so $\theta_4 = 85.53°$ and $\theta_3 = 17.33°$. The center $P_{24}$ is where line $AB$ meets the ground line, at $x = -12.819$. Then $\omega_4/\omega_2 = P_{24}/(P_{24} - d) = 0.5875$, and $\omega_3/\omega_2 = 0.0336$, from $P_{13}$ where lines $O_2A$ and $O_4B$ meet. On the other circuit, $\theta_4 = 226.55°$ and $\omega_4/\omega_2 = -0.2576$.

21. With $r_a = r + m$, each gear contributes $\sqrt{r_a^2 - r_b^2}$: $16.009$ and $30.773$. Subtract $c\sin\varphi = 32.321$ to get a length of action of $14.461$ mm, and divide by the base pitch to get $m_c = 1.633$. There is no interference, because $16.009$ and $30.773$ are both less than $32.321$. At $c = 96$ mm, $\cos\varphi' = (r_{b1} + r_{b2})/c$, which gives $\varphi' = 22.33°$ and $m_c = 1.164$. That is below the usual $1.2$.

24. The arcs are: $+x$, $A \to B$; $+y$, $A \to C$ and $B \to C$; $-x$, $B \to A$; $-y$, $C \to A$ and $C \to B$. A set can move off when no arc leaves it, which gives the following.

| direction | sets that can move off |
|---|---|
| $+x$ | $\{B\}$, $\{C\}$, $\{A,B\}$, $\{B,C\}$ |
| $+y$ | $\{C\}$, $\{A,C\}$, $\{B,C\}$ |
| $-x$ | $\{A\}$, $\{C\}$, $\{A,B\}$, $\{A,C\}$ |
| $-y$ | $\{A\}$, $\{B\}$, $\{A,B\}$ |

All three splits, $\{A\}\{B,C\}$, $\{B\}\{A,C\}$ and $\{C\}\{A,B\}$, are feasible.

25. With $\cos\mu = (b^2 + c^2 - a^2 - d^2 + 2ad\cos\theta)/(2bc)$, the extremes are at $\theta = 0$ and $180°$. They depart equally from $90°$ when the constant term vanishes, so $b^2 + c^2 = a^2 + d^2 = 40$ and $b = c = 2\sqrt5 \approx 4.472$. Then $\cos\mu = 0.6\cos\theta$ and $\mu$ runs from $53.13°$ to $126.87°$. Since $2 + 6 \le 2\sqrt5 + 2\sqrt5$, it is a Grashof crank-rocker.

26. Each point gives one linear equation, $K_1\cos\psi_i - K_2\cos\varphi_i + K_3 = \cos(\varphi_i - \psi_i)$. Solve the $3 \times 3$ system for $K = (1.4404, 1.4855, 1.4323)$. Then $a = d/K_1 = 6.943$, $c = d/K_2 = 6.732$ and $b^2 = a^2 + c^2 + d^2 - 2acK_3$, so $b = 7.722$. Since $6.732 + 10 > 6.943 + 7.722$, the linkage is a triple rocker. The input has limit positions near $\pm 116°$, so it can move from $30°$ to $90°$ on one branch. The transmission angles are $42.2°$, $75.4°$ and $114.6°$.

27. The third pivot is $O_C = O_A + z(O_B - O_A) = (6, 6)$. The cognate on $O_A$ and $O_C$ has lengths $|z|(b, a, c)$ and ground $|z|\,d$, with $|z| = \sqrt2$: a link of $7.071$ at $O_A$, coupler $2.828$, a link of $5.657$ at $O_C$, and ground $8.485$. Its shortest link is the coupler, so it is a Grashof double rocker. The cognate on $O_B$ and $O_C$ has $|1 - z| = 1$: a link of 5 at $O_B$, coupler 4, a crank of 2 at $O_C$, and ground 6, so it is a crank-rocker. Its crank is $-(z - 1)(A - O_A)$, so it turns at the same rate as the original crank but is offset by $\arg(1 - z) = -90°$. It is parallel to the original crank only when $z$ is real.

28. Each addendum circle must meet the line of action no farther out than the tangent point of the other base circle: $\sqrt{(r + m)^2 - r^2\cos^2\varphi} \le c\sin\varphi = 2r\sin\varphi$. Squaring gives $3r^2\sin^2\varphi - 2rm - m^2 \ge 0$, and $r = mz/2$ gives the stated form. The positive roots are $8.36$, $12.32$ and $22.23$, so 9, 13 and 23 teeth.

29. There are 8 liaisons and 29 connected sets. Of the 96 orders in which each new part touches one already placed, 80 are feasible. The 16 that fail put the block last, when the base, the posts and the lid close it in on all four sides. There are 68 two-handed plans, and 40 of them are linear; each linear plan gives two orders, because the first two parts can swap. Count by computer, testing each split in the four directions.

30. For a radial roller follower, $\tan\phi = s'/(R_p + s)$, with $s' = ds/d\theta$ in mm per radian. So $R_p \ge \max_\theta \big(s'/\tan 30° - s\big)$. For the 3-4-5 law, $s = L(10u^3 - 15u^4 + 6u^5)$ and $s' = (30L/\beta)\,u^2(1 - u)^2$. The maximum comes at $u \approx 0.43$ and gives $R_p = 16.80$ mm, against $18.22$ mm for the cycloidal law. Over $\beta = 90°$, the 3-4-5 law needs $24.30$ mm.
