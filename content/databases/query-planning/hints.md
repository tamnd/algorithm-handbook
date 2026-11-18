1. Each prefix of the order must be connected, so it is an interval of the chain that grows by one relation at either end. The eight orders are 1234, 2134, 2314, 2341, 3214, 3241, 3421 and 4321, so 16 of the 24 orders are left out. A script that lists all 24 orders checked this.

2. The defaults are $1/10$ for the equality, $1/3$ for the comparison and $1/4$ for BETWEEN. Under independence the estimate is $30{,}000 / 120 = 250$ rows. For OR the rule is $s_1 + s_2 - s_1 s_2 = 1/10 + 1/3 - 1/30 = 2/5$, which gives 12,000 rows.

3. The lower bound is $\max(0, 0.7 + 0.6 - 1) \cdot 1000 = 300$, the upper bound is $\min(0.7, 0.6) \cdot 1000 = 600$, and independence gives 420. The upper bound is reached when every row that satisfies the second predicate also satisfies the first. The lower bound is reached when the 300 rows that fail the first predicate all satisfy the second.

4. The estimate is $2000 \cdot 600 / 150 = 8000$. It is exact when the values are uniform in each relation and the 120 values of $S$ are among the 150 values of $R$, the containment assumption.

5. The bucket $[20, 40)$ gives half of 4000 and $[40, 60)$ half of 3000, so the estimate is 3500. With the second predicate it is 350, assuming the two predicates are independent.

6. The scan costs $1200 + 50{,}000 \cdot 0.01 = 1700$, and $1700 + 50{,}000 \cdot 0.0025 = 1825$ with the condition. The scan still reads every page and tests every row, whatever fraction of the rows passes.

8. The q-errors are 4, 5 and 1. The ratio treats an estimate 4 times too small and one 4 times too large alike, and errors in a plan multiply along the joins, so a ratio measures them in the way that matters for cost.

9. $R \bowtie S$ has 1000 tuples and the final result has 1000, so the first order costs 2000. $S \bowtie T$ has 100 tuples, so the second costs 1100. The cross product has 10,000 tuples, so the third costs 11,000. The order $(S \bowtie T) \bowtie R$ is cheapest. A script checked the three sums.

11. The counts are 20 for the chain, 32 for the star and 90 for the clique. They match the closed forms $(n^3 - n)/6$, $(n - 1)2^{n-2}$ and $(3^n - 2^{n+1} + 1)/2$. A script that lists all pairs of disjoint connected sets checked them.

13. The best split is $(1, 1) \mid (9, 10) \mid (2, 2, 3)$, with sum of squares $0 + 1/2 + 2/3 = 7/6$. The next best split, $(1, 1) \mid (9, 10, 2) \mid (2, 3)$, has $77/2$. A script that tried all 15 splits with exact fractions checked this. The point is that a bucket should hold values of similar frequency, not a fixed number of rows.

14. In the first round the benefits are 100 for $a$, 120 for $b$ and 99 for $\emptyset$, so $b$ is chosen. In the second round $a$ saves 50 and $\emptyset$ saves 39, so $a$ is chosen, for a total cost of $100 + 50 + 40 + 40 = 230$. The pairs $\{a, \emptyset\}$ and $\{b, \emptyset\}$ cost 251 and 241, so greedy is optimal here.

16. A tuple $t \bowtie u$ of $R \bowtie S$ appears $m_R(t) \cdot m_S(u)$ times. On both sides it is kept exactly when $p(t)$ holds, because $p$ looks only at $t$. For the second part, take $R = \{(a{:}1, b{:}1)\}$ and $S = \{(a{:}1, c{:}9)\}$: the joined row passes the disjunction through $S.c$, but $\sigma_{R.b > 5}(R)$ is empty. Only the part of a filter that uses $R$ alone may move to $R$.

18. The first plan builds 1000 rows and then 100, for $C_{\mathrm{out}} = 1100$. The cross product has only 100 rows, and joining it with $R_2$ gives the final 100 rows, for $C_{\mathrm{out}} = 200$. An optimizer that never forms a cross product misses the best plan when the relations it would combine are very small.

20. Swapping two neighbors $R_a$ and $R_b$ changes only the size after the first of them, from $P n_a f_a$ to $P n_b f_b$, where $P$ is the size before both. All other terms of the sum stay the same.

22. For the chain, a left-deep order starts at some relation and then extends an interval to the left or to the right. For the star, the center must be first or second, and the satellites then come in any order.
