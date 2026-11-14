A designer sketches the profile of a bracket: a few lines, two arcs and a hole, drawn roughly. Then come the dimensions. This edge is 40 mm long, these two lines are perpendicular, the arc is tangent to that line, and the center of the hole lies 12 mm from the edge. The CAD program must move the drawing so that every constraint holds, keep the result close to what was drawn, and do it again each time the designer changes a value. If the dimensions leave the bracket free to move, or fix it twice in ways that conflict, the program should say so and point to the constraints at fault. Assemblies raise the same problem in space: the parts are rigid bodies with six degrees of freedom each, and mates such as a pin concentric with a hole remove some of them.

Each [geometric constraint](/geometric-constraint/) is a polynomial equation that does not change under rigid motions, so a sketch is a polynomial system, and solving such systems in general is hard. Placing points with given distances is NP-complete already on a line, and in the plane it is as hard as deciding whether any system of polynomial equations has a real solution. Practical solvers avoid the general case. They read the structure of the constraints from a graph, split the sketch into small parts that are rigid by themselves, solve each part with ruler and compass or a small numerical solve, and glue the parts together. The theory that says which graphs are rigid comes from the study of frames by Maxwell, and the same results serve sensor networks, robot formations and molecules.

Three kinds of guarantee run through the chapter, and they should be kept apart. Counting results, such as [Laman's theorem](/laman-theorem/), are about generic positions: they hold for almost all values, and a particular drawing with parallel lines or collinear points can break them. Graph-constructive solvers are exact in a model with exact real arithmetic, but they choose between solutions with orientation tests that must be computed exactly, or they can return a mirrored part. Numerical solvers such as Newton's method work in floating point and are proved to converge only near a regular solution. And the choice of the solution that the user meant is a rule judged by experience, not a theorem.

## What the chapter covers

1. **Constraints and the solving problem.** [Geometric constraints](/geometric-constraint/), the [constraint graph](/geometric-constraint-graph/) with its counts of degrees of freedom, and the [geometric constraint problem](/geometric-constraint-problem/) with its hardness results.
2. **First solvers.** [Local propagation](/local-propagation-solving/), which solves one constraint at a time and fails on cycles, [variational geometry](/variational-geometry/), which solves everything at once with Newton's method, and [ruler-and-compass constructibility](/ruler-and-compass-constructibility/), which marks what exact step-by-step solvers can reach.
3. **Rigidity of frameworks.** [Bar-and-joint frameworks](/bar-and-joint-framework/), [infinitesimal rigidity](/infinitesimal-rigidity/) as a rank condition, [generic rigidity](/generic-rigidity/), [Maxwell's counting rule](/maxwell-counting-rule/) and [well-constrained systems](/well-constrained-system/).
4. **Laman's theorem and its algorithms.** The exact count for generic rigidity in the plane, the [Henneberg construction](/henneberg-construction/) that builds every minimally rigid graph, and the [pebble game](/pebble-game-rigidity/) that tests the count fast.
5. **Decomposition solvers in the plane.** [Graph-constructive solving](/constructive-constraint-solving/), the bottom-up [Fudos-Hoffmann reduction](/fudos-hoffmann-reduction/), the top-down [Owen decomposition](/owen-triconnected-decomposition/), and the [root identification problem](/root-identification-problem/) of choosing among the many solutions.
6. **Bodies, assemblies and decomposition plans.** [Degrees of freedom analysis](/degrees-of-freedom-analysis/) with flows, [Tay's theorem](/tay-theorem/) for rigid bodies joined by bars, [assembly constraint solving](/assembly-constraint-solving/) and [DR-plans](/dr-plan/).
7. **Global rigidity.** When the lengths fix the shape uniquely: [global rigidity](/global-rigidity/), Hendrickson's necessary conditions and the [Jackson-Jordán theorem](/jackson-jordan-theorem/) that settles the plane.

## A first reading

Read these in order:

1. [Geometric constraint](/geometric-constraint/)
2. [Geometric constraint problem](/geometric-constraint-problem/)
3. [Local propagation solving](/local-propagation-solving/)
4. [Variational geometry](/variational-geometry/)
5. [Bar-and-joint framework](/bar-and-joint-framework/)
6. [Infinitesimal rigidity](/infinitesimal-rigidity/)
7. [Generic rigidity](/generic-rigidity/)
8. [Laman's theorem](/laman-theorem/)
9. [Well-constrained system](/well-constrained-system/)
10. [Graph-constructive constraint solving](/constructive-constraint-solving/)
11. [Fudos-Hoffmann reduction](/fudos-hoffmann-reduction/)
12. [Root identification problem](/root-identification-problem/)
13. [Degrees of freedom analysis](/degrees-of-freedom-analysis/)

This path goes from the problem to the two simplest solvers, then through the rigidity theory that explains when a sketch has finitely many solutions, and ends with the decomposition solver used in practice and its choice of solution. On a first pass you can skip the proofs of Laman's theorem, the pebble game, Owen's decomposition, Tay's theorem, DR-plans and the two entries on global rigidity, and come back to them when a later topic needs them.

## Before you start

The chapter uses graphs throughout: the basic notions of a [graph](/graph/), [depth-first search](/depth-first-search/), [biconnected components](/biconnected-components/) and [vertex connectivity](/k-vertex-connected-graph/), and for the advanced entries the [max-flow min-cut theorem](/max-flow-min-cut-theorem/) and the [Nash-Williams and Tutte theorem](/nash-williams-tutte-theorem/) on spanning trees, all in Volume 7. From linear algebra you need the [rank](/rank/) of a matrix (Volume 11), and for the matroid view of rigidity the notion of a [matroid](/matroid/) (Volume 2). The proofs use [induction](/induction/) (Volume 1).

The solvers rest on algebra and numerics: [polynomial system solving](/polynomial-system-solving/) and [minimal polynomials](/minimal-polynomial-algebraic-element/) of algebraic numbers (Volume 11), and [Newton's method for systems](/newton-method-for-systems/) and [homotopy continuation](/homotopy-continuation/) (Volume 12). The geometric steps use the [orientation test](/orientation-test/) and [circle-circle intersection](/circle-circle-intersection/) from Volume 13, and the chapter on solid modeling of this volume explains in [exact geometric computation](/exact-geometric-computation/) why signs must be computed exactly. [Constraint propagation](/constraint-propagation/) in Volume 16 is the discrete cousin of local propagation, and the [Schwartz-Zippel lemma](/schwartz-zippel-lemma/) in Volume 17 justifies the randomized rank test for generic rigidity.
