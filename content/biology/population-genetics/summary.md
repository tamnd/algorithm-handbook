## What to remember

- In the neutral [Wright-Fisher model](/wright-fisher-model/) with $N$ diploids, the allele frequency is a martingale, so an allele fixes with probability equal to its frequency, and the expected heterozygosity decays as $H_t = H_0 (1 - 1/(2N))^t$. Drift removes variation in a time of order $N$ generations.
- The [Hardy-Weinberg principle](/hardy-weinberg-principle/) gives the proportions $p^2$, $2pq$, $q^2$ after one generation of random mating, under its hypotheses: Mendelian transmission, equal frequencies in the sexes, and no selection, mutation, migration or drift. With unequal frequencies in the sexes it takes two generations.
- Under the neutral [infinite sites model](/infinite-sites-model/) with $\theta = 4N\mu$, the number of segregating sites has $E[S] = \theta a_n$ with $a_n = \sum_{i=1}^{n-1} 1/i$, and the mean pairwise difference has $E[\hat\pi] = \theta$. [Watterson's estimator](/watterson-estimator/) $S/a_n$ and $\hat\pi$ agree on average, and [Tajima's D](/tajimas-d/) scales their difference. These statements hold for a neutral population of constant size, and a departure is evidence against one of those assumptions, not a measure of selection alone.
- Under the [infinite alleles model](/infinite-alleles-model/) the equilibrium homozygosity is about $1/(1 + \theta)$, and the [Ewens sampling formula](/ewens-sampling-formula/) gives the law of the allele counts of a sample with $\theta$ as its only parameter.
- [Kimura's formula](/kimura-fixation-probability/) gives the fixation probability of an additive mutant with advantage $s$ as $(1 - e^{-2s})/(1 - e^{-4Ns})$ in the diffusion limit, about $2s$ when $4Ns \gg 1$, against $1/(2N)$ for a neutral one. At [mutation-selection balance](/mutation-selection-balance/) a harmful allele sits near $u/(hs)$, $u/s$ when dominant and $\sqrt{u/s}$ when recessive.
- [Linkage disequilibrium](/linkage-disequilibrium/) is $D = p_{AB} - p_A p_B$, scaled to $D'$ by its largest possible value and to $r^2 = D^2/(p_A q_A p_B q_B)$. The [fixation index](/fixation-index/) is $F_{ST} = (H_T - H_S)/H_T$.
- A [GWAS](/genome-wide-association-study/) tests each variant alone and uses a threshold near $5 \times 10^{-8}$. Stratification inflates every statistic, which [genomic control](/genomic-control/) corrects by $\lambda$, the median observed chi-squared over 0.4549, and polygenic signal also inflates them, which [LD score regression](/ld-score-regression/) separates from confounding.
- [Haplotype phasing](/haplotype-phasing/), [imputation](/genotype-imputation/) and [local ancestry](/local-ancestry-inference/) are HMMs along the chromosome. The [Li-Stephens model](/li-stephens-model/) builds a haplotype as a mosaic of known ones, and the [Lander-Green algorithm](/lander-green-algorithm/) and [PSMC](/psmc/) are HMMs over inheritance vectors and over coalescence times.

| Method | Input | Time |
|---|---|---|
| [Hardy-Weinberg exact test](/hardy-weinberg-exact-test/) | $m$ copies of the minor allele | $\Theta(m)$ |
| [Watterson estimator](/watterson-estimator/), [Tajima's D](/tajimas-d/) | $n$ sequences, $m$ sites | $\Theta(n m)$ |
| [Coalescent simulation](/coalescent-simulation/) | $n$ copies, $s$ segregating sites | $\Theta(n + n s + s \log s)$ |
| [EM haplotype frequencies](/em-haplotype-frequency-estimation/) | $n$ people, $m$ sites, $h$ heterozygous sites, $T$ rounds | $O(T n m 2^h)$ |
| [Principal components](/genetic-principal-components/) | $n$ people, $m$ sites, $k$ components | $O(n^2 m + T n^2 k)$ |
| [ML admixture estimation](/maximum-likelihood-admixture-estimation/) | $n$ people, $m$ sites, $k$ populations, $T$ rounds | $O(T n m k)$ |
| [PBWT](/positional-burrows-wheeler-transform/) | $M$ haplotypes, $N$ sites, $R$ matches | $O(N M + R)$ |
| [Elston-Stewart](/elston-stewart-algorithm/) | $n$ people, $G$ genotypes each | $\Theta(n G^3)$ |
| [Lander-Green](/lander-green-algorithm/) | $M$ markers, $b$ meioses, $n$ people | $\Theta(M 2^b (b + n))$ |
| [Mixed model association](/mixed-model-association/) | $n$ people, $M$ SNPs | $\Theta(n^3 + M n^2)$ |
| [Genomic control](/genomic-control/) | $M$ SNPs, $N$ people | $\Theta(M N + M \log M)$ |

: Costs of the main algorithms of the chapter, as given in their entries. The two pedigree algorithms trade places: Elston-Stewart is linear in the people and Lander-Green in the markers.

## Choosing a method

To summarize diversity in a region, report $\hat\pi$ and Watterson's estimate together, and read Tajima's D only with the demography in mind: growth gives a negative $D$ across the whole genome, and a bottleneck or structure in the sample can give a positive one. Compare a region with the genome-wide distribution, not with zero. For a neutral expectation of anything more complex, simulate it with the coalescent rather than derive it.

To find structure, start with principal components, which need no model of the populations. Use the admixture model, by maximum likelihood for speed or by the Gibbs sampler for posteriors, when you want ancestry proportions for a chosen $K$. Test a specific admixture hypothesis with $f_3$, $f_4$ or the ABBA-BABA test.

For association, a mixed model is the safe default when the sample has relatives or fine structure. Genomic control is simple but treats real polygenic signal as inflation; LD score regression tells the two apart.

For pedigrees, use Elston-Stewart for large families with few markers and Lander-Green for small families with many markers.
