A CAD model describes a part by the NURBS patches of its boundary. A finite element solver wants a mesh of the volume and piecewise polynomial basis functions on it. Getting from one to the other takes much of the time of an analysis, and the mesh only approximates the exact shape. Isogeometric analysis, proposed by Hughes, Cottrell and Bazilevs in 2005, uses the spline basis of the CAD model as the basis of the analysis, so the geometry stays exact under refinement. Other routes skip the volume mesh: immersed methods put the part in a background grid and integrate only over the material, and model preparation simplifies a solid before meshing.

The results are of two kinds. Approximation estimates for refined NURBS spaces, and the linear independence of analysis-suitable T-splines, are theorems; general T-splines can have dependent blending functions. Defeaturing and mid-surface extraction are geometric procedures whose effect on the computed answer is judged case by case. Building a spline map of a solid with a positive Jacobian from its boundary remains the main gap between B-rep CAD and isogeometric analysis.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Isogeometric analysis.** The method itself, Bézier extraction, k-refinement, approximation estimates for NURBS spaces, quadrature rules for spline spaces and isogeometric collocation.
2. **Splines with local refinement.** T-splines, analysis-suitable T-splines with their linear independence and local refinement, hierarchical and truncated hierarchical B-splines, LR B-splines and PHT-splines.
3. **Shells, boundaries and shapes.** The isogeometric Kirchhoff-Love shell, subdivision surface shell elements, the isogeometric boundary element method and isogeometric shape optimization.
4. **Volumes, trims and immersed methods.** Volumetric spline parameterization, trimmed isogeometric analysis, the finite cell method, the cut finite element method and immersogeometric analysis.
5. **Preparing CAD models for analysis.** Defeaturing and mid-surface extraction.

## What to read meanwhile

The splines come from Volume 28: the [B-spline](/b-spline/), the [knot vector](/knot-vector/), the [Cox-de Boor recursion](/cox-de-boor-recursion/), the [partition of unity](/partition-of-unity/), [NURBS](/nurbs/), [knot refinement](/knot-refinement/) and [Boehm knot insertion](/boehm-knot-insertion/), and the [Bernstein polynomials](/bernstein-polynomials/) and [Bézier patch](/bezier-patch/) that Bézier extraction maps to. [Loop subdivision](/loop-subdivision/) gives the surfaces of subdivision shells.

The analysis comes from Volume 12: the [Galerkin method](/galerkin-method/), whose error is near-best in the chosen space, the [finite element method](/finite-element-method/), [Gaussian quadrature](/gaussian-quadrature/) and the [Poisson equation](/poisson-equation/) as the model problem. In this volume, the [boundary representation](/boundary-representation/) and the [trimmed surface](/trimmed-surface/) in the chapter on solid modeling describe what a CAD model hands to analysis, and [feature recognition](/feature-recognition/) finds features such as holes in a B-rep, which defeaturing must do before it can remove them. The [medial axis](/medial-axis/) (Volume 13) underlies one approach to mid-surfaces. [Topology optimization](/topology-optimization/), the [SIMP method](/simp-method/) and [level set topology optimization](/level-set-topology-optimization/), in the chapter on CAM and additive manufacturing, couple design with finite element analysis.
