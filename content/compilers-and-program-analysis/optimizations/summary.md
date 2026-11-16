## What to remember

- An optimization must keep the behavior on all inputs; that it makes the program faster is usually a measurement. Exact program facts are undecidable, so each pass acts on what a conservative analysis proves. The [full employment theorem](/full-employment-theorem/) says no algorithm finds a smallest equivalent of every program.
- Local passes are linear or close to it. [Local value numbering](/local-value-numbering/) takes $\Theta(n)$ expected time with a hash table.
- Dead code elimination by liveness removes instructions one name at a time. The [aggressive version](/aggressive-dead-code-elimination/) assumes everything is dead and marks what is useful through data and control dependence, in $O(b^2 n + n^2)$ time. It can remove a whole loop, so it may make a run end that used to run forever.
- Value equality is undecidable in general, but Herbrand equivalence, with uninterpreted operators, is decidable. The [Alpern-Wegman-Zadeck algorithm](/alpern-wegman-zadeck-value-numbering/) finds the coarsest congruence of the SSA value graph in $O((n + e) \log n)$ time; it sees through loops where pessimistic hashing does not, but it knows no algebra.
- [Lazy code motion](/lazy-code-motion/) solves partial redundancy elimination with four unidirectional bit-vector analyses. Its placement is safe, computationally optimal and, among those, lifetime optimal, for each expression on its own. [SSAPRE](/ssapre/) is computationally optimal too, and works sparsely on SSA form. Both are lexical.
- Strength reduction replaces a multiplication by an induction variable with an addition. The SSA version finds induction variables as strongly connected components in $O(b^3 + (n + m)^2)$ worst-case time; replacing the loop test needs a bound that cannot wrap.
- [Ball-Larus path profiling](/ball-larus-path-profiling/) numbers the $N$ acyclic paths of a procedure in $O(V + E \log E)$ time so that the sum of the values along a path is its number, in $0..N-1$. Laying out blocks to maximize fall-through is NP-hard; [Pettis-Hansen positioning](/pettis-hansen-code-positioning/) is a greedy heuristic, judged by measurement.
- Search methods find the best code for short loop-free sequences. [Superoptimization](/superoptimization/) is exhaustive and returns a shortest equivalent program, with tests that can only reject. [Equality saturation](/equality-saturation/) is sound but may never saturate, and extracting the cheapest DAG is NP-complete. [Stochastic superoptimization](/stochastic-superoptimization/) is sound because of its final check, and complete only in the limit.

| method | scope | what it finds | time |
|---|---|---|---|
| [local value numbering](/local-value-numbering/) | one block | equal values by hashing | $\Theta(n)$ expected |
| [copy propagation](/copy-propagation/) | procedure | uses that can read the source of a copy | $O(Rbnc + cbnv)$ |
| [aggressive DCE](/aggressive-dead-code-elimination/) | procedure | statements not needed for any effect | $O(b^2 n + n^2)$ |
| [AWZ value numbering](/alpern-wegman-zadeck-value-numbering/) | SSA procedure | the coarsest congruence | $O((n + e)\log n)$ |
| [lazy code motion](/lazy-code-motion/) | procedure | optimal placement of each expression | $O(n^2 m)$ |
| [SSAPRE](/ssapre/) | SSA procedure | a computationally optimal placement | $O((m + v)(n + d))$ |
| [operator strength reduction](/operator-strength-reduction/) | SSA procedure | induction variables, multiplies to adds | $O(b^3 + (n + m)^2)$ |
| [interprocedural constant propagation](/interprocedural-constant-propagation/) | whole program | formals constant on every call | $O((v + 1)(n + bv) + (k + 1)n)$ |
| [Ball-Larus path profiling](/ball-larus-path-profiling/) | procedure | a unique number for each acyclic path | $O(V + E \log E)$ |
| [Pettis-Hansen positioning](/pettis-hansen-code-positioning/) | procedure and program | a block and procedure order, greedily | $O(E \log E + CE)$ |
| [binding-time analysis](/binding-time-analysis/) | program | static and dynamic parts | $O(NT)$ |
| [superoptimization](/superoptimization/) | a few instructions | a shortest equivalent program | exponential in length |

: The algorithms of the chapter, with their worst-case time as given in their entries. The letters are defined in the entries.

## Choosing a method

Start with the cheap local passes: [constant folding](/constant-folding/), local value numbering, [copy propagation](/copy-propagation/) and [dead code elimination](/dead-code-elimination/), run in a loop, since each makes work for the others. Across blocks, global value numbering finds redundancy hidden behind different names, and partial redundancy elimination finds redundancy on some paths only. Use loop-invariant code motion and strength reduction on hot loops.

Across procedures, [inlining](/function-inlining/) comes first, because it exposes the callee to every other pass; [devirtualization](/devirtualization/) makes more calls inlinable, and scalar replacement cleans up after both. A stale training profile can make a profile-guided layout worse than none.

When part of the input is fixed, as for an interpreter and its program, specialize with [partial evaluation](/partial-evaluation/). For a small hot kernel, a search can beat hand-written rules: exhaustive superoptimization for a few instructions, stochastic search for longer loop-free code, and equality saturation when a set of rewrite rules is already known.
