1. ◦ Three layers have the velocities 2000, 2500 and 2200 m/s and the densities 2100, 2300 and 2250 kg/m³; the first two are 300 m and 500 m thick. In the [seismic reflection model](/seismic-reflection-model/), give the two reflection coefficients and their two-way times.

2. ◦ A reflection has $t_0 = 0.8$ s and $v = 2500$ m/s. Find its time at the offset $x = 1500$ m, the [normal moveout correction](/normal-moveout-correction/) at that offset, the stretch factor and the frequency that a 40 Hz wavelet has after the correction.

3. ◦ A marine line has 96 receivers at a 25 m group interval and fires every 25 m. Find the fold of [common midpoint stacking](/common-midpoint-stacking/) and the factor by which the stack lowers independent noise, also in dB.

4. ◦ Three traces in a two-sample window hold $(1, 2, 3)$ at the first sample and $(1, 1, 1)$ at the second. Compute the [semblance](/semblance-velocity-analysis/) of the window.

5. ◦ Stacking velocities of 2200 m/s at 0.8 s and 2600 m/s at 1.4 s are picked. Use the [Dix formula](/dix-formula/) to find the interval velocity between the two reflections.

6. ◦ In the [exploding reflector model](/exploding-reflector-model/), a plane reflector dips at 40°. With the time axis of the zero-offset section shown as depth $vt/2$, at what angle does its event appear?

7. ◦ A source at the surface sends a wave down through rock at 3000 m/s to a reflector at 1200 m, and a receiver at the source position records the echo. Under the [imaging condition](/imaging-condition/), at which time do the source field and the back-propagated receiver field meet at the reflector? At the depth of 900 m, at which times does each field pass?

8. ◦ Three stations at the distances 6, 9 and 12 km from a known epicentre record P arrivals at 1.5, 2.1 and 2.45 s, with $v = 6$ km/s. As in the [Geiger method](/geiger-method/), find the best origin time and the three residuals.

9. ◦ A straight ray crosses 200 m of a body whose slowness is 5% higher than the background of 2500 m/s. Using the linearization of [traveltime tomography](/traveltime-tomography/), how much later does the wave arrive?

10. • A layer 500 m thick at 2000 m/s lies over a layer 300 m thick at 3000 m/s. Compute the rms velocity and $t_0$ of the second reflection, its hyperbolic time at offsets of 1000 m and 2000 m, and compare with the exact ray-traced times.

11. • Three layers have the interval velocities 2000, 2800 and 3500 m/s and the two-way times 0.4, 0.3 and 0.5 s. Compute the rms velocity at the bottom of each layer, and check that the Dix formula gives back the interval velocities.

12. • A wavelet $w = (1, 0.6)$ is deconvolved with a [predictive deconvolution](/predictive-deconvolution/) filter of one coefficient and gap 1. Compute the autocorrelation values, the coefficient, and the output of the prediction error filter on $w$. Which infinite filter would give a perfect spike?

13. • Compute the varimax norm $\sum y^4/(\sum y^2)^2$ of $(1, -0.5)$ and of $(-0.5, 1)$. What does the result say about the phase that [minimum entropy deconvolution](/minimum-entropy-deconvolution/) can recover?

14. • In [Kirchhoff migration](/kirchhoff-migration/) with $v = 2500$ m/s and a trace spacing of 1 m, the image point $(0, 400)$ m receives the zero-offset trace at $x = 300$ m. Compute the distance $\rho$, the time read from the trace and the weight $\cos\theta/\sqrt{2\pi v'\rho}$ with $v' = v/2$.

15. • In [phase-shift migration](/phase-shift-migration/) at 25 Hz with $v' = 1000$ m/s, compute $k_z$ for $k_x = 0.1$ rad/m, the phase of one depth step of 10 m, the largest $k_x$ that propagates, and the propagation angle of this plane wave.

16. • The 15-degree equation of [finite-difference migration](/finite-difference-migration/) replaces $\cos\theta$ by $1 - \sin^2\theta/2$. Compute its relative error at 30°, and find the angle at which the error reaches 1%.

17. • In [split-step Fourier migration](/split-step-fourier-migration/), take $\omega = 2\pi \cdot 20$ rad/s, $\Delta z = 10$ m, a reference slowness $s_0 = 1/2000$, a true slowness $s = 1/1800$ s/m and $k_x = 0.03$ rad/m. Compare the exact phase of one step with the split-step phase, and the error with its leading term.

18. • In [Stolt migration](/stolt-migration/) with $v' = 1000$ m/s, which frequency $\omega$ maps to $(k_x, k_z) = (0.015, 0.02)$ rad/m, and what is the Jacobian $v'|k_z|/\sqrt{k_x^2 + k_z^2}$?

19. • A 2D [reverse time migration](/reverse-time-migration/) grid has $\Delta x = 10$ m and a maximum velocity of 4500 m/s. Find the largest stable time step. In 3D, a grid of $500 \times 500 \times 300$ points in single precision runs for 4000 steps: how much memory does the full source wavefield need, and how much do $\sqrt{4000}$ checkpoints need?

20. • A 1D [full waveform inversion](/full-waveform-inversion/) fits a reflection at 0.8 s from a reflector at 1000 m. At 8 Hz, which constant starting velocities satisfy the half-period rule? Which satisfy the Ricker basin $|\tau| < 0.4315/f_0$ of [cycle skipping](/cycle-skipping/) for a peak frequency of 8 Hz?

21. • A primary has $v_p = 2200$ m/s and a multiple $v_m = 1800$ m/s at $t_0 = 1.2$ s. After moveout correction with $v_p$, compute the curvature $q$ of the [parabolic Radon transform](/parabolic-radon-transform/), the parabolic residual moveout at 1500 m, and the exact residual moveout there.

22. ★ Let $A(m)$ be lower bidiagonal with diagonal $(m_1, m_2, m_3)$ and $-1$ below it, $f = (1, 0, 0)$, $Au = f$ and $J = \frac12 u_3^2$. At $m = (1, 1, 2)$, compute $u$, $J$, the adjoint state $\lambda$ and the gradient by the [adjoint-state method](/adjoint-state-method/), and check it against the derivative of $J$ in closed form.

23. ★ A $2 \times 2$ grid of 100 m cells has the slownesses $(0.4, 0.5, 0.5, 0.4)$ ms/m in reading order. Compute the times of the two horizontal and two vertical rays and the minimum-norm model that fits them. Then add the diagonal ray through the first and the last cell, and show that it fixes the model.

24. ★ One flat reflector with $r = 0.5$ and a surface coefficient of $-1$ give the trace $r, -r^2, r^3, \ldots$ at multiples of $\tau$. Run two steps of [surface-related multiple elimination](/surface-related-multiple-elimination/), $P_0 \leftarrow P + P_0 P$, starting from $P_0 = P$, and give the output up to $6\tau$. Find the error after $k$ steps in closed form.

25. ★ Stations at $(0, 0)$, $(10, 0)$ and $(0, 10)$ km record a source at $(3, 4)$ km with $t_0 = 0$ and $v = 5$ km/s. Start Gauss-Newton on $(x, y, t_0)$ at $(2, 2, 0)$. Give the location error after each of the first three steps, and show that it converges quadratically.

26. ★ [Least-squares migration](/least-squares-migration/) uses CGLS on $L = \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix}$ with the data $d = L(1, 1)$. Compare the migrated image $L^{\mathsf T}d$ with the true model, and compute the first two CGLS iterates exactly.
