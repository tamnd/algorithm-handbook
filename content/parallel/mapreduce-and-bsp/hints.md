1. Without a combiner the shuffle carries 11 pairs and 34 bytes, and $q = 4$ for "to". With one, it carries $4 + 4 = 8$ pairs and 25 bytes, and no key has more than 2 values. The output is (be, 3), (do, 1), (is, 1), (not, 1), (or, 1), (to, 4).

3. Range: task 0 gets 3, 5, 8, 9, task 1 gets 14, 15, 26, and task 2 gets 32, 35, 97, so the loads are 4, 3, 3 and the output read in task order is sorted. Modulo 3: task 0 gets 3, 9, 15, task 1 gets 97, and task 2 gets 5, 8, 14, 26, 32, 35, so the loads are 3, 1, 6.

6. The processors send 4, 4, 4 and 3 words and receive 5, 4, 4 and 2; the 5 words that P0 keeps are free. So $h = 5$, set by P0 as a receiver, and $V = 15$, so $h \ge V/p = 3.75$ holds. The superstep costs $100 + 3 \cdot 5 + 20 = 135$.

10. Every count is a multiple of 5, so every load is one too. A largest load of at most 69 would leave each task at most 65, and a total of at most 195, below $N = 200$.

11. Without salting the heavy key's task gets $200{,}000 + 16{,}000$ pairs, so the speedup is about 4.63 and never above $N/c = 5$. Each salt adds $200{,}000/S$ to a task that already has 16,000.

12. The sorted sample has $S[4] = 23$ and $S[8] = 56$, and a key equal to a split point goes to the higher task. For the sample size, $\ln(n/\delta) = \ln(2 \cdot 10^9) \approx 21.42$, so $a \ge 2 \cdot 1.2 \cdot 21.42/0.04 \approx 1284.98$.

13. The samples are the keys of rank 2, 4 and 6 of each sorted block: $4, 9, 17$, then $3, 11, 18$, then $7, 12, 16$. The splitters are the third and the sixth of the nine sorted samples. Count only the keys that leave or reach a processor for $h$.

14. In round $r$ process $i$ sends to $i + 2^r \bmod 6$, so the distances are 1, 2 and 4. Use $t_i(r) = \max(t_i(r - 1), t_{i - 2^r}(r - 1)) + 1$ with $t_i(-1)$ the arrival time.

17. A vertex changes for the last time in the superstep equal to the fewest edges on a shortest path to it: vertex 1 in superstep 1, vertex 2 in 2, vertex 3 in 3 and vertex 4 in 4. Vertex 4 has no out-edge, so $H = 3$.

19. $A$ and $D$ are dominated, so their shares are 1. $R$ lacks $C$ and is copied $x_C$ times, $T$ lacks $B$ and is copied $x_B$ times, and the minimum makes $r x_C = t x_B$ with $x_B x_C = 64$.

21. The time is $2k\lceil \log_k 4096 \rceil$. Try every $k$ up to 16: the ceiling changes only at a few values, and $k = 4$ gives $4^6 = 4096$ exactly.

22. The optimum pairs the counts $2R - i$ and $R + i$ for $i = 1, \ldots, R - 1$ and puts the three keys of count $R$ together, so every task gets $3R$. The rule places the $2R$ largest keys so that task $j$ gets the $j$-th and the $(2R + 1 - j)$-th largest, which sum to $3R - 1$, and the last key makes one task $4R - 1$.

23. At the optimum the three terms $r x_C$, $s x_A$ and $t x_B$ are equal, each $(rstk)^{1/3}$. For integers, $x_A$ must divide 1000; $x_A = 2$ leaves $x_B x_C = 500$.

24. The splitting algorithm cuts the string into $k$ segments with $k$ dividing $b$, and then $q = 2^{b/k}$ and $r = k$, with $k\,2^{b - b/k}$ reducers. A limit $q \le 2^8$ forces $b/k \le 8$.

25. For (a), a split of three equal values and a split of three spread values can have the same median. For (b), put $a$ values below the smallest value of $X$ and $b$ values above the largest, and choose $a$ and $b$ so that $x$ has the middle rank of $X \cup Y$.
