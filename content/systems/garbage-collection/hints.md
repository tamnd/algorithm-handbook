1. Reachable: A, B, C and D. Garbage: E, F and G. E and F point to each other and F points to G, so the counts are E 1, F 1 and G 1. No count can reach zero, so none of the three is ever freed: the cycle of E and F keeps itself and G.

2. Copying costs $cL/(H/2 - L) = 20/30 = 2/3$ and mark-and-sweep $(mL + sH)/(H - L) = 120/80 = 3/2$. Copying costs at most $1/4$ when $H/2 - 20 \ge 80$, so $H \ge 200$, where mark-and-sweep costs $220/180 = 11/9$.

3. The roots copy C to 0 (2 words) and A to 2 (3 words): $\mathit{scan} = 0$, $\mathit{free} = 5$. Scanning C finds A forwarded: 2 and 5. Scanning A copies B to 5 and finds C forwarded: 5 and 7. Scanning B copies D to 7: 7 and 8. Scanning D ends the loop at 8 and 8. E is never copied or visited, and 8 words are copied.

4. $(5 \cdot 600 + 1000)/400 = 10$ and $(3000 + 2000)/1400 = 25/7 \approx 3.57$. Each allocation visits $1/(1 - 0.6) = 2.5$ cells on average, and the 400 allocations visit 1000 cells: the work of the eager sweep, moved out of the pause.

5. B goes to 0, D to 2 and E to 3, so the field of B becomes 3 and the first free word is 6. All three objects move, 6 words in all, and they keep their order. Two-finger compaction needs cells of one size, so that a live cell from the top fits exactly into a hole at the bottom.

6. $S(0) = S(1) = 1$, $S(a) = 0.2$ for $2 \le a \le 99$, and $S(a) = 0$ from 100 on. So $\sigma(10) = (2 + 8 \cdot 0.2)/10 = 0.36$, $\sigma(100) = (2 + 98 \cdot 0.2)/100 = 0.216$ and $\sigma(1000) = 0.0216$. The hazard is $h(0) = 0$, $h(1) = 0.8$, $h(a) = 0$ for $2 \le a \le 98$, and $h(99) = 1$. It rises twice, so the strong form fails.

9. Without resurrection, collection 1 keeps F and G and queues the finalizer, and collection 2 frees both. With resurrection, F and G are reachable through $g$ again. Java runs a finalizer at most once, so the first collection after $g$ is set to nil frees F and G without calling it again.

12. No barrier: after the first store the strong invariant fails and the weak one holds, since gray B still points to C. The second store destroys that path, and C is freed while A points to it. Dijkstra: the store shades C, the strong invariant holds, and C survives. Steele: the store makes A gray again, the strong invariant holds, and the new scan of A finds C. Yuasa: the first store overwrites nil and does nothing, so only the weak invariant holds; the second store shades the old value C, which survives.

14. MARK-GRAY subtracts each internal pointer once: A 0, B 0, C 1, D 0. SCAN colors A and B white. C has count 1, from E, so SCAN-BLACK colors C and D black and adds back the pointers from C and D, which leaves C at 2 and D at 1. COLLECT-WHITE frees A and B. The pointer B → C was subtracted and not added back. That is right: B is gone, and C keeps the pointers from D and E.

16. Here $P(n) = 2 + 0.2(n - 2)$ for $2 \le n \le 100$. For (10, 1): pause 3.6, work 0.36, promotion 0.36, and the 1.6 short-lived objects alive at each collection are promoted, 0.16 per allocation. For (10, 2): pause $P(20) = 5.6$, work 0.56, promotion $(5.6 - 3.6)/10 = 0.2$, and no short-lived object is promoted. For (20, 1): pause 5.6, work 0.28, promotion 0.28, and 0.08 short-lived objects promoted per allocation.

21. Clear the denominators of $2c/(k-2) = (m + sk)/(k-1)$ to get $f(k) = sk^2 + (m - 2s - 2c)k + 2c - 2m = 0$, and evaluate $f(2)$. Since $s > 0$ and $f(2) = -2c < 0$, the parabola has exactly one root above 2, and $f(k) > 0$, which means copying is cheaper, beyond it. Unit costs give $k^2 - 3k = 0$, so $k^* = 3$.

22. Let the rule take regions $1, \ldots, j-1$ in ratio order and stop at region $j$. The [fractional knapsack](/fractional-knapsack/) optimum takes the regions in the same order and a part of region $j$. It bounds the 0-1 optimum and is at most $g_1 + \cdots + g_{j-1} + g_j$. The first part is the greedy set, and $g_j$ is at most the best single region, which fits because $c_j \le B$. On the instance, the rule takes the first region (10), the best single region gives 90, and 90 is the optimum.

24. Show by induction over the steps of the cycle that each object the incremental collector shades was reachable at some moment of the cycle. A root at the rescan is reachable then, and so is the target of a store. When the collector scans $x$ and shades the target $y$ of a field, either $x$ is reachable at that moment, or no store has changed $x$ since it was last reachable, when it already pointed to $y$. An object reachable at some moment of the cycle was live at the start or allocated during the cycle, and the snapshot collector keeps exactly those. Exercise 13 gives a strict case.

25. Each copy halves the copied weight, so $2^k$ reaches 1 after $k$ copies. Without cells, the total weight $W$ is split among the references, each of weight at least 1, so after $W - 1$ copies every weight is 1 and copy $W$ must make a cell. While fewer than $W$ references share the weight $W$, one of them has weight at least 2, so copying a largest one needs no cell before copy $W$.
