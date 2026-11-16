1. ◦ Take the framework with arguments $a, b, c, d, e$ and attacks $a \to b$, $b \to c$, $c \leftrightarrow d$ and $d \to e$. List its [admissible sets](/admissible-set/), its [complete extensions](/complete-extension/), its grounded extension, its [preferred extensions](/preferred-extension/) and its [stable extensions](/stable-extension-argumentation/).

2. ◦ Show that an argument is in every complete extension of a framework exactly when it is in the [grounded extension](/grounded-extension/). Does the same hold if "every" is replaced by "some"? Use the framework of exercise 1.

3. ◦ Take the arguments $a, \ldots, g$ with the attacks $a \to b$, $b \to c$, $c \to d$, $d \to e$, $b \to g$, $f \to e$ and $f \to f$. Compute $\emptyset, F(\emptyset), F^2(\emptyset), \ldots$ for the characteristic function $F$ until it stops, and give the grounded labelling. Then run the [counting algorithm](/grounded-extension-algorithm/): which arguments reach count 0, and which are left with no label at the end?

4. • Show that an argument is in some admissible set exactly when it is in some complete extension, and exactly when it is in some preferred extension. Which result of Dung's paper does the proof need?

5. • Take the framework $a \leftrightarrow b$, $b \to c$, $c \to c$, $d \to d$. Find its preferred, stable and [semi-stable extensions](/semi-stable-extension/), and give the range of each preferred extension. Which preferred extension is not semi-stable, and why?

6. • For the framework $a \leftrightarrow b$, $b \to c$, write the admissible [SAT encoding](/argumentation-sat-encoding/) with the variables $\mathit{in}_x$ and $\mathit{out}_x$. How many variables and clauses does it have? List the in parts of its models. Then decide with one more unit clause whether $c$ is in some preferred extension, and run the loop of calls that enumerates the preferred extensions, starting from the model $\{a\}$.

7. • Build the framework $F_\varphi$ of the standard reduction in [complexity of preferred semantics](/preferred-semantics-complexity/) for $\varphi = (x \vee y) \wedge (\neg x \vee \neg y) \wedge (x \vee \neg y)$. Count its arguments and attacks, and find all its preferred extensions. Which of them contains $\varphi$, and which assignment does it give?

8. ★ Let $\varphi$ be any CNF formula over the variables $X$, and $F_\varphi$ the framework of exercise 7. Prove that $F_\varphi$ has exactly $2^{|X|}$ preferred extensions, one for each assignment $\tau$: the literals true under $\tau$, the clauses false under $\tau$, and $\varphi$ when $\tau$ satisfies every clause. Show that all of them are stable.

9. ★ A framework is symmetric if $a \to b$ holds exactly when $b \to a$ holds, and here it also has no self-attack. Show that every conflict-free set is admissible, and that the preferred extensions are the stable extensions and are the maximal [independent sets](/independent-set/) of the undirected graph. Deduce that every argument is credulously accepted under preferred semantics, and that an argument is sceptically accepted exactly when it has no attacker.

10. ★ For any framework, form the undirected graph on the arguments with an edge between $a \ne b$ when one attacks the other. Show that each stable extension is a maximal independent set of this graph. A graph with $n$ vertices has at most $3^{n/3}$ maximal independent sets (Moon and Moser); deduce a bound on the number of stable extensions, and give a framework with $n = 3k$ arguments that reaches it. How many complete extensions does your framework have?

11. ◦ Write the normal logic program $p \leftarrow \mathit{not}\ q$, $q \leftarrow \mathit{not}\ r$, $r \leftarrow \mathit{not}\ p$ as an [assumption-based framework](/assumption-based-argumentation/) with the assumptions $\mathit{np}$, $\mathit{nq}$, $\mathit{nr}$. Which assumptions attack which? Find the grounded, preferred and stable extensions, and compare them with the [stable models](/stable-model-semantics/) and the [well-founded model](/well-founded-semantics/) of the program.

12. ◦ In [ASPIC+](/aspic-plus/), take the axiom $a$ and the defeasible rules $d_1: a \Rightarrow b$ and $d_2: a \Rightarrow \neg b$, with $b$ and $\neg b$ contradictories. List the arguments and the attacks. Give the grounded and preferred extensions with no preferences, and then with $d_1 < d_2$ under the last-link principle.

13. • In a [value-based framework](/value-based-argumentation/), let $A \leftrightarrow B$ and $B \to C$, where $A$ and $C$ promote the value red and $B$ promotes blue. For each of the two specific audiences, give the defeats that succeed and the preferred extension. Which arguments are objectively acceptable, and which only subjectively? Compare with the preferred extensions of the plain Dung framework.

14. ◦ Over the atoms $a$ and $b$, let $K = \mathrm{Cn}(a \wedge b)$. Revise $K$ by $\neg a \vee \neg b$ and by $\neg a$, first with [Dalal's operator](/dalal-revision/) and then with full meet revision.

15. ◦ Write a world over $a, b$ as the bit string $ab$, and take the [system of spheres](/grove-spheres/) $\{11\} \subset \{11, 01\} \subset \{11, 10, 01, 00\}$ around $K = \mathrm{Cn}(a \wedge b)$. Compute $K * \neg a$ and $K * \neg b$, and then $K \div a$ and $K \div b$ by the Harper identity $K \div p = K \cap (K * \neg p)$.

16. • Over the atoms $a$ and $b$, let $K = \mathrm{Cn}(a)$. Up to equivalence, list the sentences $p \in K$ that are not tautologies and the remainders $K \perp p$ of each, using the finite form of [partial meet contraction](/partial-meet-contraction/). How many partial meet contraction functions does $K$ have, and which of them satisfy K÷7 and K÷8?

17. • Let $K = \mathrm{Cn}(a \wedge b)$ and rank the worlds by their Hamming distance from $11$: $11$ has rank 0, $10$ and $01$ rank 1, $00$ rank 2. With the [entrenchment](/epistemic-entrenchment/) $E(p)$ given by the least rank of a model of $\neg p$, compute $E$ for $a$, $b$, $a \vee b$ and $a \wedge b$. Contract $K$ by $a$ and by $a \wedge b$ with the rule "$q$ stays when $p < p \vee q$". Then get $K * \neg a$ by the [Levi identity](/levi-identity/), and compare it with Dalal's revision.

18. • Fix a strict linear order $L$ on the worlds. Let $\psi \circ \mu$ be $\psi \wedge \mu$ when that is consistent, and otherwise the formula whose only model is the $L$-least model of $\mu$. Show that $\circ$ satisfies R1 to R6 by giving the faithful assignment of the [Katsuno and Mendelzon theorem](/katsuno-mendelzon-revision/). Show that each revision by a $\mu$ that contradicts $\psi$ gives a complete theory. Which kind of partial meet contraction gives revisions of this kind through the Levi identity?

19. ◦ Let $K = \mathrm{Cn}(q)$ and $K' = \mathrm{Cn}(q \wedge \neg p)$. Show that $K \subseteq K'$, and compute $K * p$ and $K' * p$ under full meet revision. Which condition of the [impossibility theorem of Gärdenfors](/gardenfors-impossibility-theorem/) fails, and why must it fail for every AGM revision of all the belief sets of a language with two or more atoms?

20. • Two switches are in the same state, $\psi = a \leftrightarrow b$, and then you learn $\mu = a$. Compute Dalal's revision, Forbus's update and the [PMA update](/possible-models-approach/). Which postulate of Katsuno and Mendelzon does the [update](/belief-update/) break here, and why is that the right answer if someone has just switched $a$ on?

21. ◦ Over $a, b$, take the [ranking](/ordinal-conditional-functions/) $\kappa(11) = 0$, $\kappa(10) = 2$, $\kappa(01) = 1$, $\kappa(00) = 3$. Compute the $(\neg a, 2)$-conditionalization and the revision by $\neg a$ of Darwiche and Pearl. What is the belief set after each, and how firmly is $\neg a$ held?

22. • Take $\kappa(11) = 0$, $\kappa(10) = 1$, $\kappa(01) = 1$, $\kappa(00) = 5$. Revise by $\neg a$ and then by $\neg b$, with the operator of Darwiche and Pearl, with natural revision and with lexicographic revision. Compare with revising by $\neg b$ alone. All three operators satisfy the [Darwiche and Pearl postulates](/darwiche-pearl-postulates/); why do C1 to C4 not decide this case?

23. ★ Show that the $(\mu, n)$-conditionalization of a ranking $\kappa$ always satisfies CR1 and CR2, and satisfies CR3 and CR4 whenever $n \ge \kappa(\neg \mu) - \kappa(\mu)$. What does this condition say when $\mu$ was not believed before, and when it was?

24. • Merge the profile of three copies of $a \wedge b \wedge c$ and one copy of $\neg a \wedge \neg b \wedge \neg c$, with no constraint, using the [Hamming distance](/hamming-distance/) and the sum, the maximum and Gmax. Describe each result in words.

25. ★ Show that the sum merging operator with the Hamming distance satisfies Maj with an explicit number of copies: over $N$ atoms, $\Delta_\mu(\Psi_1 \sqcup \Psi_2^n) \models \Delta_\mu(\Psi_2)$ for $n = |\Psi_1| \cdot N + 1$. Show that for the maximum, by contrast, $\Delta^{\max}_\mu(\Psi_1 \sqcup \Psi_2^n) = \Delta^{\max}_\mu(\Psi_1 \sqcup \Psi_2)$ for every $n \ge 1$.
