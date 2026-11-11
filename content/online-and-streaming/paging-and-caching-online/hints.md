1. LRU has 7 faults, FIFO 8, Belady's algorithm 6 and flush when full 10. The phases are $[1\,2\,3]$, $[4\,2\,1]$, $[5\,2\,1]$ and $[3]$.

3. The phases are $[1\,2\,1\,3]$, $[4\,2\,4\,5]$, $[1\,5\,3]$ and $[2]$, with $m_i = 3, 2, 2, 1$. Four phases from an empty cache give $\mathrm{OPT} \ge 4$, and $\frac12 \sum m_i = 4$ gives the same. A marking algorithm has at most $kN = 12$ faults. In fact the optimum has 6, flush when full 10 and LRU 9.

4. The static list costs 22, move-to-front 19 and transpose 22. The best static order puts $e$ first, $d$ second and $c$ third and costs 8. That cost leaves out the exchanges that turn $a, b, c, d, e$ into the new order; the optimum of 16 has to pay for them.

7. The bits are $110$, $100$, $001$, $000$, and after the hit on $a$ they are $110$ again. The victim path goes right at the root and left below it, so $e$ replaces $c$ in way 2. LRU would replace $b$. An exact order of 16 ways needs $\lceil \log_2 16! \rceil = 45$ bits against 15 for tree PLRU; for 8 ways the numbers are 16 and 7.

11. On the cycle each phase after the first has one new page, and it is the first request of the phase. The bound $m(1 + H_k - H_m)$ is exact when the new pages come first, and with $m = 1$ it is $H_k$. For $k = 3$ the 12 requests make a first phase of 3 faults and three more phases, so the expectation is $3 + 3 \cdot \frac{11}{6} = 17/2$. LRU faults 12 times and the optimum 6 times.

13. Five of the six pages are in the cache, and the next request is independent of them. A phase ends just before the sixth distinct page, so its expected length is $6H_6 - 1 = 6H_5 = 13.7$ by the coupon collector argument. The ratio is $H_5 = 137/60 \approx 2.283$.

15. With full resets the credits after each request are $a{:}4$; $a{:}4, b{:}1$; $a{:}3, c{:}2$; $a{:}4, c{:}2$; $a{:}2, b{:}1$; $a{:}1, c{:}2$; and then the last three repeat. The total is 13. The optimum is 11, LRU pays 21, and Landlord with no change on a hit pays 17.

19. From servers at 0 and 1, the request at 2 moves the right server (cost 1). The request at 1 lies between the servers, so both move one step (cost 2). The request at 0 moves one of the two servers at 1 (cost 1), and the servers are back at 0 and 1. The optimum keeps one server at 0 and moves the other between 1 and 2.

20. The server at 7 moves to 9 and back, at a cost of 2 each time, until the eighth request, which asks for 7 while the servers are at 0 and 9. Moving the server at 0 gives the value 16, and moving the server at 9 gives 18, so the server at 0 moves. The total is $7 \cdot 2 + 7 = 21$. The optimum moves the server at 0 to 9 at once and pays 9, so the ratio is $7/3$.

21. After a fault Belady's rule evicts the page whose next request is latest. Until that request only the other $k$ pages are asked for, and they are in the cache. The online rate is $1/(k + 1)$ and the optimum has one fault per phase of expected length $(k + 1)H_k$. For $k = 2$ the rates are $1/3$ and $2/9$.

22. At the first $c$, page $b$ comes back sooner than $a$, so Belady's rule evicts $a$; at each $a$ it evicts $c$, and at the next $c$ it evicts $a$ again. Every block after the first costs $M + 1$. Keeping $a$ leaves one slot to $b$ and $c$, which fault four times in each block. For $M = 10$ and $r = 5$ the costs are 66 and 30; for large $r$ the ratio is at least about $(M + 1)/4$.

23. The online list pays $n$ for each of $m$ requests. Averaged over the $n!$ orders, each request costs $(n + 1)/2$, so some static order costs at most $m(n + 1)/2$. Putting the list in that order costs at most $n(n - 1)/2$, which does not grow with $m$.
