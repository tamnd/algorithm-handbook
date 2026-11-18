1. ◦ A sample of 100 people has 50 of genotype AA, 30 of Aa and 20 of aa. Compute the [allele frequency](/allele-frequency/) of A, the counts expected under [Hardy-Weinberg](/hardy-weinberg-principle/) proportions, the chi-squared statistic with those expectations, and the deficit of heterozygotes $1 - H_{\text{obs}}/H_{\text{exp}}$.

2. ◦ In a neutral [Wright-Fisher](/wright-fisher-model/) population of 100 diploids, a new mutation appears as a single copy. What is its probability of fixation? By what factor does the expected heterozygosity of the population fall in 100 generations?

3. ◦ A population has 1000, 100, 1000 and 1000 diploids in four successive generations. Give its [effective size](/effective-population-size/) over the four generations by the harmonic mean. A herd has 10 breeding males and 90 breeding females; give its effective size from the sex ratio.

4. ◦ Two subpopulations of equal size have allele frequencies 0.2 and 0.6. Compute $H_S$, $H_T$ and the [fixation index](/fixation-index/) $F_{ST}$.

5. ◦ The haplotype frequencies at two sites are $p_{AB} = 0.4$, $p_{Ab} = 0.1$, $p_{aB} = 0.2$ and $p_{ab} = 0.3$. Compute $D$, $D'$ and $r^2$ of [linkage disequilibrium](/linkage-disequilibrium/).

6. ◦ Give the [kinship coefficient](/kinship-coefficient/) of two half-sibs who are not inbred, and the inbreeding coefficient of a child of theirs.

7. ◦ Four aligned sequences, with ancestral base A, read `GAAAAAGA`, `AAAAAAGA`, `AAGAAAAA` and `AAAAGAAA`. Compute the number of segregating sites $S$, [Watterson's estimate](/watterson-estimator/) of $\theta$ for the region, and the mean number of pairwise differences $\hat\pi$.

8. ◦ For a sample of $n = 3$ genes under the [Ewens sampling formula](/ewens-sampling-formula/) with $\theta = 1$, give the probabilities that the three genes carry three different alleles, two alleles, and one allele.

9. ◦ A genome scan counts 1200 ABBA sites and 1000 BABA sites. Compute the D statistic of the [ABBA-BABA test](/abba-baba-test/). If the block jackknife gives a standard error of 0.03, what is the Z score?

10. • In the [Moran model](/moran-model/) with $N = 20$ and relative fitness $r = 1.05$, compute the fixation probability of a single mutant to four decimals and compare it with the neutral value.

11. • Use [Kimura's formula](/kimura-fixation-probability/) for a new mutant in a diploid population of $N = 1000$ with $s = 0.001$ and with $s = -0.001$. Give each value and its ratio to the neutral value $1/(2N)$.

12. • A recessive lethal-like allele has $s = 0.1$ and mutation rate $u = 10^{-5}$. Give its equilibrium frequency at [mutation-selection balance](/mutation-selection-balance/) when it is fully recessive, when $h = 1/2$, and when it is dominant. Explain in one sentence why the recessive case is so much higher.

13. • Ten people are genotyped at a site with 6 copies of the minor allele, and none of them is heterozygous. Use the conditional distribution of the [Hardy-Weinberg exact test](/hardy-weinberg-exact-test/) to list the probabilities of 0, 2, 4 and 6 heterozygotes given the allele counts, and give the p-value of the observation.

14. • Two biallelic sites are genotyped in 8 people: 3 are homozygous AB/AB, 2 are ab/ab, 1 is Ab/Ab, and 2 are heterozygous at both sites. Start [EM](/em-haplotype-frequency-estimation/) from equal haplotype frequencies, do one round, and find the limit of the iteration.

15. • For a sample of $n = 5$ under the [Kingman coalescent](/kingman-coalescent/) with time in units of $2N$ generations, give the expected time to the most recent common ancestor and the expected total branch length. Convert the first to generations for $N = 10^4$.

16. • Under the neutral [site frequency spectrum](/site-frequency-spectrum/) $E[\xi_i] = \theta / i$, write the expected unfolded spectrum for $n = 5$ and $\theta = 3$, and the expected folded spectrum.

17. • A [McDonald-Kreitman](/mcdonald-kreitman-test/) table has $D_n = 20$, $D_s = 10$, $P_n = 10$ and $P_s = 20$. Compute the neutrality index, the estimate $\alpha$ of the fraction of adaptive substitutions, and the two-sided p-value of Fisher's exact test to three decimals.

18. • Two coding sequences differ at a proportion 0.2 of synonymous sites and 0.05 of nonsynonymous sites. Apply the Jukes-Cantor correction of the [Nei-Gojobori method](/nei-gojobori-method/) to get $d_S$ and $d_N$, and give $\omega = d_N/d_S$.

19. • A scan has median chi-squared 0.5915. Compute the [genomic control](/genomic-control/) factor $\lambda$. A SNP has chi-squared 39.0 before correction; give its corrected statistic and say whether it still passes $5 \times 10^{-8}$.

20. • Four haplotypes over three sites read $h_0 = 010$, $h_1 = 110$, $h_2 = 011$ and $h_3 = 001$. Build the [PBWT](/positional-burrows-wheeler-transform/) orders $a_1$, $a_2$, $a_3$ by stable partitioning on each site, and check $a_3$ against a direct sort of the reversed prefixes.

21. • In [LD score regression](/ld-score-regression/), $E[\chi^2_j] = 1 + N a + N h^2 \ell_j / M$. With $N = 10^5$, $M = 10^6$, $h^2 = 0.3$ and intercept $1 + N a = 1.05$, give the expected statistic for SNPs with LD score 50 and 100. Explain why genomic control would read most of this as confounding, and why the regression cannot separate the two if all SNPs have the same LD score.

22. • From the formula for the mean absorption time of the neutral Moran model in its entry, show that a single new copy is absorbed after $N H_{N-1}$ steps on average, where $H_k = \sum_{j=1}^{k} 1/j$, and evaluate it for $N = 10$.

23. ★ Use Hoppe's urn to show that the expected number of distinct alleles in a sample of $n$ genes under the Ewens sampling formula is $\sum_{i=0}^{n-1} \theta/(\theta + i)$. Evaluate it for $n = 10$ and $\theta = 2$.

24. ★ Under the Kingman coalescent for a large population, show that the most recent common ancestor of a sample of $n$ genes is the common ancestor of the whole population with probability $(n - 1)/(n + 1)$.

25. ★ Suppose all $n$ lineages of a sample coalesce at the same moment, as in a star tree after rapid growth, so every mutation is a singleton. Express $\hat\pi$ in terms of $S$ and show that the numerator $\hat\pi - S/a_n$ of [Tajima's D](/tajimas-d/) is 0 for $n = 2$ and $n = 3$ and negative for every $n \ge 4$.

26. ★ Show that the kinship coefficient of an individual with itself is $(1 + F)/2$, where $F$ is its inbreeding coefficient. Then compute by path counting the kinship of double first cousins (their fathers are brothers and their mothers are sisters, all four parents unrelated otherwise), and the inbreeding coefficient of their child.

27. ★ A plant line reproduces only by selfing. Using the result of exercise 26, show that the inbreeding coefficient after $t$ generations is $F_t = 1 - 2^{-t}(1 - F_0)$, and find the first generation at which a line that starts with $F_0 = 0$ has $F_t \ge 0.99$. Then show that the heterozygosity of the line halves in each generation, and compare this rate with the loss of $1/(2N)$ per generation by drift.
