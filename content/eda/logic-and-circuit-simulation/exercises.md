In these exercises node 0 is ground, every gate of a logic exercise has a delay of one unit unless stated otherwise, and $V_t$ is the thermal voltage.

1. ◦ A connected circuit has 7 nodes, one of them ground, and 12 branches, two of which are independent voltage sources and none inductors. How many independent equations do [Kirchhoff's current and voltage laws](/kirchhoff-circuit-laws/) give? How many unknowns has its [modified nodal analysis](/modified-nodal-analysis/), and how many its [sparse tableau](/sparse-tableau-analysis/)?

2. ◦ An n-channel MOSFET follows the [Shichman-Hodges model](/shichman-hodges-model/) with $k = 200\ \mu\text{A/V}^2$, $V_T = 0.5$ V and $\lambda = 0$, and has $V_{GS} = 1.0$ V. Find $I_D$ at $V_{DS} = 0.2$ V and at $V_{DS} = 1.0$ V. Then take an inverter output node of 5 fF at 1.2 V whose input has just switched from 0 to 1.2 V, with an n device of $k = 100\ \mu\text{A/V}^2$ and $V_T = 0.4$ V and the p device off. Find the change of the output voltage in one backward Euler step of $h = 2$ ps, as [timing simulation](/timing-simulation/) computes it with one Newton update.

3. ◦ A capacitor $C = 2$ F with $v(0) = 1$ V discharges through $R = 1\ \Omega$. Give the [companion model](/companion-model/) conductance and $v(1)$ after one step $h = 1$ s of backward Euler and of the trapezoidal rule, and compare both with the exact value.

4. ◦ A buffer has delay 4. Its input rises at 0, falls at 3, rises at 10 and falls at 16. Give the output pulses under [transport and inertial delay](/inertial-and-transport-delay/). Which pulses pass if the inertial delay has a rejection limit of 2 instead?

5. ◦ Use the resolution function of IEEE 1164 from [multi-valued logic simulation](/multi-valued-logic-simulation/) to give the value of a wire driven by (H, L, 0), by (1, 0, Z), by (L, Z) and by (W, H).

6. ◦ A [compiled-code simulator](/compiled-code-logic-simulation/) packs eight input vectors into bytes, with $a = $ `0xF0`, $b = $ `0xCC` and $c = $ `0xAA`. Give the output byte of the majority gate $ab + bc + ca$.

7. ◦ Simulate $y = ab + \bar a c$, built from an inverter, two AND gates and an OR gate, with $b = c = 1$ and $a$ rising from 0 to 1 at time 10, in an [event-driven simulator](/event-driven-logic-simulation/). Does $y$ change? How many gate evaluations take place from time 10 on?

8. ◦ A VHDL design has the concurrent assignments `b <= not a;`, `c <= b;` and `d <= a xor c;`, all without delay, and starts with $a = 0$, $b = c = d = 1$. At time 10, $a$ becomes 1. List the [delta cycles](/delta-cycle/) at time 10 with the signals that change in each. In which deltas is $d = 0$?

9. ◦ A $4 \times 4$ matrix has a nonzero diagonal and off-diagonal nonzeros only at $a_{12}$, $a_{21}$, $a_{24}$ and $a_{43}$. Give the block triangular form that the [KLU solver](/klu-solver/) finds and the blocks that it factors.

10. • Two buffers with inertial delays $d_1$ and $d_2$ are in series. For which widths $w$ does an isolated pulse reach the output, and with what delay? Compare with one buffer of inertial delay $d_1 + d_2$.

11. • An XOR gate has inputs $(a, b)$ that change from $(0, 0)$ to $(1, 1)$. What does [ternary simulation](/ternary-simulation/) report for the output? Show that every circuit for XOR gets the same report, so that no added gate removes it.

12. • A source $E$ in series with $1\ \Omega$ drives an element with $i = v^3 - 6v^2 + 10v$. For which $E$ does the circuit have three [DC operating points](/dc-operating-point-analysis/)?

13. • The trapezoidal rule integrates $\dot v = -v/\tau$ with a fixed step $h$. For which $h$ is the factor $v_{k+1}/v_k$ negative? At $h = 38\tau$, give the factor and the number of steps until $|v_k| < 0.01\, |v_0|$, and the factor of backward Euler at the same step.

14. • A symmetric matrix has the pattern of a ring of $n \ge 4$ nodes, with a nonzero diagonal and one pair of nonzeros for each edge of the ring, and every pivot is taken on the diagonal. Show that every elimination order gives the same number of fill entries, and find it. Compare the count of [Markowitz pivoting](/markowitz-pivoting/) for the first pivot with the fill that pivot creates.

15. • A 1 A source drives node 1. $R_1 = 1\ \Omega$ joins node 1 to ground, $R_2 = 1\ \Omega$ joins nodes 1 and 2, and $R_3 = 2\ \Omega$ joins node 2 to ground. The output is $\phi = e_2$. Use [adjoint sensitivity](/adjoint-sensitivity-analysis/) to find $\partial \phi / \partial R_k$ for $k = 1, 2, 3$ and $\partial \phi / \partial I$, and check that $\sum_k R_k\, \partial \phi / \partial R_k = \phi$. Explain why it must hold.

16. • In [switch-level simulation](/switch-level-simulation/), a bus of size 3 holds 1 and two storage nodes $c_1$ of size 1 and $c_2$ of size 3 hold 0. Two transistors that are on join the bus to $c_1$ and $c_1$ to $c_2$, and no input drives any of the three nodes. What values do the three nodes take? What if $c_2$ has size 2?

17. • Three nodes in a row each have 1 F and 1 S to ground, and neighbours are joined by 1 S. With backward Euler and $h = 1$, [iterated timing analysis](/iterated-timing-analysis/) solves each step by Gauss-Seidel sweeps over the nodes in order 1, 2, 3. By what factor does the error shrink per sweep in the long run?

18. • An RC ladder has 1 S from node 1 to ground, 1 S between nodes 1 and 2 and between nodes 2 and 3, and 1 F from each node to ground. A current enters node 1, and the output is $e_3$. Find the transfer function and its first five moments at $s = 0$. Give the models of order $q = 1$ and $q = 2$ that [Padé via Lanczos](/pade-via-lanczos/) produces, with their poles, and compare with the poles of the ladder.

19. • The Hopf oscillator of the [phase noise analysis](/phase-noise-analysis/) entry has $\mu = 1$ and $\omega = 2\pi$, but white noise of intensity $\sigma = 0.1$ now enters the first state only. Find the diffusion constant $c$ and the phase noise at an offset of 1 Hz.

20. • [Harmonic balance](/harmonic-balance-analysis/) with $K = 3$ solves an RC lowpass with $\omega RC = 1$ driven by $\cos \omega t + \cos 3\omega t$. Give the amplitude and phase of the output at $\omega$ and $3\omega$. What does a run with $K = 1$, on $M = 3$ samples, give?

21. ★ In an acyclic gate circuit with unit delays, one primary input changes at time 0 and nothing else changes. Show that a net can change only at times that are lengths of paths from the input to it, so that it changes at most as many times as there are distinct such lengths. Apply the bound to $y$ in $y = ab + \bar a c$ and say whether it is reached.

22. ★ [TR-BDF2](/tr-bdf2/) with $\gamma = 2 - \sqrt 2$ applied to $\dot y = \lambda y$ gives $y_{k+1} = R(z) y_k$ with $z = h\lambda$. Find $R(z)$. Show that $R(z) - e^z = O(z^3)$, that $R(z) \to 0$ as $z \to -\infty$, find the zero of $R$ on the negative axis, and find the smallest value of $R$ there and where it occurs.

23. ★ A current $\cos \omega t$ drives a conductor with $i = v + v^3$ and nothing else. Run harmonic balance with $K = 1$, that is collocation at $M = 3$ equally spaced times. Give the samples of $v$, the DC term and the amplitude of the fundamental of the result. Compare with the DC term and fundamental of the true waveform.

24. ★ Use [noise analysis](/circuit-noise-analysis/) to find the thermal noise density at node 2 of the circuit of exercise 15 at 300 K, with the source removed. Then prove for any network of resistors that the output noise density at node $k$ is $4kT Z_{kk}$, where $Z_{kk}$ is the driving-point resistance at node $k$.

25. ★ [Gilbert-Peierls LU](/gilbert-peierls-lu/) factors an $n \times n$ arrow matrix that is strictly diagonally dominant by columns, so the diagonal pivots are kept. Leaving the fill aside, count the multiply and subtract operations $f$ and the rows reached by the depth-first searches, summed over all columns, when the full row and column are last and when they are first. Give both values of $f$ for $n = 10$.
