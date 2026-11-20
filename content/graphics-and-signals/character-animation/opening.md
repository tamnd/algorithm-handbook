A game character runs, turns and ducks under a branch, and its skin follows the bones without tearing. A film face smiles, and the corners of the mouth crease in the way the sculptor made them. Neither is drawn frame by frame. A skeleton carries the motion, a skinning method moves the mesh with it, and the motion comes from keys, from motion capture, from a physics simulation or from a search over a database.

Two questions run through the chapter. The first is how a mesh follows a skeleton. Linear blend skinning mixes the joint matrices with weights, and it is fast. But a mix of rotations is not a rotation, so twisted and bent joints lose volume. Most skinning entries trade some speed or a precomputation for a blend that stays rigid. The second question is how to get new motion from old motion. Captured clips must be aligned before they are mixed, edits move the feet, and a character of other proportions needs the motion adapted to it. The methods differ in what they promise. Skinning formulas and inverse kinematics solves have exact properties. Motion graphs and motion matching are data-driven searches, and the physics controllers are judged by measurements.

## What the chapter covers

1. **Skeletons and linear blend skinning.** The [character skeleton](/character-skeleton/), the [bind pose](/bind-pose/) and [skeletal animation](/skeletal-animation/) set up the joints and their transforms. The [skinning problem](/character-skinning/) states what a method should do, [linear blend skinning](/linear-blend-skinning/) is the standard answer, and the [candy wrapper artifact](/candy-wrapper-artifact/) is its best known failure.
2. **Rigid blends.** [Dual quaternion skinning](/dual-quaternion-skinning/), [spherical blend skinning](/spherical-blend-skinning/) and [optimized centers of rotation](/optimized-centers-of-rotation-skinning/) give a rigid transform at every vertex. [Implicit skinning](/implicit-skinning/) adds fields around the bones to model contact.
3. **Corrections on top of skinning.** [Delta mush](/delta-mush/) smooths the skinned mesh and restores stored detail, and [pose space deformation](/pose-space-deformation/) interpolates sculpted fixes over the pose.
4. **Rigs and weights.** [Automatic rigging](/automatic-rigging/) embeds a skeleton and computes heat weights, [bounded biharmonic weights](/bounded-biharmonic-weights/) solve a bounded smoothness problem, and [skinning decomposition](/skinning-decomposition/) fits bones and weights to a mesh animation.
5. **Faces.** The [blendshape model](/blendshape-model/), the [Facial Action Coding System](/facial-action-coding-system/), [direct manipulation of blendshapes](/blendshape-direct-manipulation/), [deformation transfer](/deformation-transfer/) and [example-based facial rigging](/example-based-facial-rigging/).
6. **Blending and editing captured motion.** [Motion blending](/motion-blending/), [verbs and adverbs](/verbs-and-adverbs/), [motion warping](/motion-warping/) and [motion signal processing](/motion-signal-processing/).
7. **Motion from a database.** The [motion graph](/motion-graph/) precomputes transitions between clips, [registration curves](/registration-curves/) align clips before a blend, and [motion matching](/motion-matching/) searches for the next frame at run time.
8. **Constraints and new characters.** [Spacetime constraints](/spacetime-constraints/) optimize a whole motion, and [two-bone inverse kinematics](/two-bone-inverse-kinematics/), [motion retargeting](/motion-retargeting/), [footskate cleanup](/footskate-cleanup/) and [style-based inverse kinematics](/style-based-inverse-kinematics/) fix the limbs and adapt the motion to a new body.
9. **Physics-based control.** [SIMBICON](/simbicon/) controls a simulated biped with simple rules, and [DeepMimic](/deepmimic/) learns to track a clip.
10. **Crowds.** The [social force model](/social-force-model/) pushes people as particles, and [continuum crowds](/continuum-crowds/) plan for a whole crowd with one potential per group.

## A first reading

Read these in order:

1. character skeleton;
2. skeletal animation;
3. linear blend skinning;
4. the candy wrapper artifact;
5. dual quaternion skinning;
6. the blendshape model;
7. motion blending;
8. motion warping;
9. the motion graph;
10. motion matching;
11. two-bone inverse kinematics;
12. SIMBICON.

The first five carry all the skinning entries. The bind pose and the skinning problem are short and fill in the details. Spherical blend skinning, optimized centers, implicit skinning and delta mush can wait. Each one fixes a fault of linear or dual quaternion skinning that you will know by then. The face entries after the blendshape model, the rigging entries, registration curves, verbs and adverbs, motion signal processing, style-based inverse kinematics, DeepMimic and the two crowd entries can be read in any order on a second pass.

## Before you start

The skeleton entries assume rigid transforms: [homogeneous transformation matrices](/homogeneous-transformation-matrix/), [unit quaternions](/unit-quaternion-rotation/), [slerp](/spherical-linear-interpolation/) and [dual quaternions](/dual-quaternion/), all in Volume 37. [Forward kinematics](/forward-kinematics/) and [inverse kinematics](/inverse-kinematics/), with [FABRIK](/fabrik/) and [damped least squares](/damped-least-squares-inverse-kinematics/), are also there. [Keyframe interpolation](/keyframe-interpolation/) and [squad](/squad/) in Chapter 28.8 come before motion editing.

Several entries rest on numerical tools from Volume 12: [least squares problems](/least-squares-problem/) for faces and retargeting, [radial basis function interpolation](/radial-basis-function-interpolation/) for pose space deformation and verbs and adverbs, and the [fast marching method](/fast-marching-method/) for continuum crowds. The [cotangent Laplacian](/cotangent-laplacian/) of Volume 31 and [quadratic programming](/quadratic-programming/) of Volume 15 appear in the weight methods. The motion graph prunes with [Tarjan's algorithm](/tarjan-scc/) from Volume 7, and motion matching uses a [k-d tree](/kd-tree/) from Volume 3. DeepMimic trains with [PPO](/ppo/) from Volume 25. The physics controllers run on a rigid body simulator; see the [rigid body simulation problem](/rigid-body-simulation-problem/) of Chapter 28.10.
