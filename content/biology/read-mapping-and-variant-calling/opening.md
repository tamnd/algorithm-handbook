A human genome sequenced at 30x coverage comes off the machine as about 600 million reads of 150 bases, each base with a quality. None of those reads says where it came from or how it differs from the reference. The work of this chapter turns them into a list of differences: a single base changed at one position, three bases deleted at another, a 5 kb deletion further on, two extra copies of a gene on one chromosome. A clinical lab reports such lists for each patient, and a cancer study compares the list from a tumor with the list from the same person's blood.

The work runs as a pipeline. The reads are mapped to the reference, cleaned, and stacked into columns. Then a caller decides at each position which genotype the reads support. Every step works with probabilities. A base quality is the probability that the base is wrong, a mapping quality is the probability that the read is in the wrong place, and a call carries the probability that the genotype is wrong. The mappers are heuristics, so they can miss the true place of a read. The callers are judged by measured precision and recall against benchmark genomes, not by a proof.

## What the chapter covers

1. **Formats and qualities.** The [Phred scale](/phred-quality-score/) $Q = -10 \log_{10} e$ for error probabilities, the [SAM format](/sam-alignment-format/) with its FLAG bits and CIGAR strings, the [pileup](/read-pileup/) of bases at each position, the [VCF format](/variant-call-format/) for calls, and the [mapping quality](/mapping-quality/) of a read.
2. **Mapping pairs and preparing the reads.** [Paired-end mapping](/paired-end-read-mapping/) with mate rescue, [duplicate marking](/duplicate-read-marking/) by the unclipped 5' ends of the reads, [base quality score recalibration](/base-quality-score-recalibration/) from counts of mismatches, and the [variation graph](/variation-graph/) as a reference that holds known variants.
3. **Calling small variants.** The [genotype likelihood](/genotype-likelihood/) of the reads at a site, the [variant calling problem](/variant-calling-problem/), [Bayesian genotype calling](/bayesian-genotype-calling/) with a prior, [variant normalization](/variant-normalization/) of indels, [haplotype-based calling](/haplotype-based-variant-calling/) with local assembly and a pair HMM, [VQSR](/variant-quality-score-recalibration/) filtering, and [somatic calling](/somatic-variant-calling/) in tumors.
4. **Haplotype assembly.** Splitting the heterozygous alleles into the two chromosomes with [haplotype assembly](/haplotype-assembly/), the NP-hard [minimum error correction problem](/minimum-error-correction-problem/), and the [fixed-parameter dynamic program](/fixed-parameter-mec/) that solves it in $O(2^c m)$ time for coverage $c$ and $m$ sites.
5. **Structural variants.** The four signals of [structural variant detection](/structural-variant-detection/), with [discordant read pairs](/discordant-read-pair-method/) and [split reads](/split-read-method/) in detail.
6. **Copy number.** [Copy number segmentation](/copy-number-segmentation/) as a change-point problem, [read-depth analysis](/read-depth-copy-number-analysis/), [circular binary segmentation](/circular-binary-segmentation/) and [HMM calling](/hmm-copy-number-calling/) by the Viterbi algorithm in $\Theta(K^2 n)$ time.

## A first reading

Read the formats first, then follow one variant from the reads to the VCF line:

1. [Phred quality score](/phred-quality-score/)
2. [SAM alignment format](/sam-alignment-format/)
3. [Read pileup](/read-pileup/)
4. [Mapping quality](/mapping-quality/)
5. [Genotype likelihood](/genotype-likelihood/)
6. [Variant calling problem](/variant-calling-problem/)
7. [Bayesian genotype calling](/bayesian-genotype-calling/)
8. [Variant call format](/variant-call-format/)
9. [Variant normalization](/variant-normalization/)
10. [Structural variant detection](/structural-variant-detection/)
11. [Copy number segmentation](/copy-number-segmentation/)

The preparation steps, haplotype-based calling, VQSR and the somatic caller refine this core and can wait. So can the haplotype assembly group, which reads best after a first pass through the calling group, and the variation graph, which changes the reference rather than the caller.

## Before you start

The reads come from a mapper. [Read mapping](/read-mapping/), the [seed-and-extend](/seed-and-extend/) strategy and the mappers [BWA](/bwa/) and [minimap2](/minimap2/) are in other chapters of this volume, as are [paired-end reads](/paired-end-reads/), [sequencing coverage](/sequencing-coverage/) and the [pair HMM](/pair-hmm/). The probability used throughout is basic: the [binomial distribution](/binomial-distribution/) in Volume 1, and [Bayes' theorem](/bayes-theorem/), the [hidden Markov model](/hidden-markov-model/) and the [Gaussian mixture model](/gaussian-mixture-model/) in Volume 25. Copy number segmentation is a case of [change-point detection](/change-point-detection/) in Volume 33, and the exact algorithm for haplotype assembly is a [fixed-parameter tractable](/fixed-parameter-tractable/) one in the sense of Volume 39. No biology is assumed beyond the fact that a human cell carries two copies of each autosome.
