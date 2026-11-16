## What to remember

- **Lists and laws.** An index keeps, for each term, the sorted [posting list](/posting-list/) of the documents that contain it. Zipf's law $\mathrm{cf}_i \approx c\,i^{-\alpha}$ and Heaps' law $M \approx k T^b$ are empirical fits whose constants depend on the collection.
- **Intersection bounds.** The merge of lists of lengths $m \le n$ makes at most $m + n - 1$ comparisons, which is optimal when $m = n$. Every comparison method needs $\lceil \log_2 \binom{m+n}{m} \rceil \ge m \log_2(1 + n/m)$ in the worst case. Galloping, the Baeza-Yates method and adaptive intersection stay within constant factors of it.
- **Positions.** A [positional index](/positional-index/) takes $\Theta(T)$ space for $T$ tokens, and a phrase or proximity query of two terms costs $O(m + n + P + z)$ with $P$ positions read and $z$ results.
- **Compression.** Lists are stored as gaps. [Simple-9](/simple-9/) packs them into 32-bit words with 9 layouts. [Partitioned Elias-Fano](/partitioned-elias-fano/) finds its best split for a fixed cost per chunk with an $O(n^2)$ dynamic program. Finding a best document order is NP-hard for the objective of Dhulipala and others, so reordering methods are heuristics with measured gains.
- **Building and updating.** Single-pass in-memory indexing inverts a block in $O(T)$ expected time. [Logarithmic merging](/logarithmic-merging/) writes at most $T \lfloor \log_2(T/n) \rfloor$ postings in its merges, against $\Theta(T^2/n)$ for one auxiliary index, and a query then reads up to $\lfloor \log_2(T/n) \rfloor + 1$ disk indexes.
- **Exhaustive ranking.** [Term-at-a-time evaluation](/term-at-a-time-evaluation/) keeps an accumulator for each matching document; document-at-a-time evaluation keeps $O(m + k)$ state.
- **Safe pruning.** MaxScore, [WAND](/wand/) and block-max WAND return exactly the top $k$ of exhaustive scoring when their score upper bounds are true bounds. Their worst case is no better than DAAT, and their speedups are measured.
- **Unsafe shortcuts.** A tiered index with the approximate stop, an impact-ordered index with a budget of postings, and [static pruning](/static-index-pruning/) can miss documents of the true top $k$. The safe rule of a tiered index stops after tier $j$ only when the $k$-th score is at least $m\tau_j$, for $m$ query terms.

| Method | Task | Cost | Guarantee |
|---|---|---|---|
| [Merge](/merge-based-list-intersection/) | AND of two lists | $\le m + n - 1$ comparisons | exact, optimal for $m = n$ |
| [Skip pointers](/skip-pointers/), spacing $s$ | AND of two lists | $n/s + (2s-1)m$ steps | exact |
| Small versus small | AND of two lists | $2m \log_2(1 + n/m) + 3m$ tests | within 5 of the lower bound |
| [Baeza-Yates](/baeza-yates-intersection/) | AND of two lists | $2m \log_2(2 + n/m) + 6m$ tests | within 10 of the lower bound |
| [Adaptive](/adaptive-set-intersection/), one-sided | AND of two lists | $2m \log_2(1 + n/m) + 6m$ tests | within 8 of the lower bound |
| Logarithmic merging | updates | $T \lfloor \log_2(T/n) \rfloor$ postings written | $\le \lfloor \log_2(T/n) \rfloor + 1$ indexes |
| [Geometric partitioning](/geometric-partitioning/), ratio $r$ | updates | $\le (r-1)(1 + \lfloor \log_r m \rfloor)$ writes per posting | $\le 1 + \lfloor \log_r m \rfloor$ partitions |
| [DAAT](/document-at-a-time-evaluation/) | top $k$ | $O(T(m + \log k))$ | exact |
| [MaxScore](/maxscore/) | top $k$ | $O(T(m \log T + \log k))$ worst case | exact with true bounds |
| WAND, [block-max WAND](/block-max-wand/) | top $k$ | $O(T m \log m)$ worst case | exact with true bounds |
| [Tiered index](/tiered-index/) | top $k$ | $O(T m)$ expected | safe rule exact, quick rule not |
| [Impact-ordered index](/impact-ordered-index/) | top $k$ | $O(S T \log k)$ with the safe stop | safe stop: exact docids and order; budget not |

: Main methods of the chapter. $m \le n$: lengths of two lists (for logarithmic merging, $n$ is the buffer size; for geometric partitioning, $m$ is the number of flushes); $T$: postings of the query lists or of the index; $k$: results; $m$ in the ranking rows: query terms; $S$: segments.

## Choosing a method

For an AND of lists of similar length, merge them. When one list is much shorter, gallop from it into the others, shortest list first. Store gaps with Simple-9 for fast decoding, or with partitioned Elias-Fano when fast skips matter. Build with single-pass in-memory indexing when the dictionary of a block fits in memory, and keep a growing index with logarithmic merging or geometric partitioning, choosing the ratio by the balance of update cost against the number of indexes a query reads.

For ranked queries, use DAAT with WAND or block-max WAND, or MaxScore for long queries, and check that the bounds are true upper bounds of the score. Use tiers, budgets or static pruning only when a measured loss of quality is acceptable.
