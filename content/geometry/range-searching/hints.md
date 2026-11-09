1. The first key $\ge 12$ is $15$ at index $3$, and the first key $> 40$ is $44$ at index $8$. The count is $8 - 3 = 5$, and the keys are $15, 20, 26, 31, 40$.

3. $D(5,5) = 2$, for $(2,3)$ and $(4,1)$. $D(7,6) = 4$, for $(2,3)$, $(4,1)$, $(5,6)$ and $(7,4)$. $D(4,9) = 4$, for $(1,7)$, $(2,3)$, $(3,9)$ and $(4,1)$. $D(10,10) = 10$.

5. Four nodes: $19 = [3,4)$, $5 = [4,8)$, $6 = [8,12)$ and $28 = [12,13)$. The bound $2 \lceil \log_2 10 \rceil = 8$ is far from tight here.

6. Expanding $(x-4)^2 + (y-5)^2 \le 10$ gives $x^2 + y^2 \le 8x + 10y - 31$. The points are $(2,3)$, with $13 \le 15$, $(5,6)$, with $61 \le 69$, and $(7,4)$, with $65 = 65$, which lies on the circle.

8. The terms are $(4/\varepsilon) \log_2(2/\delta) = 40 \log_2 40 \approx 212.9$ and $(8d/\varepsilon) \log_2 (8d/\varepsilon) = 240 \log_2 240 \approx 1897.7$, so $m = 1898$.

11. Each call either finds an empty range, finds a lowest point above $c$, or reports a point and makes two more calls. So the calls form a tree in which the $k$ reporting calls are the internal nodes, each with two children, and such a tree has $2k + 1$ nodes.

12. Follow the pointers: the left child uses positions $\mathrm{left}[s]$ to $\mathrm{left}[t]$, and the right child uses $s - \mathrm{left}[s]$ to $t - \mathrm{left}[t]$. No new binary search is needed.

13. Unroll the recurrence $j$ times: $Q(4^j) = 2(1 + 2 + \dots + 2^{j-1}) + 2^j Q(1)$. At an $x$-split the line enters one child, and at the $y$-split below it enters both, which is where the factor $2$ per two levels comes from.

18. The arrangement has $\binom{1000}{2}$ vertices, and a simplex crossed by at most $100$ lines contains at most $\binom{100}{2}$ of them in its interior. Divide.

20. Below the split node, the left part of the range takes at most one canonical node per level, and only from the level of the split node's grandchildren down to the leaves, unless it is a whole child; the right part is the same. With the split node at the root, each part has the levels $2$ to $k$ available.

21. Five consecutive points always contain a multiple of $5$, so $\{5, 10, 15, 20\}$ is a net. The four disjoint intervals $[1,5]$, $[6,10]$, $[11,15]$, $[16,20]$ are all heavy and need four different points.

22. If the line through $u$ and $v$ has five points strictly on one side, a halfplane slightly shifted from it holds those five and misses $u$ and $v$. So the line must leave at most four points strictly on each side. Eight pairs pass this test; test the other heavy halfplanes, whose boundaries can be taken through two points of $P'$, against them.

23. The $i$-th insertion builds a block of size $2^{z}$, where $z$ is the number of trailing zero bits of $i$. Group the insertions by $z$: for $z < k$ there are $n / 2^{z+1}$ of them.

24. Take logarithms in $V(n) = (3\sqrt{r})^{\log_r n}$. The extra $\log_r 3$ above $1/2$ shrinks only slowly as $r$ grows, which is why Matoušek lets $r$ grow with $n$.
