1. ◦ An episode gives the rewards $R_1 = 1$, $R_2 = 0$, $R_3 = 2$, $R_4 = -1$ and then ends. With $\gamma = 1/2$, compute the [discounted returns](/discounted-return/) $G_3, G_2, G_1, G_0$ with the recursion $G_t = R_{t+1} + \gamma G_{t+1}$. If instead the episode had no end and stopped after each step with probability $1 - \gamma$, what would its expected length be?

2. ◦ A policy in a two-state MDP gives these dynamics: from state a the reward is 1 and the next state is b; from state b the reward is 0 and the next state is a or b with probability $1/2$ each. With $\gamma = 0.9$, solve the [Bellman expectation equation](/bellman-expectation-equation/) for $V(a)$ and $V(b)$ exactly.

3. ◦ An MDP has two states. In $s_1$ the action *stay* pays 1 and stays in $s_1$, and the action *go* pays 0 and moves to $s_2$. In $s_2$ the only action pays 2 and stays in $s_2$. With $\gamma = 0.9$, run three synchronous sweeps of [value iteration](/value-iteration/) from $V_0 = 0$. After which sweep is the greedy policy for $V_k$ first optimal? What is $V^*$? For which discounts $\gamma$ is *go* the better action?

4. ◦ Rewards lie in $[-1, 1]$ and value iteration starts from $V_0 = 0$. Using only $\lVert V_k - V^* \rVert_\infty \le \gamma^k \lVert V_0 - V^* \rVert_\infty$ and $\lVert V^* \rVert_\infty \le 1/(1 - \gamma)$, how many sweeps guarantee an error of at most $0.01$ when $\gamma = 0.9$? When $\gamma = 0.99$?

5. ◦ A bandit has four Bernoulli arms with means $0.9$, $0.8$, $0.5$ and $0.5$, and [ε-greedy](/epsilon-greedy/) runs with the constant $\varepsilon = 0.2$. Once the estimates rank the arms correctly, with what probability does a round pull each arm? Show that the expected regret after 1000 rounds is at least 45, however good the estimates are.

6. ◦ Before round $t = 11$ of [UCB1](/ucb1/) on two arms, arm 1 has 3 pulls with total reward 2 and arm 2 has 7 pulls with total reward 5. Compute both indices, with the bonus $\sqrt{2 \ln(t-1)/N}$. Which arm is pulled, and why is it not the arm with the higher mean?

7. ◦ A step from $S$ with action $A$ gives $R = 1$ and $S'$, where $Q(S', \cdot) = (2, 5, 3)$ over three actions and $Q(S, A) = 4$. The policy is ε-greedy with $\varepsilon = 0.3$, and the action it draws in $S'$ is the third one. With $\gamma = 0.9$ and $\alpha = 1/2$, give the new $Q(S, A)$ after an update of [Q-learning](/q-learning/), of [SARSA](/sarsa/) and of [Expected SARSA](/expected-sarsa/) with the ε-greedy target policy.

8. ◦ An episode goes from A to B with reward 0 and from B to the end with reward 1, and $\gamma = 1$. The current values are $V(A) = 0.5$ and $V(B) = 0.2$. Compute the two [TD errors](/td-error/) and check that their sum is $G_0 - V(A)$. Then give the new values after one pass of [TD(0)](/temporal-difference-learning/) and after one update of [Monte Carlo evaluation](/monte-carlo-policy-evaluation/), both with $\alpha = 0.1$.

9. ◦ A behavior policy picks L or R with probability $1/2$ each, in each of two steps; the target policy always picks L. Four episodes are logged: (L, L) with return 2, (L, R) with return 0, (R, L) with return 1, and (L, L) with return 4. Compute the ordinary and the weighted [importance sampling](/importance-sampling-off-policy/) estimates of the target policy's value. Which of the two is unbiased?

10. ◦ Which of these step-size sequences meet the [Robbins-Monro conditions](/robbins-monro-conditions/) $\sum_t a_t = \infty$ and $\sum_t a_t^2 < \infty$: $1/t$, $1/\sqrt t$, $1/t^2$, the constant $0.1$, $10/(t + 100)$, and $1/(t \ln t)$ for $t \ge 2$?

11. • Give a one-state MDP in which the bound $\lVert V_k - V^* \rVert_\infty \le \gamma^k \lVert V_0 - V^* \rVert_\infty$ of value iteration holds with equality for every $k$. What does this say about the factor $1/(1-\gamma)$ in the number of sweeps?

12. • Let $P^\pi$ be the transition matrix of a policy in a finite MDP and $0 \le \gamma < 1$. Show that $I - \gamma P^\pi$ is invertible, that its inverse is $\sum_{k \ge 0} \gamma^k (P^\pi)^k$, and that this inverse has nonnegative entries and row sums $1/(1-\gamma)$. Deduce $\lVert V^\pi \rVert_\infty \le R_{\max}/(1-\gamma)$.

13. • Three episodes are logged, with $\gamma = 1$: (A, 0, C, 1, end), (B, 2, C, 0, end) and (C, 0, end), where each triple is a state, the reward of the step, and the next state. Find the batch Monte Carlo estimates of $V(A)$, $V(B)$ and $V(C)$, and the batch TD(0) estimates, which are the values of the maximum likelihood model of the data.

14. • Two actions both have the true value 0. Their estimates $X_1$ and $X_2$ are independent with law $N(0, \sigma^2)$. Show that $\mathbb{E}[\max(X_1, X_2)] = \sigma/\sqrt{\pi}$. Then let $Y_1, Y_2$ be a second, independent pair of such estimates, and show that the double estimate $Y_{\arg\max_i X_i}$ of [Double Q-learning](/double-q-learning/) has mean 0.

15. • In a $K$-armed bandit, ε-greedy explores in round $t$ with probability $\varepsilon_t$, by a coin flip independent of everything else. Show that with $\varepsilon_t = 1/t$ every arm is pulled infinitely often with probability 1, while with $\varepsilon_t = 1/t^2$ there are only finitely many exploration rounds with probability 1. Give a two-armed Bernoulli bandit on which the second schedule keeps pulling the worse arm forever with positive probability.

16. • Two Bernoulli arms have uniform priors. Arm 1 has paid 1 three times and 0 once, and arm 2 has paid 1 once and 0 once. With what probability does [Thompson sampling](/thompson-sampling/) pull arm 1 in the next round? Give the exact number.

17. • Two Bernoulli arms have means $0.6$ and $0.5$. Compute $\mathrm{kl}(0.5, 0.6)$ and the constant $c$ in the [Lai-Robbins bound](/lai-robbins-lower-bound/), $\liminf_n R_n/\ln n \ge c$, for every consistent policy. Compare it with the leading constant $8/\Delta$ of the UCB1 bound.

18. • In the adversarial bandit, the reward table is fixed in advance but may depend on the algorithm. Show that every deterministic algorithm on two arms has regret at least $n/2$ on some table with rewards in $\{0, 1\}$. Why does this not contradict the $O(\sqrt{nK \log K})$ bound of [EXP3](/exp3/)?

19. • A one-state problem has two actions with rewards 1 and 0, and a softmax policy with parameters $\theta = (\theta_1, \theta_2)$. At $\theta = 0$, find the mean and the variance of the first component of the [REINFORCE](/reinforce/) estimate $R\,\nabla_\theta \log \pi(A)$ from one sample. Repeat with the baseline $b = 1/2$, that is with $(R - b)\nabla_\theta \log \pi(A)$.

20. • In the [linear programming formulation](/linear-programming-for-mdps/) of a discounted MDP, show that every feasible solution $x$ of the dual program has $\sum_{s, a} x(s, a) = \sum_s \alpha(s)/(1-\gamma)$.

21. • An arm starts in state 0, which pays 0 and moves to state 1; state 1 pays 1 in every round and stays. Show that with discount $\gamma$ the [Gittins index](/gittins-index/) of state 0 is $\gamma$. A second arm always pays $c$. With $\gamma = 0.9$, which arm should be pulled first when $c = 0.85$, and when $c = 0.95$? Check both answers by computing the values of the two plans.

22. • Show that the operator of the λ-return, $(1-\lambda)\sum_{n \ge 1} \lambda^{n-1} (T^\pi)^n$, is a contraction in the max norm with modulus $\gamma(1-\lambda)/(1-\gamma\lambda)$. What are the moduli at $\lambda = 0$ and as $\lambda \to 1$, and why does that not make $\lambda$ near 1 the best choice for [TD(λ)](/td-lambda/)?

23. • The learner and the opponent of [minimax-Q](/minimax-q/) face the matrix game with rows $(3, -1)$ and $(-2, 1)$, where the learner picks the row and wants a large payoff. Show that the game has no saddle point in pure strategies, and find its value and the learner's optimal mixed strategy. What is the minimax-Q target $r + \gamma V(s')$ if this is $Q(s', \cdot, \cdot)$, $r = 0$ and $\gamma = 0.9$?

24. ★ Let $\lVert V - V^* \rVert_\infty \le \varepsilon$ and let $\pi$ be greedy for $V$. Prove that $\lVert V^\pi - V^* \rVert_\infty \le 2\gamma\varepsilon/(1-\gamma)$.

25. ★ Let $X_1, \ldots, X_K$ be independent unbiased estimates of $\mu_1, \ldots, \mu_K$, and $Y_1, \ldots, Y_K$ a second set, independent of the first. Prove that $\mathbb{E}[\max_i X_i] \ge \max_i \mu_i$ and $\mathbb{E}[Y_{\arg\max_i X_i}] \le \max_i \mu_i$. This is the reason the single estimator of Q-learning overestimates and the double estimator does not.

26. ★ Two states have one feature each, 1 and 2, so their values are $\theta$ and $2\theta$. The first state moves to the second with reward 0, and the second ends the episode with reward 0. Show that semi-gradient TD(0) that updates only on the first transition, as an off-policy learner might, multiplies $\theta$ by $1 + \alpha(2\gamma - 1)$ at each update and diverges when $\gamma > 1/2$. Then show that the expected update with both transitions weighted equally, as on-policy sampling gives, converges to $\theta = 0$ for every $\gamma \le 1$ and small $\alpha$. Name the three ingredients of the [deadly triad](/deadly-triad/) in the first case.

27. ★ A cloned policy runs for $T$ steps. While it is on the expert's states it errs with probability at most $\varepsilon$ per step, and after its first error every step, including that one, costs at most 1; steps before the first error cost 0. Show that its expected cost is at most $\varepsilon T(T+1)/2$, and that if each error leads to an absorbing region where every step costs exactly 1 and the error probability is exactly $\varepsilon$, the cost is $\sum_{t=1}^{T}\bigl(1 - (1-\varepsilon)^t\bigr)$, which is about $\varepsilon T^2/2$ when $\varepsilon T$ is small. Compare with the linear bound of [DAgger](/dagger/).

28. ★ A one-state problem has $K$ actions with rewards $r \in \mathbb{R}^K$ and a softmax policy $\pi_\theta$. Show that the gradient of $J(\theta) = \sum_a \pi_\theta(a) r_a$ is $F r$, where $F = \mathrm{diag}(\pi) - \pi\pi^\top$ is the Fisher matrix of the policy. Deduce that $r - \bar r\mathbf 1$, with $\bar r$ the plain mean of $r$, is a [natural gradient](/natural-policy-gradient/) direction, so that natural gradient ascent moves $\theta$ by the same vector in every step.
