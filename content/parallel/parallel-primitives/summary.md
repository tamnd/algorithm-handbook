## What to remember

- A combine tree needs an [associative operator](/associative-operator/), and nothing more. [Parallel reduction](/parallel-reduce/) does $n - 1$ combines in span $\lceil \lg n \rceil$, and both numbers are optimal. Floating-point addition is not associative, so a parallel sum can differ from the loop's.
- A shallow scan costs about twice the loop. A prefix circuit of size $s$ and depth $d$ has $s + d \ge 2n - 2$, against $n - 1$ combines for the loop. The [Hillis-Steele scan](/hillis-steele-scan/) has the least depth and $\Theta(n \log n)$ work. The [Blelloch scan](/blelloch-scan/) does $2(m - 1)$ combines in $2\lceil \lg n \rceil$ rounds, where $m = 2^{\lceil \lg n \rceil}$.
- Many problems are scans under the right operator: the carries of an adder, linear recurrences as pairs $(m, c)$, runs of a finite automaton, and segments with the operator $\oplus_s$ of the [segmented scan](/segmented-scan/).
- [Parallel pack](/parallel-pack/) is a flag array, an exclusive scan and a scatter, with $\Theta(n)$ work and $\Theta(\log n)$ span. The output length is $X[n-1] + F[n-1]$, not the last scan value.
- A gather with repeated indices needs concurrent reads, so a CREW PRAM. A scatter with repeated indices needs concurrent writes and a rule to settle them, so a CRCW PRAM. With distinct indices both are one EREW step.
- Fork-join divide and conquer gives span $\Theta(\log^2 n)$ for [parallel merge](/parallel-merge/), and for the matrix product when a temporary matrix holds one half of the sums. Without the temporary the span is $\Theta(n)$.
- [Pointer jumping](/pointer-jumping/) ranks a list in $\lceil \lg n \rceil$ rounds with $\Theta(n \log n)$ work. [List contraction](/list-contraction/) with random mate removes about a quarter of the nodes in each round, which gives $O(n)$ expected work and $O(\log^2 n)$ span.
- [Tree contraction](/tree-contraction/) applies RAKE and COMPRESS in $O(\log n)$ rounds. With linear functions $ax + b$ on the edges it evaluates an expression tree in $O(\log n)$ time and $O(n)$ work on the EREW PRAM.

| Primitive | Work | Span | Notes |
|---|---|---|---|
| [Parallel reduction](/parallel-reduce/) | $n - 1$ | $\lceil \lg n \rceil$ | optimal in both |
| [Hillis-Steele scan](/hillis-steele-scan/) | $nK - 2^K + 1$ | $K$ | least depth |
| [Blelloch scan](/blelloch-scan/) | $2(m - 1)$ | $2K$ rounds | $\Theta(\log^2 n)$ as fork-join loops |
| [Ladner-Fischer](/parallel-prefix/) $P_0$ | at most $4n$ | $K$ | least depth, linear size |
| [Parallel pack](/parallel-pack/) | $2n + 2(m - 1)$ | $2 + 2K$ | flags, scan, scatter |
| [Parallel merge](/parallel-merge/) | $\Theta(n)$ | $\Theta(\log^2 n)$ | not stable |
| [Matrix product](/parallel-matrix-multiplication/), with temporary | $\Theta(n^3)$ | $L^2 + 5L + 1$ | a new temporary in each call |
| Matrix product, no temporary | $\Theta(n^3)$ | $5n - 4$ | in place |
| [Parallel Strassen](/parallel-strassen/) | $(37 \cdot 7^L - 32n^2 - 2)/3$ | $2L^2 + 11L + 1$ | 17 temporaries a level |
| [Pointer jumping](/pointer-jumping/) | $nK - 2^K + 1$ | $K$ | not work-efficient |
| [Parallel list ranking](/parallel-list-ranking/) | $O(n)$ expected | $O(\log^2 n)$ | random mate |
| [Tree contraction](/tree-contraction/) | $O(n)$ expected | $O(\log^2 n)$ w.h.p. | RAKE and COMPRESS |

: Costs of the chapter's primitives on $n$ items or $n \times n$ matrices, with $K = \lceil \lg n \rceil$, $m = 2^K$ and $L = \lg n$ for $n$ a power of 2. Exact counts follow each entry's own cost rules, so compare exact numbers only within a row.

## Choosing a method

For maps and reductions the only real choice is the grain size: give each leaf of the spawn tree a block of items, so that the spawn overhead is small against the work of a leaf.

For scans, count the processors. With about $n$ of them, as in a GPU warp, the Hillis-Steele scan wins, because its extra work is free and its rounds are fewest. With $p$ much smaller than $n$, scan blocks of $n/p$ items serially, scan the $p$ block totals and add them back, in time $O(n/p + \log p)$. On GPUs the [decoupled look-back scan](/decoupled-look-back-scan/) of Chapter 20.4 does one pass over memory. For many short scans, use one [segmented scan](/segmented-scan/).

For merging, P-MERGE is the short program, with span $\Theta(\log^2 n)$. When $p$ is known, cut the output into $p$ pieces by [co-ranks](/merging-sorted-sequences/) and merge each piece serially. This has span $O(n/p + \log n)$ and needs no recursion.

For lists, pointer jumping is simple and fast when $n$ is small or there is one thread per node. For large $n$, random mate contraction does $O(n)$ expected work.

For matrices, the product without a temporary saves memory, the product with a temporary saves span, and parallel Strassen saves work for large matrices over an exact ring.
