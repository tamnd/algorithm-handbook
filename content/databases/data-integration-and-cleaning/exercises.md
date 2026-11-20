1. ◦ Classify each source-to-target dependency as [GAV, LAV](/gav-and-lav/), both or neither: (a) $\mathrm{Emp}(e, d) \to \mathrm{Works}(e, d)$; (b) $\mathrm{Emp}(e, d) \wedge \mathrm{Dept}(d, m) \to \mathrm{Mgr}(e, m)$; (c) $\mathrm{Emp}(e, d) \to \exists m\, (\mathrm{Works}(e, d) \wedge \mathrm{Boss}(e, m))$; (d) $\mathrm{Emp}(e, d) \wedge \mathrm{Dept}(d, m) \to \exists z\, \mathrm{Rep}(e, z)$.

2. ◦ In the [Fellegi-Sunter model](/fellegi-sunter-model/) two fields are compared, with agreement probabilities $m = (0.9, 0.8)$ among matches and $u = (0.1, 0.2)$ among non-matches, and the fields are independent. Give $m(\gamma)$, $u(\gamma)$ and the ratio $m(\gamma)/u(\gamma)$ for the four patterns AA, AD, DA and DD, where A means agree. If the rule links only AA and rejects only DD, what are its two error levels $\mu$ and $\lambda$?

3. ◦ Ten records fall into blocks of sizes 4, 3, 2 and 1 under a [blocking](/entity-resolution-blocking/) key. How many pairs are compared, and what is the reduction ratio? If 6 pairs are true matches and 5 of them are in the same block, give the pair completeness and the pair quality.

4. ◦ The [sorted neighborhood method](/sorted-neighborhood-method/) runs on $n = 1000$ records with window $w = 10$. How many comparisons does one pass make, and how many do three passes with different keys make? Compare with the number of all pairs.

5. ◦ The [conditional functional dependency](/conditional-functional-dependency/) $([\mathit{AC}] \to [\mathit{CT}],\ \{(908 \,\|\, \mathrm{MH}),\ (\_ \,\|\, \_)\})$ is checked on the rows $(908, \mathrm{MH})$, $(908, \mathrm{NYC})$, $(212, \mathrm{NYC})$, $(212, \mathrm{LA})$ and $(415, \mathrm{SF})$, numbered 0 to 4. Which rows violate the constant pattern alone, and which rows take part in some violation?

6. ◦ The [denial constraint](/denial-constraint/) $\forall t, t'\ \neg(t.\mathit{st} = t'.\mathit{st} \wedge t.\mathit{sal} < t'.\mathit{sal} \wedge t.\mathit{rate} > t'.\mathit{rate})$ is checked on the rows (NY, 50, 10), (NY, 70, 8), (NY, 90, 12), (CA, 40, 9) and (CA, 60, 7), numbered 0 to 4. List the violating pairs. How many subset [repairs](/database-repair/) are there, and which of them are cardinality repairs?

7. ◦ The mapping $\mathrm{Takes}(s, c) \to \exists t\, (\mathrm{Enrolled}(s, c) \wedge \mathrm{Teaches}(t, c))$ is applied to the source $\{\mathrm{Takes}(\mathrm{ann}, \mathrm{db}), \mathrm{Takes}(\mathrm{bob}, \mathrm{db}), \mathrm{Takes}(\mathrm{ann}, \mathrm{ai})\}$. Chase it into a [universal solution](/universal-solution/). Then give the [certain answers](/certain-answers/) of $Q_1(c) \text{ :- } \mathrm{Teaches}(t, c)$, of $Q_2(t) \text{ :- } \mathrm{Teaches}(t, c)$, of $Q_3(s) \text{ :- } \mathrm{Enrolled}(s, c), \mathrm{Teaches}(t, c)$, and of $Q_4(s, s') \text{ :- } \mathrm{Enrolled}(s, c), \mathrm{Teaches}(t, c), \mathrm{Enrolled}(s', c'), \mathrm{Teaches}(t, c')$.

8. ◦ Say which sets of target tgds are [weakly acyclic](/weak-acyclicity/): (a) $E(x, y) \to \exists z\, E(y, z)$; (b) $\mathrm{Emp}(e) \to \exists d\, \mathrm{Works}(e, d)$ and $\mathrm{Works}(e, d) \to \mathrm{Dept}(d)$; (c) $\mathrm{Works}(e, d) \to \exists m\, \mathrm{Mgr}(d, m)$ and $\mathrm{Mgr}(d, m) \to \exists d'\, \mathrm{Works}(m, d')$; (d) $\mathrm{Works}(e, d) \to \exists m\, \mathrm{Mgr}(d, m)$ and $\mathrm{Mgr}(d, m) \to \mathrm{Emp}(m)$. For (c), chase the instance $\{\mathrm{Works}(a, b)\}$ for a few steps.

9. ◦ The relation $r(A, B, C, D)$ holds $(1, x, p, 10)$, $(1, x, q, 10)$, $(2, y, p, 20)$, $(2, z, p, 20)$ and $(3, y, q, 30)$. List every minimal nontrivial [functional dependency](/functional-dependency-discovery/) with one attribute on the right that holds in $r$.

10. • The query is $Q(x, z) \text{ :- } p(x, y), r(y, z)$ and the views are $V_1(a, b) \text{ :- } p(a, b)$, $V_2(a) \text{ :- } p(a, b), r(b, c)$, $V_3(b, c) \text{ :- } r(b, c)$ and $V_4(a, c) \text{ :- } p(a, b), r(b, c)$. Fill the buckets of the [bucket algorithm](/bucket-algorithm/), test the candidate rewritings, and give the maximally contained rewriting. Then list the MCDs of [MiniCon](/minicon-algorithm/) and explain why $V_2$ gives none.

11. • The source $V(a, c) \text{ :- } e(a, b), e(b, c)$ holds $\{(1, 3), (3, 5)\}$. Write the [inverse rules](/inverse-rules-algorithm/), derive the global facts, and give the certain answers of the queries "paths of length 2", "paths of length 4" and $Q(x, y) \text{ :- } e(x, y)$.

12. • The relation $\mathrm{Emp}(\mathit{id}, \mathit{name}, \mathit{dept})$ holds $t_1 = (1, \mathrm{ann}, \mathrm{sales})$ of weight 3, $t_2 = (2, \mathrm{ann}, \mathrm{hr})$ and $t_3 = (3, \mathrm{ann}, \mathrm{hr})$ of weight 2 each, and $t_4 = (4, \mathrm{bob}, \mathrm{it})$ and $t_5 = (5, \mathrm{bob}, \mathrm{ops})$ of weight 1 each, with the FD $\mathit{name} \to \mathit{dept}$. List the subset repairs and give the repairs of largest total weight. Which one does a cardinality repair choose for ann?

13. • $\mathrm{Emp}(\mathit{name}, \mathit{dept})$ has the key $\mathit{name}$ and holds (ann, sales), (ann, hr), (bob, hr), (bob, it) and (cat, it). How many repairs are there? Give the [consistent answers](/consistent-query-answering/) of $Q(x) \text{ :- } \mathrm{Emp}(x, \mathrm{hr})$, of the Boolean queries $\exists x\, \mathrm{Emp}(x, \mathrm{hr})$ and $\exists x\, \mathrm{Emp}(x, \mathrm{it})$, and of $Q(x) \text{ :- } \mathrm{Emp}(x, y)$.

14. • Compute the [core](/data-exchange-core-computation/) of the universal solution of exercise 7, and check that the four queries of that exercise have the same certain answers on it.

15. • On the solution of exercise 7, evaluate naively the Boolean query $\mathrm{Teaches}(t, \mathrm{db}) \wedge \mathrm{Teaches}(t', \mathrm{db}) \wedge t \ne t'$, treating nulls as distinct values. Give a solution in which the query is false, and say what this shows about naive evaluation.

16. • Records are sets of attribute values: $r_1 = \{N{:}\,\mathrm{ann}, E{:}\,e_1\}$, $r_2 = \{N{:}\,\mathrm{ann}, P{:}\,p_1\}$ and $r_3 = \{E{:}\,e_1, P{:}\,p_1\}$. Two records match when they share an $E$ value, or share both an $N$ value and a $P$ value, and a merge takes the union. Give the clusters of the transitive closure of pairwise matches. Then run [R-Swoosh](/r-swoosh/) in the order $r_1, r_2, r_3$, give its output, and count the match calls.

17. • For the relation of exercise 9, compute the agree set of every pair of rows. Use them to show that no nontrivial FD has $C$ on the right. For $A$ on the right, take the complements of the agree sets that miss $A$ and find their minimal hitting sets; do the same for $D$, and compare with exercise 9.

18. • Four sources claim values for four objects: $o_1$: $s_1, s_2, s_3$ say $a$ and $s_4$ says $b$; $o_2$: $s_1, s_2$ say $c$ and $s_3, s_4$ say $d$; $o_3$: $s_1$ says $e$ and $s_3, s_4$ say $f$; $o_4$: $s_2, s_3$ say $g$ and $s_4$ says $h$. Pick a value for each object by a plain vote. Then weight each source by $\ln(a_i/(1 - a_i))$ with accuracies $(0.9, 0.9, 0.6, 0.6)$, and pick again. Where do the two methods of [truth discovery](/truth-discovery/) disagree? With three independent sources each right with probability 0.8 on a yes-or-no question, how often is the majority right?

19. • The relation $R(A, B)$ holds $(a_1, b_1)$ of weight 2, $(a_1, b_2)$ of weight 3, $(a_2, b_1)$ of weight 2, $(a_2, b_2)$ of weight 1 and $(a_3, b_2)$ of weight 1, with the FDs $A \to B$ and $B \to A$. Find the subset repair of largest weight, and name the classical problem it is an instance of.

20. • For [schema matching](/schema-matching/) by name, score two names by $1 - d/\ell$, where $d$ is the edit distance and $\ell$ the length of the longer name. Fill the $3 \times 3$ table for the source names custname, phone and addr against the target names name, telephone and address, and find the one-to-one assignment of largest total score.

21. ★ [Compose](/schema-mapping-composition/) the mapping $\mathrm{Student}(s) \to \exists c\, \mathrm{Enr}(s, c)$ with the mapping $\mathrm{Enr}(s, c) \wedge \mathrm{Enr}(s', c) \to \mathrm{Classmates}(s, s')$. Write the composition as a second-order tgd with a function $f$, and then show that it is equivalent to the first-order tgd $\mathrm{Student}(s) \to \mathrm{Classmates}(s, s)$.

22. ★ Prove that the chase with full tgds, which have no existential variables, always stops, and bound the number of facts it can add by the active domain of the instance and the arities of the target relations. Why does the argument fail once a single tgd has an existential variable?

23. ★ Let $\mathrm{dom}(A) = \{\mathrm{true}, \mathrm{false}\}$ and take the CFDs $([A] \to [B], (\mathrm{true} \,\|\, b_1))$, $([A] \to [B], (\mathrm{false} \,\|\, b_2))$, $([B] \to [A], (b_1 \,\|\, \mathrm{false}))$ and $([B] \to [A], (b_2 \,\|\, \mathrm{true}))$. Show that no nonempty instance satisfies them. Then show that they become satisfiable when $\mathrm{dom}(A)$ is infinite, and explain why consistency of CFDs is harder than consistency of plain FDs.

24. ★ For a stripped partition $\hat\pi_X$, let $e(X) = \|\hat\pi_X\| - |\hat\pi_X|$. Prove that $e(X) = n - |\pi_X|$, where $\pi_X$ is the full partition of the $n$ rows by their values on $X$. Then prove the test of [TANE](/tane-algorithm/): $X \to A$ holds if and only if $e(X) = e(X \cup \{A\})$.
