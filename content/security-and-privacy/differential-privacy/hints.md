1. (a) 1 under both relations. (b) Add/remove: the count moves by 1 and the sum by up to 10, so $\Delta_1 = 11$ and $\Delta_2 = \sqrt{101}$; replace: the count is fixed, so $\Delta_1 = \Delta_2 = 10$. (c) 10 under both: add 10 to the dataset $\{0\}$ or replace its 0 by 10. (d) Add/remove: one bin and the count each move by 1, so $\Delta_1 = 2$ and $\Delta_2 = \sqrt 2$; replace: two bins and the count move, so $\Delta_1 = 3$ and $\Delta_2 = \sqrt 3$.

2. The scale is $b = 2$. $P(\lvert Z\rvert > 4) = e^{-2} \approx 0.1353$. $t = 2\ln 20 \approx 5.991$. The standard deviation is $2\sqrt 2 \approx 2.828$. For 20 bins, give each bin the failure chance $0.005$: $t = 2\ln 200 \approx 10.60$.

3. $\alpha = 1/3$. $P(Z = 0) = 1/2$, $P(Z = 1) = 1/6$, $P(\lvert Z\rvert \ge 2) = 2\alpha^2/(1+\alpha) = 1/6$, and $\operatorname{Var} Z = 2\alpha/(1-\alpha)^2 = 3/2$. The Laplace variance $2/(\ln 3)^2 \approx 1.657$ is larger.

4. $p = 4/5$. The estimate is $(0.38 - 0.2)/0.6 = 3/10$. The variance is $(4/25)/(1000 \cdot 9/25) = 1/2250$, so the standard deviation is about $0.02108$.

5. With $\exp(\varepsilon u/2)$ the weights are $2^5, 2^4, 2^2$, so the probabilities are $(8/13, 4/13, 1/13)$. With $\exp(\varepsilon u)$ they are $2^{10}, 2^8, 2^4$, so $(64/81, 16/81, 1/81)$.

8. Groups of 4: $(0.8, \delta_4)$ with $\delta_4 = 10^{-7}(e^{0.8} - 1)/(e^{0.2} - 1) \approx 5.535 \times 10^{-7}$; the simpler bound gives $4e^{0.6} \cdot 10^{-7} \approx 7.288 \times 10^{-7}$. Replace is a group of 2: $(0.4, (1 + e^{0.2}) \cdot 10^{-7}) \approx (0.4, 2.221 \times 10^{-7})$.

9. OLH: $g = 6$, variance $20/16 = 5/4$ per user, so $12500$ for the count and a standard deviation of about $111.8$. Randomized response over 100 items: $103/16$ per user, $64375$ in all, a standard deviation of about $253.7$.

11. $L = 5$, so each node has variance $2 \cdot 25 = 50$. The output at $t$ sums one node per 1 bit of $t$: $11 = 1011_2$ uses 3 nodes (variance 150), $15 = 1111_2$ uses 4 (200), $16 = 10000_2$ uses 1 (50). One node closes per time step, so the run uses 16 nodes. The simple method has variance $2 \cdot 15 = 30$ at $t = 15$. At $j = 10$ the tree gives $2420 > 2046$; at $j = 11$ it gives $3168 < 4094$, so $j = 11$, $T = 2048$.

12. (a) $\mathrm{Lap}(4)$ on the threshold and $\mathrm{Lap}(8)$ on the queries; $\hat T = 47$, the noisy answers are $39, 38, 45, 62$, and the output is $(\bot, \bot, \bot, \top)$. (b) $\sigma = 8$: $\mathrm{Lap}(8)$ and $\mathrm{Lap}(16)$. $\hat T = 54$; the noisy answers $40, 47, 47, 63$ give $\top$ at query 4; the fresh $\hat T = 44$; then $36$ gives $\bot$ and $76$ gives the second $\top$. The output is $(\bot, \bot, \bot, \top, \bot, \top)$. (c) No: $\alpha = 16(\ln 6 + \ln 20) \approx 76.6$, and the bound only says that a $\bot$ has $f_i < T + \alpha$.

14. For $k = 400$: $0.05\sqrt{800\ln 10^5} + 20(e^{0.05} - 1) \approx 4.799 + 1.025 = 5.824$, against 20. Divide the inequality by $k\varepsilon$: the advanced bound wins when $\sqrt{2\ln(1/\delta')/k} < 2 - e^{\varepsilon}$, which first holds at $k = 26$: there the bound is $1.290$ against $1.3$, while at $k = 25$ it is $1.264$ against $1.25$.

16. The first step is wrong. The classical calibration is proved only for $\varepsilon < 1$, and here it fails: $\delta(10) \approx 1.902 \times 10^{-6}$ for $\sigma = 0.5299$. The analytic calibration needs $\sigma \approx 0.5411$. The rounding step is right: post-processing keeps any valid guarantee.

18. $\rho = 100/200 = 1/2$. zCDP: $0.5 + 2\sqrt{0.5\ln 10^6} \approx 5.757$. Rényi DP: the minimum is at $\alpha = 1 + \sqrt{\ln(1/\delta)/\rho} \approx 6.26$ and gives the same $5.757$, since the Gaussian curve is exactly $\alpha\rho$. GDP: $\mu = 1$, and the exact value is $\varepsilon \approx 4.887$. The first two are upper bounds; the third is exact for this composition.

20. $A_0, \ldots, A_4 = 1, 2, 4, 6, 22$, so $\gamma = 3$ for $b = 5$ and $\gamma = 4$ for $b = 10$. The test passes with probability $\frac{1}{2}e^{4 - \ln 1000} = e^4/2000 \approx 0.0273$, so the release is almost always $\bot$. $S^* = 52e^{-1} \approx 19.13$ and the Cauchy scale is about $114.8$, which is also the median absolute error, against $69.31$ for Laplace. With 13 values neither method beats the global sensitivity.

21. The true counts are $(1, 0)$ on $x$ and $(0, 2)$ on $x'$. The log ratio of the densities at $z$ is $\varepsilon(\lvert z_1\rvert - \lvert z_1 - 1\rvert + \lvert z_2 - 2\rvert - \lvert z_2\rvert)$, at most $3\varepsilon$, reached for $z_1 \ge 1$ and $z_2 \le 0$. The theorem needs a partition fixed before the data are seen.

24. Let $P = \mathrm{Lap}(0, 1)$ and $Q = \mathrm{Lap}(1, 1)$. The log ratio $\lvert z - 1\rvert - \lvert z\rvert$ is $1 - 2z$ on $[0, 1]$, so $P > e^{\varepsilon'}Q$ exactly for $z < c = (1 - \varepsilon')/2$. Then $\delta(\varepsilon') = P(Z < c) - e^{\varepsilon'}Q(Z < c) = 1 - \frac{1}{2}e^{-c} - \frac{1}{2}e^{\varepsilon' + c - 1}$, and $\varepsilon' + c - 1 = -c$. The hockey-stick divergence is the least $\delta$ by definition, so it is tight.

27. Identity: $\Delta = 1$ and $\operatorname{tr}(WW^{\mathsf T}) = 2$, so $4/\varepsilon^2$. For $A$: the columns are $(1, t)$ and $(1, 0)$, so $\Delta_A = 1 + t$; $A^{\mathsf T}A$ has the inverse $t^{-2}\begin{pmatrix}1 & -1\\ -1 & 1 + t^2\end{pmatrix}$, and $W(A^{\mathsf T}A)^{-1}W^{\mathsf T} = 1$. For $t = 1/4$ the error is $25/(8\varepsilon^2)$. $A$ wins when $(1 + t)^2 < 2$, that is $t < \sqrt 2 - 1$. The limit is $2/\varepsilon^2$, the variance of one Laplace answer to the total.

28. Fix the other bits. Let $c_b$ be the chance of a correct guess when the bit is $b$. By the definition with the neighbor that flips the bit, $c_0 \le e^{\varepsilon}(1 - c_1)$ and $c_1 \le e^{\varepsilon}(1 - c_0)$. Add them and solve for $(c_0 + c_1)/2$. Randomized response, guessed by its report, is right with probability exactly $e^{\varepsilon}/(1 + e^{\varepsilon})$.
