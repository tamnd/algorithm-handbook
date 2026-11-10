1. `p cnf 3 3`, then `1 -2 0`, `-1 2 3 0` and `-3 0`, one clause per line.

3. The eight arcs give two components, $\{x_2, \neg x_3, \neg x_1\}$ and $\{\neg x_2, x_1, x_3\}$. No variable has both literals in one component, so the formula is satisfiable. Its models are $(x_1, x_2, x_3) = (1, 0, 1)$ and $(0, 1, 0)$.

6. The rank is 3 and there are $2^{4-3} = 2$ solutions, $(1, 0, 0, 0)$ and $(0, 1, 0, 1)$. The direct CNF has $4 + 2 + 4 + 2 = 12$ clauses.

8. With $x_1 = 1$, $x_3$ must be 0, so $x_4 = 1$ and $x_2$ is free: 2 models. With $x_1 = 0$, $x_2 = 1$ and $(x_3 \vee x_4)$ has 3 models. The count is 5.

10. Yes for $(x_2)$: setting $x_2 = 0$ makes the first clause unit, so $x_1 = 1$, and then the second clause is false. No for $(x_1)$: setting $x_1 = 0$ propagates $x_2 = 1$ and reaches no conflict. Indeed $F$ does not imply $x_1$.

11. Tseitin: 7 variables, $4 + 3 + 4 + 1 = 12$ clauses and $10 + 7 + 10 + 1 = 28$ literal occurrences. Every gate has positive polarity, so Plaisted-Greenbaum keeps only the clauses from each gate variable to its definition: $1 + 3 + 2 + 1 = 7$ clauses with 15 literal occurrences.

14. At level 2 propagation sets $x_2, x_3, x_4, x_5$, and $C_5$ is false. Every path from $x_1$ to the conflict passes through $x_3$, which is the first UIP. Resolving $C_5$ with $C_4$ and then with $C_3$ gives $(\neg x_3 \vee \neg x_6)$, with literal block distance 2. The solver jumps back to level 1 and propagates $x_3 = 0$, then $x_2 = 0$ and $x_1 = 0$. The decision cut gives $(\neg x_1 \vee \neg x_6)$.

16. At the start the expectation is $7/8 + 4 \cdot 3/4 = 3.875$. For $x_1$ it is 3.75 with $x_1 = 1$ and 4.0 with $x_1 = 0$, so $x_1 = 0$. Then both values of $x_2$ give 4, and both values of $x_3$ give 4, so the ties give $x_2 = x_3 = 1$, which satisfies 4 clauses. The formula is unsatisfiable, since its 2-clauses force $x_1 = 0$, then $x_3 = 0$ and $x_2 = 0$, which falsifies the first clause. So 4 is optimal.

17. The expectation is $2^{100} (7/8)^m$, about $2^{3.68} \approx 12.8$ at $m = 500$. It first falls below 1 at $m = 520$, a ratio of 5.20. The limit of the bound is $\ln 2 / \ln(8/7) \approx 5.19$, well above the predicted threshold of about 4.267.

20. For at most one the counter has $3n - 4$ clauses against $n(n-1)/2$: 11 against 10 at $n = 5$ and 14 against 15 at $n = 6$, so it wins from $n = 6$. For $n = 8$ and $k = 2$ it has 33 clauses and 14 new variables, against $\binom{8}{3} = 56$ clauses.

21. A clause is Horn after the renaming when no two of its literals become positive, which gives one 2-clause in the $s_i$ for each pair of literals. The conditions force $s_1 = s_2$, then $s_1 = s_2 = 1$ from $(s_1 \vee s_2)$, and then $s_3 = 0$. The only renaming flips $x_1$ and $x_2$.

22. Six edge variables, and each vertex has degree 3, so its parity constraint takes 4 clauses: 16 clauses. Each edge appears in two vertex constraints, so the XOR of all constraints has left side 0 and right side 1. The formula is unsatisfiable. With charges $(1, 1, 0, 0)$ the system has rank 3 and $2^{6 - 4 + 1} = 8$ models.

23. The MUSes are $\{a, b\}$, $\{c, e\}$ and $\{a, c, d\}$. The MCSes are $\{a, c\}$, $\{a, e\}$, $\{b, c\}$ and $\{b, d, e\}$. The smallest MCS has 2 clauses, so the MaxSAT value is 3.

24. Without $(x_1)$, set all variables false; without $(\neg x_n)$, set all true; without $(\neg x_i \vee x_{i+1})$, set $x_1, \ldots, x_i$ true and the rest false. A refutation must therefore use all $n + 1$ clauses. In its DAG with $I$ inputs and $s$ steps, each step has two parents, and every node reaches the empty clause, so $2s \ge I + s - 1$ and $s \ge n$. Resolving along the chain takes exactly $n$ steps.
