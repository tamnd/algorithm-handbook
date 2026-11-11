1. ◦ In the [ski rental problem](/ski-rental-problem/), renting costs 1 a day and buying costs $B = 5$. For the rule "rent until day $j - 1$ and buy on day $j$", find the worst [competitive ratio](/competitive-ratio/) over all season lengths, for $j = 1, \ldots, 8$. Which $j$ is best, and how does it compare with $2 - 1/B$?

2. ◦ With $B = 2$, a [randomized online algorithm](/randomized-online-algorithm/) buys on day 1 with probability $1/3$ and on day 2 with probability $2/3$. Compute its expected cost for seasons of 1 day and of at least 2 days, and its ratio against an [oblivious adversary](/oblivious-adversary/). Compare it with the best deterministic rule.

3. ◦ The lift takes $E = 10$ seconds to ride once it arrives, and the stairs take $S = 50$ seconds. The [take-the-stairs strategy](/take-the-stairs-strategy/) waits $S - E$ seconds and then walks. Find its worst ratio. What are the worst ratios if you wait 30 or 45 seconds instead?

4. ◦ In the [linear search problem](/linear-search-problem/), excursion $i = 0, 1, 2, \ldots$ walks to distance $2^i$ and back, to the right when $i$ is even and to the left when $i$ is odd. Find the distance walked and the ratio when the target is 6 to the left, and when it is 5 to the right.

5. ◦ In the [secretary problem](/secretary-problem/) with $n = 9$, the rule rejects the first $r$ candidates and then takes the first one better than all before it. It finds the best with probability $P_9(r) = \frac{r}{9} \sum_{j = r + 1}^{9} \frac{1}{j - 1}$. Compute $P_9(2)$, $P_9(3)$ and $P_9(4)$, and find the best $r$.

6. ◦ Eight candidates arrive with values $5, 3, 8, 2, 7, 10, 6, 9$. Which one does the [1/e stopping rule](/one-over-e-stopping-rule/) take, with $r = \lfloor 8/e \rfloor$? Which one does it take with $r = 3$?

7. ◦ A list holds $a, b, c$ in this order, and the requests are $a, a, a, b, b, b, c, c, c, c$. An access at position $i$ costs $i$. Find the cost of [frequency count](/frequency-count/), which moves an item forward past the items with a strictly smaller count, and the cost of [move-to-front](/move-to-front/). Why does frequency count lose here?

8. ◦ Three experts predict rain (1) or no rain (0) for six days. Their predictions are $(1, 1, 0)$, $(0, 1, 1)$, $(1, 0, 0)$, $(0, 0, 1)$, $(1, 1, 1)$, $(0, 1, 0)$, and the outcomes are $0, 1, 0, 1, 1, 1$. Run [weighted majority](/weighted-majority/) with $\beta = 1/2$, predicting 1 when the weight on 1 is at least the weight on 0. Count its mistakes, the mistakes of each expert, and compare with the bound $(\ln n + m^* \ln 2)/\ln(4/3)$.

9. ◦ In [online bipartite matching](/online-bipartite-matching/), the offline side is $\{a, b, c\}$, and four vertices arrive with neighbour sets $\{a, c\}$, $\{a, b\}$, $\{a\}$, $\{b\}$. Run [greedy online matching](/greedy-online-matching/) that takes the first free neighbour in alphabetical order. Find the size of its matching and of a maximum matching.

10. ◦ Points arrive on a line at $0, 9, 3, 6, 1$, in this order. In the [online minimum spanning tree problem](/online-minimum-spanning-tree-problem/), each point must be joined to an earlier point when it arrives. Find the cost of the greedy rule, the weight of the minimum spanning tree, and a lower bound for every online algorithm on this input.

11. ◦ The edges of a cycle $a, b, c, d, e, f$ arrive one at a time. In [online vertex cover](/online-vertex-cover-problem/), the rule "take both endpoints of each uncovered edge" is used. Find its cost for the order $ab, cd, ef, bc, de, fa$ and for the order $ab, de, bc, ef, cd, fa$, and the size of an optimal cover.

12. • Randomized ski rental with $B = 3$ buys on day $j$ with probability proportional to $(2/3)^{3 - j}$, for $j = 1, 2, 3$. Find the probabilities, check that the expected cost is the same multiple of the optimum for every season length, and compare the ratio with $1/(1 - (1 - 1/B)^B)$ and with the deterministic $5/3$.

13. • A target lies on one of three rays from the start. Excursion $i$ walks along ray $i \bmod 3$ to distance $b^i$ and back. Show that the worst ratio tends to $1 + 2b^3/(b - 1)$ as the target moves away. Evaluate it for $b = 2$ and find the best $b$.

14. • In the [TCP acknowledgment problem](/tcp-acknowledgment-problem/), packets arrive at times $0, 0.5, 2, 2.1, 2.2$. One acknowledgment costs 1, and each packet costs the time it waits. The greedy rule sends an acknowledgment when the total waiting time of the pending packets reaches 1. Find its acknowledgment times and cost, the [offline optimum](/offline-optimum/), and the ratio.

15. • In the [prophet inequality](/prophet-inequality/), $X_1$ is 1 or 3 with probability $1/2$ each, and $X_2$ is 10 with probability $1/4$ and 0 otherwise. Find $\mathbb{E}[\max(X_1, X_2)]$, the expected reward of the threshold $\mathbb{E}[M]/2$, and the reward of the best stopping rule.

16. • [Multiplicative weights](/multiplicative-weights-update/) with $\eta = 1/2$ and the update $w_i \leftarrow w_i(1 - \eta m_i)$ plays two experts. The costs are $(1, 0)$, $(1, 0)$, $(0, 1)$, $(0, 1)$. Find the probabilities in each round, the expected total cost, and the bound $\sum_t m_{t,i} + \eta \sum_t \lvert m_{t,i} \rvert + (\ln n)/\eta$ for the better expert.

17. • [Online gradient descent](/online-gradient-descent/) plays $x_t \in [-1, 1]$ against the losses $f_t(x) = g_t x$ with $g = (1, 1, -1, 1)$. It starts at $x_1 = 0$ and uses the fixed step $\eta = D/(G\sqrt{T})$. Find $D$, $G$, $\eta$, the points played, the [regret](/regret/), and the bound $GD\sqrt{T}$.

18. • A [metrical task system](/metrical-task-systems/) has two states at distance 1 and starts in state 0. The tasks are $(1, 0)$ three times, then $(0, 1)$ three times, as costs in states 0 and 1. Compute the [work function](/work-function/) after each task and the optimum. Find the cost of the rule that never moves, and of the rule that moves after it has paid 2 in task costs since its last move.

19. • In the [page migration problem](/page-migration-problem/), two nodes are at distance 1, the page has size $D = 1$ and starts at node 0, and the page may move only after a request is served. The rule COUNT moves the page when $2D$ requests have come from the other node since its last move. Find its cost on the requests $1, 1, 1, 1, 0, 0, 1, 1$, the optimum, and the ratio.

20. • Run the [Ranking algorithm](/ranking-algorithm/) on the instance of Exercise 9 for each of the 6 orders of $\{a, b, c\}$. Find the expected size and the ratio, and compare with greedy.

21. • The [threshold algorithm](/online-threshold-knapsack/) for knapsack with densities in $[L, U] = [1, e^2]$ takes a small item when its density is at least $\Psi(z)$, where $\Psi(z) = 1$ for $z < c$ and $\Psi(z) = (Ue/L)^z (L/e)$ for $z \ge c$, with $c = 1/(1 + \ln(U/L))$. Find $c$, the ratio, and $\Psi$ at $z = 0.4$, $0.5$, $2/3$ and $1$. Does it take an item of density 1.1 at $z = 0.4$, of density 2 at $z = 0.5$, of density 2.5 at $z = 2/3$?

22. • [Meyerson's algorithm](/meyerson-algorithm/) with facility cost $f = 6$ sees points at $0, 2, 5$ on a line, in this order. Find its expected cost and the cost of an optimal offline solution.

23. • For [weighted majority](/weighted-majority/), the bound is $m \le (\ln n + m^* \ln(1/\beta))/\ln(2/(1 + \beta))$. Write it as $a\,m^* + b \ln n$ for $\beta = 1/2$ and $\beta = 1/4$. With $n = 8$ experts and one that never errs, compare the bound for $\beta = 1/2$ with the bound of the halving algorithm.

24. • In online $b$-matching with $b = 2$, the offline vertices $a$ and $b$ can each take two arrivals. The arrivals have neighbour sets $\{a, b\}$, $\{a, b\}$, $\{a\}$, $\{a\}$. Run [Balance](/balance-algorithm/), with ties to $a$, and First Fit, which fills $a$ before $b$. Compare both with the optimum and with $1 - (1 + 1/b)^{-b}$.

25. ★ Use [Yao's principle](/yao-minimax-principle/) to show that the ratio of Exercise 12 is optimal. Take the season length $n = 1$ with probability $1/3$, $n = 2$ with probability $2/9$, and $n = 5$ with probability $4/9$. Find $\mathbb{E}[\mathrm{OPT}]$ and the least expected cost of a deterministic rule.

26. ★ In the doubling search of Exercise 4, flip a fair coin to choose the first direction, and keep the rest of the rule. Find the worst expected ratio. Is it attained?

27. ★ In a two-state metrical task system with distance 1, a rule moves to the other state after it has paid $\alpha$ in task costs since its last move. The cruel adversary gives each task cost $\varepsilon$ in the state of the rule and 0 in the other state. Find the ratio as $\varepsilon \to 0$ as a function of $\alpha$, and the best $\alpha$.

28. ★ Two experts always predict 0 and 1. Show that an adversary forces every deterministic learner to make $T$ mistakes in $T$ rounds while the better expert makes at most $T/2$. What does this say about the factor of $m^*$ in the bound of Exercise 23? Compute that factor for $\beta = 0.9$ and $\beta = 0.99$, and the factor of $\ln n$.

29. ★ An [adaptive offline adversary](/adaptive-offline-adversary/) for ski rental with $B = 4$ sees the day on which a randomized algorithm buys. Show that no randomized algorithm has a ratio below $7/4$ against it, and compare with the oblivious ratio $256/175$.

30. ★ A [learning-augmented](/learning-augmented-algorithms/) ski rental rule with $B = 10$ and trust $\lambda = 1/2$ gets a prediction $y$ of the season length. It buys on day $\lceil \lambda B \rceil$ if $y \ge B$ and on day $\lceil B/\lambda \rceil$ otherwise. Find the worst ratio in each case, over all true lengths, and the ratio when the prediction is right. Compare with the consistency $1 + \lambda$ and the robustness $(1 + \lambda)/\lambda$.
