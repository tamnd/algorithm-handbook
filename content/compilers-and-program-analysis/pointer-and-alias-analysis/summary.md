## What to remember

- [Andersen's analysis](/andersen-analysis/) turns `p = &a`, `p = q`, `p = *q` and `*p = q` into subset constraints and finds their least solution in $O(n^3 + m)$ time and $O(n^2 + m)$ space. Its output alone can have $\Theta(n^2)$ pairs. No subcubic algorithm is known; Heintze and McAllester tie the cubic cost to 2NPDA reachability.
- [Steensgaard's analysis](/steensgaard-analysis/) unifies instead, in $O((n + m)\,\alpha(n + m))$ time. Each of its sets contains Andersen's set for the same variable, and any two of its sets are equal or disjoint. [One-level flow](/das-one-level-flow/) keeps subset edges at the top level only, costs $O(n(n + m))$, and always contains Andersen's sets; that it comes close to them is a measurement.
- [Offline substitution](/offline-variable-substitution/), [online cycle elimination](/online-cycle-elimination/) and [hybrid cycle detection](/hybrid-cycle-detection/) give exactly Andersen's answer. They merge variables whose sets must be equal, such as those on a cycle of copies, and do not lower the worst case.
- A sound call graph for virtual calls comes from declared types ([CHA](/class-hierarchy-analysis/)), from the created classes ([RTA](/rapid-type-analysis/)), or from the classes that reach each receiver ([VTA](/variable-type-analysis/)). Each keeps a subset of the edges of the one before it, under a closed world.
- [0-CFA](/zero-cfa/) runs in $O(n^3)$ time and is complete for PTIME. [k-CFA](/k-cfa/) takes $2^{O((k+1) n \log n)}$ time and is [EXPTIME-complete](/k-cfa-exptime-completeness/) for every fixed $k \ge 1$. [Object sensitivity](/object-sensitivity/) stays polynomial for fixed $k$; its precision is measured.
- Precise may-alias analysis is [undecidable](/may-alias-undecidability/) with dynamic allocation, PSPACE-complete for flow-sensitive analysis without it, and [NP-hard](/flow-insensitive-alias-np-hardness/) even when statement order is ignored, once statements may dereference many times.
- [Mod-ref analysis](/mod-ref-analysis/) without aliases is solved in linear time plus $O(N + E)$ bit-vector operations; [escape analysis](/escape-analysis/) costs $O(n^2 h + s h)$ on top of points-to facts; [type-based alias analysis](/type-based-alias-analysis/) needs only declared types and is sound only for type-safe code.

| Method | Problem | Time | Result |
|---|---|---|---|
| Andersen | points-to, inclusion | $O(n^3 + m)$ | least solution of subset constraints |
| Steensgaard | points-to, unification | $O((n + m)\alpha(n + m))$ | contains Andersen; sets equal or disjoint |
| One-level flow | points-to, mixed | $O(n(n + m))$ | contains Andersen; closeness measured |
| Offline substitution, cycle detection | Andersen's constraints | worst case not lowered | same as Andersen; speed measured |
| Demand-driven | chosen queries | $O(m^3 + ms)$ | Andersen's sets of the queries |
| Sparse flow-sensitive | flow-sensitive points-to | $O(n^3 m^4)$ | strong updates along def-use chains |
| CHA, RTA | call graph | $O(n + SK + KM)$ | sound under a closed world |
| VTA | call graph | $O((n + P)K)$ | subset of the initial call graph |
| 0-CFA | higher-order control flow | $O(n^3)$ | PTIME-complete |
| k-CFA, $k \ge 1$ | higher-order control flow | $2^{O((k+1) n \log n)}$ | EXPTIME-complete |
| Type-based | alias of field references | $O(t^2 h + m \log t)$ | sound for type-safe code |
| Escape | stack allocation, lock removal | $O(n^2 h + sh)$ | sound given its points-to facts |

: Main methods. $n$ counts variables (for CFA, nodes of the program; for sparse flow-sensitive analysis, nodes and edges of the control flow graph), $m$ statements (for demand-driven analysis, variables and queries, with $s$ statements), $S$ call sites, $K$ classes, $M$ method names, $P$ edges of the initial call graph, $t$ types of height $h$, and for escape analysis $h$ allocation sites and $s$ the size of the statements.

## Choosing a method

For a compiler that needs alias facts quickly, start with type-based alias analysis where the language allows it, and add Steensgaard's analysis or one-level flow for whole-program pointer facts. When precision matters more than time, run Andersen's analysis with offline substitution and hybrid cycle detection; Hardekopf and Lin measured it on C programs of over a million lines. If only a few variables matter, as in a bug checker, a demand-driven solver avoids solving the whole program.

For Java and other object-oriented code, take CHA or RTA as the first call graph and refine it with VTA or with points-to analysis computed together with the call graph. Add object sensitivity, such as 2-object sensitivity with a 1-object heap context, when containers and factories lose precision. For functional programs, 0-CFA is the cubic baseline; use k-CFA with $k \ge 1$ only on small programs or with a bound on the work. Feed the result to mod-ref and escape analysis, and remember that every answer is sound only for the semantics and the closed world that the entry states.
