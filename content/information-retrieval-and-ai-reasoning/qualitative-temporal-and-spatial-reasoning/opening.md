A site report says three things. The pond lies inside the park and does not touch its edge. The park touches the road along one side. The pond and the road overlap. No map comes with the report and no distances, yet the report contradicts itself: whatever is strictly inside the park cannot reach anything that only touches the park from outside. A program can find this with one table lookup. In [RCC8](/region-connection-calculus-rcc8/), "pond NTPP park" composed with "park EC road" gives only DC, so the pond and the road are disconnected, and the stated "overlaps" is impossible.

That is qualitative reasoning. Facts come as relations from a small fixed set, such as before, inside, north of or touches, and the questions are whether the facts can all hold, what follows from them, and a picture or a timeline that satisfies them. This chapter builds directly on [Allen's interval algebra](/allens-interval-algebra/), entry 6.5.9 in Volume 6, which gives the 13 interval relations and their composition. Here that algebra becomes one example of a general method. The same method serves regions, directions and rectangles. Then come numbers: time differences with gaps, durations that the world chooses, and quantities known only by their signs.

The method has a weak point that runs through every group. [Algebraic closure](/algebraic-closure/) is a cubic propagation of the composition table. It never loses a solution, but for the full interval algebra and for RCC8 it can leave an inconsistent network untouched, because both consistency problems are NP-complete. Most of the theory therefore marks out subclasses of relations on which closure is exact, and proves that they cannot be made larger.

## What the chapter covers

1. **Calculi and networks.** A [qualitative constraint calculus](/qualitative-constraint-calculus/) of base relations, its [composition table](/composition-table/), [qualitative constraint networks](/qualitative-constraint-network/), and the [point algebra](/point-algebra/) of $<$, $=$ and $>$.
2. **Propagation.** [Algebraic closure](/algebraic-closure/), Allen's [incremental propagation](/allen-constraint-propagation/) with a queue, and the [point algebra algorithms](/point-algebra-consistency/), where closure is exact and strongly connected components give a solution.
3. **Intervals, hardness and tractable classes.** The [NP-completeness](/interval-algebra-np-completeness/) of interval networks, the [ORD-Horn subclass](/ord-horn-subclass/), the [Nebel-Bürckert theorem](/nebel-burckert-theorem/) that closure decides it, and the [18 maximal tractable subalgebras](/interval-algebra-tractable-subclasses/).
4. **Topology of regions.** The [nine-intersection model](/nine-intersection-model/), RCC8, the coarser [RCC5](/rcc5/), and the [tractable classes of RCC8](/rcc8-tractable-subclasses/).
5. **Directions and orientation.** The [rectangle algebra](/rectangle-algebra/) and the [cardinal direction calculus](/cardinal-direction-calculus/), both products of one-dimensional calculi, and the ternary [double-cross calculus](/double-cross-calculus/).
6. **Metric time with disjunctions.** The [temporal constraint satisfaction problem](/temporal-constraint-satisfaction-problem/) and the [disjunctive temporal problem](/disjunctive-temporal-problem/), both NP-complete and both solved by search over simple temporal problems.
7. **Durations that nature chooses.** The [simple temporal network with uncertainty](/simple-temporal-network-with-uncertainty/), strong, weak and [dynamic controllability](/dynamic-controllability/), and [Morris's polynomial algorithm](/morris-dynamic-controllability/) for the dynamic case.
8. **Qualitative physics.** [QSIM](/qsim/), which simulates a qualitative differential equation, and [qualitative process theory](/qualitative-process-theory/), which builds such models from processes.

## A first reading

Read these first, in this order:

1. [Qualitative constraint calculus](/qualitative-constraint-calculus/)
2. [Composition table](/composition-table/)
3. [Qualitative constraint network](/qualitative-constraint-network/)
4. [Algebraic closure](/algebraic-closure/)
5. [Point algebra](/point-algebra/)
6. [Point algebra consistency](/point-algebra-consistency/)
7. [Interval algebra NP-completeness](/interval-algebra-np-completeness/)
8. [ORD-Horn subclass](/ord-horn-subclass/)
9. [Region connection calculus RCC8](/region-connection-calculus-rcc8/)
10. [Temporal constraint satisfaction problem](/temporal-constraint-satisfaction-problem/)
11. [Simple temporal network with uncertainty](/simple-temporal-network-with-uncertainty/)
12. [Dynamic controllability](/dynamic-controllability/)

That path gives the pattern of the whole chapter: a calculus, its table, the closure that propagates it, one case where closure is exact, one where it is not, and the tractable class that repairs it. RCC8 then repeats the pattern for regions, and the last two entries add metric time and uncertainty. Leave for later the 18 subalgebras, the RCC8 subclasses, the double cross, Morris's algorithm and the two entries on qualitative physics. The physics entries stand apart from the rest: they are about continuous quantities that change in time, not about relations between events or regions.

## Before you start

Read entry 6.5.9 on [Allen's interval algebra](/allens-interval-algebra/) first; this chapter assumes its 13 relations and does not repeat them. From Volume 16 you need the [constraint satisfaction problem](/constraint-satisfaction-problem/), [arc consistency](/arc-consistency/) and [path consistency](/path-consistency/), the [simple temporal problem](/simple-temporal-problem/) (entry 16.3.37) on which the metric groups rest, and [3-SAT](/3-sat/) and [Horn clauses](/horn-clause/) for the hardness and tractability proofs. From Volume 7 you need [Bellman-Ford](/bellman-ford/), [Dijkstra's algorithm](/dijkstra/), [difference constraints](/difference-constraints/) and [strongly connected components](/strongly-connected-components/), and for regions the [Jordan curve theorem](/jordan-curve-theorem/). The double cross uses the [orientation test](/orientation-test/) and the nine-intersection model uses [simple polygons](/simple-polygon/), both from Volume 13. QSIM is the qualitative counterpart of the [ODE initial value problem](/ode-initial-value-problem/) of Volume 12. You should be at ease with sets, relations and their composition, and with NP-completeness proofs by reduction.
