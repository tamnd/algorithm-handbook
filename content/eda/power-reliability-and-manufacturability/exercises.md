1. ◦ A 64-bit bus has 50 fF on each line, a 0.9 V supply and a 1.5 GHz clock, and each line has a rising transition in 20 percent of the cycles. Compute its [dynamic power](/dynamic-power-dissipation/).

2. ◦ The inputs of a two-input XOR gate are independent, each is 1 with probability $1/4$, and each is temporally independent from cycle to cycle. Find the signal probability of the output, its zero-delay toggle rate $\alpha$ and its rising activity $\alpha_{0 \to 1}$, in the sense of [switching activity](/switching-activity/).

3. ◦ A transistor has subthreshold slope factor $n = 1.5$ and thermal voltage $v_T = 25.9$ mV. By what factor does its [leakage](/leakage-power/) grow when its threshold voltage is lowered by 60 mV? What is its subthreshold swing in mV per decade?

4. ◦ Putting a block to sleep and waking it costs 3 nJ. The block leaks 15 mW when on, and the sleep switch still lets 5 percent of that through when off. Find the shortest idle period for which [power gating](/power-gating/) saves energy.

5. ◦ A pilot run of [Monte Carlo power estimation](/monte-carlo-power-estimation/) gives a sample standard deviation of 0.3 times the sample mean. How many samples does the stopping rule with $z = 1.96$ and relative error $\varepsilon = 0.05$ need?

6. ◦ A victim wire has 18 fF to ground and 6 fF of coupling to an aggressor that swings 1 V. Find the [crosstalk](/crosstalk-noise/) glitch on the victim when it floats. Then take a driven victim with $R = 1$ kΩ, 20 fF to ground and 10 fF of coupling, and give the delay estimate $0.69 R (C_g + k C_c)$ for the charge-based [Miller factors](/miller-coupling-factor/) $k = 0, 1, 2$ of an aggressor switching with the victim, quiet, and against it, with equal ramps.

7. ◦ Two parallel wires of length $L = 50$ µm are $s = 2$ µm apart. Compute the short [critical area](/critical-area/) $(L + 2r)(2r - s)^+$ for square defects of half-width $r = 0.9$, $1.5$ and $3$ µm.

8. ◦ A chip has mean fault count $\lambda = 0.5$. Compute its yield under the [Poisson](/poisson-yield-model/), [Murphy](/murphy-yield-model/) and [negative binomial](/negative-binomial-yield-model/) models, the last with $\alpha = 2$.

9. ◦ With [Black's equation](/black-equation/) and $E_a = 0.7$ eV, how many times longer does a wire last at 105 °C than at 125 °C at the same current density? What does doubling the current density do to the lifetime when $n = 2$?

10. ◦ A metal has $(jL)_c = 2500$ A/cm. Find the [Blech length](/blech-length/) at $j = 1.25$ MA/cm², and the largest current density for which a 25 µm segment is immortal.

11. ◦ Under the [Hopkins model](/hopkins-imaging-model/), the smallest pitch that a lens of numerical aperture NA passes is $\lambda / \mathrm{NA}$ for coherent light and $\lambda / (\mathrm{NA}(1 + \sigma))$ for partial coherence $\sigma$. Compute both for a dry ArF scanner with $\lambda = 193$ nm, NA $= 0.93$ and $\sigma = 0.7$.

12. • Inputs $a$ and $b$ are independent and fair. Run [signal probability propagation](/signal-probability-propagation/) gate by gate on $y = a \oplus (a \wedge b)$ and on $z = a \wedge (a \vee b)$, and compare with the exact probabilities. Which way is each error?

13. • Use [transition density](/transition-density/) to propagate densities of $10^6$ transitions per second on three independent fair inputs through a three-input OR gate, and through a three-input XOR gate.

14. • The inputs $a$ and $b$ of an AND gate are independent and fair, and each keeps its value from one cycle to the next with probability $9/10$. Compute the exact zero-delay toggle rate of the output, as the [BDD method](/bdd-switching-activity-estimation/) would, and compare it with the value under temporal independence.

15. • All four inputs of a four-input parity function take new uniform random values at time 0. Count the expected transitions on the three gate outputs under unit delay for the chain $((a \oplus b) \oplus c) \oplus d$ and for the tree $(a \oplus b) \oplus (c \oplus d)$, and compare with zero delay. How much of the chain's activity is [glitch power](/glitch-power/)?

16. • A 4-bit bus with [bus-invert coding](/bus-invert-coding/) starts in state (0000, INV = 0) and sends the words 1110, 0001, 0111. Give the coded words and count the toggles of all five lines, against the plain bus. Then find the mean number of toggles per transfer for uniform random words.

17. • A chain of three gates has deadline $T = 36$. Gate $g_1$ has delay 10 or 14 and leakage 32 or 2 at low or high threshold, $g_2$ has delay 8 or 11 and leakage 15 or 1, and $g_3$ has delay 12 or 15 and leakage 25 or 3. Solve [threshold assignment](/multi-threshold-voltage-assignment/) exactly, and compare with the greedy rule that raises gates in order of leakage saved per unit of added delay.

18. • A circuit has gates $g_1 \to g_2 \to g_3$ and $g_4 \to g_3$, with $g_3$ driving a register and the deadline $T = 8$. Each gate has delay 2 at $V_H = 1.2$ V and 2.8 at $V_L = 0.8$ V, and all gates switch the same capacitance. Run [clustered voltage scaling](/clustered-voltage-scaling/) back from the output and give the fraction of dynamic power saved.

19. • A [power grid](/power-grid-analysis/) is a chain: a pad feeds node 1 through 40 S, node 1 feeds node 2 through 20 S, and node 2 feeds node 3 through 20 S. Each node draws 0.2 A. Find the three drops and row 3 of $G^{-1}$. Then let each current lie in $[0, 0.4]$ A with total at most 0.6 A, and find the worst drop at node 3 by [vectorless verification](/vectorless-power-grid-verification/), and without the total bound.

20. • On the grid of exercise 19 with 0.2 A at each node, a [random walk](/random-walk-power-grid-analysis/) from node 3 moves to a neighbor with probability proportional to the conductance and stops at the pad. Find the expected number of visits to each node and check that the expected reward is the drop at node 3.

21. • A victim RC tree has a driver resistance of 2 kΩ to node 1 and a wire of 1 kΩ from node 1 to node 2. An aggressor rising 1 V in 40 ps couples 5 fF into node 2. Compute the [Devgan metric](/devgan-noise-metric/) at both nodes. Then split the same 5 fF as 2.5 fF at each node and compute it again.

22. • A product has yield 0.7, fitted by the negative binomial model with $\alpha = 2$. Predict the yield of a chip with twice the critical area, and compare with the Poisson prediction from the same 0.7.

23. • For [design centering](/design-centering/), find the largest disc inside the triangle $x \ge 0$, $y \ge 0$, $x + 2y \le 4$ by writing the linear program that [simplicial approximation](/simplicial-approximation/) solves on a polytope, and solving it.

24. • A row of four unit tiles has metal densities 0.6, 0.2, 0.5 and 0.1, and at most 0.15 of fill can be added to each tile. Windows are pairs of adjacent tiles, with density the mean of the two. Find the largest possible smallest window density, as in [LP fill](/lp-density-fill/), and the least total fill that reaches it.

25. • A PMOS transistor shifts by 8.0 mV after $10^3$ s of stress and by 11.7 mV after $10^4$ s. Fit the exponent of a power law $A t^n$, compare it with the exponents of the [reaction-diffusion model](/nbti-reaction-diffusion-model/), and extrapolate to ten years ($3.156 \times 10^8$ s) with $n = 1/6$ and with $n = 1/4$.

26. ★ Let the defect density of a chip be $D X$, with $X \ge 0$ random and $E[X] = 1$. Prove that the yield $E[e^{-\lambda X}]$ is at least the Poisson yield $e^{-\lambda}$. Then prove that the negative binomial yield $(1 + \lambda/\alpha)^{-\alpha}$ falls as $\alpha$ grows and tends to $e^{-\lambda}$.

27. ★ Prove that every stationary zero-delay 0-1 sequence with $P(y_k = 1) = p$ has toggle rate $\alpha \le 2 \min(p, 1 - p)$, whatever its correlation in time, and that the bound is attained. Conclude the largest toggle rate of a four-input AND gate whose inputs are independent fair processes, and give inputs that reach it.

28. ★ A die has thermal resistance $R$ to ambient and draws 30 W of dynamic power and $10 e^{0.02 \theta}$ W of leakage at a temperature rise of $\theta$ K. Find $\theta$ for $R = 0.8$ K/W, show that the iteration $\theta \leftarrow R(30 + 10 e^{0.02 \theta})$ converges there, and find the largest $R$ for which a fixed point exists, as with the [compact thermal model](/compact-thermal-model/).

29. ★ A transmission cross coefficient matrix on two frequencies is $T = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$, and the intensity at a point is $u^* T u$ for mask amplitudes $u$. Keep one kernel as in the [sum of coherent systems](/sum-of-coherent-systems/), and compute the error for $u = (1, 1)$ and $u = (1, -1)$. Prove that the error for any $u$ lies in $[0, \lambda_2 \|u\|^2]$, and show that both ends are attained.

30. ★ A victim node with resistance $R$ to its driver and capacitance $C$ to ground is coupled by $C_c$ to an aggressor ramp of slope $s$ and length $t_r$. Solve for the victim voltage, find its peak, and show that it is below Devgan's $R C_c s$ and tends to it as $t_r$ grows. Evaluate with $R = 1$ kΩ, $C = 15$ fF, $C_c = 5$ fF and a 1 V ramp of 20 ps.
