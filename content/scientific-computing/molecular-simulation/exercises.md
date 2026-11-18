1. ◦ An atom with $m = 1$ sits on a spring with $k = 1$, at $x = 1$ with $v = 0$. Do one step of the velocity Verlet loop of [molecular dynamics](/molecular-dynamics/) with $h = 0.2$, writing down the velocity after the first half kick, the new position, the new force and the final velocity. Compute $H = \frac12 v^2 + \frac12 x^2$ after the step and the quantity $v^2 + (1 - h^2/4) x^2$.

2. ◦ For the Lennard-Jones pair potential $U(r) = 4\epsilon\bigl((\sigma/r)^{12} - (\sigma/r)^6\bigr)$, find the distance $r_m$ where $U$ is smallest and the value $U(r_m)$. At $r = \sigma$, what are $U$ and the force $-U'(\sigma)$, and is that force attractive or repulsive?

3. ◦ A periodic box has side $L = 10$. In one coordinate, atom $i$ is at $0.5$ and atom $j$ at $9.0$. What separation does the minimum image convention give, and what is the largest cutoff $r_c$ for which the convention finds every pair within $r_c$?

4. ◦ A simulation of $N = 10^4$ atoms runs for 1 µs with $h = 2$ fs. How many steps does it take? How many pairs does the all-pairs force loop visit in one step, and how many with a neighbour list in which each atom has about 300 neighbours (each pair counted once)?

5. • Run the spring of Exercise 1 with $h = 0.5$. Using the quantity that velocity Verlet conserves for this system, find the largest speed $|v|$ on the curve that the numerical solution stays on, and the energy $H$ at that point of the curve. Compare $|H - \frac12|$ there with the bound $h^2/8$ stated in the entry.

6. • Run the spring of Exercise 1 with $h = 1$ and list $x$ after each of the first six steps. Show that the numerical solution is periodic with a period of 6 time units, and compare with the exact period $2\pi$. Is the numerical oscillation faster or slower than the exact one?

7. • The O-H stretch of water has a wavenumber of about $3700 \text{ cm}^{-1}$. Taking the speed of light as $2.998 \times 10^{10}$ cm/s, find its period in femtoseconds and the largest stable Verlet step $h < T/\pi$ for this motion, treated as harmonic. Explain why simulations with flexible water use $h = 1$ fs or less.

8. • Two Lennard-Jones atoms with $\epsilon = \sigma = m = 1$ rest at the distance $r_m$ of Exercise 2. For small vibrations about $r_m$, find the angular frequency $\omega$ of the relative motion (use the reduced mass $m/2$) and the largest stable step $h$ in these units. Write a program that starts the pair at rest at $r = r_m + 10^{-4}$ and runs velocity Verlet for 4000 steps with $h = 0.186$ and with $h = 0.19$; report what happens to the distance and the energy in each run.

9. ★ Let $\Phi_h$ be one velocity Verlet step for $\dot{x} = v$, $m \dot{v} = f(x)$, without a box, and let $R(x, v) = (x, -v)$. Prove that $R \circ \Phi_h \circ R \circ \Phi_h$ is the identity: if a step takes $(x, v)$ to $(x', v')$, then a step from $(x', -v')$ ends at $(x, -v)$. Deduce the statement for $S$ steps.

10. ★ For the spring $\ddot{x} = -\omega^2 x$, write one velocity Verlet step as $(x', v') = M (x, v)$ with a $2 \times 2$ matrix $M$ that depends on $z = h\omega$. Show that $\det M = 1$ and $\operatorname{tr} M = 2 - z^2$. Deduce that the numerical solution stays bounded for every start if and only if $0 < z < 2$, and that for those $z$ it rotates by the angle $\theta$ with $\cos\theta = 1 - z^2/2$ per step. Prove that $\theta > z$, so the numerical oscillation is always a little too fast.
