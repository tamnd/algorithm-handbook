## What to remember

- A state of $n$ [qubits](/qubit/) is a unit vector of $2^n$ complex amplitudes, defined up to a global phase. Measuring in the computational basis returns $x$ with probability $|\alpha_x|^2$ ([Born rule](/born-rule/)) and leaves $|x\rangle$. Qubit 0 is the rightmost symbol and the least significant bit, and a circuit that applies $A$ then $B$ has matrix $BA$.
- [Gates](/quantum-gate/) are unitary. $H$, $S$ and [CNOT](/cnot-gate/) generate the [Clifford group](/clifford-group/), whose circuits a classical computer simulates in polynomial time ([Gottesman-Knill](/gottesman-knill-theorem/)); adding $T$ gives a [universal gate set](/universal-gate-set/), and [Solovay-Kitaev](/solovay-kitaev-theorem/) approximates any one-qubit gate to error $\varepsilon$ with $O(\log^c(1/\varepsilon))$ gates from it.
- Classical logic runs inside a quantum circuit only [reversibly](/reversible-computation/), with [Toffoli](/toffoli-gate/) gates and [ancillas](/ancilla-qubits/). Garbage left on the ancillas is entangled with the data and spoils interference, so it must be [uncomputed](/uncomputation/).
- An [oracle](/quantum-oracle/) query on $|x\rangle|-\rangle$ gives $(-1)^{f(x)}|x\rangle|-\rangle$ ([phase kickback](/phase-kickback/)). With Hadamard gates before and after, one query solves [Deutsch-Jozsa](/deutsch-jozsa-algorithm/) and [Bernstein-Vazirani](/bernstein-vazirani-algorithm/) exactly, and $n + O(1)$ expected queries solve [Simon's problem](/simon-algorithm/). These separations hold in the query model and relative to an oracle only.
- The [quantum Fourier transform](/quantum-fourier-transform/) on $n$ qubits takes $n$ Hadamards, $n(n-1)/2$ controlled phases and $\lfloor n/2 \rfloor$ swaps. Its output cannot be read, only sampled. [Phase estimation](/quantum-phase-estimation/) with $t$ counting qubits and the inverse transform returns a $t$-bit estimate of $\varphi$ within $2^{-t}$ with probability at least $8/\pi^2$.
- A shared [Bell pair](/bell-states/) plus two classical bits [teleports](/quantum-teleportation/) one qubit; a Bell pair plus one qubit sent carries two bits ([superdense coding](/superdense-coding/)). Neither sends anything faster than light ([no-communication theorem](/no-communication-theorem/)), and no circuit copies an unknown state ([no-cloning](/no-cloning-theorem/)). In the [CHSH](/chsh-inequality/) game classical strategies win with probability at most $3/4$ and quantum ones with at most $\cos^2(\pi/8) \approx 0.854$.
- [Density matrices](/density-matrix/) describe mixtures and parts of entangled systems; [channels](/quantum-channel/) with [Kraus operators](/kraus-operators/) describe noise. With equal priors, the best measurement tells $\rho$ from $\sigma$ with probability $(1 + D(\rho, \sigma))/2$, where $D$ is the [trace distance](/trace-distance/).
- [Error correction](/quantum-error-correction/) measures the syndrome, never the data. The [threshold theorem](/quantum-threshold-theorem/) says that below a constant error rate, under a local stochastic noise model, any circuit runs to accuracy $\delta$ with polylogarithmic overhead. Numeric thresholds such as about 1% for the surface code are estimates from simulation.

| Primitive | Model | Cost | Guarantee |
|---|---|---|---|
| [Deutsch-Jozsa](/deutsch-jozsa-algorithm/) | query, promise | 1 query, $n + 1$ qubits | exact |
| [Bernstein-Vazirani](/bernstein-vazirani-algorithm/) | query | 1 query | exact |
| [Simon](/simon-algorithm/) | query, promise | fewer than $n + 2.61$ queries expected | zero error |
| [QFT](/quantum-fourier-transform/) | gates | $n(n+1)/2 + \lfloor n/2 \rfloor$ gates, $O(n \log(n/\varepsilon))$ approximate | exact, or error $\varepsilon$ |
| [Phase estimation](/quantum-phase-estimation/) | controlled-$U$ queries | $2^t - 1$ uses of controlled $U$ | within $2^{-t}$ w.p. $\ge 8/\pi^2$ |
| [Hadamard test](/hadamard-test/) | gates | 1 ancilla, one controlled $U$ per run | $\mathrm{Re}\langle\psi\vert U\vert\psi\rangle$ to $\pm\varepsilon$ with $O(1/\varepsilon^2)$ runs |
| [Swap test](/swap-test/) | gates | $2n + 1$ qubits, $n$ controlled swaps | overlap to $\pm\varepsilon$ with $O(\log(1/\delta)/\varepsilon^2)$ copies |
| [Teleportation](/quantum-teleportation/) | LOCC with entanglement | 1 Bell pair, 2 bits per qubit | exact |
| [Gottesman-Knill](/gottesman-knill-theorem/) | classical simulation | $O(n)$ per gate, $O(n^2)$ per measurement | exact, Clifford circuits only |
| [Threshold theorem](/quantum-threshold-theorem/) | local stochastic noise | polylog$(m/\delta)$ overhead | error $\delta$ below threshold |

: The main primitives. $n$ is the number of qubits of the input, $t$ the counting qubits, $m$ the size of the ideal circuit.

## Choosing a method

To learn a global property of a function from few queries, put the input register in uniform superposition, query with the target in $|-\rangle$, and apply Hadamards or a Fourier transform before measuring. If $f$ is linear over $\mathbb{F}_2$, one query suffices; if $f$ hides a subgroup, sample the dual and solve a linear system, as Simon's algorithm does.

To learn an eigenvalue of a unitary, use phase estimation when you need many bits and can afford controlled powers of $U$; use the Hadamard test when an expectation value to a few digits is enough. To compare two states you hold, use the swap test; to tell two known states apart, use the Helstrom measurement of [state discrimination](/state-discrimination-problem/); to learn an unknown state, use [tomography](/quantum-state-tomography/) and expect a number of copies that grows with $d^2$ for dimension $d$.

To check that a circuit does what you expect without a quantum computer, simulate it: a state vector of $2^n$ amplitudes for small $n$, the stabilizer tableau for Clifford circuits of any size. To run a long circuit on noisy hardware, encode it in a stabilizer code such as [Steane's](/steane-code/).
