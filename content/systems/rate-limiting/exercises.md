1. ◦ A [token bucket](/token-bucket/) with $r = 2$ tokens per second and $b = 4$ starts full. Unit requests arrive at times $0, 0, 0, 0, 0, 0.5, 1, 1, 1, 3$. Which requests pass? For the first request refused at time 1, what retry time does $t + (1 - x)/r$ give?

2. ◦ A [fixed window counter](/fixed-window-counter/) allows $n = 3$ requests in each aligned window $[10k, 10k + 10)$. Requests arrive at times $8, 8, 9, 9, 10, 10, 10, 11, 19, 20$. Which pass, and how many passed requests lie in the interval $[8, 10]$?

3. ◦ A [sliding window counter](/sliding-window-counter/) has $n = 10$ and $w = 60$. At time 135 the window $[60, 120)$ holds 8 passed requests and the window $[120, 180)$ holds 4. Is a request at time 135 passed? If no other request arrives, what is the earliest time at which a request passes?

4. ◦ For [GCRA](/gcra/)$(T, \tau)$ with $T = 5$ and $\tau = 12$, give the equivalent token bucket. How many cells can a quiet source send at the same instant, and how many back to back at spacing 2?

5. ◦ Run the [single rate three color marker](/single-rate-three-color-marker/) in color-blind mode with $CIR = 1000$ bytes per second, $CBS = 1500$ and $EBS = 1000$, both buckets full at time 0. Packets of 1000 bytes arrive at times $0, 0, 0, 1, 2.5, 2.5$. Give the color of each packet and the token counts $T_c$ and $T_e$ at the end.

6. ◦ A token bucket has $r = 200$ requests per second and $b = 50$. A quiet client sends unit requests back to back at a peak rate of $R = 1000$ per second. How many pass before the first refusal, by the formula of [burst tolerance](/burst-tolerance/)? What does the fluid bound $bR/(R - r)$ give?

7. ◦ A link uses credit-based [backpressure](/backpressure/) with $B = 50$ credits, items of 1000 bytes and a credit round trip of 200 microseconds. What is the largest rate it can carry, in Gbit/s? How many credits does it need to run at 10 Gbit/s?

8. ◦ A FIFO link of 1 Gbit/s has a delay target of 2 ms and uses parameter-based [admission control](/admission-control/). Every flow declares a token bucket of rate 40 Mbit/s and depth 150 kbit. How many flows are admitted, which of the two tests stops the next one, and what fraction of the link do the declared rates use?

9. ◦ A flow with arrival curve $r\tau + b$, $r = 1$ Mbit/s and $b = 60$ kbit, crosses a server with rate $R = 10$ Mbit/s and latency $T = 2$ ms. Give the bounds on its delay and on the backlog it builds.

10. • A token bucket with $r = 5$ per second and $b = 10$ starts full. A client sends a unit request every $1/8$ second from time 0. Which request is the first to be refused, and at what time? What fraction of the requests pass in the long run?

11. • A [sliding window log](/sliding-window-log/) enforces $n = 100$ requests per 60 seconds with a clock in milliseconds, so $W = 60{,}000$ ticks. Compute the lower bound $\log_2 \binom{W}{n}$ on the bits per key. Show that storing each time modulo $W$ in 16 bits is enough to run the log, and compare the cost with 64-bit timestamps.

12. • Show that the sliding window counter is sound for the sliding rule (at most $n$ passes in every window $(t - w, t]$) if and only if $n = 1$. For $n = 2$ and $w = 60$, give arrival times at which three requests pass within one window of length 60.

13. • Run GCRA$(10, 25)$ in the virtual scheduling form on cells at times $0, 0, 0, 0, 5, 30, 31, 32$, with $tat$ starting at 0. Which cells conform? Check the answer with the equivalent token bucket.

14. • A flow has peak rate $p = 10^7$ bytes per second, maximum packet size $M = 1500$ bytes, rate $r = 10^6$ bytes per second and depth $b = 10^5$ bytes, so its curve is $\min(M + p\tau, r\tau + b)$. A quiet source sends 1500-byte packets back to back at the peak rate. How many packets conform? Compare their bytes with the fluid burst $M + p(b - M)/(p - r)$.

15. • A [leaky bucket queue](/leaky-bucket-queue/) has $r = 2$ packets per second and $K = 2$. Unit packets arrive at times $0, 0, 0, 0.2, 1, 1, 1, 3$. Which are accepted, when does each leave, and what is the largest delay? When would a [leaky bucket meter](/leaky-bucket-meter/) with $b = 2$ release the same packets?

16. • Run the [two rate three color marker](/two-rate-three-color-marker/) in color-blind mode with $PIR = 3000$, $PBS = 2000$, $CIR = 1000$ and $CBS = 1500$ (bytes and bytes per second), both buckets full at time 0, on packets (time, bytes) $(0, 1500)$, $(0, 1000)$, $(0.5, 1000)$, $(1, 1500)$. Give the colors, and check that the packets that are not red are exactly those that a token bucket $(PIR, PBS)$ passes.

17. • A trunk group is offered $a = 20$ erlangs. Write a short program for the Erlang B formula of admission control and find the smallest number of circuits $c$ with blocking below 1 percent.

18. • A variant of the token bucket lets a request of size $L$ pass whenever $x \ge 0$ and then sets $x \leftarrow x - L$, so $x$ can go negative; refills are as usual, up to $b$. Requests have size at most $L_{\max}$. Prove that at most $r\tau + b + L_{\max}$ units pass in any interval of length $\tau$, and show that it is reached for $\tau = 0$ when $L_{\max}$ divides $b$.

19. • A greedy [traffic shaper](/traffic-shaping/) has the curve $\sigma(\tau) = \min(M + p\tau, r\tau + b)$ with $M = 1500$ bytes, $p = 10^7$ bytes per second, $r = 10^6$ bytes per second and $b = 20{,}000$ bytes. A burst of 100,000 bytes arrives at time 0 into an empty shaper. In the fluid model, when does its last byte leave?

20. • A global token bucket with $R = 1000$ requests per second and $B = 2000$ is split evenly over 4 servers, as in [distributed rate limiting](/distributed-rate-limiting/). For one minute every request of the key arrives at one server, at 900 per second. Give an upper bound on how many pass under the split, and how many a single global bucket would pass.

21. ★ Consider any limiter for the rule "$n$ requests in every window $(t - w, t]$" whose decision at time $t$ depends only on $\lfloor t/w \rfloor$, the fraction $f$ of the current aligned window that has gone, and the numbers of passed requests in the current and the previous aligned window. Prove that for every $n \ge 1$ it is either unsound or refuses some request that the rule allows.

22. ★ Prove that a sequence of unit cells $t_1 \le t_2 \le \cdots$ conforms to GCRA$(T, \tau)$ in full, with $tat$ starting at $t_1$, if and only if $t_j \ge t_m + (j - m)T - \tau$ for all $m < j$.

23. ★ A dual bucket passes a request of size $L$ only if bucket A holds at least $L$ tokens and bucket B holds at least $L$, and then takes $L$ from each. Prove that its output meets both curves $r_A\tau + b_A$ and $r_B\tau + b_B$ and that it refuses only requests that would break one of them. A faulty version takes $L$ from A whenever A has enough, and only then tests B. For A $= (0.5, 3)$ and B $= (1, 1)$, both full at time 0, find unit requests that the correct version passes and the faulty version refuses.

24. ★ A flow with curve $r\tau + b$, $r = 1$ kbit/ms and $b = 10$ kbit, crosses two servers in series, each with rate $R = 5$ kbit/ms and latency $T = 1$ ms. Bound the end-to-end delay by adding the per-hop bounds, using the output curve $r\tau + b + rT$ of the first server. Then bound it with the service curve of the two servers together, which has rate $\min(R_1, R_2)$ and latency $T_1 + T_2$. Which bound is smaller, and why does the difference grow with $b$?

25. ★ Prove that a token bucket $(r, b)$ contains every output of the sliding window log with limit $(n, w)$ if and only if $r \ge n/w$ and $b \ge n$. Prove that for the fixed window counter with the same $n$ and $w$, every such token bucket has $b \ge 2n$.
