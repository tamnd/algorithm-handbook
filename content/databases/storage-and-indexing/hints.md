1. LRU misses 10 times: only the two hits on 1 and 2 after page 5 arrives. CLOCK misses 9 times; it also hits the last request, for page 5. Both end with pages 3, 4 and 5, CLOCK in frames holding 5, 3, 4. On this sequence CLOCK beats LRU, the reverse of the example in the entry, so neither policy is always better.

2. $T^* = (128/200)(50/0.004) = 0.64 \cdot 12{,}500 = 8000$ seconds, a little over two hours. A page read once an hour, every 3600 seconds, is read more often than that, so it stays. With 64 KB pages $K = 16$ and $T^* = 1000$ seconds. Halving the price of memory doubles $T^*$.

3. Records are 32 bytes, so an N-ary page holds $\lfloor 8188/36 \rfloor = 227$ records and every scan reads $\lceil 10^6/227 \rceil = 4406$ pages. A column page holds 1023 values, so one attribute takes 978 pages, two take 1956 and all four 3912. One record costs 1 page in the N-ary layout and 4 in the column layout. PAX reads the same pages as the N-ary layout.

6. The clustered index reads about $3 + 10{,}000/100 = 103$ pages, the unclustered one about $3 + 10{,}000 = 10{,}003$, and a full scan $10{,}000$. The unclustered index stops paying when $k$ reaches about $n/p$, a selectivity of about $1/p = 1\%$, which is exactly this query.

8. $t = \lfloor 3/4 \cdot 4 \rfloor = 3$, so ten full leaves $[2\,4\,6] \ldots [56\,58\,60]$. $u = \lfloor 3/4 \cdot 5 \rfloor = 3$, so the leaves group as 3, 3, 3, 1; the last group is short and joins the one before it, which gives nodes with 3, 3 and 4 children and the separators $[8, 14]$, $[26, 32]$ and $[44, 50, 56]$. The root has the separators $[20, 38]$. Height 3, 14 nodes.

9. Ten bitmaps with equality encoding and nine with range encoding, since $R^{9}$ is all ones. Equality reads $E^{3}$ to $E^{6}$, four bitmaps; range encoding reads $R^{6}$ AND NOT $R^{2}$, two. For the column: $E^{3} = 010100$, $R^{0} = 001000$, $R^{2} = 101011$. Equality: $E^{1}$ OR $E^{2} = 100001$ OR $000010 = 100011$; range: $R^{2}$ AND NOT $R^{0} = 101011$ AND $110111 = 100011$. Both give rows 0, 4 and 5.

11. The header takes 4 bytes. After the inserts the slots are $(80, 20)$, $(65, 15)$, $(35, 30)$, $(27, 8)$, with $n = 4$, $e = 27$ and a gap of $27 - 20 = 7$. Deleting slot 1 marks it $(0, 0)$ and raises the free space to 22, but not the gap. Deleting slot 3 removes the trailing slot, so $n = 3$, the gap is 11 and the free space 34. E reuses slot 1 but does not fit in the gap, so the page is compacted first: A stays at 80, C moves to 50, and E goes to $(25, 25)$, leaving 9 bytes. F needs 10 bytes and a new slot, 14 in all, so the page is full.

12. The sizes are 9, 4, 13 and 2. $Q_1$ starts (9), and $Q_2$ starts ($9 + 4 = 13$). $Q_3$ would bring the sum to 26, so it waits, and $Q_4$ waits behind it. When $Q_1$ ends, $4 + 13 = 17$ admits $Q_3$, and then $17 + 2 = 19$ admits $Q_4$.

13. The index-only plan reads 2 internal nodes and $10{,}000/250 = 40$ leaves, 42 pages. The other plan reads the same 42 index pages plus, by Yao's formula on 40,000 pages, about 8,868 table pages; the approximation gives $40{,}000(1 - e^{-1/4}) \approx 8{,}848$.

15. The fifth insert splits the root leaf into $\{10, 30\}$ and $\{40, 70, 90\}$. Then 20 goes left, 60 goes right, and 50 goes right and splits it into $\{40, 50\}$ and $\{60, 70, 90\}$. For 33 the penalties are 3, 7 and 27, so it goes left. The root keys end as $[10, 33]$, $[40, 50]$, $[60, 90]$. The search reads the root and the first two leaves and returns 33 and 40.

19. $X$ is 0xC0000003, 0x80000001, 0x0000001F, 0x7E000000, and $Y$ is 0x80000002, 0xC0000004. The AND is 0x80000002, 0xC0000001, 0x80000001, 0x0000001F, 0x7E000000, found in 5 steps, which meets the bound $4 + 2 - 1 = 5$. The OR is the single fill 0xC0000006.

21. The first query cracks all 10 entries in three, adding the pivots 5 and 10, and returns $\{5, 7, 9\}$. The second cracks the piece of values below 5 for 3 and the piece $[5, 10)$ for 7, three entries each, 6 in all; it adds 3 and 7 and returns $\{4, 5\}$. The third cracks the piece $[7, 10)$ for 8, two entries, and the piece of values at least 10 for 13, four entries, 6 in all; it adds 8 and 13 and returns $\{9, 10, 11, 12\}$.

22. The runs are $[2, 5, 9, 14]$, $[1, 7, 11, 12]$, $[4, 10]$. The first query moves 5, 7, 9; the second moves only 4, since $[5, 7)$ is already in the final partition, and returns 4, 5; the third moves 10, 11, 12 and returns 9, 10, 11, 12. That is 7 keys moved against 22 entries touched by cracking, but adaptive merging also sorted all 10 values at the first query.

23. The first segment takes $2, \ldots, 34$, since no line fits the first eight keys, up to 55, within 1; the second takes 55, 89, 144. Two segments, against the bound $\lceil 10/3 \rceil = 4$. The line $y = (43/231)x + 93/154$ has errors at most 1 on the first seven keys. With $\varepsilon = 2$ one segment suffices.

25. Memory beats flash when $r < \varphi + a_f/T$, that is $T < a_f/(r - \varphi)$, and flash beats disk when $T < (a_d - a_f)/\varphi$. Flash has an interval of its own when the first bound is less than the second; clear the denominators. Here memory wins below about 263 seconds, flash up to 1,245,000 seconds (about 14 days), and disk beyond. Without flash the break-even is $a_d/r = 62{,}500$ seconds.

26. The expected cost per row is $\sum_i c_{\pi(i)} \prod_{j < i} s_{\pi(j)}$. Swap two adjacent predicates $a, b$: only their two terms change, and $a$ first is better exactly when $c_a + s_a c_b \le c_b + s_b c_a$. The ratios are 2, 40/9 and 5, so the order is integer, string, date, at 3.05 per row; string first costs 4.15.

27. After $k$ midpoint insertions every free interval has at least $2^{w-k} - 1$ codes. For the lower bound, let the adversary always put the next value in the smaller of the two free intervals the last code created; it has at most half of the free codes, rounded down, so after $w$ values it is empty.

28. Each term is $w_q$ times the maximum of a fixed set of numbers, clipped at 0. Adding $i$ raises that maximum by $\max(0, g_i - M)$, where $g_i = c_q - c_{q,i}$ and $M$ is the current maximum. $M$ only grows from $S$ to $T$, so the increase only shrinks. Sums of such terms keep both properties.

29. Run greedy until the first index $j$ that does not fit. The greedy set plus $j$ is at least the optimum of the fractional relaxation, because it takes items in order of ratio, so it is at least the optimum. So either the greedy set or the single index $j$ has at least half of it.
