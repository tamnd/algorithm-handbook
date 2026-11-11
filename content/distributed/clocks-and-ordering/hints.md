2. $a_1 = 1$, $a_2 = 2$, $b_1 = 3$, $b_2 = 4$, $b_3 = 5$, $c_1 = 1$, $c_2 = 2$, $c_3 = 5$, $c_4 = 6$, $a_3 = 7$. The total order is $a_1, c_1, a_2, c_2, b_1, b_2, b_3, c_3, c_4, a_3$.

3. $a_1 = (1,0,0)$, $a_2 = (2,0,0)$, $a_3 = (3,2,4)$, $b_1 = (2,1,0)$, $b_2 = (2,2,0)$, $b_3 = (2,3,0)$, $c_1 = (0,0,1)$, $c_2 = (0,0,2)$, $c_3 = (2,2,3)$, $c_4 = (2,2,4)$. The events concurrent with $b_3$ are $c_1$, $c_2$, $c_3$, $c_4$ and $a_3$.

5. $G$ is every machine but the last, with spread 48 ms, and $a = -6/5 = -1.2$ ms. The adjustments $a - \Delta_i$ are $-1.2$, $-13.2$, $28.8$, $-19.2$, $4.8$ and $-401.2$ ms. The round sends $3(n - 1) = 15$ messages. A plain average would be about 65.7 ms, pulled up by the faulty clock.

7. $\theta = (0.130 + 0.122)/2 = 0.126$ s and $\delta = 0.010 - 0.002 = 0.008$ s, so the true offset lies in $[0.122, 0.130]$ s. The filter takes the sample with the least delay, $(15, 18)$, and passes on 15 ms.

9. $s = C(50.000) + \varepsilon = 50.001$. TT.after($s$) needs $C(t) - \varepsilon > s$, that is $t > 50.006$, so the writes become visible just after real time 50.006 s, a wait of $2\varepsilon$.

12. Stamp the events with vector clocks and compare each pair. There are 32 ordered pairs and 13 concurrent ones. A cut $(k_1, k_2, k_3)$ is consistent when $k_1 \ge 2$ if $k_2 \ge 1$, $k_2 \ge 2$ if $k_3 \ge 3$, and $k_3 \ge 4$ if $k_1 \ge 3$; 24 of the 80 vectors pass.

14. A channel's state is what arrives after the receiver records and before the marker on it. $p_0$ records 200, $p_2$ records 50 and $p_1$ records 40. Channel $(1, 0)$ holds 40 and channel $(1, 2)$ holds 20; the other four are empty. The total is 350.

15. Nothing is delivered until $x_2$ arrives, since each earlier message waits for $x_2$, directly or through $y_1$. Then $x_2$ and $y_1$ are delivered, followed by $x_3$ and $y_2$ in either order, and $VC = (3, 2, 0)$.

17. The round trip is the sum of two uniform delays, so $P(\mathrm{RTT} > 22) = 8^2 / 200 = 0.32$ and an attempt is accepted with probability 0.68. That gives $1/0.68 \approx 1.47$ attempts and about 2.94 messages, and an accepted reading has error at most $U - d_{\min} = 6$ ms.

21. Process 0 waits for the white message, so its report is 30, or 27 if the red message has arrived. Process 1 reports $\min(50, 27) = 27$, and the estimate is 27. Without $t_{\min}$ process 1 reports 50 and the estimate can be 30, above the red message of timestamp 27 that is still in transit.

22. Induct over the events in any order that extends happened-before. The rules give $C(e) = 1 + \max$ of $C$ over the direct predecessors of $e$ (the previous event of its process and, for a receive, the send), with 0 when there are none. A longest chain ending at $e$ consists of a longest chain ending at one direct predecessor, plus $e$.

23. A cut $(k_0, k_1)$ is consistent exactly when $k_1 \le k_0$, which gives $(m + 1)(m + 2)/2$ cuts. A run is a monotone path through these cuts from $(0, 0)$ to $(m, m)$ that never goes above the diagonal, so there are $\binom{2m}{m}/(m + 1)$ of them, the Catalan number. For $m = 3$: 10 cuts and 5 runs.

24. In $\alpha_0$ messages from $p_i$ to $p_j$ take 7 when $i < j$ and 10 when $i > j$. $\alpha_k$ shifts $p_0, \dots, p_{k-1}$ by 3, which turns the delays across the boundary into 10 and 7. The two inequalities $A_k \ge A_{k-1} + u - \varepsilon$ and $A_2 - A_0 \le \varepsilon$ give $3\varepsilon \ge 2u = 6$. Averaging gives offsets $(-1, 0, 1)$, $(2, 0, 1)$ and $(2, 3, 1)$.

25. Let $m$ be the $t$-th broadcast of $p_j$. Show by induction along the causal chain that $VT(m')[j] \ge t$, or $VT(m')[j] > t$ when $p_j$ also sends $m'$. A receiver delivers $m'$ only when $VC[j] \ge t$, and $VC[j]$ counts the messages of $p_j$ delivered, in order, so $m$ is among them.

26. The interval of TT.now() always holds the real time. Commit wait ends only when $\mathit{earliest} > s_1$, so $s_1$ is below the real time at which $T_1$ becomes visible. That is before $T_2$'s request arrives, and $s_2$ is a $\mathit{latest}$ read after it, which is at least the real time of the read.
