## What to remember

- In the paging problem a cache of $k$ pages pays 1 for each fault. An online rule is $c$-competitive if $\mathrm{ALG}(\sigma) \le c \cdot \mathrm{OPT}(\sigma) + b$ for every sequence $\sigma$. Demand paging loses nothing.
- **Belady's rule** evicts the page whose next request is furthest away. It is optimal offline and runs in $O(n \log k)$ time with an indexed heap. With pages of different costs it is no longer optimal.
- **No deterministic rule beats $k$.** An adversary on $k + 1$ pages requests the page just evicted: the online rule faults on every request, and the optimum at most once in $k$ requests.
- **Every marking algorithm is $k$-competitive.** A marking rule never evicts a page requested in the current phase of $k$ distinct pages, so it has at most $k$ faults per phase, and the optimum has at least one. LRU and flush when full are marking rules; FIFO is not, but it is conservative and also $k$-competitive. Against an optimum with $h \le k$ pages, the ratio is $k/(k - h + 1)$.
- **Randomness gives a logarithm.** Randomized marking is $2H_k$-competitive against an oblivious adversary, with exact ratio $2H_k - 1$. No randomized rule beats $H_k$, and Partition and Equitable reach it. Here $\ln(k + 1) < H_k \le 1 + \ln k$. Against an adaptive offline adversary, randomness does not help: the bound is $k$ again.
- **LFU and MRU are not competitive**, and neither is tree PLRU with 4 ways.
- **Move-to-front is 2-competitive** for list update: $\mathrm{MTF}(\sigma) \le 2\,\mathrm{OPT}(\sigma) - m$ for $m$ requests, by a potential that counts inversions. No deterministic rule beats $2n/(n + 1)$. Transpose is not competitive.
- **The $k$-server problem** has a lower bound $k$ on every metric with more than $k$ points. Double coverage is $k$-competitive on the line and on trees, and the work function algorithm is $(2k - 1)$-competitive on every metric. Whether $k$ is always possible is open; the randomized version of the conjecture is false.
- **Weighted paging** is $k$-server on a star. GreedyDual and Landlord are $k$-competitive, and randomized rules reach $O(\log k)$.

## The rules side by side

| Rule | Problem | Competitive ratio | Notes |
|---|---|---|---|
| [Belady's rule](/belady-algorithm/) | paging, offline | 1 | needs the future; a stack algorithm |
| LRU | paging | $k$ | marking, conservative, stack algorithm |
| FIFO | paging | $k$ | conservative, not marking; Belady's anomaly |
| [Flush when full](/flush-when-full/) | paging | $k$ | marking, not demand paging |
| [Randomized marking](/randomized-marking/) | paging | $2H_k - 1$ | oblivious adversary; $k$ on every run |
| Partition, Equitable | paging | $H_k$ | optimal for randomized rules |
| LFU, MRU, [tree PLRU](/plru-replacement/) with 4 ways | paging | unbounded | |
| [Move-to-front](/move-to-front/) | list update | $2 - 1/n$ | within 2 of the best static order too |
| [Transpose](/transposition-rule/) | list update | unbounded | ratio about $2n/3$ on two alternating items |
| [Double coverage](/double-coverage/) | $k$-server on lines and trees | $k$ | not lazy; $O(\log k)$ time per request on the line |
| [Work function algorithm](/work-function-algorithm/) | $k$-server, any metric | at most $2k - 1$ | $k$ on the line, on $k + 1$ points and for $k = 2$ |
| [Landlord](/landlord-algorithm/) | file caching | $k$ | GreedyDual for unit sizes, LRU for unit costs |

: Online rules of this chapter. Ratios are against an optimum with the same cache, and against an oblivious adversary for the randomized rules; $n$ is the length of the list and $k$ the size of the cache or the number of servers.

## Choosing a rule

- To judge a rule on a trace, compare it with Belady's rule on the same trace. One pass of LRU stack distances gives the LRU fault counts for every cache size at once.
- For a general-purpose cache, use LRU or a cheap approximation of it. Its worst case is $k$, but every marking rule shares that bound, and a larger cache helps quickly: with twice the pages of the optimum, the ratio is below 2.
- If an adversary could choose the requests, use randomized marking; its expected ratio grows like $\ln k$.
- If scans of pages that are used once are common, as in a database buffer, filter them with 2Q or a similar rule before the main LRU list.
- If pages differ in fetch cost or size, use Landlord or GreedyDual-Size, not a rule that counts faults.
- For a self-organizing list, use move-to-front; avoid transpose when an adversary or a bad access pattern is possible.
