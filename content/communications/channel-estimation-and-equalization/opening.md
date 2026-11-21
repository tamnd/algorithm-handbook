A telephone line, a cable, a wireless link with echoes off buildings: each is a channel with memory. The
sample the receiver takes at one symbol time holds the current symbol and some energy from the last few,
$y_k = \sum_l h_l x_{k-l} + w_k$. This is [intersymbol interference](/intersymbol-interference/). On a
voiceband modem line it spans tens of symbols; on a wideband radio channel it spans hundreds. A receiver
that ignores it makes errors at any SNR. The chapter is about the two jobs that a receiver does against it.
It learns the taps $h$, which is [channel estimation](/channel-estimation/), and it undoes their effect,
which is [channel equalization](/channel-equalization/).

The methods form a ladder of cost and quality. A linear filter costs a few multiplications per symbol and
loses the most. Decision feedback removes the noise enhancement of the linear filter at the price of error
propagation. The [Viterbi equalizer](/viterbi-equalizer/) finds the maximum likelihood sequence, at a cost
of $O(NM^L)$ for $N$ symbols, an alphabet of $M$ points and $L$ taps. On the 3-tap channel B of Proakis at
20 dB, a 31-tap MMSE linear equalizer reaches an unbiased SINR of 6.60 dB, a short MMSE-DFE 15.14 dB, and
the Viterbi equalizer loses only 1.76 dB of distance against an ISI-free channel. The channel itself has to
be learned first, from pilots, from decisions or, in blind methods, from the statistics of the data alone.

## What the chapter covers

1. **The two problems.** [Channel equalization](/channel-equalization/) and
   [channel estimation](/channel-estimation/): the model, the matched filter bound and the Cramer-Rao bound
   against which every later method is measured.
2. **Estimating the channel from pilots.**
   [Least squares](/least-squares-channel-estimation/) and [LMMSE](/lmmse-channel-estimation/) estimation,
   [pilot-symbol-assisted modulation](/pilot-symbol-assisted-modulation/) on a fading channel,
   [Kalman tracking](/kalman-channel-tracking/) of the taps between pilots, and
   [sparse estimation](/sparse-channel-estimation/) for channels with few nonzero taps.
3. **Linear equalizers.** The [zero-forcing](/zero-forcing-equalizer/) and
   [MMSE](/mmse-linear-equalizer/) designs, the [fractionally spaced](/fractionally-spaced-equalizer/)
   equalizer, [frequency-domain equalization](/frequency-domain-equalization/) with a cyclic prefix, and the
   [channel-shortening equalizer](/channel-shortening-equalizer/) of DSL modems.
4. **Decision feedback.** The [decision feedback equalizer](/decision-feedback-equalizer/), the
   [canonical MMSE-DFE theorem](/mmse-dfe-canonical-theorem/), which ties its unbiased SNR to the mutual
   information of the channel, and [Tomlinson-Harashima precoding](/tomlinson-harashima-precoding/), which
   moves the feedback to the transmitter.
5. **Sequence detection.** The [whitened matched filter](/whitened-matched-filter/), the
   [Viterbi equalizer](/viterbi-equalizer/), the [Ungerboeck receiver](/ungerboeck-mlse-receiver/), and the
   cheaper [reduced-state sequence estimation](/reduced-state-sequence-estimation/) and
   [per-survivor processing](/per-survivor-processing/).
6. **Adaptive and blind equalization.** [Adaptive equalization](/adaptive-equalization/) with training and
   decisions, the [blind equalization](/blind-equalization/) problem, the
   [Sato algorithm](/sato-algorithm/) and the [constant modulus algorithm](/constant-modulus-algorithm/).
7. **Blind identification from second-order statistics.** The
   [Tong-Xu-Kailath method](/tong-xu-kailath-identification/) and the
   [subspace method](/subspace-channel-identification/), which identify an oversampled channel without
   higher-order statistics.
8. **Iterative receivers.** [Turbo equalization](/turbo-equalization/) and the
   [soft interference cancellation equalizer](/soft-interference-cancellation-equalizer/) that makes it
   cheap.

## A first reading

Read these in order:

1. [Channel equalization](/channel-equalization/)
2. [Channel estimation](/channel-estimation/)
3. [Least squares channel estimation](/least-squares-channel-estimation/)
4. [LMMSE channel estimation](/lmmse-channel-estimation/)
5. [Zero-forcing equalizer](/zero-forcing-equalizer/)
6. [MMSE linear equalizer](/mmse-linear-equalizer/)
7. [Decision feedback equalizer](/decision-feedback-equalizer/)
8. [Frequency-domain equalization](/frequency-domain-equalization/)
9. [Whitened matched filter](/whitened-matched-filter/)
10. [Viterbi equalizer](/viterbi-equalizer/)
11. [Adaptive equalization](/adaptive-equalization/)
12. [Constant modulus algorithm](/constant-modulus-algorithm/)
13. [Turbo equalization](/turbo-equalization/)

They give the two problems, one estimator of each kind, the three classes of equalizer and the step from
training to blind adaptation. On a first pass, skip the canonical theorem, the reduced-state and
per-survivor detectors, the two second-order identification methods, the channel-shortening equalizer and
the sparse estimator. Each of them builds on an entry of the first reading and can wait until it is needed.

## Before you start

The chapter assumes linear algebra, some probability and the discrete-time signal model. From this volume
you need [intersymbol interference](/intersymbol-interference/),
[pulse-amplitude modulation](/pulse-amplitude-modulation/), the
[tapped delay line channel model](/tapped-delay-line-channel-model/) and, for the frequency-domain entries,
the [cyclic prefix](/cyclic-prefix/). From Volume 28 you need the [matched filter](/matched-filter/), the
[Wiener filter](/wiener-filter/), the [LMS algorithm](/lms-algorithm/), the
[Kalman filter](/kalman-filter/) and [minimum phase](/minimum-phase/) filters. From Volume 12 you need the
[least squares problem](/least-squares-problem/), the
[Cholesky decomposition](/cholesky-decomposition/) and the
[generalized eigenvalue problem](/generalized-eigenvalue-problem/). The estimation entries use the
[Cramer-Rao bound](/cramer-rao-bound/) of Volume 33. Sequence detection rests on the
[Viterbi algorithm](/viterbi-algorithm/) of Volume 25 and on
[maximum likelihood sequence estimation](/maximum-likelihood-sequence-estimation/) of Volume 24, and the
iterative receivers on the [BCJR algorithm](/bcjr-algorithm/) and [turbo decoding](/turbo-decoding/), also
in Volume 24. The [fast Fourier transform](/fast-fourier-transform/) of Volume 11 makes frequency-domain
equalization cheap.
