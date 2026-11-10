1. ◦ Name the smallest [SMT-LIB](/smt-lib/) logic for each formula: (a) $x - y \le 3 \wedge y - z \le -1$ over the integers; (b) $f(x) + 1 \le y$ over the integers with a free $f$; (c) $\mathrm{bvadd}(x, y) = 0$ on 8-bit words; (d) $\mathrm{select}(\mathrm{store}(a, i, v), j) = w$ with free index and element sorts.

2. ◦ Run [congruence closure](/congruence-closure/) on the equations $a = b$, $f(a) = c$ and the disequality $g(f(b)) \ne g(c)$. List the final classes of the subterms and decide the conjunction.

3. ◦ Draw the constraint graph of the [difference logic](/difference-logic-satisfiability/) atoms $a - b \le 2$, $b - c \le -1$, $c - a \le -2$, $c - d \le 0$, $d - a \le 1$, with an edge from $y$ to $x$ of weight $c$ for each atom $x - y \le c$. Find a negative cycle and the conflict clause that a solver learns from it.

4. ◦ Over 4-bit [bit-vectors](/bit-vector-satisfiability/), find all $x$ with $\mathrm{bvneg}(x) = x$, and all $x$ with $3x = 1$ modulo $2^4$.

5. ◦ In the [theory of arrays](/array-theory-satisfiability/), is $\mathrm{select}(\mathrm{store}(a, i, 5), j) = 3 \wedge \mathrm{select}(a, j) = 3$ satisfiable? What if $i = j$ is added?

6. ◦ Apply [Ackermannization](/ackermannization/) to $f(f(x)) \ne f(x) \wedge f(x) = x$ and decide the result. How many functional consistency constraints does a formula with 5 applications of $f$ and 3 applications of $g$ need?

7. ◦ The theory of 3-bit bit-vectors is not [convex](/convex-theory/). What is the least number $k$ such that the empty conjunction entails the disjunction of all equalities between $k$ constants? Does it entail any single one of them?

8. ◦ A simplex solver for SMT replaces the strict bounds of $2 < x < 3$, $y > 2$, $x + y \le 5$ by bounds with an infinitesimal $\delta$. Check that $x = y = 2 + \delta$ meets all bounds. For which rational values $\delta_0 > 0$ does it give a real model?

9. • Over the integers, let $\varphi = (x \le 2 \vee x \ge 5) \wedge x \ge 3 \wedge x \le 6$. Write its [Boolean abstraction](/boolean-abstraction/) with atoms $p_1, \ldots, p_4$ in order of appearance and list the models of the abstraction. Which of them are consistent in the theory? Give one theory lemma of two literals that blocks all the inconsistent ones.

10. • Decide $(a = b \vee a = c) \wedge b = d \wedge f(a) \ne f(d) \wedge f(c) = f(b)$ in [EUF](/euf-satisfiability/) by splitting on the disjunction. Give the congruence step that closes each case.

11. • Purify $1 \le x \le 2 \wedge f(x) \ne f(1) \wedge f(x) \ne f(2)$ into an integer part and an EUF part with new constants $c_1 = 1$ and $c_2 = 2$. Which disjunction of equalities between the shared constants does the integer part entail? Run [Nelson-Oppen](/nelson-oppen/) with case splits and decide the formula. What changes over the reals?

12. • [Bit-blast](/bit-blasting/) the equality $x = y$ of two 8-bit words in two ways: as a constraint at the top level, and as a gate whose output is used under a disjunction, with one XNOR gate per bit and one AND gate. Count the clauses and new variables of each.

13. • Use the [omega test](/omega-test/) to eliminate $z$ from $3z \ge y$, $2z \le y + 1$, $-3 \le y \le -2$. Compute the real shadow and the dark shadow and decide each. Which splinters must be tried, and what integer solution do they give?

14. • Over the reals, the assertions are $A: x > 5$, $B: y < 2$, $C: x + y = 3$, $D: x < 10$, $E: y > 0$. Find every minimal [unsat core](/unsat-core/), every minimal correction set, and the largest number of assertions that can hold together.

15. • Run [CEGIS](/cegis/) for $f(x) = a x + b$ with $a, b \in \{0, 1, 2, 3\}$ and the specification $f(x) = 2x + 1$ for all $x \in \{0, \ldots, 15\}$. The first example is $x = 0$, the synthesizer returns the smallest $a$ and then the smallest $b$ that fit the examples, and the verifier returns the smallest counterexample. Give each round.

16. • In integer difference logic, show that $0 \le x - z \le 1 \wedge y - z = 0 \wedge w - z = 1$ entails $x = y \vee x = w$ but neither equality alone. Is the disjunction entailed over the reals?

17. • A congruence closure solver holds $e_1: a = b$, $e_2: b = c$, $e_3: c = d$, $e_4: f(a) = x$, $e_5: f(d) = y$ and derives $x = y$. Which input equations form the [explanation](/theory-conflict-explanation/)? If $e_6: a = d$ is also asserted, what smaller explanation exists?

18. ★ Show that $\exists y\, (3y \le x < 3y + 2)$ is equivalent to a quantifier-free [Presburger](/presburger-arithmetic/) formula in $x$ with a divisibility or congruence atom, and give that formula.

19. ★ Show that $f^6(a) = a \wedge f^{10}(a) = a$ entails $f^2(a) = a$ in EUF. Run congruence closure on the terms $a, f(a), \ldots, f^{10}(a)$ and give the sizes of the final classes. Give a model in which $f(a) \ne a$, to show that $f(a) = a$ is not entailed.

20. ★ For $\varphi = \exists^{[-1, 1]} x\, (x^2 + 1 = 0)$, find every $\delta \ge 0$ for which the δ-weakening of $\varphi$ is true. Which answers may a [δ-complete](/delta-satisfiability/) solver give for $\delta = 1/2$, and which for $\delta = 1$?

21. ★ In union by size, the smaller class is relabelled at each merge. Show that for $n$ a power of two the largest total number of relabellings over all sequences of $n - 1$ merges is $(n/2) \log_2 n$, and give a merge order that reaches it.

22. ★ Over the reals and over the integers, decide $x - y \le 0 \wedge y - x \le 0 \wedge x + y = 1$. Explain why the argument that a difference logic conjunction with integer constants has an integer model, if it has a real one, does not apply here.
