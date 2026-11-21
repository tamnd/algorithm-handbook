## What to remember

- **One model, one function.** After the matched filter, $y = x + w$ with $w \sim \mathcal{CN}(0, N_0)$. Two
  points at distance $d$ are confused with probability $Q(d/\sqrt{2N_0})$, where
  $Q(x) = \tfrac12\operatorname{erfc}(x/\sqrt2) \le \tfrac12 e^{-x^2/2}$. Every exact error rate of the chapter
  holds for this model only: coherent detection, white Gaussian noise, perfect synchronization.
- **MAP is optimal.** The MAP detector minimizes the probability of symbol error; with equal priors it is
  the ML detector, and in white Gaussian noise ML is the minimum-distance rule. Unequal priors move the
  thresholds: for BPSK with priors $0.9$ and $0.1$ and $N_0 = 1$ the threshold moves to $-0.5493$, and the
  error falls from $0.0787$ to $0.0390$.
- **Exact and approximate rates.** QPSK has $P_s = 2Q(\sqrt{\gamma}) - Q(\sqrt{\gamma})^2$ with
  $\gamma = E_s/N_0$, M-PAM has $P_s = 2(1 - 1/M)\,Q\bigl(\sqrt{6\gamma/(M^2 - 1)}\bigr)$, and square QAM has
  $1 - (1 - p)^2$ with $p$ the PAM rate of one axis. With Gray labels $P_b \approx P_s/\log_2 M$; that is an
  approximation, good at high SNR, while every labeling has $P_b \ge P_s/\log_2 M$.
- **Nyquist pulses.** A pulse has no intersymbol interference at the instants $kT$ exactly when its folded
  spectrum is constant. The minimum band is $1/(2T)$; a raised cosine with roll-off $\beta$ uses
  $(1 + \beta)/(2T)$ and decays like $1/t^3$. The root raised cosine splits it between the transmitter and a
  matched receiver.
- **The limit.** At spectral efficiency $\eta$ bits/s/Hz, reliable transmission needs
  $E_b/N_0 \ge (2^\eta - 1)/\eta$, which falls to $\ln 2$, or $-1.59$ dB, as $\eta \to 0$. A linear modulation
  with code rate $r$ and roll-off $\beta$ has $\eta = r\log_2 M/(1 + \beta)$.
- **Constant envelope and no phase reference.** MSK is continuous-phase FSK with $h = 1/2$, and also offset
  QPSK with half-sine pulses; GMSK smooths it with a Gaussian filter. DPSK has $P_b = \tfrac12 e^{-E_b/N_0}$,
  $0.75$ dB worse than BPSK at $10^{-5}$, and noncoherent BFSK needs $13.35$ dB against $12.60$ dB coherent.
- **Soft bits.** The bit LLR is
  $L_k = \ln\sum_{x:\,b_k = 0} e^{-|y - hx|^2/N_0} - \ln\sum_{x:\,b_k = 1} e^{-|y - hx|^2/N_0}$. Max-log keeps
  the largest term of each sum; it is exact for BPSK and Gray QPSK and is off by at most $\ln(M/2)$ otherwise.
- **Coding and shaping gains.** Set partitioning gives TCM its gain: the 4-state 8-PSK code has
  $d_{\mathrm{free}}^2 = 4$, $3.01$ dB above uncoded QPSK. Shaping can gain at most $\pi e/6$, or $1.53$ dB; on
  8-ASK at 2 bits per symbol, a Maxwell-Boltzmann distribution needs $11.84$ dB, against $12.62$ dB uniform and
  $11.76$ dB for the Shannon limit.

| Scheme | Bits per symbol | $d_{\min}^2/E_s$ | Peak to average | $E_b/N_0$ for $P_b = 10^{-5}$ | Shannon limit at $\eta = \log_2 M$ |
|---|---|---|---|---|---|
| [BPSK](/phase-shift-keying/) | 1 | 4 | 1 | 9.59 dB | 0 dB |
| QPSK | 2 | 2 | 1 | 9.59 dB | 1.76 dB |
| 8-PSK | 3 | 0.586 | 1 | 12.97 dB | 3.68 dB |
| 16-PSK | 4 | 0.152 | 1 | 17.44 dB | 5.74 dB |
| [16-QAM](/quadrature-amplitude-modulation/) | 4 | 0.4 | 1.8 | 13.44 dB | 5.74 dB |
| 64-QAM | 6 | 0.095 | 2.33 | 17.79 dB | 10.21 dB |

: Uncoded constellations with Gray labels and coherent detection in AWGN. The required $E_b/N_0$ comes from
the high-SNR Gray formulas of the entries; the Shannon limit is $(2^\eta - 1)/\eta$ with ideal Nyquist pulses.

## Choosing a method

- **For power-limited links,** use BPSK or QPSK, which have the same $E_b/N_0$ per bit and the largest
  distance per energy; add a strong code from Volume 24 rather than more points.
- **For band-limited links,** use 16-QAM to 64-QAM or more, with a root raised cosine and the smallest
  roll-off the filters allow. QAM beats PSK of the same size by 4 dB at 16 points.
- **For nonlinear amplifiers,** use a constant-envelope scheme such as [GMSK](/gaussian-minimum-shift-keying/),
  or [APSK](/amplitude-and-phase-shift-keying/), whose rings keep the peak low.
- **Without a phase reference,** use [DPSK](/differential-phase-shift-keying/) or noncoherent
  [FSK](/frequency-shift-keying/), and accept the loss in power.
- **With a binary decoder,** compute LLRs by [max-log demapping](/max-log-demapping/) with Gray labels and use
  [BICM](/bit-interleaved-coded-modulation/), as Wi-Fi does.
- **To close the last decibel,** use [probabilistic shaping](/probabilistic-constellation-shaping/) with a
  [distribution matcher](/constant-composition-distribution-matching/).
