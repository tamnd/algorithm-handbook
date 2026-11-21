1. ◦ A link at 5.8 GHz spans 200 m in free space. Use the decibel form of
[free-space path loss](/free-space-path-loss/) to find the loss, to two decimals.

2. ◦ A power delay profile has powers $0.6$, $0.3$ and $0.1$ at delays $0$, $2$ and $5$ microseconds.
Compute the mean delay and the RMS [delay spread](/delay-spread/) $\sigma_\tau$. What lower bound does
Fleury's theorem give for the [coherence bandwidth](/coherence-bandwidth/) $B_c(0.5)$, and what does the
rule $1/(5\sigma_\tau)$ give?

3. ◦ A train moves at 120 km/h and uses a carrier of 3.5 GHz. Find the maximum
[Doppler shift](/doppler-spread/) $f_D$. In the [Clarke model](/clarke-model/), after what delay does
$|J_0(2\pi f_D\tau)|$ first fall to $0.5$? What [coherence time](/coherence-time/) does the rule
$0.423/f_D$ give?

4. ◦ An indoor channel follows the [log-distance model](/log-distance-path-loss-model/) with
$PL(1\text{ m}) = 40$ dB and exponent $n = 3.5$. The link budget allows 120 dB of path loss. How far can
the receiver be?

5. ◦ In a [Rayleigh fading channel](/rayleigh-fading-channel/) with mean power $\Omega$, what is the
probability that the power is more than 15 dB below $\Omega$? How many dB below the mean is the median
power?

6. ◦ A Rayleigh channel has mean SNR 20 dB and the transmitter does not know the channel. Find the
[outage probability](/outage-probability/) at the rate $R = 2$ bits per channel use, and the
[outage capacity](/outage-capacity/) $C_{0.01}$ at a mean SNR of 30 dB.

7. ◦ Two branches have gains $h_1 = 2$ and $h_2 = 1 + j$ and noise power $N_0 = 1$ each. Give the output
SNR of [maximal ratio combining](/maximal-ratio-combining/), of
[selection combining](/selection-combining/) and of [equal gain combining](/equal-gain-combining/).

8. ◦ A [Gilbert-Elliott channel](/gilbert-elliott-channel/) moves from good to bad with probability
$p = 0.02$ and from bad to good with probability $r = 0.2$. The error probabilities are $e_G = 0$ and
$e_B = 0.5$. Find the stationary probability of the bad state, the mean error rate, and the mean lengths
of a bad period and of a good period.

9. ◦ [Log-normal shadowing](/log-normal-shadowing/) has $\sigma = 6$ dB. What margin over the median
path loss gives 95% coverage at the cell edge? What fraction of edge positions is in outage with a margin
of 10 dB?

10. • A two-tap channel has powers $0.8$ and $0.2$ at delays $0$ and $2$ microseconds. Find $\sigma_\tau$
and the smallest value of the frequency correlation $|R(\Delta f)|$. Show that $B_c(0.5)$ does not exist
for this channel. Then find $B_c(0.9)$ and compare it with Fleury's bound and with the rule
$1/(50\sigma_\tau)$.

11. • A car drives at 72 km/h with a carrier of 1.9 GHz, in a channel that follows the Clarke model. For
the level 6 dB below the RMS envelope, find the [level crossing rate](/level-crossing-rate/), the average
fade duration and the fraction of time spent below the level. Check that the last is the product of the
first two.

12. • A flat fading gain with unit mean power has $\mathbb{E}|h|^4 = 1.5$. Find the
[Rician](/rician-fading-channel/) factor $K$ with these two moments, and the
[Nakagami](/nakagami-m-fading-channel/) parameter $m$ with the same moments. Use the small-$x$ tails to
estimate $\Pr[|h|^2 < 0.01]$ under each model, and say what the difference means for the
[diversity order](/diversity-order/).

13. • A Rayleigh channel has mean SNR 10 dB per branch and the code rate is $R = 1$ bit per channel use.
How many independent branches does selection combining need to bring the outage probability to $10^{-3}$
or below? How many does maximal ratio combining need?

14. • A Nakagami-m channel with $m = 3$ has mean SNR $\bar\gamma$. Compute $\Pr[\gamma < 0.1\bar\gamma]$ and
$\Pr[\gamma < 0.01\bar\gamma]$ exactly. What slope on a log-log plot do the two values show?

15. • Use the Gilbert-Elliott channel of exercise 8. Compute the probability that 20 consecutive bits are
all correct, starting in the stationary distribution, and compare it with a
[binary symmetric channel](/binary-symmetric-channel/) of the same mean error rate. Then find
$\Pr[Z_{t+1} = 1 \mid Z_t = 1]$ for the error process $Z$.

16. • Use the [Okumura-Hata model](/okumura-hata-model/) at 900 MHz with a base station height of 30 m
and a mobile height of 1.5 m (small or medium city). How far does a budget of 145 dB reach in an urban
area? How far in a suburban area?

17. • A [WSSUS channel](/wssus-channel-model/) has a separable scattering function: an exponential power
delay profile with RMS delay spread $0.5$ microseconds, and the Clarke Doppler spectrum with
$f_D = 100$ Hz. Compute $|R_H(\Delta t, \Delta f)|/R_H(0, 0)$ at $\Delta t = 0.5$ ms and
$\Delta f = 200$ kHz. If the delay profile is cut at 3 microseconds, what is the spread factor
$2 f_D \tau_{\max}$?

18. • A [tapped delay line](/tapped-delay-line-channel-model/) has three equal taps at delays $0$, $T$ and
$2T$. Find $|R(\Delta f)|$, its first zero and $B_c(0.5)$ in units of $1/T$, and compare $B_c(0.5)$ with
Fleury's bound.

19. • At 2.4 GHz, how far apart must two antennas on a mobile be for their Clarke-model gains to be
uncorrelated? Now take the one-ring model of a
[geometry-based stochastic channel model](/geometry-based-stochastic-channel-model/) with ring radius
$R = 30$ m and base station distance $D = 2$ km. What spacing, broadside, makes the base station antennas
uncorrelated? Give the RMS delay spread of this ring.

20. • Take the [Saleh-Valenzuela model](/saleh-valenzuela-model/) with $\Gamma = 30$ ns, $\gamma = 10$ ns,
$1/\Lambda = 100$ ns and $1/\lambda = 2$ ns. Find the mean total energy relative to the first ray, the
share of the first cluster, the mean delay and the RMS delay spread of the mean profile.

21. • Compute the [ergodic capacity](/ergodic-capacity/) of a Rayleigh channel at a mean SNR of 5 dB with
receiver knowledge only, using $C = \log_2(e)\, e^{1/\bar\gamma} E_1(1/\bar\gamma)$, and compare it with
the AWGN channel at 5 dB. Explain the sign of the difference with
[Jensen's inequality](/jensens-inequality/).

22. ★ A sum-of-sinusoids simulator outputs
$h(t) = N^{-1/2} \sum_{n=1}^{N} e^{j(2\pi f_D t\cos\alpha_n + \phi_n)}$, with all $\alpha_n$ and $\phi_n$
independent and uniform on $[0, 2\pi)$. Prove that $\mathbb{E}[h(t + \tau) h^*(t)] = J_0(2\pi f_D\tau)$
for every $N$, and that $\mathbb{E}|h(t)|^4 = 2 - 1/N$. What is $\mathbb{E}|h|^4$ for a Rayleigh gain of unit
mean power, and what does the comparison say about the
[Jakes](/jakes-fading-simulator/) and [Zheng-Xiao](/zheng-xiao-fading-simulator/) simulators?

23. ★ Prove that the maximum of $L$ independent exponential random variables of mean $\bar\gamma$ has mean
$H_L\bar\gamma$, with $H_L = 1 + 1/2 + \dots + 1/L$. Give the array gain of selection combining for
$L = 4$ as an exact fraction and in dB.

24. ★ Prove that for Rayleigh fading with unit mean power,
$\log_2(1 + \bar\gamma) - \mathbb{E}\log_2(1 + \bar\gamma|h|^2) \to \gamma_E\log_2 e$ as $\bar\gamma \to \infty$,
where $\gamma_E = 0.5772\ldots$ is Euler's constant. Evaluate the limit in bits and in dB of SNR.

25. ★ A Rayleigh channel with mean SNR 5 dB has channel knowledge at both ends and an average power
constraint. Write the condition on the water-filling cutoff $\gamma_0$, solve it numerically, and compute
the capacity. Compare it with the ergodic capacity without transmitter knowledge from exercise 21.

26. ★ Derive the level crossing rate $N_R = \sqrt{2\pi}\, f_D\, \rho\, e^{-\rho^2}$ of the Clarke model
from Rice's formula $N_R = \int_0^\infty \dot r\, p(R, \dot r)\, d\dot r$. State the facts about $h$ and
its derivative that you use.
