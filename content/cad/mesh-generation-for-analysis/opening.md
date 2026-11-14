Before a solver can compute the stress in a bracket or the flow over a wing, the domain must be divided into simple elements: triangles or quadrilaterals in the plane, tetrahedra or hexahedra in space. The mesh sets both the accuracy and the cost. An element with an angle near $180°$ spoils the interpolation, an inverted element makes the solve meaningless, and elements smaller than needed waste time. The meshes must follow a CAD boundary, with well-shaped elements whose size changes gradually.

The guarantees differ by element type and dimension. Delaunay refinement has proofs: angle bounds in the plane, and in space a bound on the radius-edge ratio that still lets flat slivers through; methods such as sliver exudation and isosurface stuffing add proved bounds on dihedral angles. Every ball bounded by a quadrilateral mesh with an even number of quadrilaterals has a compatible hexahedral mesh in the topological sense, but the theorem gives no practical method, and the hexahedral meshers used in industry are judged by measured quality on test models, as are smoothing and most mesh improvement.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Element quality and size.** Mesh quality measures, the radius-edge ratio, the scaled Jacobian, the Babuška-Aziz maximum angle condition, sliver tetrahedra and mesh sizing functions.
2. **Structured grids.** Structured grid generation, transfinite interpolation and elliptic grid generation.
3. **Triangles and tetrahedra.** Advancing front, quadtree and octree meshing, constrained Delaunay tetrahedralization, boundary recovery, Shewchuk's tetrahedral Delaunay refinement, protecting balls for sharp features, sliver exudation, isosurface stuffing, DistMesh and optimal Delaunay triangulations.
4. **Surfaces, stretched and curved elements.** Meshing in the parameter space of a surface, restricted Delaunay triangulations and Delaunay surface meshing, boundary-layer meshes, metric-based anisotropic adaptation and high-order curved meshes.
5. **Quadrilaterals and hexahedra.** Paving, Q-Morph, Blossom-Quad, medial axis decomposition, the hexahedral existence theorem, the spatial twist continuum, whisker weaving, plastering, sweeping, polycube and frame-field methods.
6. **Mesh improvement.** Optimization-based smoothing, topological improvement of tetrahedral meshes and mesh untangling.

## What to read meanwhile

The planar theory is in Volume 13: [mesh generation](/mesh-generation/) as a problem, the [Delaunay triangulation](/delaunay-triangulation/) and the [constrained Delaunay triangulation](/constrained-delaunay-triangulation/), [Delaunay refinement](/delaunay-refinement/), [Ruppert's algorithm](/ruppert-algorithm/), which proves a smallest angle of about $20.7°$ for inputs with no angle below $60°$, and [Chew's second algorithm](/chew-second-algorithm/). It also has [tetrahedralization](/tetrahedralization/), the [Schönhardt polyhedron](/schonhardt-polyhedron/), which needs Steiner points, the [regular triangulation](/regular-triangulation/) of weighted points, the [centroidal Voronoi tessellation](/centroidal-voronoi-tessellation/) and the [medial axis](/medial-axis/). The [quadtree](/quadtree/) and [octree](/octree/) are in Volume 3.

The solvers that use the meshes are in Volume 12: the [finite element method](/finite-element-method/), the [Galerkin method](/galerkin-method/) and the [finite difference method](/finite-difference-method/). Blossom-Quad rests on [minimum-weight perfect matching](/minimum-weight-perfect-matching/) (Volume 7). In the chapter on mesh processing, [isotropic remeshing](/isotropic-remeshing/), [Laplacian smoothing](/laplacian-smoothing/) and [mixed-integer quadrangulation](/mixed-integer-quadrangulation/) work on surfaces.
