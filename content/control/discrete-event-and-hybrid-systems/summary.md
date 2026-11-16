## What to remember

- A specification $K$ can be enforced exactly by disabling controllable events if and only if it is [controllable](/controllable-language/): $\overline{K}\,\Sigma_{uc} \cap L(G) \subseteq \overline{K}$. Controllability is closed under union, so a supremal controllable sublanguage exists. For regular $K$ it is computed in $O(n^2 q)$ time on the product of $n$ states, and by one $O(nq)$ backward pass when $K$ is prefix-closed.
- Under partial observation the condition adds [observability](/observable-language/), which is not closed under union, so a largest observable sublanguage need not exist. [Normality](/normal-language/) is closed under union and implies observability.
- [Diagnosability](/diagnosability/) assumes a live language and no unobservable cycle. The [diagnoser](/diagnoser-automaton/) can be exponential in the number of states, while the [twin plant](/twin-plant-diagnosability-test/) decides diagnosability in $O(n^2 q)$ time.
- A [timed event graph](/timed-event-graph/) in which every circuit holds a token obeys $x(k) = A \otimes x(k-1)$ in [max-plus algebra](/max-plus-algebra/). An irreducible $A$ has one eigenvalue, the maximum cycle mean, and $x(k)/k \to \lambda$ ([eigenvalue theorem](/max-plus-eigenvalue-theorem/)).
- Stable modes do not make a stable [switched system](/switched-system/). A [common Lyapunov function](/common-lyapunov-function/) gives stability under arbitrary switching, and one exists whenever the system is GUAS, though it need not be quadratic. No quadratic one exists if some convex combination of the modes is not Hurwitz.
- In discrete time, GUES under arbitrary switching holds if and only if the [joint spectral radius](/joint-spectral-radius/) is below 1, and $\max_P \rho(P)^{1/k} \le \rho(\mathcal{M}) \le \max_P \|P\|^{1/k}$ over products $P$ of length $k$. Deciding $\rho \le 1$ is undecidable.
- The [dwell-time theorem](/dwell-time-theorem/) is sufficient, not necessary: GUES holds for switches at least $\tau_D > (\ln c)/\lambda_0$ apart when $\|e^{A_p t}\| \le c\, e^{-\lambda_0 t}$ for every mode.
- [Reachability](/reachable-set-computation/) is undecidable for general hybrid automata and decidable for timed automata (PSPACE-complete) and initialized rectangular automata, so practical tools over-approximate. A [barrier certificate](/barrier-certificate/) proves safety without computing the reachable set.

| Method | Problem | Cost | What you get |
|---|---|---|---|
| [Supremal controllable sublanguage](/supremal-controllable-sublanguage/) | least restrictive nonblocking supervisor | $O(n^2 q)$ time | exact, for regular $K$ |
| [Monitor places](/supervision-based-on-place-invariants/) | enforce $L\mu \le b$ on a Petri net | $O(cnq)$ time | maximally permissive if all transitions are controllable and observable |
| [Diagnoser](/diagnoser-automaton/) | diagnosability, online detection | $O(2^{n 2^m} n^4 16^m q)$ | exact test and online monitor |
| [Twin plant](/twin-plant-diagnosability-test/) | diagnosability | $O(n^2 q)$ | exact test, no monitor |
| [Hybrid MPC](/hybrid-mpc/), enumeration | horizon problem of a PWA model | $O(s^N(N^3 n m^2 + c))$ | optimal input |
| [Zonotopes](/zonotope-reachability/) | reachable sets, linear systems | $O(n^3 + N n^2 m + N m \log m)$ | sound over-approximation |
| [Hamilton-Jacobi](/hamilton-jacobi-reachability/) | backward reachable sets, nonlinear | $O(K n k^n)$ | grid approximation, neither inner nor outer |

: Main algorithms of the chapter, worst-case time. Discrete-event rows: $n$ states (of the product for the first row, of the plant for diagnosis, places for monitors), $q$ events or transitions, $c$ constraints, $m$ fault types. Hybrid MPC: $s$ modes, horizon $N$, state and input dimensions $n$ and $m$, $c$ the cost of one QP. Zonotopes: $N$ time steps, $m$ generators kept. Hamilton-Jacobi: $k$ grid nodes per axis, $K$ time steps.

## Choosing a method

For a plant automaton and a regular specification, compute the supremal controllable sublanguage on the product. It is exact, but the product grows with every component, so large plants use modular supervisors, which must then be checked for conflict. For a Petri net with linear constraints on the marking, monitor places avoid the state explosion but do not ensure liveness. With unobserved events, aim for a normal sublanguage, which always has a largest element.

To decide diagnosability, use the twin plant. Build the diagnoser only for an online monitor, or run it on the fly.

For a switched linear system, try a common quadratic Lyapunov function first, which is one semidefinite program. If none exists, the system may still be stable, and sum-of-squares functions or joint spectral radius bounds can show it. If the switching can be made slow, the dwell-time theorem gives a bound to enforce.

For safety, use zonotopes for linear systems, and Hamilton-Jacobi methods for nonlinear systems with disturbances up to about four or five state variables. A barrier certificate found by sum-of-squares programming is the lightest proof, but failing to find one proves nothing.
