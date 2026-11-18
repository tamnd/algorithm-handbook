1. ◦ A sample has three genes with effective lengths 1000, 2000 and 4000 bases and read counts 300, 200 and 100, and no other reads. Compute the [FPKM](/rpkm-and-fpkm/) and the [TPM](/transcripts-per-million/) of each gene. Check that TPM is FPKM times $10^6$ divided by the sum of the FPKM values.

2. ◦ In a second sample of the same three genes, the counts are 300, 200 and 1100. Compute the TPM of the first gene. Its count did not change; explain in one sentence why its TPM did.

3. ◦ Compute the [median of ratios](/median-of-ratios-normalization/) size factors of two samples with these counts for five genes: $(10, 20)$, $(20, 40)$, $(30, 60)$, $(40, 400)$ and $(0, 7)$. Which gene is left out, and why does the fourth gene not change the answer?

4. ◦ Apply [quantile normalization](/quantile-normalization/) to two samples of three genes, with values $(5, 2, 3)$ in sample A and $(4, 1, 6)$ in sample B. Give the target distribution and the normalized matrix.

5. ◦ A universe has 20 genes. A gene set has 5 of them, and a list of 4 changed genes shares 3 genes with the set. Compute the one-sided p-value of [over-representation analysis](/over-representation-analysis/) as an exact fraction, and the expected overlap under the null.

6. ◦ A bundle of one cell and one locus has these UMIs and read counts: AAAA 40, AAAC 25, AAAT 15, CCCC 8, AATT 6, CCCG 3, GCCG 1. How many molecules do the "unique", "cluster" and directional methods of [UMI deduplication](/umi-deduplication/) report? List the directional groups.

7. ◦ Two transcripts A and B have the same effective length. The equivalence classes are $\{A\}$ with 30 reads, $\{A, B\}$ with 60 reads and $\{B\}$ with 10 reads. Run one round of the [EM](/em-isoform-quantification/) from $\alpha = (1/2, 1/2)$, then find the fixed point.

8. ◦ A gene follows the [negative binomial model](/negative-binomial-count-model/) with mean 50 and dispersion $\alpha = 0.2$. Give its variance, the part of the variance beyond the Poisson part, and the mean at which the two parts are equal.

9. ◦ In a [pseudoalignment](/pseudoalignment/) index, the k-mers of a read have the colors $\{T_1, T_2, T_3\}$, $\{T_1, T_2\}$ and $\{T_1, T_2, T_4\}$, and one more k-mer of the read is not in the index. What compatible set is reported? Is the source transcript sure to be in it if the read has a sequencing error?

10. • A [splice graph](/splice-graph/) has nodes 1 to 6 and edges $(1,2)$, $(1,3)$, $(2,3)$, $(2,4)$, $(3,4)$, $(3,5)$, $(4,5)$, $(4,6)$, $(5,6)$. Count the paths from node 1 to node 6 by the dynamic program over a topological order. Give the count at every node.

11. • A splice graph has nodes 1 to 5 and edges $(1,2)$, $(1,3)$, $(2,4)$, $(3,4)$, $(3,5)$, $(4,5)$. The fragments are $(1,2)$, $(2,4)$, $(1,3)$, $(3,4)$, $(4,5)$ and $(3,5)$. Find the fewest paths that together hold every fragment, as in [minimum path cover assembly](/minimum-path-cover-transcript-assembly/). Prove that fewer paths do not suffice by giving fragments no two of which fit on one path.

12. • In limma, the prior has $d_0 = 4$ and $s_0^2 = 0.5$. A gene with two samples per group has residual variance $s^2 = 2$ on $d = 2$ degrees of freedom, and a difference of group means of 1.5. Compute the [moderated t-statistic](/moderated-t-statistic/) and its degrees of freedom, and compare with the ordinary t-statistic. What is the moderated variance of a second gene with $s^2 = 0.01$?

13. • Ten genes are ranked, and a gene set holds the genes at ranks 1, 2 and 5. Compute the unweighted ($p = 0$) running sum of [GSEA](/gene-set-enrichment-analysis/) at every rank, and the enrichment score.

14. • Five cells have the 2-nearest-neighbor lists $N(1) = \{2, 3\}$, $N(2) = \{1, 3\}$, $N(3) = \{2, 4\}$, $N(4) = \{3, 5\}$, $N(5) = \{3, 4\}$. List the edges of the graph of [shared nearest neighbor clustering](/shared-nearest-neighbor-clustering/) and their Jaccard weights, with each cell counted in its own set.

15. • Six cells lie at $(0,0)$, $(1,0)$, $(2,0)$, $(3,1)$, $(3,-1)$ and $(2,2)$, numbered 1 to 6. Build the minimum spanning tree as in [MST pseudotime](/mst-pseudotime/), find the backbone, the branch point and the pseudotime of every cell with cell 1 as the root.

16. • Six cells have spliced and unspliced counts $(s, u)$ of one gene: $(0, 0.1)$, $(1, 0.6)$, $(2, 1.2)$, $(4, 1.3)$, $(6, 1.2)$, $(8, 2.0)$. With one cell taken at each end of $s$, fit $\gamma$ as in [RNA velocity](/rna-velocity/) and give the velocity of every cell. Which cells are being induced and which are being repressed?

17. • Three genes have correlations $r_{12} = 0.9$, $r_{13} = 0.6$ and $r_{23} = 0.5$. With soft threshold $\beta = 2$, compute the adjacencies, the connectivities and the three topological overlaps of [WGCNA](/weighted-gene-coexpression-network-analysis/).

18. • In [single-cell RNA sequencing](/single-cell-rna-sequencing/) with Poisson loading, find the mean $\lambda$ of cells per droplet at which 1% of the occupied droplets hold two or more cells. What fraction of the droplets is then empty?

19. • Two transcripts A and B have the same effective length, and every read that fits one fits the other. Show that the likelihood of the EM depends on $\alpha_A$ and $\alpha_B$ only through their sum, and describe the set of maximizers. What does the EM return from a uniform start?

20. • Five gene sets have ORA p-values 0.001, 0.008, 0.039, 0.041 and 0.6. Which sets does the [Benjamini-Hochberg procedure](/benjamini-hochberg-procedure/) reject at $q = 0.05$? Give the five adjusted p-values.

21. ★ Show that the log-likelihood of the EM on equivalence classes, $\sum_e n_e \log \sum_{t \in e} \alpha_t / \ell_t$, is concave on the simplex. Conclude that a fixed point of the EM with every $\alpha_t > 0$ is a global maximum.

22. ★ A splice graph has nodes $1, \ldots, n$ and the edges $(i, i+1)$ and $(i, i+2)$ for every $i$ where they fit. Show that the number of paths from node 1 to node $n$ is the Fibonacci number $F_n$, with $F_1 = F_2 = 1$. What does this say about listing all candidate transcripts?

23. ★ A DAG has nodes $s, a, b, c, d, t$ and edge flows $sa = 16$, $sb = 12$, $ab = 9$, $ac = 7$, $bc = 14$, $bt = 7$, $cd = 5$, $ct = 16$, $dt = 5$. Write the flow as a sum of four weighted $s$-$t$ paths. Then run the greedy rule that takes, each time, a path whose smallest edge flow is largest and subtracts that value. Show that it uses five paths whatever the ties, so the greedy rule of [flow decomposition](/flow-decomposition/) is not optimal.

24. ★ Show that the unweighted ($p = 0$) running sum of GSEA at rank $i$ equals $F_S(i) - F_{\bar S}(i)$, the difference of the empirical distribution functions of the ranks of the set and of the other genes. Conclude that the absolute enrichment score is the two-sample [Kolmogorov-Smirnov](/kolmogorov-smirnov-test/) statistic of the two groups of ranks.

25. ★ With Poisson loading, the fraction of occupied droplets that hold two or more cells is $f(\lambda) = (1 - e^{-\lambda} - \lambda e^{-\lambda})/(1 - e^{-\lambda})$. Show that $f(\lambda) = \lambda/2 - \lambda^2/12 + O(\lambda^3)$.
