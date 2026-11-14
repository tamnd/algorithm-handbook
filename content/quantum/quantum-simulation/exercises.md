1. ◦ The two-qubit operator $N$ multiplies each basis state $|x\rangle$ by $x$, for $x = 0, 1, 2, 3$. Qubit 0 is the least significant bit of $x$ and the rightmost symbol of a Pauli string. Write $N$ as a [Pauli string decomposition](/pauli-string-decomposition/), and give the coefficient sum $\lambda$ of the terms other than $II$.

2. ◦ Run [qDRIFT](/qdrift/) on $H = 2\,ZZ - 0.5\,XI + 1.5\,IX + 3\,II$ for $t = 0.5$. Which term should be dropped before sampling, and why? Give $\lambda$, the probability of each remaining term, the time $\lambda t/N$ for which each sampled term acts, and the number of samples $N = \lceil 2\lambda^2t^2/\epsilon\rceil$ for $\epsilon = 10^{-3}$.

3. ◦ A Hamiltonian has $L = 3$ terms and is simulated with $r = 10$ steps. How many exponentials of single terms does the second order formula use, after merging neighbouring half steps? How many do the [higher-order Trotter-Suzuki](/higher-order-trotter-suzuki/) formulas of order 4 and order 6 use with the same $r$?

4. ◦ A Pauli list has $L = 4$ terms with $\lambda = 3$, and the time is $t = 10$. For the [truncated Taylor series](/truncated-taylor-series-simulation/), find the number of segments $r$, the value of $\lambda\tau$ for one segment, and the number of calls to SELECT in the whole circuit. How many index tuples does the list of terms up to order $K = 4$ contain?

5. ◦ Find the weights $C_1, C_2$ of the [multi-product formula](/multi-product-formulas/) with step numbers $k = (1, 3)$, check that they cancel the error term in $1/k^2$, and give the 1-norm $s = |C_1| + |C_2|$. Compare it with $s$ for $k = (1, 2)$.

6. ◦ Under the [Jordan-Wigner transformation](/jordan-wigner-transformation/) on 4 modes, write the hop $a_1^\dagger a_3 + a_3^\dagger a_1$ as a sum of Pauli strings, with qubit 0 on the right.

7. ◦ A qubit starts in $|{+}\rangle$ and undergoes amplitude damping with rate $\gamma = 1$, as in [open quantum system simulation](/open-quantum-system-simulation/). Give its density matrix at $t = 2\ln 2$ and its purity $\mathrm{Tr}\,\rho^2$.

8. ◦ Compute the Chebyshev value $T_3(1/2)$. Using $\sin((2\ell + 1)\theta) = (-1)^\ell T_{2\ell+1}(\sin\theta)$, explain what it says about one round of [amplitude amplification](/amplitude-amplification/) started from success probability $1/4$.

9. ◦ A particle on a chain with hopping $J$ meets a single impurity of strength $V$. With the transmission $T(k) = 4J^2\sin^2k/(4J^2\sin^2k + V^2)$ from [quantum scattering simulation](/quantum-scattering-simulation/), find $T(\pi/2)$ for $V = 2J$, and the strength $V$ at which $T(\pi/2) = 0.9$.

10. • The transverse-field Ising ring of $n$ sites has $H = A + B$ with $A = \sum_j Z_jZ_{j+1}$ (indices mod $n$) and $B = h\sum_j X_j$. Show by the triangle inequality that $\|[A, B]\| \le 4hn$. Using the [Lie-Trotter](/lie-trotter-product-formula/) bound, how many steps suffice for $n = 20$, $h = 0.5$, $t = 5$ and $\epsilon = 0.01$?

11. • A Hamiltonian has $L$ Pauli terms, each with coefficient of size $\Lambda$. Compare the number of exponentials that Lloyd's [universal quantum simulator](/universal-quantum-simulator/) bound asks for, $Lr$ with $r = \lceil L(L-1)\Lambda^2t^2/(2\epsilon)\rceil$, with the qDRIFT count $\lceil 2\lambda^2t^2/\epsilon\rceil$. For which $L$ does qDRIFT ask for fewer? Say why the comparison is fair even though the two bounds use different norms.

12. • Suzuki's order 6 formula is $S_6(x) = S_4(p_3x)^2\,S_4((1 - 4p_3)x)\,S_4(p_3x)^2$ with $p_3 = 1/(4 - 4^{1/5})$, and $S_4$ is built the same way from $S_2$ with $p_2 = 1/(4 - 4^{1/3})$. Each of its 25 stages runs $S_2$ for a time $w\,x$. List the distinct weights $w$ with their multiplicities, check that they add up to 1, and find the most negative one and the sum $\sum |w|$.

13. • Block-encode $H = 0.6\,X + 0.8\,Z$ by LCU with $\alpha = 1.4$, using a PREP that is a reflection, so that $U$ is Hermitian. What are the eigenvalues of the [qubitization](/qubitization/) walk $W = (2\Pi - I)U$ on the two qubits? If phase estimation on $W$ returns the phase $0.7752$, which energy does it report?

14. • For $H = -ZZ - XI - IX$, minimize the energy over all product states $|a\rangle \otimes |b\rangle$ with real amplitudes, that is over Bloch vectors in the $xz$-plane. Compare the best value with the ground energy $-\sqrt5$. Why can complex amplitudes not do better?

15. • For the same $H$ and the trial state $|{+}{+}\rangle$, compute $\langle H\rangle$, $\langle H^2\rangle$ and the variance. Find the first excited energy $E_1$ and apply Temple's inequality from the [variational method](/variational-method/). Which interval for $E_0$ do the two bounds give?

16. • A qubit undergoes amplitude damping with rate $\gamma$ and dephasing with $L = \sqrt g\,Z$ at the same time. Show that the populations follow the damping alone and that the coherence decays as $e^{-(\gamma/2 + 2g)t}$. For $\gamma = 1$ and $g = 0.5$, when has the coherence halved?

17. • In [Hamiltonian learning](/hamiltonian-learning/) at high temperature one estimates the coefficient of a Pauli term by $c \approx -\mathrm{Tr}(P\rho)/\beta$. For one qubit with $H = hZ$ and $h = 1$, give the estimate and its error at $\beta = 0.2$ and $\beta = 0.1$, and find the leading term of the error in $\beta$.

18. • The [variational quantum eigensolver](/variational-quantum-eigensolver/) measures each of the $L$ terms of $H$ with $S = \lceil 2\lambda^2\ln(2L/\delta)/\epsilon^2\rceil$ shots. For $H = -ZZ - XI - IX$, $\epsilon = 0.01$ and $\delta = 0.05$, find $S$ and the total number of circuit runs for one energy. How does the total change if $\epsilon$ is halved?

19. • Write a program that finds the least degree $2R + 1$ for which the Jacobi-Anger tail $2\sum_{k > 2R}|J_k(\tau)|$ is at most $\epsilon$, as in [optimal Hamiltonian simulation](/optimal-hamiltonian-simulation/). Check it on $\tau = 1, 2, 4, 8$, then give the degree and the number of calls $5(4R + 1)$ for $\tau = 16$ and $\tau = 32$ at $\epsilon = 10^{-6}$.

20. ★ The symmetric second order step has error $x^3E_3 + O(x^5)$ with no even powers. Show that the composition $S_2(px)^2S_2((1 - 4p)x)S_2(px)^2$ is of order 4 exactly when $4p^3 + (1 - 4p)^3 = 0$. Solve for $p$, and show that every real solution makes at least one step run backwards in time.

21. ★ Prove that the weights $C_q = \prod_{p \ne q} k_q^2/(k_q^2 - k_p^2)$ of a multi-product formula satisfy $\sum_q C_q = 1$ and $\sum_q C_qk_q^{-2j} = 0$ for $1 \le j \le m - 1$. Then give the weights and the 1-norm $s$ for $k = (1, 2, 4)$, and compare with $s = 3.1333$ for $k = (1, 2, 3)$.

22. ★ The [Lieb-Robinson bound](/lieb-robinson-bound/) for a chain with couplings of size $J$ is $\frac43\|A\|\|B\|\sum_{k \ge d}(6J|t|)^k/k!$. Take $J = 1$ and $\|A\| = \|B\| = 1$, and find, to three digits, the largest $t$ at which the bound is at most $10^{-3}$, for $d = 50$ and $d = 100$. Compare $d/t$ with $v = 6eJ$, and with the speed $2J$ of the front measured for the XX chain.

23. ★ For $H = ZZ + 0.8\,XI + 0.8\,IX$, with $\beta_2 = 1.12$, $t = 4$ and $\epsilon = 10^{-4}$, find the number of second order steps that the bound $t^3\beta_2/r^2 \le \epsilon$ asks for. Then write a program that computes the true error $\|S_2(t/r)^r - e^{-iHt}\|$, with the step $e^{-iZZ\delta/2}e^{-0.4iXI\delta}e^{-0.8iIX\delta}e^{-0.4iXI\delta}e^{-iZZ\delta/2}$, and find the least $r$ that meets $\epsilon$. Give both exponential counts.

24. ★ Run qDRIFT on $H = ZI + IZ$, whose terms commute, so that one step of the first order formula is exact. Start from $|{+}{+}\rangle$ with $t = 1$. Show that after $N$ samples the fidelity of the averaged state with the exact state is $\sum_m \binom{N}{m}2^{-N}\cos^4\big((2m/N - 1)t\big)$, give its value for $N = 100$, and find the leading behaviour of $1 - F$ in $N$.
