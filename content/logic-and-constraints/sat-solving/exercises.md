1. ◦ Write the formula $(x_1 \vee \neg x_2) \wedge (\neg x_1 \vee x_2 \vee x_3) \wedge \neg x_3$ in the [DIMACS CNF format](/dimacs-cnf-format/), header line included.

2. ◦ Run [unit propagation](/unit-propagation/) on $(x_1) \wedge (\neg x_1 \vee x_2) \wedge (\neg x_2 \vee \neg x_3 \vee x_4) \wedge (\neg x_2 \vee x_3) \wedge (\neg x_4 \vee x_5 \vee \neg x_1)$. In what order are the variables set, and does propagation alone decide the formula?

3. ◦ Build the implication graph of the [2-SAT](/2-sat/) formula $(x_1 \vee x_2) \wedge (\neg x_1 \vee x_3) \wedge (\neg x_2 \vee \neg x_3) \wedge (x_2 \vee x_3)$. List its strongly connected components, decide the formula, and list all its models.

4. ◦ Find the least model of the [Horn](/horn-sat/) formula $(x_1) \wedge (\neg x_1 \vee x_2) \wedge (\neg x_2 \vee \neg x_3 \vee x_4) \wedge (\neg x_1 \vee \neg x_2 \vee x_3) \wedge (\neg x_4 \vee \neg x_5) \wedge (\neg x_5 \vee x_1)$ by forward chaining. What happens when the unit clause $(x_5)$ is added?

5. ◦ The models of a Horn formula are closed under the bitwise AND of two models. Use this to show that the clause $(x_1 \vee x_2)$ is equivalent to no Horn formula over $x_1, x_2$.

6. ◦ Solve the [XOR-SAT](/xor-sat/) system $x_1 \oplus x_2 \oplus x_3 = 1$, $x_2 \oplus x_4 = 0$, $x_1 \oplus x_3 \oplus x_4 = 1$, $x_1 \oplus x_2 = 1$ over GF(2). What is the rank, and how many solutions are there? How many clauses does the direct CNF of the system have, with $2^{j-1}$ clauses for an XOR of $j$ variables?

7. ◦ The pigeonhole formula for 5 pigeons and 4 holes has a variable $p_{ih}$ for "pigeon $i$ sits in hole $h$", a clause saying that each pigeon sits somewhere, and a clause $(\neg p_{ih} \vee \neg p_{jh})$ for each hole and each pair of pigeons. Count its variables and its clauses of each width.

8. ◦ Count the models of $(x_1 \vee x_2) \wedge (x_3 \vee x_4) \wedge (\neg x_1 \vee \neg x_3)$ by splitting on $x_1$.

9. ◦ Decide the two [quantified Boolean formulas](/qbf/) $\forall x\, \exists y\, (x \vee y) \wedge (\neg x \vee \neg y)$ and $\exists y\, \forall x\, (x \vee y) \wedge (\neg x \vee \neg y)$. Which is true?

10. ◦ Let $F = (x_1 \vee x_2) \wedge (\neg x_1 \vee x_2)$. Is the clause $(x_2)$ a RUP clause for $F$, in the sense of [DRAT](/drat-proof/)? Is $(x_1)$?

11. • Let $\varphi = (x_1 \wedge x_2 \wedge \neg x_3) \vee (x_3 \wedge x_4) \vee \neg x_1$, with one gate for each AND and one for the OR, and negations kept on the literals. Count the variables, clauses and literal occurrences of its [Tseitin CNF](/tseitin-transformation/), with the unit clause on the output. Do the same for the [Plaisted-Greenbaum](/plaisted-greenbaum-transformation/) CNF.

12. • Split the clause $(\ell_1 \vee \cdots \vee \ell_6)$ into 3-clauses with new variables $y_1, y_2, y_3$ as in the reduction of [3-SAT](/3-sat/). How many clauses are there? When all six literals are true, how many settings of $y_1, y_2, y_3$ satisfy the split? When only $\ell_1$ is true? Is the reduction parsimonious?

13. • Eliminate $x$ from $(x \vee a \vee b) \wedge (x \vee \neg a) \wedge (\neg x \vee a) \wedge (\neg x \vee c)$ by [bounded variable elimination](/bounded-variable-elimination/). List the resolvents, drop tautologies and subsumed clauses, and compare the clause counts. Then extend the model $a = 1, b = 0, c = 1$ of the result to $x$.

14. • Take the clauses $C_1 = (\neg x_1 \vee x_2)$, $C_2 = (\neg x_2 \vee x_3)$, $C_3 = (\neg x_3 \vee \neg x_6 \vee x_4)$, $C_4 = (\neg x_3 \vee x_5)$, $C_5 = (\neg x_4 \vee \neg x_5)$, the decision $x_6 = 1$ at level 1 and the decision $x_1 = 1$ at level 2. Draw the [implication graph](/implication-graph/) up to the conflict. Find the [first UIP](/first-uip/), the learned clause, its literal block distance and the backjump level. Which literals does propagation set after the backjump? What clause would the decision cut give instead?

15. • Run one flip of [WalkSAT](/walksat/) on the formula of exercise 3 from the assignment $x_1 = x_2 = x_3 = 0$. Which clauses are false? For each false clause, give the break counts of its variables and the flips that WalkSAT may make. If the false clause is chosen uniformly, what is the probability that this one flip reaches a model?

16. • Apply the method of conditional expectations to the [MaxSAT](/max-sat/) instance $(x_1 \vee x_2 \vee x_3) \wedge (\neg x_1 \vee x_2) \wedge (\neg x_1 \vee \neg x_2) \wedge (x_1 \vee \neg x_3) \wedge (\neg x_2 \vee x_3)$. Fix $x_1$, then $x_2$, then $x_3$, breaking ties towards true. What is the expected number of true clauses at the start, and how many clauses does the result satisfy? Is that optimal?

17. • A random 3-CNF formula has $n = 100$ variables and $m$ clauses, each with three distinct variables and random signs. Write the expected number of models. Evaluate it at $m = 500$ and find the least $m$ for which it is below 1. Compare that ratio $m/n$ with the limit of the first-moment bound and with the predicted [threshold](/satisfiability-threshold/).

18. • A formula has exactly $k = 5$ literals in each clause, and each variable occurs in at most $t$ clauses. Use the local lemma condition $e \cdot 2^{-k}(d + 1) \le 1$ to find the largest $t$ that guarantees a model. What largest $d$ does the condition allow for $k = 3$?

19. • Let $F$ be $(x_1 \vee \neg x_2) \wedge (x_2 \vee x_3) \wedge (\neg x_3 \vee x_1)$ together with the four clauses $(x_4 \vee x_5)$, $(x_4 \vee \neg x_5)$, $(\neg x_4 \vee x_5)$, $(\neg x_4 \vee \neg x_5)$. Is $\{x_1 = 1\}$ an [autarky](/autarky/)? Is $\{x_3 = 1\}$? Which variables can the largest autarkies assign, and which clauses form the lean kernel?

20. • The [sequential counter](/sequential-counter-encoding/) for "at most $k$ of $n$" uses $k(n - 1)$ new variables and $2nk + n - 3k - 1$ clauses. For at most one, from which $n$ does it use fewer clauses than the pairwise encoding? For $n = 8$ and $k = 2$, compare it with the encoding that forbids every set of three true inputs.

21. ★ A formula is renamable Horn if flipping the signs of some variables makes it Horn. Write the 2-SAT conditions on the flip variables $s_1, s_2, s_3$ for $(x_1 \vee x_2 \vee x_3) \wedge (\neg x_1 \vee x_2) \wedge (\neg x_2 \vee \neg x_3 \vee x_1)$, and find every renaming that works.

22. ★ The Tseitin formula of a graph has one variable per edge and, for each vertex, the constraint that the XOR of its edges equals the vertex charge. For $K_4$ with charges $(1, 0, 0, 0)$, count the variables and the clauses, and decide the formula. How many models are there with charges $(1, 1, 0, 0)$?

23. ★ Name the clauses $a = (x)$, $b = (\neg x)$, $c = (y)$, $d = (\neg y \vee \neg x)$, $e = (\neg y)$. Find all [minimal unsatisfiable subsets](/minimal-unsatisfiable-subset/) and all [minimal correction subsets](/minimal-correction-subset/), and check that each family is the set of minimal hitting sets of the other. What is the MaxSAT value?

24. ★ Let $A_n = (x_1) \wedge (\neg x_1 \vee x_2) \wedge \cdots \wedge (\neg x_{n-1} \vee x_n) \wedge (\neg x_n)$. Show that $A_n$ is minimally unsatisfiable and that every resolution refutation of it has at least $n$ resolution steps. Show that $n$ steps suffice.
