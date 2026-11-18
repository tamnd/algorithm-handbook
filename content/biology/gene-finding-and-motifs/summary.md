## What to remember

- An [open reading frame](/open-reading-frame/) is necessary for a gene but far from sufficient. In random sequence with equal base frequencies a stop codon comes every $64/3 \approx 21$ codons on average, so short ORFs are everywhere, and a long ORF is evidence only because random ones are rarely long.
- Coding DNA has statistics that depend on the codon position. The [three-periodic Markov chain](/periodic-markov-chain-gene-model/) and the [interpolated Markov model](/interpolated-markov-model/) score a stretch in each of the six frames, and the frame with the best score is the likely coding frame.
- [CpG island detection](/cpg-island-detection/) is the model case of HMM segmentation: two states, a Viterbi pass in $\Theta(n)$, and islands read off as runs of one state. The transition probabilities set how long a run must be before a state change pays.
- Eukaryotic gene finding is a parse of the sequence into exons, introns and intergenic regions. The [generalized HMM](/generalized-hmm-gene-finder/) does it with explicit length distributions in $\Theta(nKD + nK^2)$, and [exon chaining](/exon-chaining/) is the simplest version, weighted interval scheduling in $\Theta(n \log n)$.
- Repeats are masked first, or the gene finder reports the open frames of transposable elements as genes.
- The [information content](/motif-information-content/) of a motif is a sum of relative entropies of its columns, at most 2 bits per column for DNA with a uniform background. It is 0 for a column that matches the background.
- [Motif finding](/motif-finding-problem/) and the [median string problem](/median-string-problem/) are the same problem under the Hamming score, and they are NP-hard when the motif length is part of the input.
- The local methods differ in how they leave a local optimum. [Greedy search](/greedy-motif-search/) never revisits a choice, [randomized search](/randomized-motif-search/) restarts, the [Gibbs sampler](/gibbs-motif-sampler/) draws sites at random so that it can move to a worse state, and [MEME](/meme-algorithm/) runs EM from many seeds.
- In the [planted motif problem](/planted-motif-problem/) two copies of a $(15, 4)$ motif with exactly 4 changes each differ from each other in about 6.6 positions on average, so millions of random pairs of windows are as close as the true pairs. [WINNOWER](/winnower-algorithm/) and [random projection](/random-projection-motif-finding/) were designed for this case.

| Method | Input | Time |
|---|---|---|
| [ORF finding](/orf-finding/) | $G$ bases, $R$ ORFs reported | $\Theta(G + R \log R)$ |
| [CpG island detection](/cpg-island-detection/) | $n$ bases | $\Theta(n)$ |
| [Codon adaptation index](/codon-adaptation-index/) | $M$ reference codons, $N$ codons in the gene | $\Theta(M + N)$ |
| [Exon chaining](/exon-chaining/) | $n$ candidate exons | $\Theta(n \log n)$ |
| [Generalized HMM gene finder](/generalized-hmm-gene-finder/) | $n$ bases, $K$ states, segments up to $D$ | $\Theta(nKD + nK^2)$ |
| [Branch-and-bound motif search](/branch-and-bound-motif-search/) | $n$ sequences, $W$ windows each, length $L$ | $O(4^L n W)$ |
| [Greedy motif search](/greedy-motif-search/) | the same | $O(W^2 n L)$ |
| [Gibbs motif sampler](/gibbs-motif-sampler/) | the same, $T$ iterations | $O(T n W L)$ |
| [MEME](/meme-algorithm/) | the same, $I$ EM iterations | $O(n W^2 L + I n W L)$ |
| [Weight matrix p-value](/pwm-score-p-value/) | $L$ columns, $S$ partial scores, $r$ rounds | $O(r L c S)$ with $c = 4$ |

: Costs of the main algorithms of the chapter, as given in their entries. The $W^2$ terms of greedy search and MEME come from trying every window of the data as a seed.

## Choosing a method

For a prokaryotic genome, ORF finding with a length cutoff and a coding score from an interpolated Markov model trained on the genome itself finds most genes, because the genes are long and have no introns. For a eukaryotic genome, mask repeats first, then run a generalized HMM gene finder trained for a related species, and add evidence: aligned proteins through [spliced alignment](/spliced-alignment-problem/), a second genome through [comparative gene finding](/comparative-gene-finding/), and transcripts. [Genome annotation](/genome-annotation/) pipelines combine all of these, and then name the genes by [homology-based function transfer](/homology-based-function-transfer/).

For motifs in a few dozen promoter regions with a motif of 6 to 12 bases, MEME or the Gibbs sampler is the usual first choice. Run either from many starts, since both can stop at a local optimum. For short motifs, exact search over all $4^L$ strings by the median string or branch and bound is feasible and gives a certificate. When the copies are weak, as in the planted motif problem, use random projection to find the start and then refine it with EM. When orthologous regions from several species are available, [phylogenetic footprinting](/phylogenetic-footprinting/) uses conservation, which is evidence of a different kind. When many labeled regions are available, as in a chromatin assay, a [convolutional model](/convolutional-regulatory-sequence-model/) learns the motifs and their interplay together. In every case, report a [p-value](/pwm-score-p-value/) for the sites found, against the right background.
