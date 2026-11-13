## What to remember

- A limit is a family of intervals with caps. A limiter is sound if its output meets every cap, and greedy if it refuses only what would break a cap. For unit requests the greedy limiter passes as many requests as any limiter, even an offline one. With requests of many sizes no deterministic online limiter is optimal.
- The fixed window counter is exact for aligned windows but passes $2n$ requests across an edge. The sliding window log is exact for every window $(t - w, t]$, and any exact sliding window needs at least $\log_2 \binom{W}{n}$ bits per key for $W$ clock ticks in a window.
- The sliding window counter estimates the count as $prev \cdot (1 - f) + cur$. It passes at most $2n - 1$ in a window of length $w$, a bound that is reached, and it can refuse in an empty window. Its small error on real traffic is measured, not proved.
- A token bucket of rate $r$ and depth $b$ that starts full passes at most $r\tau + b$ units in any interval of length $\tau$, for any arrivals, and refuses only what would break that bound. The leaky bucket meter keeps $X = b - x$ and decides the same way. GCRA$(T, \tau)$ is the token bucket with $r = 1/T$ and $b = 1 + \tau/T$.
- At a peak rate $R > r$ a token bucket passes $1 + \lfloor (b-1)/(1 - r/R) \rfloor$ unit requests back to back.
- A policer drops or marks and adds no delay; a shaper delays. A leaky bucket queue of $K$ unit packets accepts what a meter with $b = K$ passes and delays each by at most $K/r$.
- With token-bucket flows on a FIFO link of rate $C$ and $\sum_i r_i \le C$, the delay is at most $\sum_i b_i / C$. Measurement-based admission, client-side throttling and adaptive limits rest on measurements, not worst-case bounds.
- Credit-based backpressure keeps $c + f + q + g = B$, so no buffer overflows, and runs at most at rate $B/T$ for a credit round trip $T$.

| Method | State per key | Time per request | Limit enforced | Largest burst |
|---|---|---|---|---|
| Fixed window counter | window index, count | $O(1)$ | $n$ per aligned window | $2n$ across an edge |
| Sliding window log | up to $n$ times | $O(1)$ amortized | $n$ per sliding window | $n$ |
| Sliding window counter | window index, two counts | $O(1)$ | approximate | $2n - 1$ within $w$ |
| Token bucket | tokens, last time | $O(1)$ | $r\tau + b$ | $b$ |
| Leaky bucket meter | level, last time | $O(1)$ | $r\tau + b$ | $b$ |
| GCRA | one time | $O(1)$ | token bucket with $r = 1/T$, $b = 1 + \tau/T$ | $\lfloor \tau/T \rfloor + 1$ cells |
| Leaky bucket queue | up to $K$ packets | $O(1)$ amortized | output $r\tau + L_{\max}$ | one packet out |

: The limiters of the chapter. For the window counters the limit is $n$ requests per window of length $w$; for GCRA, $T$ is the cell spacing and $\tau$ the tolerance. A ring of the last $n$ pass times gives the sliding log $O(1)$ worst-case time.

## Choosing a method

- **One API limit per key.** Use a token bucket, or GCRA when one number per key matters, as in a shared store. Both are sound, greedy and constant time, and the parameters mean a steady rate and a burst.
- **A limit stated as $n$ per window.** Use the sliding log when $n$ is small, the sliding counter when memory per key matters and an overshoot to $2n - 1$ is acceptable, and the fixed window only for aligned quotas such as a daily one.
- **Packets on a link.** Police when loss is cheaper than delay; shape when the next hop needs smooth traffic. Mark with a three color marker so that a later node can choose what to drop.
- **Overload of a server.** Per-client limits do not bound the total. Add admission control for the total, backpressure where the producer can wait and throttling where work can be slowed.
