1. ◦ A pin has the size limits 19.90 mm and 20.00 mm and a position tolerance of diameter 0.05 mm at maximum material condition, in the sense of [GD&T](/geometric-dimensioning-and-tolerancing/). Give its virtual condition, and the diameter of the position zone when the pin is made at 20.00, 19.95 and 19.90 mm.

2. ◦ [Geometric primitive fitting](/geometric-primitive-fitting/) uses $4$ parameters for a sphere, $5$ for a circular cylinder, $6$ for a cone and $7$ for a torus. Split each count into the parts of the shape it describes, and explain why a cylinder needs $5$ and not the $6$ that a point on the axis, a unit direction and the radius seem to need.

3. ◦ A part has a plane as primary datum A and a round hole perpendicular to A as secondary datum B. How many degrees of freedom does each datum remove in the [datum reference frame](/datum-reference-frame/), which motion is still free, and what kind of feature must the tertiary datum be to fix it?

4. ◦ The circle $x^2 + y^2 - 16 = 0$ has radius 4. Give the geometric and the algebraic distance, as used in [algebraic distance fitting](/algebraic-distance-fitting/), of the points $(3, 4)$ and $(0, 3)$. Which of the two points weighs more in the sum of squared algebraic distances, and by what factor?

5. ◦ Points lie on a cylinder of radius $R = 50$ mm across a strip of width $L = 10$ mm. Find the sagitta. With a distance tolerance $\varepsilon = 0.1$ mm, can one plane cover the strip in [segmentation into primitives](/primitive-segmentation/)? And with $\varepsilon = 0.2$ mm?

6. ◦ In [slippage analysis](/slippage-analysis/), give the number of independent slippable motions of a cone, of two planes that meet at a right angle along a line, of the three faces at a corner of a box, and of a hemisphere together with its flat base.

7. ◦ A [small displacement torsor](/small-displacement-torsor/) has the rotation $\omega = (0.001, 0, 0.002)$ rad and the displacement $D(O) = (0.01, 0, 0)$ mm at the origin $O$. Find the displacement of the point $B = (100, 50, 0)$.

8. ◦ [Hammersley sampling](/hammersley-sampling-for-cmm/) with $N = 16$ uses the points $(i/16, \varphi_2(i))$ for $i = 0, \dots, 15$, where $\varphi_2$ reverses the binary digits of $i$ after the binary point. Give the points for $i = 6$ and $i = 11$, scaled to a face of 40 mm by 16 mm.

9. ◦ A [Monte Carlo tolerance analysis](/monte-carlo-tolerance-analysis/) of $N = 1500$ simulated assemblies finds no reject. Give the exact one-sided $95\%$ upper limit for the reject rate, and compare it with the rule of three.

10. • The points $(0, 0)$, $(1, 2)$, $(2, 1)$, $(3, 3)$, $(4, 2)$ are measured along a line. Find the minimum-zone straightness of [form error evaluation](/form-error-evaluation/) and the pair of hull features that sets it. Then fit the [least-squares reference feature](/least-squares-reference-feature/), the line of least orthogonal squared distance, and give the width of the zone of lines parallel to it.

11. • Find the [minimum-zone flatness](/minimum-zone-flatness/) of the five points $(0, 0, 0)$, $(4, 0, 2)$, $(0, 4, 1)$, $(4, 4, 1)$, $(2, 1, 2)$, exactly. Say whether a face-vertex pair or an edge-edge pair of the hull sets it, and give the normal of the two planes.

12. • A model has the points $(0, 0)$, $(4, 0)$, $(0, 2)$, and the measured matching points are $(1.0, 2.0)$, $(1.02, 6.0)$, $(-1.0, 1.98)$. Find the rotation and translation of [inspection localization](/inspection-localization/) that move the measured points onto the model in the least-squares sense, and the three residual distances.

13. • In [CMM probe path planning](/cmm-probe-path-planning/), probe direction A reaches the features $\{1, 2, 3, 4\}$, direction B reaches $\{1, 2, 5\}$ and direction C reaches $\{3, 4, 6\}$. Run [greedy set cover](/greedy-set-cover/) and compare with the fewest directions that reach all six features.

14. • A probe starts and ends at $(0, 0)$ and must visit $A = (4, 0)$, $B = (1, 1)$, $C = (4, 3)$, $D = (0, 4)$ and $E = (2, 2)$, with straight moves. Give the tour of the [nearest neighbor heuristic](/nearest-neighbor-heuristic/) and its length, and the shortest tour by trying all orders.

15. • [Tolerance allocation](/tolerance-allocation/) with costs $c_i = a_i / T_i$, $a = (1, 2, 1)$, sensitivities $s = (1, 1, 2)$ and the RSS requirement $\sqrt{\sum_i s_i^2 T_i^2} \le 0.1$ mm. Find the optimal $T_i$ and the cost, and compare with equal tolerances that meet the same requirement.

16. • Three dimensions, all with sensitivity 1, each choose one process, given as (tolerance in mm, cost): dimension 1 from $(0.02, 9)$, $(0.04, 5)$, $(0.06, 3)$; dimension 2 from $(0.01, 8)$, $(0.03, 4)$, $(0.05, 2)$; dimension 3 from $(0.02, 6)$, $(0.03, 4)$, $(0.05, 1)$. The worst-case sum of the tolerances must be at most $0.10$ mm. Solve by a dynamic program over the budget in steps of $0.01$ mm, and give the cheapest choice and the number of feasible choices.

17. • A gap is $G = A - B - C$ with $A = 30 \pm 0.06$, $B = 20 \pm 0.03$ and $C = 9.9 \pm 0.03$ mm. Each dimension is normal with the standard deviation one third of its tolerance, and an assembly is rejected when $G < 0.03$ mm. Compute the reject rate exactly, and the number of Monte Carlo samples for a relative standard error of $10\%$.

18. • A ball of radius $r = 5 \pm 0.01$ mm sits in a V-groove of angle $\alpha = 90° \pm 0.5°$, and its center is at the height $h = r / \sin(\alpha/2)$ above the bottom line. Linearize as in the [direct linearization method](/direct-linearization-method/): find the sensitivities, the worst-case and the RSS variation of $h$, and compare the worst case with the exact extremes over the four corners.

19. • A rectangular face of 40 by 20 mm has a size zone of width $t = 0.1$ mm, so its deviations satisfy $\lvert w \rvert + 10 \lvert \alpha \rvert + 20 \lvert \beta \rvert \le 0.05$. The output is the displacement $w + 10 \alpha + 20 \beta$ of a corner. Find its worst case over this octahedron and over the smallest box around it, as the [Jacobian-torsor model](/jacobian-torsor-model/) uses. Show that for any linear output the box overstates the worst case by a factor of at most 3.

20. • [Constrained primitive fitting](/constrained-primitive-fitting/): line A carries the points $(0, 0)$, $(2, 0)$, $(4, 0)$ and line B the points $(0, 1)$, $(2, 1.2)$, $(4, 1.4)$. Fit each line alone, then fit two parallel lines together by orthogonal least squares. Give the joint direction, the total squared error and the distance between the lines.

21. • Show that [Taubin fitting](/taubin-fitting/) of a line $ax + by + c = 0$ returns the orthogonal regression line, and that its minimum cost is the smallest eigenvalue of the centered scatter matrix. Give this value for the points of exercise 10.

22. ★ Let $N = 2^m$. Show that the Hammersley set $\{(i/N, \varphi_2(i)) : 0 \le i < N\}$ has exactly one point in every box $[a/2^j, (a+1)/2^j) \times [b/2^{m-j}, (b+1)/2^{m-j})$ with $0 \le j \le m$.

23. ★ A convex polygon with perimeter $P$ and interior angles $\theta_i$ gets [Requicha's tolerance zone](/requicha-tolerance-zone-theory/) with $t_+ = t_- = t$, smaller than its inradius. Show that the zone has area $2Pt + \pi t^2 - t^2 \sum_i \cot(\theta_i/2)$, check it on the 100 by 50 plate with $t = 0.1$, and evaluate it for an equilateral triangle of side 10.

24. ★ Allocate a worst-case budget $T_1 + T_2 + T_3 = T$ with costs $c_i = a_i e^{-b T_i}$. Show that at the optimum all cost terms are equal and $T_i = T/3 + (\ln a_i - \overline{\ln a})/b$, where $\overline{\ln a}$ is the mean of the $\ln a_i$. Evaluate for $a = (4, 1, 1)$, $b = 50$ per mm and $T = 0.15$ mm, and compare the cost with equal tolerances.

25. ★ A planar rigid motion has the velocity field $v + \omega J (p - o)$, with $J$ the rotation by $90°$. Show that a connected smooth curve along which this field is tangent everywhere, with $(v, \omega) \ne 0$, is a piece of a line or of a circle. This is slippage analysis in the plane.

26. ★ Measured deviations $e_1, \dots, e_n$ along one direction are localized by a single shift. The least-squares shift is the mean, the minimax shift the midrange. Show that the largest remaining deviation after the least-squares shift is at most $2(1 - 1/n)$ times the one after the minimax shift, and that the deviations $(0, \dots, 0, R)$ reach this factor.
