1. The four requests at time 0 empty the bucket and the fifth is refused. The bucket holds one token at 0.5 and one at 1, so requests 6 and 7 pass and 8 and 9 are refused; at time 3 it holds 4 tokens again and request 10 passes. Seven pass. After request 7, $x = 0$, so the retry time is $1 + 1/2 = 1.5$.

3. Here $f = 15/60 = 1/4$ and the estimate is $8 \cdot 3/4 + 4 = 10$; since $10 + 1 > 10$ the request is refused. A request passes when $8(1 - f) + 5 \le 10$, that is $f \ge 3/8$, at time $142.5$.

4. The token bucket has $r = 1/5$ and $b = 1 + 12/5 = 3.4$. A quiet source sends $\lfloor 12/5 \rfloor + 1 = 3$ cells at once, and $1 + \lfloor 12/(5 - 2) \rfloor = 5$ cells at spacing 2.

6. $1 + \lfloor 49/0.8 \rfloor = 1 + 61 = 62$ requests. The fluid bound is $50 \cdot 1000/800 = 62.5$.

8. The rate test allows 25 flows, but the delay test needs $\sum_i b_i \le CD = 2$ Mbit, which allows 13 flows ($1.95$ Mbit). So 13 are admitted, the delay test stops the 14th, and the declared rates use $520/1000 = 52$ percent of the link.

10. If every request so far has passed, the bucket holds $10 + 5k/8 - k$ tokens before request $k$ (counting from 0), since it never fills up again. This is at least 1 while $k \le 24$. So request $k = 25$, the 26th, at time $3.125$ s is the first refused. In the long run 5 of every 8 pass.

12. The counter passes at most $2n - 1$ requests in a window of length $w$, which is at most $n$ only for $n = 1$. For $n = 2$: two requests at 45 pass, and at 90 the estimate is $2 \cdot (1 - 1/2) + 0 = 1$, so one request passes; the window $(30, 90]$ holds three.

18. Fix an interval and let $x_0 \le b$ be the count before its first pass. Refills in the interval add at most $r\tau$, and the last pass found $x \ge 0$, so the count after it is at least $-L_{\max}$. The units passed are the difference. For the bound at $\tau = 0$, send requests of size $L_{\max}$ to a full bucket: $b/L_{\max} + 1$ of them pass.

19. The output of a greedy shaper for a burst $B$ at time 0 is $\min(B, \sigma(t))$. So the last byte leaves when both pieces of $\sigma$ reach $B$: at $\max((B - M)/p, (B - b)/r) = \max(9.85, 80)$ ms, that is 80 ms.

21. Compare two inputs: $n$ requests at time 0, and $n$ requests at time $0.9w$. If the limiter refuses any of them, it refuses a request the rule allows. Otherwise at time $1.5w$ both inputs give the same state, with $n$ in the previous window and 0 in the current one, but the rule allows a request in the first case and forbids it in the second.

22. While every cell conforms, $tat$ before cell $j$ equals $\max_{m < j}(t_m + (j - m)T)$; prove this by induction from line L2. Cell $j$ conforms if and only if $t_j \ge tat - \tau$. For the converse, look at the first cell that does not conform.

23. A refused request takes nothing from either bucket, so each bucket alone sees exactly the passed requests, and each is sound and tight for its own curve. For the faulty version take unit requests at times $0, 0, 0, 1$: the correct dual bucket passes the ones at time 0 and 1, but the faulty one has spent A on the two refused requests and refuses at time 1.

24. Per hop: $1 + 10/5 = 3$ ms, then $1 + 11/5 = 3.2$ ms, in total $6.2$ ms. Together: $2 + 10/5 = 4$ ms. The per-hop sum charges the burst at both servers, so it exceeds the end-to-end bound by $(b + rT)/R$.

25. The sliding log's output fits $(n/w, n)$. For the converse, $n$ requests at one instant need $b \ge n$, and $n$ requests at each multiple of $w$ all pass and need $r \ge n/w$. For the fixed window, $n$ requests just before an edge and $n$ at the edge pass within a time $\varepsilon$, so $b + r\varepsilon \ge 2n$ for every $\varepsilon > 0$.
