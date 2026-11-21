1. ◦ The five schemes of [link adaptation](/link-adaptation/) have rates $R = (0.5, 1, 2, 3, 4.5)$ and the
block error rates $\mathrm{BLER}_j(\gamma) = 1/(1 + e^{1.5(\gamma - t_j)})$, with $\gamma$ in dB and
$t = (-2, 1, 6, 10, 15)$. Give the SNR threshold of each scheme for a 10% BLER target, and the throughput
$R_j(1 - \mathrm{BLER}_j)$ of every scheme at 8 dB. Do the threshold rule and the best throughput agree?

2. ◦ With the [SNR gap](/snr-gap-approximation/) $\Gamma = 9.8$ dB, how many bits per symbol does a
subcarrier at 25 dB carry? How many with an extra 3 dB margin?

3. ◦ $K$ users see independent Rayleigh fading with the same mean SNR $\bar\gamma$. By how many dB is the
mean SNR of the best user above $\bar\gamma$ for $K = 3$ and $K = 10$? Use the result of
[multiuser diversity](/multiuser-diversity/).

4. ◦ Three users report these rates (bits per slot) for six slots.

| slot | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| user 1 | 4 | 1 | 2 | 3 | 1 | 2 |
| user 2 | 1 | 3 | 1 | 1 | 2 | 4 |
| user 3 | 2 | 2 | 1 | 4 | 3 | 1 |

Give the schedule and the total of [max-rate scheduling](/max-rate-scheduling/), and the share of each user.
Compare with round robin in the order 1, 2, 3, 1, 2, 3.

5. ◦ Apply [water-filling](/water-filling-power-allocation/) to three channels with noise levels
$\nu = (0.5, 1, 2)$ and the power $P = 2$. Give the water level, the powers and the sum rate
$\sum_i\log_2(1 + p_i/\nu_i)$, and compare with equal powers.

6. ◦ Every round of [hybrid ARQ](/hybrid-arq/) sees the SNR $\gamma = 1$, and the block has the rate
$R = 3$ bits per symbol. How many rounds does [Chase combining](/chase-combining/) need, and how many does
incremental redundancy need?

7. ◦ An [energy detector](/energy-detector/) uses a single complex sample, so its statistic is exponential
with mean 1 under noise alone. Set the threshold for $P_{fa} = 0.01$. For a Gaussian signal at SNR 10
(linear), the statistic is exponential with mean 11; give $P_d$.

8. ◦ Three sensors each have $P_d = 0.8$ and $P_{fa} = 0.05$ and decide independently. Give the detection
and false alarm probabilities of the OR rule and of the AND rule of
[spectrum sensing](/spectrum-sensing/).

9. ◦ An [outer loop](/outer-loop-link-adaptation/) targets $\beta_T = 0.1$ with $\Delta_{\mathrm{up}} = 1$ dB.
What is $\Delta_{\mathrm{down}}$? For $\beta_T = 0.01$ and $\Delta_{\mathrm{down}} = 0.01$ dB, what is
$\Delta_{\mathrm{up}}$?

10. • Three subcarriers have gains $g = (10, 4, 1.5)$ and $\Gamma = 1$, so $b$ bits on subcarrier $i$ cost
$(2^b - 1)/g_i$. Run the [Hughes-Hartogs algorithm](/hughes-hartogs-algorithm/) for $B = 6$ bits and give
the loading and its power. Compare with two bits on each subcarrier. Then find the most bits that fit in
the power $P = 3$.

11. • Start the [Levin-Campello algorithm](/levin-campello-algorithm/) at the loading $(2, 2, 2)$ for the
gains of exercise 10. Give the last and next bit costs, make the swaps until the loading is efficient, and
check that it matches exercise 10.

12. • A channel is in state $\gamma = 4$ or $\gamma = 1$ with probability $1/2$ each. Compare the rate of
full channel inversion with that of [truncated channel inversion](/truncated-channel-inversion/) that
serves only the state 4, both with unit average power.

13. • Two links have the gains $G = [[1, 0.2], [0.3, 1]]$ ($G_{ij}$ from transmitter $j$ to receiver $i$),
noise 0.1 at each receiver and the common target $\gamma = 2$. Write the
[Foschini-Miljanic](/foschini-miljanic-power-control/) iteration $p \leftarrow Fp + u$, check that the
target is feasible, give the fixed point, and find the largest common target that is feasible.

14. • Which of these are [standard interference functions](/standard-interference-function/) for one link
with $p \ge 0$: (a) $I(p) = 1 + p/2$; (b) $I(p) = 0.1 + p^2$; (c) $I(p) = \min(1 + p/2, 3)$? Find the fixed
points of each, and explain what (b) shows about the scalability axiom.

15. • Two links have direct gains 1, cross gains $G_{12} = 0.25$ and $G_{21} = 0.16$, noise 0.1 and the
total power limit $p_1 + p_2 = 1$. Find the best common SINR of
[max-min SINR power control](/max-min-sinr-power-control/) and the powers that reach it. What is the value
without noise?

16. • Maximize the [energy efficiency](/energy-efficient-power-allocation/)
$\log_2(1 + 4p)/(p + 0.5)$ (bits per second per hertz per watt) over $0 \le p \le 10$ by Dinkelbach's method
from $q_0 = 0$. Give the iterates of $p$ and $q$ until they settle, and compare with full power.

17. • Two users share two subcarriers with the gains $(4, 1)$ for user 1 and $(3, 2)$ for user 2, and the
total power is 2. For each of the four assignments, water-fill the power and give the sum rate. Which
assignment wins, and how does it relate to the rule of
[OFDMA resource allocation](/ofdma-resource-allocation/)?

18. • Compute the [EESM](/effective-snr-mapping/) effective SNR of two subcarriers with the linear SNRs 1
and 10 for $\beta = 1$ and $\beta = 10$, in dB, and compare with the mean SNR.

19. • A type I [hybrid ARQ](/hybrid-arq/) link retransmits until success on a Rayleigh channel with mean
SNR 20 dB that changes independently between attempts. An attempt at rate $R$ succeeds when
$\log_2(1 + \gamma) \ge R$. Find the integer rate with the largest throughput $R\,P(\text{success})$.

20. • An energy detector has a noise level known only to within 1.5 dB. Where is its SNR wall? Compare with
the walls for 1 and 2 dB of uncertainty in [spectrum sensing](/spectrum-sensing/).

21. • With the fit $\mathrm{BER} \approx 0.2\,e^{-1.5\gamma/(M - 1)}$ of
[adaptive modulation](/adaptive-modulation/), give the SNR in dB at which 4-QAM, 16-QAM and 64-QAM meet
$\mathrm{BER} = 10^{-4}$ at a fixed power.

22. • Run two rounds of the margin loop of the [Chow-Cioffi-Bingham algorithm](/chow-cioffi-bingham-algorithm/)
on three subcarriers with $\mathrm{SNR} = (30, 12, 3)$, $\Gamma = 1$ and $B_{\mathrm{target}} = 7$, rounding
to the nearest integer. What does the third round give, and what does that show?

23. ★ For the sum rate of OFDMA under a total power limit, prove that giving each subcarrier to the user
with the largest gain, then water-filling, is optimal.

24. ★ Two links have normalized cross gains $a = G_{12}/G_{11}$ and $b = G_{21}/G_{22}$. Show that a common
SINR target $\gamma$ is feasible for some positive noise if and only if $\gamma < 1/\sqrt{ab}$, and that the
least powers grow without bound as $\gamma$ approaches it.

25. ★ Let $X_1, \ldots, X_K$ be independent exponential variables with mean 1. Prove that
$E[\max_k X_k] = H_K = \sum_{k=1}^K 1/k$, and that $H_K - \ln K$ tends to a constant. What does this
give for the SNR gain of the best of $K$ Rayleigh users?

26. ★ Let $R(p)$ be concave and positive for $p > 0$, $P(p) = p + P_c$ with $P_c > 0$, and
$F(q) = \max_p\,(R(p) - qP(p))$ over a compact interval. Show that $F$ is strictly decreasing, that its
root is the optimal energy efficiency $q^*$, and that the Dinkelbach iterates $q_t$ increase.

27. ★ Show that the componentwise minimum and maximum of two standard interference functions are standard.
Use this to argue that a power cap $\min(I(p), \bar p)$ keeps the iteration convergent.
