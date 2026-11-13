1. ◦ Five jobs of sizes 4, 3, 3, 2, 2 arrive in this order at two equal servers, an instance of the [load balancing problem](/load-balancing-problem/). Give the largest load under round robin (job $j$ to server $j \bmod 2$, counting from 0), under the rule "send each job to the server with the least work so far, ties to server 0", which is [list scheduling](/list-scheduling/), and in the offline optimum.

2. ◦ Four backends have weights $2, 0, 5, 3$, so the prefix sums are $(2, 2, 7, 10)$. A [weighted random](/weighted-random-load-balancing/) pick draws an integer $r$ uniform in $\{0, \ldots, 9\}$ and returns the least $i$ with $prefix[i] > r$. Which values of $r$ go to which backend? What shares do the four backends get if the test is written $prefix[i] \ge r$ by mistake?

3. ◦ Run the smooth form of [weighted round robin](/weighted-round-robin/) on backends $a$ and $b$ with weights 3 and 2, ties to $a$. Give the counters after each of the first five picks and the order of the picks. Compare the longest run of one backend, with the cycle read in a loop, with the classic order a a a b b.

4. ◦ Two backends have [least response time](/least-response-time/) estimates $L = (20, 30)$ ms and weight 1, and five requests arrive before any response ends. Give the backend of each request when the score is $L_j(a_j + 1)$ and ties go to the lower index. Compare the split with the speed shares $1/L_j$, and with the rule that ranks by $L_j$ alone.

5. ◦ A [peak EWMA](/peak-ewma/) cost with $\tau = 10$ s jumps to 400 ms at time 0 and gets no samples after that. When does it fall below 50 ms? At time 10 s, backend A has this cost and no request pending, and backend B has cost 30 ms and 3 requests pending. Which one is picked if the pair drawn is A and B?

6. ◦ A [hash ring](/hash-ring/) has positions 0 to 99. Servers A, B and C sit at 15, 55 and 85, and each key goes to the first server at or after its position, wrapping past 99 to 0. Place the keys 10, 20, 60, 90 and 99, and give the arc length of each server. Then server D joins at 70, and after that B leaves. Which keys move at each step, and what are the final arc lengths?

7. ◦ Run [consistent hashing with bounded loads](/bounded-load-consistent-hashing/) with $\varepsilon = 1/2$ on the ring of Exercise 6 with only A at 30, B at 60 and C at 90. Balls hash to 5, 10, 15, 20, 25 and 40 and are inserted in this order, with CAP $= \lceil 1.5\, m/3 \rceil$, where $m$ counts the balls placed so far, the new one included. A ball goes to the first server clockwise that holds fewer than CAP balls. Where does each ball go? Compare with the plain ring.

8. ◦ In the supermarket model of [two choices](/power-of-two-choices/) at load $\lambda = 0.8$, give the fraction of queues with at least 1, 2, 3 and 4 jobs, for one choice and for two. Compute the expected time in the system, $T_2 = \sum_{i \ge 1} \lambda^{2^i - 2}$, to three decimals, and compare it with $T_1 = 1/(1 - \lambda)$.

9. ◦ By the [max load bound](/consistent-hashing-max-load-bound/), how many random points per server does a ring of $n = 50$ servers need so that, with probability at least $1 - 1/n$, every share lies within a factor 3 of $1/n$ on either side? Use $\delta = 1/2$ and $c = 1$.

10. • A pool has two backends of weights 3 and 7 and receives $m = 10{,}000$ requests. Under weighted random choice, give the mean and the standard deviation of the count of the first backend, and use the normal approximation to estimate the probability that it gets more than 3,100. What is its count under smooth weighted round robin, and by how much can it differ from $t \cdot 3/10$ after any $t$ picks?

11. • Three backends report connection counts $(5, 2, 4)$ once per second, and the balancer sees no other counts in between. Thirty requests arrive within one second. Where does [least connections](/least-connections/) on the reported counts send them? Where does the rule "draw two different backends at random and take the one with the smaller reported count" send them in expectation? Give the expected counts at the end of the second, if no connection closes.

12. • The union bound gives $\Pr[\text{some server has at least } k \text{ requests}] \le n/k!$ for $m = n$ ([maximum load](/balls-into-bins-max-load/)). For $n = 10^6$, find the least $k$ that makes this at most $1/n$. Compare it with $\ln n/\ln\ln n$ and with the mean maximum of about 8.9 that simulation gives.

13. • Three requests go to three servers. Compute the exact law of the largest load, and its mean, for one uniform choice per request and for two uniform choices with replacement, taking the less loaded. Does the tie rule matter?

14. • A server's share on a ring with $n$ servers and $v$ random points each has relative standard deviation $\sqrt{(n - 1)/(nv + 1)}$ ([virtual nodes](/virtual-nodes/)). For $n = 50$, find the least $v$ that makes it at most 10 percent. How does the answer scale with the target?

15. • In [jump consistent hash](/jump-consistent-hash/), the bucket of a key in the view of $b + 1$ buckets is $b$ with probability $1/(b + 1)$, and the loop visits exactly the buckets that the key holds in some view of at most $n$ buckets. Show that the expected number of loop runs is $H_n$, and compute it for $n = 1000$.

16. • Three servers have weights 1, 1 and 2. In weighted [rendezvous hashing](/rendezvous-hashing/), each server gets an independent uniform $u_s \in (0, 1)$ for each key. Compute the share of each server when the score is $w_s u_s$, and when it is $-w_s/\ln u_s$.

17. • [CARP](/carp/) gives each of two proxies a multiplier $x_1 \le x_2$ with $x_1 x_2 = 1$, and a URL goes to the proxy with the larger $x_s u_s$, where the $u_s$ are independent and uniform in $(0, 1)$. Show that proxy 1 gets the share $x_1/(2x_2)$. Which multipliers give proxy 1 the share $1/4$? What share does it get with the plain multipliers 1 and 3?

18. • A store keeps each key on the top 2 servers by rendezvous score. With $n$ servers and scores from a random oracle, what fraction of keys changes its pair of servers when one server fails, and how many new copies does each such key need? Answer the same for a join.

19. • A ring of length 1 holds two nodes for [multi-probe consistent hashing](/multi-probe-consistent-hashing/), node A owning an arc of length $x \le 1/2$ and node B the rest. A key takes the node at the smallest clockwise distance over $k$ independent probes. Show that A's share is $\frac{1}{2}(1 - (1 - 2x)^k)$. For $x = 1/4$, give the largest share over the mean for $k = 1, 2, 3$, and the least $k$ that brings it to 1.05 or below.

20. • Build the [Maglev](/maglev-hashing/) table of size $M = 7$ for backends B1, B2 and B3 with (offset, skip) equal to $(0, 3)$, $(1, 2)$ and $(4, 1)$. Then remove B3 and build the table again. How many slots change, how many would a monotone rule change, and which slot moves between two backends that both stay?

21. ★ Two backends have weights $p$ and $q$, $W = p + q$, and run smooth weighted round robin with ties to backend 0. Prove that after $t$ picks backend 0 has exactly $\lfloor tp/W + 1/2 \rfloor$ of them, the integer nearest its fair share. Conclude that its count never differs from $tp/W$ by more than $1/2$.

22. ★ In the supermarket model, $n \to \infty$ queues each serve at rate 1, jobs arrive at rate $\lambda n$ with $\lambda < 1$, and each job joins the shortest of $d$ queues chosen at random. The fraction $s_i$ of queues with at least $i$ jobs obeys $ds_i/dt = \lambda (s_{i-1}^d - s_i^d) - (s_i - s_{i+1})$ with $s_0 = 1$. Find the fixed point, and derive the expected time in the system $T_d = \sum_{i \ge 1} \lambda^{(d^i - d)/(d - 1)}$.

23. ★ A ring of length 1 has $n$ servers with one independent uniform point each. Prove that the expected largest arc is $H_n/n$ and the expected smallest arc is $1/n^2$. Give both for $n = 100$, as multiples of the mean share.

24. ★ Prove that the weighted rendezvous score $w_s / (-\ln u_s)$ gives server $s$ the share $w_s / W$ exactly. Then show that raising one weight moves keys only to that server, and compute the fraction of keys that moves, and from where, when the weights $1, 1, 2$ become $1, 1, 4$.

25. ★ A lookup table has $M$ slots and $N \ge 2$ backends, and each backend holds $\lfloor M/N \rfloor$ or $\lceil M/N \rceil$ slots. Show that when one backend leaves, its slots alone can be handed out so that each of the others holds $\lfloor M/(N-1) \rfloor$ or $\lceil M/(N-1) \rceil$. Explain why a fleet of balancers that each keep such a table would still disagree after a few changes, and how Maglev avoids this at the cost of extra moves.
