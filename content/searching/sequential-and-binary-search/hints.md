1. For $x = 20$: $(lo, hi, mid) = (0, 8, 4)$, then $(0, 4, 2)$, then $(3, 4, 3)$, where $A[3] = 20$, so it returns 3. For $x = 28$: $(0, 8, 4)$, $(5, 8, 6)$, $(5, 6, 5)$, and then $lo = hi = 5$, so it returns NIL. The final $lo = 5$ is the insertion point.

2. $(\ell, u)$ is $(1, 4)$ for 2, $(5, 7)$ for 7, $(5, 5)$ for 6, $(0, 0)$ for 0 and $(8, 8)$ for 10. The difference $u - \ell$ is the number of copies for every key: 3 copies of 2, 2 copies of 7 and none of the others.

3. For $512 \le n \le 1023$, since the worst case is $\lfloor \lg n \rfloor + 1$. For $n = 1000$ it makes 10; for $n = 1024$ it makes 11.

4. The doubling reads $A[0], A[1], A[3], A[7], A[15], A[31]$, all less than $x$, and then $A[63]$, which is not. The binary search gets $[lo, hi] = [32, 63]$, 31 positions, and makes 5 comparisons. With the final equality test the total is $7 + 5 + 1 = 13 = 2\lfloor \lg 37 \rfloor + 3$.

5. On the powers of 2 the probes are at indices 0, 1, 2 and 3: the large last item pulls each guess to the left end, and the range shrinks by one per probe. On the evenly spaced array the first probe is $\lfloor 460 \cdot 99 / 990 \rfloor = 46$, and $A[46] = 470$.

7. The peaks are at indices 2, 4 and 7. The search probes $mid = 4$ (go left, since $5 > 1$), then $mid = 2$ (go left), then $mid = 1$ (go right), and returns 2, a peak that is not the maximum.

9. The slots hold $70, 40, 90, 20, 60, 80, 100, 10, 30, 50$. The walk reads slots 1, 2 and 5 (70, 40, 60) and stops at $k = 11 = 1011_2$. Removing the trailing 1 bits and one more bit leaves $k = 1$, and slot 1 holds 70, the first item not less than 65.

10. Move to front pays $3 + 1 + 3 + 2 + 3 = 12$. The best fixed order puts $c$ first: $c, a, b$ pays $3 \cdot 1 + 3 + 2 = 8$.

13. Because the items are distinct integers, $A[i+1] \ge A[i] + 1$, so $A[i] - i$ is non-decreasing. Find the lower bound of 0 in the sequence $A[i] - i$ and test it. With repeated items, $A[i] - i$ can go down, as in $\langle 1, 1, 1, 3, 5 \rangle$, and the halving loses its meaning.

15. Compare $x$ with $A[mid - 1]$, $A[mid]$ and $A[mid + 1]$. If none is equal and $x < A[mid]$, the key cannot be at an index $k \ge mid + 2$: its sorted rank would be at least $mid + 1$, while the rank of $A[mid]$ is at most $mid + 1$. So keep $[lo, mid - 2]$, or $[mid + 2, hi]$ in the other case.

16. The item at position $i$ is the largest of the first $i$ with probability $1/i$. Add these by linearity of expectation. For $n = 4$, $H_4 = 25/12$.

18. Write increasing values along a snake: all of rows $0, 2, 4, \ldots$, joined by one cell at alternate ends of the odd rows, and 0 everywhere else. No two cells of the snake touch except where they follow each other, so the walk follows the whole snake, about $n^2/2$ cells.

21. Alternate an interpolation probe with a probe at the middle of the range. The middle probes alone halve the range, so the search ends after at most $2(\lfloor \lg n \rfloor + 1)$ probes.

24. Use Yao's principle with the key at a uniform random position: a deterministic algorithm learns only "not here" until it succeeds, so its $k$-th read finds the key with probability $1/n$, and its expected cost is $(n+1)/2$. Reading the items in a uniform random order costs exactly $(n+1)/2$ on every input.

25. Read the middle row, the middle column and the border of the grid, $O(n)$ cells, and take the largest cell $c$ among them. If $c$ is not a local maximum, step to a larger neighbour, which lies in one of the four quarters; that quarter, with its border, holds a local maximum of the whole grid. Recurse on it: $T(n) = T(n/2) + O(n) = O(n)$.

26. Test $P$ at $2^{2^j}$ for $j = 0, 1, 2, \ldots$ until it is true; this costs about $\lg \lg N$ tests. A binary search on the exponent then finds $k = \lfloor \lg N \rfloor$ with about $\lg \lg N$ more tests, and a binary search in $[2^k, 2^{k+1})$ costs $k$ tests.

27. The rank $R$ of $x$ among the keys has the binomial distribution with mean $nx$ and variance $nx(1-x) \le n/4$. The probe lands within $O(1)$ of $nx$, so the scan costs $|R - nx| + O(1)$, and $\mathrm{E}|R - nx| \le \sqrt{\mathrm{Var}\, R} \le \sqrt{n}/2$.

28. Let $\Phi$ be the number of pairs of items that are in different orders in the two lists. If the requested item is at position $k$ in the move-to-front list and $j$ in the fixed list, show that the cost $k$ plus the change of $\Phi$ is at most $2j - 1$. Sum over the requests, using $\Phi \ge 0$ at the end and $\Phi = 0$ at the start.
