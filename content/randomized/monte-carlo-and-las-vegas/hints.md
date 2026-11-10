1. The bolt $3$ meets all four nuts and its nut meets the other three bolts: $7$ comparisons. The piles of smaller items, $\{2, 1\}$, cost $2 + 1$ for the pivot $1$ and then $1$ for the pair $2$. The pile of larger items, $\{4\}$, costs $1$. The total is $12$. The expected value is $20 H_4 - 28 = 41/3 \approx 13.67$, and the worst case is $16$.

2. $AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, so $D = C - AB$ has first row $(1, 1)$ and second row zero. For $r = (1, 0)$, $(0, 1)$ and $(1, 1)$ the first entries of $A(Br)$ and $Cr$ are $2$ and $3$, $1$ and $2$, $3$ and $5$, so all three catch the error. Only $r = (0, 0)$ misses, and the error of one round is $1/4$. Five rounds give $4^{-5} = 1/1024$; the general bound needs $10$.

3. $2^{340} \equiv 1 \pmod{341}$, so the Fermat test is fooled. $340 = 2^2 \cdot 85$, and $2^{85} \equiv 32$, $32^2 \equiv 1$: Miller-Rabin says composite, and $\gcd(31, 341) = 31$. Since $341 \equiv 5 \pmod 8$, $\left(\frac{2}{341}\right) = -1$, but $2^{170} \equiv 1$, so Solovay-Strassen says composite too.

5. $x^2 - y^2 = (x - y)(x + y)$ vanishes on the lines $y = x$ and $y = -x$, which share the point $(0, 0)$: $7 + 7 - 1 = 13$ zeros. The bound allows $(2/7) \cdot 49 = 14$.

7. Cut-off $2t = 20$ ms needs $\lceil \ln 10^4 / \ln 2 \rceil = 14$ runs, $280$ ms in all. Cut-off $et \approx 27.18$ ms needs $\lceil \ln 10^4 \rceil = 10$ runs, about $272$ ms. A single run must be cut off at $t/\delta = 10^5$ ms, which is $100$ s.

10. One-sided: $\lceil \ln 1000 / \ln 4 \rceil = 5$, since $4^{-5} = 1/1024$. Two-sided: $\gamma = 1/4$, so $k \ge 8 \ln 1000 \approx 55.3$, and the least odd $k$ is $57$. The exact tail needs only $33$.

12. The pivot has rank $k$, uniform in $\{1, \ldots, m\}$, and the step costs $2m - 1$. So $C(m) = 2m - 1 + \frac{1}{m} \sum_{k=1}^{m} C(k-1)$ with $C(0) = 0$. Subtract the equation for $m - 1$, multiplied by $m - 1$, from the one for $m$, multiplied by $m$: you get $C(m) = C(m-1) + 4 - 3/m$.

13. For the cut $\{d\}$, the first edge must avoid $d$: probability $3/6$. The three vertices left have edges of multiplicity $2$, $2$ and $1$, and the edge to contract must avoid $d$: probability $2/5$. So the answer is $1/5 \ge 1/6$. For a cut into two pairs the first edge must lie inside a pair ($2/6$), and the second must be the other pair's edge ($1/5$): $1/15$. Check that $4/5 + 3/15 = 1$.

19. $1728 = 2^6 \cdot 27$. The chain is $2^{27} \equiv 645$, then $1065$, then $1$. So $1065$ is a nontrivial square root of $1$, and $\gcd(1064, 1729) = 133$, $\gcd(1066, 1729) = 13$. Since $1729 \equiv 1 \pmod 8$, $\left(\frac{2}{1729}\right) = 1$, and $2^{864} \equiv 1$: the base $2$ is an Euler liar.

20. Condition on the first $k$ runs. Two more runs change the majority only when exactly $j$ of the first $k$ are wrong and both new runs are wrong, or exactly $j + 1$ are wrong and both new runs are right. Use $\binom{k}{j} = \binom{k}{j+1}$.

21. Follow the proof of the $\binom{n}{2}$ bound, but stop the contraction at $3$ vertices. A cut of size at most $3\lambda/2$ survives the step from $i$ vertices with probability at least $1 - 3/i$, so it survives to $3$ vertices with probability at least $6/(n(n-1)(n-2))$. Then pick one of the $3$ cuts of the $3$-vertex graph at random.

22. The group of units modulo $p^2$ is cyclic of order $p(p-1)$. The Fermat liars are the solutions of $a^{p^2 - 1} = 1$, and there are $\gcd(p^2 - 1, p(p-1)) = p - 1$ of them. Each is a strong liar, because a cyclic group has only one element of order $2$, namely $-1$. For $25$ the liars are $1, 7, 18, 24$, and the probability is $2/22 = 1/11$.

23. The $k$ vectors span a space of dimension less than $n$, so some nonzero row vector $w$ is orthogonal to all of them. Put $w$ in the first row of $D$. For the given vectors, $w = (1, 1, -1)$.
