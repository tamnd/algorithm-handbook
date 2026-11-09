## What to remember

- In the [external memory model](/external-memory-model/) the cost is the number of block transfers. With $n = N/B$ and $m = M/B$, sorting takes $\Theta(n \log_m n)$ transfers, that is, $\Theta(\log_m n)$ passes over the data. Because $m$ is large, real files need one or two merge passes.
- **External merge sort** makes $\lceil N/M \rceil$ [runs](/sorted-run/) of $M$ items, then merges $k = m - 1$ runs at a time. It does at most $2n\big(1 + \lceil \log_{m-1} \lceil N/M \rceil \rceil\big)$ transfers, which meets the [lower bound](/external-sorting-io-lower-bound/) up to a constant factor.
- A [k-way merge](/k-way-merge/) with a heap takes $O(k + n \log k)$ time; a tree of losers needs only $\lceil \lg k \rceil$ comparisons per item. Merging the runs one after the other instead costs $\Theta(nk)$.
- The number of passes is $\lceil \log_k r \rceil$ for $r$ runs. [Replacement selection](/replacement-selection/) with a heap of $P$ items makes $\frac{n}{2P} < \mathbb{E}[R_n] < \frac{n}{2P} + 2$ runs on random input, never more than $\lceil n/P \rceil$, and one run on sorted input. Halving the number of runs saves at most one pass.
- **Memory for buffers comes out of the fan-in.** [Double buffering](/double-buffering/) gives each run two blocks and lowers the fan-in to about $m/2$. [Disk striping](/disk-striping/) on $D$ disks lowers it to $m/D - 1$, which costs a factor of about $\log m / \log(m/D)$: at most 2 when $D \le \sqrt m$, but $\Theta(\log m)$ when $D$ is a constant fraction of $m$.
- **On tapes**, the [balanced merge](/balanced-merge-sort/) merges $\lfloor T/2 \rfloor$ ways; the [polyphase](/polyphase-merge-sort/) and [cascade](/cascade-merge-sort/) merges merge $T - 1$ ways from uneven *perfect distributions* padded with dummy runs. Polyphase moves the least data on fewer than about 8 tapes.
- **Distribution meets the same bound.** [External samplesort](/external-samplesort/) splits by sampled splitters into up to $m/2$ buckets, with $O(n \log_m n)$ expected transfers. [Balance Sort](/balance-sort/) reaches $O\big(\frac nD \log_m n\big)$ on $D$ independent disks.
- [Funnelsort](/funnelsort/) meets the bound without knowing $M$ or $B$, under the tall-cache assumption $M = \Omega(B^2)$.

## The main methods side by side

| Method | Setting | Merge order or buckets | Cost | Stable |
|---|---|---|---|---|
| [External merge sort](/external-merge-sort/) | one disk | $m - 1$ | $2n\big(1 + \lceil \log_{m-1} \lceil N/M \rceil \rceil\big)$ transfers | yes |
| [External samplesort](/external-samplesort/) | one disk | up to $m/2$ buckets | $O(n \log_m n)$ expected transfers | yes |
| [Funnelsort](/funnelsort/) | cache-oblivious | $\lceil N^{1/3} \rceil$ parts | $O(1 + n \log_m n)$ misses, tall cache | yes |
| Striped merge sort | $D$ disks | $m/D - 1$ | $\Theta\big(\frac nD \log_{m/D} \frac nD\big)$ parallel transfers | yes |
| [Balance Sort](/balance-sort/) | $D$ disks | up to $m - 2D$ buckets | $O\big(\frac nD \log_m n\big)$ parallel transfers | yes |
| [Balanced merge sort](/balanced-merge-sort/) | $T \ge 4$ tapes | $\lfloor T/2 \rfloor$ | $\lceil \log_{\lfloor T/2 \rfloor} S \rceil$ merge passes | yes |
| [Polyphase merge sort](/polyphase-merge-sort/) | $T \ge 3$ tapes | $T - 1$ | merges move $6.92N$ items for $S = 1000$, $T = 4$ | no |
| [Cascade merge sort](/cascade-merge-sort/) | $T \ge 3$ tapes | $T - 1$ down to 2 | merges move $7.93N$ items for $S = 1000$, $T = 4$ | no |
| [Oscillating sort](/oscillating-sort/) | tapes that read backward | $T - 2$ | $\lceil \log_{T-2} S \rceil$ merge passes, no rewinds | no |

: The main external sorts. Here $n = N/B$, $m = M/B$, and $S$ is the number of initial runs. For $S = 1000$ on 4 tapes, the balanced merge needs 10 merge passes and so moves $10N$ items in its merges, against $6.92N$ for polyphase and $7.93N$ for cascade.

## Choosing a method

- On one disk, use external merge sort with the largest fan-in memory allows, and replacement selection when the input may be partly sorted or arrives as a stream.
- Add double buffers only if the smaller fan-in does not add a pass.
- With $D \le \sqrt m$ disks, striping is close to optimal. With more, drive each disk on its own, as Balance Sort does.
- When the buckets are useful by themselves, or many keys are equal, use a distribution sort.
- Sorting keys and then gathering large records pays only when a block holds very few records; see [external permuting](/external-permuting/).
