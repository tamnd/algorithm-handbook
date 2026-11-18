## What to remember

- [Keyframe interpolation](/keyframe-interpolation/) fits a curve through the keys. The Catmull-Rom tangent at key $i$ is $\tfrac12(p_{i+1} - p_{i-1})$ for unit spacing, which gives a local $C^1$ curve. Kochanek-Bartels adds tension, continuity and bias to that tangent. A $C^2$ interpolant needs a global solve.
- An [ease curve](/ease-in-ease-out/) is a monotone map $e$ of $[0, 1]$ onto itself with $e'(0) = e'(1) = 0$, so a motion starts and ends at rest. The cubic $3t^2 - 2t^3$ has peak speed $3/2$ times the average. The [arc length table](/arc-length-table/) inverts arc length by binary search and $r$ Newton steps.
- [Squad](/squad/) passes through its unit quaternion keys with three nested slerps per segment and is $C^1$. The [cumulative B-spline quaternion curve](/cumulative-b-spline-quaternion-curve/) is $C^2$ but only approximates its control rotations.
- A [rotation minimizing frame](/rotation-minimizing-frame/) has normals that do not turn about the tangent. The Frenet normal flips at an inflection and twists along a helix. The [double reflection method](/double-reflection-method/) uses two reflections per step, with a global error of $O(h^4)$.
- [Barr's deformations](/barr-global-deformations/) move a point by a matrix that varies along an axis, and move normals by the inverse transpose Jacobian. The bend has $\det J = 1 - kz$ inside its region and is only $C^0$ at the region ends.
- [Free-form deformation](/free-form-deformation/) sends $X$ to $\sum_{i,j,k} B_i^l(s) B_j^m(t) B_k^n(u) P_{ijk}$. It is the identity at rest, reproduces affine maps and does not interpolate the control points. It folds space where the Jacobian determinant reaches 0.
- [Cage coordinates](/generalized-barycentric-coordinates/) with partition of unity $\sum_i \lambda_i = 1$ and linear precision $\sum_i \lambda_i v_i = x$ reproduce every affine map of the cage. [Mean value coordinates](/floater-mean-value-coordinates/) have a closed form but can be negative in a concave cage. [Harmonic coordinates](/harmonic-coordinates/) are never negative but need a grid solve. [Green coordinates](/green-coordinates/) give conformal maps in 2D but reproduce only similarities.
- [As-rigid-as-possible manipulation](/as-rigid-as-possible-shape-manipulation/) meets its handles exactly and reproduces rigid motions; nothing stops a triangle from flipping. [As-rigid-as-possible interpolation](/as-rigid-as-possible-shape-interpolation/) splits each triangle's map into a rotation and a stretch, interpolates them apart and fits vertices by least squares.

| Method | Passes through | Keeps | Cost |
|---|---|---|---|
| Catmull-Rom keys | keys | $C^1$ | $\Theta(1)$ per frame |
| Squad | keys | $C^1$ | $\Theta(n)$ build, $\Theta(1)$ query |
| Cumulative B-spline | no | $C^2$ | $\Theta(n)$ build, $\Theta(1)$ query |
| Arc length table | sample points | speed up to table error | $\Theta(m)$ build, $O(\log m + r)$ query |
| Double reflection | samples | frame to $O(h^4)$ | $\Theta(N)$ |
| Barr bend, twist, taper | n/a | $C^0$ at bend ends | $\Theta(Ng)$ |
| Free-form deformation | no | affine maps | $\Theta(lmn)$ per point |
| Extended FFD | no | glued lattices | $O(NcKq)$ embed, $\Theta(Nq)$ deform |
| Wires | n/a | rest pose | $\Theta(NwV)$ |
| Mean value coordinates | cage vertices | affine maps | $\Theta(n)$ per point |
| Harmonic coordinates | cage vertices | affine maps, $\lambda_i \ge 0$ | $O(G^4 + nG^3)$ setup, $O(n)$ per point |
| Green coordinates | no | similarities, conformal in 2D | $\Theta(n)$ per point |
| ARAP manipulation | handles | rigid motions | $O(n^3 + m)$ setup, $O(n^2 + m)$ per move |
| ARAP interpolation | both shapes | turning triangles | $O(n^3 + m)$ setup, $O(n^2 + m)$ per frame |
| Beier-Neely morphing | n/a | n/a | $\Theta(nL)$ per image |

: The main methods. $n$ is the number of keys, cage vertices or mesh vertices; $N$ the number of points moved; $m$ the table size or the number of triangles; $l, m, n$ in FFD the lattice degrees; $G$ the grid side; $w$ wires of $V$ samples; $L$ line pairs.

## Choosing a method

For position channels, start with Catmull-Rom keys and reshape time with an ease curve. Use Kochanek-Bartels to tighten or loosen a key. Move along a path at a set speed with an arc length table. For rotations, use squad when the keys must be met and the cumulative B-spline curve when smooth angular acceleration matters more. Orient a camera along a path with the double reflection method, not the Frenet frame.

For deformation, choose by the handle the artist wants. Barr's operations bend or twist a whole object about an axis, free-form deformation uses a box of control points, wires follow a crease, and cages wrap a detailed model in a coarse shell. Take mean value coordinates by default, harmonic coordinates when the cage is concave, and Green coordinates when details must keep their angles. For a 2D shape dragged by a few points, use as-rigid-as-possible manipulation. To morph two meshes with the same triangles, use as-rigid-as-possible interpolation, and to morph two images, use Beier-Neely.
