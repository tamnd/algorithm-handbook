1. The window $j$ is $[4j, 4j + 10)$ for $j$ from $\lfloor(\tau - 10)/4\rfloor + 1$ to $\lfloor \tau/4 \rfloor$. So 17 is in $[8, 18)$, $[12, 22)$ and $[16, 26)$, and 19 is in $[12, 22)$ and $[16, 26)$. Both are in the tumbling window $[10, 20)$. Half of the items are in three windows and half in two, which averages $s/h = 5/2$. The panes have size $\gcd(10, 4) = 2$, and each window is 5 panes.

5. The deques are $(1, 2)$; $(2, 7)$; $(2, 7), (3, 3)$; $(2, 7), (4, 5)$; $(5, 5)$; $(5, 5), (6, 1)$; $(7, 6)$, and the maxima are $2, 7, 7, 7, 5, 5, 6$. At step 5 the new 5 pops the old 5, a tie, and the 7 at position 2 expires.

7. For $k = 2$: $L = 1$, $\rho = 6$, at most 14 buckets and 98 bits. For $k = 4$: $L = 2$, $\rho = 8$, at most 27 buckets and 270 bits.

9. The windows hold $n_A = 3000$ and $n_B = 1200$ tuples. The output rate is $\sigma(\lambda_A n_B + \lambda_B n_A) = 180$ results per second, and nested loops make $R/\sigma = 180{,}000$ comparisons per second. An index on $B$ pays off when it costs less than $\lambda_A T_B (1 - \sigma) = 5994$ comparisons per tuple of $B$; an index on $A$ when it costs less than $\lambda_B T_A (1 - \sigma) = 599.4$.

11. At $t = 4$ the weights are $1/4, 1/2, 1, 1$, so $C = 11/4$, $S = 10$ and the average is $40/11$. Going to $t = 8$ multiplies both by $2^{-4/2} = 1/4$: $C = 11/16$, $S = 5/2$, and the average stays $40/11$. The steady count is the geometric series $1/(1 - 2^{-1/2}) = 2 + \sqrt 2 \approx 3.414$, against $2/\ln 2 + 1/2 \approx 3.385$.

13. At $t = 6$ the buckets are $(6, 1), (5, 2), (2, 2)$, with estimate $9/2$ and true count 5. At $t = 9$ the third bucket of size 1 starts a cascade of two merges: $(9, 1), (8, 2), (5, 4)$, estimate $11/2$, true count 6. At $t = 10$: $(10, 1), (9, 1), (8, 2), (5, 4)$, estimate $13/2$, true count 6. There are 4 merges, at the steps 3, 6, 9 and 9.

14. With $L = 3$, the fifth bucket of size 1 merges the two oldest: $(5, 1), (4, 1), (3, 1), (2, 2)$. The midpoint estimate is $3 + 3/2 = 9/2$, error $1/10$. The half-bucket estimate is $3 + 1 = 4$, error $1/5$, which is more than $1/6$.

16. After the first evict, $F$ holds $(s, s), (r, rs), (q, qrs)$ from the bottom to the top and $B$ is empty. The queries are p, pq, pqr, pqrs, qrs, rs, rst, st, t and the empty string. The calls are $1, 1, 1, 1, 4, 0, 1, 0, 0, 1$, 10 in all, which is exactly $2I$ for $I = 5$: each item costs one call when it is inserted and one when a flip moves it.

19. The lists are $(1, 2)$; $(1, 4), (2, 2)$; $(1, 5), (2, 3), (3, 1)$; $(1, 9), (3, 5), (4, 4)$; $(1, 9), (3, 5), (4, 4), (5, 0)$; $(1, 10), (4, 5), (5, 1), (6, 1)$; $(4, 8), (6, 4), (7, 3)$. The answers are $2, 4, 5, 5, 5, 5, 4$ and the true sums $2, 4, 5, 7, 5, 5, 4$. Only $t = 4$ is low: start 2 was pruned, and the answer comes from start 3, with $5 \ge 7/2$.

22. The operations make $1, 4, 1, 4, 4, 1, 0, 4, 3$ calls, 22 in all, with the cases singleton; flip and shrink; shift; flip and shrink; shrink; shift; shift; flip and shrink; shrink. After insert(g) the positions are $0, 1, 3, 5, 6, 6$ and the aggregates bcdefg, cd, d, e, ef, g. The last evict is a shrink, which costs 3 calls: the positions become $0, 1, 2, 3, 5, 5$ and the aggregates cdefg, d, e, fg, g. Both worst-case bounds, 4 per insert and 3 per evict, are reached.

23. At step 3 the sample is item 1, 2 or 3 with probability $1/3$ each. Only item 1 expires at step 4. Its successor is uniform on 2, 3, 4, and then item 4 still wins with probability $1/3$. So item 4 is the sample with probability $\frac13(\frac13 + \frac23 \cdot \frac13) + \frac23 \cdot \frac13 = 11/27$, and items 2 and 3 with $8/27$ each, against $1/3$ each in the correct order.

24. $m = \lfloor 8/4 \rfloor = 2$ and $q = \lfloor \frac12 \log_2 2^{19} \rfloor = 9$, so at least $mq^2 = 162$ bits. With $P = 2^9$ and $B = 9$, the strings have length $T = mP(2^B - 1) = 523{,}264 \le W$. The asymptotic form gives only about 19.3 bits. DGIM with $k = 7$ has $L = 4$ and $\rho = 18$, so at most 95 buckets and 1900 bits, about 12 times the lower bound.

25. At $t = 6$ the list is $(1, 3), (5, 2), (6, 1)$, and at $t = 9$ it is $(1, 6), (5, 3), (8, 2), (9, 1)$. The window is the items 2 to 9, with five x, but start 1 is outside, so the answer is $f(5) = 3$. Starts 2 to 4 were pruned while the y were arriving, because their values were close to those of later starts. The closeness did not survive the continuation x x x, so condition 4 of the definition fails.

26. The mean age is $\sum_j j\alpha\beta^j = \beta/\alpha$ with $\beta = 1 - \alpha = (N - 1)/(N + 1)$, which is $(N - 1)/2$. The variance is $\sigma^2 \sum_j \alpha^2\beta^{2j} = \alpha^2\sigma^2/(1 - \beta^2) = \alpha\sigma^2/(2 - \alpha)$, and $\alpha = 2/(N + 1)$ makes it $\sigma^2/N$. For $N = 19$, $\alpha = 0.1$, the last 19 items carry $1 - 0.9^{19} \approx 0.8649$, the limit is $1 - e^{-2} \approx 0.8647$, and the half-life is $\ln 2/(-\ln 0.9) \approx 6.58$ items.
