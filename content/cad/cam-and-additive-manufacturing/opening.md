A part designed on a computer still has to be made. A milling machine makes it by cutting material away
from a block. A printer makes it by laying material down, one thin layer at a time. In both cases a program
drives the machine, and that program is computed from the model of the part. This chapter is about those
computations: computer-aided manufacturing (CAM) for cutting, and the slicing and support methods of
additive manufacturing.

Take a bracket stored as a triangle mesh. To print it, the slicer cuts the mesh with a few hundred
horizontal planes, links the cut segments into closed contours, chooses a fill for the inside of each layer,
and adds supports under the parts that hang over air. To mill the same bracket instead, the CAM system
clears its pockets with offset loops or zigzag lines and finishes its curved faces with a ball cutter. It
then simulates the cuts to make sure the tool never digs into the part. Each of these steps is a geometric
algorithm, and most of them come from the geometry of Volume 13 and the surfaces of Volume 28.

The chapter also covers three neighbours of these tasks. Nesting places flat parts on a sheet with little
waste. Topology optimization decides where material should go before the part is drawn. Tolerance analysis
asks whether parts that are each slightly off still fit together.

Keep two kinds of result apart as you read. Some results are exact theorems: a slice computed with exact
comparisons of $z$ values has the right topology, a dexel Boolean on rational endpoints is exact, and a
common access direction exists exactly when a linear program is feasible. The quality of toolpaths, infill,
supports and optimized designs is usually measured on test parts, and the topology optimizers find local
optima only.

## What the chapter covers

1. **Slicing and layers.** [Slicing](/slicing-for-additive-manufacturing/) a mesh into contours, the
   [sweep algorithm](/triangle-mesh-slicing/) whose expected time matches the lower bound, the
   [staircase effect](/staircase-effect/), [adaptive slicing](/adaptive-slicing/) and the
   [infill pattern](/infill-pattern/).
2. **Build orientation and supports.** Choosing the [build orientation](/build-orientation/), and generating
   [support structures](/support-structure-generation/) and [tree supports](/tree-support/).
3. **Toolpaths and cutter positions.** [Toolpath planning](/toolpath-planning/),
   [cutter location data](/cutter-location-data/) for three tool shapes, the
   [scallop height](/scallop-height/) between passes, [gouge detection](/gouge-detection/) and the
   [inverse tool offset](/inverse-tool-offset/).
4. **Pocket machining.** The [pocket machining](/pocket-machining/) problem and its
   [contour-parallel](/contour-parallel-toolpath/), [direction-parallel](/direction-parallel-toolpath/),
   [Voronoi-based](/voronoi-pocket-machining/) and [Fermat spiral](/fermat-spiral-toolpath/) paths.
5. **Surface finishing paths.** [Iso-parametric](/iso-parametric-toolpath/),
   [iso-planar](/iso-planar-toolpath/) and [iso-scallop](/iso-scallop-toolpath/) passes on a free-form
   surface.
6. **Simulation and verification.** The [swept volume](/swept-volume/) of a moving tool,
   [NC verification](/nc-verification/), and its two main data structures, the [z-map](/z-map-model/) and the
   [dexel representation](/dexel-representation/).
7. **Checks on the design.** The [accessibility cone](/accessibility-cone/),
   [mold parting directions](/mold-parting-direction/) and [tolerance stack-up](/tolerance-stack-up/).
8. **Nesting.** The [nesting problem](/nesting-problem/), the [no-fit polygon](/no-fit-polygon/) and
   [bottom-left fill](/bottom-left-fill/).
9. **Topology optimization.** The [problem](/topology-optimization/), the [SIMP method](/simp-method/) and
   the [level set method](/level-set-topology-optimization/).

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
10. [NC verification](/nc-verification/)
11. [z-map model](/z-map-model/)
12. [no-fit polygon](/no-fit-polygon/)
13. [topology optimization](/topology-optimization/)

They give the main problem of each part of the chapter and one method for it. On a first pass you can skip
the Voronoi and Fermat spiral pocket paths, the iso-scallop method, the dexel representation, mold parting
directions and the level set method. Each refines a method from the list. The three groups at the end,
checks on the design, nesting and topology optimization, can be read in any order.

## Before you start

The geometry comes from Volume 13: [Minkowski sums](/minkowski-sum/),
[polygons with holes](/polygon-with-holes/), the [medial axis](/medial-axis/), the
[Voronoi diagram](/voronoi-diagram/) and [convex polytopes](/convex-polytope/). From Volume 28 you need
[polygon meshes](/polygon-mesh/), [parametric surfaces](/parametric-surface/),
[surface curvature](/surface-curvature/), [offset curves](/offset-curve/) and the [z-buffer](/z-buffer/). In
this volume, [offset surfaces](/offset-surface/) and
[regularized set operations](/regularized-set-operations/) come from solid modeling, and
[indexed face sets](/indexed-face-set/) and [manifold meshes](/manifold-mesh/) from mesh processing.

The last groups use other tools. Topology optimization needs the
[finite element method](/finite-element-method/) and the [level set method](/level-set-method/) of
Volume 12. Accessibility uses [linear programming](/linear-programming-problem/) from Volume 15, nesting
builds on [strip packing](/strip-packing/) and [bin packing](/bin-packing/) from Volume 18, and tolerance
stack-up uses [variance](/variance/) and the [central limit theorem](/central-limit-theorem/) from Volume 1.
