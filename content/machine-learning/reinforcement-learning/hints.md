1. $G_3 = -1$, $G_2 = 2 - \tfrac12 = \tfrac32$, $G_1 = 0 + \tfrac34 = \tfrac34$ and $G_0 = 1 + \tfrac38 = \tfrac{11}{8}$. The length has the geometric law with success probability $1 - \gamma$, so its mean is $1/(1-\gamma) = 2$.

3. $V_1 = (1, 2)$, $V_2 = (1.9, 3.8)$ and $V_3 = (3.42, 5.42)$. For $V_1$ the greedy choice in $s_1$ compares $1 + 0.9 \cdot 1 = 1.9$ with $0.9 \cdot 2 = 1.8$ and still stays; for $V_2$ it compares $2.71$ with $3.42$ and goes. So the greedy policy is optimal from $V_2$ on, while the values are still far from $V^* = (18, 20)$. *Go* is better exactly when $2\gamma/(1-\gamma) > 1/(1-\gamma)$, that is when $\gamma > 1/2$.

4. The error is at most $\gamma^k/(1-\gamma)$. For $\gamma = 0.9$ you need $0.9^k \le 10^{-3}$, so $k \ge 65.6$ and 66 sweeps suffice. For $\gamma = 0.99$ you need $0.99^k \le 10^{-4}$, so $k \ge 916.4$ and 917 sweeps suffice.

6. $U_1 = 2/3 + \sqrt{2\ln 10/3} \approx 0.667 + 1.239 = 1.906$ and $U_2 = 5/7 + \sqrt{2\ln 10/7} \approx 0.714 + 0.811 = 1.525$. Arm 1 is pulled: it has the lower mean but fewer pulls, so its confidence interval is wider and its upper end is higher.

7. Q-learning: target $1 + 0.9 \cdot 5 = 5.5$, new value $4.75$. SARSA: target $1 + 0.9 \cdot 3 = 3.7$, new value $3.85$. Expected SARSA: the ε-greedy probabilities are $(0.1, 0.8, 0.1)$, the mean is $4.5$, the target $5.05$ and the new value $4.525$.

9. The ratios $\prod \pi/\mu$ are $4, 0, 0, 4$. The ordinary estimate is $(4 \cdot 2 + 4 \cdot 4)/4 = 6$, and the weighted estimate is $24/8 = 3$. The ordinary estimate is unbiased; the weighted one is biased but has a smaller variance.

13. Monte Carlo: $V(A) = 1$, $V(B) = 2$ and $V(C) = (1 + 0 + 0)/3 = 1/3$. The model of the data sends A and B to C with rewards 0 and 2, and C ends with mean reward $1/3$, so batch TD(0) gives $V(C) = 1/3$, $V(A) = 1/3$ and $V(B) = 7/3$.

15. The exploration coins are independent. With $\varepsilon_t = 1/t$ each arm is explored in round $t$ with probability $1/(Kt)$, and these sum to infinity, so by the second Borel-Cantelli lemma each arm is explored infinitely often. With $1/t^2$ the sum is finite, and the first lemma applies. For the example take means $0.9$ and $0.5$, with an untried arm valued $+\infty$ as in the entry. With probability $\tfrac34 \cdot 0.1 \cdot 0.5$ the first two rounds pull both arms, arm 1 pays 0 and arm 2 pays 1; with probability $\prod_{t \ge 3}(1 - 1/t^2) = 2/3$ no later round explores. Then the estimate of arm 2 stays positive and that of arm 1 stays 0, so arm 2 is pulled forever, with probability at least $0.025$.

16. The posteriors are $\mathrm{Beta}(4, 2)$ and $\mathrm{Beta}(2, 2)$. The answer is $\Pr[X > Y] = \int_0^1 6y(1-y)\,(1 - 5y^4 + 4y^5)\,dy = 1 - 2/7 = 5/7$, since $1 - 5y^4 + 4y^5$ is the tail of $\mathrm{Beta}(4, 2)$.

17. $\mathrm{kl}(0.5, 0.6) = \tfrac12\ln(25/24) \approx 0.0204$, so every consistent policy pulls the worse arm at least about $49 \ln n$ times, and $c = 0.1/0.0204 \approx 4.90$. The UCB1 bound has the leading term $80\ln n$, about 16 times more.

21. For the stopping time "after $m$ pulls" the ratio is $(\gamma - \gamma^m)/(1 - \gamma^m)$, which increases to $\gamma$ as $m \to \infty$. With $c = 0.85 < 0.9$, pull the new arm first and keep it: value $\gamma/(1-\gamma) = 9$, against $8.5$ for the safe arm forever. With $c = 0.95$, pull the safe arm forever: $9.5$ against $9$.

23. The row minima are $-1$ and $-2$ and the column maxima are $3$ and $1$, so the pure maximin $-1$ is below the pure minimax $1$. The learner plays row 1 with probability $3/7$, the opponent plays column 1 with probability $2/7$, and the value is $1/7$. The target is $0.9/7 = 9/70 \approx 0.129$.

24. For a greedy $\pi$, $T^\pi V = TV$. So $\lVert V^\pi - V^* \rVert \le \lVert T^\pi V^\pi - T^\pi V \rVert + \lVert TV - TV^* \rVert \le \gamma\lVert V^\pi - V \rVert + \gamma\varepsilon \le \gamma\lVert V^\pi - V^* \rVert + 2\gamma\varepsilon$. Solve for $\lVert V^\pi - V^* \rVert$.

25. The maximum is a convex function, so Jensen's inequality gives the first claim. For the second, the index $i^* = \arg\max_i X_i$ is independent of the $Y$'s, so $\mathbb{E}[Y_{i^*} \mid X] = \mu_{i^*} \le \max_i \mu_i$.

26. The off-policy update is $\theta \leftarrow \theta + \alpha(2\gamma\theta - \theta) \cdot 1$. The on-policy expected update adds the second transition, $\alpha(0 - 2\theta) \cdot 2$, for a total of $\alpha(2\gamma - 5)\theta$, which is negative for every $\gamma \le 1$. The three ingredients are linear function approximation, bootstrapping and off-policy updating.

27. The learner has left the expert's states by step $t$ only if it erred in one of the first $t$ steps, which has probability at most $t\varepsilon$ by a union bound. Summing over $t$ gives $\varepsilon T(T+1)/2$. In the absorbing example $1 - (1-\varepsilon)^t \ge t\varepsilon - t(t-1)\varepsilon^2/2$. DAgger's bound is $uT(\varepsilon_N + \gamma_N + \dots)$, linear in $T$: $u$ bounds the extra cost of one deviation, $\varepsilon_N$ is the best error on the states the learner's own policies visit, and $\gamma_N$ is the average regret of the online learner.

28. $\partial J/\partial\theta_b = \pi_b(r_b - \pi^\top r)$, which is the $b$-th entry of $Fr$. When every $\pi_a > 0$, $Fx = 0$ forces $x_a = \pi^\top x$ for every $a$, so the null space of $F$ is spanned by $\mathbf 1$. Since $F$ is symmetric, $F^+F$ projects onto the vectors orthogonal to $\mathbf 1$, and $F^+\nabla J = r - \bar r\mathbf 1$, which does not depend on $\theta$.
