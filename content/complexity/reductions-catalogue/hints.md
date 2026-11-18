1. (a) Neither: it shows again that $X$ is in NP. (b) NP-hard. (c) In P, since 2-SAT is in P. (d) NP-hard under Cook reductions. It does not show Karp hardness, which is the usual meaning. (e) In P, and in this case P = NP.

2. (a) The output of $f$ has length $O(n^2)$, so $g \circ f$ runs in time $O(n^2 + (n^2)^3) = O(n^6)$ and writes $O(n^6)$ symbols. (b) The degrees multiply: $O(n^{16})$. (c) A chain of $k$ steps of degree $d$ has degree $d^k$, which is not a constant when $k$ grows.

3. (a) 6 vertices. Of the 9 pairs between the two clauses, $x_1, \lnot x_1$ and $x_2, \lnot x_2$ conflict, so there are 7 edges. (b) The formula fails only at $(x_1, x_2, x_3) = (0, 0, 0)$ and $(1, 1, 0)$, so it has 6 satisfying assignments. The 2-cliques are the 7 edges. (c) No: the counts differ.

4. (a) $\{8, 9\}$ and $\{3, 5, 9\}$. (b) The subset sums are $0, 3, 5, 8, 9, 11, 12, 13, 14, 16, 17, 20, 22, 25$, so the best value within capacity 15 is 14 and the answer is no.

5. (a) $g_1 = 1$, $g_2 = 1$, $g_3 = 1$, $g_4 = 0$, $g_5 = 0$. (b) Each of the four AND and OR gates becomes two gates, one for $g$ and one for $\lnot g$ by De Morgan, so 8 gates. The NOT gates disappear: $\lnot x_2$ is an input, and $g_4$ is the rail $\lnot g_3$.

6. $B/4 = 7.5$ and $B/2 = 15$, and the sum is $60 = 2 \cdot 30$. The only split as multisets is $\{8, 9, 13\}$ and $\{8, 10, 12\}$. Since there are two 8s, it is two splits of the indices.

7. The 8 solutions are $0010$, $0011$, $0100$, $0110$ and their complements $1101$, $1100$, $1011$, $1001$. Complementing every variable keeps "not all equal" in every clause, and no assignment is its own complement, so the solutions come in pairs.

8. (a) The cycle $1, 2, 3, 4$ is Hamiltonian, so the optimal cost is $4$. (b) A tour on 4 vertices meets the center only twice, so it uses two graph edges and two non-edges: cost $6$. The bound is $n = 4$, so the answers are yes and no.

10. "Is 17 reachable from $5, 8, 9$?" Yes, so drop 3. "From $8, 9$?" Yes, so drop 5. "From $9$?" No, so keep 8, and the target becomes 9. "From the empty list?" No, so keep 9. With the first question, whether 17 is reachable at all, that is 5 questions, and $n + 1$ in general. The result is $\{8, 9\}$.

11. (a) $4n + 3m$ clauses. (b) 35 clauses, and 30 satisfying assignments, the same as the number of proper 3-colorings of the 5-cycle, $2^5 - 2$. (c) 34 clauses and no satisfying assignment. (d) Yes, since a satisfying assignment gives each vertex exactly one color. Without the "at most one" clauses the reduction is still correct but not parsimonious, because a vertex may get several colors.

12. (a) $1 + 1 + 5 = 7$, but the row of the middle digit has no 1 at all, so $Ax = \mathbf{1}$ has no solution. The two 1s in the last digit carry into the middle one. (b) A digit is a sum of at most $n$ ones, which is at most $n$ and so below the base $n + 1$. Then the digits of the sum are the row sums, and the sum equals the target only if every row sum is 1.

14. (a) There are 8 variables, the three inputs and five gate variables, and 3 clauses per gate plus 1 for the output, which makes 16 clauses. (b) 4 satisfying assignments, one for each input with majority 1. The encoding is parsimonious.

19. (a) Try all eight values of $(a, b, c)$ with both values of $d$, or argue directly: with one true literal and $d$ false you satisfy 7. If $a = b = c = 0$, then $d = 0$ gives 6 and $d = 1$ gives 4. (b) With $m$ clauses, ask for $K = 7m$. The problem is in NP, and the map takes polynomial time.

20. Each clause has three variables and each variable is in three clauses, so every set of $j$ clauses meets at least $j$ variables: its $3j$ incidences cover each variable at most three times. Hall's theorem gives a matching. Set each matched variable so that it makes its own clause true. With four occurrences per variable, a set of clauses can meet fewer variables than its size, and Hall's condition fails.

21. If the reduction runs in time $p(n)$, it asks only about strings of length at most $p(n)$, and $S$ has polynomially many of them. Give their list as advice. The machine answers each question by looking it up, which gives a polynomial-size circuit for SAT.

22. For example, let $\mathrm{pad}(\varphi, y)$ add new variables $z_0, z_1, \ldots, z_{|y|}$ and the clauses $(z_0 \lor \lnot z_0)$ and $(z_i \lor \lnot z_i)$ or $(z_i \lor z_i \lor \lnot z_i)$ according to bit $i$ of $y$. These clauses are always true, so satisfiability is kept, and the shape of the clauses spells out $y$. An isomorphism is a polynomial-time bijection $h$ with $x \in \mathrm{SAT} \iff h(x) \in \mathrm{CLIQUE}$ whose inverse is also polynomial-time, so the two sets are the same set written in two notations.
