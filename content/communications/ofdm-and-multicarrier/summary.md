## What to remember

- A cyclic prefix of $N_{cp} \ge L-1$ samples makes a channel of $L$ taps act as a circular convolution, so
  after the FFT $Y[k] = H[k]X[k] + W[k]$ on every subcarrier. OFDM costs $O(N\log N)$ per symbol and keeps
  the rate fraction $N/(N+N_{cp})$, 0.8 for 802.11a.
- Comb pilots with spacing $D \le N/L$ sample $H[k]$ often enough to recover it. The DFT-based estimator
  keeps only the first $L_t$ taps of the least squares impulse response, and its error is $L_t N_0/N$ against
  $N_0$ for least squares alone. Wiener interpolation is the best linear estimate but needs the channel
  statistics.
- A frequency offset of $\varepsilon$ subcarrier spacings scales each subcarrier by $S(\varepsilon)$ and
  leaks the rest of its power into the others: $1-|S(\varepsilon)|^2 \approx (\pi\varepsilon)^2/3$. An
  integer offset only moves the data to other subcarriers.
- The frequency offset estimators trade range against variance: a longer repeated part gives a smaller
  variance and a shorter range. The van de Beek estimator needs no training but has only the prefix.
- The PAPR of $N$ subcarriers is at most $N$. Measured with oversampling $L = 4$, its tail is close to the rule
  $\Pr(\text{PAPR} > \gamma) \approx 1-(1-e^{-\gamma})^N$, which is exact only for independent complex
  Gaussian samples. In one measurement on $N = 64$ QPSK, $L = 1$ understates the 1 percent point by 0.55 dB.
- Every PAPR reduction method pays for its gain: clipping with in-band distortion and regrowth, selected
  mapping and partial transmit sequences with inverse FFTs and side information, tone reservation with data
  tones, active constellation extension with transmit power. SC-FDMA avoids most of the problem with a DFT spread.
- Shaped waveforms give up something OFDM has: FBMC/OQAM keeps only real orthogonality and drops the prefix,
  GFDM is not orthogonal, and UFMC drops the prefix and needs a $2N$-point FFT at the receiver.
- In a doubly dispersive channel, OTFS and AFDM spread each symbol over the whole time-frequency block, so a
  channel of a few paths acts as a few separable shifts on the delay-Doppler grid or on the chirp grid.

| Method | Distortion | Side information | Receiver change | Other cost | Time |
|---|---|---|---|---|---|
| Clipping and filtering | in-band noise | none | none | PAPR target not guaranteed | $O(KLN\log(LN))$ |
| Selected mapping | none | $\log_2 U$ bits | undo the phase sequence | $U$ inverse FFTs | $O(ULN\log(LN))$ |
| Partial transmit sequences | none | $(V-1)\log_2 W$ bits | undo the phase factors | $W^{V-1}$ candidates | $O(VLN\log(LN) + W^{V-1}VLN)$ |
| Tone reservation | none | none | ignore reserved tones | $\lvert R\rvert$ tones and their power | $O(LN\log(LN) + KLN)$ |
| Active constellation extension | none at the decision | none | none | about 0.1 to 0.7 dB more power | $O(KLN\log(LN))$ |

: The PAPR reduction methods of the chapter, for $N$ subcarriers oversampled $L$ times and $K$ iterations.

| Estimator | Training | Range of $\varepsilon$ | Variance at high SNR |
|---|---|---|---|
| Schmidl-Cox | one symbol with two equal halves, a second for the integer part | $\lvert\varepsilon\rvert < 1$ from the first symbol | $1/(\pi^2 (N/2)\,\mathrm{SNR})$ |
| Moose | two repeated symbols | $\lvert\varepsilon\rvert < N/(2(N+G))$ | $1/(4\pi^2 N\,\mathrm{SNR})$ for $G = 0$ |
| van de Beek | none, uses the cyclic prefix | $\lvert\varepsilon\rvert < 1/2$ | $1/(4\pi^2 N_{cp}\,\mathrm{SNR})$ |

: The three frequency offset estimators of the chapter. Each variance has a further factor
$1 + 1/(2\,\mathrm{SNR})$.

## Choosing a method

Pick the subcarrier spacing first. The prefix must cover the delay spread and its share sets the rate loss,
so long delay spreads push toward narrow subcarriers. Doppler spread and oscillator offset push the other
way, through inter-carrier interference.

For the channel estimate, least squares on comb pilots with linear interpolation is the cheap baseline. Add
the DFT-based projection when the delay spread is short compared with the symbol, and use Wiener
interpolation when you can estimate the correlation.

For synchronization, a preamble with repeated halves (Schmidl-Cox) gives timing and a wide frequency range in
one step, and Moose on two full symbols refines the estimate. Use the van de Beek estimator when no training
is available; it is maximum likelihood only for the Gaussian model without dispersion.

For peak power, clipping and filtering is the simplest and needs nothing from the receiver. When distortion
is not allowed, selected mapping is the easiest choice. Tone reservation fits systems that leave tones unused,
and active constellation extension fits QPSK and small QAM, where most points lie on the outside. For the
uplink, where the handset amplifier is the weak point, SC-FDMA is the usual answer.
