## What to remember

- **Least squares is unbiased and efficient.** With pilot matrix $X$, $\hat h = (X^HX)^{-1}X^Hy$ has error
  $N_0\,\mathrm{tr}((X^HX)^{-1})$, which attains the Cramer-Rao bound. For pilot energy
  $T = \mathrm{tr}(X^HX)$ the error is at least $L^2N_0/T$, with equality if and only if $X^HX = (T/L)I$.
- **LMMSE trades bias for error.** With a prior covariance $R_h$, the error covariance is
  $(R_h^{-1} + X^HX/N_0)^{-1}$, never larger than the LS error $N_0(X^HX)^{-1}$.
- **Zero forcing enhances noise; MMSE does not blow up.** The infinite-length ZF output noise is
  $N_0\frac{1}{2\pi}\int |H|^{-2}\,d\omega$, infinite at a spectral null. The MMSE error
  $\frac{1}{2\pi}\int E_sN_0/(E_s|H|^2 + N_0)\,d\omega$ is always finite. The MMSE output is biased: its
  cursor is $1 - J/E_s$ and its unbiased SINR is $E_s/J - 1$.
- **Decision feedback replaces the arithmetic mean by the geometric mean.** With correct decisions the
  infinite-length MMSE-DFE has $J = N_0/G$, where $G$ is the geometric mean of $|H|^2 + N_0/E_s$. The
  canonical theorem gives $\log_2(1 + \mathrm{SNR}_U) = \frac{1}{2\pi}\int\log_2(1 + Q)\,d\omega$ for a
  Gaussian input. Wrong decisions propagate; Tomlinson-Harashima precoding avoids this at a power loss of
  $M^2/(M^2 - 1)$, 0.280 dB for 4-PAM.
- **The Viterbi equalizer is maximum likelihood sequence detection.** It needs $M^{L-1}$ states and
  $O(NM^L)$ time. The whitened matched filter and the Ungerboeck metric give the same decisions.
  Reduced-state sequence estimation spans the range from the DFE to the full trellis.
- **A cyclic prefix of at least $L - 1$ samples makes the channel circular.** Then one complex tap per
  frequency equalizes the block, in $O(N\log N)$ time with the FFT.
- **Blind methods rest on structure, not on pilots.** Symbol-rate second-order statistics fix only $|H|$,
  Oversampled second-order statistics fix the channel up
  to a scalar if the subchannels share no zero. CMA and Sato use the non-Gaussian alphabet and have
  no global convergence theorem for finite equalizers.
- **Iterative receivers are heuristics with good measurements.** Turbo equalization has no convergence
  theorem. The soft interference cancellation equalizer is linear MMSE with priors, not MAP.

| Method | Criterion | Cost per block | Needs | Weak point |
|---|---|---|---|---|
| [LS estimation](/least-squares-channel-estimation/) | least squares, unbiased | $O(mL^2)$ | pilots | noisy at low SNR |
| [LMMSE estimation](/lmmse-channel-estimation/) | mean squared error | $O(mL^2 + L^3)$ | pilots, $R_h$, $N_0$ | biased, needs statistics |
| [Kalman tracking](/kalman-channel-tracking/) | MMSE for a Gauss-Markov model | $O(KL^2)$ | Doppler, $N_0$ | model mismatch |
| [ZF equalizer](/zero-forcing-equalizer/) | no ISI in the window | $O(N^3 + KN)$ | channel | noise enhancement at nulls |
| [MMSE linear equalizer](/mmse-linear-equalizer/) | mean squared error | $O(N^2(N + L) + KN)$ | channel, $N_0$ | biased, loses on deep nulls |
| [SC-FDE](/frequency-domain-equalization/) | ZF or MMSE per frequency | $O(N\log N)$ | cyclic prefix | prefix overhead |
| [DFE](/decision-feedback-equalizer/) | mean squared error | $O(N^2(N + L) + K(N + L))$ | channel, $N_0$ | error propagation |
| [THP](/tomlinson-harashima-precoding/) | DFE at the transmitter | $O(KL)$ | channel at the transmitter | power and shaping loss |
| [Viterbi equalizer](/viterbi-equalizer/) | ML sequence | $O(NM^L)$ | channel | exponential in $L$ |
| [RSSE](/reduced-state-sequence-estimation/) | ML on a reduced trellis | $O(NS(M + L))$ | minimum-phase channel | not ML in general |
| [CMA](/constant-modulus-algorithm/) | constant modulus cost | $O(KN)$ | nothing but the alphabet | false minima, phase ambiguity |
| [SIC equalizer](/soft-interference-cancellation-equalizer/) | linear MMSE with priors | $O(KW^3)$ | channel, $N_0$, priors | Gaussian LLR model |
| [Turbo equalization](/turbo-equalization/) | iterated BCJR | $O(IN2^L)$ | channel, $N_0$, a code | no convergence theorem |

: The main methods of the chapter. $N$ is the number of equalizer taps, the block length for SC-FDE and
the number of symbols for the trellis methods; $K$ is the number of symbols; the other letters are as in
the entries.

## Choosing a method

Start with LS on orthogonal pilots: it needs nothing else, and at high SNR LMMSE is only slightly better.
Use LMMSE when the power delay profile and the noise level are known, and Kalman tracking or
[pilot-symbol-assisted modulation](/pilot-symbol-assisted-modulation/) when the channel fades between
pilots. For equalization, an MMSE design is almost always better than its zero-forcing twin, and an
MMSE-DFE better than a linear equalizer, unless error propagation dominates; then precode if the
transmitter knows the channel. Use the Viterbi equalizer when $M^{L-1}$ states are affordable, and RSSE or
DDFSE after a whitened matched filter when they are not. For long channels with block transmission, add a
cyclic prefix and equalize in the frequency domain. Use CMA only when training costs too much, and switch
to decision-directed adaptation once the eye is open. With a strong code, iterate with the decoder.
