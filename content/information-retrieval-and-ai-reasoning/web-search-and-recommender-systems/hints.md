1. Host a needs $4 \cdot 2 = 8$ seconds of gaps after its first fetch and host b needs $2 \cdot 5 = 10$, so no crawl ends before $10 + 0.5 = 10.5$ seconds, whatever the number of machines. One machine reaches it: b at 0, a at 0.5, 2.5, 4.5, 6.5 and 8.5, and b at 5 and 10. The fetches never overlap, so more machines do not help; host b sets the pace.

2. The only cycle is 1→2→3→1, so CORE is $\{1, 2, 3\}$. IN is $\{0, 5\}$, which reach the core, and OUT is $\{4\}$, which the core reaches. Of the rest, 6 hangs off IN and 7 points into OUT, so both are tendrils; 9 leads from IN to OUT without passing the core, so it is a tube. Page 8 is disconnected. From seed 0 the crawl finds $\{0, 1, 2, 3, 4\}$. From seed 5 it finds everything except 0, 7 and 8: nothing links to 0 or 7, and 8 has no links at all.

3. Here $r = \lambda I = 1$. Fixed order gives $\bar F = (1 - e^{-r})/r = 1 - e^{-1} \approx 0.632$, and purely random refresh gives $1/(1 + r) = 0.5$. The mean age is $I/2 - 1/\lambda + (1 - e^{-r})/(\lambda^2 I) = 0.25 - 0.5 + (1 - e^{-1})/2 \approx 0.066$ day, about an hour and a half.

6. With $\lambda = 0.5$: $d_1$ first; then $d_2$ scores $0.425 - 0.475 = -0.05$, $d_3$ scores $0.3 - 0.05 = 0.25$ and $d_4$ scores $0.25 - 0.1 = 0.15$, so $d_3$; then $d_4$ ($0.25 - 0.15 = 0.1$) beats $d_2$ ($-0.05$). The list is $d_1, d_3, d_4$. With $\lambda = 0.7$ it is $d_1, d_3, d_2$: $d_2$ (score $0.31$) passes $d_4$ ($0.26$) for third place. In the second step, $d_2$ beats $d_3$ when $0.85\lambda - 0.95(1 - \lambda) > 0.6\lambda - 0.1(1 - \lambda)$, that is, when $\lambda > 17/22 \approx 0.773$.

7. The gains in the first step are $0.54$, $0.48$ and $0.36$, so $d_1$ comes first. After it, the car intent is left with $1 - 0.9 = 0.1$, so $d_2$ can add only $0.6 \cdot 0.8 \cdot 0.1 = 0.048$, and $d_3$ adds $0.36$. The objective goes $0.54$, $0.90$, $0.948$. For $k = 2$ the three pairs give $0.588$, $0.84$ and $0.90$, so the greedy pair $\{d_1, d_3\}$ is optimal here.

8. The clicks have probability $0.3$, $0.7 \cdot 0.6 = 0.42$ and $0.7 \cdot 0.4 \cdot 0.5 = 0.14$, and no click has $0.7 \cdot 0.4 \cdot 0.5 = 0.14$. Rank $i$ is examined when all results above it were skipped, so the expected number examined is $1 + 0.7 + 0.28 = 1.98$.

10. The deviations of $i_1$ from the items $u_4$ rated are $-1/3$ from $i_2$ (three users), $-1/2$ from $i_3$ (two users) and $2/3$ from $i_4$ (three users). The guesses are $2/3$, $1/2$ and $14/3$. Their plain mean is $35/18 \approx 1.94$, and their mean weighted by $3, 2, 3$ is $17/8 = 2.125$.

11. The shingle sets share "the cat", "cat sat" and "sat on" out of 7, so the resemblance is $3/7$; the word sets give $5/6$. With 200 values the standard deviation is $\sqrt{(3/7)(4/7)/200} \approx 0.035$. For SimHash, $\theta = \arccos 0.9 \approx 0.451$, so each bit differs with probability $\theta/\pi \approx 0.144$, about 9.2 bits out of 64. Such a pair is usually not caught at 3 bits: SimHash is tuned for near copies, not for pages with cosine 0.9.

13. Solve the five linear equations $t = \alpha M t + (1 - \alpha) e_0$ with fractions. The result is $t^* \approx (0.309, 0.263, 0.112, 0.171, 0.145)$, and $X = t^*(2)/2 = 867/15527$. The bound is reached because no link leaves the farm, so the inequality in the proof of the bound is an equality. Spam page 3 ends up with more trust than good page 2, so a trust threshold alone cannot separate them; the spam mass variant asks instead how much of a page's PageRank comes from outside the good pages.

15. After $d_1$, the score of $d_2$ is $0.8(1 - \lambda) + 0.048\lambda$, and the score of $d_3$ is $0.6(1 - \lambda) + 0.28\lambda$. Set them equal.

17. Column $a_2 = (1, 1, 1, 0, 0)$ correlates 2 with $a_1$ and with $a_3$, and 0 with $a_4$. By symmetry and uniqueness $w_{12} = w_{32}$. Write down the KKT equation for a positive common value $w$, and check $w_{42} = 0$ with the residual. At $\lambda = 0.5$ you should get the $1/3$ of the entry.

20. Coherence $\mu$ runs from 1 (spread out) to $n$ (one coordinate). The observed entries of $e_1 e_1^\top$ are all 0, and the zero matrix has nuclear norm 0.

22. With the identity, $Y^\top Y$ costs $n r^2$ once, and each user adds $r^2$ for each nonzero count. Without it, each user pays $n r^2$.

24. Under proportional allocation every page has the same $r_i = \lambda_i / f_i$. Under uniform allocation the $r_i$ differ but have the same mean, and $1/(1 + r)$ is convex. For the optimum, use a Lagrange multiplier on the concave objective $\sum_i f_i / (f_i + \lambda_i)$. The answer gives up the fast page altogether.

25. Use four intents and documents that each cover two of them, with the first document slightly better alone but overlapping with both others.

26. Rank $i + 1$ is examined if rank $i$ was examined, the user either did not click or clicked and was not satisfied, and then chose to continue. Then multiply.

27. On a row with no sampled entry, multiply that row of the all-ones matrix by any constant: the result still has rank 1 and agrees with all samples. For the bound, use $1 - x \le e^{-x}$.

28. Over the zero cells the term is $(x_u^\top y_i)^2$. Write the sum over all cells of this term as a trace of $r \times r$ matrices, and correct the nonzero cells one by one.
