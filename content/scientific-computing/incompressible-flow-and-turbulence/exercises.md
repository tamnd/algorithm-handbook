1. ◦ In lattice units, what kinematic viscosity does the [lattice Boltzmann method](/lattice-boltzmann-method/) give at $\tau = 0.8$, and what $\tau$ gives $\nu = 0.05$? What is the Mach number of a lattice speed $|u| = 0.1$? A simulation of water ($\nu = 10^{-6}$ m²/s) uses $\Delta x = 1$ mm and $\tau = 0.8$: how long is one time step in seconds?

2. ◦ For the D2Q9 weights $w_0 = \frac49$, $w_{1..4} = \frac19$, $w_{5..8} = \frac1{36}$ and velocities $(0,0)$, $(\pm1, 0)$, $(0, \pm1)$, $(\pm1, \pm1)$, compute $\sum_i w_i$, $\sum_i w_i c_{ix}^2$, $\sum_i w_i c_{ix} c_{iy}$, $\sum_i w_i c_{ix}^4$ and $\sum_i w_i c_{ix}^2 c_{iy}^2$. Which of them equal $c_s^2$ and which equal $c_s^4$, with $c_s^2 = \frac13$?

3. ◦ Compute the nine D2Q9 equilibrium populations for $\rho = 1$ and $u = (0.05, 0.05)$, with $c_1 = (1,0)$, $c_2 = (0,1)$, $c_3 = (-1,0)$, $c_4 = (0,-1)$, $c_5 = (1,1)$, $c_6 = (-1,1)$, $c_7 = (-1,-1)$, $c_8 = (1,-1)$. Check that they sum to 1 and that $\sum_i c_{ix} f_i^{\mathrm{eq}} = 0.05$.

4. ◦ For the cubic spline kernel of [smoothed particle hydrodynamics](/smoothed-particle-hydrodynamics/) in one dimension, find $W(0, h)$, $W(h/2, h)$ and $W(h, h)$. Particles of equal mass sit on a regular lattice with spacing $\Delta p$ and $h = \Delta p$; compute the lattice sum $\sum_k W(k\Delta p, h)\,\Delta p$.

5. ◦ Run the Sod setup of the SPH entry with 640 particles on the left. How many particles are on the right, and how many in total? With $\Delta t = 0.3\, h_{\min}/1.2$ and $T = 0.2$, how many steps does the scheme take? Roughly how many pair interactions do you expect, given the entry's 213 859 for 320 left particles?

6. • Run D1Q3 with $\tau = 1$ from a unit mass at one node. Give the masses after three steps. Show that the variance of the mass distribution grows by exactly $\frac13$ per step, and compare its value after 30 steps with $2Dt$ for the diffusivity $D = (\tau - \frac12)/3$.

7. • Run D1Q3 with $\tau = \frac34$ from a unit mass at one node, starting at equilibrium. Show that after two steps the density two nodes away is $-\frac1{54}$. Why does this not contradict the requirement $\tau > \frac12$?

8. • For the Poiseuille channel of the lattice Boltzmann entry, use the slip formula $s = g\bigl(2(\tau - \frac12) - \frac{3}{8(\tau - \frac12)}\bigr)$ to find $s/g$ at $\tau = 0.7$ and at $\tau = 1.2$. With $n_y = 16$, $\tau = 0.8$ and $g = 10^{-6}$, find the exact centre velocity, and compare the slip with it.

9. • The Taylor-Green vortex decays like $e^{-2\nu k^2 t}$. On a $32 \times 32$ lattice with $\tau = 0.8$, after how many steps has the velocity amplitude halved, and after how many the kinetic energy? Show that over the entry's $S = N^2/8$ steps the amplitude falls by the same factor $e^{-\pi^2/10} \approx 0.373$ for every $N$.

10. • The D2Q9 equilibrium is a second-order expansion in $u$ and turns negative at large speeds. With $\rho = 1$, find the largest $|u|$ for which all nine populations are nonnegative when $u$ points along the $x$ axis, and when it points along the diagonal $(1, 1)$. Which populations reach zero first in each case?

11. ★ Show that FTCS for $u_t = D u_{xx}$ has local truncation error $\frac{D \Delta x^2}{2}\bigl(\mu - \frac16\bigr)u_{xxxx} + O(\Delta t^2 + \Delta x^4)$ with $\mu = D\Delta t/\Delta x^2$, and deduce that D1Q3 with $\tau = 1$ is consistent of order 4 in $\Delta x$ under diffusive scaling. By what factor should the error fall when $N$ doubles, and does the entry's table agree?

12. ★ For the cubic spline kernel in one dimension, prove that the lattice sum $\sum_k W(k\Delta p, h)\,\Delta p$ equals 1 exactly whenever $h/\Delta p$ is a positive integer. Then compute the sum with exact fractions for $h/\Delta p = \frac32$ and $\frac52$, and compare with the value 1.0018 that the entry gives for $h = 1.2\,\Delta p$.
