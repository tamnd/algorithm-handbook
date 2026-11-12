1. MIN misses 5 times, LRU 7 times and FIFO 6 times. The two online policies part at the sixth request, d: LRU evicts c and FIFO evicts a. FIFO pays for this at once with a miss on a, but afterwards LRU misses on c, b and a, and FIFO only on b.

2. The distances are ∞ ∞ ∞ 2 2 ∞ 2 1 3 3 2 3 2. LRU of size $k$ hits the requests with distance below $k$, so the misses are 13, 12, 7 and 4. At $k = 4$ all four items fit, so every policy misses only on the four first requests.

3. There are $32768/64 = 512$ lines and $512/8 = 64$ sets, so 6 offset bits, 6 index bits and a tag of $48 - 12 = 36$ bits. Since $0\text{x}12345 = 74565 = 1165 \cdot 64 + 5$ and $1165 = 18 \cdot 64 + 13$, the offset is 5, the set is 13 and the tag is $18 = 0\text{x}12$.

5. Direct mapped: 7 misses. Blocks 0 and 4 share set 0 and evict each other. The infinite cache misses 4 times, and so does a fully associative LRU cache of 4 blocks, so there are 4 compulsory, 0 capacity and 3 conflict misses. Two ways: set 0 sees 0 4 0 4 2 0 and misses on 0, 4, 2 and the last 0, set 1 misses once, so 5 misses, with 1 conflict miss.

7. a, b and c miss; c needs 2 units and only 1 is free, so a (value 1) leaves and $L = 1$. The hit on b sets its value to $1 + 3 = 4$. d misses and fits. a misses and needs 2 units: d (value 2) leaves, then c (value 3), and $L = 3$; a gets $3 + 1 = 4$. The values of $L$ are 0, 0, 1, 1, 1, 3, and there are 5 misses.

9. Absolute: $\lambda T/(1 + \lambda T) = 0.95$ gives $T = 0.95/(2 \cdot 0.05) = 9.5$ seconds. Sliding: $1 - e^{-2T} = 0.95$ gives $T = (\ln 20)/2 \approx 1.50$ seconds. Only the absolute TTL bounds the age of a value, by $T$.

10. The factor is $k/(k-h+1) = 8/5$, so LRU has at most $1.6 \cdot 1000 + 8 = 1608$ misses. The factor is below 2 when $k < 2(k - h + 1)$, that is $h < k/2 + 1$, so $h \le 4$.

11. CLOCK misses 9 times and SIEVE 8 times; LRU misses 8 times, FIFO 10 times and MIN 7 times. In SIEVE, a keeps its place near the tail with its bit set, and the hand passes over it and evicts the newer objects. In CLOCK the hand clears a's bit on the request for d and evicts a, because every frame had its bit set.

12. MRU: at each miss it evicts the page requested just before, which comes back after $k - 1$ other requests, all of them hits. So one request in $k$ misses. Random: just after a miss, exactly one page is missing, the one just evicted. It is equally likely to be any of the $k$ pages that come next in the cycle, so the number of requests until the next miss is uniform on $1, \ldots, k$, with mean $(k+1)/2$.

13. Solve the balance equations on the six ordered pairs. The pairs with item 1 as the most recent have probability $1/4$ each, the pairs with item 1 as the least recent have $1/6$ each, and the pairs (2, 3) and (3, 2) have $1/12$ each. LRU hits with probability $17/24$. FIFO hits with probability $7/10$; use Exercise 23. A0 keeps item 1 for good and hits with probability $1/2 + 2 \cdot (1/4)^2/(1/2) = 3/4$.

15. There are 6 misses, as for LRU. At the fifth request b is in $B_1$, so $p$ rises from 0 to 1 and REPLACE evicts a from $T_2$ into $B_2$. At the seventh request a is in $B_2$, so $p$ falls back to 0. At the end $T_2$ = a b, $B_2$ = c, and $T_1$ and $B_1$ are empty.

17. The rule misses 6 times and the optimum 5 times. At the request for c, the rule evicts b, whose next request is furthest; at d it must then evict a, which is needed again soon. The optimum evicts a at once, which frees 3 units in one step, and later hits on b and c.

23. For FIFO, write the balance equation for the queue $(i_1, \ldots, i_k)$: it is entered from any queue $(i_2, \ldots, i_k, j)$ with $j$ outside it, by a request for $i_1$, and from itself by a hit. For random replacement, check detailed balance between $S$ and $S - i + j$.

24. A request for item $i$ misses under the working set policy exactly when $i$ was not among the last $\tau$ requests, which has probability $p_i(1-p_i)^\tau$.

26. For perfect LFU, the priority of an item does not depend on the cache size; apply the argument of the inclusion property entry. For the second part, the cache of size 2 ends with {a, d} and the cache of size 3 with {b, c, d}: in the larger cache a, b and c all reach count 2, and the tie evicts a.
