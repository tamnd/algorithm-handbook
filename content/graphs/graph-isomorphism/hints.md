1. $C_6$ is connected and two triangles are not, so the number of components separates them. The prism contains two triangles and $K_{3,3}$ is bipartite and has none, so the number of triangles separates the second pair.

2. The map $i \mapsto 2i \bmod 5$ works. The complement of the cycle has the edges $02, 24, 41, 13, 30$, which form the cycle $0, 2, 4, 1, 3$. The map sends each cycle edge $\{i, i+1\}$ to $\{2i, 2i+2\}$, which is a chord of the original cycle and so an edge of the complement.

3. $|\mathrm{Aut}(P_4)| = 2$ (the reversal). $|\mathrm{Aut}(K_{1,3})| = 6$ (any permutation of the leaves). $|\mathrm{Aut}(C_6)| = 12$ (the dihedral group: six rotations and six reflections). $|\mathrm{Aut}(K_{2,3})| = 2! \cdot 3! = 12$. $|\mathrm{Aut}(K_{3,3})| = 2 \cdot 3! \cdot 3! = 72$, where the 2 swaps the two sides. $|\mathrm{Aut}(Q_3)| = 48$.

4. The group has two elements: the identity and the map that swaps $a$ with $b$ and $d$ with $e$ and fixes $c$. The orbits are $\{a, b\}$, $\{d, e\}$ and $\{c\}$. No automorphism can move $c$, because it is the only vertex of degree 2 on the triangle.

5. Vertices 3 and 4 are the only vertices of degree 3. Vertex 4 is adjacent to a leaf, vertex 5, and vertex 3 is not, so no automorphism swaps them and both are fixed. Then 5 is fixed as the only leaf joined to 4, 6 as the only common neighbour of 3 and 4, 2 as the remaining neighbour of 3, and 1 as the remaining neighbour of 2. The only automorphism is the identity.

6. In $T_1$, $c$, $d$ and $e$ are $()$, $a$ is $(()())$ and $b$ is $(())$. Sorting the children and wrapping gives $((()())(()))$ for the root. $T_2$ has the same multiset of child codes and so the same root code. In $T_3$, $c$ is $(())$, $a$ is $((()))$ and $b$ is $(())$, so the root is $(((()))(()))$. $T_1 \cong T_2$, and $T_3$ is different from both.

7. Both trees have the degree sequence $3, 2, 2, 1, 1, 1$. After one round, the degree-3 vertex has neighbours of degrees $1, 1, 2$ in $T$ (vertices 1, 6 and 3) and $1, 2, 2$ in $T'$ (vertices 6, 2 and 4). So the histograms already differ after the first round.

8. In the first pair every vertex has degree 2, and in the second every vertex has degree 3, so every vertex sees the same multiset of neighbour colors. The starting coloring with one color is stable from the first round. Color refinement cannot separate two regular graphs with the same degree and the same number of vertices.

9. $K_4$ has 4 triangles, and each triangle is the image of $3! = 6$ embeddings, so there are 24 embeddings. In the Petersen graph a path on 3 vertices is fixed by its middle vertex and a pair of its neighbours, so there are $10 \cdot \binom{3}{2} = 30$ paths and $60$ embeddings, since each path can be traversed in two directions.

10. If $\varphi$ is one isomorphism from $G$ to $H$, the others are exactly $\varphi \circ \alpha$ for $\alpha \in \mathrm{Aut}(G)$.

12. Each neighbour of $v$ has one neighbour in $\{v\}$ and two among the other six. Each of the other six has one neighbour among the three and two among the six. The quotient matrix has eigenvalues $3$, $1$ and $-2$, which are the eigenvalues of the Petersen graph itself.

14. The clique problem is subgraph isomorphism with the pattern $K_k$, and Hamiltonian cycle is subgraph isomorphism with the pattern $C_n$. Both reductions need a pattern that is smaller than, or sparser than, the host.

16. Use the association graph of compatible vertex pairs and look for a largest clique. The induced version reaches 3 vertices, for example a path on 3 vertices. Without the induced condition, the paw contains $P_4$ as a subgraph ($a, b, c, d$), so the answer is all of $P_4$.

18. The class sizes are $1, 1, 3, 3, 4, 4, 6, 6, 12, 12, 12$. Every graph on 4 vertices has a nontrivial automorphism; the smallest asymmetric graphs have 6 vertices.

20. The original vertices are the vertices of degree at least 3 in the subdivision, and the new vertices have degree 2, so an isomorphism of subdivisions must map original vertices to original vertices.

21. Each class has at most $n!$ labeled members.

22. Fix one dart of $G$. For each dart of $H$ and each of the two orientations, walk the two rotation systems in step and check that the correspondence they force is consistent. Each trial is linear.

24. Deleting edges from $G$ to leave a set of $k$ vertices that spans a clique, and adding the missing edges in that set, costs $m - e(S) + \binom{k}{2} - e(S)$ for the best set $S$.
