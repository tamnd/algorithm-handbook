A film character or a game hero has a mesh of tens of thousands of vertices, but an animator moves only a skeleton of a few dozen joints and a handful of facial controls. Character animation is the set of methods that turn those few controls into a moving, deforming body: skinning binds the mesh to the bones, blendshapes add the face, motion capture supplies the poses, and editing, blending and control make the poses fit a new scene, a new body or a game controller in real time. Each step trades exactness for speed or for artistic control, and each has artifacts that animators know by name, such as the collapsing elbow of linear blend skinning or the sliding feet of a blended walk.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Skeletons and skinning.** The skeleton and its bind pose, skeletal animation, linear blend skinning with its candy-wrapper artifact, dual quaternion and spherical blend skinning, optimized centres of rotation, implicit skinning, delta mush and pose space deformation.
2. **Rigging and weights.** Automatic rigging, bounded biharmonic weights and skinning decomposition, which fit bones and weights to example meshes.
3. **Faces.** The blendshape model, direct manipulation of blendshapes, the facial action coding system, example-based facial rigging and deformation transfer between characters.
4. **Editing captured motion.** Motion blending, warping and signal processing, motion graphs and motion matching, registration curves, verbs and adverbs, retargeting to a new skeleton and footskate cleanup.
5. **Inverse kinematics for characters.** Two-bone analytic solutions for arms and legs, and style-based inverse kinematics learned from examples.
6. **Physics-based control and crowds.** Spacetime constraints, SIMBICON and DeepMimic controllers, and crowds by the social force model and continuum crowds.

## What to read meanwhile

Start with the [principles of animation](/principles-of-animation/) and [keyframe interpolation](/keyframe-interpolation/) in the previous chapter, with [squad](/squad/) for joint rotations and [cage-based deformation](/cage-based-deformation/) for an older way to move a mesh. From Volume 37, read the [kinematic chain](/kinematic-chain/), [forward kinematics](/forward-kinematics/), [inverse kinematics](/inverse-kinematics/) with [FABRIK](/fabrik/) and the [damped least-squares method](/damped-least-squares-inverse-kinematics/), [spherical linear interpolation](/spherical-linear-interpolation/) and the [dual quaternion](/dual-quaternion/) behind dual quaternion skinning. For crowds, read [boids](/boids/) and [optimal reciprocal collision avoidance](/optimal-reciprocal-collision-avoidance/), and for the physics of a body, the [rigid body simulation problem](/rigid-body-simulation-problem/).
