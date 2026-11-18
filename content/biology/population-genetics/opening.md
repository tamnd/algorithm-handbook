Take 2,000 people from one country, genotype them at 500,000 sites, and the data already hold a history. The allele frequencies say how far the population has drifted from its neighbors. The way alleles at nearby sites travel together says how many generations recombination has had to break them up. A few long shared segments between two people say that they are cousins. A single genome, read along its length, says how large the population was 50,000 years ago. Population genetics is the theory that turns such data into statements about populations, and the set of algorithms that make those statements in practice.

The theory rests on simple random models. In the [Wright-Fisher model](/wright-fisher-model/) each gene copy of the next generation picks a parent copy at random, so the [allele frequency](/allele-frequency/) moves by binomial sampling. Every result of the chapter holds for its model: Hardy-Weinberg proportions for random mating in a large population, the coalescent results for a neutral sample from a population of constant size, Kimura's formula for the diffusion limit. When the data disagree with a model, the disagreement is itself the signal, as with [Tajima's D](/tajimas-d/) or the [ABBA-BABA test](/abba-baba-test/).

## What the chapter covers

1. **Populations, drift and equilibrium.** Allele frequency, the Wright-Fisher model, [genetic drift](/genetic-drift/) with its loss of heterozygosity at rate $1/(2N)$ per generation, the [Hardy-Weinberg principle](/hardy-weinberg-principle/) and its [exact test](/hardy-weinberg-exact-test/), [effective population size](/effective-population-size/) and the [Moran model](/moran-model/).
2. **Mutation and diversity.** The [infinite alleles](/infinite-alleles-model/) and [infinite sites](/infinite-sites-model/) models, the [Ewens sampling formula](/ewens-sampling-formula/), [nucleotide diversity](/nucleotide-diversity/), the [site frequency spectrum](/site-frequency-spectrum/), [Watterson's estimator](/watterson-estimator/) $S/a_n$, Tajima's D and [coalescent simulation](/coalescent-simulation/).
3. **Selection.** The [Wright-Fisher diffusion](/wright-fisher-diffusion/), [Kimura's fixation probability](/kimura-fixation-probability/), [mutation-selection balance](/mutation-selection-balance/), and the tests on coding sequences: the [dN/dS ratio](/dn-ds-ratio/), the [Nei-Gojobori method](/nei-gojobori-method/), [codon models](/codon-substitution-model/) and the [McDonald-Kreitman test](/mcdonald-kreitman-test/), with [extended haplotype homozygosity](/extended-haplotype-homozygosity/) for recent sweeps.
4. **Relatedness and pedigrees.** [Identity by descent](/identity-by-descent/), the [kinship coefficient](/kinship-coefficient/), and pedigree likelihoods by the [Elston-Stewart](/elston-stewart-algorithm/) and [Lander-Green](/lander-green-algorithm/) algorithms.
5. **Haplotypes, phasing and imputation.** [Linkage disequilibrium](/linkage-disequilibrium/), [phasing](/haplotype-phasing/), [EM for haplotype frequencies](/em-haplotype-frequency-estimation/), the [Li-Stephens model](/li-stephens-model/), [imputation](/genotype-imputation/) and the [PBWT](/positional-burrows-wheeler-transform/).
6. **Structure and admixture.** The [fixation index](/fixation-index/) $F_{ST}$, [population structure inference](/population-structure-inference/) by the [STRUCTURE model](/pritchard-stephens-donnelly-model/), by [maximum likelihood](/maximum-likelihood-admixture-estimation/) and by [principal components](/genetic-principal-components/), [local ancestry](/local-ancestry-inference/), and the [f-statistics](/patterson-f-statistics/) with the ABBA-BABA test.
7. **Association and heritability.** The [genome-wide association study](/genome-wide-association-study/), [genomic control](/genomic-control/), [mixed model association](/mixed-model-association/), [SNP heritability](/snp-heritability-estimation/) and [LD score regression](/ld-score-regression/).
8. **Genealogies along the genome.** The [sequentially Markov coalescent](/sequentially-markov-coalescent/) and [PSMC](/psmc/).

## A first reading

1. [Allele frequency](/allele-frequency/)
2. [Wright-Fisher model](/wright-fisher-model/)
3. [Genetic drift](/genetic-drift/)
4. [Hardy-Weinberg principle](/hardy-weinberg-principle/)
5. [Effective population size](/effective-population-size/)
6. [Infinite sites model](/infinite-sites-model/)
7. [Watterson estimator](/watterson-estimator/)
8. [Tajima's D](/tajimas-d/)
9. [Kimura fixation probability](/kimura-fixation-probability/)
10. [Linkage disequilibrium](/linkage-disequilibrium/)
11. [Fixation index](/fixation-index/)
12. [Genome-wide association study](/genome-wide-association-study/)

The diffusion, the pedigree algorithms, the codon models and the last group can wait. They are the most mathematical parts of the chapter, and each is self-contained once the first reading is done.

## Before you start

The genealogy of a sample is the [Kingman coalescent](/kingman-coalescent/), described with [coalescent theory](/coalescent-theory/) in the phylogenetics chapter of this volume, which also has the [Jukes-Cantor model](/jukes-cantor-model/) and the [substitution models](/substitution-model/) used for coding sequences. From probability you need the [binomial distribution](/binomial-distribution/) and [martingales](/martingale/) (Volume 1) and [Markov chains](/markov-chain/) and [Gibbs sampling](/gibbs-sampling/) (Volume 17). Many methods are statistical models fitted by standard tools: the [hidden Markov model](/hidden-markov-model/), [expectation maximization](/expectation-maximization/) and [principal component analysis](/principal-component-analysis/) in Volume 25, and the [chi-squared test of independence](/chi-squared-test-of-independence/) and the [linear mixed model](/linear-mixed-model/) in Volume 33. The PBWT builds on the [Burrows-Wheeler transform](/burrows-wheeler-transform/) of Volume 24.
