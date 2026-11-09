1. The column lengths of the diagram are $5, 4, 3, 3, 1, 1$, so $\lambda' = (5, 4, 3, 3, 1, 1)$. Since $\lambda_3 = 4 \ge 3$ and $\lambda_4 = 2 < 4$, the Durfee square has side 3. The Frobenius coordinates are $(5, 2, 1 \mid 4, 2, 0)$.

3. The order is $(6)$, $(5,1)$, $(4,2)$, $(4,1,1)$, $(3,3)$, $(3,2,1)$, $(3,1,1,1)$, $(2,2,2)$, $(2,2,1,1)$, $(2,1,1,1,1)$, $(1^6)$, so $(3,2,1)$ follows $(3,3)$. The short branch runs from the five partitions that contain a 2, which is $p(4)$.

6. The prefix `(()())(` has one bracket open, so the scan stops at position 8. The result is `(()())()()`.

8. The edges are $\{1, 2\}$, $\{3, 6\}$, $\{4, 2\}$, $\{2, 5\}$, $\{5, 6\}$. A vertex has degree one more than the number of times it appears in the code, so vertex 2 has degree 3.

12. Remove the $d \times d$ square. What is left to its right is a partition with at most $d$ parts, and what is left below it has parts at most $d$. For $d = 3$ the two pieces share the remaining 4 cells, so the count is $\sum_{k=0}^{4} q(k)\,q(4-k)$ with $q = 1, 1, 2, 3, 4$, which is 18. Sides 1 and 2 give 13 and 70, and $13 + 70 + 18 = 101 = p(13)$.

13. The list is in reverse lexicographic order, so count the partitions that come before. Those with first part 6 to 12 number $p(6) + p(5) + \cdots + p(0) = 30$. Among those with first part 5, the rest $(3, 2, 1, 1)$ of 7 is preceded by 5 partitions, then $(2, 1, 1)$ of 4 by 1, then $(1, 1)$ by 1. The rank is 37, and rank 40 is $(5, 2, 2, 1, 1, 1)$.

16. By inclusion and exclusion over the set of singletons, the count is $\sum_j (-1)^j \binom{n}{j} B_{n-j}$. For $n = 6$ this is $203 - 312 + 225 - 100 + 30 - 6 + 1 = 41$, and for $n = 7$ it is 162.

18. The only crossing partition of $[4]$ is $\{1, 3\}, \{2, 4\}$. The crossing partitions are the rest of the $B_n$, so there are $52 - 42 = 10$ for $n = 5$ and $203 - 132 = 71$ for $n = 6$.

22. Take a partition into distinct parts. Let $s$ be its smallest part and $\sigma$ the length of the run of largest parts that drop by one each. If $s \le \sigma$, remove the smallest part and add one cell to each of the $s$ largest parts; otherwise take one cell from each of the $\sigma$ largest parts and make them a new smallest part. This pairs partitions with even and odd numbers of parts, and it fails only when the run meets the smallest part with $s = \sigma$ or $s = \sigma + 1$, which happens exactly at $n = j(3j \mp 1)/2$. The differences are $+1$, $0$ and $-1$ for $n = 7$, 8 and 12. Multiplying $\prod_k (1 - x^k)$ by $\sum p(n) x^n$ gives 1, and this yields $p(n) = \sum_{j \ge 1} (-1)^{j+1}\bigl[p(n - j(3j-1)/2) + p(n - j(3j+1)/2)\bigr]$.

23. Code the tree by the numbers of children of its nodes in preorder. These are $n$ non-negative integers with sum $n - 1$, and by the cycle lemma exactly one of the $n$ rotations of such a sequence codes a tree. A leaf is an entry 0: choose the $k$ zeros in $\binom{n}{k}$ ways and split $n - 1$ into the $n - k$ positive entries in $\binom{n-2}{k-1}$ ways, then divide by $n$. For $n = 7$ the counts are $1, 15, 50, 50, 15, 1$, which add up to $C_6 = 132$.

24. Vertex 1 has degree $k$ when it appears $k - 1$ times in the Prüfer code: choose those positions and fill the other $n - 1 - k$ with the $n - 1$ other labels. For $n = 7$ the counts for $k = 1, \ldots, 6$ are $7776, 6480, 2160, 360, 30, 1$, with sum $7^5$. The average degree is $1 + (n - 2)/n = 2 - 2/n$, which is $12/7$ here, and the leaf fraction $\bigl((n-1)/n\bigr)^{n-2}$ tends to $1/e$.

25. Cut the edge between the two centroids. Each side is a rooted tree with $m$ nodes, and the pair is unordered, so there are $\binom{r_m}{2} + r_m$ trees. For $n = 8$ this is 10 of the 23, and for $n = 6$ it is 3 of the 6. Either centroid could be the root, so the generator must compare the two halves and root at the one with the larger code.

26. A permutation with cycle type $1^5$, $2\,1^3$, $2^2 1$, $3\,1^2$, $3\,2$, $4\,1$ or $5$ has $10, 7, 6, 4, 3, 3$ or $2$ cycles on pairs, and the classes have $1, 10, 15, 20, 20, 30$ and $24$ members. The sum of $2^{\text{cycles}}$ is $1024 + 1280 + 960 + 320 + 160 + 240 + 96 = 4080$, and $4080/120 = 34$.
