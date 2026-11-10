1. $\pi = (1/4, 1/2, 1/4)$, from $\pi(0)\cdot\frac12 = \pi(1)\cdot\frac14$ and $\pi(1)\cdot\frac14 = \pi(2)\cdot\frac12$. The chain is irreducible and has period 1, because $P(0, 0) > 0$. Without holding, every return to a state takes an even number of steps, so the period is 2.

5. $\Pr(x_1 = 1 \mid x_2 = 0) = \Pr(x_2 = 1 \mid x_1 = 0) = 1/4$ and $\Pr(x_1 = 1 \mid x_2 = 1) = \Pr(x_2 = 1 \mid x_1 = 1) = 3/4$. Whichever coordinate is chosen, the chain leaves $00$ with probability $1/4$. One step changes one coordinate, so $11$ is out of reach in one step.

8. Each $s_j^2 = 1$, so $W = 1$. The means are 2, 3 and 5, with grand mean $10/3$, so $B = \frac32\cdot\frac{42}{9} = 7$. Then $\widehat{\operatorname{var}}^+ = \frac23 + \frac73 = 3$ and $\hat R = \sqrt3 \approx 1.73$.

11. $\pi = (1/3, 2/3)$ and the second eigenvalue is $1 - a - b = 1/2$. From state 1 the distance is $\frac23 2^{-t}$, which is the larger, so $t_{mix} = 2$ and $t_{mix}(1/100) = 7$. The asymptotic variance is $ab(2 - a - b)/(a + b)^3 = 2/3$, against $\operatorname{Var}_\pi f = 2/9$, so $\tau = 3 = (1 + \lambda)/(1 - \lambda)$.

13. Metropolis-Hastings gives $P(1, 2) = 1$ and $P(2, 1) = 1/2$; Barker gives $2/3$ and $1/3$. The asymptotic variances are $2/27$ and $2/9$, and $\operatorname{Var}_\pi f = 2/9$. So Barker's chain is as good as independent draws here, and the Metropolis-Hastings chain is three times better. This is the order of Peskun's theorem.

15. The two ends of the bridge have degree 5, the other vertices degree 4, and the degrees sum to 42. So $\pi(S) = 1/2$ and $Q(S, S^c) = \frac{5}{42}\cdot\frac12\cdot\frac15 = \frac1{84}$, which gives $\Phi_* = 1/42$. Then $t_{mix} \ge 42/4$, so $t_{mix} \ge 11$, and $1/3528 \le \gamma \le 1/21$. The exact values are $t_{mix} = 21$ and $\gamma \approx 0.0363$.

17. From states 0 and 1 the chain moves to each state with probability $1/3$. From state 2 it moves to 0 and to 1 with probability $1/6$ each. The eigenvalues are 1, $1/3$ and 0, and $d(t) = \frac12 3^{-t}$, half of the bound with $M = 3/2$. The bound needs $t = 5$ to reach $1/100$; the exact distance gets there at $t = 4$.

20. From $(1, 0)$ the step gives $(1/2, -3/4)$, $\Delta H = -3/32$ and acceptance 1. From $(0, 1)$ it gives $(1, 1/2)$, $\Delta H = 1/8$ and acceptance $e^{-1/8} \approx 0.88$. The quantity $p^2/2 + 3q^2/8$ is $3/8$ on the first pair of points and $1/2$ on the second; it is the modified energy $\tilde H_\varepsilon$ of the leapfrog step.

22. Level 0 goes to level 1 with probability $1/3$; level 1 goes to 0 with probability $1/3$ and to 2 with probability $2/3$; the chain is symmetric under $E \mapsto 3 - E$. Detailed balance holds with equal weights, so each level has probability $1/4$: the histogram of energies is flat.

23. The copies coalesce at a step exactly when $u < a$ or $u \ge 1 - b$, so $T_*$ is geometric and $\Pr[T_* > t] = (1 - a - b)^t$. Given coalescence, the merged state is 1 with probability $a/(a + b)$. Every later step, between time $-T_* + 1$ and time 0, has $a \le u < 1 - b$ and keeps the state, so the output is the merged state.

24. Flipping coordinate $i$ multiplies $\chi_S$ by $-1$ if $i \in S$ and leaves it alone otherwise. So $P\chi_S = \frac12\chi_S + \frac1{2n}\big((n - |S|) - |S|\big)\chi_S = (1 - |S|/n)\chi_S$. The $2^n$ functions $\chi_S$ form a basis, so these are all the eigenvalues. The gap is $1/n$, $t_{rel} = n$, and $1 - k/n$ has multiplicity $\binom nk$.

25. With $\pi > 0$ and $Q$ symmetric, every proposed move is accepted with positive probability, so $P$ has the same graph as $Q$ and is irreducible. The graph is connected and $\pi$ is not constant, so some edge $xy$ has $\pi(y) < \pi(x)$, and then $P(x, x) \ge Q(x, y)(1 - \pi(y)/\pi(x)) > 0$. An irreducible chain with one holding state is aperiodic. With $\pi$ uniform and $Q$ the simple walk on the 4-cycle, nothing is rejected and the chain has period 2.

26. The centred function $\bar f = (-1/5, 4/5, -1/5)$ satisfies $P\bar f = -\frac14\bar f$, so it is an eigenvector. Then $\sigma_f^2 = \operatorname{Var}_\pi f\cdot\frac{1 - 1/4}{1 + 1/4} = \frac{4}{25}\cdot\frac35 = \frac{12}{125}$ and $\tau = 3/5$. A run of length $t$ is worth $5t/3$ independent draws, because a nice day is never followed by another.

27. The proposal mean is $x/2$. From 1 to 0, $r = e^{1/2}\cdot e^{-1/2}/e^{-1/8} = e^{1/8} > 1$, so the move is accepted. From 0 to 1, $r = e^{-1/8} \approx 0.88$. Without the accept step, $X' = (1 - \varepsilon^2/2)X + \varepsilon Z$, a stationary AR(1) with variance $\varepsilon^2/(1 - (1 - \varepsilon^2/2)^2) = 1/(1 - \varepsilon^2/4)$, which is $4/3$ for $\varepsilon = 1$.
