## What to remember

- An alignment is scored under a scheme: a substitution score $s(a, b)$ and a gap penalty $g(L)$, linear $dL$ or affine $d + (L - 1)e$. A substitution matrix holds log-odds scores $s(a, b) = \frac{1}{\lambda} \log \frac{q_{ab}}{p_a p_b}$. Every guarantee below holds under the scheme.
- Global, local and semi-global alignment are heaviest paths in the same grid DAG. Needleman-Wunsch, Smith-Waterman and the semi-global program fill $(m + 1)(n + 1)$ cells in $\Theta(mn)$ time and are exact.
- The score alone needs two rows, $\Theta(\min(m, n))$ space; Hirschberg's algorithm recovers the alignment in linear space with about twice the cell work. Gotoh's three tables keep affine gaps at $\Theta(mn)$; a general $g$ costs $O(mn(m + n))$.
- Under the Strong Exponential Time Hypothesis, no algorithm aligns two sequences of length $n$ in $O(n^{2 - \varepsilon})$ time. A band of width $w$ costs $O(wm)$ and is exact only when an optimal path stays inside it.
- For ungapped local scores of random sequences with negative expected score, the number of segment pairs scoring at least $S$ is about Poisson with mean $E = Kmn\,e^{-\lambda S}$, and $P = 1 - e^{-E}$. In bits, $E = mn\,2^{-S'}$. For gapped scores, $\lambda$ and $K$ are fitted by simulation.
- BLAST, FASTA, BLAT, Bowtie, BWA and minimap2 are seed-and-extend heuristics. Each alignment they report has its true score, but they can miss the best one, and their sensitivity is measured, not proved.
- Colinear chaining of $n$ fragments is exact in $\Theta(n \log n)$ time, and alignment to a DAG takes $O((|V| + |E|)m)$ time.
- The exact sum-of-pairs program for $k$ sequences of length $n$ fills $(n + 1)^k$ cells, each the best of $2^k - 1$ moves, and the problem is NP-hard. The center-star alignment is within a factor $2 - 2/k$ of the optimum when the cost is a metric. Progressive, iterative and consistency aligners have no ratio; they are judged on benchmarks.

| Problem or method | Scheme | Time | Space | Guarantee |
|---|---|---|---|---|
| [Needleman-Wunsch](/needleman-wunsch/) | global, linear gaps | $\Theta(mn)$ | $\Theta(mn)$ | exact |
| [Hirschberg's algorithm](/hirschberg-algorithm/) | global, linear gaps | $\Theta(mn)$ | $O(n + \log m)$ | exact |
| [Smith-Waterman](/smith-waterman/) | local | $\Theta(mn)$ | $\Theta(mn)$ | exact |
| [Gotoh's algorithm](/gotoh-algorithm/) | affine gaps, $d \ge e$ | $\Theta(mn)$ | $\Theta(mn)$ | exact |
| [Banded Smith-Waterman](/banded-smith-waterman/) | local, band of $w$ diagonals | $O(wm)$ | $O(wm)$ | exact in the band |
| [BLAST](/blast/) | local, word seeds | $O(wma^w + n + h\min(m, n))$ | $O(a^w + ma^w)$ | heuristic |
| [Colinear chaining](/colinear-chaining/) | weighted fragments | $\Theta(n \log n)$ | $\Theta(n)$ | exact |
| [Sum-of-pairs program](/multiple-sequence-alignment/) | $k$ sequences | $O(2^k n^k)$ column scores | $(n + 1)^k$ cells | exact, NP-hard problem |
| [Center-star method](/center-star-method/) | metric cost | $O(k^2 n^2 + k^3 n)$ | $O(n^2 + k^2 n)$ | ratio $2 - 2/k$ |
| [Progressive alignment](/progressive-alignment/) | guide tree | $O(k^2 n^2)$ plus the tree | | heuristic |

: The main methods of the chapter. Here $m$ and $n$ are the sequence lengths (for Hirschberg, $n$ is the shorter), $a$ the alphabet size, $w$ the band width or BLAST word length, $h$ the number of hits, and $k$ the number of sequences.

## Choosing a method

For two sequences that should match end to end, use Needleman-Wunsch with affine gaps (Gotoh), and Hirschberg or Myers-Miller if the table does not fit in memory. For a shared domain, use Smith-Waterman; for a read against a contig or two overlapping reads, use the semi-global form. If the sequences are known to be close, a band, widened by doubling, saves most of the work.

To search a database, run BLAST or FASTA, and read the E-value, not the raw score, since it accounts for the matrix and the database size. When missing a weak hit matters more than time, run Smith-Waterman on the whole database, which is exact under the scheme. When the query belongs to a known family, search with the family's profile HMM in HMMER; its filters are heuristics too. To place short reads on a genome, use an FM-index mapper such as BWA or Bowtie; for long reads, assembly contigs or whole genomes, use minimap2 or MUMmer, which chain seeds first.

For many sequences, the exact program is practical only for a handful of short ones. For real families use MAFFT, MUSCLE or Clustal Omega, or a consistency method such as T-Coffee or ProbCons for a few sequences. The center-star method is the one to cite when a proved ratio is needed. To search with a family, build a profile HMM from its alignment.
