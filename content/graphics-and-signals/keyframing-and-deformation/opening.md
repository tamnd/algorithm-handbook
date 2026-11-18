An animator does not draw every frame. In a keyframed shot, the animator sets the position of a door at frame 1 and at frame 24, its angle at a few frames in between, and the computer fills in the rest. The filled frames must pass through the keys, move without jerks, start and stop the way a real door does, and turn the door about its hinge rather than through its frame. A second kind of work changes shape rather than position: a character's cheek bulges, a tube bends, a logo twists into a spiral. Here the artist moves a few handles, a lattice, a cage or a curve, and every point of a detailed model must follow in a smooth and predictable way.

This chapter covers both jobs. The methods are small and exact: most are a spline formula, a weighted sum or a short least-squares solve, and their entries prove what they keep (the keys, the affine maps, the rigid motions) and say plainly where they fail (folds, negative weights, flips).

## What the chapter covers

1. **Keys and timing.** The [principles of animation](/principles-of-animation/) say what good motion looks like. [Keyframe interpolation](/keyframe-interpolation/) fits splines through the keys, [ease-in and ease-out](/ease-in-ease-out/) reshapes time so that motion starts and ends at rest, and the [arc length table](/arc-length-table/) moves a point along a curve at a set speed.
2. **Interpolating rotations.** [Squad](/squad/) interpolates unit quaternions with a $C^1$ curve through the keys. The [cumulative B-spline quaternion curve](/cumulative-b-spline-quaternion-curve/) is $C^2$ but does not pass through its control rotations.
3. **Frames along a path.** The [rotation minimizing frame](/rotation-minimizing-frame/) follows a curve without spinning about the tangent, and the [double reflection method](/double-reflection-method/) computes it from samples with an error of order $h^4$.
4. **Deforming space.** The [shape deformation](/shape-deformation/) problem, then [Barr's taper, twist and bend](/barr-global-deformations/), [free-form deformation](/free-form-deformation/) in a Bezier lattice, its [extension](/extended-free-form-deformation/) to curved lattices, and [wires](/wire-deformation/).
5. **Cage coordinates.** [Generalized barycentric coordinates](/generalized-barycentric-coordinates/) write a point as a weighted sum of polygon vertices. [Cage-based deformation](/cage-based-deformation/) uses them to move a model with a coarse cage, and [Green coordinates](/green-coordinates/) and [harmonic coordinates](/harmonic-coordinates/) are two other choices of the weights.
6. **Rigidity and morphing.** [As-rigid-as-possible manipulation](/as-rigid-as-possible-shape-manipulation/) deforms a 2D mesh from handles, [as-rigid-as-possible interpolation](/as-rigid-as-possible-shape-interpolation/) morphs one mesh into another, and [Beier-Neely morphing](/beier-neely-morphing/) morphs images with line pairs.

## A first reading

For a first pass, read these entries in this order:

1. [Principles of animation](/principles-of-animation/)
2. [Keyframe interpolation](/keyframe-interpolation/)
3. [Ease-in and ease-out](/ease-in-ease-out/)
4. [Arc length table](/arc-length-table/)
5. [Squad](/squad/)
6. [Rotation minimizing frame](/rotation-minimizing-frame/)
7. [Shape deformation](/shape-deformation/)
8. [Barr's global deformations](/barr-global-deformations/)
9. [Free-form deformation](/free-form-deformation/)
10. [Generalized barycentric coordinates](/generalized-barycentric-coordinates/)
11. [Cage-based deformation](/cage-based-deformation/)
12. [As-rigid-as-possible shape manipulation](/as-rigid-as-possible-shape-manipulation/)

They give the core of each group: splines through keys, time reshaping, rotation curves, moving frames, lattice and cage deformation, and one method that keeps triangles rigid. The other eight entries refine these and can wait. The cumulative B-spline curve and the double reflection method need squad and the rotation minimizing frame first. Extended free-form deformation needs Newton's method in three unknowns. Green and harmonic coordinates are alternatives to mean value coordinates and are best read side by side. Wires and Beier-Neely morphing stand on their own and can be read at any time.

## Before you start

The chapter leans on the curves chapter of this volume. Keyframe interpolation uses [Hermite splines](/hermite-spline/) and [Catmull-Rom splines](/catmull-rom-spline/). Free-form deformation is a [Bezier curve](/bezier-curve/) in three variables, built like a [tensor product surface](/tensor-product-surface/), and the cumulative curve and wires use [B-splines](/b-spline/). The rotation minimizing frame is defined against the [Frenet frame](/frenet-frame/), and the arc length table inverts the [arc length parametrization](/arc-length-parametrization/). Beier-Neely morphing is an [image warp](/image-warping/) from the image processing chapter.

From Volume 12, you need [barycentric interpolation](/barycentric-interpolation/), [bilinear interpolation](/bilinear-interpolation/), [Gauss-Legendre quadrature](/gauss-legendre-quadrature/), the [least-squares problem](/least-squares-problem/), the [singular value decomposition](/singular-value-decomposition/), the [Cholesky decomposition](/cholesky-decomposition/), [Newton's method for systems](/newton-method-for-systems/) and the [finite difference method](/finite-difference-method/). Rotations come from Volume 37: [unit quaternion rotation](/unit-quaternion-rotation/) and [spherical linear interpolation](/spherical-linear-interpolation/). The arc length table also uses [binary search](/binary-search/) from Volume 5. Calculus of curves in the plane and in space, and the chain rule for Jacobians, are assumed.
