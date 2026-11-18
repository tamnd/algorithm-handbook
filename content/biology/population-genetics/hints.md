1. $p = (2 \cdot 50 + 30)/200 = 0.65$. The expected counts are 42.25, 45.5 and 12.25, the chi-squared statistic is 11.60, and the heterozygote deficit is $1 - 0.30/0.455 = 0.341$.

5. $p_A = 0.5$ and $p_B = 0.6$, so $D = 0.4 - 0.3 = 0.1$. For $D > 0$ the largest value is $\min(p_A q_B, q_A p_B) = 0.2$, so $D' = 0.5$, and $r^2 = 0.01/(0.5 \cdot 0.5 \cdot 0.6 \cdot 0.4) = 1/6$.

7. $S = 4$ and $a_4 = 11/6$, so $\hat\theta_W = 24/11 \approx 2.18$. A site whose derived base is in $k$ of 4 sequences adds $k(4 - k)/6$ to $\hat\pi$: three singletons and one doubleton give $(9 + 4)/6 = 13/6 \approx 2.17$.

8. Three alleles: $\theta^2/((\theta + 1)(\theta + 2)) = 1/6$. One allele: $2/((\theta + 1)(\theta + 2)) = 1/3$. Two alleles: the rest, $1/2$.

11. For $s = 0.001$, $u = (1 - e^{-0.002})/(1 - e^{-4}) = 0.002035$, 4.07 times the neutral $0.0005$. For $s = -0.001$, $u = 3.735 \times 10^{-5}$, 0.075 times the neutral value.

13. The conditional probabilities are $1/323$, $42/323$, $168/323$ and $112/323$. Only the observation itself is as unlikely as the observation, so the p-value is $1/323 \approx 0.0031$.

14. With equal frequencies, each double heterozygote splits $1/2$ to AB/ab and $1/2$ to Ab/aB. The counts become 7, 3, 1 and 5 of 16 for AB, Ab, aB and ab. The share given to Ab/aB keeps shrinking, and the iteration tends to $p_{AB} = 1/2$, $p_{Ab} = 1/8$, $p_{aB} = 0$, $p_{ab} = 3/8$, slowly.

17. $\mathrm{NI} = (10/20)/(20/10) = 0.25$ and $\alpha = 1 - D_s P_n/(D_n P_s) = 0.75$. Fisher's exact test on the table gives $p \approx 0.019$.

20. $a_1 = (0, 2, 3, 1)$, $a_2 = (3, 0, 2, 1)$ and $a_3 = (0, 1, 3, 2)$. The reversed prefixes after three sites are 010, 011, 110 and 100 for $h_0$ to $h_3$, which sort as $h_0, h_1, h_3, h_2$.

23. The urn adds a new allele at draw $i + 1$ with probability $\theta/(\theta + i)$, whatever happened before. Sum the indicator expectations. For $n = 10$ and $\theta = 2$ the value is $55991/13860 \approx 4.040$.

24. Look at the two lineages just below the root of the whole population's tree. The share $X$ of the population that descends from one of them is uniform on $(0, 1)$, by the Pólya urn that the coalescent forms going forward. The sample MRCA is the root exactly when the sample has members on both sides, which has probability $1 - E[X^n + (1 - X)^n] = 1 - 2/(n + 1)$.

25. A singleton adds $(n - 1)/\binom{n}{2} = 2/n$ to $\hat\pi$, so $\hat\pi = 2S/n$ and the numerator is $S(2/n - 1/a_n)$. It is zero when $a_n = n/2$, which holds for $n = 2$ and 3. Since $a_{n+1} - a_n = 1/n < 1/2$ for $n \ge 3$, $a_n < n/2$ for all $n \ge 4$.

26. Draw two copies from one person with replacement: the same copy with probability $1/2$, and the two different copies, which are IBD with probability $F$, otherwise. Double first cousins have four common ancestors, each joined by a path through five people, so the kinship is $4 \cdot (1/2)^5 = 1/8$, and so is the inbreeding coefficient of their child.

27. The child of a selfed plant has $F$ equal to the kinship of the parent with itself, $(1 + F)/2$, so $1 - F_t = (1 - F_{t-1})/2$. With $F_0 = 0$, $2^{-t} \le 0.01$ first holds at $t = 7$. The heterozygosity is $2pq(1 - F_t)$ and halves in each generation, as drift would only in a population of a single diploid.
