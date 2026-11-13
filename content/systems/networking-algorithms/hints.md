1. One packet takes $10\,\mu$s to send, so stop-and-wait uses $0.01/20.01 = 1/2001 \approx 0.05\%$ of the link, and a window of 2001 packets fills it. Go-Back-N allows $2^8 - 1 = 255$ packets, which gives $255/2001 \approx 12.7\%$. Selective repeat allows $2^7 = 128$, which gives $6.4\%$.

2. After 100 ms: SRTT 100, RTTVAR 50, RTO 300 ms. After the second 100 ms: RTTVAR 37.5, SRTT 100, RTO 250 ms. After 180 ms: RTTVAR $= 0.75 \cdot 37.5 + 0.25 \cdot 80 = 48.125$ (with the old SRTT), SRTT 110, RTO 302.5 ms. The timeout doubles it to 605 ms.

3. Raise all rates together. Link $Y$ fills at $4/3$, which fixes $f_2$, $f_3$ and $f_4$ at $4/3$. Then $f_1$ takes the rest of $X$, $6 - 4/3 = 14/3$. The rates are $(14/3, 4/3, 4/3, 4/3)$.

7. The matches are $P_3$, $P_5$, $P_4$, $P_1$ and $P_6$. The walk for 11011010 visits the root and the nodes for 1, 11, 110, 1101 and 11011: six nodes. There are five distinct lengths, so binary search needs $\lceil \log_2 6 \rceil = 3$ probes.

8. $[3, 12]$ is 0011, 01\*\*, 10\*\* and 1100: four prefixes. $[1, 14]$ is 0001, 001\*, 01\*\*, 10\*\*, 110\* and 1110: six prefixes, which is $2W - 2$ for $W = 4$ and the worst case. Two such fields need the cross product, $6 \times 6 = 36$ entries.

11. The difference $x_1 - x_2$ stays $-5$ under increases and halves at each decrease, so after $k$ decreases it is $5/2^k$; the bound needs $2^k > 500$. MIMD keeps the ratio and AIAD keeps the difference, so neither moves towards fairness.

14. In the fluid model each flow keeps $\alpha$ packets in the queue, so $x_i q = \alpha_i$ for the queueing delay $q$, and the rates must add up to the capacity. That fixes $q$ first, then the rates, and the window is the rate times $d_i + q$.

15. $(D_j - e)/\text{INTERVAL}$ is the partial sum $\sum_{k=1}^{j} 1/\sqrt{k}$, which must stay at most 10. Compute the sums near $j = 30$. The bound $2\sqrt{j} \le 10$ guarantees $j \le 25$ works, and $2(\sqrt{j+1} - 1) \le 10$ rules out $j > 35$.

21. Each output grants one of the two inputs at random. The matching is perfect exactly when the grants go to different inputs. Otherwise one match is made and one request out of four stays open, so the second iteration finishes.

22. Use the identity on the diagonal weight 0.2, then two transpositions that cover the 0.4 entries. Each permutation matrix has three positive entries and $M$ has seven, so two permutations cannot cover them.

23. A sample is taken only from a segment sent once. Segment 1 times out at 300 ms, and its ACK at 800 ms gives no sample. Segment 2 starts with the kept RTO of 600 ms, times out again and gives no sample. Segment 3 starts with 1200 ms, which exceeds the round trip, so it gives the first sample, 800 ms, after two timeouts in all.

24. Synchronized losses give both flows the same cycle length $T$ in seconds. Flow $i$ grows by $W_i/2$ in $T/R_i$ round trips, so $W_i = 2T/R_i$ and its rate $W_i/R_i$ is proportional to $1/R_i^2$. That makes the rate ratio 4, against 2 for the Mathis formula.

25. With price $p$ on each link, the long flow sends $1/(2p)$ and each short flow $1/p$, so the load is $3/(2p)$ and the map is $p \mapsto p + \gamma(3/(2p) - 1)$. The fixed point is $3/2$ and the derivative there is $1 - 2\gamma/3$, so the map converges near the fixed point for $0 < \gamma < 3$. With $\gamma = 4$ the prices alternate between 1 and 3.

27. Two flows are active at first, so the round number grows at rate $1/2$ and is 1.5 at time 3. That gives $C$ the tag 4.5. The fluid finishes are $B_1$ at 4.5, $A_1$ at 8.5, $C$ at 9.5 and $A_2$ at 13. Fair queueing sends the queued packet with the least tag whenever the link is free: $B_1$, then $A_1$ (since $C$ has not yet arrived at time 2), then $C$, then $A_2$.

28. Both links are tight. Write $x_2 = t$, $x_1 = 6 - t$ and $x_3 = x_4 = (4 - t)/2$, and maximize $\sum \log x_i$ over $t$. This gives $2t^2 - 13t + 12 = 0$, so $t = (13 - \sqrt{73})/4 \approx 1.114$, which is less than the max-min rate $4/3$ because $f_2$ uses both links.
