## What to remember

- A clock with drift rate $\rho$ satisfies $(1 - \rho)(t - s) \le H(t) - H(s) \le (1 + \rho)(t - s)$, so two such clocks drift apart by at most $2\rho(t - s)$. Clocks resynchronized every $R$ seconds with reading error $\varepsilon$ keep a precision of $\pi = \varepsilon + 2\rho R$.
- [Cristian's algorithm](/cristian-algorithm/) sets the clock to $T + \mathrm{RTT}/2$ with an error of at most $\mathrm{RTT}/2 - d_{\min}$ when drift is ignored. [NTP](/ntp/) computes the offset $\theta = ((T_2 - T_1) + (T_3 - T_4))/2$ and the delay $\delta = (T_4 - T_1) - (T_3 - T_2)$, and the true offset lies within $\delta/2$ of $\theta$.
- With $n$ drift-free clocks and delays known only within an interval of length $u$, no algorithm guarantees a skew below $(1 - 1/n)u$, and averaging with the middle delay reaches this bound. The uncertainty $u$ limits precision, not the delay itself.
- [Happened-before](/happened-before/) is the smallest transitive relation that contains program order and send-before-receive; it is a strict partial order. [Lamport clocks](/lamport-clocks/) give $a \to b \implies C(a) < C(b)$ but not the converse, and ordering by $(C, i)$ gives a [total order](/total-order/) that extends $\to$.
- [Vector clocks](/vector-clocks/) give $a \to b \iff V(a) < V(b)$. For $e$ on $p_i$, one entry decides: $e \to f$ if and only if $V(e)[i] \le V(f)[i]$ and $e \ne f$. Charron-Bost showed that vectors with fewer than $n$ entries cannot capture $\to$ in general.
- Causal order holds if and only if FIFO order and local order hold. [Causal broadcast](/causal-broadcast/) delivers a message from $p_k$ with timestamp $VT$ once $VT[k] = VC[k] + 1$ and $VT[x] \le VC[x]$ for $x \ne k$.
- The [consistent cuts](/consistent-cut/) of a run form a distributive lattice under componentwise max and min. The [Chandy-Lamport algorithm](/chandy-lamport-snapshot/) records one with $e$ markers on FIFO channels, and the recorded state is reachable from the initial state and leads to the final one.
- Deciding whether a predicate held at some consistent cut is NP-complete in general; for a conjunction of local predicates the [Garg-Waldecker checker](/weak-conjunctive-predicate-detection/) answers in $O(n^2 m)$ comparisons.
- [TrueTime](/truetime/) returns an interval of width $2\varepsilon$ that holds the real time. Taking $s = \mathit{latest}$ and waiting until $\mathit{earliest} > s$ gives [external consistency](/external-consistency/), and the wait ends at most $4\varepsilon$ after the request arrives.

## The logical clocks side by side

| Clock | Stamp size | Work per event | What the order tells |
|---|---|---|---|
| [Lamport clock](/lamport-clocks/) | 1 integer | $O(1)$ | $a \to b \implies C(a) < C(b)$ |
| [Vector clock](/vector-clocks/) | $n$ integers | $\Theta(n)$ | $a \to b \iff V(a) < V(b)$ |
| [Matrix clock](/matrix-clocks/) | $n^2$ integers | $\Theta(n^2)$ | also which events every process has seen |
| [Plausible clock](/plausible-clocks/) | $r$ integers and a site | $\Theta(r)$ | never misses or reverses a causal pair; may order a concurrent pair |
| [Hybrid logical clock](/hybrid-logical-clocks/) | 2 integers | $O(1)$ | clock condition, with $0 \le l - pt \le \varepsilon$ |
| [Version vector](/version-vectors/) | $n$ integers per copy | $\Theta(n)$ | which copies conflict |
| [Interval tree clock](/interval-tree-clocks/) | trees of $t$ nodes | $O(t)$ | exact, with replicas that fork and join |

: Logical clocks of the chapter. $n$ is the number of processes or replicas, $\varepsilon$ the clock skew, $r$ the fixed size of a plausible clock.

## Choosing a method

For physical time, take NTP when milliseconds are enough and the clients are spread over the Internet. Take [PTP](/precision-time-protocol/) on a local network with timestamping hardware and transparent or boundary switches, when you need a microsecond or better. The [Berkeley algorithm](/berkeley-algorithm/) suits a closed group with no reference clock. Use a [monotonic clock](/monotonic-clock/) for every timeout and interval, since a wall clock can be stepped back.

For order, start with a Lamport clock when you need a total order that respects causality. Move to vector clocks when you must tell concurrent events from ordered ones, and pay $n$ entries for it. For replicated data, use version vectors on a fixed set of replicas, [dotted version vectors](/dotted-version-vectors/) when a few servers act for many clients, and interval tree clocks when replicas come and go. When timestamps must also be near the time of day, a hybrid logical clock costs two integers; TrueTime gives real-time order, but only with a tight bound on clock error and a commit wait.

For snapshots, use Chandy-Lamport on FIFO channels and the [Lai-Yang algorithm](/lai-yang-snapshot/) when messages can overtake each other. In parallel simulation, the [Chandy-Misra-Bryant algorithm](/chandy-misra-bryant/) suits models with good lookahead, and [Time Warp](/time-warp/) suits models with little lookahead, at the cost of saved states and rollbacks.
