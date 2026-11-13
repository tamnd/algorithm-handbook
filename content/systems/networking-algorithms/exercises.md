1. ◦ A link of 1 Gbit/s has a round trip of 20 ms, and packets have 10,000 bits. Find the utilization of [stop-and-wait](/stop-and-wait/) and the smallest window that fills the link. With 8-bit sequence numbers, find the largest window and the utilization of [Go-Back-N](/go-back-n/) and of [selective repeat](/selective-repeat/).

2. ◦ Run [Jacobson's estimator](/jacobson-rto-estimation/) with $\alpha = 1/8$, $\beta = 1/4$, $K = 4$ on the samples 100, 100 and 180 ms, ignoring the clock granularity and the 1 s minimum. Give SRTT, RTTVAR and the RTO after each sample, and the RTO after a timeout that follows the third sample.

3. ◦ Link $X$ has capacity 6 and carries flows $f_1$ and $f_2$. Link $Y$ has capacity 4 and carries $f_2$, $f_3$ and $f_4$. Find the [max-min fair](/max-min-fairness/) rates and the link that fills first.

4. ◦ In [slotted ALOHA](/slotted-aloha/) with $n = 5$ backlogged stations, each sending with probability $p$ in a slot, find the throughput for $p = 1/5$ and for $p = 0.4$. Compare them with the Poisson model at offered load $G = 0.5$.

5. ◦ Two Ethernet stations collide for the first time and then follow [binary exponential backoff](/binary-exponential-backoff/). Find the probability that they collide again at once, the probability that they collide three more times in a row, and the mean wait in slots of one station after its third collision.

6. ◦ [CSMA/CD](/csma-cd/) needs the transmission time of the shortest frame to be at least the round trip $2\tau$. Signals travel at $2 \times 10^8$ m/s; ignore repeaters and the jam. Find the time of a 512-bit frame at 10 Mbit/s and at 1 Gbit/s, the longest cable at 1 Gbit/s, and the longest cable if the slot is 4096 bits.

7. ◦ A forwarding table holds $P_1 = 0*$, $P_2 = 01*$, $P_3 = 0110*$, $P_4 = 1*$, $P_5 = 110*$ and $P_6 = 11011*$. Give the [longest prefix match](/longest-prefix-match/) for 01101100, 11010001, 10000000, 00111111 and 11011010. How many nodes does a binary [trie](/trie/) walk visit for 11011010, counting the root, and how many hash probes does binary search on lengths need for this table?

8. ◦ A rule matches the 4-bit field range $[3, 12]$. Write it as prefixes. Do the same for $[1, 14]$. How many TCAM entries does a rule need that has the range $[1, 14]$ on each of two fields?

9. ◦ [Deficit round robin](/deficit-round-robin/) serves two backlogged flows with quanta $Q_A = 1000$ and $Q_B = 500$ bytes. All packets have 300 bytes. Give the packets each flow sends in each of the first three rounds and the deficit counters at the end of each round.

10. ◦ A message of 1.2 Mbit crosses three [store-and-forward](/store-and-forward/) links of 100 Mbit/s with no propagation delay and no headers. Find its delay sent as one packet and sent as 100 packets of 12,000 bits.

11. • Two [AIMD](/aimd/) flows share a link of capacity $c = 10$ and start at $(1, 6)$. At each step, if $x_1 + x_2 > 10$ both rates are multiplied by $b = 1/2$, and otherwise both grow by $a = 1$. Give the first four states. After how many decreases is $|x_1 - x_2| < 0.01$? What happens to the two rates under MIMD and under AIAD from the same start?

12. • By the formula of Mathis et al., find the rate of one Reno flow with segments of 1460 bytes, a round trip of 100 ms and loss rate $p = 10^{-4}$. What loss rate lets the same flow send at 10 Gbit/s, and how many segments lie between two losses at that rate?

13. • A [CUBIC](/tcp-cubic/) flow with $\beta = 0.7$ and $C = 0.4$, time in seconds, loses a packet at $W_{max} = 2000$ segments. Find the window just after the loss, the time $K$ to return to $W_{max}$ and the window 1 s after the loss. Ignore the TCP-friendly region. Compare $K$ with the time Reno needs to grow back from 1000 to 2000 segments at round trips of 50 ms and of 200 ms.

14. • Two [Vegas](/tcp-vegas/) flows share a link of 1000 packets/s. Their propagation round trips are 20 ms and 80 ms. In the fluid model, find the rates, the queue, the queueing delay and the windows when both flows use $\alpha = \beta = 2$. Repeat for $\alpha_1 = \beta_1 = 1$ and $\alpha_2 = \beta_2 = 3$. With the round trips of the first case, what rate ratio does the formula of Mathis et al. give two Reno flows with the same loss rate?

15. • [CoDel](/codel/) enters the dropping state at time $e$ with $c_0 = 1$ and INTERVAL = 100 ms, and the delay stays above the target. Find the largest $j$ with $D_j \le e + 1$ s. Compare it with the estimate $(\tau / 2\,\text{INTERVAL})^2$ and with the two bounds on $D_j$ given in the entry.

16. • Under the Gao-Rexford rules, AS1 is the provider of AS2 and AS3, AS2 and AS3 are peers, AS4 is a customer of AS2 and AS5 is a customer of AS3. AS4 and AS5 each originate one prefix. Give the [BGP](/bgp/) AS path that AS2, AS4 and AS1 use to reach the prefix of AS5, and the path that AS3 uses to reach the prefix of AS4.

17. • A [Chord](/chord/) ring has $m = 5$ and nodes 2, 7, 13, 19, 25 and 30, with finger $i$ of node $v$ equal to $\mathrm{succ}(v + 2^i)$ for $i = 0, \ldots, 4$. Give the fingers of nodes 2, 19 and 25. Trace the lookup of key 28 from node 2.

18. • In [Kademlia](/kademlia/) with 4-bit identifiers, node 6 knows nodes 1, 5, 7, 8, 11 and 14. Give the XOR distance from 6 to each, the bucket each falls in, and the bucket that overflows when $k = 2$. Which two of the seven nodes are closest to key 10?

19. • A [tree bitmap](/tree-bitmap/) with stride 3 stores $*$, $1*$, $01*$, $0110*$, $101*$ and $11101*$. Write the internal and external bitmaps of the root, in the order $*, 0, 1, 00, 01, 10, 11$ and children 000 to 111. Say where $101*$ is stored, and give the result of lookups that start 1011 and 0110.

20. • A flow is shaped by a [token bucket](/token-bucket/) with $\sigma = 12{,}000$ bits and $\rho = 100$ kbit/s, and it has a guaranteed rate $g = 200$ kbit/s on a link of $r = 10$ Mbit/s with $L_{max} = 12{,}000$ bits. Find its delay bound under [GPS](/generalized-processor-sharing/) and under [WFQ](/weighted-fair-queueing/). What rate $g$, and what share of the weights, gives a WFQ bound of 20 ms?

21. • A $2 \times 2$ switch has all four requests. Find the probability that the first iteration of [PIM](/parallel-iterative-matching/) yields a perfect matching, the expected number of iterations, and the expected fraction of the requests resolved in the first iteration.

22. • Write $M = \begin{pmatrix} 0.6 & 0.4 & 0 \\ 0.4 & 0.2 & 0.4 \\ 0 & 0.4 & 0.6 \end{pmatrix}$ as a convex combination of permutation matrices ([Birkhoff-von Neumann](/birkhoff-von-neumann-decomposition/)). Show that no decomposition uses fewer than three permutations, give the Marcus-Ree bound, and give a 5-slot frame schedule.

23. ★ A sender has one segment in flight at a time. Its RTO starts at 300 ms and every round trip is 800 ms. With [Karn's algorithm](/karn-algorithm/), trace the first three segments: the timeouts, the samples taken and the RTO used for each segment. What happens without the rule that keeps the doubled RTO, and what sample does the first segment give if the sender times the last copy?

24. ★ Two [Reno](/tcp-reno/) flows with round trips of 50 and 100 ms share a bottleneck, and every loss hits both flows at the same instant. Each window grows by one segment per round trip and halves at a loss. Find the ratio of their rates, and compare it with the ratio that the formula of Mathis et al. gives under independent losses.

25. ★ In the line network of the [network utility maximization](/network-utility-maximization/) entry, two links of capacity 1 carry a long flow over both and one short flow each, all with log utility, and the two prices stay equal. Write the price update $p \leftarrow p + \gamma(y - 1)$ as a map of $p$ alone. For which step sizes $\gamma$ does it converge near the fixed point, and what happens with $\gamma = 4$ from $p = 1$?

26. ★ Every node of an [overlay](/overlay-lookup/) with $n = 2^{20}$ nodes keeps $d$ neighbours. Give a lower bound on the hop count of the worst lookup as a function of $d$ and $n$, and evaluate it for $d = 2$, $d = 20$ and $d = 32$.

27. ★ A link of rate 1 runs [fair queueing](/fair-queueing/). At time 0, flow $A$ has packets $A_1$ and $A_2$ of size 4 and flow $B$ has $B_1$ of size 2. At time 3, flow $C$ sends one packet of size 3. Find the finish tags, the finish times in the fluid system and the order and times in which fair queueing sends the packets.

28. ★ For the network of exercise 3, find the [proportionally fair](/proportional-fairness/) rates. Compare the rate of $f_2$ with its max-min rate.
