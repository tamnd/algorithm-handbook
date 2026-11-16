## What to remember

- **Calculi.** A [qualitative calculus](/qualitative-constraint-calculus/) has jointly exhaustive, pairwise disjoint base relations, an identity, a converse and a [composition table](/composition-table/). The table may be weak, the smallest relation that contains the true composition, as for RCC8, or strong and exact, as for the interval and point algebras.
- **Closure is sound and cubic, not complete.** [Algebraic closure](/algebraic-closure/) runs in $O(|B| n^3)$ time and $O(n^2)$ space and never removes a solution. An empty label proves inconsistency; a closed network proves nothing in general. With a weak table, closure is weaker than path consistency.
- **Points are easy.** For the [point algebra](/point-algebra/), closure decides consistency, and [strongly connected components](/point-algebra-consistency/) give a solution in $O(n^2)$ time on a complete network. Without $\ne$ closure also gives the minimal labels; with $\ne$ they take $O(n^4)$ time.
- **Intervals and regions are hard.** Consistency of [interval networks](/interval-algebra-np-completeness/) and of [RCC8](/region-connection-calculus-rcc8/) networks is NP-complete. RCC8 networks of base relations alone are polynomial.
- **Tractable classes are exact and maximal.** On the 868 [ORD-Horn](/ord-horn-subclass/) relations, closure decides interval networks ([Nebel and Bürckert](/nebel-burckert-theorem/)), and adding any relation makes the problem NP-complete. Of the [18 maximal tractable subalgebras](/interval-algebra-tractable-subclasses/), only ORD-Horn contains all base relations. RCC8 has three such classes, $\hat{H}_8$, $C_8$ and $Q_8$, of 148, 158 and 160 relations ([Renz and Nebel](/rcc8-tractable-subclasses/)).
- **Products split by axis.** For the [rectangle algebra](/rectangle-algebra/) and the [cardinal directions](/cardinal-direction-calculus/) of points, a network of product labels is consistent exactly when each axis network is. The [double cross](/double-cross-calculus/) is ternary and NP-hard already for base relations.
- **Disjunctive metric time is NP-complete.** [TCSP](/temporal-constraint-satisfaction-problem/) and [DTP](/disjunctive-temporal-problem/) are both NP-complete. Each choice of one disjunct per constraint is a [simple temporal problem](/simple-temporal-problem/) decided by a negative-cycle test.
- **Controllability has three strengths.** In an [STNU](/simple-temporal-network-with-uncertainty/), strong implies dynamic, which implies weak, and neither converse holds. Strong controllability reduces to an STP in $O(N^3)$. [Dynamic controllability](/dynamic-controllability/) is polynomial, $O(N^4)$ by [Morris (2006)](/morris-dynamic-controllability/) and $O(N^3)$ by Morris (2014). For weak controllability the sources give no polynomial algorithm.
- **Qualitative simulation over-approximates.** [QSIM](/qsim/) is sound and not complete: every real behavior is in its tree, but the tree may also hold behaviors that no real system has. In [qualitative process theory](/qualitative-process-theory/), influences of opposite sign leave a derivative ambiguous, and each possible sign starts a branch.

| Problem | Method | Cost | What is guaranteed |
|---|---|---|---|
| any calculus | algebraic closure | $O(\lvert B \rvert n^3)$ | sound; decides only on classes proved exact |
| point algebra | closure, or SCC on the $\le$ graph | $O(n^3)$, or $O(n^2)$ | decides consistency; minimal labels if no $\ne$ |
| interval algebra, all relations | backtracking with closure | exponential worst case | NP-complete |
| ORD-Horn networks | algebraic closure | $O(n^3)$ | decides consistency |
| RCC8, all relations | backtracking over $\hat{H}_8$, $C_8$ or $Q_8$ pieces | exponential worst case | NP-complete |
| RCC8 over $\hat{H}_8$, $C_8$ or $Q_8$ | algebraic closure | $O(n^3)$ | decides consistency |
| rectangles, ORD-Horn products | closure on each axis | $O(n^3)$ | decides consistency |
| TCSP, $e$ constraints of $l$ intervals | enumerate STP labelings | $O(n^3 l^e)$ | exact minimal network |
| DTP | meta-CSP over disjuncts, or SMT | exponential worst case | NP-complete |
| STNU, strong | rewrite to an STP | $O(N^3)$ | decides |
| STNU, dynamic | Morris (2006) | $O(N^4)$ | decides |
| QSIM | transitions, Waltz filtering, search | $O(b(c^3 + c n 4^n))$ | sound, not complete |

: Main problems and methods of the chapter. $B$: base relations; $n$: variables; $l$: intervals per TCSP constraint; $e$: TCSP constraints; $N$: time points of an STNU; $b$: QSIM states; $c$: QSIM constraints.

## Choosing a method

First check whether every label lies in a known tractable class: ORD-Horn or another of the 18 subalgebras for intervals, the point algebra, one of the three RCC8 classes for regions, or a product of ORD-Horn relations for rectangles. If so, algebraic closure is the whole algorithm. If not, search over refinements into pieces of the largest available class, and run closure at every node. Use Allen's incremental queue when constraints arrive one at a time.

With numbers, an STP is a shortest-path problem. For disjunctions use a DTP solver or an SMT solver with [difference logic](/difference-logic-satisfiability/), since TCSP path consistency can split intervals into many pieces. When durations are not under your control, test dynamic controllability with Morris's algorithm. Settle for strong controllability only when no observation is possible during execution.

For physical systems with unknown parameters, use QSIM or a process model, and treat each predicted behavior as a possibility to check. When all parameters are known, a numeric [ODE solver](/ode-initial-value-problem/) is cheaper and exact.
