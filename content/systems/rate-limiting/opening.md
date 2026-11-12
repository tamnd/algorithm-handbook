An API that allows each user 100 requests a minute, a router that holds a customer to the bandwidth they pay for, and a server that turns away new work when it is full all apply a rate limit. The limiter must decide each request at once, with a few words of state per client, and it must say exactly how large a burst it allows. Without one, a single busy client or a retry storm can take a whole service down.

The token bucket is the standard answer. Tokens accrue at rate $r$ up to a capacity $b$, and each admitted request spends one. It admits at most $b + rt$ requests in any interval of length $t$, so $r$ fixes the long-run rate and $b$ the largest burst. The leaky bucket used as a meter makes the same decisions, and GCRA keeps the same state as a single timestamp. Window counters are simpler. A fixed window resets a counter at each boundary and can pass twice the limit in a short span around a boundary; a sliding log is exact but stores one timestamp per request; a sliding window counter estimates the sliding count from two fixed windows.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The problem.** The rate limiting problem, the rate limiter interface, burst tolerance, throttling and admission control.
2. **Buckets.** The token bucket, the leaky bucket as a meter and as a queue, and the generic cell rate algorithm (GCRA).
3. **Windows.** The fixed window counter, the sliding window log and the sliding window counter.
4. **Policing and shaping.** Dropping or marking traffic against delaying it, and the single-rate and two-rate three-color markers that routers use to sort packets into green, yellow and red.
5. **Beyond one server.** Distributed rate limiting with partial and delayed counts, and backpressure from slow consumers to fast producers.

## What to read meanwhile

The window algorithms are streaming algorithms. Chapter 19.5 has the [sliding window model](/sliding-window-model/), [time-based windows](/time-based-window/) and [tumbling windows](/tumbling-window/), which are the fixed windows of this chapter, and the [exponential moving average](/exponential-moving-average/) for smoothed rates. A sliding log is a [queue](/queue/), often a [circular buffer](/circular-buffer/), and a limiter for many clients keeps its state in a [hash table](/hash-table/); with too many clients to count exactly, a [count-min sketch](/count-min-sketch/) estimates each one's rate.

[Online admission control](/online-admission-control/) in Chapter 19.2 treats accept-or-reject decisions online. A global limit over many servers needs a shared counter: the [G-counter](/g-counter/) and [PN-counter](/pn-counter/) of Chapter 21.4 and the [gossip protocol](/gossip-protocol/) show how replicas combine counts. The congestion control of TCP, planned for Chapter 26.6, is rate limiting that the sender applies to itself.
