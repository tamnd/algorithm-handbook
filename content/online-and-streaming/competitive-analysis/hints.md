1. The worst season ends on the buying day, so the worst ratio is $(j - 1 + 5)/\min(j, 5)$. For $j = 1, \ldots, 8$ this gives $5, 3, 7/3, 2, 9/5, 2, 11/5, 12/5$. The best is $j = 5$ with $9/5 = 2 - 1/5$.

3. If the lift comes just after you leave, you pay $w + S$ and the optimum pays $\min(w + E, S)$. Waiting 40 gives $90/50 = 9/5$. Waiting 30 gives a ratio that tends to $80/40 = 2$, and waiting 45 gives $95/50 = 19/10$.

4. Target 6 to the left: excursions 1, 2 and 4 cost $2(1 + 2 + 4) = 14$, then the walk of 6 finds it, so 20 in total and ratio $10/3$. Target 5 to the right: four full excursions cost $2(1 + 2 + 4 + 8) = 30$, so 35 in total and ratio 7.

7. Frequency count pays $3 \cdot 1 + 3 \cdot 2 + 4 \cdot 3 = 21$: $c$ passes $a$ and $b$ only at its fourth request, when its count exceeds theirs. Move-to-front pays $3 + 4 + 6 = 13$. The old counts of $a$ and $b$ keep $c$ at the back while it is the only item requested.

10. The nearest earlier points are at distances $9, 3, 3, 1$, so greedy pays 16, and every online algorithm pays at least 16, since each point needs an edge to some earlier point. The minimum spanning tree is the path from 0 to 9, of weight 9. The ratio is $16/9$.

12. The weights are $4/9, 2/3, 1$, so the probabilities are $4/19, 6/19, 9/19$. A season of 1 day costs $\frac{4}{19} \cdot 3 + \frac{15}{19} \cdot 1 = 27/19$; a season of 2 days costs $\frac{4}{19} \cdot 3 + \frac{6}{19} \cdot 4 + \frac{9}{19} \cdot 2 = 54/19$ against 2; a season of 3 days or more costs $81/19$ against 3. The ratio is $27/19 \approx 1.421$ every time, equal to $1/(1 - 8/27)$, against $5/3$ for the best deterministic rule.

13. The worst target on a ray sits just beyond the last visit to that ray, at about $b^{k-3}$, and is found at excursion $k$ after the walk $2\sum_{i<k} b^i \approx 2b^k/(b - 1)$. Dividing by $b^{k-3}$ gives $1 + 2b^3/(b - 1)$. For $b = 2$ it is 17. The derivative of $b^3/(b - 1)$ vanishes at $b = 3/2$, which gives $14.5$.

14. The first batch has waited $0.5$ by time $0.5$, and two packets then add the rest in $0.25$, so the first acknowledgment is at $0.75$. The second batch has waited $0.3$ by time $2.2$, and three packets add $0.7$ in $7/30$, so the second is at $73/30 \approx 2.43$. Greedy pays $2 + 2 = 4$. The optimum acknowledges at $0.5$ and $2.2$ and pays $2 + 0.5 + 0.3 = 2.8$. The ratio is $10/7$.

15. $M = 10$ with probability $1/4$, and otherwise $M = X_1$, so $\mathbb{E}[M] = 2.5 + 1.5 = 4$. The threshold 2 takes $X_1 = 3$ and otherwise waits for $X_2$: $\frac12 \cdot 3 + \frac12 \cdot 2.5 = 11/4$. Going on is worth $\mathbb{E}[X_2] = 2.5$, so the best rule also takes $X_1$ only when it is 3, and it earns $11/4$ as well, $11/16$ of the prophet.

19. COUNT pays 1, 1 and a move of 1 for the first two requests, nothing for the next two, 1, 1 and a move for the two requests from node 0, and 1, 1 and a move for the last two: 9. The optimum serves the first request from node 0, moves the page once, and pays 2 for the two requests from node 0: 4. The ratio is $9/4$.

22. The first point opens, at cost 6. The second opens with probability $2/6$, so its expected cost is $\frac13 \cdot 6 + \frac23 \cdot 2 = 10/3$. The third sees distance 3 with probability $1/3$ and then opens with probability $1/2$, or distance 5 with probability $2/3$ and then opens with probability $5/6$. Its expected cost is $\frac13 \cdot \frac92 + \frac23 \cdot \frac{35}{6} = 97/18$. The total is $6 + 10/3 + 97/18 = 265/18 \approx 14.72$. One facility at 2 costs $6 + 2 + 3 = 11$.

25. $\mathbb{E}[\mathrm{OPT}] = \frac13 \cdot 1 + \frac29 \cdot 2 + \frac49 \cdot 3 = 19/9$. Buying on day 1 costs 3. Buying on day 2 or 3 costs $\frac13 + \frac23 \cdot 4 = 3$ and $\frac13 + \frac29 \cdot 2 + \frac49 \cdot 5 = 3$. Buying on day 4 or 5 costs more, and never buying costs 3. So every deterministic rule pays at least 3 in expectation, and by Yao's principle every randomized rule has ratio at least $3/(19/9) = 27/19$.

26. Take the target at $d = 2^k(1 + \varepsilon)$ on one side. With one first direction the next excursion to that side has length $2^{k+2}$, with the other it has length $2^{k+1}$. The two walks are $2(2^{k+2} - 1) + d$ and $2(2^{k+1} - 1) + d$, with mean $6 \cdot 2^k - 2 + d$, so the ratio just beyond $2^k$ is $7 - 2^{1-k}$. A target at $x \cdot 2^k$ with $1 < x \le 2$ gives about $1 + 6/x$, which is smaller. So the worst ratio is 7, approached as $k$ grows but never attained, against 9 for a fixed first direction.

27. In each phase the rule pays $\alpha$ and then 1 to move. The optimum either stays in one state and pays $\alpha$ every second phase, or moves every phase and pays 1, so it pays about $\min(\alpha/2, 1)$ per phase. The ratio is $(\alpha + 1)/\min(\alpha/2, 1)$, which is $2 + 2/\alpha$ for $\alpha \le 2$ and $\alpha + 1$ for $\alpha \ge 2$. The best is $\alpha = 2$, with ratio $3 = 2n - 1$.

28. The adversary makes each outcome the opposite of the learner's prediction. The two experts are right in different rounds, so their mistakes add to $T$, and the better one has at most $T/2$. So no deterministic bound can have a factor below 2 in front of $m^*$. For $\beta = 0.9$ the factors are $2.05$ and $19.5$, and for $\beta = 0.99$ they are $2.005$ and $199.5$: the factor of $m^*$ tends to 2 while the factor of $\ln n$ grows.

30. If $y \ge 10$ the rule buys on day 5, and a season of 5 days costs $14$ against 5: ratio $2.8$. If $y < 10$ it buys on day 20, and a season of 20 days or more costs $29$ against 10: ratio $2.9$. Both are below the robustness bound 3. With a right prediction the ratio is $14/10 = 1.4$ for long seasons and 1 for short ones, below the consistency bound $1.5$.
