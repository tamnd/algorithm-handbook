1. After the first reading the belief is $8/19$ at each door and $1/19$ elsewhere. The move shifts it to $(1/19, 8/19, 8/19, 1/19, 1/19)$. The second reading gives $(4/41, 32/41, 4/41, 1/82, 1/82)$: cell 1 is the only door that follows a door.

2. $l = 3\log 4 + 2\log(3/7) \approx 2.464$, since the odds are $4^3 (3/7)^2 = 576/49$, which gives $p = 576/625 = 0.9216$ exactly. Without clamping, the update is a sum, so the order does not matter.

7. The bias gives $0.01 \cdot 100 = 1$ rad, about $57°$. The noise gives a standard deviation of $0.001\sqrt{100} = 0.01$ rad. The bias dominates and grows as $t$; the noise grows as $\sqrt t$.

8. $D^2 = 0.36/0.09 + 0.09/0.04 = 4 + 2.25 = 6.25$. It fails the $95\%$ gate and passes the $99\%$ gate. There are $(5 + 1)^4 = 1296$ joint hypotheses.

10. The prediction is $P^- = P + 1$ and the correction is $P^+ = 2P^-/(P^- + 2)$. A fixed point solves $P^2 + P - 2 = 0$, so $P = 1$, with $P^- = 2$ and gain $K = 1/2$. The map $P \mapsto 2(P+1)/(P+3)$ has slope below 1 on $P \ge 0$, so the iteration converges from any start.

12. Setting the gradient to zero gives $2x_1 - x_2 = 0$ and $-x_1 + 5x_2 = 7.8$. So $x_1 = 13/15$, $x_2 = 26/15$, and the cost is $1/25$. The closure, with four times the weight, takes most of the disagreement of 0.3.

13. $\Lambda = \begin{pmatrix} 3 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix}$ and $\eta = (-3, 0, 3)$. The reduced matrix is $\begin{pmatrix} 5/2 & -3/2 \\ -3/2 & 3/2 \end{pmatrix}$ with $\eta' = (-3/2, 3/2)$, which gives $x_1 = 0$, $x_2 = 1$ and then $l = 2$. The link between $x_1$ and $x_2$ grows from $-1$ to $-3/2$, because the landmark seen from both poses now acts as a constraint between them.

14. Eliminating $l$ first joins its four neighbors into a clique, which adds $x_1x_3$, $x_1x_4$ and $x_2x_4$: three fill edges. In the other order each pose, when eliminated, has neighbors $x_{i+1}$ and $l$, which are already adjacent, so there is no fill. The nonzeros of $R$, and so the cost of the factorization, depend on the order.

16. $C = (2, 3, 3, 4, 5, 5, 2, 0, 4, 1, 0)$, and the bounds of the four blocks are 6, 8, 9 and 3. The search opens the block $\{4, 5\}$, scores shift 4 at 4 and shift 5 at 9, and prunes the other three blocks, whose bounds are below 9. Shift 5 wins after two of the eight shifts are scored.

17. $B = e_3 e_3^\top$, so $\sigma = 1$, $S = B + B^\top = 2e_3e_3^\top$ and $z = 0$. Then $K = \operatorname{diag}(-1, -1, 1, 1)$, with eigenvalue 1 twice. Every unit quaternion $(0, 0, \sin(\varphi/2), \cos(\varphi/2))$ is optimal: any rotation about $e_3$ maps $r$ to $b$.

20. Expand $\lVert b_i - A r_i \rVert^2 = 2 - 2\, b_i^\top A r_i$ and use $\sum_i a_i b_i^\top A r_i = \operatorname{tr}(A B^\top)$. Maximizing $q^\top K q$ over unit $q$ gives $\lambda_{\max}$. The example predicts a loss of $2 - 1.9996954 = 3.046 \times 10^{-4}$, which is the optimum the entry reports.

21. Write $m_j = x + \bar z_j + e_j$, where $\bar z_j$ is the mean of the $k$ readings and $e_j$ has variance $r/k$. Then $\operatorname{Var} x = P_0$, $\operatorname{Cov}(x, m_j) = P_0$, $\operatorname{Var} m_j = P_0 + r/k$, $\operatorname{Cov}(m_1, m_2) = P_0$ and $\operatorname{Var}(m_1 - m_2) = 2r/k$. At $P_0 = r = 1$, $k = 4$, these are $1, 1, 5/4, 1$ and $1/2$. The relative error tends to 0 and meets the bound $2R/k$ of the theorem, while the absolute error never falls below $P_0$.

22. The Schur complement of $x_1$, whose diagonal entry is $5$, gives $4/5$ on the diagonal and $-1/5$ everywhere off it: every pair is now linked. Marginalizing the old pose in each motion step links all landmarks it was linked to, so the matrix fills in. The sparse filter bounds the number of active landmarks and cuts the links of the others, which is an approximation that makes the map overconfident.

23. $P(K \le \varepsilon) = P(2nK \le 2n\varepsilon) = 1 - \delta$ when $2n\varepsilon = \chi^2_{k-1, 1-\delta}$, so $n = \chi^2_{k-1,1-\delta}/(2\varepsilon)$. The chi-square law holds only as $n \to \infty$, and the samples come from the predicted belief and are weighted afterwards, so the bound controls the histogram of the proposal, not of the posterior.
