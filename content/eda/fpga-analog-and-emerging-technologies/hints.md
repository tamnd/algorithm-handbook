1. The channels form 9 rows and 9 columns of 8 pieces each, so there are $144 \cdot 30 = 4320$ segments. Of the 81 switch blocks, 49 are inside the array with $6W$ switches, 28 are on an edge with three sides and $3W$, and 4 are corners with two sides and $W$. That gives $382W = 11460$ switches. A full crossbar inside the array has $6W^2 = 5400$ switches, against $6W = 180$.

2. The four nets form the 4-cycle $T - R - B - L - T$ on the sides. An even cycle has an edge coloring with 2 colors, so the tracks 0, 1, 0, 1 in this order route it. The three nets $TL$, $LB$, $BT$ form a triangle, which needs 3 colors, so no routing exists with $W = 2$, although no side has more than 2 nets.

3. The cut gives $W_{min} \ge \lceil 33/4 \rceil = 9$. The success at 12 gives $W_{min} \le 12$. The failure of a heuristic router at 11 proves nothing, so $9 \le W_{min} \le 12$ is all that follows. An exact router that fails at 11 proves that 11 is not routable, but the predicate need not be monotone in $W$, so 9 and 10 still have to be tried.

4. $L$ tables of $K$ inputs, joined in a tree, have at most $LK - (L - 1)$ inputs from outside, so $L \ge \lceil (10 - 1)/(4 - 1) \rceil = 3$. Two tables take 4 inputs each, and the third takes their two outputs and the last 2 inputs.

5. $WL = 1$ µm², so $\sigma = 4$ mV. For 1 mV, $WL = 16$ µm². With $W$ doubled, $\sigma = 4/\sqrt{2} \approx 2.83$ mV.

6. In the row, the positions are 1 to 6 with mean 3.5, so the positions of A would have to sum to $10.5$, which is not an integer. In the $2 \times 3$ array, the row coordinates of A would have to sum to $3 \cdot 1.5 = 4.5$. In the $2 \times 4$ array the sums are $4 \cdot 2.5 = 10$ and $4 \cdot 1.5 = 6$, and ABBA over BAAB is a solution.

7. NCT: 4 NOT, $4 \cdot 3 = 12$ CNOT and $4 \cdot \binom{3}{2} = 12$ Toffoli gates, 28 in all. MCT: each of the 4 targets with any of the $2^3$ sets of controls, $4 \cdot 2^{3} = 32$. A gate flips at most one bit of the value that started as 0, and $0$ and $15$ differ in 4 bits, so at least 4 gates.

8. Running the circuit without SWAPs needs $a$ to be adjacent to $b$, $c$ and $d$, but a vertex of the line has at most 2 neighbors. Put $b, a, c, d$ on $q_0, \ldots, q_3$, run the first two CNOTs, SWAP $q_1$ and $q_2$, which puts $a$ next to $d$, and run the third.

9. Tridiagonal of order 5: $F_6 = 8$ terms and $3 \cdot 5 - 2 = 13$ vertices. Dense: 24 terms and $4 \cdot 2^3 = 32$ vertices, 120 and 80, 720 and 192. The DDD is smaller from order 5 on.

11. With $\mathrm{Crit}$ the criticality and $s$ the shared nets, the attraction is $\lambda \, \mathrm{Crit} + (1 - \lambda) \, s/G$. For $\lambda = 0.75$: $0.725$ against $0.575$, so $b_1$. For $\lambda = 0.25$: $0.375$ against $0.725$, so $b_2$. They tie when $0.9\lambda + 0.2(1 - \lambda) = 0.5\lambda + 0.8(1 - \lambda)$, at $\lambda = 0.6$.

16. Among $a$, $s$, $a'$ the order in $\Gamma^+$ is $a, s, a'$. For the pair $s, a'$ the test asks that the mirror of $a'$, which is $a$, comes before the mirror of $s$, which is $s$, in $\Gamma^-$; it does not. With $\Gamma^- = (a, s, f, a')$: $a$ left of $s$, $f$ and $a'$; $s$ and $f$ left of $a'$; $f$ above $s$. SYM-PACK puts $a$ at $x = 0$, $s$ at $x = 1$, $a'$ at $x = 3$ with the axis at 2, and $f$ on top of $s$. The width is 4, the height 2. The test fixes the relative order of the 3 cells of the group in $\Gamma^-$, so $4!/3! = 4$ orders pass.

19. The value 0 becomes $2^n - 1$, which differs from 0 in $n$ bits, and each gate flips one bit. For the circuit: after $\mathrm{NOT}(0)$, line 0 is 1 exactly when $x_0 = 0$, which is when the subtraction borrows into bit 1. Show by induction on $k$ that the gate with target $k$ fires exactly when $x_0 = \cdots = x_{k-1} = 0$, which is the borrow into bit $k$.

23. (a) Each side has at most 3 nets, and the four nets meet pairwise at a side, so an edge coloring needs 4 colors. (b) Three edges can always get three different colors. (c) A requirement of $W$ nets between two sides uses every terminal of both, so each terminal needs a switch to each of the other three sides. That gives at least $3 \cdot 4W/2 = 6W$ switches, with equality only if each terminal has exactly one.

24. The answer is 3. Each SWAP of a line of 4 makes at most two pairs adjacent that were not, and only the middle SWAP makes two. Start from the 3 pairs of the initial line, and check the four sequences of two SWAPs (middle or end, then middle or end): none reaches all 6 pairs. For the schedule, put $b, a, c, d$ on $q_0, \ldots, q_3$; run $ab$, $ac$; SWAP $(q_1, q_2)$; run $ad$, $bc$; SWAP $(q_2, q_3)$ and $(q_1, q_2)$; run $bd$, $cd$.

25. All terms are $\ge 0$, so the rise grows with $k$. Exchange two adjacent layers $k$ and $k + 1$ with $p_k < p_{k+1}$: only $S_{k+1}$ changes, and it falls by $p_{k+1} - p_k$, so the top rise does not grow. For $5, 3, 1$ from the sink: $\tfrac{1}{2} \cdot 9 + 9 + 4 + 1 = 18.5$. For $1, 3, 5$: $\tfrac{1}{2} \cdot 9 + 9 + 8 + 5 = 26.5$.

26. Take a graph on $2k$ vertices. Add $k$ dummy cells, and join all of them by one net repeated $M = |E| + 1$ times. A split of the dummies costs at least $M$, more than any assignment that keeps them together, so they fill one tier. In an end tier, the cost is the cut of a bisection of the graph; in the middle tier, every cut edge costs 2. So the optimum is the minimum bisection.

27. The label of the self-symmetric cell is uniform among the nodes, so the fraction is $E[r]/n$, with $r$ the length of the rightmost branch of a uniform shape. A branch of length $r$ carries $r$ left subtrees, so $\sum_T r(T) = [x^n] \sum_r r (xB)^r = [x^{n}] \, xB/(1 - xB)^2$, where $B$ is the generating function of binary trees. Use $B = 1 + xB^2$, so $1 - xB = 1/B$, and Lagrange inversion for $[x^{n-1}] B^3$.
