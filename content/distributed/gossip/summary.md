## What to remember

- In the [random phone call model](/random-phone-call-model/) every process calls one uniform partner per round. The informed set can at most triple in expectation per round, so every algorithm needs at least $\log_3 n - O(1)$ rounds.
- [Push](/push-gossip/) informs all $n$ nodes in $\log_2 n + \ln n + O(1)$ rounds with about $n \ln n$ messages. The $\log_2 n$ comes from doubling at the start, the $\ln n$ from the end, where the uninformed count falls only by a factor of about $e$ per round.
- [Pull](/pull-gossip/) squares the uninformed fraction once half the nodes know: $\mathbb{E}[\varepsilon_{t+1}] \le \varepsilon_t^2$. [Push-pull](/push-pull-gossip/) combines both and needs $\log_3 n + O(\log \log n)$ rounds and $O(n \log \log n)$ transmissions, and the [lower bound](/rumor-spreading-message-lower-bound/) of $\Omega(n \log \log n)$ for address-oblivious algorithms shows that this is optimal.
- On a general graph, push-pull needs $O(\log n / \Phi)$ rounds, where $\Phi$ is the [conductance](/graph-conductance/), and the bound is [tight](/conductance-rumor-spreading-bound/). On a star, push from the centre needs $(n - 1)H_{n-1} \approx n \ln n$ rounds in expectation, and push-pull at most 2 from any start.
- A [fanout](/gossip-fanout/) of $\ln n + c$ reaches every node with probability tending to $e^{-e^{-c}}$, and a constant fanout $k$ reaches the fraction $\pi$ with $\pi = 1 - e^{-k\pi}$. The [SIR model](/epidemic-model/) gives the same law for the residue, $s_\infty = e^{-R_0(1 - s_\infty)}$.
- [Rumour mongering](/rumor-mongering/) trades messages for residue: with $m$ messages per site, the fraction that misses the update is about $s = e^{-m}$, so a backup by [anti-entropy](/anti-entropy/) is still needed.
- Real systems get random peers from a [peer sampling service](/peer-sampling-service/) built on small views. [SWIM](/swim/) finds a crash in $e/(e-1) \approx 1.58$ periods on average with a load per member that does not grow with $n$.
- [Pairwise gossip averaging](/gossip-averaging/) takes $\Theta(\log(1/\varepsilon) / \log(1/\lambda_2(\bar W)))$ ticks, and [push-pull aggregation](/gossip-aggregation/) cuts the variance by about $1/(2\sqrt e) \approx 0.303$ per cycle.

## The protocols side by side

| Protocol | Task | Time | Messages | Note |
|---|---|---|---|---|
| [Push](/push-gossip/) | rumour | $\log_2 n + \ln n + O(1)$ rounds | $\Theta(n \log n)$, about $n \ln n$ | slow end |
| [Pull](/pull-gossip/) | rumour | about $\log_2 n + \log_2 \ln n$ rounds | $O(n \log \log n)$ if stopped at the end, $O(n \log n)$ with an age bound | slow start |
| [Push-pull](/push-pull-gossip/) | rumour | $\log_3 n + O(\log \log n)$ rounds | $O(n \log \log n)$ | median counter for $O(\log n)$ rounds |
| [Rumour mongering](/rumor-mongering/) | update | $\Theta(\log n)$ rounds | $\Theta(n \log(1/s))$ | misses a fraction $s \approx e^{-m}$ |
| [Plumtree](/epidemic-broadcast-tree/) | broadcast | $O(D)$ rounds | $n - 1$ payloads after the first message | ids on the other links |
| [SWIM](/swim/) | failure detection | $e/(e-1)$ periods to first detection, $O(\log n)$ to spread | $O(1)$ per member per period | full membership list |
| [Cyclon](/cyclon/) | peer sampling | one shuffle per cycle | 2 per node per cycle | even in-degree, slow healing |
| [Push-sum](/push-sum/) | average | $O(\log n + \log \frac1\varepsilon + \log \frac1\delta)$ rounds | $n$ per round | one-way messages |
| [Push-pull averaging](/gossip-aggregation/) | average | variance $\times\, 0.303$ per cycle | $2n$ per cycle | restart in epochs under churn |

: Costs on $n$ nodes with uniform partners. $D$ is the overlay diameter, $m$ the messages per site, $\varepsilon$ the relative error, $\delta$ the failure probability.

## Choosing a method

To spread one update fast, use push-pull, with the median counter rule of Karp et al. if messages matter. A simple age bound of a little over $\log_3 n$ rounds costs $\Theta(n \log n)$ transmissions.

To keep replicas in step, combine [rumour mongering](/rumor-mongering/) for new updates with periodic anti-entropy for the residue, delete with [death certificates](/death-certificates/), and use [Scuttlebutt](/scuttlebutt-reconciliation/) when each exchange has a fixed size. To broadcast a stream of messages, [Plumtree](/epidemic-broadcast-tree/) over [HyParView](/hyparview/) sends each payload once per node. When a stated delivery probability is the goal, set the fanout of a [probabilistic broadcast](/probabilistic-broadcast/) to $\ln n + c$ with $c = -\ln(-\ln(1 - \varepsilon))$.

When every member must know every other, use [SWIM](/swim/) with suspicion. Otherwise keep partial views: [Cyclon](/cyclon/) for samples close to uniform, [Newscast](/newscast/) when dead links must vanish fast, [SCAMP](/scamp/) when the view should grow like $\ln n$ with no one knowing $n$. For heartbeats with a tunable error rate, use the [phi accrual detector](/phi-accrual-failure-detector/), and check that its model of the gaps fits the network.

To compute a mean, a sum or the network size, run push-pull averaging over peer sampling and restart it in epochs. Use [push-sum](/push-sum/) when exchanges cannot be atomic, and pairwise averaging on a fixed graph, where the spectral gap decides the speed.
