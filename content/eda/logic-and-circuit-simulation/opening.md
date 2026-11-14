Simulation computes how a design behaves over time for given inputs. It runs at two levels. Logic simulation works on gates and register-transfer descriptions, with discrete values such as 0, 1 and X and with gate delays. Circuit simulation, in the line of SPICE, works on transistors, resistors and capacitors and computes node voltages and branch currents as real waveforms, for analog circuits, for library cells and wherever charge sharing or noise matters.

A logic simulator evaluates only the gates whose inputs changed, taking events in time order, or every gate once per clock cycle; its value system and delay model decide which hazards and races it can show. In a circuit simulator, Kirchhoff's laws and the device models give nonlinear differential-algebraic equations, modified nodal analysis writes them as a sparse system, and each time step is solved by Newton's method over sparse LU factorizations. Circuit equations are stiff, so the integration is implicit; the step size is chosen from local error estimates, so the accuracy of a waveform is controlled, not guaranteed. Newton's method can fail from a poor starting point, which is why simulators add continuation aids.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Logic simulation.** The logic simulation problem, event-driven, compiled-code and cycle-based simulation, and the delta cycle of hardware description languages.
2. **Values and delays.** Multi-valued logic with X and Z, ternary simulation for hazards, inertial and transport delay, and switch-level simulation over channel-connected components.
3. **Circuit equations.** Kirchhoff's laws, Tellegen's theorem, modified nodal analysis, sparse tableau analysis, companion models and the Shichman-Hodges MOSFET model.
4. **DC and transient solution.** The DC operating point, junction voltage limiting, gmin stepping, source stepping and pseudo-transient analysis; sparse LU by Markowitz pivoting, Gilbert-Peierls and KLU; transient analysis and the TR-BDF2 integrator.
5. **Frequency-domain and periodic analyses.** AC small-signal analysis, noise analysis, adjoint sensitivity, harmonic balance, the shooting-Newton method for periodic steady state, and oscillator phase noise.
6. **Faster methods.** Timing simulation, iterated timing analysis, mixed-mode simulation, and model reduction by Padé via Lanczos.

## What to read meanwhile

The numerical side is in Volume 12: [Newton's method for systems](/newton-method-for-systems/), [sparse linear systems](/sparse-linear-systems/), [LUP decomposition](/lup-decomposition/); for time steps, [stiff problems](/stiff-ode-problem/), [differential-algebraic equations](/differential-algebraic-equations/) and [backward differentiation formulas](/backward-differentiation-formulas/); and [homotopy continuation](/homotopy-continuation/), of which source stepping is a simple form. The [shooting method](/shooting-method/), [Padé approximation](/pade-approximation/) and the [Gauss-Seidel method](/gauss-seidel-method/) underlie the periodic, reduction and relaxation methods.

The chapter on timing, verification and test has the linear interconnect models: the [RC tree](/rc-tree/), [Elmore delay](/elmore-delay/), [asymptotic waveform evaluation](/asymptotic-waveform-evaluation/) and [PRIMA](/prima/). Its [concurrent fault simulation](/concurrent-fault-simulation/) is a logic simulator with faults added. For the event queue, read [event-driven simulation](/event-driven-simulation/) (Volume 2) and the [timing wheel](/timing-wheel/) (Volume 26).
