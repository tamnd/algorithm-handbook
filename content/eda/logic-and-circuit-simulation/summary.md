## What to remember

- A [logic simulator](/logic-simulation/) is exact for its delay model and value system. [Transport delay](/inertial-and-transport-delay/) passes every pulse; inertial delay drops pulses shorter than the gate delay. X is sound but pessimistic: $x \land \lnot x$ gives X, not 0.
- The [event-driven simulator](/event-driven-logic-simulation/) costs $O(EFk + SM)$ for $E$ value changes. [Compiled-code](/compiled-code-logic-simulation/) and [cycle-based](/cycle-based-simulation/) simulation evaluate every gate each cycle. The [delta cycle](/delta-cycle/) orders zero-delay events at one time, independently of process order when no variables are shared.
- [Ternary simulation](/ternary-simulation/) runs in $O(n(n + P))$ time, and every 0 or 1 it reports holds for all gate and wire delays. It finds static hazards and races, not dynamic hazards. [Switch-level simulation](/switch-level-simulation/) is sound with X but not exact.
- [Modified nodal analysis](/modified-nodal-analysis/) has $n + m$ unknowns for $n$ non-ground nodes and $m$ voltage sources and inductors, against $n + 2b$ for the [sparse tableau](/sparse-tableau-analysis/). [Gilbert-Peierls LU](/gilbert-peierls-lu/) costs $O(n + \mathrm{nnz}(A) + f)$ for $f$ operations. Minimum fill is NP-complete, so [Markowitz pivoting](/markowitz-pivoting/) is a heuristic.
- Newton's method for the [DC operating point](/dc-operating-point-analysis/) converges only from a good start. [Gmin stepping](/gmin-stepping/), [source stepping](/source-stepping/) and [pseudo-transient analysis](/pseudo-transient-analysis/) are proved to work for uniformly monotone circuits. [Junction voltage limiting](/junction-voltage-limiting/) has no global convergence theorem.
- [Transient analysis](/transient-circuit-analysis/) chooses steps from local truncation error estimates, so the global error is controlled, not bounded. The trapezoidal rule rings on stiff parts, since $R(z) \to -1$ as $z \to -\infty$. [TR-BDF2](/tr-bdf2/) is second order and L-stable, with $\gamma = 2 - \sqrt 2$.
- [AC analysis](/ac-small-signal-analysis/) is exact for the linearization. [Adjoint sensitivity](/adjoint-sensitivity-analysis/) gives the derivatives of one output for all $P$ parameters with one extra solve, $O(N^3 + K(N^2 + P))$ for $K$ outputs. [Noise analysis](/circuit-noise-analysis/) needs one adjoint solve per frequency, and [Padé via Lanczos](/pade-via-lanczos/) matches $2q$ moments in $q$ steps but is not always passive.
- [Harmonic balance](/harmonic-balance-analysis/) truncates at $K$ harmonics and is exact only for linear circuits whose sources have no harmonic above $K$. [Shooting-Newton](/shooting-newton-steady-state/) is exact for the discrete map of one period. [Phase noise](/phase-noise-analysis/) of a free oscillator grows as $\operatorname{Var} \alpha(t) = ct$, which gives a Lorentzian spectrum.

| Method | Task | Time | Guarantee |
|---|---|---|---|
| Event-driven | gate-level waveforms | $O(EFk + SM)$ | exact for the delay model |
| Compiled-code | zero-delay values | $O(G \log G + P + (m/W + 1)(G + P))$ | exact on loop-free zero-delay netlists |
| Cycle-based | values at clock edges | $O(N + P + T(G + P))$ | exact at edges if timing holds |
| Ternary | hazards and races | $O(n(n + P))$ | every 0 or 1 holds for all delays |
| Switch-level | MOS logic values | $O(R(N + T) \log N)$ | sound with X, not exact |
| Gilbert-Peierls LU | sparse LU | $O(n + a + f)$ | exact for the given pivots |
| KLU | circuit matrices | $O(na + f)$ | exact for the given pivots |
| AC | frequency response | $O(D + FS)$ | exact for the linearization |
| Adjoint sensitivity | all parameter derivatives | $O(N^3 + K(N^2 + P))$ | exact |
| Noise | output noise density | $O(D + F(S + K))$ | exact for the linearization |
| Padé via Lanczos | reduced model of order $q$ | $O(F + qs + qN)$ | $2q$ moments, not passive |
| Harmonic balance | periodic steady state | $O(In^3K^3)$ dense | truncation error in $K$ |
| Shooting-Newton | periodic steady state | $O(ISn^3)$ | exact for the discrete map |
| TR-BDF2 | transient steps | $O(NKT)$ | second order, L-stable |
| Iterated timing analysis | digital waveforms | $O(sK(N + T))$ | sweeps to a tolerance |

: Worst-case bounds from the entries; the variables differ between rows. Newton-based rows assume convergence.

## Choosing a method

For code or gates with delays, use an event-driven simulator. If only the values at clock edges matter, cycle-based simulation is faster, and compiled code with bit-parallel words suits many vectors on combinational logic. Check asynchronous circuits by ternary simulation, and MOS logic with charge sharing by switch-level simulation.

Where voltages matter, use MNA, Newton and sparse LU, with KLU. If the operating point fails, try gmin stepping, source stepping, then pseudo-transient analysis. For stiff transients, prefer TR-BDF2 to the plain trapezoidal rule.

Use adjoint sensitivity when many parameters are tuned. Reduce a large linear network by Padé via Lanczos, or by [PRIMA](/prima/) when passivity matters. Use harmonic balance for mildly nonlinear circuits, shooting-Newton for switching ones. For large digital blocks at transistor level, use [iterated timing analysis](/iterated-timing-analysis/), or [mixed-mode simulation](/mixed-mode-simulation/) when most of the design is logic.
