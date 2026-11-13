## What to remember

- Reads of length $L$ sampled at random give coverage $c = NL/G$. Depth at a base is about Poisson with mean $c$, so a fraction $e^{-c}$ of the genome is unread and there are about $N e^{-c}$ gaps. With a minimum detectable overlap $\theta$ and $\sigma = 1 - \theta$, the [Lander-Waterman model](/lander-waterman-model/) predicts $N e^{-c\sigma}$ islands. These are model expectations.
- A read set only fixes the genome when the reads span its repeats. Ukkonen's condition is necessary, and the critical length is $L_{\text{crit}} = \max(\ell_{\text{interleaved}}, \ell_{\text{triple}}) + 1$. The shortest consistent genome is the wrong target: the [shortest common superstring](/shortest-common-superstring-np-hard/) is NP-hard and collapses repeats.
- A [contig](/contig/) is safe when every genome consistent with the reads contains it. [Unitigs](/unitig/) are safe for circular genomes, and [N50](/n50/) measures only their lengths, so misjoins raise it.
- A [k-mer](/kmer/) count table takes $O(M)$ expected time with a [hash table](/hash-table/). In the [k-mer spectrum](/kmer-spectrum/), the main peak sits at $\lambda = c_k(1-e)^k$ with $c_k = c(L-k+1)/L$, and $\hat G = \sum_{j \ge v} j\,h(j)/\lambda$.
- The [string graph](/string-graph/) is the overlap graph with transitive edges removed, in $O(E)$ expected time. [Greedy merging](/greedy-shortest-common-superstring/) is within a factor 3.5 of the shortest superstring and returns the genome when adjacent reads overlap by more than the longest repeat.
- The [de Bruijn assembler](/de-bruijn-assembly/) outputs exactly the unitigs of its graph in $O(kT)$ expected time. It returns the single contig $S$ when no $(k-1)$-mer of $S$ repeats and every $k$-mer passes the count threshold. [Tip removal](/tip-removal/) and [bubble popping](/bubble-popping/) are heuristics, since no sound rule removes all errors.
- [Consensus calling](/consensus-sequence-calling/) over a fixed layout is a weighted vote with $w_i = \log(3(1-p_i)/p_i)$, exact and linear. Over an unknown alignment it is NP-hard.
- [Scaffolding](/scaffolding/) is NP-complete, and so is orienting contigs alone. [Gap filling](/gap-filling/) with integer edge lengths runs in $O(D \cdot m)$ time and is NP-hard when the lengths are written in binary.

| Method | Graph or model | Time | Guarantee | Source |
|---|---|---|---|---|
| [Greedy merging](/greedy-shortest-common-superstring/) | overlaps of $m$ reads | $O(mn + m^2 \log m)$ | ratio 3.5; exact if overlaps exceed repeats | Blum et al. 1994; Kaplan, Shafrir 2005 |
| [String graph](/string-graph/) | overlap graph, transitive reduction | $O(E)$ expected | exact reduction | Myers 2005 |
| [Overlap detection](/overlap-detection/) | generalized suffix tree | $O(n + m^2)$ | exact for exact overlaps | Gusfield, Landau, Schieber 1992 |
| [Consensus calling](/consensus-sequence-calling/) | fixed layout | $O(n)$ | exact; NP-hard without the layout | Kececioglu, Myers 1995 |
| [De Bruijn assembly](/de-bruijn-assembly/) | $(k-1)$-mer graph | $O(kT)$ expected | exact unitigs; one contig under conditions | Idury, Waterman 1995 |
| [Tip removal](/tip-removal/) | de Bruijn graph | $O(k\,m(r+1)\log m)$ | heuristic | Velvet 2008 |
| [Eulerian superpath](/eulerian-superpath-problem/) | reads as paths | $O(m + \sum \lvert P \rvert)$ for $\mu = 1$ | NP-hard with multiplicities | EULER 2001 |
| [Scaffolding](/scaffolding/) | contig graph of links | $O(mn + m^2)$ greedy | NP-complete; greedy has no ratio | Huson, Reinert, Myers 2002 |
| [Gap filling](/gap-filling/) | walks of length $D$ | $O(D \cdot m)$ | exact; NP-hard in binary | Salmela et al. 2016 |
| [Hybrid assembly](/hybrid-assembly/) | long and short reads | tool-dependent | measured | PBcR 2012 |

: The main methods of the chapter. Here $m$ is the number of reads or edges, $n$ the total read length, $E$ the number of overlap edges, $T$ the total length of the reads, $r$ the number of rounds, $D$ the target gap length and $\mu$ the multiplicity.

## Choosing a method

For accurate short reads at high coverage, build a de Bruijn graph with $k$ a few units above $\log_4 G$, clean it with tip removal and bubble popping, and resolve repeats with [paired-end reads](/paired-end-reads/). For long reads with errors, use an overlap-based assembler: find overlaps with minimizer seeds, build a string graph, lay out its paths, and polish the consensus.

Inspect the k-mer spectrum before assembling. It gives the genome size and the error rate, and it sets the count threshold. A larger $k$ resolves more repeats but lowers $c_k$, and at low $c_k$ the threshold drops true k-mers.

To join contigs, scaffold with paired or long reads, and fill the gaps by searching for walks of the estimated length. A close relative saves work through [reference-guided assembly](/reference-guided-assembly/) but can carry over its rearrangements. With both short and long reads, let the long reads set the structure and the short reads fix the bases. Judge the result by NGA50, misjoins, the k-mer QV and gene completeness, not by N50 alone.
