## What to remember

- **Sound in one direction.** Every nontrivial property of program behavior is undecidable, so an analysis over-approximates (a may-analysis) or under-approximates (a must-analysis). Soundness is relative to a stated concretization $\gamma$ or [Galois connection](/galois-connection/); precision is a separate question.
- **Two answers.** The [meet over all paths](/meet-over-all-paths-solution/) is the ideal answer and the [maximal fixed point](/maximal-fixed-point-solution/) is the computed one. For a monotone framework $\mathrm{MFP} \sqsubseteq \mathrm{MOP}$. They are equal when the framework is distributive and every block is reachable. [Constant propagation](/constant-propagation-problem/) is not distributive.
- **Termination and speed.** The [worklist algorithm](/worklist-dataflow-algorithm/) stops on any lattice of finite height $h$, in $O((n + m)(h + 1))$ lattice operations. For rapid distributive frameworks, which include all [gen-kill problems](/gen-kill-problem/), round robin in reverse postorder stops after at most $d + 2$ passes, where $d$ is the loop-connectedness depth.
- **Best transformers.** With a Galois connection $(\alpha, \gamma)$, the most precise sound transformer of $f$ is $\alpha \circ f \circ \gamma$. Composing the best transformers of single statements can be less precise than the best transformer of the block.
- **Infinite height needs widening.** On [intervals](/interval-domain/), octagons and polyhedra, a [widening](/widening-operator/) $\nabla$ forces the ascending iteration to stop at a post-fixed point, at a cost in precision. A [narrowing](/narrowing-operator/) then descends and recovers part of what was lost, but not always all of it.
- **Relations cost more.** Intervals take $O(v)$ per operation, [octagons](/octagon-domain/) need an $O(v^3)$ closure (a tight closure over the integers), and [polyhedra](/polyhedra-domain/) are exponential in the worst case.
- **Procedures.** Only valid paths, where each return matches its call, matter. [Call strings](/context-sensitivity/) of bounded length can lose precision under recursion; the summaries of the functional approach are exact for distributive frameworks. [IFDS](/ifds-framework/) computes the meet over all valid paths of a distributive subset problem as reachability in $O(E D^3)$ time, and $O(E D)$ for gen-kill problems.
- **Slices.** A [static slice](/program-slicing/) by reachability in the dependence graph costs $O(n + e)$. The smallest slice is not computable, so every method returns a safe superset. A [dynamic slice](/dynamic-slicing/) holds for one input and lies inside the static slice.

| Method | Problem | Cost | What is guaranteed |
|---|---|---|---|
| Worklist, finite height $h$ | any monotone framework | $O((n + m)(h + 1))$ | MFP; equals MOP if distributive, all blocks reachable |
| Round robin, reverse postorder | rapid distributive frameworks | $O((d + 2)(n + m))$ | MFP after $d + 1$ passes |
| [Sparse conditional constant propagation](/sparse-conditional-constant-propagation/) | constants on SSA form | $O(n + m + s d)$ | at least as strong as any sequence of constant propagation and dead-branch removal |
| Intervals with widening | numeric bounds | $O(v)$ per operation | a sound post-fixed point, not always the least |
| Octagons | bounds on $\pm x \pm y$ | $O(v^3)$ closure | sound; inclusion test exact over the rationals, and over the integers after tight closure |
| Polyhedra | linear inequalities | exponential worst case | sound; no best abstraction in general |
| IFDS | distributive subset problems across calls | $O(E D^3)$ | meet over all valid paths |
| IDE | distributive value problems across calls | $O(E D^3)$ | meet over all valid paths |
| [PDG slicing](/pdg-slicing/) | static slice in one procedure | $O(n + e)$ | a safe slice, not minimal |
| [SDG slicing](/system-dependence-graph-slicing/) | static slice across calls | $O(N + E)$ with summary edges | no unrealizable call-return paths |
| Dynamic slicing, forward method | slice of one run | $O(T n)$ | correct for that input only |

: Main methods of the chapter. $n$, $m$: blocks or statements and edges; $h$: lattice height; $d$: loop-connectedness depth (in the SCCP row, the largest in-degree of a block); $s$: SSA edges; $v$: variables; $E$, $D$: supergraph edges and facts per procedure; $e$, $N$: dependence graph edges and nodes; $T$: executed statement instances.

## Choosing a method

For bit-vector problems, round robin or a worklist is enough. For constants on SSA form, use sparse conditional constant propagation: it costs about the same as plain propagation and finds more when a constant branch hides a constant. For numeric invariants, start with intervals, move to octagons for relations such as $i < n$, and keep polyhedra for few variables. Widen at the heads of a [weak topological ordering](/weak-topological-ordering/) and follow with a few narrowing steps.

Across procedures, use IFDS for finite sets of facts with distributive transfer functions, such as taint, and IDE when each fact carries a value. When the program recurses, prefer summaries to call strings. To debug one failing run, take a dynamic slice; otherwise a static one, on the system dependence graph when there are calls.
