A drone reads its gyroscopes many times a second and must turn those readings into an orientation. A robot arm must say where its gripper is, both the point and the way the fingers face, before it can reach for a cup. A mapping robot must chain a hundred small measured steps into one pose, and say how sure it is of the result. Each of these tasks needs a way to write down how a solid body sits in space and how it moves, and a way to compute with it that does not break at some unlucky pose. This chapter gives those ways.

A rigid motion keeps every distance. It is a rotation followed by a translation, $x \mapsto Rx + p$, and the hard part is the rotation. There are many ways to store one: a $3 \times 3$ matrix, three angles, an axis and an angle, a unit quaternion. Each is right for some job and wrong for another. Three angles are easy to read but lose one degree of freedom at some pose, and Stuelpnagel's theorem shows that every three-number chart has this flaw. A quaternion never does, but $q$ and $-q$ give the same rotation, and an interpolation that forgets this takes the long way round. The chapter states each representation exactly, gives the conversions between them with their special cases, and then builds velocities, forces and uncertainty on top.

## What the chapter covers

1. **Rotations in space.** A [skew-symmetric matrix](/skew-symmetric-matrix-of-a-vector/) $[\omega]$ writes the cross product as a matrix product. Rotations form the group [SO(3)](/special-orthogonal-group/), and [Euler's rotation theorem](/euler-rotation-theorem/) says each one turns about a fixed axis. The [Rodrigues formula](/rodrigues-rotation-formula/) builds the matrix from the [axis and angle](/axis-angle-representation/), and the [SO(3) logarithm](/so3-logarithm-map/) recovers them. [Angular velocity](/angular-velocity/) is the vector $\omega$ with $\dot R = [\omega_s] R$.
2. **Angles as coordinates.** [Euler angles](/euler-angles/) and [roll, pitch and yaw](/roll-pitch-yaw-angles/) use three turns about chosen axes. At some poses two axes line up, and [gimbal lock](/gimbal-lock/) makes one angle undefined and the angle rates unbounded.
3. **Quaternions.** A [unit quaternion](/unit-quaternion-rotation/) stores a rotation in four numbers. [Shepperd's method](/shepperd-method/) converts a matrix to a quaternion without dividing by a small number, [slerp](/spherical-linear-interpolation/) interpolates at constant angular rate, and the [quaternion kinematic equation](/quaternion-kinematic-equation/) integrates gyroscope readings. The [Cayley parameters](/cayley-rotation-parameters/) are a rational three-number chart, and [Stuelpnagel's theorem](/stuelpnagel-theorem/) proves that no three-number chart is free of singular points.
4. **Rigid motions and poses.** A [rigid body transformation](/rigid-body-transformation/) is written as a [homogeneous transformation matrix](/homogeneous-transformation-matrix/), and these matrices form the group [SE(3)](/special-euclidean-group/). A [robot pose](/robot-pose/) is one element of it.
5. **Twists, screws and wrenches.** A [twist](/rigid-body-twist/) is the six-number velocity of a body, and the [adjoint map](/adjoint-map-se3/) moves it between frames. [Screw motion](/screw-motion/) and [Chasles' theorem](/chasles-theorem/) say every rigid motion turns about a line and slides along it, and the [SE(3) exponential map](/se3-exponential-map/) computes that motion. A [wrench](/wrench/) is the force that pairs with a twist, and a [dual quaternion](/dual-quaternion/) stores a rigid motion in eight numbers.
6. **Uncertain poses.** The [pose compounding operators](/pose-compounding-operators/) chain relative poses and their covariances, and [uncertainty on Lie groups](/uncertainty-on-lie-groups/) puts the noise in the tangent space of the group.

## A first reading

Read these twelve entries in order:

1. [Skew-symmetric matrix of a vector](/skew-symmetric-matrix-of-a-vector/)
2. [Special orthogonal group SO(3)](/special-orthogonal-group/)
3. [Euler's rotation theorem](/euler-rotation-theorem/)
4. [Rodrigues' rotation formula](/rodrigues-rotation-formula/)
5. [Axis-angle representation](/axis-angle-representation/)
6. [Angular velocity](/angular-velocity/)
7. [Roll-pitch-yaw angles](/roll-pitch-yaw-angles/)
8. [Gimbal lock](/gimbal-lock/)
9. [Unit quaternion representation of rotation](/unit-quaternion-rotation/)
10. [Homogeneous transformation matrix](/homogeneous-transformation-matrix/)
11. [Pose](/robot-pose/)
12. [Twist](/rigid-body-twist/)

The general Euler angle conventions can wait; roll, pitch and yaw show every point that matters. Skip at first the Cayley parameters, dual quaternions, Shepperd's method and Stuelpnagel's theorem. The last group, on uncertain poses, needs the exponential map and the adjoint, and is best read just before the chapters on localization and SLAM.

## Before you start

The chapter uses the [cross product](/cross-product/) from Volume 13, the [determinant](/determinant/) from Volume 11 and [eigenvalues](/eigenvalue/) from Volume 12. The exponential map is a [matrix exponential](/matrix-exponential/), which Volume 36 treats in full. The last group uses the [covariance matrix](/covariance-matrix/) from Volume 25. Rotation in the plane, the case with one angle and no difficulties, is the [vector rotation](/vector-rotation/) entry of Volume 13. Linear algebra with $3 \times 3$ matrices, and the derivative of a matrix that depends on time, are assumed.
