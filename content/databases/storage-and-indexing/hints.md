1. The clustered index reads about $3 + 10{,}000/100 = 103$ pages, the unclustered one about $3 + 10{,}000 = 10{,}003$, and a full scan $10{,}000$. The unclustered index stops paying when $k$ reaches about $n/p$, a selectivity of about $1/p = 1\%$, which is exactly this query.

3. Ten bitmaps with equality encoding and nine with range encoding, since $R^{9}$ is all ones. Equality reads $E^{3}$ to $E^{6}$, four bitmaps; range encoding reads $R^{6}$ AND NOT $R^{2}$, two. For the column: $E^{3} = 010100$, $R^{0} = 001000$, $R^{2} = 101011$. Equality: $E^{1}$ OR $E^{2} = 100001$ OR $000010 = 100011$; range: $R^{2}$ AND NOT $R^{0} = 101011$ AND $110111 = 100011$. Both give rows 0, 4 and 5.

5. $t = \lfloor 3/4 \cdot 4 \rfloor = 3$, so ten full leaves $[2\,4\,6] \ldots [56\,58\,60]$. $u = \lfloor 3/4 \cdot 5 \rfloor = 3$, so the leaves group as 3, 3, 3, 1; the last group is short and joins the one before it, which gives nodes with 3, 3 and 4 children and the separators $[8, 14]$, $[26, 32]$ and $[44, 50, 56]$. The root has the separators $[20, 38]$. Height 3, 14 nodes.

6. The predictions are $0, 0, 0, 1, 1, 2, 4, 7$, so the differences $i - p$ are $0, 1, 2, 2, 3, 3, 2, 0$, and $e_{lo} = 0$, $e_{hi} = 3$. For 34, $p = 2$ and the window is positions 2 to 5, which holds 34 at position 5. For 40, $p = 3$ and the window is 3 to 6, which holds $13, 21, 34, 55$, so 40 is absent.

7. Sorted: 250 consecutive rows span at most 4 blocks, and the scan reads exactly those. Random: a block is skipped only when all 100 values lie above the range, with probability $0.9975^{100} \approx 0.779$, so about 779 of the 1000 blocks are skipped.

8. The index-only plan reads 2 internal nodes and $10{,}000/250 = 40$ leaves, 42 pages. The other plan reads the same 42 index pages plus, by Yao's formula on 40,000 pages, about 8,868 table pages; the approximation gives $40{,}000(1 - e^{-1/4}) \approx 8{,}848$.

9. Greedy takes $I_1$ first (benefit 30), then $I_2$ or $I_3$ (5 more), for a benefit of 35. The optimum $\{I_2, I_3\}$ has benefit 40. The ratio $35/40 = 0.875$ is above $1 - 1/e \approx 0.632$.

11. The pairs are $(0, 1)$, $(1, 0)$, $(1, 3)$, $(2, 1)$, $(4, 0)$, $(4, 3)$, six in two pages. The rids 0, 1, 2 and 4 of $R$ lie on 3 pages and the rids 0, 1 and 3 of $S$ on 2 pages, so the join costs $2 + 3 + 2 = 7$ I/Os.

12. The first query cracks all 10 entries in three, adding the pivots 5 and 10, and returns $\{5, 7, 9\}$. The second cracks the piece of values below 5 for 3 and the piece $[5, 10)$ for 7, three entries each, 6 in all; it adds 3 and 7 and returns $\{4, 5\}$. The third cracks the piece $[7, 10)$ for 8, two entries, and the piece of values at least 10 for 13, four entries, 6 in all; it adds 8 and 13 and returns $\{9, 10, 11, 12\}$.

13. Each term is $w_q$ times the maximum of a fixed set of numbers, clipped at 0. Adding $i$ raises that maximum by $\max(0, g_i - M)$, where $g_i = c_q - c_{q,i}$ and $M$ is the current maximum. $M$ only grows from $S$ to $T$, so the increase only shrinks. Sums of such terms keep both properties.

14. Run greedy until the first index $j$ that does not fit. The greedy set plus $j$ is at least the optimum of the fractional relaxation, because it takes items in order of ratio, so it is at least the optimum. So either the greedy set or the single index $j$ has at least half of it.

15. Cut the keys into blocks of $2\varepsilon + 1$ consecutive positions. On a block of positions $s, \ldots, s + 2\varepsilon$, the constant function $s + \varepsilon$ is within $\varepsilon$ of every true position. There are $\lceil n/(2\varepsilon + 1) \rceil$ blocks, and the optimal fit uses no more segments than this one.
