## What to remember

- A [MapReduce](/mapreduce-model/) round costs its communication and its largest reducer input $L$, not only its work. The reducer size $q$ is the largest value list of one key, the replication rate $r$ is the number of pairs emitted per input, and $L \ge q$.
- The [partitioner](/partitioner/) must be a function of the key alone. A hash partitioner stays below $(1 + \varepsilon)P/R$ per task with probability $1 - \delta$ once $P/R \ge 3c_{\max}\ln(R/\delta)/\varepsilon^2$. Split points from a sample of $O(R\log(n/\delta)/\varepsilon^2)$ keys give sorted output, as in [distributed sorting](/distributed-sorting/).
- A [combiner](/combiner/) is safe when the values form a commutative semigroup under the reduce operation and it emits the same type, since it may run any number of times. A mean needs the pair (sum, count); a median has no combiner.
- No partitioner that keeps a key whole gives a reducer less than $\max(N/R, c_{\max})$, so the speedup is at most $N/c_{\max}$. Only splitting the heavy keys, at the price of a second round, goes below $c_{\max}$.
- [Re-execution](/fault-tolerance-by-recomputation/) is correct for deterministic tasks with atomic commits. The completed map tasks of a failed worker run again, because their output is on its local disk; completed reduce tasks do not.
- A [BSP](/bsp-model/) superstep costs $w + gh + L$, and a program $W + gH + SL$. The [h-relation](/h-relation/) charges only the busiest processor, and $V$ words in all need $h \ge V/p$.
- [Pregel](/pregel-model/) is BSP with one process per vertex. Shortest paths run as a synchronous [Bellman-Ford](/bellman-ford/) in $H + 2$ supersteps, $H$ being the most edges on a fewest-edge shortest path to a vertex with an out-edge.
- In one round, a reducer with $q$ inputs covers at most $g(q)$ outputs, so $r \ge q|O|/(g(q)|I|)$: $r \ge b/\log_2 q$ for Hamming distance 1 and $r \ge 2n^2/q$ for matrix multiplication.

| Job or algorithm | Rounds | Communication | Notes |
|---|---|---|---|
| [Word count](/word-count/) | 1 | $N$ pairs; $\sum_i D_i \le \min(N, MV)$ with a combiner | at least $V$ pairs |
| [Distributed sorting](/distributed-sorting/) | 2 | $aR$ sample keys, then $n$ | buckets at most $\lceil (1+\varepsilon)n/R \rceil$ |
| [Reduce-side join](/reduce-side-join/) | 1 | $r + s$ tuples | $L \ge \max_b (\lvert R_b \rvert + \lvert S_b \rvert)$ |
| [Map-side join](/map-side-join/) | 1, map only | $Ms$ | better when $s < r/(M - 1)$ |
| [Shares join](/hypercube-shares-join/), triangle | 1 | $3(rstk)^{1/3}$ | $3rk^{1/3}$ for equal sizes |
| BSP broadcast, one word | 1 or $\lceil \lg p \rceil$ | $(p - 1)g + L$ or $\lceil \lg p \rceil (g + L)$ | tree wins only for small $L$ |
| [Dissemination barrier](/barrier-synchronization/) | $\lceil \lg p \rceil$ | $p\lceil \lg p \rceil$ messages | optimal rounds |
| Pregel shortest paths | $H + 2$ | at most $(H + 1)m$ messages | min combiner is safe |
| [Iterative](/iterative-mapreduce/) PageRank | least $k$ with $2\alpha^k \le \epsilon$ | $n + m$ records per round | 47 rounds for $\alpha = 0.85$, $\epsilon = 10^{-3}$ |
| Sum in [MRC](/mrc-model/), memory $n^{1-\epsilon}$ | $\lceil 1/(1 - \epsilon) \rceil$ | about $n$ numbers | |

: Main jobs and BSP algorithms of the chapter. $M$ and $R$ count map and reduce tasks, $r$, $s$, $t$ are relation sizes and $k$ the reducers of a join.

## Choosing a method

Count the rounds first. An iterative algorithm run as a chain of jobs pays for its whole state in every round; when most of the state does not change, keep it in memory with [resilient distributed datasets](/resilient-distributed-datasets/), or use Pregel, which keeps the graph in place and sends only messages. For graphs with a few vertices of huge degree, the vertex cut of the [gather-apply-scatter model](/gas-model/) spreads one vertex over several machines.

Then look at the shuffle. Use a combiner whenever the reduce operation is associative and commutative, and change the value to a tuple when it is not. For two relations, copy the small one to the map tasks when $s(M - 1) < r$; for three or more, one round of the Shares join replaces a chain of two-way joins.

Then look at the busiest reducer. Under a Zipf law the top key alone can bound the round, and more reducers do not help; a combiner, salting or a skew-aware assignment are the fixes, simplest first. On a machine with known $g$ and $L$, the cost $w + gh + L$ decides between algorithms: when $L$ is large compared with $g$, prefer fewer supersteps even if they send more words.
