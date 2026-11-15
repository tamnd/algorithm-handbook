Take a two-input multiplexer, $y = ab + \bar a c$, with $b = c = 1$. Logically $y$ is 1 whatever $a$ does. Give each gate a delay of one unit and let $a$ fall from 1 to 0. The term $ab$ drops after one unit, the term $\bar a c$ rises only after two, since the inverter comes first, and for one unit $y$ is 0. A [logic simulator](/logic-simulation/) with this delay model shows the glitch. Build the same multiplexer from transistors and the glitch is no longer a step of one unit but a dip of some hundreds of millivolts that may or may not cross the switching threshold of the next gate. Only a circuit simulator, which solves for the node voltages as real waveforms, tells which.

Simulation computes how a design behaves over time for given inputs, and it runs at these two levels. Logic simulation works on gates and register-transfer code with discrete values such as 0, 1 and X and with gate delays. It is exact for its delay model: an [event-driven](/event-driven-logic-simulation/) run gives the waveforms that the model defines, and no more. Circuit simulation, in the line of SPICE, writes [Kirchhoff's laws](/kirchhoff-circuit-laws/) and the device models as nonlinear differential-algebraic equations, assembles them by [modified nodal analysis](/modified-nodal-analysis/), and solves each time step by Newton's method over sparse LU factors. Its guarantees are conditional. Newton converges from a good start, the continuation aids are proved to work for monotone circuits, and the step size comes from estimates of the local truncation error, so the accuracy of a waveform is controlled, not bounded.

## What the chapter covers

1. **[Values and delays](/logic-simulation/).** The logic simulation problem, inertial and transport delay, and value systems with X, Z and the nine values of IEEE 1164.
2. **[Logic simulators](/compiled-code-logic-simulation/).** Compiled-code and [cycle-based](/cycle-based-simulation/) simulation, the event-driven simulator, and the [delta cycle](/delta-cycle/) of VHDL and Verilog.
3. **[Hazards and transistor-level logic](/ternary-simulation/).** Ternary simulation for hazards and races, [channel-connected components](/channel-connected-component/) and [switch-level simulation](/switch-level-simulation/).
4. **[Circuit equations and device models](/kirchhoff-circuit-laws/).** Kirchhoff's laws, modified nodal analysis, the [Shichman-Hodges model](/shichman-hodges-model/), [Tellegen's theorem](/tellegen-theorem/) and [sparse tableau analysis](/sparse-tableau-analysis/).
5. **[Sparse linear solvers](/markowitz-pivoting/).** Markowitz pivoting, [Gilbert-Peierls LU](/gilbert-peierls-lu/) and the [KLU solver](/klu-solver/).
6. **[DC operating point](/dc-operating-point-analysis/).** Newton's method on the resistive equations, with [gmin stepping](/gmin-stepping/), [source stepping](/source-stepping/) and [junction voltage limiting](/junction-voltage-limiting/).
7. **[Transient analysis](/companion-model/).** Companion models, [transient analysis](/transient-circuit-analysis/) with step control, [TR-BDF2](/tr-bdf2/) and [pseudo-transient analysis](/pseudo-transient-analysis/).
8. **[Small-signal analysis](/ac-small-signal-analysis/).** AC analysis, [adjoint sensitivity](/adjoint-sensitivity-analysis/), [noise analysis](/circuit-noise-analysis/) and [Padé via Lanczos](/pade-via-lanczos/).
9. **[Periodic steady state](/harmonic-balance-analysis/).** Harmonic balance, the [shooting-Newton method](/shooting-newton-steady-state/) and oscillator [phase noise](/phase-noise-analysis/).
10. **[Fast and mixed simulation](/timing-simulation/).** Timing simulation, [iterated timing analysis](/iterated-timing-analysis/) and [mixed-mode simulation](/mixed-mode-simulation/).

Fault simulation is a logic simulator run with faults added. Its entries are elsewhere: [fault simulation](/fault-simulation/) and [concurrent fault simulation](/concurrent-fault-simulation/) are in the chapter on timing, verification and test, and [parallel fault simulation](/parallel-fault-simulation/) and [PPSFP](/ppsfp/) are in the chapter on test and diagnosis. The linear interconnect models, the [RC tree](/rc-tree/), [Elmore delay](/elmore-delay/), [asymptotic waveform evaluation](/asymptotic-waveform-evaluation/) and [PRIMA](/prima/), are in the chapter on timing, verification and test too. [Switching activity](/switching-activity/) and [power grid analysis](/power-grid-analysis/) are in the chapter on power, reliability and manufacturability.

## A first reading

For a first pass, read these twelve entries in order:

1. Logic simulation
2. [Inertial and transport delay](/inertial-and-transport-delay/)
3. [Multi-valued logic simulation](/multi-valued-logic-simulation/)
4. Event-driven logic simulation
5. Delta cycle
6. Kirchhoff's circuit laws
7. Modified nodal analysis
8. Shichman-Hodges model
9. DC operating point analysis
10. Companion model
11. Transient circuit analysis
12. AC small-signal analysis

They give the two kinds of simulator from end to end. Skip at first the inside of the sparse solvers, the periodic steady state with phase noise, Padé via Lanczos and switch-level simulation. Each of them builds on the first reading and can wait until a task needs it.

## Before you start

The logic half needs a few ideas from earlier volumes. A gate netlist is a [Boolean circuit](/boolean-circuit/) (Volume 1). A synchronous design is a [Mealy machine](/mealy-machine/) (Volume 9). The event queue is that of [event-driven simulation](/event-driven-simulation/) (Volume 2), often kept as a [timing wheel](/timing-wheel/) (Volume 26), and compiled code packs vectors by [bit parallelism](/bit-parallelism/) (Volume 2).

The circuit half rests on numerical analysis. Volume 12 has [Newton's method for systems](/newton-method-for-systems/), [sparse linear systems](/sparse-linear-systems/) and [fill-in](/fill-in/), [stiff problems](/stiff-ode-problem/), [differential-algebraic equations](/differential-algebraic-equations/), the [backward Euler method](/backward-euler-method/), the [trapezoidal rule](/trapezoidal-rule/) and [homotopy continuation](/homotopy-continuation/). [LU decomposition](/lu-decomposition/) and the [discrete Fourier transform](/discrete-fourier-transform/) are in Volume 11. The sparse solvers use [depth-first search](/depth-first-search/) and [Tarjan's algorithm](/tarjan-scc/) from Volume 7. The noise entries use the [power spectral density](/power-spectral-density/) of Volume 28.
