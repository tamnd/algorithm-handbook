A part designed on a computer still has to be made. A milling machine makes it by cutting material away
from a block. A printer makes it by laying material down, one thin layer at a time. In both cases a program
drives the machine, and that program is computed from the model of the part. This chapter is about those
computations: computer-aided manufacturing (CAM) for cutting, and the slicing and support methods of
additive manufacturing.

Take a bracket stored as a triangle mesh. To print it, the slicer cuts the mesh with a few hundred
horizontal planes, links the cut segments into closed contours, chooses a fill for the inside of each layer,
and adds supports under the parts that hang over air. To mill the same bracket instead, the CAM system
roughs its pockets with offset or trochoidal loops, finishes its curved faces with a ball cutter or a
tilted flat end on five axes, and traces its concave edges with pencil cuts. The controller schedules the
feed, and a simulation checks that the tool never digs into the part. Each step is a geometric
algorithm, most of them built on the geometry of Volume 13 and the surfaces of Volume 28.

The chapter also covers three neighbours of these tasks. Nesting places flat parts on a sheet with little
waste. Topology optimization decides where material should go before the part is drawn. Tolerance analysis
asks whether parts that are each slightly off still fit together.

Keep the kinds of result apart as you read. Some are exact theorems: a slice computed with exact
comparisons of $z$ values has the right topology, the direct slice of a solid of quadrics is a set of exact
conics, a dexel Boolean on rational endpoints is exact, a common access direction exists exactly when a
linear program is feasible, and the forward and backward feed scan is time optimal under speed and
acceleration limits. Some hold for one step or one case only: the principal axis tilt is exact on a concave
cylinder, and a support-free decomposition plan is proved to print, but the search that finds it is a heuristic. The quality of
toolpaths, infill, supports, curved layers and optimized designs is usually measured on test parts; SIMP
and the level set method find local optima only, and BESO has no convergence proof.

## What the chapter covers

1. **Slicing and layers.** [Slicing](/slicing-for-additive-manufacturing/) a mesh into contours, the
   [sweep algorithm](/triangle-mesh-slicing/), [direct slicing](/direct-slicing/) of the CAD model, the [staircase effect](/staircase-effect/),
   [adaptive slicing](/adaptive-slicing/), [curved layer printing](/curved-layer-printing/) and the
   [infill pattern](/infill-pattern/).
2. **Build orientation and supports.** Choosing the [build orientation](/build-orientation/), generating
   [support structures](/support-structure-generation/) and [tree supports](/tree-support/), and the
   support-free [multi-axis printing decomposition](/multi-axis-printing-decomposition/).
3. **Toolpaths and cutter positions.** [Toolpath planning](/toolpath-planning/),
   [cutter location data](/cutter-location-data/), the
   [scallop height](/scallop-height/) between passes, [gouge detection](/gouge-detection/) and the
   [inverse tool offset](/inverse-tool-offset/).
4. **Pocket machining and roughing.** The [pocket machining](/pocket-machining/) problem, its
   [contour-parallel](/contour-parallel-toolpath/), [direction-parallel](/direction-parallel-toolpath/),
   [Voronoi-based](/voronoi-pocket-machining/) and [Fermat spiral](/fermat-spiral-toolpath/) paths, and
   [trochoidal milling](/trochoidal-milling/) and the [constant engagement toolpath](/constant-engagement-toolpath/).
5. **Surface finishing paths.** [Iso-parametric](/iso-parametric-toolpath/),
   [iso-planar](/iso-planar-toolpath/) and [iso-scallop](/iso-scallop-toolpath/) passes on a free-form
   surface, and [pencil cuts](/pencil-cut-machining/) along concave edges.
6. **Five-axis machining.** [Tool orientation](/five-axis-tool-orientation/) by lead and tilt, the
   [principal axis method](/principal-axis-method/), the [accessibility cone](/accessibility-cone/),
   [collision-free tool orientation](/collision-free-tool-orientation/) and [flank milling](/flank-milling/).
7. **Simulation, verification and machine motion.** The [swept volume](/swept-volume/) of a moving tool,
   [NC verification](/nc-verification/) with the [z-map](/z-map-model/) and the
   [dexel representation](/dexel-representation/), [feedrate scheduling](/feedrate-scheduling/) and the
   [parametric CNC interpolator](/parametric-cnc-interpolator/).
8. **Checks on the design.** [Mold parting directions](/mold-parting-direction/) and
   [tolerance stack-up](/tolerance-stack-up/).
9. **Nesting.** The [nesting problem](/nesting-problem/), the [no-fit polygon](/no-fit-polygon/) and
   [bottom-left fill](/bottom-left-fill/).
10. **Topology optimization.** The [problem](/topology-optimization/), the
    [homogenization method](/homogenization-method/), the [SIMP method](/simp-method/),
    [density filtering](/density-filtering/), the [BESO method](/beso-method/) and the
    [level set method](/level-set-topology-optimization/).

## A first reading

For a first pass, read these entries in order:

1. [slicing for additive manufacturing](/slicing-for-additive-manufacturing/)
2. [triangle mesh slicing](/triangle-mesh-slicing/)
3. [staircase effect](/staircase-effect/)
4. [support structure generation](/support-structure-generation/)
5. [toolpath planning](/toolpath-planning/)
6. [cutter location data](/cutter-location-data/)
7. [scallop height](/scallop-height/)
8. [pocket machining](/pocket-machining/)
9. [contour-parallel toolpath](/contour-parallel-toolpath/)
10. [five-axis tool orientation](/five-axis-tool-orientation/)
11. [NC verification](/nc-verification/)
12. [z-map model](/z-map-model/)
13. [feedrate scheduling](/feedrate-scheduling/)
14. [no-fit polygon](/no-fit-polygon/)
15. [topology optimization](/topology-optimization/)

They give the main problem of each part of the chapter and one method for it. On a first pass you can skip
the Voronoi and Fermat spiral paths, the iso-scallop method, collision-free orientation, flank milling, the
dexel representation, the interpolator, the multi-axis decomposition, homogenization, BESO and the level set
method. Each refines a method from the list.
The three groups at the end, checks on the design, nesting and topology optimization, can be read in any
order.

## Before you start

The geometry comes from Volume 13: [Minkowski sums](/minkowski-sum/),
[polygons with holes](/polygon-with-holes/), the [medial axis](/medial-axis/), the
[Voronoi diagram](/voronoi-diagram/) and [convex polytopes](/convex-polytope/). From Volume 28 you need
[polygon meshes](/polygon-mesh/), [parametric surfaces](/parametric-surface/), [NURBS](/nurbs/),
[ruled surfaces](/ruled-surface/), [surface curvature](/surface-curvature/), [offset curves](/offset-curve/)
and the [z-buffer](/z-buffer/). In this volume, [offset surfaces](/offset-surface/),
[constructive solid geometry](/constructive-solid-geometry/) and
[regularized set operations](/regularized-set-operations/) come from solid modeling,
[developable surfaces](/developable-surface/) from surface design, and [indexed face sets](/indexed-face-set/) and [manifold meshes](/manifold-mesh/) from
mesh processing.

Topology optimization needs the
[finite element method](/finite-element-method/) and the [level set method](/level-set-method/) of
Volume 12. Accessibility uses [linear programming](/linear-programming-problem/) and feed scheduling a
[second-order cone program](/second-order-cone-programming/), both from Volume 15. The multi-axis
decomposition uses [beam search](/beam-search/) from Volume 29, and BESO acts like the
[fractional knapsack](/fractional-knapsack/) rule of Volume 2. Nesting builds on
[strip packing](/strip-packing/) and [bin packing](/bin-packing/) from Volume 18, and tolerance stack-up uses
[variance](/variance/) and the [central limit theorem](/central-limit-theorem/) from Volume 1.
