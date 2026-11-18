## What to remember

- A rotation is a matrix $R$ with $R^{\mathsf T} R = I$ and $\det R = +1$. Every rotation turns about a fixed axis by an angle $\theta \in [0, \pi]$, with $\operatorname{tr} R = 1 + 2\cos\theta$. Rotations do not commute: $R_x(\pi/2) R_z(\pi/2) \ne R_z(\pi/2) R_x(\pi/2)$.
- The Rodrigues formula $R = I + \sin\theta\,[\hat\omega] + (1 - \cos\theta)[\hat\omega]^2$ is the closed form of $e^{[\hat\omega]\theta}$; it follows from $[\hat\omega]^3 = -[\hat\omega]$. The logarithm inverts it, and needs separate formulas near $\theta = 0$ and near $\theta = \pi$, where the skew part $R - R^{\mathsf T}$ is small.
- Angular velocity is defined by $\dot R = [\omega_s] R = R[\omega_b]$, with $\omega_s = R\omega_b$. It is not the derivative of any three angles.
- Every chart of SO(3) by three numbers has singular points (Stuelpnagel). For roll, pitch and yaw the singular set is pitch $\pm 90^\circ$, where only $\psi - \phi$ or $\psi + \phi$ is defined and the yaw rate is $1/\cos\theta$ times a body rate. The Cayley parameters $\tan(\theta/2)\,\hat\omega$ have no singular point but miss the half turns.
- A unit quaternion $q = (\cos\frac\theta2, \sin\frac\theta2\,\hat\omega)$ has no singular point, and $q$ and $-q$ give the same rotation. Interpolate with slerp after flipping the sign when $q_0 \cdot q_1 < 0$; convert from a matrix with Shepperd's method, which picks the largest of $w^2, x^2, y^2, z^2$; it is at least $1/4$, so no division by a small number occurs.
- A rigid motion is $T = \begin{pmatrix} R & p \\ 0 & 1 \end{pmatrix}$ in SE(3). Multiplying on the left acts in the fixed frame, on the right in the body frame, and $T^{-1}$ has the blocks $R^{\mathsf T}$ and $-R^{\mathsf T} p$.
- A twist $\mathcal V = (\omega, v)$ gives the velocity $\omega \times x + v$ of the point $x$, and $\operatorname{Ad}_T = \begin{pmatrix} R & 0 \\ [p] R & R \end{pmatrix}$ changes its frame. Every rigid motion is a screw motion (Chasles), and for a screw axis $\mathcal S = (\omega, v)$ with $|\omega| = 1$ the motion $e^{[\mathcal S]\theta}$ has the translation $p = (I\theta + (1 - \cos\theta)[\omega] + (\theta - \sin\theta)[\omega]^2) v$.
- Poses are not vectors. The relative pose of two robots is $T_a^{-1} T_b$, not a difference, and the covariance of a chain is carried to first order by the Jacobians of $\oplus$. With large heading noise the first-order result is poor; the noise model $T = \bar T \operatorname{Exp}(\xi)$ keeps every sample a valid pose.

| Representation | Numbers | Constraints | Covers SO(3) | Fails at |
|---|---|---|---|---|
| [Rotation matrix](/special-orthogonal-group/) | 9 | 6 | once | nowhere |
| [Euler angles](/euler-angles/) (ZYZ) | 3 | none | once away from the lock | $\beta = 0, \pi$ |
| [Roll, pitch, yaw](/roll-pitch-yaw-angles/) | 3 | none | once away from the lock | pitch $\pm 90^\circ$ |
| [Rotation vector](/axis-angle-representation/) $\theta\hat\omega$, $\theta \le \pi$ | 3 | none | once inside the ball | $\theta = \pi$: $r$ and $-r$ |
| [Cayley parameters](/cayley-rotation-parameters/) | 3 | none | all but the half turns | $\theta = \pi$, not reached |
| [Unit quaternion](/unit-quaternion-rotation/) | 4 | 1 | twice | nowhere, but $q \sim -q$ |
| [Dual quaternion](/dual-quaternion/) (rigid motions) | 8 | 2 | SE(3) twice | nowhere, but $\sigma \sim -\sigma$ |

: Ways to store a rotation, and one way to store a rigid motion. "Fails at" names the poses where the chart is singular or not one-to-one.

## Choosing a representation

Store orientations as rotation matrices or unit quaternions, and renormalize them now and then, since rounding drifts them off the group. Quaternions take four numbers and are cheap to renormalize; matrices act on vectors directly and are the natural form inside homogeneous transforms. Show roll, pitch and yaw to people, but do not integrate or filter in them near the lock.

For small changes, such as the error in a filter or the step of an optimizer, use a rotation vector or a twist in the tangent space and apply it with the exponential map: $R \leftarrow R \exp([\delta])$. The error stays near zero, far from any singular point. Write the logarithm with its two special cases, or use a library that does.

For interpolation, use slerp on quaternions with the sign check, or a constant screw for whole rigid motions. For uncertain poses, compound with $\oplus$ and first-order Jacobians when the heading noise is small, and move to the tangent-space model when it is not.
