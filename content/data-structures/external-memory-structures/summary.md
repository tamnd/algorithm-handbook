## What to remember

- In the **external memory model** the cost is the number of block transfers. Scanning $N$ items costs $\Theta(N/B)$, sorting costs $\mathrm{Sort}(N) = \Theta\big(\frac{N}{B}\log_{M/B}\frac{N}{B}\big)$, and a search by comparisons needs at least $\log_{B+1}(N+1)$ reads.
- An **external stack** with a buffer of $2B$ items makes at most $\lfloor n/B \rfloor$ transfers for $n$ operations, and an **external queue** at most $2\lfloor n/B \rfloor$. After a transfer the buffer is half full, so $B$ operations must pass before the next one.
- A **B-tree** of minimum degree $t$ has between $t - 1$ and $2t - 1$ keys in each node but the root, and height at most $\log_t \frac{n+1}{2}$. With one node per block, search, insert and delete cost $O(\log_B N)$ I/Os, which is optimal for searching.
- A **B+ tree** keeps every key in a leaf and links the leaves, so a range query with $Z$ answers reads at most $h + Z/d + 2$ nodes. Its internal nodes hold only separators, so their fan-out is larger. A **B*-tree** shares keys with a sibling before it splits, and splits two full nodes into three, so every node but the root is at least about two-thirds full.
- **Permuting** costs $\Theta(\min\{N, \mathrm{Sort}(N)\})$ I/Os, even when the permutation is known in advance. Unless blocks hold only a few items, it is as hard as sorting.
- A **buffer tree** collects operations in buffers of size $\Theta(M)$ and pushes them down in batches, for $O\big(\frac{1}{B}\log_{M/B}\frac{N}{B}\big)$ I/Os per operation, amortized. Its answers come late, so it suits batched algorithms. The **external memory priority queue** on it costs the same per insert and delete-min, and **time-forward processing** uses it to evaluate a DAG.
- **Write-optimized** dictionaries delay writes and answer searches at once. The best trade-off between inserts and searches is the one of the **B^ε-tree**, and Brodal and Fagerberg proved that no comparison-based dictionary beats it. The **LSM tree** reaches a similar trade-off with sorted runs that are merged level by level.
- The **van Emde Boas layout** stores a complete binary tree so that every subtree of the recursion is contiguous; a search touches $O(\log_B N)$ blocks for every $B$. The **packed memory array** keeps a sorted array with gaps in $O(\log^2 N)$ moves per update, and the **cache-oblivious B-tree** joins the two.

## The main structures side by side

| Structure | Search | Update, amortized | Notes |
|---|---|---|---|
| [External stack](/external-stack/), [queue](/external-queue/) | none | $O(1/B)$ | at most one I/O per operation in the worst case |
| [B-tree](/b-tree/) | $O(\log_B N)$ | $O(\log_B N)$ | range of $Z$ keys in $O(\log_B N + Z/B)$ |
| [B+ tree](/b-plus-tree/) | $h$ reads | $h$ reads | range of $Z$ keys in at most $h + Z/d + 2$ reads |
| [Buffer tree](/buffer-tree/) | answered at a flush | $O\big(\frac{1}{B}\log_{M/B}\frac{N}{B}\big)$ | batched only |
| [External priority queue](/external-memory-priority-queue/) | delete-min | $O\big(\frac{1}{B}\log_{M/B}\frac{N}{B}\big)$ | insert and delete-min |
| [B^ε-tree](/b-epsilon-tree/) | $O\big(\frac{\log_B N}{\varepsilon}\big)$ | $O\big(\frac{\log_B N}{\varepsilon B^{1-\varepsilon}}\big)$ | $\varepsilon = 1$ is a B-tree |
| [LSM tree](/log-structured-merge-tree/), leveled | $O\big(\log_T \frac{N}{C_0}\big)$ runs | $O\big(\frac{T}{B}\log_T\frac{N}{C_0}\big)$ | space about $1 + 1/T$ times the data |
| [LSM tree](/log-structured-merge-tree/), tiered | $O\big(T\log_T \frac{N}{C_0}\big)$ runs | $O\big(\frac{1}{B}\log_T\frac{N}{C_0}\big)$ | space up to about $T$ times the data |
| [Packed memory array](/packed-memory-array/) | $O(\log (N/B))$ | $O\big(1 + \frac{\log^2 N}{B}\big)$ | $O(\log^2 N)$ moves per update |
| [Cache-oblivious B-tree](/cache-oblivious-b-tree/) | $O(\log_B N)$ | $O\big(\log_B N + \frac{\log^2 N}{B}\big)$ | does not know $B$ |

Costs are block transfers. $h$ is the height and $d$ the order of the B+ tree, $T$ the size ratio and $C_0$ the memtable size of the LSM tree.
