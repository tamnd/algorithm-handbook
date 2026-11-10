1. There are $10 \cdot 3 = 30$ variables. Each vertex has 1 at-least-one clause and 3 at-most-one clauses, which gives 10 and 30, and each of the 15 edges gives 3 clauses, one per colour, which gives 45. The total is 85. The Petersen graph has chromatic number 3, so the formula is satisfiable.

2. A value of $X$ needs some larger $Y$, so $X \in \{2, 3\}$. A value of $Y$ needs some smaller $X$, so $Y \in \{3, 4\}$. The solutions are $(2, 3)$, $(2, 4)$ and $(3, 4)$.

4. $R$ is closed under majority and under $x \oplus y \oplus z$: any three tuples from $R$ give a tuple of the form $01$ or $10$. It is not closed under min or max, since $\min(01, 10) = 00$ and $\max(01, 10) = 11$, and it contains neither $00$ nor $11$. So $R$ is bijunctive and affine, and not Horn, dual Horn, 0-valid or 1-valid.

6. The width of an ordering is the largest number of earlier neighbours of a vertex. Along $(A, B, C, D)$ the counts are 0, 1, 2, 2, so the width is 2. Along $(D, C, B, A)$ the vertex $A$ has 3 earlier neighbours, so the width is 3. The triangle $ABC$ forces width at least 2, so the width of the graph is 2. Strong 3-consistency then gives a backtrack-free search along $(A, B, C, D)$.

8. The fixpoint is $X \in \{2, 4\}$, $Y \in \{1, 2\}$ and $Z \in \{2, 3, 4, 5\}$: $X = 2Y$ keeps only even $X$ with $Y \le 2$, $Y < Z$ removes $Z = 1$, and $Z + X \le 7$ with $X \ge 2$ removes nothing more. The solutions are $(2, 1, 2)$, $(2, 1, 3)$, $(2, 1, 4)$, $(2, 1, 5)$ and $(4, 2, 3)$. Here every value left is in some solution, but arc consistency does not promise this in general.

10. The minimal network is $10 \le x_1 - x_0 \le 15$, $30 \le x_2 - x_1 \le 35$ and $40 \le x_2 - x_0 \le 45$. The earliest times are $x_1 = 10$ and $x_2 = 40$. With $x_2 - x_0 \le 39$ the cycle $x_0 \to x_2 \to x_1 \to x_0$ has weight $39 - 30 - 10 = -1$.

11. The variables $x_1, x_2, x_3$ have only the three values $\{1, 2, 3\}$ between them, so they form a Hall set and take all three. Régin's filter removes the edges that lie in no maximum matching: 1, 2 and 3 from $x_4$, which leaves $x_4 = 4$, and 3 and 4 from $x_5$, which leaves $x_5 = 5$. The solutions are $(1, 2, 3, 4, 5)$ and $(2, 3, 1, 4, 5)$.

15. The search jumps to $x_4$, the latest variable in $P(6)$. Its induced ancestor set is $P(4) \cup P(6) \setminus \{x_4\} = \{x_1, x_2, x_3\}$. If $x_4$ then has no values left, the search jumps to $x_3$, the latest variable of that set. The key idea for $x_5$: it shares no constraint with $x_4$ or $x_6$, so no value of $x_5$ can change why they fail.

17. Both relations are polynomial alone: $x \neq y$ is bijunctive and affine, and $x \vee y \vee z$ is 1-valid and dual Horn. The clause is not bijunctive, since the majority of $100$, $010$ and $001$ is $000$, and it is not affine, since it has 7 tuples and an affine relation has a power of 2. The relation $\neq$ is neither 1-valid nor dual Horn, as it misses $11$ and $\max(01, 10) = 11$. No class contains both, so the language is NP-complete. For the reduction, add a fresh variable $\bar{x}$ with $x \neq \bar{x}$ for each variable of a 3-CNF formula, and write each clause with $\bar{x}$ in place of $\neg x$.

18. Build the induced graph from the last vertex to the first, joining the earlier neighbours of each vertex. In the row order $b_2$ ends with the earlier neighbours $a_2, a_3, b_1$, so $w^* = 3$. In the column order every vertex has at most 2 earlier neighbours after the fill edges $a_3 b_2$ and $a_2 b_1$, so $w^* = 2$. The costs are $O((m + n)d^4)$ and $O((m + n)d^3)$. The grid contains a cycle, so its treewidth is at least 2, and the column order reaches it.

19. Count the classes by the symmetries that fix a solution. One solution is fixed by the half-turn, so its class has $8 / 2 = 4$ members, and no solution has a larger symmetry group. So $92 = 8a + 4b$ with $b = 1$, which gives $a = 11$ classes of 8 and 12 classes in all. A constraint that keeps one solution per class leaves 12 solutions in place of 92, and cuts the search that leads to the other 80.

20. The derived relation on $(v_1, v_3)$ is the composition of $\neq$ with $\neq$, which is $=$ on two colours. On $(v_1, v_4)$, the path through $v_3$ gives $=$ composed with $\neq$, which is $\neq$, while the path through $v_5$ gives $\neq$ composed with $\neq$, which is $=$. The intersection is empty, so the network is inconsistent. An even cycle is 2-colourable, and path consistency leaves it with non-empty relations.
