The error rates of the previous chapter assume that the receiver knows three things it is never told: the
phase and frequency of the carrier, the instants at which to sample each pulse, and where each frame begins.
The transmitter's oscillator and clock are not the receiver's. A crystal off by 10 parts per million at
2.4 GHz leaves a frequency offset of 24 kHz, and a residual offset of only $0.01$ cycles per symbol turns the
constellation by $1.95$ radians over 32 symbols, while QPSK tolerates $\pi/4$ before a noiseless point crosses
a decision boundary. Synchronization estimates these unknowns from the received signal and follows them as
they drift.

Two structures run through the chapter. Feedback methods put an error detector into a
[phase-locked loop](/phase-locked-loop/), which tracks slow changes and has an acquisition range, a lock range
and a noise bandwidth $B_LT$. Feedforward methods estimate the parameter from a block at once, which suits
bursts. Both are measured against the [modified Cramér-Rao bound](/modified-cramer-rao-bound/): for the carrier
phase from $N$ known symbols it is $1/(2N\,E_s/N_0)$, about $2.3°$ of standard deviation for $N = 32$ at 10 dB.
The bound limits unbiased estimators only, and the entries quote their measured variances as multiples of it,
with the seed and the number of trials. Methods that remove the data with a power or with decisions have an
$M$-fold ambiguity, and below a threshold SNR they fail by jumps rather than by larger small errors: the loop
slips a cycle, or the frequency estimator picks a wrong peak.

## What the chapter covers

1. **Loops and the carrier phase.** The [phase-locked loop](/phase-locked-loop/) and
   [carrier recovery](/carrier-recovery/): the [Costas loop](/costas-loop/), the [squaring loop](/squaring-loop/),
   [decision-directed carrier recovery](/decision-directed-carrier-recovery/), the feedforward
   [Viterbi and Viterbi estimator](/viterbi-viterbi-phase-estimation/), and the [cycle slip](/cycle-slip/).
2. **Carrier frequency.** [Frequency offset estimation](/frequency-offset-estimation/) by the
   [Rife and Boorstyn](/rife-boorstyn-frequency-estimator/), [Kay](/kay-frequency-estimator/) and
   [Luise and Reggiannini](/luise-reggiannini-estimator/) estimators.
3. **Symbol timing.** [Symbol timing recovery](/symbol-timing-recovery/) with the
   [early-late gate](/early-late-gate-synchronizer/), the [Gardner detector](/gardner-timing-error-detector/),
   the [Mueller and Müller detector](/mueller-muller-timing-recovery/) and the
   [Oerder and Meyr estimator](/oerder-meyr-timing-estimation/), and the
   [Farrow interpolator](/farrow-interpolator/) that computes the strobes.
4. **Frames.** [Frame synchronization](/frame-synchronization/),
   [preamble correlation detection](/preamble-correlation-detection/) and
   [Massey's rule](/massey-frame-synchronization/).
5. **Known symbols and the limits.** [Data-aided synchronization](/data-aided-synchronization/) and the
   [modified Cramér-Rao bound](/modified-cramer-rao-bound/).

## A first reading

Read these in order:

1. [Phase-locked loop](/phase-locked-loop/)
2. [Carrier recovery](/carrier-recovery/)
3. [Costas loop](/costas-loop/)
4. [Decision-directed carrier recovery](/decision-directed-carrier-recovery/)
5. [Frequency offset estimation](/frequency-offset-estimation/)
6. [Symbol timing recovery](/symbol-timing-recovery/)
7. [Gardner timing error detector](/gardner-timing-error-detector/)
8. [Farrow interpolator](/farrow-interpolator/)
9. [Frame synchronization](/frame-synchronization/)
10. [Modified Cramér-Rao bound](/modified-cramer-rao-bound/)

They give one complete receiver: a loop for the phase, an estimate of the frequency, a timing loop with an
interpolator, and a frame detector, with the bound that measures them. On a first pass, skip the individual
frequency estimators, [cycle slips](/cycle-slip/) and Massey's rule, and come back to them when the SNR is low
or a burst is short.

## Before you start

The loops are linear systems in discrete time: from Volume 28 you need the [z-transform](/z-transform/),
[linear time-invariant systems](/linear-time-invariant-system/), [FIR filters](/fir-filter/),
[cross-correlation](/cross-correlation/), [autocorrelation](/autocorrelation/), the
[periodogram](/periodogram/) and the [matched filter](/matched-filter/). The
[discrete Fourier transform](/discrete-fourier-transform/), the [FFT](/fast-fourier-transform/) and
[Horner's rule](/horner-rule/) are in Volume 11, and [Lagrange interpolation](/lagrange-interpolation/) in
Volume 12. The estimators rest on the [Cramér-Rao bound](/cramer-rao-bound/) of Volume 33 and on
[maximum likelihood estimation](/maximum-likelihood-estimation/) in Volume 25. Read the previous chapter for
[PSK](/phase-shift-keying/), [QAM](/quadrature-amplitude-modulation/) and the
[Nyquist criterion](/nyquist-isi-criterion/), and the [AWGN channel](/additive-white-gaussian-noise-channel/)
of Volume 24.
