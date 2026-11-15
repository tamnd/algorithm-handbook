1. KCL gives one equation per node except ground, so 6, and KVL gives $b - n + 1 = 12 - 7 + 1 = 6$. MNA has 6 node voltages and 2 source currents, 8 unknowns. The tableau has $6 + 2 \cdot 12 = 30$.

5. (H, L, 0) gives 0, since a forcing value beats the weak ones. (1, 0, Z) gives X. (L, Z) gives L. (W, H) gives W, the weak unknown.

8. Delta 1: $b$ becomes 0 and $d = 1 \oplus 1 = 0$, both computed from the values at delta 0. Delta 2: $c$ becomes 0. Delta 3: $d = 1 \oplus 0 = 1$. So $d$ is 0 in deltas 1 and 2, a glitch of zero length that a process sensitive to $d$ still sees.

11. Phase A sets both changing inputs to X, and $X \oplus X = X$; phase B ends at $1 \oplus 1 = 0$. So the output goes 0, X, 0 and is reported as a static hazard. Gate-by-gate ternary simulation is sound, so a circuit can give 0 or 1 only where every completion of the inputs does. The completions $(0, 1)$ and $(0, 0)$ of $(X, X)$ give 1 and 0, so every circuit for XOR reports X. The hazard is in the function, not in the gates.

12. KCL gives $E = v^3 - 6v^2 + 11v = (v - 1)(v - 2)(v - 3) + 6$. With $v = 2 + u$ this is $6 + u^3 - u$, whose local extremes at $u = \pm 1/\sqrt 3$ are $6 \mp 2\sqrt 3/9$. Three operating points exist iff $|E - 6| < 2\sqrt 3/9 \approx 0.385$, that is for $5.615 < E < 6.385$.

14. Eliminating a node of a cycle of length $L \ge 4$ joins its two neighbours, which were not adjacent, so it adds one edge and leaves a cycle of length $L - 1$. A triangle gives no fill. So every order adds $n - 3$ edges, which are $2(n - 3)$ entries. The first pivot has $r = c = 3$ and a Markowitz count of $(3 - 1)(3 - 1) = 4$, but creates only 2 fill entries: two of the four positions it counts are the diagonal entries of the neighbours, which are already nonzero.

16. In charge sharing the stored values have only the strengths of their node sizes, and the largest size wins. With sizes 3, 1, 3 the two largest nodes hold 1 and 0, a tie, so all three nodes become X. With $c_2$ of size 2 the bus wins and all three become 1.

18. The node matrix is $\begin{pmatrix} s + 2 & -1 & 0 \\ -1 & s + 2 & -1 \\ 0 & -1 & s + 1 \end{pmatrix}$, whose determinant is $s^3 + 5s^2 + 6s + 1$, so $H(s) = 1/(s^3 + 5s^2 + 6s + 1)$. The moments are $1, -6, 31, -157, 793$. Order 1 gives $1/(1 + 6s)$, with the pole $-1/6$ set by the Elmore delay 6. Order 2 matches four moments and gives $(5 - s)/(5 + 29s + 19s^2)$, with poles $-0.19813$ and $-1.32818$. The ladder has poles $-0.19806$, $-1.5550$ and $-3.2470$, so the dominant pole is already close.

21. Induct over a topological order. A gate output can change at time $t$ only if some input changed at $t - 1$, so its change times are the input's change times plus 1, and the times of a net are among the path lengths to it. For $y$ the paths from $a$ have lengths 2 (through $ab$) and 3 (through the inverter and $\bar a c$). So $y$ changes at most twice, and the bound is reached when $a$ falls: $y$ drops at 2 and rises at 3.

22. The TR stage gives $y_\gamma = \frac{1 + cz}{1 - cz} y_k$ with $c = \gamma/2$, and for $\gamma = 2 - \sqrt 2$ the BDF2 stage has the same coefficient $(1 - \gamma)/(2 - \gamma) = c$. Then $R(z) = \bigl(\frac{1 + cz}{1 - cz} - (1 - \gamma)^2\bigr) / \bigl(\gamma (2 - \gamma)(1 - cz)\bigr)$. Expanding gives $R(z) - e^z \approx 0.0408\, z^3$, and as $z \to -\infty$ the numerator tends to a constant while the denominator grows, so $R \to 0$. The zero is at $z = -(1 + \sqrt 2) \approx -2.414$. The minimum is $-(\sqrt 2 - 1)/2 \approx -0.2071$ at $z = -(4 + 3\sqrt 2) \approx -8.243$.

23. The element has no memory, so collocation solves $v + v^3 = \cos t_i$ at each sample alone: $v_0 = 0.68233$ and $v_1 = v_2 = -0.42385$. These samples are exact. Their DFT gives a DC term of $-0.05513$ and a fundamental of amplitude $0.73745$. The true waveform satisfies $v(t + T/2) = -v(t)$, so its DC term is 0 and its fundamental is $0.72899$. Both errors are aliasing: on three samples the odd harmonics of $v$ fold onto DC (the third, the ninth) and onto the fundamental (the fifth, the seventh).

24. With $\lambda = (1/2, 1)$ from exercise 15, the resistors contribute $\frac14 \cdot 4kT$, $\frac14 \cdot 4kT$ and $1 \cdot 4kT/2$, which sum to $4kT \cdot 1\ \Omega = 1.657 \times 10^{-20}\ \text{V}^2/\text{Hz}$, or $0.129$ nV/$\sqrt{\text{Hz}}$. In general $Y\lambda = e_k$ and $\sum_j G_j (\lambda_p - \lambda_q)^2 = \lambda^{\mathsf T} Y \lambda = \lambda^{\mathsf T} e_k = Z_{kk}$, which is Nyquist's theorem for a one-port.

25. With the dense row and column last, each column $k < n$ has a single off-diagonal entry in row $n$, so $f = n - 1$ and the searches reach $3n - 2$ rows. With them first, column 1 fills the whole matrix, so column $k$ reaches all $n$ rows, the searches reach $n^2$ rows, and $f = \sum_{k=1}^{n-1} k^2 = (n - 1)n(2n - 1)/6$. For $n = 10$ the two values are 9 and 285.
