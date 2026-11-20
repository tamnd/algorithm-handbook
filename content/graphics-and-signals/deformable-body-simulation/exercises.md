1. ◦ A triangle has the rest corners $(0, 0)$, $(1, 0)$ and $(0, 1)$ and the deformed corners $(0, 0)$, $(1.2, 0)$ and $(0.3, 0.9)$. Compute the [deformation gradient](/deformation-gradient/) $F$, its determinant $J$, the right Cauchy-Green tensor $C = F^TF$ and the Green strain $E = \tfrac12(C - I)$. Is the triangle inverted?

2. ◦ A rubber has Young's modulus $10^5$ Pa. Compute the Lamé parameters $\mu$ and $\lambda$ of a [hyperelastic material](/hyperelastic-material/) for the Poisson ratios $\nu = 0.3$, $0.45$ and $0.49$. Which parameter grows without bound as $\nu \to 0.5$, and what does that mean for the volume?

3. ◦ A cloth particle of mass 2 g hangs on one spring of stiffness 50 N/m to a pin. What is the largest step of symplectic Euler for which this spring is stable? How many equal substeps does a frame of $1/60$ s need at least? Use the condition $\omega\Delta t < 2$ of the [mass-spring system](/mass-spring-system/).

4. ◦ Two particles of [position based dynamics](/position-based-dynamics/) sit at $(0, 0)$ with mass 2 and at $(0, 2)$ with mass 1, joined by a distance constraint of rest length 1.2. Compute the scale $s$, the two corrections with the sweep stiffness 1, and the new positions. Then compute the per-sweep stiffness $k'$ that gives the overall stiffness $k = 0.5$ with $n_s = 4$ sweeps.

5. ◦ A free particle of mass 2 at $(1.3, 0)$, at rest and without gravity, is joined to a pin at the origin by an [XPBD](/extended-position-based-dynamics/) distance constraint of rest length 1 and compliance $\alpha = 10^{-3}$ m/N, with $\Delta t = 0.02$ s. Compute $\tilde\alpha$, $\Delta\lambda$ and the new position after one sweep, and compare with the [backward Euler](/backward-euler-method/) step for a spring of stiffness $1/\alpha$. Where would plain PBD with sweep stiffness 1 put the particle?

6. ◦ A linear spring oscillator has $\omega\Delta t = 2$. By what factor does backward Euler multiply its energy in one step, and in 10 steps? What does [symplectic Euler](/symplectic-euler-method/) do at this step?

7. ◦ A [particle system](/particle-system/) emits 200 particles per second, and each particle lives for a time drawn uniformly from $[1, 3]$ s. About how many particles are alive in the steady state?

8. ◦ Four particles of mass 1 rest at $(\pm 1, \pm 1)$. They are now at $(-b, 2a)$ for the rest point $(a, b)$, a stretch along $x$ followed by a turn of 90 degrees, and at rest. For [meshless shape matching](/meshless-shape-matching/) in the rigid mode, compute $A_{pq}$, the rotation angle, the goal of the particle that rests at $(1, 1)$, and its velocity and position after one step with $\alpha = 0.5$ and $\Delta t = 0.1$, without gravity.

9. • A chain on a line has a pinned particle at 0 and free particles at 1.4 and 2.6, with two springs of rest length 1. Apply [Provot strain limiting](/provot-strain-limiting/) with $\tau = 0.1$ and $\sigma = 0$, springs in the order left to right. Give the positions after each of the first four sweeps. Show that the excess of the first spring halves with every sweep, so the limit is never met in a finite number of sweeps.

10. • For the $F$ of exercise 1, compute the rotation $R$ of the polar decomposition $F = RS$ with the 2D formula $\theta = \operatorname{atan2}(F_{10} - F_{01}, F_{00} + F_{11})$, the stretch $S = R^TF$, and the energy density $\mu|F - R|_F^2 + \frac\lambda2\operatorname{tr}(S - I)^2$ of [corotational elements](/corotational-fem/) with $E = 1$ and $\nu = 0.3$. Check that $S$ is symmetric.

11. • A bar is compressed to $F = \operatorname{diag}(s, 1)$, with $E = 1$ and $\nu = 0.3$. Compute $P_{xx}$ of the [neo-Hookean model](/neo-hookean-model/) and of the [St. Venant-Kirchhoff model](/st-venant-kirchhoff-model/) for $s = 0.5$, $0.2$ and $0.1$. Which model resists more as the bar flattens?

12. • A particle of mass 1 is joined to a pin at the origin by a spring of rest length 1 and stiffness 100, with $\Delta t = 0.1$, and its inertial prediction is $\mathbf y = (1.5, 0.5)$. Run one local and global iteration of [fast mass-spring simulation](/fast-mass-spring/), starting from $\mathbf x = \mathbf y$. Show that the result is already the exact backward Euler step, for any $\mathbf y \ne 0$, and give it.

13. • The [stable neo-Hookean](/stable-neo-hookean/) model in 3D has the target Lamé parameters $\mu_0 = 1$ and $\lambda_0 = 10$. Compute $\mu$, $\lambda$ and $\alpha$ after the remap, check that $P(I) = 0$, and compute $\Psi(0) - \Psi(I)$, the energy density it takes to collapse an element to a point. What is the same difference for the plain neo-Hookean model?

14. • A body has two degrees of freedom with $M = I$ and $K = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$. Find its modes and frequencies, the static shape under the load $\mathbf f = (1, 0)$, and the shape and the relative $M$-norm error of [modal reduction](/modal-reduction/) with the lowest mode only.

15. • A [discrete elastic rod](/discrete-elastic-rods/) has the vertices $(0, 0, 0)$, $(1, 0, 0)$ and $(1.5, \sqrt3/2, 0)$, a straight rest shape with unit edges and $\alpha = 1$ N m². Compute the curvature binormal, its length, and the bending energy $\alpha|\kappa b|^2/\bar l$ with $\bar l = 2$. Compare with the small angle value $\alpha\varphi^2/(2h)$. Is there any twist from holonomy if both ends are clamped with the same director?

16. • For an isometric bend by the angle $\theta$ of a flat pair of triangles, the [quadratic bending model](/quadratic-bending-model/) has the edge energy $\tfrac12(2\sin(\theta/2))^2|\bar e|/\bar h_e$ and [discrete shells](/discrete-shells/) has $\theta^2|\bar e|/\bar h_e$. Compute the ratio of the first to half the second at $\theta = \pi/2$ and $\theta = \pi$, and find the angle at which it falls to 0.9.

17. • In 2D an edge joins $(0, 0)$ and $(1, 0)$, both of mass 1 and at rest, and a node of mass 2 at $(0.75, 0.1)$ falls with 2 m/s onto it. All three form one [impact zone](/impact-zones/). Compute the center of mass, the mean velocity, the angular momentum about the center, the moment of inertia and the angular velocity of the zone, and its turn angle in a step of $0.1$ s. Is the linear momentum kept?

18. • [Vertex block descent](/vertex-block-descent/) updates the vertices of one color of a [graph coloring](/graph-coloring/) in parallel. How many colors does a $3 \times 3$ grid of vertices need with structural springs only, and with structural and both diagonal shear springs? Give a coloring and a reason why fewer colors fail.

19. ★ A chain has pins at 0 and 3.9 and three springs of rest length 1 between them, with free particles at 1.3 and 2.6. Show that no placement keeps every spring within $\tau = 0.1$, and that the smallest largest strain is 30%. Run Provot's sweeps left to right with $\sigma = 0$ and describe what happens to the positions and the strains.

20. ★ A vertical XPBD chain hangs from a pin at the origin: particles of mass 1 at heights $-1$ and $-2$, at rest, two distance constraints of rest length 1 with $\alpha = 10^{-3}$, gravity 9.81 m/s² and $\Delta t = 0.1$ s. The constraints stay affine along the chain. Compute the backward Euler step, run Gauss-Seidel sweeps in the order top to bottom, and show that the error falls by the same factor every sweep. Give that factor in closed form.

21. ★ In [incremental potential contact](/incremental-potential-contact/) with $b(d) = -(d - \hat d)^2\ln(d/\hat d)$, a body at rest has the contact force $\lambda = -\kappa b'(d)/\Delta t^2$ at each active pair. A square of 1 kg rests on two of its four vertices on the ground, with $\hat d = 10^{-3}$ m and $\kappa = 1$. Find the rest gap for $\Delta t = 1/30$, $1/100$ and $1/300$ s, and for $\kappa = 10^{-2}$ and $10^2$ at $\Delta t = 0.01$ s.

22. ★ The hanging cloth of the vertex block descent entry has $6 \times 6$ vertices with structural, shear and bending springs, the bending springs joining vertices two apart along a row or a column (158 springs). A greedy coloring in row-major order uses 7 colors. Find the smallest number of colors, with a proof of the lower bound and a coloring that reaches it.

23. ★ [Affine body dynamics](/affine-body-dynamics/) keeps $A$ near a rotation with the energy $V_\perp = \kappa_o\,\mathrm{vol}\,|AA^T - I|_F^2$. In 2D, take $A = (1 + \varepsilon)R$ for a rotation $R$. Compute $V_\perp$ exactly and to leading order in $\varepsilon$. For a body of area 0.08 m² and $\kappa_o = 10^7$, what scale error $\varepsilon$ costs 1 J? How does $\varepsilon$ change when $\kappa_o$ grows 100 times, and does that match the entry's measurement?
