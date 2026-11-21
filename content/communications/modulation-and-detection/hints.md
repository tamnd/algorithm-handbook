1. At 6 dB, $E_b/N_0 = 3.981$, so $P_b = Q(2.822) = 2.388 \times 10^{-3}$. The Chernoff bound is
$\tfrac12 e^{-3.981} = 9.33 \times 10^{-3}$, about 3.9 times larger. The exponent is right; the bound loses
the factor of order $1/x$ in front.

3. $C = 10^6\log_2(101) = 6.658$ Mbit/s. At $\eta = 3$ the limit is $(2^3 - 1)/3 = 7/3$, or $3.68$ dB.

4. $\eta = (2/3) \cdot 4/1.35 = 1.975$ bits/s/Hz. The symbol rate is $5/1.35 = 3.704$ million per second and
the information rate $9.877$ Mbit/s. Each symbol carries $8/3$ information bits, so
$E_b/N_0 = 12 - 10\log_{10}(8/3) = 7.74$ dB.

6. The 36-point grid has the energy sum $36 \cdot 2 \cdot 35/3 = 840$ and the corners take $200$, so
$E_s = 640/32 = 20$. Then $d_{\min}^2/E_s = 4/20 = 0.2$ and the peak is $34$, a ratio of $1.7$. The cross keeps
the peak ratio below that of 16-QAM, at half the distance per energy.

7. The in-phase value $-1.4$ lies in $(-2, 0)$, so the level is $-1$ with bits $01$; the quadrature value $2.3$
is above $2$, so the level is $3$ with bits $10$. The decision is $-1 + 3j$, label $0110$.

9. BPSK $3.87 \times 10^{-6}$, DPSK $2.27 \times 10^{-5}$, coherent BFSK $7.83 \times 10^{-4}$ and
noncoherent BFSK $3.37 \times 10^{-3}$, with $\gamma_b = 10$. Orthogonal signals lose 3 dB of distance against
antipodal ones. At $10^{-5}$, dropping the phase reference costs about $0.75$ dB in both pairs: $10.34$ against
$9.59$ dB for DPSK and BPSK, $13.35$ against $12.60$ dB for BFSK.

10. With the LLR $2y/\sigma^2 + \ln(0.8/0.2)$, the threshold is $-(\sigma^2/2)\ln 4 = -0.1733$. Then
$P_e = 0.8\,Q(1.1733/0.5) + 0.2\,Q(0.8267/0.5) = 0.01740$, against $Q(2) = 0.02275$ at the threshold $0$.

11. Only $k = 1$ and $k = 7$ matter: each gives $1.1697 \times 10^{-3}$, and the terms $k = 2, 6$ add
$1.9 \times 10^{-8}$. The union bound is $2.33947 \times 10^{-3}$ and the nearest-neighbour approximation is
$2.33945 \times 10^{-3}$, which agrees with the exact value to five digits at this SNR.

13. The interferers take four sign patterns, which give the effective amplitudes $1.5, 1.1, 0.9, 0.5$. The
eye opening is $0.5$. Averaging $Q(v/0.3)$ over the four gives $P_e = 0.01232$; without ISI it is
$Q(3.333) = 4.29 \times 10^{-4}$. The worst pattern alone causes almost all the errors.

16. Here $\bar h y = -0.1346 - 0.7469j$. The exact LLRs over the four points are $L_0 = -0.7612$ and
$L_1 = -4.2252$, equal to the closed forms, because $|y - hx|^2 = |h|^2|y/h - x|^2$ splits into a real
and an imaginary part, one for each bit. Both bits are decided as $1$, the second with much more confidence.

19. The precoded bits are $1, 0, 0, 1, 0, 1, 1$, the symbols $1, -1, -1, 1, -1, 1, 1$ and the samples
$c = 2, 0, -2, 2, 0, 0, 2$. The rule returns $1, 0, 1, 1, 0, 0, 1$, without using any earlier decision, so one
wrong sample causes one wrong bit.

20. The threshold between $0$ and $1$ is $\tfrac12 + \sigma^2\ln(P_0/P_1) = 0.5 + 0.25\ln 2 = 0.6733$, and by
symmetry $-0.6733$ on the other side. Then
$P_e = \tfrac12 \cdot 2Q(0.6733/0.5) + 2 \cdot \tfrac14 Q(0.3267/0.5) = 0.2174$, against $1.5\,Q(1) = 0.2380$
for ML.

21. Equal distances mean $2r_1^2 = 4r_2^2\sin^2(\pi/12)$, so $\gamma = 1/(\sqrt2\sin(\pi/12)) = 2.732$. Unit
energy gives $r_1^2 = 16/(4 + 12\gamma^2)$, so $r_1 = 0.4135$, $r_2 = 1.1297$, $d_{\min}^2 = 0.3420$ and the
peak $r_2^2 = 1.2763$. The closest inner and outer points share the angle $\pi/4$, at squared distance
$(r_2 - r_1)^2 = 0.513$. The value of $\gamma$ lies between the DVB-S2 ratios for the rates 4/5 ($2.75$) and 5/6 ($2.70$).

22. $d^2 = 2 - 2\,\mathrm{sinc}(\tau)$ equals 1 at $\mathrm{sinc}(\tau) = 1/2$, $\tau = 0.6034$, and
$3 - 4\,\mathrm{sinc}(\tau) + 2\,\mathrm{sinc}(2\tau) = 1$ at $\tau = 0.6809$. Both are far below $0.802$:
short events keep their distance, and the limit comes from long alternating events.

24. There are $4!/(2!\,1!\,1!) = 12$ sequences, so $k = 3$, a rate of $3/4$ bit per symbol against an entropy of
$1.5$ bits, a loss of $0.75$. Sequences that start with 1 take the indices 0 to 5, so $101 = 5$ gives
$(1, 5, 3, 1)$, and $(3, 1, 5, 1)$ has index 7. The average energy is $9$, against $35/3 = 11.67$ for a
uniform choice.
