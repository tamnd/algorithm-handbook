1. By the [sorted search lower bound](/sorted-search-lower-bound/), $\lceil \lg(n+1) \rceil$: 10, 20, 10 and 11.

2. The maximum needs 99, the maximum and minimum $\lceil 300/2 \rceil - 2 = 148$, and the second largest $100 + 7 - 2 = 105$. Two scans use $99 + 98 = 197$ in both cases.

3. There are $100$ positions and $101$ gaps, so $201$ answers, and $\lceil \lg 201 \rceil = 8$ comparisons.

4. (a) $n$; (b) $n^2$, from the output; (c) a constant, since a search need not read the whole array; (d) $n + m$. The bound for (c) is far from the true $\lceil \lg(n+1) \rceil$. For (b) the gap between $n^2$ and the best known algorithms is open.

5. (a) Match: $\lg n! = n \lg n - O(n)$ and merge sort uses $n \lg n - O(n)$. (b) Match exactly, $n - 1$. (c) No match: the best lower bound is the trivial $\Omega(n^2)$. (d) Match up to a factor of 2: $\frac n2 \lg n$ against $n \lg n$.

6. $\lceil \lg 10! \rceil = \lceil \lg 3{,}628{,}800 \rceil = 22$ bits, against 40.

7. A weighing has three outcomes and there are $n$ answers, so $\lceil \log_3 n \rceil$ weighings: 5 for $n = 100$ and 4 for $n = 81$. Splitting the coins into three nearly equal groups reaches the bound.

8. $\frac{1024}{2} \cdot 10 = 5120$ additions; the FFT uses $1024 \cdot 10 = 10{,}240$.

9. $\frac NB = 2^{19}$ and $\log_{2^{10}} 2^{19} = 1.9$, so about $10^6$ block transfers. Run formation makes $2^9$ sorted runs of $M$ items in one pass, and one merge pass with fan-in up to about $M/B$ merges them: two passes.

10. At least $100 - 5 + 1 = 96$ reads on some text, and at least $\lfloor 100/5 \rfloor = 20$ on every text.

16. Under the uniform distribution on the position of the 1, every deterministic algorithm probes in a fixed order until it finds the 1 or has one position left. Its cost is $\min(r, n - 1)$, where $r$ is uniform on $1, \ldots, n$. Probing in a uniformly random order gives the same cost on every input.

23. Answer "no edge" to a query unless the pairs not yet answered "no" would then leave the graph disconnected; in that case answer "edge". Show that the "edge" answers always form a forest and that the pairs not yet answered "no" always form a connected graph. Before the last query both answers are still possible.

24. In the yes set, $x_i - y_j$ never changes sign on a connected piece. The $(n!)^2$ interleavings $x_{\tau(1)} < y_{\sigma(1)} < x_{\tau(2)} < y_{\sigma(2)} < \cdots$ give pairwise different sign patterns, so the yes set has at least $(n!)^2$ components.

25. A leaf of the comparison tree outputs a fixed rearrangement, which is a heap for exactly $h_n$ of the $n!$ input orders, where $h_n = n!/\prod_v s_v$ is the number of heaps. For $n = 2^k - 1$, bound $\sum_{d=0}^{k-1} 2^d \lg(2^{k-d} - 1)$ by $\sum_{d=0}^{k-1} 2^d (k - d) = 2^{k+1} - k - 2$.

26. If $p_1, \ldots, p_k$ were all the primes, every $m$ would be $\prod p_i^{e_i}$ with each $e_i \le \lg m$. Then $m$ is described by the $k$ exponents in $O(k \log\log m)$ bits, which is less than $\lg m - c$ for large incompressible $m$.

27. Pad each tree to a complete tree of depth $d$. There are at most $n^{2^d - 1} \cdot 2^{2^d} < 2^{2^d(\lg n + 1)}$ such trees, and $2^d(\lg n + 1) \le 2^{n-1}$ for the given $d$.
