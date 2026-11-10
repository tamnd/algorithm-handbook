1. ◦ Let $M$ be the [Kripke structure](/kripke-structure/) with states $0, 1, 2, 3$, initial state $0$, transitions $0 \to 1$, $0 \to 2$, $1 \to 0$, $1 \to 3$, $2 \to 2$, $3 \to 3$, and labels $L(0) = \emptyset$, $L(1) = \{p\}$, $L(2) = \{q\}$, $L(3) = \{p, q\}$. Compute the sets of states that satisfy the [CTL](/computation-tree-logic/) formulas $\mathsf{EX}\,q$, $\mathsf{AX}\,p$, $\mathsf{AF}\,q$ and $\mathsf{EG}\,\neg q$. For $\mathsf{EG}\,\neg q$, list the iterates of the greatest fixed point.

2. ◦ In the structure $M$ of Exercise 1, decide whether the initial state satisfies the [LTL](/linear-temporal-logic/) formulas $\mathsf{F}\,q$, $\mathsf{G}\mathsf{F}\,p$ and $\mathsf{G}(q \to \mathsf{G}\,q)$. For each formula that fails, give a counterexample as a lasso, a finite stem followed by a loop.

3. ◦ Classify each property of infinite words as a [safety property](/safety-property/), a [liveness property](/liveness-property/) or neither: $\mathsf{G}\,\neg(c_1 \wedge c_2)$; $\mathsf{G}(\mathit{req} \to \mathsf{F}\,\mathit{grant})$; $\mathsf{X}\,p$; $\mathsf{F}\,p \wedge \mathsf{G}\,q$.

4. ◦ Write "every request is eventually granted" in LTL and in CTL, "from every reachable state a reset state can be reached" in CTL, and "from some point on the system stays stable" in LTL.

5. ◦ A system has 8 processes with 6 local states each and two shared Boolean variables. What upper bound on the number of global states does the [state explosion](/state-explosion-problem/) argument give?

6. ◦ Structure $A$ has a state $a_0$ with label $\emptyset$ and transitions to $a_1$ and $a_2$, both labelled $\{p\}$ and each with a self-loop. Structure $B$ has $b_0$ with label $\emptyset$ and one transition to $b_1$, labelled $\{p\}$ with a self-loop. Are $a_0$ and $b_0$ [bisimilar](/bisimulation/)? Give the relation or a distinguishing formula.

7. ◦ A 3-bit counter starts at $000$ and adds 1 modulo 8 at each step. What is the smallest bound $k$ for which [bounded model checking](/bounded-model-checking/) finds a counterexample to $\mathsf{G}\,\neg(x = 111)$? What is the diameter of the system?

8. ◦ How many independent simulation runs does the Hoeffding bound of [statistical model checking](/statistical-model-checking/), $N = \lceil \ln(2/\delta) / (2\varepsilon^2) \rceil$, require for $\varepsilon = 0.01$ and $\delta = 0.05$?

9. • Give a Büchi automaton with two states for $\neg\mathsf{G}(p \to \mathsf{F}\,q)$. Build the part of its product with the structure $M$ of Exercise 1 that is reachable from the initial state, and use it to decide whether $M$ satisfies $\mathsf{G}(p \to \mathsf{F}\,q)$, as in the [automata-theoretic approach](/automata-theoretic-approach/).

10. • Run [nested depth-first search](/nested-depth-first-search/) on the graph with initial state 1, edges $1 \to 2$, $2 \to 3$, $2 \to 4$, $3 \to 1$, $4 \to 4$, accepting set $\{2\}$, and successors taken in increasing order. In what order do the states finish in the first search, when does the second search start, and which lasso is reported? Which lasso is reported if the accepting set is $\{4\}$ instead?

11. • In the structure $M$ of Exercise 1, add the [fairness](/fairness/) constraint that $q$ holds infinitely often. Which states are fair, and does the initial state satisfy $\mathsf{AF}\,q$ under fairness? Then use the two constraints "infinitely often $p$" and "infinitely often $q$" together, and find the fair states with the strongly connected components.

12. • A Kripke structure has states $1$ to $6$, with $L(3) = L(4) = L(6) = \{p\}$ and the other labels empty, and transitions $1 \to 3$, $2 \to 4$, $2 \to 5$, $3 \to 3$, $4 \to 4$, $5 \to 6$, $6 \to 6$. Compute the coarsest bisimulation by partition refinement and count the states of the quotient. Does state 2 [simulate](/simulation-relation/) state 1? Does state 1 simulate state 2?

13. • Evaluate the [mu-calculus](/modal-mu-calculus/) formula $\nu Z.\, \mu Y.\, \big((p \wedge \mathsf{EX}\,Z) \vee \mathsf{EX}\,Y\big)$ on the structure $M$ of Exercise 1 by nested iteration, starting the outer iteration from all states. How many outer iterations are needed, and which CTL* formula does it express?

14. • A Markov chain has states $s_0, s_1, s_2, s_3$; $s_0$ moves to $s_1$ and to $s_2$ with probability $\tfrac12$ each, $s_2$ moves to $s_0$ and to $s_3$ with probability $\tfrac12$ each, and $s_1$ and $s_3$ are absorbing. Only $s_1$ is labelled $\mathit{goal}$. Compute the probability of $\mathsf{F}\,\mathit{goal}$ from $s_0$ as in [PCTL model checking](/pctl-model-checking/), and decide $\mathsf{P}_{\ge 0.6}[\mathsf{F}\,\mathit{goal}]$ and $\mathsf{P}_{\ge 0.7}[\mathsf{F}\,\mathit{goal}]$.

15. • Write the zone $1 \le x \le 3$, $y \ge 0$, $y - x \le 1$ as a [difference bound matrix](/difference-bound-matrix/) and bring it to canonical form. What are the tightest bounds on $y$ and on $x - y$? Show with the matrix that adding $y \ge 5$ gives the empty zone.

16. • An integer variable $x$ starts at 0, each step sets $x$ to $x + 2$, and the bad states are those with $x = 1$. With the single predicate $x = 1$, compute the abstraction, find the abstract counterexample, and show that it is spurious. Show that adding the predicate $x \ge 0$, as a [CEGAR](/cegar/) refinement could, proves the property.

17. • A [Petri net](/petri-net/) has places $p_1, p_2, p_3$, initial marking $(1, 0, 0)$, a transition $t_1$ that moves the token from $p_1$ to $p_2$, and a transition $t_2$ that takes a token from $p_2$ and puts one in $p_1$ and one in $p_3$. Build the [Karp-Miller tree](/karp-miller-tree/). Which places are bounded? Is $(0, 1, 5)$ coverable, and is $(1, 1, 0)$? What is the exact set of reachable markings?

18. • A [pushdown system](/pushdown-system/) has control states $p, q$, stack symbols $a, b$ and the rules $\langle p, a\rangle \to \langle p, aa\rangle$, $\langle p, a\rangle \to \langle q, \varepsilon\rangle$, $\langle q, a\rangle \to \langle q, \varepsilon\rangle$ and $\langle q, b\rangle \to \langle p, a\rangle$. Is $\langle q, \varepsilon\rangle$ reachable from $\langle p, ab\rangle$? Describe the set of configurations reachable from $\langle p, ab\rangle$ as a regular set.

19. • A system has a counter $x \in \{0, \ldots, 7\}$ that starts at 0 and adds 2 modulo 8 at each step. Show that the property $x \ne 5$ is [4-inductive](/k-induction/) but not 3-inductive, in the sense that $P$ on $j$ consecutive states implies $P$ on the next one. Give a 1-inductive invariant that implies the property.

20. ★ Count the clock regions of two clocks $x$ and $y$ whose largest constant is 1, and compare the count with the bound of the [region graph](/region-graph/) entry.

21. ★ A [parity game](/parity-game/) has vertices $0$ to $4$, where vertex $v$ has priority $v$; player 0 owns vertices 0, 1 and 4 and player 1 owns vertices 2 and 3. The edges are $0 \to 3$, $1 \to 1$, $1 \to 4$, $2 \to 3$, $3 \to 1$, $3 \to 3$ and $4 \to 1$. Player 0 wins a play when the largest priority seen infinitely often is even. Run [Zielonka's algorithm](/zielonka-algorithm/), listing each attractor it computes, and give the winning regions and positional winning strategies.

22. ★ A labelled transition system is deterministic when each state has at most one $a$-successor for each action $a$. Prove that two states of a deterministic system are [trace equivalent](/trace-equivalence/) if and only if they are bisimilar.

23. ★ Prove that on a finite Kripke structure the set of states satisfying $\mathsf{E}[p\, \mathsf{U}\, q]$ is the least fixed point of $\tau(Z) = q \vee (p \wedge \mathsf{EX}\,Z)$, and that the greatest fixed point of the same $\tau$ is the set of states satisfying $\mathsf{E}[p\, \mathsf{U}\, q] \vee \mathsf{EG}\,p$. Give a structure with one state on which the two fixed points differ.
