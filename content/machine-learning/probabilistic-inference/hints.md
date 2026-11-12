2. $A \perp B$ holds, because the only trail passes through the collider $C$. $A \perp B \mid D$ fails, because $D$ is a descendant of $C$ and opens it. $A \perp E$ holds, since the trail $A \to C \leftarrow B \to E$ is blocked at $C$. $A \perp E \mid C$ fails, since the collider is now open and $B$ is not observed. $A \perp E \mid \{B, C\}$ holds, since observing $B$ blocks the fork $C \leftarrow B \to E$.

5. $\alpha_1 = (0.48, 0.12)$, $\alpha_2 = (0.0768, 0.1512)$ and $\alpha_3 = (0.091392, 0.034128)$, so $P(O) = 0.12552 = 1569/12500$.

6. The Viterbi path is H, H, H, with joint probability $0.6 \cdot 0.8 \cdot 0.7 \cdot 0.2 \cdot 0.7 \cdot 0.8 = 588/15625 = 0.037632$; the next best path, H, L, H, has $0.032256$. The posteriors of H are about $0.750$, $0.398$ and $0.728$, so the most probable states one at a time are H, L, H. The answers differ: the best path and the best single states solve different problems.

9. The marginals are $P(X_1 = 1) = 0.6$ and $P(X_2 = 1) = 0.35$, so the separate maxima give $(1, 0)$, which has probability $0.25$. The MAP assignment is $(0, 0)$, with $0.4$.

12. The E-step fills each lost flip with $\theta$ expected heads, so $\theta' = (6 + 2\theta)/10$. From $1/2$ the steps give $0.7$, $0.74$, $0.748$. The fixed point is $\theta = 3/4$, the rate of the recorded flips, and the error $\theta - 3/4$ is multiplied by $1/5$ at each step, the fraction of the data that is missing.

13. Eliminating $A$ joins $B$ and $E$; then eliminating $B$ joins $C$ and $E$; $C$, $D$ and $E$ add nothing. The cliques are $\{A, B, E\}$, $\{B, C, E\}$ and $\{C, D, E\}$, so the width is 2. A cycle is not a forest, so its treewidth is at least 2, and the order is optimal. The junction tree is a chain of the three cliques with the separators $\{B, E\}$ and $\{C, E\}$.

16. The predicted variance satisfies $P = 4P/(P + 4) + 1$, so $P^2 - P - 4 = 0$ and $P = (1 + \sqrt{17})/2 \approx 2.5616$. The gain is $K = P/(P + 4) = (\sqrt{17} - 1)/8 \approx 0.3904$.

18. Adjust for $Z$ with the weights $P(Z = 0) = 0.7$ and $P(Z = 1) = 0.3$, not with $P(Z \mid X)$. The interventional probabilities are $0.49$ and $0.29$, a difference of $0.20$. The observed ones are $56/95 \approx 0.589$ and $71/310 \approx 0.229$, a difference of about $0.36$, because $Z$ raises both $X$ and $Y$.

21. A spanning tree of $K_{2,3}$ has 4 of the 6 edges, and $K_{m,n}$ has $m^{n-1} n^{m-1}$ spanning trees, here 12. All edges are alike under the symmetries of the graph, so each lies in the same fraction of the trees, $\rho_e = 4/6 = 2/3$.

22. $\Sigma_{ii} \Lambda_{ii} = \lVert \Sigma^{1/2} e_i \rVert^2 \, \lVert \Sigma^{-1/2} e_i \rVert^2 \ge \langle \Sigma^{1/2} e_i, \Sigma^{-1/2} e_i \rangle^2 = 1$ by Cauchy-Schwarz. Equality needs $\Sigma e_i$ to be a multiple of $e_i$, which happens exactly when row $i$ of $\Lambda$ is zero off the diagonal.

23. Write $Z = \operatorname{tr}(M^n)$ with the transfer matrix $M_{xy} = e^{Jxy}$ for $x, y \in \{-1, +1\}$. Its eigenvectors are $(1, 1)$ and $(1, -1)$, with eigenvalues $e^J + e^{-J}$ and $e^J - e^{-J}$. For $n = 3$ both sides equal $2e^{3J} + 6e^{-J}$.

24. Run the forward pass once and keep only $\alpha_t$ for $t$ a multiple of $k = \lceil \sqrt T \rceil$. In the backward pass, take the blocks from last to first; for each, recompute its at most $k$ forward vectors from the checkpoint before it, use them with the $\beta$ vectors, and drop them. The space is $O(N(T/k + k))$, and every $\alpha_t$ is computed twice.

25. The neighbours of a simplicial vertex are already pairwise adjacent, and removing a vertex keeps a graph chordal. A chordal graph has a simplicial vertex (Dirac), so it can be eliminated with no fill, and the eliminated vertex with its neighbours is a clique of the graph, of size at most $\omega$. For the lower bound, the first vertex of a largest clique to be eliminated still has the other $\omega - 1$ as neighbours.

26. Take a trail between $X$ and $Y$ that is active given $Z$. Each collider on it has a descendant in $Z$ and each other node is an ancestor of an endpoint or of a collider, so the whole trail lies in the ancestral set. Replace each collider by the moral edge between its two parents on the trail. The new path avoids $Z$, since non-colliders on an active trail are not in $Z$, which contradicts separation.
