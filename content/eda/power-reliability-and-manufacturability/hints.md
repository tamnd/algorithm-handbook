1. Multiply per line and then by 64: $0.2 \cdot 50 \cdot 10^{-15} \cdot 0.81 \cdot 1.5 \cdot 10^9 = 12.15\ \mu$W per line, so 0.778 mW for the bus.

2. The output is 1 when exactly one input is 1, so $p = 2 \cdot \frac14 \cdot \frac34 = 3/8$. Temporal independence gives $\alpha = 2p(1-p) = 15/32$, and the rising activity is half of that, $15/64$.

5. The rule $z s / \sqrt N < \varepsilon \bar x$ becomes $N > (1.96 \cdot 0.3 / 0.05)^2 = 138.3$, so 139 samples. Most implementations also impose a minimum such as 30 samples, because the rule leans on the central limit theorem.

6. Floating: $6/(6 + 18) = 0.25$ V. Driven: effective loads of 20, 30 and 40 fF give 13.8, 20.7 and 27.6 ps. The delay-based factor, fitted so that the grounded model gives the true delay, can lie outside $[0, 2]$ even for equal ramps.

8. Poisson $e^{-0.5} = 0.6065$; Murphy $((1 - e^{-0.5})/0.5)^2 = 0.6193$; negative binomial $(1 + 0.25)^{-2} = 0.64$. The order is the one that exercise 26 proves.

10. $L_B = 2500 / (1.25 \cdot 10^6)$ cm $= 20$ µm. For 25 µm the current density must satisfy $j \le 2500 / 0.0025 = 10^6$ A/cm², that is 1 MA/cm².

12. Gate by gate, $P(a \wedge b) = 1/4$ and the XOR of "independent" signals with probabilities $1/2$ and $1/4$ gives $1/2$, but $y = a \wedge \neg b$ has probability $1/4$: an overestimate. For $z$ the formula gives $\frac12 \cdot \frac34 = 3/8$, but $z = a$ has probability $1/2$: an underestimate. So the gate-by-gate value is not a bound in either direction.

14. $y$ toggles when it is 1 and not both inputs stay at 1, or the other way. $P(y_k = 1, y_{k+1} = 0) = \frac14 (1 - 0.81) = 0.0475$, and by stationarity the reverse has the same probability, so $\alpha = 0.095 = 19/200$. Temporal independence gives $2 \cdot \frac14 \cdot \frac34 = 3/8$, four times too much.

15. Under zero delay each gate output is a fair coin before and after, so each toggles with probability $1/2$: $3/2$ in total for both shapes. In the tree both inputs of every gate change at the same time, so there are no glitches and unit delay also gives $3/2$. In the chain the second gate can change at times 1 and 2 and the last at times 1, 2 and 3, and an exhaustive count over the 256 pairs of input vectors gives 3 expected transitions, so half of the chain's activity is glitches.

17. All low has delay 30, leakage 72 and slack 6. Raising costs 4, 3 and 3 units of delay and saves 30, 14 and 22. The greedy rule takes $g_1$ first (7.5 per unit), and then neither other gate fits in the 2 units left, so it ends at leakage 42. Raising $\{g_2, g_3\}$ uses exactly 6 units and saves 36, which gives leakage 36, the optimum. This is the knapsack structure of the problem.

19. On a chain the drop at node $k$ is the resistance of the common path times each current, so $G^{-1}$ has row 3 equal to $(1/40, 3/40, 1/8)$ Ω and the drops are 15, 35 and 45 mV. For the worst case, fill the largest entries first, a fractional knapsack: $i_3 = 0.4$, $i_2 = 0.2$ gives $0.05 + 0.015 = 65$ mV. Without the total bound every current goes to 0.4 A and the drop is 90 mV.

20. The expected number of visits to node $j$ from node 3 is $(G^{-1})_{3j} D_j$, with $D = (60, 40, 20)$ the total conductances. That gives $(3/2, 3, 5/2)$, and the expected reward $\frac32 \cdot \frac{0.2}{60} + 3 \cdot \frac{0.2}{40} + \frac52 \cdot \frac{0.2}{20} = 0.045$ V. A run of 20000 walks with `random.Random(7)` gave a mean of 0.0448 with standard error 0.0002.

22. Solve $(1 + \lambda/2)^{-2} = 0.7$ for $\lambda = 2(0.7^{-1/2} - 1) = 0.3905$. Doubling the area doubles $\lambda$, so the yield is $(1 + 0.3905)^{-2} = 0.517$. Poisson gives $0.7^2 = 0.49$, which is lower, because it ignores clustering.

24. The window of the last two tiles has density at most $(0.6 + 0.3)/2 = 0.45$ even with full fill, so 0.45 is an upper bound, and the fill $(0.05, 0.05, 0.15, 0.15)$ makes all three windows equal to 0.45. The last window forces 0.3 of fill, the middle one at least 0.05 more on tile 2, and the first window at least 0.1 in total on tiles 1 and 2, so 0.4 is the least total.

26. The function $x \mapsto e^{-\lambda x}$ is convex, so Jensen's inequality gives $E[e^{-\lambda X}] \ge e^{-\lambda E[X]}$. For the second part, write $\ln Y = -\alpha \ln(1 + \lambda/\alpha)$ and differentiate in $\alpha$: with $x = \lambda/\alpha$ the derivative is $-\ln(1 + x) + x/(1 + x)$, which is negative for $x > 0$. The limit follows from $\alpha \ln(1 + \lambda/\alpha) \to \lambda$.

27. A toggle needs a 1 in cycle $k$ or in cycle $k+1$, so $\alpha = P(y_k \ne y_{k+1}) \le P(y_k = 1) + P(y_{k+1} = 1) = 2p$, and the same with zeros gives $2(1 - p)$. Equality holds when two 1s never follow each other. For a four-input AND gate $p = 1/16$, so $\alpha \le 1/8$. One input that alternates with a random phase makes the output 1 in at most every other cycle, and this reaches $1/8$.

28. Iterating from $\theta = 0$ gives $\theta = 42.85$ K. The map has derivative $0.2 R e^{0.02 \theta}$, which is $0.38$ at the fixed point, so it is a contraction near it. A fixed point disappears where the curve becomes tangent: $0.2 R e^{0.02 \theta} = 1$ and $\theta = R(30 + 10 e^{0.02 \theta})$. Eliminating the exponential gives $50 \ln(5/R) = 30 R + 50$, so $R \approx 1.006$ K/W, with $\theta \approx 80.2$ K at the tangency.

29. The eigenvalues are 4 and 2, with eigenvectors $(1, 1)/\sqrt2$ and $(1, -1)/\sqrt2$. For $u = (1, 1)$ the full intensity is 8 and one kernel gives 8: error 0. For $u = (1, -1)$ the full intensity is 4 and one kernel gives 0: error $4 = \lambda_2 \|u\|^2$. In general the error is $\lambda_2 |v_2^* u|^2$, which is at least 0 and at most $\lambda_2 \|u\|^2$.
