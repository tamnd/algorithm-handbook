A scanner returns a million points with triangles between them, and the file has holes where the light did not reach. A CAD system exports a part as an STL file, in which every triangle lists its three corners again, so a cube has 36 points instead of 8. A printer needs a closed surface with a clear inside, a simulation needs triangles of good shape, and a texture needs the surface laid flat. Mesh processing is the work between these steps: clean the mesh, check it, smooth it, measure it, cut it, flatten it and build a better one.

Most of the chapter works on a triangle mesh with flat faces, so every predicate is a sign of a polynomial in the coordinates, and exact rational arithmetic is possible. The guarantees come in four kinds, and the pages keep them apart. Some are identities that hold for every mesh: the angle defects of a closed mesh sum to $2\pi\chi$, and a Tutte map with a convex boundary and positive weights is one to one. Some are proved in exact arithmetic and can fail with floating point predicates, which is the [robustness problem](/geometric-robustness-problem/): the triangle-triangle test, exact Booleans, and the exact geodesic methods. Some are approximations with a stated model, such as the heat method, which converges as the mesh is refined, or Metro, whose estimate is too small by at most the sample spacing. The rest, including smoothing quality, remeshing quality, segmentation and the shape of a filled hole, is measured on examples and not proved.

## What the chapter covers

1. **Meshes as data.** The [indexed face set](/indexed-face-set/) of mesh files, the [manifold mesh](/manifold-mesh/) and its Euler characteristic, and Rossignac's [corner table](/corner-table/).
2. **Cleaning and repair.** [Vertex welding](/vertex-welding/), [consistent mesh orientation](/consistent-mesh-orientation/), the [mesh repair problem](/mesh-repair-problem/), [hole filling](/hole-filling/), [Liepa hole filling](/liepa-hole-filling/) and Ju's [volumetric mesh repair](/volumetric-mesh-repair/).
3. **Intersections, inside tests and Booleans.** [Triangle-triangle intersection](/triangle-triangle-intersection/), [mesh self-intersection](/mesh-self-intersection/), the [generalized winding number](/generalized-winding-number/), [mesh Boolean operations](/mesh-boolean-operations/) and [mesh arrangements](/mesh-arrangements/).
4. **Smoothing and fairing.** [Laplacian smoothing](/laplacian-smoothing/), [Taubin smoothing](/taubin-smoothing/), the [cotangent Laplacian](/cotangent-laplacian/) and [implicit fairing](/implicit-fairing/).
5. **Discrete curvature.** The [discrete Gaussian curvature](/discrete-gaussian-curvature/) as an angle defect and the [discrete Gauss-Bonnet theorem](/discrete-gauss-bonnet-theorem/).
6. **Geodesics.** The [discrete geodesic problem](/discrete-geodesic-problem/), the [MMP algorithm](/mmp-geodesic-algorithm/) and the [heat method](/heat-method/).
7. **Parameterization.** The [mesh parameterization](/mesh-parameterization/) problem, the [Tutte embedding](/tutte-embedding/), [Floater's mean value coordinates](/floater-mean-value-coordinates/), [least squares conformal maps](/least-squares-conformal-maps/) and [angle-based flattening](/angle-based-flattening/).
8. **Remeshing, segmentation and comparison.** [Isotropic remeshing](/isotropic-remeshing/), [mixed-integer quadrangulation](/mixed-integer-quadrangulation/), [mesh segmentation](/mesh-segmentation/) and the [Metro mesh comparison](/metro-mesh-comparison/).

## A first reading

Read these in order:

1. Indexed face set and manifold mesh
2. Vertex welding and consistent mesh orientation
3. The mesh repair problem and hole filling
4. Triangle-triangle intersection
5. Laplacian smoothing and Taubin smoothing
6. The cotangent Laplacian
7. Discrete Gaussian curvature and the discrete Gauss-Bonnet theorem
8. Mesh parameterization and the Tutte embedding
9. Isotropic remeshing

Skip at first the corner table, the MMP algorithm, angle-based flattening, mesh arrangements and mixed-integer quadrangulation. They are either an implementation detail or research methods that build on the core, and they read more easily after it. Read the volumetric repair and the generalized winding number together, once the local repair steps are clear, since both decide where the inside of a broken mesh is.

## Before you start

The chapter assumes the mesh basics of Volume 28, [polygon meshes](/polygon-mesh/) and [surface curvature](/surface-curvature/), and uses [marching cubes](/marching-cubes/) to extract surfaces. From Volume 3 it uses the [hash table](/hash-table/), the [uniform grid](/uniform-grid/), the [octree](/octree/) and the [disjoint set](/disjoint-set/) structure. From Volume 7 it uses [breadth-first search](/breadth-first-search/), [Dijkstra's algorithm](/dijkstra/), the [Laplacian matrix](/laplacian-matrix/), [Euler's formula](/euler-formula/), the [doubly connected edge list](/doubly-connected-edge-list/) and [Tutte's spring theorem](/tutte-spring-theorem/).

The geometric predicates come from Volume 13: the [orientation test](/orientation-test/), the [winding number algorithm](/winding-number-algorithm/), [polygon triangulation](/polygon-triangulation/) with its [dynamic program](/polygon-triangulation-dp/), and the [Hausdorff distance](/hausdorff-distance/). Volume 12 supplies the linear algebra and the floating point background: [least squares](/least-squares-problem/), [conjugate gradients](/conjugate-gradient-method/), the [backward Euler method](/backward-euler-method/), the [heat equation](/heat-equation/), [catastrophic cancellation](/catastrophic-cancellation/) and [exact predicates](/shewchuk-expansion-sum/). Within this volume, [regularized set operations](/regularized-set-operations/) from the solid modelling chapter define what a Boolean of two solids is.
