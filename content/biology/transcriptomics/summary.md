## What to remember

- **Units within a sample, size factors between samples.** [TPM](/transcripts-per-million/) is FPKM rescaled so that each sample sums to $10^6$. Neither unit corrects for composition. [Median of ratios](/median-of-ratios-normalization/) is exact when more than half of the usable genes are unchanged, and [TMM](/tmm-normalization/) trims 30% at each end of the log ratios and 5% at each end of the mean levels.
- **The EM of isoform quantification has a concave log-likelihood.** A fixed point with every abundance positive is a global maximum. The maximum is not unique when two transcripts receive exactly the same reads.
- **Pseudoalignment returns the set of compatible transcripts, not a position.** On a read whose k-mers are all in the index, the skips along contigs give exactly the intersection of the k-mer colors; otherwise they give a superset.
- **Counting paths is easy; choosing them is hard.** A [splice graph](/splice-graph/) is a DAG, and its paths are counted in $O(|V| + |E|)$ even when they are exponentially many. The fewest paths that hold every fragment are $|F| - |M|$ for a maximum matching $M$. With paired constraints, or with weights to explain, it is NP-hard, so [StringTie-style assembly](/flow-based-transcript-assembly/) is greedy.
- **Counts are overdispersed.** The [negative binomial model](/negative-binomial-count-model/) has variance $\mu + \alpha\mu^2$. DESeq2 and edgeR shrink each dispersion toward a trend, and limma's [moderated t](/moderated-t-statistic/) mixes each variance with a prior. The p-values are only as good as these models.
- **Many tests need a false discovery rate.** [Over-representation analysis](/over-representation-analysis/) uses the hypergeometric upper tail, which treats the list as a random subset. [GSEA](/gene-set-enrichment-analysis/) permutes sample labels and so keeps the correlation between genes. Benjamini-Hochberg controls the FDR under independence or positive dependence.
- **Single cells add counting problems.** The directional UMI method counts between the connected components and the distinct UMIs. With $\lambda$ cells per droplet, about $\lambda/2$ of the occupied droplets hold two or more cells for small $\lambda$.
- **Pseudotime is an order, not a clock.** [MST pseudotime](/mst-pseudotime/) and [diffusion pseudotime](/diffusion-pseudotime/) need a root chosen from biology. [RNA velocity](/rna-velocity/) gives a direction, $u - \gamma s$, under a steady-state model with constant rates.

## The main methods side by side

| Method | Task | Guarantee | Time |
|---|---|---|---|
| [Median of ratios](/median-of-ratios-normalization/) | size factors | exact if more than half the genes are unchanged | $O(nm \log n)$ |
| [TMM](/tmm-normalization/) | size factor against a reference | antisymmetric; exact if all other genes share one ratio | $\Theta(n \log n)$ per sample |
| [EM quantification](/em-isoform-quantification/) | isoform abundances | concave log-likelihood; maximum may not be unique | $O(R + m)$ per round |
| [Pseudoalignment](/pseudoalignment/) | compatible transcripts of a read | exact intersection when all k-mers are indexed | $O(L(k + m))$ per read |
| [Minimum path cover](/minimum-path-cover-transcript-assembly/) | fewest transcripts holding all fragments | optimal, $\lvert F \rvert - \lvert M \rvert$ paths | $O(F^3 + F^2\lambda + (F + n)(n + E))$ |
| [Flow-based assembly](/flow-based-transcript-assembly/) | weighted transcripts | greedy; no optimality | polynomial per round |
| [Moderated t](/moderated-t-statistic/) | differential expression | exact t law on $d_0 + d$ df under the normal model | $\Theta(nm)$ |
| [ORA](/over-representation-analysis/) | gene set overlap | exact tail when the list is a random subset | $O(su)$ |
| [GSEA](/gene-set-enrichment-analysis/) | gene set shift in a ranking | permutation p-value | $\Theta(b(nm + sn\log n))$ |
| [UMI directional](/umi-deduplication/) | molecule counts | exact under its error model | $\Theta(m_b^2 l)$ per bundle |

: Main methods of the chapter. $n$ genes and $m$ samples, except for the EM, where $m$ is the number of transcripts and $R$ the total size of the classes. For pseudoalignment, $L$ is the read length; for path cover, $F$ fragments of at most $\lambda$ nodes in a graph with $n$ nodes and $E$ edges. $s$ gene sets, $u$ genes in the universe, $b$ permutations, $m_b$ distinct UMIs of length $l$.

## Choosing a method

- For abundances within one sample, report TPM from an EM quantifier such as RSEM, kallisto or Salmon. For comparisons between samples, use counts with size factors, never TPM alone.
- For bulk differential expression with few replicates, use a negative binomial GLM with dispersion shrinkage, or limma on log counts with precision weights.
- Use pseudoalignment when the annotation is good and speed matters, and a spliced aligner such as STAR when new junctions are needed.
- Treat the output of any assembler as a set of candidates.
- For gene sets, use ORA on a clear cut list and GSEA when many genes shift a little.
- In single-cell data, deduplicate UMIs, remove doublets, normalize with pooled size factors and select variable genes before clustering. Correct batches only when batch and condition are not confounded.
