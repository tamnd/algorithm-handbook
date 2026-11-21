## What to remember

- Free-space loss grows by 20 dB per decade of distance; the log-distance model grows by $10n$ dB per
  decade with a fitted exponent $n$, often 2 to 4. Log-normal shadowing adds a Gaussian term in dB with
  $\sigma$ of 4 to 13 dB, so covering a fraction $1 - \epsilon$ of positions at the cell edge needs a
  margin of $Q^{-1}(\epsilon)\,\sigma$ dB.
- The delay spread $\sigma_\tau$ and the coherence bandwidth are linked by Fleury's bound
  $B_c(c) \ge \arccos(c)/(2\pi\sigma_\tau)$, tight for two equal taps. At $c = 0.5$ it gives $1/(6\sigma_\tau)$,
  so the rule $1/(5\sigma_\tau)$ can overstate the coherence bandwidth.
- Clarke's model gives the time correlation $J_0(2\pi f_D\tau)$ with $f_D = v f_c/c$. It falls to 0.5 at
  $\tau = 0.2421/f_D$ and first reaches zero at $0.3827/f_D$. The two textbook rules for coherence time,
  $0.179/f_D$ and $0.423/f_D$, differ by a factor of 2.36.
- In Rayleigh fading $\Pr[|h|^2 < x\Omega] = 1 - e^{-x} \approx x$ for small $x$, and the BPSK error rate
  falls only as $1/(4\bar\gamma)$: diversity order 1. Rician fading also has order 1; Nakagami-m has
  order $m$.
- Ergodic capacity $\mathbb{E}\log_2(1 + \bar\gamma|h|^2)$ needs codewords that span many independent fades and
  channel knowledge at the receiver. By Jensen's inequality it is below the AWGN value
  $\log_2(1 + \bar\gamma)$, by 0.83 bit at high SNR in Rayleigh. Water-filling in time, with channel
  knowledge at the transmitter, raises it.
- For a codeword inside one fade and no transmitter knowledge, $P_{\text{out}}(R) = F_\gamma(2^R - 1)$ and the
  Rayleigh outage capacity is $C_\epsilon = \log_2(1 - \bar\gamma\ln(1 - \epsilon))$, a rate with a failure
  probability.
- $L$ independent branches give diversity order $L$ with any of the three combiners. Maximal ratio combining
  adds the branch SNRs, the most any linear combiner can get; the mean SNR gains are $L$ for MRC,
  $1 + (L-1)\pi/4$ for EGC and $H_L = 1 + 1/2 + \dots + 1/L$ for SC.
- In Clarke's model the envelope crosses the level $\rho$ times its RMS value
  $N_R = \sqrt{2\pi}\, f_D\, \rho\, e^{-\rho^2}$ times per second, and a fade below it lasts
  $(e^{\rho^2} - 1)/(\rho f_D\sqrt{2\pi})$ on average.
- The WSSUS model gives every second-order statistic from one scattering function $S(\tau, \nu)$, over a
  local area only. The tapped delay line is its form with finitely many delays.

| Channel and receiver | Diversity order | $P_{\text{out}}$, $R = 1$ | BPSK, 10 dB | BPSK, 20 dB |
|---|---|---|---|---|
| Rayleigh, one branch | 1 | 0.0952 | 0.0233 | $2.48 \cdot 10^{-3}$ |
| Rician, $K = 10$ | 1 | $7.39 \cdot 10^{-4}$ | $7.01 \cdot 10^{-4}$ | $2.51 \cdot 10^{-6}$ |
| Nakagami, $m = 2$ | 2 | 0.0175 | $5.53 \cdot 10^{-3}$ | $7.26 \cdot 10^{-5}$ |
| Rayleigh, SC, $L = 2$ | 2 | $9.06 \cdot 10^{-3}$ | $2.97 \cdot 10^{-3}$ | $3.66 \cdot 10^{-5}$ |
| Rayleigh, EGC, $L = 2$ | 2 | | $2.07 \cdot 10^{-3}$ | $2.45 \cdot 10^{-5}$ |
| Rayleigh, MRC, $L = 2$ | 2 | $4.68 \cdot 10^{-3}$ | $1.60 \cdot 10^{-3}$ | $1.84 \cdot 10^{-5}$ |

: Flat fading, mean SNR per branch 10 dB for the outage column ($\Pr[\gamma < 1]$) and 10 or 20 dB for
coherent BPSK with perfect receiver channel knowledge. Values are exact for these models, from the entries;
the EGC entry gives no outage value.

## Choosing a model and a measure

Start from the time scales. A band much narrower than the coherence bandwidth sees one flat gain; a wider
band needs a tapped delay line. A codeword that spans many coherence times sees the ergodic capacity, and
one inside a single coherence time sees outage. Then say who knows the channel: receiver knowledge is the
usual assumption, and transmitter knowledge allows water-filling or a rate that follows the channel.

For the gain distribution, Rayleigh is the default when no path dominates, Rician when a line-of-sight path
exists, and Nakagami-m to fit measured fade depths with one parameter. The Rician row of the table is
not more diversity: its curve has slope 1, and a diversity-2 curve overtakes it at high enough SNR. For
combining, MRC is best when every branch has a channel estimate; SC needs
only an SNR per branch and one receive chain; EGC needs phases but not amplitudes and loses about 0.6 dB
to MRC at 20 dB with two branches.

For simulation, the filtered Gaussian simulator gives exactly Gaussian samples with a correlation close to
$J_0$, Jakes' simulator is deterministic and not wide-sense stationary, and the Zheng-Xiao simulator has
the right second-order statistics over its random ensemble. Path loss formulas such as Okumura-Hata
hold only within their fitted ranges of frequency, distance and antenna height.
