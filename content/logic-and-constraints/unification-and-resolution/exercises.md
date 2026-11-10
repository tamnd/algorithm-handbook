1. ◦ Which of these propositional clauses are [Horn clauses](/horn-clause/): $\neg P \vee \neg Q \vee R$, $\neg P \vee \neg Q$, $R$, $P \vee Q$, $\neg P \vee Q \vee R$? For each Horn clause, say whether it is a fact, a rule or a goal clause.

2. ◦ Let $\sigma = \{x \mapsto g(y, z),\ z \mapsto b\}$ and $\theta = \{y \mapsto a,\ z \mapsto c\}$. Compute the compositions $\sigma\theta$ and $\theta\sigma$, where $\sigma\theta$ applies $\sigma$ first, and apply both to $h(x, z)$. Is $\sigma$ [idempotent](/idempotent-substitution/)?

3. ◦ Find a [most general unifier](/most-general-unifier/) of $q(x, y)$ and $q(y, f(z))$, and give a unifier of the two terms that is not most general. Then show that $f(x, x)$ and $f(y, g(y))$ have no unifier, and name the step where the attempt fails.

4. ◦ Put $\neg \exists x\, (P(x) \to \forall y\, Q(x, y))$ into [prenex normal form](/prenex-normal-form/), [Skolemize](/skolemization/) it, and write the resulting set of clauses.

5. ◦ The clause $\neg P(x) \vee Q(g(x, x))$ has no constant, so its [Herbrand universe](/herbrand-universe/) is built from a new constant $c$ and the function symbol $g$. How many terms of the universe have depth at most 2, where $c$ has depth 0?

6. ◦ Compute the [binary resolvent](/binary-resolution/) of $P(x, a) \vee Q(x)$ and $\neg P(b, y) \vee R(y)$, with the most general unifier that it uses.

7. ◦ Compute the [least general generalization](/plotkin-lgg/) of $f(a, g(a))$ and $f(b, g(b))$, and of $f(a, a)$ and $f(b, c)$.

8. ◦ For each pair, decide whether the first clause [subsumes](/subsumption/) the second: $P(x, y)$ and $P(a, b) \vee Q$; $P(x, x)$ and $P(a, b) \vee P(b, a)$; $P(x, y) \vee P(y, x)$ and $P(a, a)$.

9. ◦ Refute $\{f(x) = x,\ P(f(f(c))),\ \neg P(c)\}$ with [paramodulation](/paramodulation/) and binary resolution. How many inferences does the refutation take?

10. ◦ The set $S = \{P(x),\ \neg P(f(x)) \vee Q,\ \neg Q\}$, where $Q$ is a nullary predicate, is unsatisfiable. Following [Herbrand's theorem](/herbrand-theorem/), give a finite unsatisfiable set of ground instances of $S$ with as few clauses as possible.

11. • Run the [Martelli-Montanari](/martelli-montanari-unification/) rules on $f(x, h(y), y) \doteq f(g(z), h(x), w)$. Name the rule used at each step and give the solved form.

12. • Unify $f(x, y)$ and $f(y, g(x))$ with union-find on the [term DAG](/term-dag/), as in [Huet's algorithm](/huet-unification/). List the classes after all merges, and show where the final cycle test fails. At which step would [Robinson's algorithm](/robinson-unification/) fail on the same pair?

13. • The program `e(a, b). e(b, c). path(X, Y) ← path(X, Z), e(Z, Y). path(X, Y) ← e(X, Y).` uses left recursion. What does Prolog, with leftmost selection and depth-first search in program order, do on the query `← path(a, W)`? What happens when the two `path` clauses are swapped? Which answers does a breadth-first search of the [SLD tree](/sld-resolution/) find?

14. • For the program `p(X) ← q(X), r(X). q(a). q(b). r(b).` and the query `← p(X)`, draw the SLD tree under the leftmost and under the rightmost selection rule. Count the nodes and the failure leaves of each tree, and check that both give the same [computed answer](/answer-substitution/).

15. • Run [SLDNF resolution](/sldnf-resolution/) on the normal program `p ← not q. q ← not r. r.` with the query `← p`. Does it succeed? Write the completion of the program and check the answer against it.

16. • Saturate the definite program `p(a). q(b). r(X) ← p(X). r(X) ← q(X). s(X) ← r(X), p(X).` with [hyperresolution](/hyperresolution/), using in each round all positive clauses found so far. How many rounds produce new clauses, and what is the least Herbrand model?

17. • The set $\{P \vee Q,\ P \vee \neg Q,\ \neg P \vee R,\ \neg P \vee \neg R\}$ is unsatisfiable. Show that it has no [input refutation](/input-resolution/), and give a [linear refutation](/linear-resolution/) with top clause $P \vee Q$.

18. • Take the atom order $P \succ Q \succ R$, with $\neg A \succ A$ for each atom. List every inference that [ordered resolution](/ordered-resolution/) allows on $\{P \vee Q,\ \neg P \vee Q,\ \neg Q \vee R,\ \neg R\}$ until it stops. How many binary resolvents does unrestricted resolution form from the four input clauses alone?

19. • Modulo AC, the elementary problem $x + y + y \doteq z + z + z$ leads to the linear Diophantine equation $x' + 2y' = 3z'$. Find all its minimal nonzero solutions in the natural numbers, and count the unifiers that [Stickel's algorithm](/stickel-ac-unification/) builds from them.

20. • Solve the [nominal unification](/nominal-unification-problem/) problem $[a][b]f(a, X) \approx^? [b][a]f(Y, a)$, where $a$ and $b$ are distinct atoms. Check the solution by writing out both sides.

21. • Decide whether each inequation is [semi-unifiable](/semi-unification-problem/), and whether the corresponding equation is unifiable: $f(x, y) \le f(g(y), g(x))$ and $f(x, g(x)) \le f(g(y), y)$.

22. • Which of $\lambda x y.\, F(x, y)$, $\lambda x y.\, F(y)$, $\lambda x.\, F(x, x)$, $\lambda x.\, F(g(x))$ and $\lambda x.\, F(a)$ are [patterns](/pattern-unification-problem/)? Then solve $\lambda x y z.\, F(x, y) \doteq \lambda x y z.\, G(z, x)$, and show that $\lambda x.\, F(x) \doteq \lambda x.\, g(F(x))$ has no solution.

23. ★ Show that $x + y \doteq z + w$ has exactly 7 unifiers in its minimal complete set modulo AC, and exactly 2 modulo commutativity alone.

24. ★ Modulo associativity alone, with free constants $a, b, c, d$, find a minimal complete set of unifiers of $x \cdot y \cdot z \doteq a \cdot b \cdot c \cdot d$, and of $x \cdot b \doteq a \cdot y$. Prove that the second set is complete.

25. ★ With constants $a : \iota$ and $g : \iota \to \iota \to \iota$, count the solutions of the [second-order](/second-order-unification-problem/) problem $F(a, a) \doteq g(a, a)$ with $F : \iota \to \iota \to \iota$. Then show that $F(F(a)) \doteq g(a, a)$ with $F : \iota \to \iota$ has exactly one solution.

26. ★ Testing whether one clause subsumes another is NP-complete. Show that it takes polynomial time when no two literals of the subsuming clause $C$ share a variable, and give a bound on the number of matching calls in terms of the numbers of literals of $C$ and $D$.
