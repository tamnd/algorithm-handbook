2. Each agent keeps her own good when $1/3 \le p_1/p_2 \le 2$: agent 1 then gets at least as much per unit of money from good 1, and agent 2 from good 2. Every ratio in $[1/3, 2]$ is an equilibrium without trade. Outside the interval both agents want the same good, so the market does not clear. In the entry's example, with $u_1 = (1, 2)$ and $u_2 = (1, 1)$, no ratio lets both agents keep their goods, so they must swap, and a swap clears only at ratio 1.

5. Round 1 removes the cycle $1 \to 2 \to 3 \to 1$: agent 1 gets $h_2$, agent 2 gets $h_3$ and agent 3 gets $h_1$. Round 2 removes the swap of agents 4 and 5. Round 3 leaves agent 6 with $h_6$. With $r = 3$ cycles, the prices $r - k + 1$ are 3 for $h_1, h_2, h_3$, 2 for $h_4, h_5$ and 1 for $h_6$.

6. RSD gives agent 1 $(5/6, 0, 1/6)$, agent 2 $(1/6, 1/2, 1/3)$ and agent 3 $(0, 1/2, 1/2)$ over $(a, b, c)$. PS gives $(3/4, 0, 1/4)$, $(1/4, 1/2, 1/4)$ and $(0, 1/2, 1/2)$. Agent 1's RSD row dominates her PS row, agent 2's PS row dominates her RSD row, and agent 3 gets the same row from both, so neither rule is better for everyone.

7. Two with swaps only: the only 2-cycle is $1 \leftrightarrow 2$. Five with length at most 3: the swap and the cycle $4 \to 5 \to 6 \to 4$. Six with any length: the cycle $1 \to 2 \to 3 \to 4 \to 5 \to 6 \to 1$.

9. Deferred acceptance gives $i_1 s_1$, $i_2 s_3$, $i_3 s_2$, $i_4 s_2$. Top trading cycles gives $i_1 s_3$, $i_2 s_1$, $i_3 s_2$, $i_4 s_2$. Boston gives $i_1 s_3$, $i_2 s_2$, $i_3 s_1$, $i_4 s_2$: in round 1, $i_1$ takes $s_3$ and $i_3$ wins $s_1$ by priority, and when $i_2$ applies to $s_3$ in round 2 it is already full.

11. The objective is $\sum_i e_i \sum_j a_{ij} \log x_{ij}$, a sum over goods of terms that each involve only the column $j$, and the constraints are also one per good. For one good, the KKT conditions give $e_i a_{ij} / x_{ij} = p_j$ for every buyer with $a_{ij} > 0$, and summing $x_{ij} = e_i a_{ij} / p_j$ over $i$ gives $p_j$. In the check, $p = (1, 2)$, buyer 1 gets $(1/2, 1/4)$ and buyer 2 gets $(1/2, 3/4)$.

13. The update of good $j$ depends only on $p_j$, with equilibrium $p_j^* = \sum_i a_{ij} e_i$, here $(1, 2)$. The derivative of the map at $p_j^*$ is $1 - \lambda / p_j^*$, so it converges near the equilibrium when $0 < \lambda < 2 p_j^*$ for every good, that is, when $\lambda < 2$. With $\lambda = 2.1$ the price of good 2 still converges to 2, but the price of good 1 settles into a cycle of length two between about $0.821$ and $1.279$.

15. PS gives agents 1 and 2 the row $(1/2, 0, 1/3, 1/6)$, agent 3 $(0, 1/2, 1/3, 1/6)$ and agent 4 $(0, 1/2, 0, 1/2)$. RSD gives agent 1 $(5/12, 1/12, 1/3, 1/6)$, agent 2 $(5/12, 0, 5/12, 1/6)$, agent 3 $(1/12, 11/24, 1/4, 5/24)$ and agent 4 $(1/12, 11/24, 0, 11/24)$. Agent 1 holds $1/12$ of $b$ and agent 3 holds $1/12$ of $a$; exchanging these shares helps both.

16. Bidder 4 gets item 1, bidder 2 gets item 3, and item 2 goes to bidder 1 or to bidder 3, who are both indifferent at its price. The final prices are $(8, 3, 2)$ and the total value is 19. For bidder 4, the others could get 18 without her and get 10 with her, so she pays 8; the same count gives 2 for bidder 2 and 3 for the winner of item 2.

19. Four with swaps only, and still four with length at most 3, because the ring has no 3-cycle. Five with any length, by the directed cycle around the ring. The LP puts $1/2$ on each of the five swaps for a value of 5 transplants. The dual price $y_v = 1$ on every pair covers each swap, $y_u + y_v = 2$, and also sums to 5.

23. Agent 2 can afford only $h_2$, and agent 1 can afford both and likes them equally, so no trade is competitive. The swap leaves agent 1 as well off and makes agent 2 better off. Step 2 fails: agent 1 is as happy with $h_2$ as with $h_1$, yet $h_2$ is cheaper than her budget. Houses are indivisible, so local nonsatiation cannot hold.

24. Let $M$ be stable and $M'$ any matching. An agent who prefers $M'$ is matched in $M'$. Look at its partner in $M'$: if both preferred $M'$, they would block $M$. So the partner does not prefer $M'$, and its partner changed, so with strict lists it strictly prefers $M$. This pairs each voter for $M'$ with a distinct voter for $M$.

25. Every vertex of the fractional matching polytope is half-integral, and its entries equal to $1/2$ form disjoint odd cycles (Balinski). An odd cycle of length $k$ has LP value $k/2$ swaps and contains $(k - 1)/2$ disjoint swaps, and $k/(k - 1) \le 3/2$ for $k \ge 3$. The triangle has LP value 3 and integer optimum 2.

26. Let $r = p_1/p_2$. Agent 1 wants good 1 exactly when $r \le \alpha$, and agent 2 wants good 2 exactly when $r \ge \beta$. If $\beta > \alpha$, a ratio strictly between them needs a full swap, which clears only at $r = 1$; at the end $r = \alpha$, agent 1 is indifferent and agent 2 buys $1/r$ units of good 1, which is possible only if $\alpha \ge 1$, and similarly at $r = \beta$.

27. Every school points to the first student of $\sigma$ who is left, so in top trading cycles she forms a cycle with her favourite school that has a seat. For deferred acceptance, show that the serial dictatorship matching is the only stable matching. For Boston, take priority $i_1, i_2, i_3$ everywhere, $i_1$ and $i_2$ ranking $A, B, C$ and $i_3$ ranking $B, C, A$: Boston gives $i_2$ school $C$, while the other two rules give her $B$.

28. Four men and four women suffice. One instance: $m_1$: $w_2, w_1, w_4, w_3$; $m_2$: $w_3, w_1, w_4, w_2$; $m_3$: $w_4, w_2, w_3, w_1$; $m_4$: $w_3, w_1, w_2, w_4$; $w_1$: $m_3, m_1, m_4, m_2$; $w_2$: $m_1, m_4, m_3, m_2$; $w_3$: $m_3, m_2, m_4, m_1$; $w_4$: $m_4, m_1, m_2, m_3$. Its two stable matchings are $\{m_1 w_2, m_2 w_3, m_3 w_4, m_4 w_1\}$, with cost 15 and regret 4, and $\{m_1 w_2, m_2 w_4, m_3 w_3, m_4 w_1\}$, with cost 17 and regret 3.
