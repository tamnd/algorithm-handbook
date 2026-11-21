## What to remember

- **The loop.** A second-order digital PLL with the update $s \leftarrow s + K_ie$, $\psi \leftarrow \psi + K_pe + s$
  is stable exactly when $0 < K_p < 2$, $K_i > 0$ and $2K_p + K_i < 4$. For $\zeta = 1/\sqrt2$ the design rule
  gives $K_p = \tfrac83 B_LT$ and $K_i = \tfrac{32}{9}(B_LT)^2$; the exact bandwidth is a little larger. It follows a frequency step with no error and a
  frequency ramp $\alpha$ with the error $\alpha/K_i$.
- **The bounds.** For $N$ symbols at $\mathrm{SNR} = E_s/N_0$, the modified Cramér-Rao bounds are
  $1/(2N\,\mathrm{SNR})$ rad$^2$ for the phase, $6/(\mathrm{SNR}\,N(N^2 - 1))$ rad$^2$ for the frequency and
  $1/(8\pi^2\xi N\,\mathrm{SNR})$ symbol periods squared for the timing, with
  $\xi = \tfrac1{12} + \beta^2(\tfrac14 - \tfrac{2}{\pi^2})$. They bound unbiased estimators, they are below the
  true bound when the data are unknown, and they meet it at high SNR. A loop with noise bandwidth $B_LT$ is
  compared with the bound for $N = 1/(2B_LT)$ symbols.
- **Removing the data costs noise.** The Costas loop, the squaring loop and the Viterbi and Viterbi estimator
  raise M-PSK to the power $M$. They need no decisions, but the estimate is known only modulo $2\pi/M$, and the
  variance grows by the squaring loss, $1 + N_0/2$ for BPSK and $1 + 4.5N_0 + 6N_0^2 + 1.5N_0^3$ for QPSK
  ($1.05$ and $1.51$ at 10 dB).
- **Decisions are good when they are right.** A decision-directed loop has no squaring loss with correct
  decisions, but 16-QAM keeps every noiseless decision right only for errors below $16.9°$, and from $0.7$ rad
  the loop settles at a false lock point.
- **Slips are rare until they are not.** With loop SNR $\rho$, the mean time between slips of a first-order
  loop is $\pi^2\rho I_0(\rho)^2/(2B_L) \approx \pi e^{2\rho}/(4B_L)$; an $M$-fold loop behaves as if $\rho$
  were divided by $M^2$.
- **Frequency.** The Rife and Boorstyn periodogram search is the ML estimate and reaches the bound above a
  threshold that depends on $N \cdot \mathrm{SNR}$. The Kay estimator is cheaper but reaches the bound only near
  10 dB, and the Luise and Reggiannini estimator works at low SNR on the range $|\nu| < 1/(L + 1)$.
- **Timing.** The Gardner detector needs two samples per symbol, a roll-off $\beta > 0$ and no carrier phase;
  the Mueller and Müller detector needs one sample and correct decisions, and has no self-noise at lock.
- **Frames.** For the normalized correlation of a length-$L$ word against noise, the false-alarm probability
  per position is $(1 - \lambda)^{L-1}$. Massey's rule subtracts a $\ln\cosh$ term for the data around the word.

| Method | Estimates | Uses | Form | Samples per symbol | MSE over the bound at 10 dB |
|---|---|---|---|---|---|
| [Viterbi and Viterbi](/viterbi-viterbi-phase-estimation/), $p = 2$ | phase | no data | block, $N = 32$ | 1 | 1.16 |
| [Decision-directed loop](/decision-directed-carrier-recovery/), QPSK | phase | decisions | loop | 1 | 0.97 |
| [Rife and Boorstyn](/rife-boorstyn-frequency-estimator/) | frequency | known symbols | block, $N = 32$ | 1 | 1.05 |
| [Kay](/kay-frequency-estimator/) | frequency | known symbols | block, $N = 32$ | 1 | 0.99 |
| [Luise and Reggiannini](/luise-reggiannini-estimator/), $L = 16$ | frequency | known symbols | block, $N = 32$ | 1 | 1.09 |
| [Early-late gate](/early-late-gate-synchronizer/) | timing | no data | loop | 3 | 1.95 to 2.79 |
| [Gardner](/gardner-timing-error-detector/) | timing | no data | loop | 2 | 1.36 to 2.08 |
| [Mueller and Müller](/mueller-muller-timing-recovery/) | timing | decisions | loop | 1 | 2.76 to 3.62 |
| [Oerder and Meyr](/oerder-meyr-timing-estimation/) | timing | no data | block, 100 symbols | 4 | 1.92 |

: Measured mean square errors over the bound, from the simulations of the entries (QPSK where data are sent,
loops with $B_LT = 0.01$, timing with a raised cosine of roll-off $0.5$). The seeds and trial counts are on
the entries. Values just below 1 are within the scatter of the measurement.

## Choosing a method

- **For continuous signals,** track with loops: a [Costas loop](/costas-loop/) or a
  [squaring loop](/squaring-loop/) to acquire, a decision-directed loop once the decisions are reliable, and a
  [Gardner](/gardner-timing-error-detector/) timing loop with a [Farrow interpolator](/farrow-interpolator/).
- **For bursts,** use block estimators that need no acquisition: a preamble for the frame and the frequency,
  Viterbi and Viterbi or a data-aided estimate for the phase, and Oerder and Meyr for the timing.
- **At low SNR,** use known symbols ([data-aided synchronization](/data-aided-synchronization/)), the
  Rife and Boorstyn search for the frequency, and [Massey's rule](/massey-frame-synchronization/) for the frame.
- **Always** resolve the $2\pi/M$ ambiguity with a unique word or differential encoding, and check the slip
  rate, not only the variance, near the threshold.
