## History

The geometric tools came first from the study of controllability. Rashevsky (1938) and Chow (1939) showed
that a driftless system whose vector fields and brackets span every direction can reach every nearby
state. Sussmann and Jurdjevic (1972) and Hermann and Krener (1977) built the theory of accessibility for
systems with drift on Lie brackets. Brockett (1978) asked which systems become linear under a change of
coordinates and feedback, and Jakubczyk and Respondek (1980) and Hunt, Su and Meyer (1983) gave the
answer with the bracket conditions. Isidori, Krener, Gori-Giorgi and Monaco (1981) developed the
input-output view, and Byrnes and Isidori (1991) made the zero dynamics and the minimum phase property
the basis of output stabilization. Fliess, Lévine, Martin and Rouchon (1995) introduced flatness.

Lyapunov design took shape in the 1980s. Artstein (1983) proved that a smooth control Lyapunov function
gives a stabilizing feedback, without a formula, and Sontag (1989) wrote the formula down. In the same
year as Artstein's paper, Brockett (1983) gave his necessary condition and showed with the nonholonomic
integrator that controllable systems may not be stabilizable by smooth feedback; Zabczyk (1989) extended
it to continuous feedback. Coron (1992) showed that time-varying feedback stabilizes such systems, and
Clarke, Ledyaev, Sontag and Subbotin (1997) did the same with discontinuous feedback. Kanellakopoulos,
Kokotović and Morse (1991) made backstepping systematic, Krstić, Kanellakopoulos and Kokotović (1992)
removed the extra parameter estimates with tuning functions, and their 1995 book made the method standard.

Sliding modes grew in Emelyanov's group in Moscow from the late 1950s. Utkin's 1977 survey made them known
in the West, and Filippov's theory of differential equations with discontinuous right sides, collected in
his 1988 book, gave the solutions a meaning. Slotine (1984) introduced the boundary layer, and Levant
(1993) started the higher order sliding modes with the super-twisting algorithm, for which Moreno and
Osorio (2008) found a quadratic Lyapunov function. Esfandiari and Khalil (1992) used high-gain observers
for output feedback and tamed peaking by saturation, and Atassi and Khalil (1999) proved a separation
principle. Han developed active disturbance rejection control in the 1990s, Gao (2003) gave its linear
form with two bandwidths, and Guo and Zhao (2011) proved convergence for a class of nonlinear plants.

The energy view goes back to robot control: Takegaki and Arimoto (1981) stabilized robot arms with PD
control and gravity compensation, and passivity-based control of Euler-Lagrange systems grew through the
1980s and 1990s. Maschke and van der Schaft introduced port-controlled Hamiltonian systems in the early
1990s, and Ortega, van der Schaft, Maschke and Escobar (2002) built IDA-PBC on them. The time-scale methods
are older: averaging goes back to Krylov and Bogoliubov in the 1930s, and Tikhonov (1952) proved the basic
theorem of singular perturbation. Control barrier functions are recent: Wieland and Allgöwer (2007) named
them, and Ames, Xu, Grizzle and Tabuada (2017) gave the quadratic program form that is now standard.

## Further reading

- Hassan K. Khalil, *Nonlinear Systems*, third edition, Prentice Hall, 2002. The standard text for the
  analysis tools and for feedback linearization, backstepping, sliding modes, high-gain observers, averaging
  and singular perturbation.
- Alberto Isidori, *Nonlinear Control Systems*, third edition, Springer, 1995. The geometric theory:
  Lie brackets, relative degree, zero dynamics and exact linearization.
- Miroslav Krstić, Ioannis Kanellakopoulos and Petar Kokotović, *Nonlinear and Adaptive Control Design*,
  Wiley, 1995. Backstepping and adaptive backstepping with tuning functions, in full.
- Eduardo D. Sontag, *Mathematical Control Theory: Deterministic Finite Dimensional Systems*, second
  edition, Springer, 1998. Controllability, control Lyapunov functions and stabilization, with proofs.
- Arjan van der Schaft and Dimitri Jeltsema, *Port-Hamiltonian Systems Theory: An Introductory Overview*,
  Foundations and Trends in Systems and Control, 2014. A short introduction to port-Hamiltonian models and
  their control.
- Aaron D. Ames, Samuel Coogan, Magnus Egerstedt, Gennaro Notomista, Koushil Sreenath and Paulo Tabuada,
  "Control barrier functions: theory and applications", European Control Conference, 2019. A survey of
  barrier functions and safety filters.
