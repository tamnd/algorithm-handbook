2. Write each split by the side without A. The first tree has $BC$, $FG$, $EFG$ and $DEFG$; the second has $CD$, $BCD$, $FG$ and $EFG$. They share two splits, so the distance is $2 + 2 = 4$. The largest possible value is $2(n-3) = 8$.

3. The sets are $\{A, C\}$ at $(1,2)$, $\{A\}$ at $((1,2),3)$, $\{C, G\}$ at $(4,5)$, $\{G\}$ at $((4,5),6)$ and $\{A, G\}$ at the root, and the score is 3. One labeling puts A at the root and on the left side, G on the right side: it changes A to C on the edge to leaf 2, A to G on the edge to $((4,5),6)$, and G to C on the edge to leaf 5. The site is informative, since A, C and G each occur at two leaves.

5. The pair sums are $D_{AB} + D_{CD} = 10$, $D_{AC} + D_{BD} = 20$ and $D_{AD} + D_{BC} = 20$. The two largest are equal, so it is a tree metric with split $AB \mid CD$ and inner edge $(20 - 10)/2 = 5$. The pendant edges are 2, 3, 4 and 1 for A, B, C and D; for example, A gets $(D_{AB} + D_{AC} - D_{BC})/2 = 2$. With $D_{AD} = 9$ the sums are 10, 20 and 21, so the condition fails.

7. The longest path is from B to D, of length $8 + 1 + 2 + 6 = 17$. Its midpoint lies 8.5 from B, which is halfway along the edge of length 1 between the node above A and B and the central node. The rooted tree is `((A:2,B:8):0.5,(E:5,(C:3,D:6):2):0.5);`.

8. No cluster other than the leaves and the whole set is in all three trees, so the strict consensus is the star. The clusters $AB$, $ABC$ and $DE$ each occur in two of the three trees, so the majority-rule tree is $T_1$. Removing C (or A) leaves the same tree on four taxa in $T_1$ and $T_3$, so the maximum agreement subtree has 4 leaves. Moving C next to B turns $T_1$ into $T_3$, so the rooted SPR distance is 1.

11. (a) Exact. (b) NP-hard. (c) Statistically consistent. (d) No guarantee: the output is always ultrametric, and the topology can be wrong, as in Exercise 17. (e) It fails: as the number of sites grows, parsimony picks the wrong tree with probability tending to 1. (f) It converges only in the limit; a finite run has no guarantee. (g) Statistically consistent.

13. Both methods join A and B at height 1 and then C at height 3. Next, UPGMA averages over the three taxa: $D(ABC, D) = 26/3$ and $D(ABC, E) = 9$, so D joins at height $13/3$ and E last at $37/8$. WPGMA averages the two parts: $D(ABC, D) = (7 + 12)/2 = 19/2$ and $D(ABC, E) = (10 + 7)/2 = 17/2$, so E joins at $17/4$ and D last at $39/8$. On an ultrametric both are exact, so they return the same tree.

17. Restrict the ultrametric tree to the four taxa. It is either balanced or a caterpillar, and in each case the distance of two taxa is twice the height of their lowest common ancestor; write out the three sums. The tree metric has $D_{AC} = 4$ as its smallest entry and $D_{AB} = 11$, $D_{BC} = 13$, so UPGMA joins A and C first and returns the split $AC \mid BD$. Neighbor-joining is exact on every tree metric.

18. All six pairs are compatible: each pair of 1-sets is nested or disjoint. The tree has the root, the leaf $e$ below it, a node for $\{a, b\}$ with leaves $a$ and $b$, and a node for $\{c, d\}$ with leaves $c$ and $d$. The new character $c_5$ shows all four gametes with $c_1$ and with $c_3$, and is compatible with $c_2$ and $c_4$. The compatibility graph lacks only the edges $c_1c_5$ and $c_3c_5$, so the largest clique is $\{c_1, c_2, c_3, c_4\}$.

19. The node $(b_1, c_1)$ maps to the root $r$ of the species tree and is a speciation with one loss. The node $(a_1, (b_1, c_1))$ maps to $r$, and so does a child, so it is a duplication, with two losses on the edge to $a_1$. The node $(a_2, c_2)$ maps to $r$, a speciation with one loss. The root maps to $r$ and is a duplication with no loss. So there are 2 duplications and 4 losses.

22. The contrasts are $(4 - 6)/\sqrt{2} = -\sqrt{2}$ and $(5 - 1)/\sqrt{1 + 2} = 4/\sqrt{3}$, since the node of A and B gets the value 5 and its branch grows from 0.5 to 1. The root estimate is $(2 \cdot 5 + 1 \cdot 1)/3 = 11/3$, and $\hat\sigma^2 = (2 + 16/3)/2 = 11/3$. With $V$ the covariance matrix, each row of $V^{-1}$ sums to $1/2$, which gives the same $11/3$.

25. By Exercise 16, $Q(A, B) - Q(A, C) = (D_{AB} + D_{CD}) - (D_{AC} + D_{BD})$, which is $-2e$ on the tree metric and changes by at most $4\varepsilon$. For the bad case, take pendant edges 1 and inner edge 2, and set $D_{AB} = D_{CD} = D_{AC} = D_{BD} = 3$: two pair sums tie. Under the model, Exercise 15 and the law of large numbers make the error smaller than $e/2$ with probability tending to 1.

26. In the caterpillar, $t$ is the branch above $(A, B)$; in the balanced tree, it is the sum of the branches above $(A, B)$ and above $(C, D)$. If A and B coalesce in their branch, or C and D in theirs, the gene tree is $AB \mid CD$. Otherwise the lineages that meet are exchangeable, and each of the three quartets has probability $1/3$.

27. A new leaf always makes a new cherry. It also destroys one when the leaf that splits is in a cherry, which happens with probability $2C_k/k$. So $E[C_{k+1}] = E[C_k](1 - 2/k) + 1$, with $C_3 = 1$, and induction gives $k/3$.

28. Cut the edge of the split. Each side becomes a rooted binary tree, on $A$ and on $B$, and the pair determines the tree. With 105 unrooted trees on six taxa, the answers are $15/105 = 1/7$ and $9/105 = 3/35$.

29. The root splits the population into $j$ and $N - j$ copies, with $j$ uniform on $1, \ldots, N-1$. The sample misses the root exactly when all of it lies on one side. Sum $\binom{j}{n}$ over $j$ with the hockey-stick identity. The limit is $(n-1)/(n+1)$.
