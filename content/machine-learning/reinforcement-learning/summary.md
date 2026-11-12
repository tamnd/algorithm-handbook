## What to remember

- A finite [Markov decision process](/markov-decision-process/) with discount $\gamma < 1$ has one optimal value function $V^*$, the unique solution of the [Bellman optimality equation](/bellman-optimality-equation/), and every policy greedy for $V^*$ is optimal.
- The Bellman operators are $\gamma$-contractions in the max norm, so [value iteration](/value-iteration/) gets $\lVert V_k - V^* \rVert_\infty \le \gamma^k \lVert V_0 - V^* \rVert_\infty$ on every finite MDP. A policy greedy for a $V$ within $\varepsilon$ of $V^*$ loses at most $2\gamma\varepsilon/(1-\gamma)$.
- [Policy iteration](/policy-iteration/) never makes a policy worse and is strongly polynomial for a fixed $\gamma$; value iteration is not. [Linear programming](/linear-programming-for-mdps/) plans in polynomial time.
- In the stochastic [bandit](/multi-armed-bandit/) every consistent policy pulls a worse arm $i$ at least $(1-o(1))\ln n/\mathrm{kl}(\mu_i, \mu^*)$ times in expectation. [UCB1](/ucb1/) has regret $O(\sum_i \ln n/\Delta_i)$ for every $n$, [Thompson sampling](/thompson-sampling/) reaches the Lai-Robbins constant on Bernoulli arms, and constant-$\varepsilon$ [ε-greedy](/epsilon-greedy/) has linear regret.
- Against a reward table fixed in advance, [EXP3](/exp3/) has expected regret $O(\sqrt{nK\log K})$, and no algorithm does better than order $\sqrt{nK}$.
- A [TD error](/td-error/) $\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)$ has mean equal to the Bellman residual. Tabular [TD(0)](/temporal-difference-learning/), [Q-learning](/q-learning/) and SARSA with a GLIE policy converge with probability 1 in the limit, under the conditions in the caption below.
- Linear features, bootstrapping and off-policy updates together, the [deadly triad](/deadly-triad/), can make TD diverge. On-policy linear TD converges to a point within a factor $1/\sqrt{1-\gamma^2}$ of the best fit in the weighted norm, and [gradient TD](/gradient-temporal-difference/) converges off-policy.
- The [policy gradient theorem](/policy-gradient-theorem/) gives $\nabla J$ as an expectation of $Q^\pi \nabla \log \pi$, so [REINFORCE](/reinforce/) is an unbiased stochastic gradient method, and any state baseline keeps it unbiased. It can stop at a stationary point that is not optimal.
- Deep methods such as [DQN](/dqn/) and [PPO](/ppo/) have no convergence guarantee; their entries state update rules and properties of the objectives.

| Method | Setting | What is guaranteed | Kind of guarantee |
|---|---|---|---|
| Value iteration | finite MDP, known model, $\gamma < 1$ | error $\le \gamma^k \lVert V_0 - V^* \rVert_\infty$ after $k$ sweeps of cost $O(S^2A)$ | every MDP |
| Policy iteration | finite MDP, known model, $\gamma < 1$ | optimal after at most $A^S$ iterations of cost $O(S^3 + S^2A)$ | every MDP |
| Linear programming | finite MDP, known model, $\gamma < 1$ | optimal values and policy in polynomial time | every MDP |
| ε-greedy, $\varepsilon_t = \min(1, cK/(d^2t))$ | stochastic bandit, rewards in $[0,1]$, $d$ at most the smallest gap | regret $O(K\log(n)/d^2)$ for $c > 5$ | in expectation |
| UCB1 | stochastic bandit, rewards in $[0,1]$ | regret $\le \sum_i 8\ln n/\Delta_i + (1+\pi^2/3)\sum_j \Delta_j$ | in expectation, every $n$ |
| Thompson sampling | Bernoulli bandit, uniform priors | $\mathbb{E}[T_i(n)] \le (1+\varepsilon)\ln n/\mathrm{kl}(\mu_i,\mu^*) + o(\ln n)$ | in expectation, as $n \to \infty$ |
| EXP3 | adversarial bandit, rewards in $[0,1]$ | regret $\le 2.63\sqrt{gK\ln K}$ for $g \ge G_{\max}$ | in expectation, every table |
| TD(0), tabular | fixed policy, sampled transitions | $V \to V^\pi$ | with probability 1, in the limit |
| Q-learning, tabular | finite MDP, $\gamma < 1$, any exploring behavior | $Q \to q_*$ | with probability 1, in the limit |
| SARSA, tabular | finite MDP, $\gamma < 1$, GLIE policy | $Q \to q_*$ | with probability 1, in the limit |
| Linear TD, on-policy | linear features, ergodic chain | error at most $1/\sqrt{1-\gamma^2}$ times the best fit | with probability 1, in the limit |
| REINFORCE | differentiable policy | unbiased gradient; stationary point of $J$ | in the limit, under smoothness |
| DQN, PPO | neural network values or policies | none | none |

: Guarantees of the main methods. The limit results also need Robbins-Monro step sizes and updates of every state or pair infinitely often.

## Choosing a method

With a known model that fits in memory, plan. Policy iteration needs few iterations; value iteration has cheaper sweeps; [modified policy iteration](/modified-policy-iteration/) sits between them. Use the linear program for a polynomial bound or extra linear constraints.

For stochastic bandits, use UCB1 for a bound at every horizon and Thompson sampling when a prior is natural. Use EXP3 when rewards may be chosen against you, and [contextual bandits](/contextual-bandit/) when rounds come with features.

Without a model and with few states, use tabular Q-learning or SARSA; SARSA is safer while it learns, Q-learning learns $q_*$ off-policy. Use [Dyna-Q](/dyna-q/) when real steps are costly. With many states, use [value function approximation](/value-function-approximation/): linear on-policy TD or [LSTD](/least-squares-td/) when you want the convergence results, DQN for discrete actions and raw inputs, PPO or [soft actor-critic](/soft-actor-critic/) for continuous actions. Without guarantees, test on several seeds.

With logged data only, check a new policy by [off-policy evaluation](/off-policy-evaluation/) and learn it with an [offline method](/offline-reinforcement-learning/) that stays near the data.
