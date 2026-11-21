1. $\mathrm{BLER}_j = 0.1$ when $e^{1.5(\gamma - t_j)} = 9$, so the thresholds are $t_j + \ln 9/1.5 = t_j + 1.465$:
$-0.54$, $2.46$, $7.46$, $11.46$ and $16.46$ dB. At 8 dB the throughputs are $0.500$, $1.000$, $1.905$,
$0.142$ and $0.000$. Scheme 3 is the fastest whose threshold is below 8 dB, and it also has the best
throughput.

4. The best users are 1, 2, 1, 3, 3, 2, for $4 + 3 + 2 + 4 + 3 + 4 = 20$ bits; users 1, 2 and 3 get 6, 7 and
7. Round robin gets $4 + 3 + 1 + 3 + 2 + 1 = 14$.

5. With all three active, $\mu = (2 + 3.5)/3 = 1.833 < 2$, so the third is off. With two,
$\mu = (2 + 1.5)/2 = 1.75$, and the powers are $(1.25, 0.75, 0)$. The rate is
$\log_2 3.5 + \log_2 1.75 = 2.615$ bits; equal powers of $2/3$ give $2.374$.

7. $P_{fa} = e^{-\lambda} = 0.01$ gives $\lambda = \ln 100 = 4.605$. Then $P_d = e^{-4.605/11} = 0.658$.

10. The next-bit costs are $2^{b-1}/g_i$: $0.1, 0.2, 0.4, 0.8, \ldots$ on subcarrier 1,
$0.25, 0.5, 1, \ldots$ on 2 and $0.667, 1.333, \ldots$ on 3. The six cheapest are
$0.1, 0.2, 0.25, 0.4, 0.5, 0.667$, so the loading is $(3, 2, 1)$ with power $127/60 = 2.117$; two bits each
cost $3.05$. For $P = 3$ the seventh bit (0.8, on subcarrier 1) brings the power to $2.917$, and the eighth
(1.0) would exceed 3, so 7 bits fit, as $(4, 2, 1)$.

13. $F = \gamma[[0, 0.2], [0.3, 0]] = [[0, 0.4], [0.6, 0]]$ and $u = (0.2, 0.2)$. $\rho(F) = \sqrt{0.24} = 0.490 < 1$,
so the target is feasible, and $p^* = (I - F)^{-1}u = (0.28, 0.32)/0.76 = (0.368, 0.421)$. The spectral
radius is $\gamma\sqrt{0.06}$, so targets below $1/\sqrt{0.06} = 4.08$ are feasible.

14. (a) is standard, with the fixed point 2. (b) is positive and monotone, but $\alpha I(p) > I(\alpha p)$
fails when $\alpha p^2 \ge 0.1$, so it is not scalable; it has two fixed points, $(1 \pm \sqrt{0.6})/2 = 0.113$
and $0.887$, which a standard function cannot have. (c) is the minimum of (a) and the constant 3, both
standard, so it is standard; its fixed point is 2.

15. The constraint $p = t(Fp + u)$ with $\mathbf 1^\top p = 1$ gives $p = tAp$ with
$A = F + u\mathbf 1^\top = [[0.1, 0.35], [0.26, 0.1]]$. Then $\rho(A) = 0.1 + \sqrt{0.35 \cdot 0.26} = 0.4017$
and $t^* = 2.490$, with the Perron vector $p = (0.537, 0.463)$. Without noise, $t = 1/\sqrt{0.25 \cdot 0.16} = 5$.

16. For a fixed $q$ the subproblem has $p = 1/(q\ln 2) - 1/4$, clipped to $[0, 10]$. From $q_0 = 0$:
$p = 10$, $q = 0.510$; $p = 2.578$, $q = 1.137$; $p = 1.019$, $q = 1.543$; $p = 0.685$, $q = 1.606$;
$p = 0.648$, $q = 1.607$. Full power gives $0.510$, less than a third of the optimum.

17. The sum rates are $3.401$ (both to user 1), $3.919$ (subcarrier 1 to user 1, 2 to user 2), $3.059$
(1 to user 2, 2 to user 1) and $3.590$ (both to user 2). The winner gives each subcarrier to its best user,
with the water level $1.375$ and the powers $(1.125, 0.875)$.

19. The throughput is $R\,e^{-(2^R - 1)/100}$: $3.443$ for $R = 4$, $3.667$ for $R = 5$ and $3.196$ for
$R = 6$. The best integer rate is 5; the best real rate, about 4.88, gains less than 0.01.

22. Round 1 at 0 dB: real rates $(4.954, 3.700, 2.000)$, rounded $(5, 4, 2)$, 11 bits; the step is
$10\log_{10}2^{4/3} = 4.01$ dB. Round 2: $(3.690, 2.527, 1.131)$, rounded $(4, 3, 1)$, 8 bits; the step is
$+1.00$ dB. Round 3 gives $(3, 2, 1)$, 6 bits, and a step of $-1.00$ dB: the loop oscillates between 8 and 6
bits, and only the fix-up by rounding errors reaches 7.

23. Fix any assignment and its optimal powers. Replace the user of each subcarrier by the user with the
largest gain there, keeping the powers: no rate falls, because $\log_2(1 + gp)$ grows with $g$. Water-filling
on the new gains can only add more. So some optimal solution uses the best-user assignment.

24. $F = \gamma[[0, a], [b, 0]]$ has $\rho(F) = \gamma\sqrt{ab}$, and $(I - F)p = u$ has a positive solution
for positive $u$ exactly when $\rho(F) < 1$. Explicitly $p_1 = (u_1 + \gamma a u_2)/(1 - \gamma^2ab)$, which
grows without bound as $\gamma^2ab \to 1$.

25. Sort the variables. By memorylessness the smallest is exponential with rate $K$, the gap to the next
is exponential with rate $K - 1$, and so on, so the maximum is a sum of independent gaps with means
$1/K, 1/(K - 1), \ldots, 1$. $H_K - \ln K$ tends to Euler's constant $0.5772$. The best of $K$ users has
mean SNR $H_K\bar\gamma \approx \bar\gamma(\ln K + 0.577)$.

26. For $q < q'$ and the maximizer $p'$ of $F(q')$, $F(q) \ge R(p') - qP(p') > F(q')$, since $P(p') > 0$.
$F(q) \ge 0$ exactly when some $p$ has $R(p)/P(p) \ge q$, so the root is $q^*$. If $p_t$ maximizes
$R - q_tP$, then $F(q_t) \ge 0$ gives $q_{t+1} = R(p_t)/P(p_t) \ge q_t$.

27. Positivity and monotonicity pass through min and max at once. For scalability with $\alpha > 1$,
$\alpha\min(I, J)(p) = \min(\alpha I(p), \alpha J(p)) > \min(I(\alpha p), J(\alpha p))$, and the same for
max. The constant $\bar p$ is standard, so $\min(I, \bar p)$ is standard. The vector $\bar p$ is feasible for
it, since $\min(I(\bar p), \bar p) \le \bar p$, so Yates's theorem gives a unique fixed point and
convergence from any start.
