## What to remember

- The [Cooper-Harvey-Kennedy algorithm](/cooper-harvey-kennedy-dominance/) needs at most $d + 2$ passes in reverse postorder, where $d$ is the largest number of retreating edges on a simple path from the entry of the [control flow graph](/control-flow-graph/). Its worst case is worse than that of the near-linear [Lengauer-Tarjan algorithm](/lengauer-tarjan-algorithm/), but on a reducible graph the first pass is final, and it was measured faster on real procedures.
- $Y \in \mathrm{DF}(X)$ when $X$ dominates a predecessor of $Y$ but does not strictly dominate $Y$. [Dominance frontiers](/dominance-frontier/) are [computed](/dominance-frontier-computation/) in $\Theta(n + m + D)$ time, where $D = \sum_X \lvert \mathrm{DF}(X) \rvert$ can be $\Theta(n^2)$. The [control dependences](/control-dependence/) of a block are its dominance frontier on the reversed graph.
- A graph is [reducible](/reducible-flow-graph/) when every retreating edge goes to a dominator of its source, or equivalently when [T1-T2](/t1-t2-reduction/) leaves one node. Then each loop is a [natural loop](/natural-loop/) with one header. On any graph, the [loop nesting forest](/loop-nesting-forest/) gives loops with one or more headers.
- Minimal [SSA form](/static-single-assignment-form/) puts a phi node for $v$ at $\mathrm{DF}^+(S_v)$, the iterated frontier of the blocks that define $v$, and can have $\Theta(n^2)$ phi nodes. [Pruned SSA](/pruned-ssa-form/) keeps a phi node only where $v$ is live. The [Braun construction](/braun-ssa-construction/) gives pruned SSA without dominance, and minimal SSA on reducible graphs.
- The phi nodes of a block act at the same time, as a parallel copy. A parallel copy $P$ with $c$ cycles is done with $\lvert P \rvert + c$ sequential copies and one temporary, and a pure cycle of length $k$ cannot be done with fewer than $k + 1$ copies.
- After copy folding, copies at the ends of predecessors can be wrong. [Splitting critical edges](/critical-edge-splitting/) fixes the [lost-copy problem](/lost-copy-and-swap-problems/) but not the swap problem, which needs ordered copies and a temporary. [Sreedhar's translation](/sreedhar-cssa-translation/) fixes both with copies alone.
- A strict SSA procedure is a program of local functions nested along the dominator tree, with phi nodes as parameters and jumps as tail calls ([SSA and CPS](/ssa-cps-correspondence/)). [CPS conversion](/cps-conversion/) takes $O(n)$ time, [closure conversion](/closure-conversion/) $O(n^2)$ and [lambda lifting](/lambda-lifting/) $O(n^2)$ with the method of Danvy and Schultz.

| Method | Task | Time | Result |
|---|---|---|---|
| Cooper-Harvey-Kennedy | immediate dominators | $O((d + 2)\,n(n + m))$; $\Theta(n + m)$ best | exact; at most 2 passes on reducible graphs |
| Lengauer-Tarjan (Volume 7) | immediate dominators | $O(m\,\alpha(m, n))$ | exact |
| Dominance frontier computation | all frontiers | $\Theta(n + m + D)$ | exact; $D$ up to $\Theta(n^2)$ |
| T1-T2 reduction | reducibility test | $O(n^2 + m)$ | exact; order of collapse |
| Steensgaard loop forest | loops and headers | $O((h + 1)(n + m))$ | defined on every graph |
| Cytron construction | SSA form | $O(I + V(n + m + D))$ | minimal SSA |
| Braun construction | SSA form | $O(I + (B + E)V + B^2V^2)$ | pruned; minimal on reducible graphs |
| Sreedhar Method I | conventional SSA | $\Theta(N)$ | always correct; many copies |
| Sreedhar Method III | conventional SSA | $O(FBNV + N^2V^2)$ | copies only where names interfere |
| CPS conversion (Danvy-Filinski) | CPS | $O(n)$ | no administrative redexes |
| Closure conversion | closed code | $O(n^2)$ time and output | flat closures |
| Lambda lifting | global functions | $O(n^3)$; $O(n^2)$ by Danvy-Schultz | extra parameters at every call |

: Main methods. $n$ and $m$ count nodes and edges, or term nodes for the last three rows; $h$ is the depth of the loop forest; $I$ counts instructions, $V$ variables, $B$ and $E$ blocks and edges, $N$ program size with phi operands, $F$ phi nodes.

## Choosing a method

For the dominators of one procedure, use Cooper-Harvey-Kennedy: it is short, and most procedures are small and reducible. Use Lengauer-Tarjan for very large or adversarial graphs. For loops, take natural loops from the back edges of a reducible graph, and build a loop nesting forest when the graph may be irreducible.

Once the graph exists, build SSA form with the Cytron construction, with liveness for pruned form or the cheaper semi-pruned test. While translating from the syntax tree, use the Braun construction, with its SCC pass if the graph may be irreducible. To leave SSA form, split critical edges and sequence each parallel copy, or use Sreedhar's translation when edges cannot be split, and let coalescing remove the extra copies.

For a functional language, convert to CPS or ANF, then remove nested functions: closure conversion for functions that escape, lambda lifting for known local functions with few free variables, and defunctionalization when the whole program is at hand.
