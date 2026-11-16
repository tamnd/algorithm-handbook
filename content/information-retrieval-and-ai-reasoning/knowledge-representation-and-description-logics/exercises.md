1. ◦ Take the interpretation with domain $\{1, 2, 3, 4\}$, $r = \{(1, 2), (1, 3), (2, 4)\}$, $A = \{2, 4\}$ and $B = \{3\}$. Compute the extensions of the [ALC](/alc-description-logic/) concepts $\exists r.A \sqcap \forall r.(A \sqcup B)$, $\forall r.\bot$ and $\exists r.\exists r.A$.

2. ◦ Put $\neg\big(\exists r.(A \sqcap \forall s.\neg B) \sqcup \neg C\big)$ in negation normal form.

3. ◦ By [Schild's correspondence](/alc-modal-k-correspondence/) with one role $r$, write $\forall r.(A \sqcup \exists r.\neg B)$ as a formula of the modal logic K, and write $\Diamond\Box p \wedge \Box\Diamond\neg p$ as an ALC concept. Is that concept satisfiable?

4. ◦ The TBox is $\{\mathit{Parent} \equiv \mathit{Person} \sqcap \exists \mathit{hasChild}.\mathit{Person}\}$ and the ABox is $\{\mathit{Person}(\mathit{ann}), \mathit{hasChild}(\mathit{ann}, \mathit{bob})\}$. Under the [open-world assumption](/open-world-assumption/), does the knowledge base entail $\mathit{Parent}(\mathit{ann})$? Does it entail $\neg\mathit{Parent}(\mathit{ann})$? What changes when $\mathit{Person}(\mathit{bob})$ is added?

5. ◦ An ABox has $\mathit{hasChild}(m, a)$, $\mathit{hasChild}(m, b)$, $\mathit{hasChild}(m, c)$ and the inequality $a \ne b$, and the TBox is empty. What is the largest $n$ for which the number restriction $({\ge}\, n\ \mathit{hasChild})(m)$ is entailed without the [unique name assumption](/unique-name-assumption/), and what is it with the assumption?

6. ◦ A TBox has seven concept names and the six axioms $B_1 \sqsubseteq A$, $B_2 \sqsubseteq A$, $C_1 \sqsubseteq B_1$, $C_2 \sqsubseteq B_1$, $C_3 \sqsubseteq B_2$ and $C_4 \sqsubseteq B_2$. How many subsumption tests does brute-force [classification](/ontology-classification/) make? How many of them succeed, and how many edges does the hierarchy of direct subsumptions have?

7. ◦ Which of these axioms are in [DL-Lite](/dl-lite/)$_{\mathit{core}}$: (a) $A \sqsubseteq \exists r$; (b) $\exists r^- \sqsubseteq \neg B$; (c) $\exists r.A \sqsubseteq B$; (d) $A \sqcap B \sqsubseteq C$; (e) $A \sqsubseteq \exists r.B$? For the one that DL-Lite$_R$ can express with an extra role, show how.

8. ◦ In the [event calculus](/event-calculus/), $\mathit{Initiates}(\mathit{open}, \mathit{Open}, t)$ and $\mathit{Terminates}(\mathit{close}, \mathit{Open}, t)$ hold for all $t$, the narrative is $\mathit{InitiallyN}(\mathit{Open})$, $\mathit{Happens}(\mathit{open}, 2)$, $\mathit{Happens}(\mathit{close}, 6)$ and $\mathit{Happens}(\mathit{open}, 9)$, and circumscription makes these the only events and effects. Which of $\mathit{HoldsAt}(\mathit{Open}, t)$ and $\neg\mathit{HoldsAt}(\mathit{Open}, t)$ follows for $t = 1, 4, 7, 12$? What follows at $t = 1$ if $\mathit{InitiallyN}(\mathit{Open})$ is dropped?

9. ◦ Check that the circuit $\big(x_1 \wedge (x_2 \vee (\neg x_2 \wedge x_3))\big) \vee (\neg x_1 \wedge x_3)$ is a [d-DNNF](/d-dnnf/). Count its models over $\{x_1, x_2, x_3\}$ by the bottom-up pass, first without smoothing and then with it. Which count is right?

10. • Run the [tableau algorithm](/alc-tableau-algorithm/) on $\exists r.(A \sqcup B) \sqcap \forall r.(\neg A \sqcup C) \sqcap \forall r.(\neg B \sqcup C) \sqcap \forall r.\neg C$ with the empty TBox. Is it satisfiable, and how many nodes does the run create? Drop the conjunct $\forall r.\neg C$ and give a model of what remains.

11. • Let $\mathcal T = \{A \sqsubseteq \exists r.B,\ B \sqsubseteq \exists r.C,\ C \sqsubseteq \exists r.A,\ A \sqsubseteq \neg B,\ B \sqsubseteq \neg C,\ C \sqsubseteq \neg A\}$. Is $A$ satisfiable with respect to $\mathcal T$? How many nodes does the tableau with subset [blocking](/tableau-blocking/) expand before it blocks one, and what is the smallest model? What is the smallest model when $C \sqsubseteq \neg A$ is removed?

12. • Run the completion rules of [EL classification](/el-classification/) on the normalized TBox $A \sqsubseteq \exists r.B$, $B \sqsubseteq C$, $\exists r.C \sqsubseteq D$, $A \sqcap D \sqsubseteq E$, $E \sqsubseteq \exists s.A$, $\exists s.E \sqsubseteq H$. Give the set of subsumers of each name and the direct hierarchy.

13. • In [EL](/el-description-logic/) without a TBox, decide $\exists r.(A \sqcap \exists s.B) \sqsubseteq \exists r.A \sqcap \exists r.\exists s.B$ and the converse. For the one that fails, give a countermodel.

14. • Using the regularity condition of [SROIQ](/sroiq/), decide whether each RBox is regular: $R_1 = \{r \circ s \sqsubseteq r,\ s \circ s \sqsubseteq s\}$ and $R_2 = \{r \circ s \sqsubseteq t,\ t \circ r \sqsubseteq r\}$. In $R_1$, which of $r$ and $s$ may appear in a number restriction?

15. • A door has the [successor state axioms](/successor-state-axioms/) $\mathit{Open}(do(a, s)) \leftrightarrow a = \mathit{open} \vee (\mathit{Open}(s) \wedge a \ne \mathit{close})$ and $\mathit{Locked}(do(a, s)) \leftrightarrow a = \mathit{lock} \vee (\mathit{Locked}(s) \wedge a \ne \mathit{unlock})$, with $\mathit{Poss}(\mathit{open}, s) \leftrightarrow \neg\mathit{Locked}(s)$, $\mathit{Poss}(\mathit{lock}, s) \leftrightarrow \neg\mathit{Open}(s)$, and $\mathit{close}$ and $\mathit{unlock}$ always possible. Use [regression](/situation-calculus-regression/) to decide whether the sequence $\mathit{unlock}, \mathit{open}, \mathit{close}, \mathit{lock}$ is executable and ends with the door locked, and what the initial database must say for this. Is $\mathit{open}, \mathit{lock}$ executable from $\neg\mathit{Locked}(S_0)$?

16. • The action $\mathit{paint}(x, c)$ gives object $x$ the colour $c$, and an object has one colour at a time. Write the successor state axiom for $\mathit{Colour}(x, c, s)$, and check its consistency condition. After $\mathit{paint}(x, \mathit{red})$ and then $\mathit{paint}(x, \mathit{blue})$, does $\mathit{Colour}(x, \mathit{red})$ hold?

17. • Run the d-DNNF compiler (unit propagation, component split, branch on the most frequent variable, ties by index) on $(x_1 \vee x_2) \wedge (x_2 \vee x_3) \wedge (x_4 \vee x_5)$. Write the circuit, smooth it, and count the models over $x_1, \ldots, x_5$.

18. • Give the variables of exercise 9 the independent probabilities $P(x_1) = 0.2$, $P(x_2) = 0.5$ and $P(x_3) = 0.4$. Compute the probability that the circuit is true by one weighted pass, and say why the pass needs determinism.

19. • An application needs clause entailment, forgetting of variables and disjunction of any number of compiled forms. Using the tables of the [knowledge compilation map](/knowledge-compilation-map/), which languages support all three in polynomial time, and which would you pick? Which languages remain if model counting is also required?

20. • Give a smooth d-DNNF with $O(n)$ edges for the function that is true when exactly one of $x_1, \ldots, x_n$ is true, and count its models with the bottom-up pass.

21. • Build the compressed and trimmed [SDD](/sentential-decision-diagram/) of $(x_1 \wedge x_2) \vee (x_3 \wedge x_4)$ for the vtree $((x_1, x_3), (x_2, x_4))$. What is its size, and how does it compare with the size 8 on the vtree $((x_1, x_2), (x_3, x_4))$? Count its models with COUNT.

22. ★ With concept names $X_1, \ldots, X_n$ and one role $r$, write a TBox of size polynomial in $n$ such that $\mathit{Zero} = \neg X_1 \sqcap \cdots \sqcap \neg X_n$ is satisfiable but every model of it has at least $2^n$ elements. At what depth does the tableau with subset blocking first block a node on $\mathit{Zero}$?

23. ★ Let $D_{n+1} = \top$ and $D_i = \exists r.A_i \sqcap \exists r.\neg A_i \sqcap \forall r.D_{i+1}$, and $C_n = D_1$. How many nodes does the tableau without blocking or caching create on $C_n$, and how many does it keep at once when it explores depth first? How many elements has the smallest model of $C_n$?

24. ★ Let $\mathcal T = \{A \sqsubseteq \exists r,\ \exists r^- \sqsubseteq A\}$ in DL-Lite, and let $q_k$ be the Boolean query $\exists x_0 \cdots \exists x_k.\, r(x_0, x_1) \wedge \cdots \wedge r(x_{k-1}, x_k)$. For which ABoxes is $q_k$ entailed, for $k \ge 1$? Give one union of conjunctive queries that is a rewriting of every $q_k$, as [PerfectRef](/perfectref-rewriting/) would produce up to redundant disjuncts.

25. ★ For $f_k = (x_1 \wedge y_1) \vee \cdots \vee (x_k \wedge y_k)$ and the right-linear vtree on $x_1, \ldots, x_k, y_1, \ldots, y_k$, prove that the compressed and trimmed SDD has size $2^{k+2} - 2k - 4$.

26. ★ Take the door of exercise 15 with the initial database $\mathit{Open}(S_0) \vee \mathit{Locked}(S_0)$. Progress it through $\mathit{unlock}$ and then through $\mathit{close}$, that is, find the strongest statement that mentions only $S_1$, and then only $S_2$, and follows from the axioms and the initial database. Which transformation of the compilation map does progression of a propositional database need, and which languages of the map support it in polynomial time?
