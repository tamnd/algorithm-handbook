1. ◦ Take $n = 10^6$ nodes in the [random phone call model](/random-phone-call-model/). Compute the leading terms $\log_2 n + \ln n$ for [push](/push-gossip/), the term $\log_3 n$ for [push-pull](/push-pull-gossip/), and the $\lceil \log_2 n \rceil$ rounds of the telephone model, where the calls of a round form a matching chosen by the algorithm.

2. ◦ In the random phone call model with $n = 11$, each process calls one of its 10 others uniformly. Find the expected number of calls that a fixed process receives in a round, the probability that it receives none, and the probability that it receives exactly two. Give the limit of the second value as $n \to \infty$.

3. ◦ A [probabilistic broadcast](/probabilistic-broadcast/) on $n = 10^4$ processes must reach all of them with probability at least $0.99$. Find $c$ and the [fanout](/gossip-fanout/) $\ln n + c$. What fanout keeps the same guarantee when each message is lost with probability $0.2$?

4. ◦ In the [SIR model](/epidemic-model/) with $R_0 = 2.5$, solve $s_\infty = e^{-R_0(1 - s_\infty)}$ for the residue by fixed-point iteration, compute the peak fraction of infectives $i_{\max} = 1 - (1 + \ln R_0)/R_0$, and give the approximate probability that a single spreader dies out early.

5. ◦ A [phi accrual detector](/phi-accrual-failure-detector/) has fitted a normal model with $\mu = 100$ ms and $\sigma = 10$ ms to the heartbeat gaps. Compute $\varphi$ when 120 ms have passed since the last heartbeat, and the gap at which $\varphi$ reaches the threshold $\Phi = 3$.

6. ◦ A replicated store has $n = 1000$ sites. [Death certificates](/death-certificates/) must use the space of a plain timeout of $\tau = 20$ days, every site keeps a certificate for $\tau_1 = 10$ days, and $r = 5$ retention sites keep a dormant copy. Find $\tau_2$ from the equal-space rule $\tau_1 + (r/n)\tau_2 = \tau$, and the probability that all dormant copies are lost after one server half-life.

7. ◦ How many cycles of [push-pull averaging](/gossip-aggregation/) reduce the expected variance of the values by a factor of $10^6$, with each of the three pair selectors GETPAIR_PM, GETPAIR_RAND and GETPAIR_DISTR?

8. ◦ [Plumtree](/epidemic-broadcast-tree/) runs on a connected overlay with $n = 10$ nodes and $m = 20$ links, with no failures. Count the payloads and the PRUNE messages of the first broadcast, and the payloads and the IHAVE messages of the second.

9. ◦ Run one round of [push-sum](/push-sum/) on $n = 3$ nodes with $x = (9, 0, 3)$ and $w = (1, 1, 1)$, where node 1 and node 2 send to node 3 and node 3 sends to node 2. Give $s$, $w$ and the estimates $s/w$ after the round, and check both sums.

10. • On a star with 10 leaves, a rumour starts at the centre. Find the expected number of rounds of push until every leaf knows it. How many rounds does push-pull need from the centre, and from a leaf?

11. • On $n = 1000$ nodes, 950 are informed and 50 are not. For one round of push, of pull and of push-pull, find the expected number of nodes still uninformed after the round.

12. • In pull with message loss $\delta$, the uninformed fraction follows $\varepsilon_{t+1} \approx \varepsilon_t(\varepsilon_t + \delta)$. Starting from $\varepsilon_0 = 1/2$, count the rounds until $\varepsilon_t < 10^{-6}$ for $\delta = 0.1$ and for $\delta = 0$.

13. • A push in which each informed node sends to $k$ random nodes per round takes about $\log_{k+1} n + (\ln n)/k$ rounds. Evaluate this for $n = 10^6$ and $k = 1, 2, 3$, and say which term shrinks faster as $k$ grows.

14. • In [rumour mongering](/rumor-mongering/) with feedback and coin, the residue solves $s = e^{-(k+1)(1-s)}$. Find the smallest $k$ with $s < 10^{-3}$, the residue, and the messages per site $m = (k+1)(1-s)$. Check that $s \approx e^{-m}$.

15. • For the cycle $C_8$, find the [conductance](/graph-conductance/) $\Phi$ and the second smallest eigenvalue $\lambda_2$ of the normalized Laplacian, and check the Cheeger bounds $\lambda_2/2 \le \Phi \le \sqrt{2\lambda_2}$.

16. • Give the [epidemic threshold](/epidemic-threshold/) $\beta/\delta = 1/\lambda_1(A)$ for $K_{17}$, the star $K_{1,16}$, the cycle $C_{17}$ and the hypercube $Q_4$. For the star, check $\langle k \rangle \le \lambda_1 \le \Delta$.

17. • On the path $1 - 2 - 3$, write the Metropolis weight matrix $W$ of [distributed averaging](/distributed-averaging/), find its eigenvalues and its SLEM, and the number of rounds that guarantees an error reduction by $10^{-3}$. Iterate twice from $x(0) = (3, 0, 0)$.

18. • [Randomized gossip averaging](/gossip-averaging/) runs on $K_{11}$ with the natural $P_{ij} = 1/10$. Find $\lambda_2(\bar W)$ and the window of Theorem 3 for the $\varepsilon$-averaging time with $\varepsilon = 0.01$, in ticks and in absolute time.

19. • In [network size estimation](/network-size-estimation/) with the $k$-th minimum and $k = 10$, the tenth smallest value seen is $U_{(10)} = 0.002$. Give the estimate $\hat n$, its approximate relative standard deviation, and the $k$ that brings the relative standard deviation down to $0.05$.

20. • In [SWIM](/swim/) with 11 members, one member crashes and the 10 live ones each pick a uniform target among their 10 others. Find the probability that the crash is probed in a given period and the expected number of periods to the first failed probe. If each message arrives with probability $0.9$ and $k = 3$, what is the probability that a probe of a live member fails?

21. • Iterate the fluid push recurrence $i_{t+1} = 1 - (1 - i_t)e^{-i_t}$ from $i_0 = 1/1024$, and give $1024\, i_t$ for each round until $1024(1 - i_t) < 1$. Compare the number of rounds with $\log_2 n + \ln n$ for $n = 1024$.

22. ★ Show that in push-pull, once a fraction $\varepsilon_t$ is uninformed, $\mathbb{E}[\varepsilon_{t+1}] \approx \varepsilon_t^2 e^{-(1 - \varepsilon_t)}$ for large $n$. Iterate this and the pull rule $\varepsilon_{t+1} = \varepsilon_t^2$ from $\varepsilon_0 = 1/2$ with $n = 10^6$, and count the rounds until $n\varepsilon_t < 1$.

23. ★ In push-sum, let node $i$ hold the vector of shares $v_{t,i}$ and the weight $w_{t,i}$, and let $\Phi_t = \sum_{i,j} (v_{t,i,j} - w_{t,i}/n)^2$. For $n = 2$, start from $v_{0,i} = e_i$, $w_{0,i} = 1$, enumerate the four choices of targets, and check that $\mathbb{E}[\Phi_1] = (\frac12 - \frac1{4n})\Phi_0$.

24. ★ The random tour estimator of network size starts a simple random walk at node $i$, stops at the first return to $i$, and outputs $\hat n = d_i \sum_{t=0}^{T-1} 1/d_{X_t}$. On the star $K_{1,k}$, show that the estimate from the centre is always exactly $k + 1$, and that the estimate from a leaf has expectation $k + 1$.

25. ★ The wheel $W_k$ has a hub joined to every vertex of a cycle $C_k$. Show that $\lambda_1(A) = 1 + \sqrt{1 + k}$, and find the epidemic threshold for $k = 8$. Compare it with the star $K_{1,8}$, which has the same 9 vertices.

26. ★ Two copies of $K_4$ are joined by one edge. Find the conductance and the cut that attains it, compute $\lambda_2$ of the normalized Laplacian numerically, and check the Cheeger bounds. Then compare $\Phi$ with the formula $1/(k(k-1)+1)$ for the barbell of two $K_k$.
