1. (a) No ratio $\alpha \ge 0.9/0.96 = 15/16$. (b) No ratio $\rho < 5/4$. (c) A ratio $\rho < 4/3$ returns a value below 4 on every instance with $\mathrm{OPT} \le 3$, so it separates the cases; an additive $+1$ returns at most 4 on those instances, which an instance with $\mathrm{OPT} = 4$ can also give. For the chromatic index, telling 3 from 4 on cubic graphs is NP-complete (Holyer 1981), and Vizing's theorem gives $\Delta + 1 \le \mathrm{OPT} + 1$ colours in polynomial time.

3. The first set has total 24, and $\{3, 9\}$, $\{5, 7\}$ split it, so OPT $= 2$ and the algorithm must use 2 bins. The second has total 32, but no subset sums to 16 (an odd sum needs exactly one of 9 and 11, and $16 - 9 = 7$ and $16 - 11 = 5$ are not sums of $2, 4, 6$), so OPT $= 3$, and the algorithm may use 3 or 4 bins.

7. $x = (0, 4, 2, 3)$ satisfies all five. After the change, $x_3 - x_1 = 2$ and $x_3 - x_4 = 4$ force $x_4 - x_1 = 2 - 4 = 3 \pmod 5$, against the new constraint $x_4 - x_1 = 1$, so some constraint fails. The old assignment satisfies the other four, so the value is $4/5$.

8. The acceptance is $\frac12 - \frac12 \operatorname{Stab}_\rho[f]$. A dictator passes with $\frac{1 - \rho}{2} = \frac23$. $\operatorname{Stab}_\rho[\operatorname{Maj}_3] = \frac34\rho + \frac14\rho^3 = -\frac{7}{27}$, so it passes with $\frac{17}{27} \approx 0.630$. The limit is $\frac1\pi \arccos(-\frac13) \approx 0.6082$, and the ratio $0.6082 / 0.6667 \approx 0.912$ is above $\alpha_{\mathrm{GW}}$, since $\rho = -\frac13$ is not the minimizing point.

12. Induct on $k$. Replace each clause $C$ by $C \lor y_C$ and $C \lor \lnot y_C$ with a fresh variable $y_C$. A satisfiable formula stays satisfiable, and an assignment satisfies both new clauses when $C$ is true and exactly one when it is false, so the fraction becomes $\frac12(1 + \text{old fraction})$.

13. Count by the number of true literals among $a, b, c$, for $d$ true and for $d$ false. With Håstad's gap, satisfiable formulas give $7m$ satisfied clauses out of the $10m$, and formulas with at most $(\frac78 + \delta)m$ satisfied clauses give at most $(\frac{55}{8} + \delta)m$.

15. In a proper colouring of the join, different copies use disjoint sets of colours. Given a graph $G$, run the algorithm on the join of $k$ copies with $k > d/(3\varepsilon)$: if $\chi(G) \le 3$ it uses fewer than $4k$ colours, and otherwise at least $4k$.

19. Adjacent vectors are at angle $6\pi/7$, so each edge contributes $\frac12(1 + \cos\frac{\pi}{7})$. In general the vectors at angle $\frac{2m\pi}{2m+1}$ give $\frac{2m+1}{2}(1 + \cos\frac{\pi}{2m+1})$ against a cut of $2m$.

21. Let the suppliers be the sets and the clients the elements. Put a client at distance 1 from the sets that contain it and 3 from the others, and any two clients, or two suppliers, at distance 2. Then the optimal radius is 1 or 3, according as $k$ sets cover everything or not.

22. Add a vertex $w_e$ adjacent to both ends of each edge $e$. A vertex cover dominates the new graph, and a dominating set becomes a vertex cover of no larger size if each $w_e$ in it is replaced by an end of $e$. Use that the graph has no isolated vertex.

23. The first coordinates of an independent set form an independent set $I$ of $G$, and for each $u \in I$ the second coordinates of the points over $u$ form an independent set of $H$. So $|S| \le |I| \cdot \max_u |S_u|$. Apply this to the powers $G[G[\cdots]]$, which have polynomial size for a fixed number of factors, and use that independent set is APX-hard by the L-reduction from MAX 3SAT.

24. A strategy is a map from question pairs to answer pairs for each prover, and there are $4^4$ of them each, so a search is small. The value is $5/8$, larger than $(3/4)^2 = 9/16$: one optimal strategy answers $00$ everywhere except on question pair $11$, where the first prover answers $01$ and the second $10$.

25. For a Gram matrix $X$ with unit diagonal, the SDP objective is $\frac14 \operatorname{tr}(LX)$, and $\operatorname{tr}(LX) \le \lambda_{\max}(L)\operatorname{tr}(X) = n\lambda_{\max}(L)$. The eigenvalues of the cycle Laplacian are $2 - 2\cos\frac{2\pi j}{n}$; for odd $n$ the largest is $2 + 2\cos\frac{\pi}{n}$, and the vectors of exercise 19 reach the bound.
