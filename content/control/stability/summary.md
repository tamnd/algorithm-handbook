## What to remember

- For $\dot x = Ax$, asymptotic, exponential and global stability are one property: every eigenvalue of $A$ has $\operatorname{Re}\lambda < 0$. Then $\|e^{At}\| \le k e^{-\lambda t}$, and $k$ can be large.
- Positive coefficients are necessary, not sufficient: $s^3 + s^2 + 2s + 8$ has two roots in the right half plane. For a cubic $s^3 + a_1 s^2 + a_2 s + a_3$ the exact condition is $a_1, a_3 > 0$ and $a_1 a_2 > a_3$. In the regular case the sign changes in the first column of the Routh array count the roots in the right half plane.
- The Jury test is the unit circle version. Positive coefficients mean nothing there: $z + 2$ is not stable.
- $A$ is Hurwitz if and only if $A^T P + PA = -Q$ has a solution $P > 0$ for some, and then every, $Q > 0$. The same $P$ proves local exponential stability of a nonlinear system whose Jacobian at the equilibrium is $A$.
- Linearization decides only when no eigenvalue lies on the imaginary axis. $\dot x = -x^3$ and $\dot x = x^3$ both linearize to $0$; the first is asymptotically stable, the second unstable.
- The direct method is sufficient only. If $V > 0$ and $\dot V < 0$ away from the equilibrium, the equilibrium is asymptotically stable, and globally so if $V$ is also radially unbounded. A failed search for $V$ proves nothing.
- Every loop theorem here is sufficient: small gain asks $\gamma_1 \gamma_2 < 1$, the passivity theorem asks for strictness in the loop, and the circle and Popov criteria ask for a frequency condition. For $G = 1/(s+1)^3$ with a nonlinearity in the sector $[0, k]$, the circle criterion reaches $k < 4$, the Popov criterion $k < 8$, and $8$ is also the limit for constant gains.
- The describing function predicts limit cycles; it does not prove them. For a relay with output $\pm 1$ and $G = 1/(s(s+1)(s+2))$ it predicts the amplitude $0.212$ and the period $4.44$, while the true cycle has $0.220$ and $4.55$.

| Method | Applies to | Kind of answer | Cost or price |
|---|---|---|---|
| [Routh array](/routh-array/) | real polynomial, left half plane | exact count in the regular case | $O(n^2)$ operations |
| [Jury test](/jury-stability-test/) | real polynomial, unit disc | exact | $O(n^2)$ time, $O(n)$ space |
| [Linear Lyapunov theorem](/lyapunov-theorem-for-linear-systems/) | matrix $A$ | exact, with a certificate $P$ | $O(n^3)$ |
| [Indirect method](/lyapunov-indirect-method/) | $C^1$ system near an equilibrium | exact unless an eigenvalue is on the axis | eigenvalues of the Jacobian |
| [Direct method](/lyapunov-direct-method/) | any system | sufficient | a function $V$ to find |
| [Sum of squares](/sum-of-squares-programming/) | polynomial systems | sufficient | semidefinite program with Gram matrices of size $\binom{n+d}{d}$ |
| [Contraction](/contraction-analysis/) | systems with inputs | sufficient | a metric with a uniform Jacobian bound |
| [Small gain](/small-gain-theorem/) | feedback loops | sufficient | finite gains with product below $1$ |
| [Circle criterion](/circle-criterion/) | Lur'e loops, time-varying sector | sufficient | one LMI in $P$ |
| [Popov criterion](/popov-criterion/) | Lur'e loops, time-invariant sector | sufficient | one LMI in $P$ and $\eta$ |
| [Describing function](/describing-function/) | loops with one nonlinearity | approximate | one harmonic balance equation |

: The main tests of the chapter. Here $n$ is the degree or the state dimension, and $2d$ the degree of a sum-of-squares program.

## Choosing a method

For a linear model, use an exact test. The Routh array or the Jury test gives the range of a gain in closed form. For a numeric matrix, compute the eigenvalues, or solve the Lyapunov equation for a certificate.

For a nonlinear model, linearize first. A Hurwitz Jacobian gives local exponential stability, and its Lyapunov matrix $P$ gives a first estimate of the region of attraction. An eigenvalue with positive real part gives instability. For an eigenvalue on the axis, or a global result, look for a Lyapunov function: the physical energy first, then a quadratic form, then a sum-of-squares search. Use LaSalle's principle when $\dot V$ is only semidefinite.

For a loop, choose by what you know about the parts. Gains suit the small-gain theorem, energy balances suit the passivity theorem, and a sector bound on a single nonlinearity suits the circle criterion, or the Popov criterion when the nonlinearity does not change with time. When none succeeds, the loop may still be stable. To look for an oscillation, start with the describing function, and confirm a predicted cycle by simulation or, in the plane, by a trapping region for the Poincaré-Bendixson theorem.
