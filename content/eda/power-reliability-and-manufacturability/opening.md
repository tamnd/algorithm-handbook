A design that computes the right function and meets its clock can still fail. It can draw more power than its package can remove, let its supply voltage sag where many gates switch at once, pick up noise from a neighbouring wire, wear out as current moves the metal of its wires, or come out of the factory with too few working dies. Lithography adds the question of what is actually printed on the wafer.

Much of this is models rather than algorithms with proofs. The dynamic power $P = \alpha C V^2 f$, Black's equation for electromigration and the Poisson and negative binomial yield models each rest on stated assumptions and are checked against measurements. Switching activity can be computed exactly with BDDs when they stay small, propagated as probabilities that are exact on trees but approximate under reconvergent fanout, or estimated by Monte Carlo simulation to a confidence interval. Power grid analysis solves sparse linear systems that can have millions of unknowns, and vectorless verification bounds the worst-case drop by linear programs.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Power and its estimation.** Dynamic, leakage and glitch power, switching activity, signal probability propagation, transition density, BDD-based and Monte Carlo estimation, and RTL power macromodels.
2. **Reducing power.** Clock gating, operand isolation, bus-invert coding, power gating, multiple threshold voltage assignment and clustered voltage scaling.
3. **Power grids and noise.** Power grid analysis by multigrid-like methods and random walks, vectorless power grid verification, decoupling capacitance allocation, crosstalk noise, Devgan's noise metric and the Miller coupling factor.
4. **Reliability.** Black's equation and the Blech length for electromigration, the reaction-diffusion model of NBTI, soft error masking and compact thermal models.
5. **Yield.** The Poisson, Murphy and negative binomial yield models, critical area and its extraction from a Voronoi diagram, redundant via insertion, and design centering by simplicial approximation.
6. **Lithography and fill.** The Hopkins imaging model, the sum of coherent systems, inverse lithography, and the dummy fill problem solved by linear programming.

## What to read meanwhile

The chapter on timing, verification and test has the closest written entries. The [RC tree](/rc-tree/), [Elmore delay](/elmore-delay/) and [parasitic extraction](/parasitic-extraction/) give the wire models that grid and noise analysis use, and the [floating random walk](/floating-random-walk-capacitance/) is a related Monte Carlo method. [Statistical static timing analysis](/statistical-static-timing-analysis/) models process variation. [Design rule checking](/design-rule-checking/), [optical proximity correction](/optical-proximity-correction/) and [multiple patterning decomposition](/multiple-patterning-decomposition/) are the written manufacturability entries.

From other volumes: [binary decision diagrams](/binary-decision-diagram/) (Volume 16) for exact activity estimation; the [multigrid method](/multigrid-method/) and [Monte Carlo integration](/monte-carlo-integration/) (Volume 12) for grids and sampling; [linear programming](/linear-programming-problem/) (Volume 15) for vectorless verification and fill; the [Voronoi diagram](/voronoi-diagram/) (Volume 13) for critical area; and the [Poisson distribution](/poisson-distribution/) (Volume 1) behind the simplest yield model.
