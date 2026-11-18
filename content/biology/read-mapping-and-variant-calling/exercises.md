1. ◦ Convert the [Phred quality](/phred-quality-score/) 25 to an error probability, and the error probability 0.002 to a quality rounded to an integer.

2. ◦ Decode the SAM FLAG values 83 and 163 into their bits, and say what each read is: paired or not, properly paired or not, which strand it and its mate are on, and whether it is the first or second read of the pair.

3. ◦ A [SAM](/sam-alignment-format/) record has POS 100 and CIGAR `5S20M2I10M3D15M`. How many bases does its SEQ field hold, and what is the last reference position covered by the alignment?

4. ◦ A column of a [pileup](/read-pileup/) holds four A bases and one G base, all of quality 20, at a site where the reference is A. With the model of the [genotype likelihood](/genotype-likelihood/) entry ($1 - e$ for a match, $e/3$ for each other base, and the average of the two alleles for a heterozygote), compute the three PL values for AA, AG and GG, rounded to integers. Which genotype has the highest likelihood?

5. ◦ The best hit of a read has one mismatch, at a base of quality 30. The second hit has the same mismatch and one more, at a base of quality 25, and no other hit is close. Give the [mapping quality](/mapping-quality/) from the approximation $Q_{\text{second}} - Q_{\text{best}}$, and from the posterior form with $e/3$ for a mismatch and $1 - e$ for a match, to two decimals.

6. ◦ Four single-end reads are aligned to the forward strand: read a with POS 1000 and CIGAR `50M`, read b with POS 1003 and CIGAR `3S47M`, read c with POS 1000 and CIGAR `2S48M`, and read d with POS 998 and CIGAR `50M`. Compute the unclipped 5' end of each read and say which reads [duplicate marking](/duplicate-read-marking/) groups together.

7. ◦ The reference is `ACTGTGTGC` at positions 1 to 9, and a caller reports the deletion POS 6, REF `GTG`, ALT `G`. Write the [normalized](/variant-normalization/) form of the variant as a VCF POS, REF and ALT.

8. ◦ A somatic SNV is present in 10 percent of the reads of a tumor, and a call needs at least 4 alternative reads. What is the chance of a call at depth 40? Give four decimals.

9. • Take the likelihoods of exercise 4 and a Hardy-Weinberg prior with alternative allele frequency 0.1. Compute the posterior of each genotype and the genotype quality of the most probable one.

10. • A site is heterozygous and has depth 12, and each read carries either allele with probability $1/2$. A caller misses the site when 2 or fewer reads show the alternative allele. Compute the chance of a miss as an exact fraction.

11. • In one bin of [base quality score recalibration](/base-quality-score-recalibration/), 4000 bases reported as Q30 show 12 mismatches at sites that are not known variants. Compute the empirical quality with the rule $-10 \log_{10}((m + 1)/(n + 2))$, and the delta that is added for this bin. Explain why the known variant sites are left out of the counts.

12. • A library has insert size mean 400 and standard deviation 30, and the [discordant read pair method](/discordant-read-pair-method/) flags pairs whose span exceeds $\mu + 3\sigma$. Model the span of a pair across a deletion of length $D$ as normal with mean $400 + D$ and the same deviation. What fraction of the spanning pairs is flagged for $D = 90$, 120 and 150? With 10 spanning pairs and $D = 90$, what is the chance that at least 2 are flagged?

13. • Five fragments cover four heterozygous sites (a dash is a site the fragment does not cover): `011-`, `-110`, `10-1`, `010-` and `-001`. Compute the unweighted [MEC](/minimum-error-correction-problem/) cost of the haplotype pair `0110` and `1001`, and show that no pair of complementary haplotypes has cost 0.

14. • A copy number signal over eight windows reads 0.2, −0.1, 0.1, 1.2, 0.9, 1.1, 1.0, 0.1. Find the least squares [segmentation](/copy-number-segmentation/) into two segments and into three segments, with the sum of squared errors of each.

15. • [VQSR](/variant-quality-score-recalibration/) uses one annotation $x$, a good model $N(0, 1)$ and a bad model $N(2, 1)$. Write the natural log density ratio $\log p_{\text{good}}(x) - \log p_{\text{bad}}(x)$ as a function of $x$ and evaluate it at $x = 0$, 1 and 3. Explain why the value 0 at $x = 1$ does not mean that a call there is real with probability $1/2$.

16. • A read of 100 bases is [split](/split-read-method/): its first 60 bases align to reference positions 1000 to 1059 and its last 40 bases align to positions 1360 to 1399. What deletion does this show? If the reference base at 1060 equals the base at 1360, where else can the breakpoint be placed, and why does this not change the deleted length?

17. • Model a read with exactly two hits, of likelihoods $10^{-Q_1/10}$ and $10^{-Q_2/10}$ with $\Delta = Q_2 - Q_1 \ge 0$, and a uniform prior. Show that the posterior mapping quality is $10 \log_{10}(1 + 10^{\Delta/10})$, and that it exceeds $\Delta$ by more than 0 and at most $10 \log_{10} 2 \approx 3.01$.

18. • A site has $d$ reads, all showing the reference base A, each with error probability $e = 0.001$. Show that the PL of AG is $10 d \log_{10}\bigl(2(1 - e)/(1 - 2e/3)\bigr)$, and find the smallest $d$ that gives a homozygous reference call a genotype quality of at least 20.

19. ★ An [HMM copy number caller](/hmm-copy-number-calling/) has two states, stays in a state with probability $1 - \varepsilon$ and switches with probability $\varepsilon$. Inside a long run of state 1, consider a Viterbi path that switches to state 2 for $L \ge 1$ windows and back. Show that the excursion beats staying in state 1 exactly when the sum of the log emission ratios $\log(p_2(x_t)/p_1(x_t))$ over the $L$ windows exceeds $2 \log((1 - \varepsilon)/\varepsilon)$, whatever $L$ is. Evaluate the threshold for $\varepsilon = 10^{-3}$ in natural logs.

20. ★ A tumor has purity 0.3, and a clonal heterozygous SNV sits in a diploid region, so its expected allele fraction is 0.15. A call needs at least 4 alternative reads. Find the smallest depth that gives a [somatic](/somatic-variant-calling/) call with probability at least 0.95. At that depth, if each read shows one given wrong base with probability 0.001, what is the chance that a site with no mutation reaches 4 such reads?

21. ★ One billion single-end reads have 5' ends spread uniformly over $6.2 \times 10^9$ keys (two strands of a genome of $3.1 \times 10^9$ bases), with no true duplicates. What fraction of the reads does duplicate marking flag by chance? Then use pairs, whose key also includes a fragment length spread uniformly over 200 values, and compute the fraction again. Use the Poisson approximation.

22. ★ Each fragment covers exactly two adjacent heterozygous sites. Show that weighted MEC then splits into independent choices, one for each pair of adjacent sites, and is solved in linear time. Apply it to four sites with fragments `00`, `11`, `01` on sites 1 and 2, fragments `01`, `10`, `10`, `00` on sites 2 and 3, and `11` on sites 3 and 4, all of weight 1: give the optimal cost and a haplotype pair that reaches it.
