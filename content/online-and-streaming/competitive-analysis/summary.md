## What to remember

- An [online algorithm](/online-algorithm/) is $c$-competitive if its cost is at most $c$ times the [offline optimum](/offline-optimum/) plus a constant, on every input. The limit is on information, not on time.
- A [randomized online algorithm](/randomized-online-algorithm/) is judged by its expected cost against an [oblivious adversary](/oblivious-adversary/), which fixes the input first. Against an [adaptive offline adversary](/adaptive-offline-adversary/) randomness gains nothing.
- Lower bounds come from adversaries for deterministic rules and from [Yao's principle](/yao-minimax-principle/) for randomized ones: one hard distribution on inputs bounds every randomized algorithm.
- Rent or buy is the pattern behind many problems. The [break-even strategy](/break-even-strategy/) pays at most twice the optimum, and a random buying time with density proportional to $e^x$ lowers the factor to $e/(e - 1)$.
- When a quantity is unknown, guess it and double the guess. Doubling costs a constant factor, 9 in the [linear search problem](/linear-search-problem/).
- [Regret](/regret/) compares with the best fixed action, not with the best sequence. Multiplicative weights keep it near $\sqrt{T \ln n}$, so the average regret goes to 0.
- Greedy is often within a constant or a logarithm of the optimum online, and often no rule does better: matching ($1/2$), Steiner trees and spanning trees (a logarithmic factor).
- Correlated randomness beats fresh coins: [Ranking](/ranking-algorithm/) draws one order and gets $1 - 1/e$; a new random choice per arrival stays at $1/2$.
- Predictions and advice measure the value of partial knowledge of the future: one bit of advice solves ski rental exactly.

| Problem | Rule | Ratio | Notes |
|---|---|---|---|
| [Ski rental](/ski-rental-problem/), price $B$ | break-even | $2 - 1/B$ | randomized $e/(e - 1)$ |
| [Bahncard](/bahncard-problem/), discount $\beta$ | SUM | $2 - \beta$ | randomized $e/(e - 1 + \beta)$ |
| [TCP acknowledgment](/tcp-acknowledgment-problem/) | ack when latency equals ack cost | 2 | randomized $e/(e - 1)$ |
| Linear search | doubling | 9 | randomized about $4.59$ |
| [Secretary](/secretary-problem/) | reject the first $n/e$ | success $\to 1/e$ | random order needed |
| [Prophet inequality](/prophet-inequality/) | threshold $\mathbb{E}[M]/2$ | $1/2$ | tight |
| [Experts](/expert-problem/) | Hedge | regret $\sqrt{(T/2) \ln n}$ | optimal up to $1 + o(1)$ |
| [Online convex optimization](/online-convex-optimization/) | [online gradient descent](/online-gradient-descent/) | regret $O(GD\sqrt{T})$ | $O(\log T)$ if strongly convex |
| [Metrical task systems](/metrical-task-systems/), $n$ states | work function algorithm | $2n - 1$ | randomized $O(\log^2 n)$ |
| [Bipartite matching](/online-bipartite-matching/) | greedy; Ranking | $1/2$; $1 - 1/e$ | both optimal in their class |
| $b$-matching | [Balance](/balance-algorithm/) | $1 - (1 + 1/b)^{-b}$ | deterministic |
| [Adwords](/online-adwords-problem/), small bids | MSVV | $1 - 1/e$ | greedy $1/2$ |
| Knapsack, densities in $[L, U]$ | [threshold](/online-threshold-knapsack/) | $1 + \ln(U/L)$ | unbounded without limits |
| [Set cover](/online-set-cover-problem/) | primal-dual and rounding | $O(\log m \log n)$ | nearly tight for deterministic rules |
| [Steiner tree](/online-steiner-tree-problem/), $k$ terminals | [greedy](/online-greedy-steiner-tree/) | $\Theta(\log k)$ | optimal |
| [Facility location](/online-facility-location-problem/) | [Meyerson](/meyerson-algorithm/) | $O(\log n)$ | $O(1)$ in random order |
| [Online TSP](/online-traveling-salesman-problem/), closed | Plan At Home | 2 | tight |

: Online problems of this chapter, with the best simple rule. For maximization problems the ratio is the fraction of the optimum that the rule keeps.

## Choosing a model and a rule

First fix the benchmark. If the input can change at every step and a good answer must change with it, compare with the offline optimum and use the competitive ratio. If one fixed action is a fair target, as in prediction and portfolio choice, use regret; its bounds are much stronger, because the benchmark is weaker.

Then fix the adversary. If the input does not depend on the algorithm's coins, as with most real workloads, a randomized rule and the oblivious adversary are the right model, and the gain can be large: $e/(e - 1)$ against 2 for ski rental, $1 - 1/e$ against $1/2$ for matching. If the input reacts to the algorithm, use a deterministic rule.

If the input is not adversarial at all, the worst-case ratio is too pessimistic. A random arrival order, known distributions as in the prophet inequality, or a prediction with a fallback as in [learning-augmented algorithms](/learning-augmented-algorithms/), give better guarantees, and the competitive ratio stays as the safety bound.
