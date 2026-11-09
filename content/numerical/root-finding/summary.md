## What to remember

- A method has [order](/order-of-convergence/) $q$ when $|e_{k+1}| \approx C|e_k|^q$. With $w$ evaluations in each step, its efficiency index $q^{1/w}$ is the factor by which the number of correct digits grows per evaluation, and it is the fair way to compare methods.
- [Bisection](/bisection-method/) needs about $\log_2(w/\delta)$ evaluations to shrink a bracket of width $w$ below $\delta$, for every continuous function, and no method that uses only function values has a better worst case.
- [Newton's method](/newton-raphson-method/) has order 2 at a simple root and order 1 with rate $(m-1)/m$ at a root of [multiplicity](/multiplicity-of-roots/) $m$. Far from a root it can diverge or cycle: on $x^3 - 2x + 2$ from $0$ it alternates between $0$ and $1$ forever.
- The [secant method](/secant-method/) needs no derivative and has order $(1+\sqrt5)/2 \approx 1.618$ with one evaluation per step, so it beats Newton's method per evaluation when $f'$ costs as much as $f$.
- A bracketing hybrid such as [Brent's method](/brent-method/) keeps a sign change, takes interpolation steps while they shrink the bracket fast enough, and bisects otherwise. It is the default for one equation with a known bracket.
- A simple root has condition $1/|f'(x^*)|$ in the absolute sense, and a root of multiplicity $m$ moves like $\varepsilon^{1/m}$ when $f$ changes by $\varepsilon$. A double root in binary64 is therefore found to only about 8 digits by any method.
- Polynomial roots can be ill conditioned in the monomial coefficients even when they are well separated: in [Wilkinson's polynomial](/wilkinson-polynomial/), a change of $2^{-23}$ in one coefficient turns ten real roots into five complex pairs.
- For a system $F(x) = 0$, [Newton's method](/newton-method-for-systems/) solves $J(x)s = -F(x)$ in each step and converges quadratically near a root with nonsingular Jacobian; [Broyden's method](/broyden-method/) replaces $J$ by rank-one updates and keeps superlinear convergence.

## Methods for one equation side by side

| Method | Order $q$ at a simple root | Evaluations per step $w$ | Index $q^{1/w}$ | Keeps a bracket |
|---|---|---|---|---|
| [Bisection](/bisection-method/) | 1, error bound halves | 1 | linear | yes |
| [Regula falsi](/regula-falsi/) | 1, often with one end stuck | 1 | linear | yes |
| [Illinois](/illinois-method/) | $3^{1/3}$ per evaluation | 1 | 1.442 | yes |
| [Ridders](/ridders-method/) | 2 per pass, as claimed by Ridders | 2 | 1.414 | yes |
| [Brent](/brent-method/) | between 1.618 and 1.839 | 1 | 1.618 to 1.839 | yes |
| [Newton](/newton-raphson-method/) | 2 | 2 ($f$ and $f'$) | 1.414 | no |
| [Secant](/secant-method/) | 1.618 | 1 | 1.618 | no |
| [Muller](/muller-method/), [inverse quadratic](/inverse-quadratic-interpolation/) | 1.839 | 1 | 1.839 | no |
| [Halley](/halley-method/) | 3 | 3 | 1.442 | no |
| [Steffensen](/steffensen-method/) | 2 | 2 | 1.414 | no |

: Root finders for $f(x) = 0$ near a simple root of a smooth $f$. The orders are asymptotic; far from the root only the bracketing methods give a guarantee. Brent's method bisects at worst, with at most $2(k+2)^2 + 2$ evaluations where bisection alone needs $k$.

## Choosing a method

- One equation with a sign change and no derivative: use Brent's method, or Chandrupatla's method in vectorized code.
- One equation with a cheap derivative and a good start: use Newton's method, and wrap it in the [safeguarded hybrid](/newton-bisection-hybrid/) whenever a bracket is known.
- A suspected multiple root: expect linear convergence and limited accuracy; apply the method to $f/f'$, or use the multiplicity in the step if it is known.
- All roots of one polynomial: use the [companion matrix](/companion-matrix-method/) for moderate degree, and the [Aberth-Ehrlich method](/aberth-ehrlich-method/) for high degree or many digits. Polish each root on the original polynomial after any [deflation](/polynomial-deflation/).
- Real roots of a polynomial that must all be found and proved: count them with [Sturm sequences](/sturm-sequence/) or [Descartes' rule](/descartes-rule-of-signs/), then isolate and refine them.
- A small system: Newton's method with a line search or trust region; Broyden's method when the Jacobian is expensive. All isolated roots of a polynomial system: [homotopy continuation](/homotopy-continuation/).
- A result that must be certified: the [interval Newton method](/interval-newton-method/), or the Kantorovich test at the computed point.
