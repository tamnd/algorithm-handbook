## What to remember

- With $m = n$ requests on $n$ servers chosen independently and uniformly, the busiest server has $(1 + o(1)) \ln n / \ln\ln n$ requests with probability $1 - o(1)$; for $m \ge n \ln n$ the excess over $m/n$ is $\Theta(\sqrt{m \ln n / n})$ with high probability ([maximum load](/balls-into-bins-max-load/)). With the less loaded of $d \ge 2$ uniform samples, the maximum is $\ln\ln n / \ln d + O(1)$ with probability $1 - o(1/n)$, and $m/n + \ln\ln n/\ln d + O(1)$ for any $m$ ([two choices](/power-of-two-choices/)). Stale loads make requests herd.
- [Round robin](/round-robin-load-balancing/) and [smooth weighted round robin](/weighted-round-robin/) balance the count of requests exactly in every arrival order: $\lfloor m/n \rfloor$ or $\lceil m/n \rceil$ per window, and $w_j$ of every $W$ picks. They are blind to the cost of a request.
- [Least connections](/least-connections/) is join the shortest queue. For identical servers with exponential service it is optimal among the policies that know the queue lengths (Winston 1977, Weber 1978), but not for every service distribution (Whitt 1986). In the supermarket model at load $\lambda$, a fraction $\lambda^{2^i - 1}$ of the queues hold at least $i$ jobs with two choices, against $\lambda^i$ with one.
- When a server joins, any rule that ends with equal shares moves at least $m/(n+1)$ of $m$ keys, while $h(k) \bmod n$ moves about $n/(n+1)$ of them. A [monotone](/monotonicity-property/) rule moves keys only to the new server, and [consistent hashing](/consistent-hashing/) moves $1/(n+1)$ of them in expectation.
- With one ring point per server, the expected largest share is $H_n/n$, about $\ln n / n$. With $v \ge (4/\delta^2)\ln(2n^{c+1})$ random points per server, every share lies in $[\frac{1-\delta}{(1+\delta)n}, \frac{1+\delta}{(1-\delta)n}]$ with probability at least $1 - n^{-c}$ ([max load bound](/consistent-hashing-max-load-bound/)). So $\Theta(\log n)$ points give a constant factor, and a window of $1 \pm \delta$ needs $\Theta(\log n/\delta^2)$.
- [Rendezvous hashing](/rendezvous-hashing/) and [jump consistent hash](/jump-consistent-hash/) give each key a uniform server in their random models, with no ring. [Maglev hashing](/maglev-hashing/) gives exact slot balance and $O(1)$ lookups but is not monotone, and its movement is only measured. [Bounded loads](/bounded-load-consistent-hashing/) cap every server at $\lceil (1+\varepsilon) m/n \rceil$ in every outcome, at the price of monotonicity.
- Hashing the client gives affinity, not balance: [source IP hash](/source-ip-hash/) and [sticky sessions](/sticky-sessions/) spread addresses, and one busy NAT address can load its server far above the mean ([load skew](/load-skew/)).
- A backend that fails fast looks idle and fast. Least connections, [least response time](/least-response-time/) and [peak EWMA](/peak-ewma/) all send it more traffic unless [health checking](/health-checking/) or error counts take it out.

| Method | Lookup | Balance | Monotone | Source |
|---|---|---|---|---|
| $h(k) \bmod n$ | $O(1)$ | that of the hash | no | [dynamic partitioning](/dynamic-partitioning-problem/) |
| Ring, $v$ points per server | $O(\log(nv))$ | every share at most $3/n$ w.p. $1 - n^{-c}$ if $v \ge 16\ln(2n^{c+1})$ | yes | max load bound |
| Rendezvous | $\Theta(n)$ | each key uniform | yes | rendezvous hashing |
| Jump | $H_n$ steps expected, $O(n)$ worst | each key uniform | on $\{0, \ldots, n-1\}$ only | jump consistent hash |
| Maglev | $O(1)$ | $\lfloor M/N \rfloor$ or $\lceil M/N \rceil$ slots, exact | no | Maglev hashing |
| Multi-probe, $k$ probes | $O(k \log n)$ | largest share $\frac{k}{k-1}\cdot\frac{1}{n} + o(1/n)$ w.h.p. | yes | multi-probe |
| Bounded loads | $O(n)$ worst walk | every load at most $\lceil (1+\varepsilon)m/n \rceil$ | no | bounded loads |

: Consistent hashes. "Uniform" holds in a random-oracle or ideal-hash model; ring and multi-probe bounds are over random server points; the multi-probe bound needs $2 \le k \ll \sqrt{n}/\ln n$.

## Choosing a method

For requests without keys behind one balancer, use least connections when request costs vary and round robin when they do not; weight either when backends differ in capacity. With many independent balancers or clients, no one sees all the load: use two random choices on local counts, or peak EWMA when backends stall now and then.

For keys, decide first whether servers leave in any order. If only the last one can go, jump consistent hash needs no memory. Otherwise use a ring with enough virtual nodes, or rendezvous hashing when the server list is short. Use Maglev when lookups must take constant time and a few extra moves are acceptable, and bounded loads when a hard cap on each server matters more than monotonicity.
