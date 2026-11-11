1. ◦ A quartz clock has [drift](/clock-drift/) rate $\rho = 20$ ppm. (a) By how much can it be off after one day, if it was exact at the start? (b) Two such clocks agree at noon. How far apart can they be at 6 p.m.? (c) They are resynchronized with reading error $\varepsilon = 2$ ms. How long can the period $R$ be if the [skew](/clock-skew/) must stay at most 10 ms?

2. ◦ Three processes run as follows. $P_1$ does a local event $a_1$, sends $m_1$ to $P_2$ ($a_2$) and receives $m_3$ ($a_3$). $P_2$ receives $m_1$ ($b_1$), sends $m_2$ to $P_3$ ($b_2$) and does a local event $b_3$. $P_3$ does local events $c_1$ and $c_2$, receives $m_2$ ($c_3$) and sends $m_3$ to $P_1$ ($c_4$). Give the [Lamport clock](/lamport-clocks/) value of each event, and list the ten events in the [total order](/total-order/) by (clock, process number).

3. ◦ For the run of the previous exercise, give the [vector clock](/vector-clocks/) of each event, and list the events that are [concurrent](/concurrent-events/) with $b_3$.

4. ◦ A client runs [Cristian's algorithm](/cristian-algorithm/), ignoring drift. It sends its request at local time 50.000 s, the reply carries the server time 72.300 s, and the reply arrives at local time 50.040 s. The one-way delay is at least 8 ms. What time does the client set, and what is the error bound?

5. ◦ The master of the [Berkeley algorithm](/berkeley-algorithm/) estimates the offsets of six machines, itself included, as $\Delta = (0, 12, -30, 18, -6, 400)$ ms, with $\gamma = 50$ ms. Find the set $G$, the average $a$, the adjustment sent to each machine, and the number of messages of the round. What would a plain average of all six offsets have been?

6. ◦ Run [Marzullo's algorithm](/marzullo-algorithm/) on the intervals $[3, 9]$, $[5, 12]$, $[8, 10]$, $[11, 14]$ and $[1, 4]$. Give the number of intervals in the best region and the region.

7. ◦ An [NTP](/ntp/) client sends a request at $T_1 = 100.000$ s on its clock. The server receives it at $T_2 = 100.130$ s and replies at $T_3 = 100.132$ s on its clock, and the reply arrives at $T_4 = 100.010$ s. Compute $\theta$ and $\delta$, and the interval that must hold the true offset. If the last four samples in the clock filter are, as ($\theta$, $\delta$) in ms, $(12, 30)$, $(15, 18)$, $(9, 45)$ and $(14, 22)$, which offset does the filter pass on?

8. ◦ In a [PTP](/precision-time-protocol/) exchange, $t_1 = 5000$, $t_2 = 5127$, $t_3 = 5300$ and $t_4 = 5207$ µs. A transparent switch puts 20 µs in the correctionField of the Sync and 0 in that of the Delay_Req. Compute offsetFromMaster and meanPathDelay. What would the slave compute if the switch were an ordinary one that reports nothing?

9. ◦ A [TrueTime](/truetime/) server has $\varepsilon = 3$ ms, and its clock reads $C(t) = t - 0.002$ s at real time $t$. A commit request arrives at real time 50.000 s. Which timestamp $s$ does the start rule pick, and from what real time on are the writes visible?

10. ◦ Three replicas $A$, $B$, $C$ keep [version vectors](/version-vectors/) in the order $(A, B, C)$, all starting at zero. In turn: $A$ updates; $A$ and $B$ sync; $B$ updates; $C$ updates; $A$ updates; $B$ and $C$ sync; $A$ and $B$ sync; $A$ and $C$ sync. Which syncs report a conflict, and what are the three vectors at the end?

11. • Under the [clock synchronization lower bound](/clock-synchronization-lower-bound/) model with $d = 10$ and $u = 4$, two processes have offsets $c = (0, 3)$. Messages from $p_0$ to $p_1$ take 7 and messages from $p_1$ to $p_0$ take 9. (a) Compute the adjusted offsets $A_0$, $A_1$ of the averaging algorithm and the skew. (b) Find admissible delays for which averaging has skew exactly $u/2$. (c) What is the best guaranteed skew for $n = 5$ processes with $u = 6$ ms?

12. • Take the run with events $a_1, a_2, a_3$ on $P_1$, $b_1, b_2, b_3$ on $P_2$ and $c_1, \dots, c_4$ on $P_3$, in that order, and three messages: sent by $a_2$ and received by $b_1$, sent by $b_2$ and received by $c_3$, sent by $c_4$ and received by $a_3$. Count the ordered pairs and the concurrent pairs among the 45 pairs of events, and count the [consistent cuts](/consistent-cut/) among the 80 cut vectors.

13. • Run [hybrid logical clocks](/hybrid-logical-clocks/) on this trace, with the physical reading $pt$ given at each event. $P_1$: local event at $pt = 20$, send $m_1$ to $P_2$ at $pt = 21$. $P_2$: local event at $pt = 18$, receive $m_1$ at $pt = 19$, send $m_2$ to $P_3$ at $pt = 20$. $P_3$: local event at $pt = 21$, receive $m_2$ at $pt = 21$, local event at $pt = 23$. Give each $(l, c)$ and the largest value of $l - pt$.

14. • Three bank branches hold $p_0 = 200$, $p_1 = 100$ and $p_2 = 50$ on FIFO channels between every pair, and run the [Chandy-Lamport algorithm](/chandy-lamport-snapshot/). In order: $p_1$ sends 40 to $p_0$; $p_0$ starts the snapshot; $p_0$ sends 30 to $p_2$; $p_0$'s marker reaches $p_2$; the 30 reaches $p_2$; the 40 reaches $p_0$; $p_1$ sends 20 to $p_2$; $p_0$'s marker reaches $p_1$; $p_2$'s marker reaches $p_1$; $p_2$'s marker reaches $p_0$; the 20 reaches $p_2$; $p_1$'s marker reaches $p_2$; $p_1$'s marker reaches $p_0$. Give the three recorded balances, the state of each of the six channels, and the total.

15. • Process $p_3$ runs [causal broadcast](/causal-broadcast/) with vectors ordered $(p_1, p_2, p_3)$ and has $VC = (1, 0, 0)$. Four messages arrive in this order: $x_3$ from $p_1$ with $VT = (3, 1, 0)$, $y_2$ from $p_2$ with $(2, 2, 0)$, $y_1$ from $p_2$ with $(2, 1, 0)$ and $x_2$ from $p_1$ with $(2, 0, 0)$. Which messages are delivered after each arrival, in what order, and what is $VC$ at the end?

16. • Three processes keep [matrix clocks](/matrix-clocks/). $P_1$ does a local event and then sends $m_1$ to $P_2$; $P_2$ receives it and sends $m_2$ to $P_3$; $P_3$ receives it and sends $m_3$ to $P_1$; $P_1$ receives $m_3$. Give the matrix of $P_1$ after the last event, and say which events of each process $P_1$ knows to be seen by everyone.

17. • A client runs Cristian's algorithm with retries against a server whose one-way delays are independent and uniform on $[5, 15]$ ms, and it accepts a round trip of at most $2U$ with $U = 11$ ms. Find the probability that an attempt is accepted, the expected number of attempts and of messages, and the worst error bound of an accepted reading.

18. • Process $p_0$ sets $x = 1$, sends $m$ to $p_1$, then sets $x = 0$. Process $p_1$ sets $y = 1$, receives $m$, then sets $y = 0$. Both variables start at 0, and each step is one event. For $\Phi = (x = 1 \wedge y = 1)$, count the consistent cuts, list those where $\Phi$ holds, and decide possibly $\Phi$ and definitely $\Phi$ in the sense of [distributed predicate detection](/distributed-predicate-detection/).

19. • Process $p_0$ sends $m$ to $p_1$, does a local event, and receives $m'$ from $p_1$. Process $p_1$ does a local event, receives $m$, and sends $m'$ to $p_0$. The local predicate $l_0$ holds in the states $s_0^0$ and $s_0^3$, and $l_1$ in $s_1^2$ and $s_1^3$. Give the queues of the [weak conjunctive predicate detection](/weak-conjunctive-predicate-detection/) checker and the cut it returns. What does it return if $l_1$ holds only in $s_1^2$?

20. • In [Time Warp](/time-warp/), an LP whose state is a number runs events that add their timestamp to it. It has run the events at 3, 7 and 9 from state 0; the event at 7 sent a message with timestamp 11 to LP $A$ and the event at 9 one with timestamp 12 to LP $C$. A straggler with timestamp 5 arrives. Which events are rolled back, to which state, which antimessages are sent, and what is the state after the LP catches up? Which events can be committed if the GVT then becomes 8?

21. • Two processes run Mattern's algorithm for [global virtual time](/global-virtual-time/). At CUT1, $LVT_0 = 40$ and $LVT_1 = 25$, and a white message with timestamp 30 is in transit from process 1 to process 0. After CUT1, process 1 runs its event at 25, which sends a red message with timestamp 27 to process 0, and its next event is at 50. Give each report and the estimate. What would the estimate be without $t_{\min}$, and why is it wrong?

22. ★ Prove that the Lamport clock value $C(e)$ equals the number of events on a longest chain of happened-before that ends at $e$, with $e$ counted.

23. ★ Two processes each run $m$ events. The $i$-th event of $p_0$ sends a message that is received by the $i$-th event of $p_1$, for $i = 1, \dots, m$. Find, as functions of $m$, the number of consistent cuts and the number of runs, that is, of orders of all $2m$ events that extend happened-before. Check your formulas for $m = 3$.

24. ★ Carry out the shifting proof of the clock synchronization lower bound for $n = 3$, $d = 10$ and $u = 3$. Give the delays of the executions $\alpha_0$, $\alpha_1$ and $\alpha_2$, derive $\varepsilon \ge 2$, and show that the averaging algorithm has skew exactly 2 in each of the three.

25. ★ Prove that causal broadcast is safe: if the broadcast of $m$ happened before the broadcast of $m'$, then no process delivers $m'$ before $m$.

26. ★ Prove that the start rule and commit wait of TrueTime give external consistency: if $T_1$ becomes visible before the commit request of $T_2$ arrives, then $s_1 < s_2$.
