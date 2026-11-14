## What to remember

- The Grover iteration $G = D\,O_f$ is two reflections: the oracle flips the sign of the marked items, and the [diffusion operator](/grover-diffusion-operator/) $D = 2|s\rangle\langle s| - I$ reflects about the uniform state. On the plane of the marked and unmarked states, $G$ turns by $2\theta$ with $\sin\theta = \sqrt{M/N}$, so after $k$ iterations a measurement gives a marked item with probability $\sin^2((2k+1)\theta)$.
- [Grover's algorithm](/grover-search/) with a known $M$ stops at $k = \lfloor \pi/(4\theta) \rfloor \le \frac{\pi}{4}\sqrt{N/M}$ and fails with probability at most $M/N$; more iterations make it worse. Every bounded-error algorithm needs $\Omega(\sqrt{N/M})$ queries ([optimality](/grover-optimality/)), and an exact decision of whether any item is marked needs $N$. These are query bounds, not bounds on time.
- [Amplitude amplification](/amplitude-amplification/) does the same for any measurement-free algorithm $A$ with success probability $a$: $O(1/\sqrt a)$ calls of $A$ and $A^{-1}$ in place of $O(1/a)$ repeats.
- With $M$ unknown, [BBHT search](/bbht-search/) picks a random count from a range that grows by $6/5$ per round and makes $O(\sqrt{N/M})$ iterations in expectation. [Fixed-point search](/fixed-point-quantum-search/) never overshoots: Grover's $\pi/3$ recursion needs $\Theta(1/w)$ queries for $M/N \ge w$, the phases of Yoder, Low and Chuang $O(\log(1/\delta)/\sqrt w)$.
- [Quantum counting](/quantum-counting/) is phase estimation on $G$: $P - 1$ queries give $\tilde M = N\sin^2(\pi y/P)$ within $2\pi\sqrt{M(N-M)}/P + \pi^2N/P^2$ with probability at least $8/\pi^2$.
- [Minimum finding](/minimum-finding/) is search below a moving threshold, $\Theta(\sqrt N)$ queries; the expected number of thresholds is at most the harmonic number $H_N$. [Grover adaptive search](/grover-adaptive-search/) has this guarantee only with a budget of order $\sqrt N$; with a fixed patience its success falls to 0 as $N$ grows.
- [Quantum walk search](/quantum-walk-search/) finds a marked state of a reversible Markov chain with cost $O(S + \frac{1}{\sqrt\varepsilon}(\frac{U}{\sqrt\delta} + C))$, against $S + \frac{1}{\varepsilon}(\frac{U}{\delta} + C)$ classically. It gives element distinctness in $O(N^{2/3})$ queries and triangle finding in $\tilde O(n^{13/10})$.
- [Ordered search](/quantum-ordered-search/) gains only a constant factor: exact algorithms need more than $\frac{1}{\pi}(\ln N - 1) \approx 0.221 \lg N$ queries.

| Algorithm | Problem | Queries | Guarantee |
|---|---|---|---|
| [Grover search](/grover-search/) | find a marked item, $M$ known | $\lfloor \pi/(4\theta) \rfloor \le \frac{\pi}{4}\sqrt{N/M}$ | bounded one-sided error, at most $M/N$ |
| [BBHT search](/bbht-search/) | find a marked item, $M$ unknown | $O(\sqrt{N/M})$ expected | Las Vegas; with a time-out, bounded error |
| [Fixed-point search](/fixed-point-quantum-search/) | find a marked item, $M/N \ge w$ | $\Theta(1/w)$ ($\pi/3$); $O(\log(1/\delta)/\sqrt w)$ (Yoder, Low, Chuang) | failure $(1 - M/N)^{3^n}$; at most $\delta^2$ |
| [Quantum counting](/quantum-counting/) | estimate $M$ | $P - 1$ | additive error $O(\sqrt{MN}/P + N/P^2)$, probability $\ge 8/\pi^2$ |
| [Dürr-Høyer](/durr-hoyer-minimum-finding/) | minimum of a table | $O(\sqrt N)$ | success $\ge 1/2$ within the budget |
| [Spatial search](/spatial-search/) | marked vertex of a 2D grid | $O(\sqrt{N \log N})$ steps | bounded error, local moves counted |
| [Brassard-Høyer-Tapp](/brassard-hoyer-tapp-collision/) | collision of an $r$-to-one function | $O((N/r)^{1/3})$ expected | Las Vegas |
| [Ambainis walk](/ambainis-element-distinctness/) | $k$-distinctness | $O(N^{k/(k+1)})$ | bounded one-sided error |
| [Belovs](/belovs-k-distinctness/) | $k$-distinctness, $k$ constant | $O(N^{3/4 - 1/(4(2^k - 1))})$ | bounded error; query bound only |
| [Magniez-Santha-Szegedy](/magniez-santha-szegedy-triangle/) | triangle in an $n$-vertex graph | $\tilde O(n^{13/10})$ | bounded one-sided error |
| [Høyer-Neerbek-Shi](/hoyer-neerbek-shi-ordered-search/) | first 1 in a sorted bit string | $\log_3 N + O(1)$ | exact |

: The main algorithms. All costs are queries in the quantum query model, except spatial search, which counts oracle calls and moves along edges. A time bound needs the cost of the oracle and, for the walks, a quantum data structure.

## Choosing a method

With $M$ known, use Grover's algorithm with $\lfloor \pi/(4\theta) \rfloor$ iterations and check the measured item with one more query. If $M/N > 1/4$, sample classically instead. If $M$ is unknown, use BBHT search; if the search must be one coherent circuit inside a larger algorithm and a lower bound $w$ on $M/N$ is known, use fixed-point search with the phases of Yoder, Low and Chuang. If a quantum subroutine succeeds too rarely, amplify it, with every measurement moved to its end.

To estimate $M$ or a probability, use quantum counting or amplitude estimation, with the [median](/median-trick/) of a few runs to raise the confidence. For a minimum, use Dürr-Høyer with its budget when a guarantee is needed. Grover adaptive search on a QUBO is the same loop; its gain over classical solvers on real instances is not established.

For collisions, distinctness and subgraphs, the walk algorithms give the best query bounds, but they need quantum random access memory for a matching time bound. For a sorted list, use binary search: an exact quantum algorithm saves at most a factor $\pi \lg e \approx 4.53$ in queries.
