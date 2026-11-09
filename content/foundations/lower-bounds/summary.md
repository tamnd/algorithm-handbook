## What to remember

- An [upper bound](/upper-bound/) is about one algorithm; a [lower bound](/lower-bound/) is about every algorithm in a fixed model. An algorithm is [optimal](/optimality/) when its cost matches a lower bound, up to a constant factor or exactly.
- [Counting](/counting-argument/): a decision tree of height $h$ with $k$ answers per node has at most $k^h$ leaves, so a problem with $N$ distinct outcomes needs height $\lceil \log_k N \rceil$. Sorting needs $\lceil \lg n! \rceil = n \lg n - n \lg e + O(\log n)$ comparisons, and searching a sorted array needs $\lceil \lg(n+1) \rceil$.
- Counting fails when there are few outcomes. Element distinctness has two answers, so the count gives 1, yet it needs $\Omega(n \log n)$ comparisons, and by [Ben-Or's theorem](/ben-or-theorem/) $\Omega(n \log n)$ operations of an algebraic computation tree, because its yes inputs form $n!$ connected components.
- An [adversary](/adversary-argument/) answers each query to keep as many inputs alive as possible. Adversaries give the exact bounds $n - 1$ for the [maximum](/max-finding-lower-bound/), $\lceil 3n/2 \rceil - 2$ for the [maximum and minimum](/max-min-lower-bound/) and $n + \lceil \lg n \rceil - 2$ for the [second largest](/second-largest-lower-bound/).
- [Reductions](/reduction-lower-bound/) carry bounds from problem to problem: if $A$ needs $T(n)$, and each input of $A$ can be turned into an input of $B$ of the same size and the answer turned back at cost $r(n)$, then $B$ needs $T(n) - r(n)$ in the same model.
- [Yao's principle](/yao-minimax-principle/): the expected cost of the best randomized algorithm on its worst input is at least the expected cost of the best deterministic algorithm on any chosen input distribution.
- A lower bound holds only in its model. Counting sort beats $\lg n!$ by reading keys as numbers; the cell-probe model, which charges only for memory accesses, gives bounds that hold for every word RAM program.

## Tight bounds in this chapter

| Problem | Model | Lower bound | Matching algorithm |
|---|---|---|---|
| [Maximum](/max-finding-lower-bound/) | comparisons | $n - 1$ | scan |
| [Maximum and minimum](/max-min-lower-bound/) | comparisons | $\lceil 3n/2 \rceil - 2$ | compare in pairs |
| [Second largest](/second-largest-lower-bound/) | comparisons | $n + \lceil \lg n \rceil - 2$ | [tournament](/tournament-method/) |
| [Search in a sorted array](/sorted-search-lower-bound/) | comparisons | $\lceil \lg(n+1) \rceil$ | [binary search](/binary-search/) |
| Sorting | comparisons | $\lceil \lg n! \rceil$ | [merge sort](/merge-sort-optimality/), within $O(n)$ |
| [Element distinctness](/element-distinctness-lower-bound/) | algebraic computation trees | $\Omega(n \log n)$ | sort, then scan |
| [Polynomial of degree $n$](/horners-rule-optimality/) | straight-line programs | $n$ additions, $n$ multiplications | Horner's rule |
| [DFT of order $n$](/fft-lower-bound/) | linear, constants of modulus $\le 1$ | $\frac n2 \lg n$ additions | FFT, $n \lg n$ |
| [External sorting](/external-sorting-lower-bound/) | block transfers | $\Omega(\frac NB \log_{M/B} \frac NB)$ | [external merge sort](/external-merge-sort/) |
| [Partial sums](/dynamic-partial-sums-lower-bound/) | cell probes | $\Omega(\log n)$ per operation | [Fenwick tree](/fenwick-tree/) |
| [Union-find](/union-find-lower-bound/) | cell probes | $\Omega(m\,\alpha(m, n))$ | [disjoint-set forest](/disjoint-set-forest/) |

: Lower bounds of the chapter and the algorithms that meet them. The bounds in the first four rows are exact; the others hold up to a constant factor or, for sorting and the DFT, up to a lower-order term or a factor of 2.

## Proving a lower bound

- Fix the model first: what the algorithm may do, and what is counted. A bound without a model is not a theorem.
- Try the trivial bound and the count of outcomes. They are often enough, and they show what a stronger method must beat.
- If the count is too weak, find a property that every correct run must establish, such as one loss for each key that is not the maximum, and an adversary that makes each query establish as little of it as possible.
- Look for a known hard problem that reduces to yours. Check that the reduction stays inside the model and costs less than the bound.
- For randomized algorithms, choose a hard input distribution and bound deterministic algorithms on it.
