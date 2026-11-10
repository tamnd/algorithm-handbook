## What to remember

- **A CSP is variables, domains and constraints.** A solution gives each variable a value from its domain so that every constraint holds. The general problem is NP-complete, and graph colouring is the standard example.
- **Propagation removes values that cannot be part of a solution.** [Arc consistency](/arc-consistency/) keeps a value only if each constraint on its variable has a support for it. [AC-3](/ac-3/) reaches the fixpoint in $O(ed^3)$ time and [AC-4](/ac-4/) in the optimal $O(ed^2)$. The fixpoint does not depend on the order of revisions.
- **Stronger consistency costs more.** [Path consistency](/path-consistency/) works on pairs of variables and [k-consistency](/k-consistency/) on sets of $k$, at a cost of $O(n^k d^k)$. Arc consistency is often the best trade inside search.
- **Search interleaves guesses with propagation.** [Forward checking](/forward-checking/) prunes the neighbours of each assigned variable, and [maintaining arc consistency](/maintaining-arc-consistency/) restores full arc consistency at every node. The [minimum remaining values](/minimum-remaining-values/) heuristic branches on the variable with the smallest domain, so failures come early.
- **Backjumping goes back to a cause.** [Conflict-directed backjumping](/conflict-directed-backjumping/) keeps for each variable the earlier variables that took part in its failures, and jumps to the latest of them. Nogood learning records the failure so the search does not repeat it.
- **Global constraints prune more than their parts.** Pairwise $\neq$ on three variables with domain $\{1, 2\}$ is arc consistent, but [Régin's filter](/regin-all-different-filtering/) for [all-different](/all-different-constraint/) sees through matching that no solution exists.
- **Structure makes hard problems easy.** A [tree-structured CSP](/tree-structured-csp/) is solved in $O(nd^2)$ time without backtracking. [Cutset conditioning](/cutset-conditioning/) and [bucket elimination](/bucket-elimination/) extend this to graphs that are close to trees, at a cost exponential in the cutset size or the induced width.
- **The constraint language decides the complexity.** Over $\{0, 1\}$, [Schaefer's theorem](/schaefer-dichotomy-theorem/) gives six polynomial cases and NP-completeness for the rest. The [CSP dichotomy theorem](/csp-dichotomy-theorem/) of Bulatov and Zhuk extends this to every finite domain: a language is easy when it has a weak near-unanimity polymorphism, and NP-complete otherwise.

| Method | Time | Space | Use it for |
|---|---|---|---|
| AC-3 | $O(ed^3)$ | $O(e + nd)$ | simple arc consistency |
| AC-4 | $O(ed^2)$ | $O(ed^2)$ | optimal arc consistency |
| PC-2 | $O(n^3 d^5)$ | $O(n^3 + n^2 d^2)$ | path consistency on binary networks |
| Forward checking | $O(nd^{n+1})$ | $O(nd)$ | cheap pruning during search |
| MAC | $O(ed^{n+3})$ | $O(e + nd)$ | strong pruning during search |
| Min-conflicts | $O(snd)$ for $s$ steps | $O(n)$ | large, loosely constrained problems |
| Tree CSP | $O(nd^2)$ | $O(nd)$ | acyclic constraint graphs |
| Cutset conditioning | $O(d^c(ed + (n - c)d^2))$ | $O(nd)$ | graphs with a small cycle cutset |
| Bucket elimination | $O((m + n)d^{w^*+1})$ | $O(nd^{w^*})$ | small induced width |
| Régin's all-different | $O(n^{3/2} d)$ | $O(nd)$ | all-different with full pruning |
| STP | $O(nm)$, or $O(n^3)$ for all bounds | $O(n^2)$ | simple temporal constraints |

: Methods of the chapter. $n$ is the number of variables, $d$ the largest domain, $e$ the number of binary constraints, $m$ the number of constraints, $c$ the cutset size and $w^*$ the induced width of the ordering.

## Choosing a method

For a finite problem of moderate size, use backtracking with maintaining arc consistency and minimum remaining values, and state structured parts as global constraints such as all-different. This is what constraint programming systems do by default. Add conflict-directed backjumping or nogood learning when the search repeats the same failures. When the problem has many symmetric solutions, add symmetry breaking constraints before search.

When only a good assignment is needed fast and the problem is large and loosely constrained, try min-conflicts. On n-queens the number of repairs it needs stays about the same as $n$ grows, but it cannot prove that no solution exists.

Look at the constraint graph before choosing. A tree is solved by directional arc consistency and one backtrack-free pass. A graph with a small cycle cutset or a small induced width suits cutset conditioning or bucket elimination. Bucket elimination needs memory exponential in the width, and cutset conditioning needs only linear memory.

When constraints are soft or some may be broken, use the maximum CSP or soft constraint frameworks with branch and bound. For real-valued variables, use interval propagation with splitting. For timing constraints of the form $x_j - x_i \le c$, use the simple temporal problem: it is a shortest path problem.
