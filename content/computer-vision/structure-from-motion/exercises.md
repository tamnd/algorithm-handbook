1. ◦ In the [structure from motion problem](/structure-from-motion-problem/) for two views, each point adds 3 unknowns and 4 measurements. Count how many points are needed when the cameras are calibrated (5 unknowns of relative pose) and when they are not (7 for the fundamental matrix).

2. ◦ A [bundle adjustment](/bundle-adjustment/) has 100 cameras with 6 parameters and 50000 points. How many unknowns are there? Compare the cost $n^3/3$ of a dense Cholesky factorization with the cost of factoring the [reduced camera system](/reduced-camera-system/).

3. ◦ Run three steps of the [Gauss-Newton algorithm](/gauss-newton-algorithm/) on the single residual $r(x) = x^2 - 2$ from $x_0 = 1$. Which method of root finding does it reduce to here?

4. ◦ One residual $r = 2$ has the Jacobian $J = (1, 1)$ in two parameters, so $J^{\mathsf T} J$ is singular. Compute the [Levenberg-Marquardt](/levenberg-marquardt/) step with $D = I$ for $\mu = 1$, $\mu = 0.1$ and $\mu \to 0$, and say which step the limit is.

5. ◦ A monocular [visual odometry](/visual-odometry/) system overestimates the scale of each step by 1 percent. What is the scale error after 100 steps? What if it underestimates by 1 percent?

6. ◦ A camera records 30 frames per second for 10 minutes. How many frames are there, and how many keyframes if [keyframe selection](/keyframe-selection/) keeps one every half second?

7. ◦ Build the [feature tracks](/feature-track/) of the matches $(A_1, B_1)$, $(B_1, C_2)$, $(C_2, A_3)$ and $(A_2, B_3)$, where $A_1$ is feature 1 of image $A$. Which track is inconsistent, and why?

8. • Dennis and Schnabel give the residuals $r_1 = x + 1$ and $r_2 = \lambda x^2 + x - 1$. Show that $x = 0$ is a stationary point of $\frac12 (r_1^2 + r_2^2)$ with second derivative $2 - 2\lambda$, and that a [Gauss-Newton](/gauss-newton-algorithm/) step near 0 gives $x_+ \approx \lambda x$. Run the method for $\lambda = 0.5$, $-0.5$ and $-2$ from $x_0 = 0.1$, and explain the result for $\lambda = -2$, where 0 is a strict minimum.

9. • For $J = \operatorname{diag}(2, 1)$ and $r = (2, 2)$, compute the Gauss-Newton step $b$, the gradient $g = J^{\mathsf T} r$ and the Cauchy point $a = -\alpha g$ with $\alpha = \|g\|^2/\|Jg\|^2$. Give the [dog leg](/powell-dogleg/) step for the radii $\Delta = 1$, 2 and 3.

10. • Three cameras with one scalar parameter each have $U = 3I$. Two points have $V = 2$ each; point 1 is seen by cameras 1 and 2, point 2 by cameras 2 and 3, and every nonzero block of $W$ equals 1. Form $S = U - W V^{-1} W^{\mathsf T}$ and explain its pattern of zeros.

11. • Three cameras turn in the plane. The measured relative angles are $\theta_2 - \theta_1 = 30°$, $\theta_3 - \theta_2 = 50°$ and $\theta_1 - \theta_3 = -75°$. Find the error around the cycle and solve the [rotation averaging](/rotation-averaging/) problem by least squares on the angles with $\theta_1 = 0$.

12. • A [view graph](/view-graph/) has the edges $(1, 2)$ with 120 inliers and angle $40°$, $(2, 3)$ with 80 and $25°$, $(1, 3)$ with 30 and $62°$, $(3, 4)$ with 200 and $-10°$, and $(2, 4)$ with 15 and $20°$. Find the [maximum spanning tree](/maximum-spanning-tree/) on the inlier counts, the angles it gives with $\theta_1 = 0$, and the residuals of the two edges off the tree.

13. • A host patch has the intensities $(10, 20, 30, 40)$ and the target patch $(25, 45, 65, 85)$. Fit the affine brightness change $I_t = a I_h + b$ of the [photometric error](/photometric-error/), and say why a direct method needs it.

14. • Model [scale drift](/scale-drift/) as a random walk of the log scale with steps of standard deviation 0.005. After 1000 steps, give the standard deviation of the log scale and a 95 percent band for the scale factor. Check it with a simulation.

15. • Show that the centred $2F \times P$ matrix of [Tomasi-Kanade factorization](/tomasi-kanade-factorization/) has rank at most 3. The metric upgrade gives 3 equations per frame on the symmetric $3 \times 3$ matrix $L = QQ^{\mathsf T}$. How many frames does counting ask for, and why does the method need 3?

16. • Three cameras lie on one line, and the directions between all pairs are measured. Show that [translation averaging](/translation-averaging/) cannot fix their positions up to one shift and one scale. What changes if one camera moves off the line?

17. ★ Show that in calibrated bundle adjustment, fixing the pose of the first camera and the distance between the first two centres removes the [gauge freedom](/gauge-freedom/) of dimension 7, provided the first two centres differ. Why does fixing only the first camera leave $J^{\mathsf T} J$ singular?

18. ★ The [inexact Newton](/inexact-newton-bundle-adjustment/) method solves $S\delta = e$ by preconditioned conjugate gradients. Show that the method ends in at most $k$ iterations when the preconditioned matrix has $k$ distinct eigenvalues. What happens with a block Jacobi preconditioner when no two cameras share a point?

19. ★ Show that the Gauss-Newton iterates do not change under a linear change of parameters $x = By$ with $B$ invertible, and that gradient descent does not have this property.

20. ★ Show that solving the reduced camera system and then back-substituting for the points gives exactly the step of the full normal equations, as [sparse bundle adjustment](/sparse-bundle-adjustment/) claims, whenever $V$ is invertible.
