## What to remember

- A window protocol with $k$-bit sequence numbers is correct over a FIFO channel exactly when $w_s + w_r \le 2^k$, so [Go-Back-N](/go-back-n/) allows $N \le 2^k - 1$ and [selective repeat](/selective-repeat/) allows $w \le 2^{k-1}$.
- [Jacobson's estimator](/jacobson-rto-estimation/) sets $\mathrm{RTO} = \mathrm{SRTT} + \max(G, 4\,\mathrm{RTTVAR})$ from two moving averages. [Karn's algorithm](/karn-algorithm/) takes no sample from a retransmitted segment and keeps the doubled RTO.
- [AIMD](/aimd/) converges to equal shares in the synchronous binary feedback model: each decrease multiplies the difference of two rates by $b < 1$. In a periodic loss model [Reno](/tcp-reno/) gets about $(\mathrm{MSS}/\mathrm{RTT})\sqrt{3/(2p)}$. [CUBIC](/tcp-cubic/) and [BBR](/bbr-congestion-control/) have no proved worst-case bound; their behaviour is measured.
- [Distance-vector routing](/distance-vector-routing/) is correct after at most $\lceil I/c \rceil + n - 1$ synchronous rounds. A bad change can make it [count to infinity](/count-to-infinity/). [BGP](/bgp/) converges when there is no dispute wheel; otherwise it may oscillate.
- [Longest prefix match](/longest-prefix-match/) by binary search on lengths needs $\lceil \log_2(L+1) \rceil$ hash probes for $L$ distinct lengths, each expected $O(1)$. A [tree bitmap](/tree-bitmap/) with stride $s$ needs at most $\lfloor W/s \rfloor + 2$ memory reads in the worst case.
- [Weighted fair queueing](/weighted-fair-queueing/) delays a $(\sigma, \rho)$ token-bucket flow with rate $g \ge \rho$ by at most $\sigma/g + L_{max}/r$. [Deficit round robin](/deficit-round-robin/) keeps $|s_i - s_j| < Q + 2M$ with equal quanta $Q$.
- In an input-queued switch, FIFO queues saturate at $2 - \sqrt{2} \approx 0.586$ under uniform traffic. [Max-weight matching](/switch-scheduling/) gives 100% throughput for every admissible i.i.d. load. [PIM](/parallel-iterative-matching/) needs at most $\lceil \log_2 N \rceil + 4/3$ iterations in expectation and $N$ in the worst case.
- [Slotted ALOHA](/slotted-aloha/) with $n$ stations has throughput at most $(1 - 1/n)^{n-1}$, which tends to $1/e$. [Valiant's routing](/valiant-routing/) routes any permutation on the $n$-cube in $14n$ steps with probability at least $1 - 1/N$.

| Method | Bound | Kind | Model |
|---|---|---|---|
| Distance vector | $\lceil I/c \rceil + n - 1$ rounds | worst case | synchronous rounds, costs $\ge c$ |
| BGP, path vector | converges, no time bound | proved convergence | no dispute wheel, or Gao-Rexford |
| [Chord](/chord/) | $O(\log n)$ hops | whp | random identifiers, correct fingers |
| Binary search on lengths | $\lceil \log_2(L+1) \rceil$ probes | expected $O(1)$ per probe | hashing |
| Tree bitmap | $\lfloor W/s \rfloor + 2$ reads | worst case | stride $s$, $W$-bit addresses |
| WFQ | $\sigma/g + L_{max}/r$ delay | worst case | token bucket, $\rho \le g$ |
| DRR | $\lvert s_i - s_j \rvert < Q + 2M$ | worst case | equal quanta $Q \ge M$ |
| Max-weight matching | 100% throughput | stability | i.i.d. admissible arrivals |
| PIM | $\lceil \log_2 N \rceil + 4/3$ iterations | expected | random grants and accepts |
| Valiant | $14n$ steps | probability $\ge 1 - 1/N$ | $n$-cube, any permutation |
| AIMD | equal shares | convergence | synchronous binary feedback |
| Reno | $(\mathrm{MSS}/\mathrm{RTT})\sqrt{3/(2p)}$ | fluid or periodic | random loss at rate $p$ |
| [Vegas](/tcp-vegas/) | weighted proportional fairness | equilibrium only | fluid model |
| CUBIC, BBR | none proved | measured | real networks |
| [CoDel](/codel/), [PIE](/pie-aqm/), [RED](/red-random-early-detection/) | no delay bound | measured | heuristics |

: The main bounds of the chapter, with the kind of guarantee and the model in which each holds.

## Choosing a method

For reliable transfer, choose the window first. It must cover the bandwidth-delay product, and the sequence space must be at least $w_s + w_r$. Selective repeat wastes less on a lossy path; Go-Back-N keeps the receiver simple.

On a host, CUBIC is the common default; BBR keeps throughput up under random loss but is unfair to loss-based flows, both as measured. In the network, use [ECN](/ecn/) with CoDel or PIE when the problem is queueing delay. [Network utility maximization](/network-utility-maximization/) tells whether a protocol reaches [max-min](/max-min-fairness/) or [proportional fairness](/proportional-fairness/).

Inside one domain, [link-state routing](/link-state-routing/) converges faster than distance-vector routing. Between domains, the safety of BGP depends on policy. For lookups, use a multibit trie such as the tree bitmap when worst-case reads matter. For [classification](/packet-classification/), use a TCAM for few rules, [tuple space search](/tuple-space-search/) when the rules have few distinct prefix-length tuples, and otherwise a decision tree such as [HiCuts](/hicuts/), measured on real rule sets.

For scheduling at a link, DRR gives near-fair shares at $O(1)$ cost, and WFQ gives a delay bound. For a switch, use [iSLIP](/islip/) in hardware, with speedup 2 when full throughput must be proved. In wireless networks, [backpressure routing](/backpressure-routing/) is throughput optimal but needs a max-weight schedule, which is NP-hard; greedy maximal scheduling is the usual compromise.
