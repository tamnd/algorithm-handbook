1. ◦ Let $\mathrm{Supplies}(S, P)$ hold $(s_1, p_1)$, $(s_1, p_2)$, $(s_2, p_1)$, $(s_3, p_1)$, $(s_3, p_2)$, $(s_3, p_3)$ and $\mathrm{Parts}(P)$ hold $p_1$ and $p_2$. Compute the [relational algebra](/relational-algebra/) expressions $(\pi_S(\mathrm{Supplies}) \times \mathrm{Parts}) - \mathrm{Supplies}$ and $\pi_S(\mathrm{Supplies}) - \pi_S\big((\pi_S(\mathrm{Supplies}) \times \mathrm{Parts}) - \mathrm{Supplies}\big)$. Which derived operator does the second expression compute?

2. ◦ Table $R(A)$ has the rows 1, 2 and NULL, and table $S(B)$ has the rows 2 and NULL. Under the [three-valued logic of SQL](/sql-null-semantics/), give the result of each query: (a) `SELECT COUNT(*) FROM R WHERE A <> 2`; (b) `SELECT A FROM R INTERSECT SELECT B FROM S`; (c) `SELECT A FROM R, S WHERE A = B`; (d) `SELECT SUM(A) FROM R WHERE A > 5`.

3. ◦ Relation $R(A, B, C, D, E)$ has the [functional dependencies](/functional-dependency/) $A \to B$, $BC \to D$, $D \to E$, $E \to A$. Find all its [candidate keys](/candidate-key/) with the [attribute closure](/attribute-closure-algorithm/). Is $R$ in [3NF](/third-normal-form/)? Is it in [BCNF](/boyce-codd-normal-form/)?

4. ◦ From $F = \{A \to B,\ B \to C,\ CD \to E\}$, derive $AD \to E$ with [Armstrong's axioms](/armstrongs-axioms/), naming the axiom used at each step. Does $F$ imply $A \to E$?

5. ◦ Compute a [minimal cover](/minimal-cover-problem/) of $F = \{A \to BC,\ B \to C,\ AB \to D\}$ over $ABCD$, doing the three steps in the usual order.

6. ◦ For each schema, give the highest of 1NF, 2NF, 3NF and BCNF that it satisfies: (a) $R(A, B, C, D)$ with $AB \to C$ and $C \to D$; (b) $R(A, B, C, D)$ with $AB \to C$ and $B \to D$; (c) $R(A, B, C)$ with $AB \to C$ and $C \to B$.

7. ◦ The relation $\mathrm{Emp}(E, C, S)$ of employees, children and skills holds $(e_1, c_1, s_1)$, $(e_1, c_2, s_2)$, $(e_1, c_1, s_2)$ and $(e_2, c_3, s_3)$. Which tuple must be added for the [multivalued dependency](/multivalued-dependency/) $E \twoheadrightarrow C$ to hold? After adding it, how many tuples do the two parts of the [4NF](/fourth-normal-form/) split on $E \twoheadrightarrow C$ hold together?

8. ◦ Run the [GYO reduction](/gyo-reduction/) on the hypergraph with edges $ABC$, $CDE$, $EFA$, $ACE$, and then on the hypergraph with edges $ABC$, $CDE$, $EFA$. Which of the two is [acyclic](/acyclic-hypergraph/)?

9. ◦ Annotate $R(A, B) = \{(1, a){:}\,p,\ (1, b){:}\,q,\ (2, a){:}\,r\}$ and $S(B) = \{(a){:}\,s,\ (b){:}\,t\}$ with variables. Compute the [provenance polynomial](/provenance-semirings/) of each answer of $\pi_A(R \bowtie S)$. Evaluate them as bag counts with $p = 2$, $q = 1$, $r = 1$, $s = 3$, $t = 1$, and give the [why-provenance](/why-and-where-provenance/) of the answer $(1)$.

10. • Decompose the relation of exercise 3 into BCNF with [BCNF decomposition](/bcnf-decomposition/), splitting first on $A \to B$ and then on $D$. Which dependency is lost? Then run [3NF synthesis](/third-normal-form-synthesis/) on the same dependencies, and say which of its schemas is not in BCNF.

11. • With the dependencies $A \to B$, $BC \to D$, $D \to E$, $E \to A$ over $ABCDE$, decide whether each split is a [lossless join decomposition](/lossless-join-decomposition/): (a) $AB$ and $ACDE$; (b) $ABC$ and $ADE$. For the lossy one, give a relation of two tuples that satisfies the dependencies and is not the join of its projections.

12. • Use the [tableau test](/lossless-join-test/) to decide whether the split of $R(A, B, C, D)$ into $AB$, $BC$, $CD$ is lossless (a) under $B \to C$ and $C \to D$, and (b) under $C \to B$ and $D \to C$. For the lossy case, read a counterexample relation off the final tableau.

13. • Decide which of these calculus queries are [domain independent](/domain-independent-query/): (a) $\{x \mid R(x) \land \neg S(x)\}$; (b) $\{x \mid \neg R(x)\}$; (c) $\{(x, y) \mid R(x) \lor S(y)\}$; (d) $\{x \mid \exists y\, R(x, y) \land \forall z\, (S(z) \to T(x, z))\}$. For each domain-independent one, give an equivalent algebra expression, as [Codd's theorem](/codds-theorem/) promises. Take care with (d) when $S$ is empty.

14. • [Minimize](/conjunctive-query-minimization/) the conjunctive query $Q(x) \leftarrow R(x, y), R(y, z), R(z, w), R(x, u), R(u, u)$. Give the homomorphism that shows the result is equivalent.

15. • Let $Q_m$ be the Boolean conjunctive query that asks whether a directed graph has a closed walk of length $m$. Using the [Chandra-Merlin theorem](/chandra-merlin-theorem/), decide which of $Q_3 \subseteq Q_6$, $Q_6 \subseteq Q_3$, $Q_3 \subseteq Q_4$ and $Q_4 \subseteq Q_3$ hold.

16. • On directed graphs, let $P$ be the Boolean union "there is a triangle or a loop", and $Q$ the union "there is a closed walk of length 6 or a cycle of length 2", each written as a union of two conjunctive queries. Use the [Sagiv-Yannakakis theorem](/sagiv-yannakakis-theorem/) to decide whether $P \subseteq Q$ and whether $Q \subseteq P$. For a containment that fails, give a graph that shows it.

17. • Run the program $\mathit{path}(x, y) \leftarrow e(x, y)$; $\mathit{path}(x, y) \leftarrow \mathit{path}(x, z), e(z, y)$ on a chain of $n$ nodes. Count the rule instances fired by naive evaluation, which runs until a round adds nothing, and by [semi-naive evaluation](/semi-naive-evaluation/), as closed forms in $n$. Check them against the counts 6 and 20 for $n = 4$ and 190 and 2660 for $n = 20$.

18. • A graph has the labelled edges $1 \xrightarrow{a} 2$, $2 \xrightarrow{a} 3$, $3 \xrightarrow{b} 4$, $2 \xrightarrow{b} 5$, $5 \xrightarrow{a} 1$ and $4 \xrightarrow{a} 4$. Evaluate the [regular path query](/regular-path-query/) for $a^{+} b$ with the automaton $s_0 \xrightarrow{a} s_1$, $s_1 \xrightarrow{a} s_1$, $s_1 \xrightarrow{b} s_2$ and final state $s_2$. Give all answer pairs and the number of edges of the product graph.

19. • Show that $Q_1(x) \leftarrow R(x, y)$ and $Q_2(x) \leftarrow R(x, y), R(x, z)$ are equivalent under set semantics. With $R = \{(1, a){:}\,p,\ (1, b){:}\,q\}$, compute the provenance polynomial of the answer $(1)$ under each query, and the bag counts when $p = q = 1$. What does this say about query equivalence and provenance?

20. • In a [tuple-independent probabilistic database](/probabilistic-database/), $R(a)$ and $R(b)$ have probability $1/2$; $S(a, 1)$ and $S(a, 2)$ have $1/2$ and $S(b, 1)$ has $1/4$; $T(a, 1)$ has $1/3$, and $T(b, 1)$ and $T(b, 2)$ have $1/2$. Compute exactly the probability of $\exists x\, \exists y\, \exists z\, (R(x) \land S(x, y) \land T(x, z))$. Then say which of these queries are hierarchical in the sense of the [Dalvi-Suciu dichotomy](/dalvi-suciu-dichotomy/): the query above, $R(x) \land S(x, y) \land T(y)$, and $R(x, y) \land S(y)$, each with its variables existentially quantified.

21. ★ Over $ABCD$, let $D = \{A \twoheadrightarrow BC,\ D \to C\}$. Use the [chase](/chase-algorithm/) to show that $D$ implies $A \to C$. Show that it does not imply $A \to B$, and give a counterexample relation with two tuples.

22. ★ Prove that a schema in 3NF all of whose candidate keys consist of one attribute is in BCNF. Show by an example from the entries that the condition on the keys cannot be dropped.

23. ★ Let $Q_2$ be a Boolean conjunctive query whose hypergraph is acyclic, and $Q_1$ any Boolean conjunctive query. Show that $Q_1 \subseteq Q_2$ can be decided in time polynomial in the sizes of $Q_1$ and $Q_2$, although containment of conjunctive queries is NP-complete in general.

24. ★ Let $H$ be the hypergraph on $\{A, B, C, D\}$ whose edges are the four sets of three vertices. Find its fractional edge cover number $\rho^*(H)$, its [hypertree width](/hypertree-width/) and its [fractional hypertree width](/fractional-hypertree-width/), and prove each value.

25. ★ Evaluate the nonlinear program $\mathit{path}(x, y) \leftarrow e(x, y)$; $\mathit{path}(x, y) \leftarrow \mathit{path}(x, z), \mathit{path}(z, y)$ on a chain of $n \ge 3$ nodes with the refined semi-naive method, which fires each true rule instance once. Show that it fires $\binom{n}{3} + n - 1$ instances, and that after the round of the exit rule exactly $\lceil \log_2 (n - 1) \rceil$ rounds derive new facts, against $n - 2$ rounds for the program of exercise 17.
