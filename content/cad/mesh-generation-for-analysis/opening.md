A bracket drawn in a CAD system is a boundary: a few dozen faces, each a patch of a plane, cylinder or spline. A finite element solver cannot use that. It needs the solid cut into small triangles, quadrilaterals, tetrahedra or hexahedra, it needs each element to be well shaped, and it needs small elements only where the solution changes fast. A triangle with an angle near $180°$ spoils the gradient of the interpolant, a tetrahedron with an angle near $0°$ spoils the stiffness matrix, and an inverted element makes the result meaningless. Mesh generation for analysis is the work of producing such a mesh from the boundary, and of improving it afterwards.

The guarantees come in four kinds, and the pages keep them apart. Some are proved quality bounds: the quadtree method bounds every angle, isosurface stuffing bounds every dihedral angle, and Delaunay refinement bounds the radius-edge ratio of every tetrahedron when the input has no angle below $90°$. That last bound allows flat slivers, and the proved fix, sliver exudation, gives an angle constant too small to state. Some are topological: a ball whose boundary has an even number of quadrilaterals has a hexahedral mesh with that boundary, but the theorem says nothing about its quality. Some are monotone: a smoothing or flipping step never makes the worst element worse. The rest, including advancing front, paving, whisker weaving and frame-field meshing, are heuristics judged by the quality they reach on test models.

## What the chapter covers

1. **Element quality and size.** [Mesh quality measures](/mesh-quality-measures/), the [radius-edge ratio](/radius-edge-ratio/), the [sliver tetrahedron](/sliver-tetrahedron/), the [scaled Jacobian](/scaled-jacobian/), the [maximum angle condition](/maximum-angle-condition/) of Babuška and Aziz, and the [mesh sizing function](/mesh-sizing-function/).
2. **Structured grids.** [Structured grid generation](/structured-grid-generation/), [transfinite interpolation](/transfinite-interpolation-grid/) and [elliptic grid generation](/elliptic-grid-generation/).
3. **Fronts, trees and lattices.** The [advancing front](/advancing-front-mesh-generation/) method, [quadtree](/quadtree-mesh-generation/) and [octree](/octree-mesh-generation/) meshing, [isosurface stuffing](/isosurface-stuffing/) and [DistMesh](/distmesh/).
4. **Delaunay tetrahedral meshing.** The [constrained Delaunay tetrahedralization](/constrained-delaunay-tetrahedralization/), [boundary recovery](/boundary-recovery/), Shewchuk's [tetrahedral Delaunay refinement](/tetrahedral-delaunay-refinement/), [sliver exudation](/sliver-exudation/) and the [optimal Delaunay triangulation](/optimal-delaunay-triangulation/).
5. **Surfaces and sharp features.** [Parametric surface meshing](/parametric-surface-meshing/), the [restricted Delaunay triangulation](/restricted-delaunay-triangulation/), [Delaunay surface meshing](/delaunay-surface-meshing/) and [protecting balls](/protecting-balls/).
6. **Stretched and curved elements.** [Boundary layer meshes](/boundary-layer-mesh-generation/), [anisotropic mesh adaptation](/anisotropic-mesh-adaptation/) and [high-order meshes](/high-order-mesh-generation/).
7. **Quadrilaterals.** [Paving](/paving/), [Q-Morph](/q-morph/) and [Blossom-Quad](/blossom-quad/).
8. **Hexahedra.** [Hexahedral mesh generation](/hexahedral-mesh-generation/) as a problem, the [spatial twist continuum](/spatial-twist-continuum/), the [hexahedral mesh existence theorem](/hexahedral-mesh-existence-theorem/), [whisker weaving](/whisker-weaving/), [plastering](/plastering/), [sweeping](/hexahedral-sweeping/), [medial axis decomposition](/medial-axis-decomposition-meshing/), [polycube](/polycube-hex-meshing/) and [frame-field](/frame-field-hex-meshing/) methods.
9. **Mesh improvement.** [Optimization-based smoothing](/optimization-based-mesh-smoothing/), [mesh untangling](/mesh-untangling/) and [topological improvement](/topological-tetrahedral-mesh-improvement/) of tetrahedral meshes.

## A first reading

Read these in order:

1. Mesh quality measures and the radius-edge ratio
2. The sliver tetrahedron and the scaled Jacobian
3. The maximum angle condition
4. The mesh sizing function
5. Structured grid generation
6. The advancing front method
7. Tetrahedral Delaunay refinement
8. Parametric surface meshing
9. Paving
10. Hexahedral mesh generation
11. Optimization-based mesh smoothing

Skip at first protecting balls, Delaunay surface meshing, whisker weaving and frame-field meshing. The first two need the restricted Delaunay triangulation and the sampling theory behind it, and the last two need the dual-sheet view of a hex mesh from the spatial twist continuum. Read sliver exudation together with the regular triangulation, since the method is a choice of weights.

## Before you start

The planar theory is in Volume 13, and the pages here do not repeat it: [mesh generation](/mesh-generation/) as a problem, the [Delaunay triangulation](/delaunay-triangulation/), the [constrained Delaunay triangulation](/constrained-delaunay-triangulation/), [Delaunay refinement](/delaunay-refinement/) and [Ruppert's algorithm](/ruppert-algorithm/), which proves a smallest angle of about $20.7°$ for inputs with no angle below $60°$. Volume 13 also has [tetrahedralization](/tetrahedralization/), the [Schönhardt polyhedron](/schonhardt-polyhedron/), [Steiner points](/steiner-points/), the [regular triangulation](/regular-triangulation/), the [centroidal Voronoi tessellation](/centroidal-voronoi-tessellation/), the [medial axis](/medial-axis/) and the [orientation test](/orientation-test/). The [quadtree](/quadtree/), [octree](/octree/) and [disjoint set](/disjoint-set/) are in Volume 3.

The solvers that use the meshes are in Volume 12: the [finite element method](/finite-element-method/), the [Galerkin method](/galerkin-method/), the [finite difference method](/finite-difference-method/) and the [finite volume method](/finite-volume-method/), with the [Lipschitz condition](/lipschitz-condition/) behind sizing functions. Blossom-Quad uses [minimum-weight perfect matching](/minimum-weight-perfect-matching/) from Volume 7, and isosurface stuffing uses the [signed distance function](/signed-distance-function/) of Volume 28. On surfaces, [isotropic remeshing](/isotropic-remeshing/), [cross fields](/cross-field/) and [mixed-integer quadrangulation](/mixed-integer-quadrangulation/) in the mesh processing chapter do the related work on a mesh that already exists.
