1. ◦ A ball is dropped from 2 m onto a floor with the [coefficient of restitution](/coefficient-of-restitution/) $e = 0.6$. Take $g = 9.81$ m/s². Find the speed at the first impact, the height of the first rebound, and the total distance the ball travels until it comes to rest.

2. ◦ A box rests on a slope of $20°$ with the friction coefficient $\mu = 0.3$ under the [Coulomb friction law](/coulomb-friction-law/). Does it stay at rest? If it slides, find its acceleration along the slope with $g = 9.81$ m/s².

3. ◦ A ball of mass 2 without spin hits the floor, with normal $(0, 1)$, at the velocity $(3, -4)$. There is no friction and $e = 0.5$. Find the [collision impulse](/collision-impulse/), the velocity after the hit and the kinetic energy before and after.

4. ◦ Run [sweep and prune](/sweep-and-prune/) on both axes for the boxes $B_0 = [0, 2] \times [0, 2]$, $B_1 = [1, 3] \times [3, 4]$, $B_2 = [2.5, 5] \times [1, 3.5]$ and $B_3 = [6, 7] \times [0, 1]$, with closed intervals. For each pair, count the axes on which the intervals overlap, and list the pairs that are reported.

5. ◦ A $6 \times 2$ rectangle is turned by $45°$. Compare the area of its [axis-aligned bounding box](/axis-aligned-bounding-box/) with the area of its oriented box, the box an [OBB tree](/obb-tree/) would use.

6. ◦ Compute the 8-DOP of the triangle $(1, 0)$, $(5, 0)$, $(1, 4)$ with the directions $x$, $y$, $x + y$ and $x - y$, as used by a [k-DOP tree](/k-dop-tree/). Does it overlap the square $[4, 6] \times [3, 5]$? What does the test of the two axis-aligned boxes report?

7. ◦ A body of mass $0.5$ kg rests on a [penalty contact](/penalty-contact/) spring of stiffness $k = 2 \cdot 10^4$ N/m, integrated by the [symplectic Euler method](/symplectic-euler-method/). The step is stable when $\omega\,\Delta t < 2$ with $\omega = \sqrt{k/m}$. Find the largest stable step, say whether $\Delta t = 1/60$ s and $1/120$ s are stable, and find the depth at rest under $g = 9.81$ m/s².

8. ◦ A joint of a chain has the position error $C = 0.02$ m, and [Baumgarte stabilization](/baumgarte-stabilization/) with $\beta = 0.2$ removes it under the linear model. What is the error after 5 steps, and after how many steps is it below $0.001$ m? Then a resting contact overlaps by $0.02$ m with no gravity and $\Delta t = 1/60$ s: what separating speed does the same rule give a body of mass 1, and how much kinetic energy does that add?

9. • A thin rod of mass 1 and length 2, with $I = 1/3$ about its centre, falls flat without spin at the velocity $(0, -1)$. Its left end hits a fixed ledge at $r = (-1, 0)$ from the centre, with $e = 0$ and no friction. Find the effective mass term $k$, the impulse, the velocity of the centre, the angular velocity, and the velocities of both ends after the hit. Check the energy loss against $(1 - e^2)(v^-)^2/(2k)$.

10. • The rod of exercise 9 now lands flat on the ground with both ends at once, at the speed 1 and $e = 0$. The two contact impulses satisfy $A\lambda + b \ge 0$, $\lambda \ge 0$ and complementarity with $A = \begin{pmatrix} 4 & -2 \\ -2 & 4 \end{pmatrix}$ and $b = (-1, -1)$. Run [projected Gauss-Seidel](/projected-gauss-seidel/) from $\lambda = 0$ for three sweeps, find the exact solution, and find how many sweeps bring the error below $10^{-6}$.

11. • A column of 1000 unit boxes stands on the ground with small gaps between them, so no two boxes touch. All share the $x$ interval $[0, 1]$. How many pairs does sweep and prune on the $x$ axis alone report, and how many are true overlaps? What does the $y$ axis report?

12. • Find the [penetration depth](/penetration-depth/) of the boxes $A = [0, 4] \times [0, 2]$ and $B = [3, 6] \times [1.5, 3.5]$ from their [Minkowski difference](/minkowski-sum/) $A - B$, and the shortest move of $A$ that separates them.

13. • A disk $A$ of radius 1 rests at the origin. A disk $B$ of radius $1/2$ moves at constant velocity from $(5, 1)$ at $t = 0$ to $(-3, 1)$ at $t = 1$. Find the time of first contact. Show that a test only at $t = 0$ and $t = 1$ misses the collision, which is the reason for [continuous collision detection](/continuous-collision-detection/).

14. • A unit disk rests at the origin. A square of half side 1 starts with its centre at $(6, 0)$, edges parallel to the axes, and moves at $(-4, 0)$ while it turns at $2$ rad/s. Find a bound $\mu$ on the approach speed of any point of the square, and the first step of [conservative advancement](/conservative-advancement/). Show that this step does not pass the first contact.

15. • Run the [elementary vertex-face test](/elementary-ccd-tests/) on the triangle $a = (0, 0, 0)$, $b$ moving from $(2, 0, 0)$ to $(2, 0, 2)$, $c = (0, 2, 0)$ fixed, and the point $p$ moving from $(0.5, 0.5, 1)$ to $(0.5, 0.5, 0)$, all linearly for $0 \le t \le 1$. Find the coplanarity function, its root, and the barycentric coordinates of $p$ in the triangle at that time. Is it a real contact?

16. • For the square $[0, 2]^2$ and the triangle $(4, 3)$, $(6, 1)$, $(6, 5)$, find the closest pair of features and the distance. Verify the pair with the Voronoi region tests that [Lin-Canny](/lin-canny-closest-features/) uses.

17. • Two boxes collide in a stack: the lower box, of mass 2, moves up at 1 m/s and the upper box, of mass 1, moves down at 2 m/s. Find the velocities after a plastic collision, and after one sweep of [shock propagation](/shock-propagation/) that treats the lower box as fixed. Compare the momentum before and after each.

18. • A plank of mass 1, with $I = 1/3$, rests on the ground on contacts at $x = -1$ and $x = 1$ under $g = 10$, with an applied torque $\tau$. Then $A = \begin{pmatrix} 4 & -2 \\ -2 & 4 \end{pmatrix}$ and $b_i = -10 + 3\tau x_i$. Find the contact forces of the [Baraff algorithm](/baraff-contact-force-algorithm/) for $\tau = -5$, $-10$ and $-15$. For which $\tau$ does the plank start to tip?

19. ★ Show that for a $2 \times 2$ positive definite system with fixed bounds that are not active, each sweep of projected Gauss-Seidel multiplies the error of the second unknown by $A_{12}^2/(A_{11}A_{22})$. Use it to explain the answer of exercise 10.

20. ★ Write one step of the symplectic Euler method for the spring $\ddot x = -\omega^2 x$ as a $2 \times 2$ matrix. Show that its determinant is 1 and its trace $2 - \omega^2 h^2$, and prove that the step is stable exactly when $\omega h < 2$.

21. ★ The plank of exercise 18, with no torque, rests on three contacts at $x = -1, 0, 1$. Write $A$, show that it has rank 2, and find all contact forces that satisfy the complementarity conditions. Show that the accelerations are the same for all of them.

22. ★ For a frictionless central collision with the effective mass term $k$ and approach speed $v^- < 0$, show that Newton's, Poisson's and Stronge's laws with the same $e$ give the same impulse. Find the impulse at maximum compression, and the work done in compression and in restitution.
