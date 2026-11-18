Take a loop that a compiler meets every day:

```
i = 0
while i < n:
    a[i] = x * y
    i = i + 1
```

The product `x * y` is computed on every trip, but neither `x` nor `y` changes inside the loop, so it can be computed once before it. After the loop, `x` and `y` may be dead, and their registers free. If the array `a` has length `n`, the check that `i` is in bounds can go, because `0 <= i` and `i < n` hold at every access. Each of these facts is about all runs of the program, not one, and each comes from the same kind of computation: attach a fact to every program point and push facts along the edges of the [control flow graph](/control-flow-graph/) until nothing changes.

That computation is a [dataflow analysis](/dataflow-analysis/), and its general form is abstract interpretation. Every interesting property of what a program does is undecidable, by Rice's theorem, so no analysis is exact. An analysis is sound in one direction: a may-analysis reports a superset of what can happen, a must-analysis a subset. How much it loses is a separate question, and much of this chapter is about where precision goes. The bounds check above shows it well: [intervals](/interval-domain/) prove $0 \le i$ but cannot relate $i$ to $n$, while [octagons](/octagon-domain/) keep $i - n \le -1$ and can.

## What the chapter covers

1. **Classic dataflow problems.** [Available expressions](/available-expressions/), [live variables](/live-variable-analysis/), [reaching definitions](/reaching-definitions/) and [very busy expressions](/very-busy-expressions/): forward or backward, on all paths or on some path.
2. **Frameworks and their solutions.** A [monotone framework](/monotone-dataflow-framework/) is a lattice of facts and monotone transfer functions. The [meet over all paths](/meet-over-all-paths-solution/) is the ideal answer and the [maximal fixed point](/maximal-fixed-point-solution/) is the computed one; they agree for distributive frameworks with every block reachable, by the [coincidence theorem](/mop-mfp-coincidence-theorem/).
3. **Solving the equations.** The [worklist algorithm](/worklist-dataflow-algorithm/) for any monotone framework of finite height, the [Kam-Ullman bound](/kam-ullman-iteration-bound/) of $d + 2$ passes for rapid distributive frameworks, and [elimination methods](/elimination-dataflow-methods/).
4. **Constant propagation.** The [problem](/constant-propagation-problem/) that is monotone but not distributive, and [sparse conditional constant propagation](/sparse-conditional-constant-propagation/), which finds constants and dead branches together.
5. **Abstract interpretation.** From the [collecting semantics](/collecting-semantics/) to an [abstract domain](/abstract-domain/) through a [Galois connection](/galois-connection/); intervals with [widening](/widening-operator/) and [narrowing](/narrowing-operator/), and the [weak topological ordering](/weak-topological-ordering/) that decides where to widen.
6. **Richer domains.** Octagons, [convex polyhedra](/polyhedra-domain/), the [reduced product](/reduced-product/) of two domains, and [strictness analysis](/strictness-analysis/) for lazy functional programs.
7. **Across procedures.** [Flow sensitivity](/flow-sensitivity/) and [context sensitivity](/context-sensitivity/), the [functional approach](/functional-approach-interprocedural/) with procedure summaries, the [IFDS framework](/ifds-framework/) and the [IDE framework](/ide-framework/), and [taint analysis](/taint-analysis/) as their main client.
8. **Slicing.** [Program slicing](/program-slicing/) by [Weiser's dataflow method](/weiser-slicing/) and by [dependence graph reachability](/pdg-slicing/), [dynamic slicing](/dynamic-slicing/) for one run, and [slicing across procedures](/system-dependence-graph-slicing/).
9. **The heap, and analysis in Datalog.** [Shape analysis](/shape-analysis/), its [three-valued logic](/three-valued-logic-shape-analysis/) form, [bi-abduction](/bi-abduction/) for separation-logic specifications, and [analyses written in Datalog](/datalog-program-analysis/).

## A first reading

Read these first, in this order:

1. [Dataflow analysis](/dataflow-analysis/)
2. [Live variable analysis](/live-variable-analysis/)
3. [Reaching definitions](/reaching-definitions/)
4. [Monotone dataflow framework](/monotone-dataflow-framework/)
5. [Gen-kill dataflow problem](/gen-kill-problem/)
6. [Maximal fixed-point solution](/maximal-fixed-point-solution/)
7. [MOP-MFP coincidence theorem](/mop-mfp-coincidence-theorem/)
8. [Worklist dataflow algorithm](/worklist-dataflow-algorithm/)
9. [Constant propagation](/constant-propagation-problem/)
10. [Abstract domain](/abstract-domain/)
11. [Galois connection](/galois-connection/)
12. [Interval abstract domain](/interval-domain/)
13. [Widening operator](/widening-operator/)
14. [Program slicing](/program-slicing/)

That path gives the whole method: problems, frameworks, a solver, a domain of infinite height and the widening that tames it. Skip at first the [Kleene fixed-point theorem](/kleene-fixed-point-theorem/), elimination methods, the weak topological ordering, the relational domains, strictness analysis, IDE and three-valued shape analysis. Come back to the interprocedural group once the single-procedure case is clear; it reuses every idea of the earlier groups.

## Before you start

The analyses run on the [control flow graph](/control-flow-graph/) of [basic blocks](/basic-block/), and some on [static single assignment form](/static-single-assignment-form/) or the [program dependence graph](/program-dependence-graph/) of Chapter 34.2. The solvers need [fixed points](/fixed-point/) and the [Knaster-Tarski theorem](/knaster-tarski-theorem/) of Volume 16, and the ordering results need [depth-first orders](/depth-first-orders/) and [graph reachability](/graph-reachability/) from Volume 7. Octagons build on the [difference-bound matrix](/difference-bound-matrix/) of Volume 16, and polyhedra on the [Minkowski-Weyl theorem](/minkowski-weyl-theorem/) of Volume 13. Volume 1 has a single entry on [abstract interpretation](/abstract-interpretation/) that states the idea and its soundness; this chapter splits it into semantics, domains, connections and solvers, with algorithms and costs for each. The Datalog entry uses [Datalog](/datalog/) from Volume 40 and [Andersen's analysis](/andersen-analysis/) from Chapter 34.7. You should be comfortable with partial orders, induction on paths, and reading short programs in three-address form.
