A bacterial genome of about five million bases arrives from the sequencer as one string. About 88 percent of it codes for protein, in more than 4,000 genes on both strands, and nothing in the string marks where they are. A human genome is worse: its 20,000 protein-coding genes are split into exons whose coding parts make up about 1.5 percent of the sequence, separated by introns that can be a hundred thousand bases long, inside a genome that is half repeats. Upstream of the genes sit short binding sites, 6 to 20 bases long, where proteins attach to switch them on and off. This chapter is about the algorithms that find these things: the genes, their exons, and the motifs that control them.

Both tasks are searches for a signal in a long string that looks random. A gene is an [open reading frame](/open-reading-frame/), a stretch with no stop codon in one frame, but a random sequence also has many short open frames. What separates real genes from chance is a set of weak statistics: codon usage, base composition at the three codon positions, the bases around splice sites. The gene finders combine these statistics with a model of gene structure, most often a [hidden Markov model](/hidden-markov-model/) decoded by the [Viterbi algorithm](/viterbi-algorithm/). A motif is a short pattern shared, with variation, by a set of sequences, and finding it is a combinatorial search over windows. The scores come from the [position-specific scoring matrix](/position-specific-scoring-matrix/) of the sequence alignment chapter.

## What the chapter covers

1. **Reading frames and coding statistics.** Open reading frames and [ORF finding](/orf-finding/), the [codon adaptation index](/codon-adaptation-index/), the [three-periodic Markov chain](/periodic-markov-chain-gene-model/) and the [interpolated Markov model](/interpolated-markov-model/) of coding DNA, and [CpG island detection](/cpg-island-detection/) with a two-state HMM or a sliding window.
2. **Gene structure.** [Gene prediction](/gene-prediction/), [splice site prediction](/splice-site-prediction/) and [maximal dependence decomposition](/maximal-dependence-decomposition/), [exon chaining](/exon-chaining/) and the [spliced alignment problem](/spliced-alignment-problem/), the [generalized HMM gene finder](/generalized-hmm-gene-finder/) and [comparative gene finding](/comparative-gene-finding/).
3. **Annotation.** [Repeat masking](/repeat-masking/), [tandem repeat finding](/tandem-repeat-finding/), [homology-based function transfer](/homology-based-function-transfer/) and the whole pipeline of [genome annotation](/genome-annotation/).
4. **Motifs and their scores.** [Motif information content](/motif-information-content/), the [motif finding problem](/motif-finding-problem/), the [median string problem](/median-string-problem/) and the exact [p-value of a weight matrix score](/pwm-score-p-value/).
5. **Searching for motifs.** [Branch and bound](/branch-and-bound-motif-search/), [greedy search](/greedy-motif-search/), [randomized search](/randomized-motif-search/), the [Gibbs motif sampler](/gibbs-motif-sampler/) and [MEME](/meme-algorithm/).
6. **Subtle motifs and other signals.** The [planted motif problem](/planted-motif-problem/), [WINNOWER](/winnower-algorithm/), [random projection](/random-projection-motif-finding/), [phylogenetic footprinting](/phylogenetic-footprinting/) and the [convolutional regulatory sequence model](/convolutional-regulatory-sequence-model/).

The groups pair up. The first three are gene finding, from single frames to a full annotation. The last three are motif finding, from the problem statement to the methods for the hardest cases.

## A first reading

1. [Open reading frame](/open-reading-frame/)
2. [ORF finding](/orf-finding/)
3. [CpG island detection](/cpg-island-detection/)
4. [Gene prediction](/gene-prediction/)
5. [Exon chaining](/exon-chaining/)
6. [Generalized HMM gene finder](/generalized-hmm-gene-finder/)
7. [Repeat masking](/repeat-masking/)
8. [Motif information content](/motif-information-content/)
9. [Motif finding problem](/motif-finding-problem/)
10. [Median string problem](/median-string-problem/)
11. [Greedy motif search](/greedy-motif-search/)
12. [Gibbs motif sampler](/gibbs-motif-sampler/)
13. [MEME](/meme-algorithm/)
14. [Planted motif problem](/planted-motif-problem/)

CpG island detection is the smallest complete HMM application in the chapter and a good warm-up for the generalized HMM. The interpolated Markov model, maximal dependence decomposition, weight matrix p-values and the subtle motif methods can wait until the first reading is done.

## Before you start

The gene finders use hidden Markov models, the Viterbi algorithm and the [hidden semi-Markov model](/hidden-semi-markov-model/) of Volume 25, and the coding statistics are [Markov chains](/markov-chain/) of Volume 17. Exon chaining is [weighted interval scheduling](/weighted-interval-scheduling/) of Volume 6. The motif entries use the [Hamming distance](/hamming-distance/) and [Shannon entropy](/shannon-entropy/) of Volume 24, [Gibbs sampling](/gibbs-sampling/) of Volume 17 and [expectation maximization](/expectation-maximization/) of Volume 25. From the sequence alignment chapter of this volume you need the weight matrix, [BLAST](/blast/) and [Smith-Waterman alignment](/smith-waterman/). Only basic probability is needed beyond these.
