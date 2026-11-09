1. One node for each path from S: S once, A once, B twice, C three times and G five times, so 12 nodes. The five paths to G cost 14 (S-B-G), 13 (S-A-B-G), 11 (S-A-C-G), 9 (S-B-C-G) and 8 (S-A-B-C-G).

3. Breadth-first search generates $4 + 16 + 64 + 256 + 1024 = 1364$ nodes. Iterative deepening generates the nodes at depth $i$ in the $6 - i$ runs with limits $i$ to 5, so $5 \cdot 4 + 4 \cdot 16 + 3 \cdot 64 + 2 \cdot 256 + 1024 = 1812$. The ratio is about 1.328, just below $4/3$.

6. The states are 4, 0, 1, 2, 5, 9, 14, 10, 16, and then 2 again, since $16^2 + 1 = 257 = 15 \cdot 17 + 2$. So $\mu = 3$ and $\lambda = 6$. As $10^9 - 3 \equiv 1 \pmod 6$, $x_{10^9} = x_4 = 5$.

8. Limit 0: *cutoff*, 1 test. Limit 1: *cutoff*, 3 tests (S, A, B). Limit 2: *cutoff*, 6 tests, because D has a child below the limit while C and E report *failure*. Limit 3: the path S-A-D-G after 5 tests (S, A, C, D, G). Iterative deepening returns S-A-D-G after $1 + 3 + 6 + 5 = 15$ tests. If G is not a goal, limit 3 tests all 7 nodes and returns *failure*, and iterative deepening stops there after 17 tests.

9. The expansions are S, A, B and C. The frontier is $\{A{:}2, B{:}5\}$ after S, $\{B{:}4, C{:}8\}$ after A, $\{C{:}5, G{:}13\}$ after B and $\{G{:}8\}$ after C; then G is selected and S-A-B-C-G, cost 8, is returned. With the test at generation, G is first made when B is expanded, and the search returns S-A-B-G of cost 13.

11. $h(A) = 6 > c(A, B) + h(B) = 2$. Without reopening, A* expands S, B (at $g = 5$), A and C, and returns S-B-C-G of cost 9: when A finds B at cost 4, B is already closed. With reopening, B is expanded again at $g = 4$, and the search returns S-A-B-C-G of cost 8 after 5 expansions.

13. The state $v_i$ lies on $2^i$ paths from $v_0$, and $a_i$ and $b_i$ on $2^{i-1}$ each. Sum over all states. Tree-like depth-first search expands $v_{k-1}$ $2^{k-1}$ times and reaches $v_k$ $2^k$ times; graph search expands each of the $3k + 1$ states once.

16. The total is $(2^{k+1} - 2) + (8^{13-k} - 8)/7$. It is least at $k = 9$, with $1022 + 584 = 1606$ nodes, against $8190$ for a forward search alone. The frontier sizes are $2^a$ and $8^\beta$, and the rule keeps them within a factor 8 of each other, which forces $a \approx 3\beta$; with $a + \beta = 12$ this gives $a = 9$.

19. Each term $c^d$ with $2 \le c \le b - 1$ is at most $\int_c^{c+1} x^d \, dx$, so these terms sum to less than $b^{d+1}/(d+1)$; add the last term $b^d$. The factor is below 2 when $b < d + 1$. For $b = 10$ and $d = 5$ the sum is $220824$ and the bound is about $266667$.

20. After the first two turns M is reached by both sides, with $3 + 5 = 8$. With the second rule, the forward side then expands A and reaches B, which gives $\mu = 7$; the backward side expands B; now $3 + 5 \ge 7$ and the search stops with S-A-B-G. For the proof, take a cheapest path, the last state on it that the forward side has expanded, and the next state on it; that next state has either been expanded by the backward side or has distances to both ends at least the two frontier minima.

21. Let $T$ be a local optimum and $e = uv$ an edge not in $T$. If some edge on the path from $u$ to $v$ in $T$ were heavier than $e$, swapping the two would give a lighter tree. So every non-tree edge is at least as heavy as each edge on the cycle it closes, which is the cycle condition for a minimum spanning tree.

22. Admissibility follows by induction on the number of edges of a cheapest path to the goal. For an edge $u \to v$, $g(u) + c(u, v) + h(v) \ge g(u) + h(u)$. If A* selected a state $v$ with a path that is not cheapest, some node on a cheapest path to $v$ would be on the frontier with a smaller $f$, a contradiction. In Exercise 11 the edge A→B breaks the condition.
