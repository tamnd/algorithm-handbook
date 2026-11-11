2. The number of calls received is $\mathrm{Bin}(10, 1/10)$, so its mean is 1. No call: $0.9^{10} \approx 0.349$. Exactly two: $\binom{10}{2} 0.1^2\, 0.9^8 \approx 0.194$. The probability of no call tends to $1/e \approx 0.368$.

4. Iterating from $s = 0.01$ gives $s_\infty \approx 0.107$, so about 89 percent of the nodes are reached. The peak is $1 - (1 + \ln 2.5)/2.5 \approx 0.233$. Early die-out has probability about $1/R_0 = 0.4$.

5. The gap is two standard deviations, so $P_{later} = 1 - F(120) \approx 0.0228$ and $\varphi = -\log_{10} 0.0228 \approx 1.64$. $\Phi = 3$ is reached at $\mu + z_3 \sigma = 100 + 3.09 \cdot 10 \approx 130.9$ ms.

7. The factor per cycle is $\rho = 1/4$, $1/e$ and $1/(2\sqrt e)$, so the cycles are $\ln 10^6 / \ln(1/\rho)$: $9.97$, $13.8$ and $11.6$, that is 10, 14 and 12 cycles.

10. The centre pushes to a uniform leaf each round, and the leaves can only push back to the centre, so this is a [coupon collector](/coupon-collector-problem/) with 10 coupons: $10 H_{10} \approx 29.3$ rounds. Push-pull needs 1 round from the centre, since every leaf calls the centre and pulls, and 2 rounds from a leaf: the leaf pushes to the centre in round 1, and all leaves pull in round 2.

11. Push: an uninformed node is missed by each of the 950 pushes with probability $1 - 1/999$, so the answer is $50 (1 - 1/999)^{950} \approx 50 \cdot 0.386 \approx 19.3$. Pull: an uninformed node stays so if it calls one of the other 49, so $50 \cdot 49/999 \approx 2.45$. Push-pull needs both events: $50 \cdot 0.386 \cdot 0.049 \approx 0.95$. In 4000 simulated rounds from this state the means are about 19.4, 2.46 and 0.95.

12. With $\delta = 0.1$: $0.3$, $0.12$, $0.0264$, $3.3 \times 10^{-3}$, $3.4 \times 10^{-4}$, $3.5 \times 10^{-5}$, $3.5 \times 10^{-6}$, $3.5 \times 10^{-7}$, so 8 rounds. With $\delta = 0$: $0.25$, $0.0625$, $3.9 \times 10^{-3}$, $1.5 \times 10^{-5}$, $2.3 \times 10^{-10}$, so 5 rounds. Once $\varepsilon_t \ll \delta$ the decay is only by a factor $\delta$ per round, not squaring.

17. Every edge gets $1/(1 + 2) = 1/3$, so $W$ has rows $(\frac23, \frac13, 0)$, $(\frac13, \frac13, \frac13)$, $(0, \frac13, \frac23)$. The eigenvalues are $1$, $\frac23$ and $0$, so the SLEM is $\frac23$ and $\lceil \ln 1000 / \ln 1.5 \rceil = \lceil 17.04 \rceil = 18$ rounds. The iterates are $(2, 1, 0)$ and $(\frac53, 1, \frac13)$, with mean 1 throughout.

20. $p = 1 - 0.9^{10} \approx 0.651$, so the first failed probe comes after $1/p \approx 1.54$ periods on average. A probe of a live member fails when the direct round trip fails, probability $1 - 0.9^2 = 0.19$, and all three indirect paths fail, each with probability $1 - 0.9^4 \approx 0.344$: $0.19 \cdot 0.344^3 \approx 7.7 \times 10^{-3}$.

21. The values of $1024\, i_t$ are 2.0, 4.0, 8.0, 15.8, 31.3, 61.2, 117, 215, 368, 566, 761, 899, 972, 1004, 1016, 1021.2, 1023.0 and 1023.6. After round 17 the uninformed mass is 1.04, so the count first drops below 1 after 18 rounds, against $\log_2 1024 + \ln 1024 \approx 16.9$. The seeded run on the [push gossip](/push-gossip/) page, 1, 2, 4, 8, 16, 31, 60, 115, 215, 370, 577, 754, 889, 973, ..., follows the same curve and ends in 17 rounds.

22. An uninformed node stays uninformed if none of the $(1 - \varepsilon)n$ informed nodes pushes to it, probability about $e^{-(1-\varepsilon)}$, and its own call reaches an uninformed node, probability about $\varepsilon$. Push-pull: $0.152$, $9.8 \times 10^{-3}$, $3.6 \times 10^{-5}$, $4.8 \times 10^{-10}$, so 4 rounds. Pull: $1.5 \times 10^{-5}$ after 4 rounds is still 15 nodes, so 5 rounds.

23. $\Phi_0 = 1$, and a node that picks itself keeps everything. If both pick themselves, nothing changes and $\Phi_1 = 1$. If each picks the other, both hold $(\frac12, \frac12)$ with weight 1 and $\Phi_1 = 0$. If both pick node 1, node 1 holds $(1, \frac12)$ with weight $\frac32$ and node 2 holds $(0, \frac12)$ with weight $\frac12$, so $\Phi_1 = \frac18 + \frac18 = \frac14$, and the same holds when both pick node 2. So $\mathbb{E}[\Phi_1] = (1 + 0 + \frac14 + \frac14)/4 = \frac38 = (\frac12 - \frac18)\Phi_0$. The same enumeration for $n = 3$ gives $\frac56 = (\frac12 - \frac1{12}) \cdot 2$.

24. From the centre, each tour is centre, leaf, centre, so $\hat n = k(1/k + 1) = k + 1$. From a leaf, let $M$ be the number of visits to the centre; it is geometric with mean $k$, and the tour visits $M - 1$ other leaves. So $\hat n = 1 + M/k + (M - 1)$ and $\mathbb{E}\hat n = 1 + 1 + k - 1 = k + 1$.

25. By symmetry the top eigenvector has a value $a$ at the hub and $b$ on the rim. Then $\lambda a = kb$ and $\lambda b = a + 2b$, so $\lambda(\lambda - 2) = k$ and $\lambda = 1 + \sqrt{1 + k}$. For $k = 8$, $\lambda_1 = 4$ and the threshold is $1/4$. The star $K_{1,8}$ has $\lambda_1 = \sqrt 8 \approx 2.83$ and threshold $\approx 0.354$; the rim edges make the epidemic easier to sustain.

26. The graph has $m = 13$ edges, and each side has volume $4 \cdot 3 + 1 = 13 \le m$ with one cut edge, so $\Phi = 1/13 \approx 0.077$, attained by the cut at the bridge. Numerically $\lambda_2 \approx 0.113$, and $0.057 \le 0.077 \le 0.476$. The formula with $k = 4$ gives $1/13$.
