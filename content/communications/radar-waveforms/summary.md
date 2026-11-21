## What to remember

- **The range equation is a model.** The echo's signal to noise ratio is
  $P_t G^2 \lambda^2 \sigma / ((4\pi)^3 R^4 k T_0 B F L)$. It holds under its assumptions (one antenna, free space, a
  point target in the far field, all losses in $L$); multipath and clutter change it. Twice the range costs
  12.04 dB.
- **The matched filter fixes the detection, the waveform fixes the resolution.** In white noise the peak
  output signal to noise ratio depends only on the energy of the pulse. Pulse compression gives the range
  resolution $c/(2B)$ with a pulse of any length $T$, compressed by the factor $TB$.
- **The ambiguity volume is fixed.** $|\chi(\tau, \nu)| \le E = |\chi(0, 0)|$, and
  $\iint |\chi|^2 = E^2$ for every waveform. A waveform moves the volume around; it cannot remove it.
- **Each waveform has its sidelobes.** A linear chirp has range sidelobes near $-13.5$ dB and a peak that
  moves by $\nu T/B$ in delay for a Doppler shift $\nu$. A window lowers the sidelobes at a loss of 1 to 2 dB;
  nonlinear FM lowers them with no loss but only near zero Doppler. Barker codes reach sidelobes of
  magnitude 1, and no Barker code of odd length above 13 exists.
- **Fluctuation costs signal to noise ratio.** For one pulse at $P_{fa} = 10^{-6}$ and $P_d = 0.9$, a steady
  target needs 13.18 dB and a Swerling 1 target 21.14 dB.
- **CFAR keeps its false alarm rate only under its noise model.** Cell-averaging CFAR gives
  $P_{fa} = (1 + \tau)^{-N}$ exactly in homogeneous exponential noise. Other targets in the window raise
  its threshold and can mask a target; clutter that is not exponential changes the rate.
  Ordered-statistic CFAR tolerates $N - k$ interferers at about 1 dB more loss.
- **Doppler separates moving targets from still clutter.** MTI cancellers have blind speeds at multiples
  of $\lambda\,\mathrm{PRF}/2$. A range-Doppler map has a velocity bin of $\lambda\,\mathrm{PRF}/(2P)$ and a
  straddle loss of up to 3.92 dB without a window. On a moving radar, STAP uses the weight $R^{-1}v$, the
  largest output SINR of any linear filter for the true covariance $R$.

| Waveform | Range resolution | Peak sidelobe at zero Doppler | Loss | Doppler behaviour |
|---|---|---|---|---|
| [Linear FM](/linear-frequency-modulation-pulse/), $TB = 50$ | $c/(2B)$ | $-13.52$ dB; $-42.7$ dB with Hamming | 0 dB; 1.34 dB with Hamming | tolerant, peak shifted by $\nu T/B$ |
| [Nonlinear FM](/nonlinear-frequency-modulation/), Hamming, $TB = 50$ | wider than $c/(2B)$, as with a window | $-27.33$ dB | 0 dB | sidelobes about $-15.7$ dB at $\nu T = 1$ |
| [Barker 13](/barker-code/) | $c\tau_c/2$ | $-22.28$ dB | 0 dB | sidelobe $-10.63$ dB at $\nu T = 0.25$ |
| Barker 13, [mismatched filter](/mismatched-filter-design/) of 39 taps | $c\tau_c/2$ | $-38.47$ dB | 0.204 dB | designed at zero Doppler |
| [Frank code](/frank-code/), 16 chips | $c\tau_c/2$ | $-21.07$ dB | 0 dB | peak 0.85, moved one chip, at $\nu T = 1$ |
| [Stepped frequency](/stepped-frequency-waveform/), $N$ steps of $\Delta f$ | $c/(2N\Delta f)$ | that of the DFT window | 0 dB | range shift $f_0 v T_r/\Delta f$ |
| [FMCW](/fmcw-radar/), sweep $B$ in $T_c$ | $c/(2B)$ | that of the beat window | 0 dB | range offset from the Doppler beat |

: The waveforms of the chapter, with the values computed in their entries; $\tau_c$ is the chip length and
$T$ the pulse length.

## Choosing a method

- **For a long range search radar with a saturated transmitter,** use a linear chirp with a receive window,
  or nonlinear FM if the 1 to 2 dB of the window is too costly and the Doppler shifts are small.
- **For a digital waveform of moderate length,** use a [phase code](/phase-coded-waveform/): Barker 13,
  a Frank or other polyphase code for more chips, and a mismatched filter when a strong echo can hide a
  weak one.
- **For fine resolution with narrow band hardware,** use a stepped frequency waveform; for short range at
  low cost, as in cars, use [FMCW](/fmcw-radar/).
- **To set the threshold,** use [cell-averaging CFAR](/cell-averaging-cfar/) in thermal noise with sparse
  targets, and [ordered-statistic CFAR](/ordered-statistic-cfar/) when targets come in groups.
- **To see moving targets from a fixed radar,** use [MTI](/moving-target-indication/) and
  [range-Doppler processing](/range-doppler-processing/); from an aircraft, use
  [STAP](/space-time-adaptive-processing/) with at least twice as many training cells as degrees of freedom,
  or diagonal loading.
