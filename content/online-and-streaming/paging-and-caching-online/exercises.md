1. ◦ A cache of $k = 3$ pages starts empty and serves $\sigma = 1\,2\,3\,4\,2\,1\,5\,2\,1\,3$. Count the faults of LRU, FIFO, [Belady's algorithm](/belady-algorithm/) and [flush when full](/flush-when-full/). Split $\sigma$ into [marking phases](/marking-phases/).

2. ◦ Compute the LRU stack distance of every request in $\sigma = 1\,2\,3\,1\,4\,2\,1\,3\,4\,1$, writing $\infty$ for a first request. From the distances alone, give the number of LRU faults for every cache size from 1 to 5. Which property of [stack algorithms](/stack-algorithms/) makes one pass enough?

3. ◦ Take $k = 3$ and $\sigma = 1\,2\,1\,3\,4\,2\,4\,5\,1\,5\,3\,2$. Split $\sigma$ into phases and count the new pages $m_i$ of each phase, that is, the pages not requested in the phase before. What lower bounds on the optimum do the number of phases and $\frac12\sum_i m_i$ give, and what upper bound holds for every [marking algorithm](/marking-algorithm/)? Then compute the faults of the optimum, of flush when full and of LRU.

4. ◦ A list holds $a, b, c, d, e$ in this order, and an access to the item in position $i$ costs $i$. Find the cost of the requests $e, d, e, c, e$ for the static list, for [move-to-front](/move-to-front/) and for the [transposition rule](/transposition-rule/). The offline optimum, which may pay for exchanges, costs 16. What does the best static order cost, and why is that less than the optimum?

5. ◦ For a cache of $k = 6$ pages give: the best ratio of a deterministic online rule; the ratio $2H_k - 1$ of [randomized marking](/randomized-marking/) as an exact fraction; the lower bound $H_k$ for randomized rules against an [oblivious adversary](/oblivious-adversary/); and the best ratio of a randomized rule against an [adaptive adversary](/adaptive-adversary/) that serves the requests offline.

6. ◦ An online cache has $k = 12$ pages and the optimum is given $h = 9$. What ratio does the [Sleator-Tarjan bound](/sleator-tarjan-paging-bound/) give for LRU? What is the largest $h$ for which the ratio is at most 2?

7. ◦ A 4-way set uses [tree PLRU](/plru-replacement/) with the conventions of its entry: three bits in heap order, a bit 0 points to the left, an access sets the bits on its path to point away from it, empty ways fill from the left, and the victim is found by following the bits. The set receives $a, b, c, d, a, e$. Give the bits after each access, and say which block $e$ replaces. Which block would LRU replace? How many bits does an exact LRU order of a 16-way set need, and how many does tree PLRU use? Answer the same for 8 ways.

8. ◦ Show that FIFO is not a marking algorithm: for $k = 3$, find where FIFO evicts a marked page on $\sigma = 1\,2\,3\,4\,2\,5$. Does it follow that FIFO is not $k$-competitive?

9. • For $k = 3$, check that LRU has more faults than FIFO on $\sigma_A = 1\,2\,3\,1\,4\,2\,3$ and fewer on $\sigma_B = 1\,2\,3\,1\,2\,4\,1\,2$. Give the optimum on each sequence. What does the example say about comparing two online rules by their competitive ratios?

10. • A cache of $k = 4$ pages starts empty and serves the cycle $1, 2, 3, 4, 5, 1, 2, \ldots$. Show that for LRU and FIFO each request after the fourth is for the one page of the five that is missing, so the cycle is the sequence of the [deterministic lower bound](/online-caching-lower-bound/). How many faults do LRU, FIFO and flush when full have on the first 20 requests? How many does Belady's rule have? Find a formula for the faults of Belady's rule on the first $n$ requests and check it at $n = 20, 21, 24, 25$.

11. • Randomized marking serves the cycle $1, 2, \ldots, k + 1, 1, 2, \ldots$ with an empty cache at the start. Show that its expected number of faults in each phase after the first is $H_k$. For $k = 3$ and 12 requests, compute the expected number of faults exactly, and compare it with LRU and with the optimum.

12. • For $k = 3$, randomized marking serves $1\,2\,3\,4\,1\,2$ and $1\,2\,3\,1\,2\,4$, both from an empty cache. Compute the expected faults of each exactly. Why does the order of the requests inside the second phase change the answer, and which order does the analysis of the entry take as the worst case?

13. • Requests are drawn uniformly and independently from 6 pages, and the cache holds $k = 5$. Show that every online rule faults with probability $1/6$ on each request after the cache is full. What is the expected length of a marking phase? What ratio between an online rule and the optimum does the [harmonic bound](/harmonic-paging-bound/) give for these numbers, as a fraction and as a decimal?

14. • Run the predictive marker of [learning-augmented marking](/learning-augmented-marking/) with perfect predictions on the sequence of Exercise 3, $k = 3$. Count its faults, compare them with the number of new pages in each phase and with the optimum, and check the bound for perfect predictions.

15. • Run the [Landlord algorithm](/landlord-algorithm/) on unit-size pages with $k = 2$, costs $a = 4$, $b = 1$, $c = 2$, and the requests $(a\,b\,c)^3$. On a hit, reset the credit of the page to its full cost. Give the credits after each request and the total cost. Compare the total with the weighted optimum and with LRU, which pays the cost of each page it loads. What does Landlord cost if a hit leaves the credit unchanged?

16. • A list holds $a, b, c$, and an adversary always requests the last item of the list kept by move-to-front. Write the first 12 requests and the cost of move-to-front. Show that the static order $a, b, c$ costs 24 on these requests, and compare the ratio with the lower bound $2n/(n + 1)$ of the [list update problem](/list-update-problem/).

17. • A list holds $a, b, c, d$, and the requests alternate $d, c, d, c, \ldots$, $m$ of them with $m$ even. Show that the transposition rule pays $4m$. Show that the optimum pays at most $3m/2 + 4$ by moving $d$ and $c$ to the front first. What ratio does this give as $m$ grows, and what does move-to-front pay for $m = 10$?

18. • [Double coverage](/double-coverage/) has servers at 0 and 10 on the line, and the requests are $11, 10, 11, 10, \ldots$. Follow the two servers through the first requests. How much does double coverage pay for the first $2j$ requests while $j \le 10$, and for $m$ requests when $m \ge 21$? What does the optimum pay, and what does the greedy rule that moves the nearest server pay? Check the bound $\mathrm{DC} \le 2\,\mathrm{OPT} + C$ with the constant $C = 10$ given by the distance between the servers.

19. ★ Double coverage on the points $0, 1, 2$ of the line starts with servers at 0 and 1. An adversary always requests the smallest point that has no server. Show that the requests are $2, 1, 0$ repeated, that double coverage pays 4 for each round of three requests, and that the optimum pays 2 for each round in the long run. Conclude that the ratio $k$ of double coverage is tight for $k = 2$.

20. ★ Run the [work function algorithm](/work-function-algorithm/) for $k = 2$ on the points $0, 7, 9$ of the line, with servers at 0 and 7 and the requests $9, 7, 9, 7, \ldots$, 20 in all. At which request does it move the server at 0 for the first time, and what are the two values it compares there? Give its total cost, the optimum and the ratio, and compare the ratio with the bound $2k - 1$.

21. ★ Requests are uniform on $k + 1$ pages. Show that Belady's rule faults exactly once in each marking phase: the page it evicts is the one that starts the next phase. Conclude that every online rule pays $H_k$ times the optimum in the long run. For $k = 2$, give the fault rates of an online rule and of Belady's rule, and check them with a simulation.

22. ★ In [weighted paging](/weighted-paging-problem/), page $a$ costs $M$ and pages $b$ and $c$ cost 1, and $k = 2$. Show that Belady's rule, which ignores the costs, pays $(M + 1)(r + 1)$ on $a\,(b\,c\,b\,c\,a)^r$, while keeping $a$ in the cache costs $M + 4r$. For $M = 10$ and $r = 5$ give both numbers. Show that the ratio of Belady's rule to the optimum is unbounded for fixed $k$.

23. ★ Prove the lower bound $2n/(n + 1)$ for deterministic list update. Let the adversary always request the last item of the online list, and compare the online cost with the average cost of the $n!$ static orders on the same requests. Why may the cost of putting the list in the chosen static order be ignored?
