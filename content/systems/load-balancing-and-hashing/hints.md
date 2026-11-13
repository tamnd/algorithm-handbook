1. Round robin gives server 0 the jobs 4, 3, 2 and server 1 the jobs 3, 2, so the largest load is 9. The least-work rule gives loads 8 and 6, so 8. The optimum is 7, with $\{4, 3\}$ and $\{3, 2, 2\}$; no split does better, since the total is 14.

3. The counters after the picks are $(-2, 2)$, $(1, -1)$, $(-1, 1)$, $(2, -2)$, $(0, 0)$, and the order is a b a b a. Read in a loop, the longest run is the pair a a across the end of the cycle, so 2, against 3 for a a a b b.

6. The owners are A, B, C, A, A, with arcs of 30, 40 and 30. When D joins, key 60 moves from C to D. When B leaves, key 20 moves from B to D. The final arcs are A 30, D 55 and C 15.

7. CAP is 1, 1, 2, 2, 3, 3 for the six balls. They go to A, B, A, B, A, B, so A holds 5, 15, 25 and B holds 10, 20, 40, and C holds none. The plain ring puts five balls on A and one on B.

12. Solve $k! \ge n^2 = 10^{12}$. Since $14! \approx 8.7 \cdot 10^{10}$ and $15! \approx 1.3 \cdot 10^{12}$, the answer is 15, far above both 5.26 and the simulated 8.9. The union bound is loose by a constant factor here.

13. Track the multiset of loads. With two choices the second request lands on the loaded server only if both samples hit it, with probability $1/9$. The tie rule does not change the multiset of loads, so it does not change the law of the maximum.

15. Write the number of loop runs as a sum of indicators, one per bucket $b < n$, of the event that the key sits in bucket $b$ in the view of $b + 1$ buckets, and use linearity of expectation.

16. For the score $w_s u_s$, the server of weight 2 wins when $u_C > \max(u_A, u_B)/2$; condition on the maximum, whose mean is $2/3$. For the score $-w_s/\ln u_s$, note that $-\ln u_s / w_s$ is exponential with rate $w_s$.

19. A probe at distance more than $t$ from the next node clockwise falls outside two arcs of length $t$, one before each node, so this has probability $1 - 2t$ for $t \le x$. A wins when the closest of the $k$ probes lies in its arc.

20. Each backend fills the next free slot of its own permutation, $(\mathit{offset} + j \cdot \mathit{skip}) \bmod 7$, in turns B1, B2, B3. The first table is [B1, B2, B1, B1, B3, B2, B3]. Without B3, compare slot by slot and look at slot 2.

21. Let $c_0$ be the counter of backend 0 after a pick, so $c_0 + c_1 = 0$. Show that backend 0 is picked at step $t$ exactly when $2 c_0 \ge q - p$ before the step, and write $c_0$ in terms of $t$ and the count $k_0$.

22. At a fixed point the right side vanishes for every $i$. Sum the equations from $i$ to infinity: the service terms telescope to $s_i$, and the arrival terms to $\lambda s_{i-1}^d$. For the time, use Little's law with the mean queue length $\sum_{i \ge 1} s_i$.

23. Write the $n$ arcs as $E_i / S$, where the $E_i$ are independent exponentials of mean 1 and $S$ is their sum, and use that $S$ is independent of the ratios. The largest of $n$ such exponentials has mean $H_n$, and the smallest has mean $1/n$.

24. With $X_s = -\ln u_s / w_s$ exponential of rate $w_s$, the server with the largest score is the one with the smallest $X_s$, and an exponential race is won by $s$ with probability $w_s / W$. For the move, fix the $u_s$ of a key and see which winners can change when one $w_s$ grows.

25. Give the slots of the leaving backend one at a time to a remaining backend with the fewest slots. For the fleet, ask whether the table after a change depends only on the new list of backends or also on the order of earlier changes.
