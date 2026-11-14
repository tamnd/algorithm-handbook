1. ◦ Two [qubits](/qubit/) are in the [state](/quantum-state/) $\frac{1}{\sqrt6}\left(|00\rangle + i|01\rangle - 2|11\rangle\right)$, with qubit 0 the rightmost symbol. Give the probability of each outcome of a measurement of both qubits ([Born rule](/born-rule/)). Then measure only qubit 0: give the probability that it reads 1 and the state that is left. Is the state [entangled](/entanglement/)?

2. ◦ Write the $4 \times 4$ matrix, in the basis $|00\rangle, |01\rangle, |10\rangle, |11\rangle$, of the [CNOT gate](/cnot-gate/) with control qubit 0 and target qubit 1. Apply a [Hadamard gate](/hadamard-gate/) on qubit 0 and then this CNOT to $|00\rangle$. Then check that the circuit "$H$ on qubit 1, then $X$ on qubit 0" has the matrix $H \otimes X$.

3. ◦ Apply $H$, then $S$, then $H$ to $|0\rangle$ ([phase and T gates](/phase-and-t-gates/)). Give the final state, the probability of reading 0, and the point on the [Bloch sphere](/bloch-sphere/).

4. ◦ Apply $H$ to qubit 1 and then a CNOT with control qubit 1 and target qubit 0 to the basis state $|10\rangle$. Which [Bell state](/bell-states/) do you get? Compute its expectation values for $Z \otimes Z$, $X \otimes X$ and $Y \otimes Y$.

5. ◦ Run the [Deutsch-Jozsa algorithm](/deutsch-jozsa-algorithm/) for $n = 2$ on $f(x) = x_0 \oplus x_1$ and on $f(x) = x_1$, where $x = x_1 x_0$. Which string $y$ does each run measure? Then run it on the function that is 1 only at $x = 11$, which breaks the promise, and give the probability of each outcome.

6. ◦ The [Bernstein-Vazirani algorithm](/bernstein-vazirani-algorithm/) is given the oracle of $f(x) = s \cdot x \oplus 1$ instead of $s \cdot x$, with $s = 1011$. What does it measure, and why does the added constant not matter? How many queries would a deterministic classical algorithm need?

7. ◦ The three-qubit state $(|1\rangle + |5\rangle)/\sqrt2$, with basis states written as integers, has period 4. Apply the [quantum Fourier transform](/quantum-fourier-transform/) and give the probability of each outcome. How many gates does the exact QFT circuit on 5 qubits use, counting Hadamards, controlled phases and swaps?

8. ◦ A qubit is $|0\rangle$ or $|+\rangle$, each with probability $\frac12$. Write its [density matrix](/density-matrix/), its Bloch vector, its eigenvalues, its purity $\mathrm{Tr}\,\rho^2$ and its [von Neumann entropy](/von-neumann-entropy/).

9. ◦ A qubit is $|0\rangle$ or $|+\rangle$ with equal priors. Find the best probability of guessing which, using the [trace distance](/trace-distance/) ([state discrimination](/state-discrimination-problem/)). Then find the success probability of the best measurement that never guesses wrong but may answer "don't know".

10. • A state-vector simulator stores $2^n$ complex amplitudes of 16 bytes each. What is the largest $n$ that fits in $2^{40}$ bytes? Write the loop that applies a $2 \times 2$ gate to qubit $j$: which pairs of indices does it combine, and how many pairs are there? Test it on exercise 2.

11. • Build a circuit of [Toffoli gates](/toffoli-gate/) and $X$ gates on wires $x_1, x_2, x_3$, one clean [ancilla](/ancilla-qubits/) and a target $y$ that maps $|x_1 x_2 x_3\rangle|0\rangle|y\rangle$ to $|x_1 x_2 x_3\rangle|0\rangle|y \oplus (x_1 \vee x_2 \vee x_3)\rangle$. The ancilla must end in $|0\rangle$ ([uncomputation](/uncomputation/)). How many Toffoli gates do you need?

12. • For the two-qubit state $(|00\rangle + |01\rangle + |10\rangle)/\sqrt3$, compute the reduced density matrix of qubit 0 by the [partial trace](/partial-trace/), its eigenvalues, and the [entanglement entropy](/entanglement-entropy/). Write the Schmidt decomposition of the state.

13. • In [Simon's problem](/simon-problem/) with $n = 3$ and $s = 110$, list the strings $y$ that one run of [Simon's algorithm](/simon-algorithm/) can return. Give the probability that the first two runs already determine $s$, and the expected number of runs until they do. Check the expectation against the formula $n - 1 + \sum_{j=1}^{n-1} 1/(2^j - 1)$.

14. • Run [quantum phase estimation](/quantum-phase-estimation/) with $t = 2$ counting qubits on an eigenvector with phase $\varphi = 1/3$. Give the exact probability of each outcome $m \in \{0, 1, 2, 3\}$ and check that the outcomes within $1/4$ of $\varphi$ have total probability at least $8/\pi^2$. How many counting qubits does the rule $t = b + \lceil \log_2(2 + 1/(2\delta)) \rceil$ give for $b = 5$ bits with failure probability $\delta = 0.01$?

15. • You hold many copies of an unknown state that is either $|0\rangle$ or $|+\rangle$, and you test whether it equals $|0\rangle$ by running the [swap test](/swap-test/) against fresh copies of $|0\rangle$. You answer "equal" unless some run reads 1. If the state is $|+\rangle$, what is the chance of a wrong answer after $k$ runs, and how many runs make it below 1%?

16. • Use the [stabilizer formalism](/stabilizer-formalism/) to track the circuit $H$ on qubit 0, CNOT from qubit 0 to qubit 1, CNOT from qubit 1 to qubit 2, on $|000\rangle$. Start from the generators $IIZ$, $IZI$, $ZII$ and give the generators after each gate. Then measure $X$ on qubit 0: give the probability of each outcome and the new generators ([Gottesman-Knill theorem](/gottesman-knill-theorem/)).

17. • The depolarizing [channel](/quantum-channel/) $\mathcal D_p(\rho) = (1 - p)\rho + p I/2$ has the [Kraus operators](/kraus-operators/) $\sqrt{1 - 3p/4}\,I$ and $\frac{\sqrt p}{2}X$, $\frac{\sqrt p}{2}Y$, $\frac{\sqrt p}{2}Z$. Check that they satisfy $\sum_k K_k^\dagger K_k = I$. Show that $\mathcal D_q \circ \mathcal D_p = \mathcal D_r$ with $1 - r = (1 - p)(1 - q)$. For the input $|0\rangle$, give the [fidelity](/fidelity/) and the trace distance between $\mathcal D_p(|0\rangle\langle 0|)$ and $|0\rangle\langle 0|$.

18. • For the three-qubit bit-flip code with projector $P = |000\rangle\langle 000| + |111\rangle\langle 111|$, check the Knill-Laflamme conditions $P E_a^\dagger E_b P = c_{ab} P$ for the error set $\{I, X_0, X_1, X_2\}$ ([quantum error correction](/quantum-error-correction/)). Show that they fail once $Z_0$ is added, and say what a $Z_0$ error does to the encoded qubit.

19. • Alice and Bob share $|\Phi^+\rangle$, and Bob and Charlie share another $|\Phi^+\rangle$. Bob measures his two qubits in the Bell basis. Show that each of the four outcomes has probability $\frac14$ and leaves Alice and Charlie in a Bell state, and say which one. This is entanglement swapping; compare it with [teleportation](/quantum-teleportation/).

20. • Show that every circuit of CNOT and $X$ gates computes a map $x \mapsto Ax \oplus b$ on bit strings, with $A$ an invertible matrix over $\mathbb{F}_2$. Deduce that no such circuit computes the Toffoli gate, even with ancillas that start and end in fixed states ([reversible computation](/reversible-computation/)).

21. • The approximate QFT on $n$ qubits keeps only the controlled phase gates $\mathrm{CR}_k = \mathrm{diag}(1, 1, 1, e^{2\pi i/2^k})$ with $k \le m$. For $n = 5$ and $m = 3$, how many controlled phases are kept? Bound the operator-norm error by summing $\lVert \mathrm{CR}_k - I\rVert = 2\sin(\pi/2^k)$ over the dropped gates, and give an $m$ of order $\log_2(n/\varepsilon)$ for which the bound is at most $\varepsilon$ for any $n$.

22. ★ In the GHZ game three players who cannot talk receive bits $r, s, t$ with $r \oplus s \oplus t = 0$, each of the four allowed inputs with probability $\frac14$, and answer bits $a, b, c$. They win when $a \oplus b \oplus c = r \vee s \vee t$. Show that every classical strategy wins with probability at most $\frac34$. Show that players who share $(|000\rangle + |111\rangle)/\sqrt2$ and measure $X$ on input 0 and $Y$ on input 1 always win. Compare with the [CHSH inequality](/chsh-inequality/) and [Bell's theorem](/bell-theorem/).

23. ★ Phase estimation with one control qubit. In round $r = 0, 1, \ldots, t - 1$, prepare the control in $|+\rangle$, apply controlled $U^{2^{t-1-r}}$ to the eigenvector, apply $\mathrm{diag}(1, e^{-2\pi i \omega_r})$ with $\omega_r = \sum_{j < r} b_j 2^{j - r - 1}$, apply $H$ and measure the bit $b_r$. Show that $m = \sum_r b_r 2^r$ has the same distribution as the output of the [phase estimation](/quantum-phase-estimation/) circuit with $t$ counting qubits and the inverse QFT. Check it on $\varphi = 5/8$, $t = 3$, and on $\varphi = 0.3$, $t = 4$.

24. ★ The swap test needs controlled swaps. Show that the following gives the same statistics: pair qubit $i$ of $|\psi\rangle$ with qubit $i$ of $|\phi\rangle$ for each $i$, measure each pair in the Bell basis, and output 1 when the number of singlets $|\Psi^-\rangle$ is odd. Prove that the probability of output 1 is $(1 - |\langle\psi|\phi\rangle|^2)/2$. Check that this circuit needs only CNOT and $H$ gates and no ancilla.

25. ★ The Werner state $\rho_p = p\,|\Phi^+\rangle\langle\Phi^+| + (1 - p) I/4$ is entangled exactly when $p > 1/3$. Show that its largest CHSH value over all choices of one-qubit observables $A_0, A_1, B_0, B_1$ is $2\sqrt2\,p$, so the CHSH test detects its entanglement only for $p > 1/\sqrt2$. Use the correlation matrix $T_{ij} = \mathrm{Tr}(\rho_p\, \sigma_i \otimes \sigma_j)$.

26. ★ You receive $k$ copies of a pure state, $|\psi\rangle^{\otimes k}$ or $|\phi\rangle^{\otimes k}$, with equal priors. Show that the best probability of a correct guess is $\frac12\left(1 + \sqrt{1 - |\langle\psi|\phi\rangle|^{2k}}\right)$. For $|0\rangle$ against $|+\rangle$, how many copies make the error probability at most 1%? How many copies does it take to reach 1% if you measure each copy in the same one-copy optimal basis and take a majority vote?
