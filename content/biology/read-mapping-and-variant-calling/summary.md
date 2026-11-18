## What to remember

- A quality is an error probability on a log scale: $Q = -10 \log_{10} e$, so Q20 means $e = 0.01$ and Q30 means $e = 0.001$. Base qualities, [mapping qualities](/mapping-quality/), genotype qualities and the QUAL of a [VCF](/variant-call-format/) line all use this [Phred scale](/phred-quality-score/).
- Mapping quality is the posterior probability that a read is placed wrongly, $\mathrm{MAPQ} = -10 \log_{10}(1 - P(u^* \mid x))$. Maq approximates it by $Q_{\text{second}} - Q_{\text{best}}$; each aligner has its own rule and its own cap. A read that matches two copies of a repeat equally well has posterior $1/2$, so MAPQ is 3.01 in the posterior form, and BWA writes 0.
- The [genotype likelihood](/genotype-likelihood/) treats the bases of a column as independent given the genotype, with probability $1 - e$ for a matching base and $e/3$ for each other base. A heterozygote averages the two alleles, so one read gives at most $10 \log_{10} 2 \approx 3$ phred of evidence against it.
- [Bayesian genotype calling](/bayesian-genotype-calling/) multiplies the likelihoods by a prior, such as the Hardy-Weinberg proportions of a known allele frequency, and reports the posterior. The cost is $\Theta(n)$ per site for $n$ reads.
- An indel in a repeat can be written in many places. [Normalization](/variant-normalization/) moves it left and trims shared bases, and the left-aligned parsimonious form is unique, so two call sets can be compared line by line.
- Weighted [minimum error correction](/minimum-error-correction-problem/) is NP-hard even when the fragments have no gaps, but the [dynamic program over columns](/fixed-parameter-mec/) solves it exactly in $O(2^c m)$ time for coverage $c$.
- Each structural variant signal has a blind spot. Read pairs with a cutoff of $z$ standard deviations cannot see a deletion much smaller than $z\sigma$, split reads need a read that crosses the breakpoint, depth cannot see a balanced inversion, and assembly fails in repeats.
- [Circular binary segmentation](/circular-binary-segmentation/) is a heuristic for cutting a copy number signal, with a valid permutation p-value for each test. Least squares segmentation into a given number of pieces, or with a penalty per piece, is solved exactly by [dynamic programming](/copy-number-segmentation/).

| Method | Input | Time | Exact for its model |
|---|---|---|---|
| [Base quality recalibration](/base-quality-score-recalibration/) | $n$ bases counted, $m$ recalibrated | $\Theta(n + m)$ | counts, not a model fit |
| [Duplicate marking](/duplicate-read-marking/) | $n$ reads, $b$ bases | $O(n + b)$ expected | yes, for its key |
| [Bayesian genotype calling](/bayesian-genotype-calling/) | $n$ reads at a site | $\Theta(n)$ | yes |
| [Haplotype-based calling](/haplotype-based-variant-calling/) | $R$ reads, $H$ haplotypes | $O(R H L n)$ for the pair HMMs | no, haplotypes capped |
| [Variant normalization](/variant-normalization/) | $k$ alleles of length $L$, shift $s$ | $O(k L (s + L))$ | yes |
| [Fixed-parameter MEC](/fixed-parameter-mec/) | $m$ columns, coverage $c$ | $O(2^c m)$ | yes |
| [Discordant read pairs](/discordant-read-pair-method/) | $n$ pairs, $w$ per window | $O(n \log n + n w \log n)$ | no |
| [Circular binary segmentation](/circular-binary-segmentation/) | $n$ points, $N$ permutations | $O(N n^2)$ per test, $O(N n^3)$ worst | no |
| [HMM copy number calling](/hmm-copy-number-calling/) | $n$ windows, $K$ states | $\Theta(K^2 n)$ | yes, Viterbi path |

: The main algorithms of the chapter. "Exact" means the method finds the optimum of its own objective; it does not mean the calls are right.

## Choosing a method

For germline SNVs and short indels in a sample sequenced at 30x, a haplotype-based caller is the standard, since local assembly handles reads that a pileup caller would misalign around an indel. A pileup caller with [genotype likelihoods](/genotype-likelihood/) is simpler, faster and good enough for SNVs away from indels. Normalize both call sets before comparing them, and judge a caller by precision and recall on a benchmark genome rather than by its QUAL values.

For tumors, use a [somatic caller](/somatic-variant-calling/) with a matched normal. The power to see a variant is a binomial tail in the depth and the allele fraction, so low purity calls for more depth, not a lower threshold.

For variants of 50 bases or more, combine signals: [discordant pairs](/discordant-read-pair-method/) find candidates, [split reads](/split-read-method/) give the breakpoints to the base, and depth confirms a change in copy number. For copy number alone, the exact DP is the choice when $n$ is small enough for its quadratic cost; [CBS](/circular-binary-segmentation/) and an [HMM](/hmm-copy-number-calling/) scale to more windows, and the HMM also labels each segment with a copy number.

For phasing a single sample from long reads, use the [fixed-parameter algorithm](/fixed-parameter-mec/) after downsampling to a coverage the $2^c$ factor allows.
