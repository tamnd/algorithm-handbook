1. The columns of $S$ are $(-1, -1, 1, 0)$, $(1, 1, -1, 0)$ and $(0, 0, -1, 1)$, so the rank is 2. The vectors $(1, -1, 0, 0)$ and $(1, 0, 1, 1)$ are orthogonal to every column: $x_A - x_B$ and $x_A + x_C + x_D$ are constant. The ODE is $A' = B' = -k_1AB + k_2C$, $C' = k_1AB - (k_2 + k_3)C$, $D' = k_3C$.

4. The propensities are 2 and 2, so $a_0 = 4$ and $\tau = \ln 2/4 \approx 0.173$. Then $U_2 a_0 = 2.8$, which exceeds the first propensity, so the death reaction fires and $x = 3$.

5. The state 000 is a fixed point and only it leads there. The other seven states end in the cycle $010 \to 100 \to 011 \to 010$.

6. Steady state gives $v_1 = v_2 + v_3$, $v_3 = v_5$ and $v_4 = v_2 + v_5$, so $v_4 = v_1 \le 10$. The optimum is 10, reached by every $v_3 = v_5 \in [0, 3]$ with $v_2 = 10 - v_3$. The value is unique, the vector is not.

7. The mutual informations are 0.511, 0.337 and 0.188, so the edge $X$-$Z$ is removed at $\tau = 0$. With $\tau = 0.5$ it is removed only if $0.188 < 0.5 \cdot 0.337 = 0.168$, which is false, so it stays.

9. The count at $t = 2$ is Poisson with mean 2, and the error is the mass outside the set: $1 - \sum_{k \le 5} e^{-2}2^k/k! \approx 0.0166$.

11. The first has three complexes in one linkage class and rank 2, so $\delta = 0$, and it is weakly reversible. For every choice of positive rate constants, each class $\{x > 0 : x_A - x_B = a,\ x_A + x_C + x_D = b\}$ holds exactly one equilibrium, locally asymptotically stable within the class. The second has four complexes, two linkage classes and rank 1, so $\delta = 1$.

14. Subtracting $u(1 + v^2) = 3$ and $v(1 + u^2) = 3$ gives $(u - v)(1 - uv) = 0$. The outer pair is $((3 \mp \sqrt5)/2, (3 \pm \sqrt5)/2)$, with $h'(u)h'(v) = 4/9$ and eigenvalues $-1/3$ and $-5/3$: stable nodes. The symmetric point solves $u^3 + u = 3$, $u \approx 1.2134$, where the slope has size $2u^2/(1 + u^2) \approx 1.19 > 1$, so the eigenvalues $0.19$ and $-2.19$ make it a saddle.

20. Compute $P(\min > s,\ \text{index} = j) = \int_s^\infty a_j e^{-a_jr}\prod_{i \ne j}e^{-a_ir}\,dr = (a_j/a_0)e^{-a_0s}$. It factors into a function of $j$ and a function of $s$.

21. Given that reaction $k$ has not fired by $t$, its remaining time is exponential with rate $a$ by the memoryless property. Multiplying an exponential with rate $a$ by $a/a'$ gives an exponential with rate $a'$.

22. At a fixed point with $y = 0$ the rule demands $0 = \varphi(x) \vee 1$, which is impossible. With $y = 1$ it demands $\varphi(x) = 1$.

23. A steady flux sends the same total through each step. A minimal support uses one of the two reactions at each step, since otherwise one of them can be dropped. Each of the $2^n$ choices gives a mode, and the network has only $2n + 2$ reactions.

24. The Jacobian is $-I - gP$, where $P$ is the cyclic shift, whose eigenvalues are the cube roots of unity. For $\omega = e^{\pm 2\pi i/3}$ the real part is $-1 + g/2$.
