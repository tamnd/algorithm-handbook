## What to remember

- [Hamiltonian simulation](/hamiltonian-simulation/) asks for a circuit $V$ with $\|V - e^{-iHt}\| \le \epsilon$ in the spectral norm, for $H$ in a stated access model: local terms, a Pauli list with $\lambda = \sum_j |c_j|$, a sparse oracle with $\tau = d\|H\|_{\max}t$, or a block encoding of $H/\alpha$.
- The first order product formula has error at most $t^2\alpha_1/(2r)$ and the second order one at most $t^3\beta_2/r^2$, where $\alpha_1$ and $\beta_2$ are sums of norms of commutators and double commutators ([Trotter-Suzuki formulas](/trotter-suzuki-product-formulas/)). A formula of order $p$ needs $r = O(\tilde\alpha_{\mathrm{comm}}^{1/p}t^{1+1/p}/\epsilon^{1/p})$ steps ([commutator scaling](/commutator-scaling/)). Every formula of order 3 or more has negative time steps.
- [qDRIFT](/qdrift/) samples term $j$ with probability $|c_j|/\lambda$ and has error at most $(2\lambda^2t^2/N)e^{2\lambda t/N}$ in half the diamond norm after $N$ rotations, so $N \approx 2\lambda^2t^2/\epsilon$, whatever the number of terms. The bound is for the channel averaged over the random sequences.
- The [truncated Taylor series](/truncated-taylor-series-simulation/), a [linear combination of unitaries](/linear-combination-of-unitaries/) with oblivious amplitude amplification, uses $r = \lceil\lambda t/\ln 2\rceil$ segments and $O(\lambda t\log(\lambda t/\epsilon)/\log\log(\lambda t/\epsilon))$ queries.
- [Qubitization](/qubitization/) makes the walk $W = (2\Pi - I)U$ with eigenvalues $e^{\pm i\arccos(E/\alpha)}$ for each eigenvalue $E$ of $H$, and $W^k$ has $T_k(H/\alpha)$ in its corner. With [quantum signal processing](/quantum-signal-processing/), simulation costs $O(\alpha t + \log(1/\epsilon))$ queries. In the sparse model the tight count is $O(\tau + \log(1/\epsilon)/\log(e + \log(1/\epsilon)/\tau))$.
- The [no-fast-forwarding theorem](/no-fast-forwarding-theorem/) and its successors give $\Omega(\tau + \log(1/\epsilon)/\log\log(1/\epsilon))$ queries for some $d$-sparse $H$. These are query lower bounds; they say nothing about the gates for one explicit Hamiltonian.
- Under the [Jordan-Wigner transformation](/jordan-wigner-transformation/), $a_j$ becomes $Z_0\cdots Z_{j-1}(X_j + iY_j)/2$, a string of weight up to $n$; under [Bravyi-Kitaev](/bravyi-kitaev-transformation/) the weight is $O(\log n)$.
- Every exact energy $\langle\psi|H|\psi\rangle$ is at least $E_0$ ([variational method](/variational-method/)), but an estimate from finitely many shots can fall below it, and [VQE](/variational-quantum-eigensolver/) has no proved speedup. Deciding the ground energy of a 2-local Hamiltonian is QMA-complete; with a guiding state of overlap $\gamma$, [ground state energy estimation](/ground-state-energy-estimation/) uses $\tilde O((\alpha/(\gamma\epsilon))\log(1/\delta))$ calls to a block encoding.

| Method | Access | Cost for time $t$, error $\epsilon$ | Guarantee |
|---|---|---|---|
| First order formula | local terms or Pauli list | $\lceil t^2\alpha_1/(2\epsilon)\rceil$ steps, $L$ exponentials each | spectral norm, proved bound |
| Second order formula | same | $\lceil t^{3/2}(\beta_2/\epsilon)^{1/2}\rceil$ steps, $2(L-1)r + 1$ exponentials | spectral norm, proved bound |
| [Order $2k$ formula](/higher-order-trotter-suzuki/) | same | $O(t^{1+1/(2k)}/\epsilon^{1/(2k)})$ steps of $5^{k-1}$ stages | spectral norm, bounds often loose |
| qDRIFT | Pauli list | about $2\lambda^2t^2/\epsilon$ rotations | half diamond norm, random |
| Truncated Taylor series | Pauli list or sparse | $O(\lambda t\log(\lambda t/\epsilon)/\log\log(\lambda t/\epsilon))$ queries | spectral norm, ancillas |
| [Interaction picture](/interaction-picture-simulation/) | $H = A + B$, $e^{-iAs}$ easy | the same with $\lambda_B$ for $\lambda$ | spectral norm, ancillas |
| [Multi-product formula](/multi-product-formulas/) | Pauli list | $m$ product formulas joined by LCU | error order $2m$ |
| Qubitization with QSP | block encoding of $H/\alpha$ | $O(\alpha t + \log(1/\epsilon))$ queries | spectral norm, success $\ge (1-\epsilon)^2$ |
| [Optimal sparse simulation](/optimal-hamiltonian-simulation/) | sparse oracle | $O(\tau + \log(1/\epsilon)/\log(e + \log(1/\epsilon)/\tau))$ queries | matches the query lower bound |
| [Density matrix exponentiation](/density-matrix-exponentiation/) | copies of $\rho$ | at most $4t^2/\epsilon$ copies | diamond norm; $\Omega(t^2/\epsilon)$ copies needed |
| VQE | Pauli list | $L\lceil 2\lambda^2\ln(2L/\delta)/\epsilon^2\rceil$ runs per energy | heuristic optimization |

: Methods for dynamics and energies. $L$ is the number of terms, $\lambda$ their coefficient sum, $\alpha$ the normalization of a block encoding, $\tau = d\|H\|_{\max}t$, and $\delta$ the failure probability of an estimate.

## Choosing a method

For a lattice model on a device with no spare qubits, use the second or fourth order formula and choose $r$ from commutator bounds or from the error measured on small sizes; the norm bounds can ask for hundreds of times more steps than needed. For a Hamiltonian with very many terms of unequal weight, as in chemistry, compare qDRIFT with the product formulas: its count does not grow with $L$, but it grows as $t^2/\epsilon$.

For long times and small errors on a fault-tolerant machine, build a block encoding by LCU of the Pauli strings, so $\alpha = \lambda$, and use qubitization with quantum signal processing. Use the interaction picture when a large part of $H$ is diagonal or otherwise easy, and the time-dependent methods, whose cost follows $\int\|H(t)\|\,dt$, when $H$ changes.

For ground energies, phase estimation with a good guiding state has proved costs; VQE is a heuristic for small devices. Check any variational energy against a lower bound, such as Temple's, or against exact results on small sizes.
