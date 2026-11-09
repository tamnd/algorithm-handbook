1. $\binom{36}{6} = 1\,947\,792$, $6^6 = 46\,656$ and $6! = 720$. The 4 solutions are $4/720 = 1/180$ of the permutations.

3. One day is $8.64 \times 10^{13}$ steps. Since $16!/2 \approx 1.05 \times 10^{13}$ fits and $17!/2 \approx 1.78 \times 10^{14}$ does not, brute force reaches $n = 17$. Since $35^2 \cdot 2^{35} \approx 4.2 \times 10^{13}$ fits and $36^2 \cdot 2^{36} \approx 8.9 \times 10^{13}$ does not, Held-Karp reaches $n = 35$.

8. The options $AB$, $ACE$ and $AF$ leave the lists of their other items. $B$ loses $AB$, $C$ and $E$ lose $ACE$, and $F$ loses $AF$, so the lengths of $B, C, D, E, F$ become $2, 2, 3, 2, 2$.

10. L2 passes, since $abc$ meets both $a$ and $b$. L3 fails for $c$, which is in the term $abc$ of $f$ and in no term of $g$, and returns $x = \{a, b\}$. Then $f(x) = 0$ because $abc \not\subseteq x$, and $g(\bar{x}) = g(\{c\}) = 0$, so $f(x) = g(\bar{x})$. The dual of $f$ has the terms $a$, $b$ and $c$.

12. There are $\binom{16}{4} = 1820$ candidates and 8 Golomb rulers, 4 up to reflection: $\{0, 1, 4, 10, 12, 17\}$, $\{0, 1, 4, 10, 15, 17\}$, $\{0, 1, 8, 11, 13, 17\}$ and $\{0, 1, 8, 12, 14, 17\}$. The other four are their mirror images $a \mapsto 17 - a$.

13. The cases remove 1 and at least 3 vertices, so $T(n) \le T(n-1) + T(n-3)$, and $\lambda$ is the root of $x^3 = x^2 + 1$, about $1.4656$. Waiting for degree 3 gives $T(n-1) + T(n-4)$ and $\lambda \approx 1.3803$, but then the graphs of maximum degree 2, unions of paths and cycles, must be solved directly, which is easy.

14. All items have 3 options, so the root branches on $A$ with children $AB$, $ACE$, $AF$. Below $AB$, item $C$ has the single option $CDF$, and then $E$ has none. Below $ACE$, item $F$ has no option at once. Below $AF$, item $C$ has only $BC$, and then $D$ has only $DE$, which completes the cover. The tree has 7 nodes, and $\{AF, BC, DE\}$ is the only solution.

17. The triangles at vertex 1 form a fan, and the side of each opposite vertex 1 is a polygon edge or a diagonal. If one of them is a diagonal, flipping it in its quadrilateral gives a diagonal at vertex 1. Each such flip adds one diagonal at vertex 1, so the depth is 3 minus the number of diagonals at vertex 1. The counts at depths 0, 1, 2, 3 are 1, 3, 5, 5, which add up to the 14 triangulations.

18. The identity fixes 63, the quarter turns fix 1 each (the X), the half turn fixes 7 (the X, the two I and the four Z), the reflections in the horizontal and vertical axes fix 7 each, and the diagonal reflections fix 5 each. So there are $(63 + 1 + 1 + 7 + 7 + 7 + 5 + 5)/8 = 12$ free pentominoes and $(63 + 1 + 7 + 1)/4 = 18$ one-sided ones.

19. Closing the walk gives a self-avoiding polygon with 6 edges, the boundary of a $1 \times 2$ rectangle, lying either way. Each of the 2 rectangles can have the origin at any of its 6 corners and be traced in 2 directions, so there are $2 \cdot 6 \cdot 2 = 24$ walks. For 3 steps the unit square gives $4 \cdot 2 = 8$.

20. Split by the first vertex of the set, which is $v_1$ or $v_2$. If it is $v_1$, the rest is any maximal independent set of the path $v_3 \ldots v_n$; if it is $v_2$, the rest is any of the path $v_4 \ldots v_n$. The values for $n = 0, \ldots, 8$ are $1, 1, 2, 2, 3, 4, 5, 7, 9$.

23. The $c_r$ run over all residues, and so do the $r + c_r$, so both sums are $n(n-1)/2$ modulo $n$. But $\sum_r (r + c_r) = \sum_r r + \sum_r c_r = n(n-1) \equiv 0$. For even $n$, $n(n-1)/2 \equiv n/2 \not\equiv 0 \pmod n$.

24. If the copies of $k$ sit at positions $j_k$ and $j_k + k + 1$, the sum of all positions is $2\sum_k j_k + n(n+3)/2$, and it equals $1 + 2 + \cdots + 2n = n(2n+1)$. So $n(3n-1)/2 = 2\sum_k j_k$ must be even, which holds exactly when $n \equiv 0$ or $3 \pmod 4$. For $n = 5$ and $n = 6$ the search must exhaust its tree and finds nothing.

25. $P$ lies in the columns up to some $x$ and $Q$ in the columns from $x + 1$, so they do not overlap, and the two joined cells are neighbors. Every column between the leftmost and rightmost has a cell, so the number of cells in the columns up to $x'$ grows strictly with $x'$, and $P$ is the part up to the column where this number reaches $m$. Then $a(kn) \ge a(n)^k$, so $\lambda \ge a(n)^{1/n}$, and $36\,446^{1/10} \approx 2.86$.

26. Every maximal independent set $I$ meets $N[v]$, or $v$ could be added. If $u$ is the first vertex of $I \cap N[v]$, then $I \setminus \{u\}$ is a maximal independent set of $G - N[u]$, and $I$ is determined by $u$ and this set. Since $|N[u]| \ge d + 1$, induction gives $\mu(G) \le (d+1) 3^{(n-d-1)/3}$, which is at most $3^{n/3}$ because $s \le 3^{s/3}$ for every integer $s \ge 1$, with equality at $s = 3$.

27. A set $S$ with $k$ vertices has at most $3^{k/3}$ maximal independent sets, so the number of pairs is at most $\sum_k \binom{n}{k} 3^{k/3} = (1 + 3^{1/3})^n$ by the binomial theorem. So $c = 1 + 3^{1/3} \approx 2.4422$, which is the bound $O^*(2.4423^n)$ quoted in the entries.
