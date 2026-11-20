## What to remember

- A skeleton is a tree of joints stored in parent order. Forward kinematics computes all world transforms in one pass, $M_i = M_{p(i)} L_i$, in $O(j)$ time. Skinning uses $C_i = M_i B_i^{-1}$, which is the identity in the bind pose.
- Linear blend skinning computes $v' = (\sum_i w_i C_i)\,v$ in $O(j + nk)$ time per frame. A weighted sum of rotation matrices is not a rotation. For a twist by $\theta$ at the weight $1/2$, the section shrinks by the factor $|\cos(\theta/2)|$, which is 0 at a half turn: the candy wrapper.
- Dual quaternion skinning gives a rigid transform at every vertex. Align the signs to the pivot of largest weight before you blend. It costs about as much as linear blending, but it bulges at bends and cannot scale. Optimized centers of rotation precompute one center per vertex; that they bulge less is a measurement.
- Corrections sit on top of a skinning method. Pose space deformation interpolates sculpted offsets over the pose with a positive definite Gaussian system, and it must add them in the rest frame before skinning. Delta mush smooths and restores stored detail, but it does not cure a candy wrapper.
- A blendshape face is $v = b_0 + Dw$. Fitting the weights is a least squares problem. Its solution is unique only if the deltas are independent; a regularizer toward the current weights fixes that and keeps drags predictable.
- Before blending motions, align them in time, on the ground and in quaternion sign, or feet cross and slide. Registration curves find the alignment by dynamic programming.
- Every edit moves the feet. Retargeting solves for a smooth least-norm displacement under constraints. Footskate cleanup pins planted feet with closed-form two-bone solves, and a stretch is allowed only within a set limit.
- Motion graphs precompute transitions and keep the largest strongly connected component, so playback never gets stuck. Motion matching searches the whole database every few frames. Both searches are exact; whether the result looks good is judged by eye.
- Spacetime optimization, SIMBICON and DeepMimic make motion that obeys physics. The controllers are shown to work by measurements, not proofs.

| Method | Rigid per vertex | Cost per frame | Main fault |
|---|---|---|---|
| [Linear blend](/linear-blend-skinning/) | no | $O(j + nk)$ | collapse in twists and bends |
| [Dual quaternion](/dual-quaternion-skinning/) | yes, after sign alignment | $O(j + nk)$ | bulge at bends, no scale |
| [Spherical blend](/spherical-blend-skinning/) | yes | $O(j + nk^2)$ | a center per joint set, each frame |
| [Optimized centers](/optimized-centers-of-rotation-skinning/) | yes | $O(j + nk)$ | $O(nmk^2)$ precomputation |
| [Implicit skinning](/implicit-skinning/) | no | $O(j + n(k + ij))$ | field setup, iterations per vertex |
| [Delta mush](/delta-mush/) | no | $O(j + nk + K(n + f))$ | no cure for twists |
| [Pose space deformation](/pose-space-deformation/) | no | $O(md + nm)$ on top of skinning | sculpted examples needed |

: Skinning methods of the chapter, for $n$ vertices, $f$ faces, $j$ joints and $k$ influences per vertex. For optimized centers $m$ counts the triangles of the refined rest mesh; for pose space deformation it counts the examples, with $d$ pose dimensions. $K$ is the number of smoothing steps and $i$ the number of projection iterations.

## Choosing a method

For a game character, start with linear blend skinning, and switch to dual quaternion skinning when forearms or necks collapse in twists. If the bulge at elbows then shows, use optimized centers of rotation. For film, put pose space deformation or delta mush on top of skinning, and use implicit skinning where skin presses on skin. For weights without painting, use bounded biharmonic weights for mixed handles, heat weights for a quick rig, and skinning decomposition to turn a simulated mesh animation into a rig.

For faces, name blendshape targets after FACS action units, edit with direct manipulation, and copy a generic rig to a new actor with deformation transfer, refined by example-based rigging when scans exist.

For locomotion from capture, use motion matching when the database is large and the input changes fast. Use a motion graph when the transitions must be checked ahead of time. Use registration curves or verbs and adverbs for parametric blends. After any edit, retarget to the new proportions and clean up footskate with two-bone inverse kinematics. Use a physics controller when the character must react to pushes, and spacetime optimization for a short motion with known events. For crowds, social forces suit dense local pushing, and continuum crowds suit large groups that share goals.
