1. ◦ Four relations form a chain query $R_1 - R_2 - R_3 - R_4$, with a join predicate only between neighbors. List the left-deep [join orders](/join-ordering/) that never form a cross product. How many of the $4! = 24$ orders are left out?

2. ◦ A table has 30,000 rows and no statistics, so the optimizer uses the System R default [selectivities](/selectivity/). Estimate the rows that pass `city = 'Lyon' AND age > 40 AND salary BETWEEN 10 AND 20`, assuming independence. Then estimate `city = 'Lyon' OR age > 40` with the rule for OR.

3. ◦ Two predicates on a table of 1000 rows have selectivities 0.7 and 0.6. Give the Fréchet lower and upper bounds on the number of rows that satisfy both, and the estimate under independence. Describe a table for which each bound is the true count.

4. ◦ Relation $R$ has 2000 rows and $S$ has 600. The join attribute has 150 distinct values in $R$ and 120 in $S$. Estimate the size of the equijoin $R \bowtie_{R.a = S.a} S$ with the rule $|R|\,|S| / \max(V(R, a), V(S, a))$, and name the assumption that makes this rule exact.

5. ◦ An equi-width [histogram](/histogram/) on $\mathit{age}$ over 10,000 rows has the buckets $[0, 20)$ with 1000 rows, $[20, 40)$ with 4000, $[40, 60)$ with 3000 and $[60, 80)$ with 2000. Estimate the number of rows with $30 \le \mathit{age} < 50$, assuming values are spread evenly inside each bucket. Estimate it again for the same predicate combined by AND with a predicate of selectivity $0.1$, and name the assumption you used.

6. ◦ Using the PostgreSQL rule of the [cost model](/cost-model/) entry, with `seq_page_cost` = 1, `cpu_tuple_cost` = 0.01 and `cpu_operator_cost` = 0.0025, find the estimated cost of a sequential scan of a table with 50,000 rows on 1200 pages, without and with one `WHERE` condition. Why does the selectivity of the condition not change the cost?

7. ◦ A query computes $R \mathbin{⟕} S$ on $R.a = S.a$, a left outer join that keeps every row of $R$. For each filter in the `WHERE` clause, say whether [predicate pushdown](/predicate-pushdown/) may move it below the join, and to which side: (a) $R.b = 5$; (b) $S.c = 7$; (c) $S.c \text{ IS NULL}$.

8. ◦ The q-error of an estimate $\hat{c}$ of a true count $c$ is $\max(\hat{c}/c, c/\hat{c})$. Find the q-errors of the estimates 25, 1000 and 300 for the true counts 100, 200 and 300. Why does [cardinality estimation](/cardinality-estimation/) use this ratio and not the difference?

9. • A chain query joins $R$ with 1000 tuples, $S$ with 100 and $T$ with 10. The join of $R$ and $S$ has selectivity $1/100$ and that of $S$ and $T$ has selectivity $1/10$, and there is no predicate between $R$ and $T$. Compute $C_{\mathrm{out}}$, the sum of the sizes of the join results, for $(R \bowtie S) \bowtie T$, $(S \bowtie T) \bowtie R$ and $(R \times T) \bowtie S$. Which order is cheapest under $C_{\mathrm{out}}$?

10. • The [Selinger join enumeration](/selinger-join-enumeration/) over left-deep plans keeps one best plan for each nonempty set of relations, and builds the plan for a set $S$ by choosing the relation $j \in S$ that is joined last. For $n = 10$ relations, count the sets, and the pairs $(S, j)$ with $|S| \ge 2$ that the dynamic program examines. Compare with the number of left-deep orders.

11. • A bushy enumerator that avoids cross products looks at pairs $(S_1, S_2)$ of disjoint sets of relations, each connected in the query graph, with at least one join predicate between them. Count these unordered pairs for $n = 5$ relations when the query graph is a chain, a star and a clique.

12. • Build an equi-depth histogram with three buckets on the twelve values $2, 3, 3, 5, 8, 8, 8, 9, 15, 30, 31, 40$. Estimate the number of values with $A \le 20$, assuming values are spread evenly over the range of each bucket, and compare with the true count. Show that for any range predicate on one side, the error is at most the count of one bucket.

13. • The frequencies of seven consecutive values are $(1, 1, 9, 10, 2, 2, 3)$. Find the V-optimal histogram with three buckets of consecutive values, the one that minimizes the sum over buckets of the squared deviations from the bucket mean. Give its sum of squares.

14. • A data cube has the views $ab$ with 100 rows, $a$ with 50, $b$ with 40 and $\emptyset$ with 1, where each view can be computed from any view above it in the lattice and the cost of a query is the size of the view it reads. The top view $ab$ is always stored. Run the greedy algorithm of [view selection](/view-selection/) for two more views, and check its choice against all pairs.

15. • Relations $R$, $S$ and $T$ join on one attribute $A$, and $T$ is stored sorted on $A$. For $\{R, S\}$ a hash join costs 100, and a merge join costs 120 and returns its output sorted on $A$. Joining the result with $T$ by a merge costs 50 if the input is sorted on $A$; unsorted input must first be sorted at a cost of 100. Which plan does a dynamic program that keeps only the cheapest plan for each set return, and which plan is best? How do interesting orders fix this?

16. • Show that $\sigma_p(R \bowtie S) = \sigma_p(R) \bowtie S$ in bag semantics when $p$ uses only attributes of $R$: compare the multiplicity of each output tuple on the two sides. Then give an instance showing that replacing the filter $R.b > 5 \lor S.c > 5$ above the join by $\sigma_{R.b > 5}(R) \bowtie S$ loses rows.

17. • Predicates $p_1, \ldots, p_k$ have selectivities $s_1, \ldots, s_k$. Prove that the true selectivity of their conjunction lies between $\max(0, s_1 + \cdots + s_k - (k - 1))$ and $\min_i s_i$. When all $s_i = s$ and the predicates hold on the same rows, find the q-error of the estimate under independence.

18. • A chain query $R_1 - R_2 - R_3$ has $|R_1| = |R_3| = 10$, $|R_2| = 10{,}000$ and both join selectivities equal to $1/100$. Compare $C_{\mathrm{out}}$ for $(R_1 \bowtie R_2) \bowtie R_3$ and for $(R_1 \times R_3) \bowtie R_2$. What does this say about [query optimization](/query-optimization/) that never considers cross products?

19. ★ In a chain query $R_1 - \cdots - R_n$, show that every connected set of relations is an interval $\{R_i, \ldots, R_j\}$. Give a dynamic program over intervals that finds the best bushy plan without cross products under $C_{\mathrm{out}}$ in $O(n^3)$ time, and relate it to [matrix chain multiplication](/matrix-chain-multiplication/).

20. ★ A star query has a center $R_0$ and satellites $R_1, \ldots, R_m$, where $R_i$ has $n_i$ rows and its join with $R_0$ has selectivity $f_i$. Among left-deep plans that start with $R_0$, prove by an exchange argument that $C_{\mathrm{out}}$ is smallest when the satellites are joined in increasing order of $n_i f_i$.

21. ★ A chain of $n$ relations is estimated by multiplying $n - 1$ join selectivities, each with q-error at most $q$, while the base table sizes are exact. Prove that the estimate of the full join has q-error at most $q^{n-1}$, and give an instance where this bound is reached.

22. ★ Prove that a chain query on $n$ relations has $2^{n-1}$ left-deep orders without cross products, a star query on $n$ relations has $2(n - 1)!$, and a clique has $n!$. Check the counts 16, 48 and 120 for $n = 5$.
