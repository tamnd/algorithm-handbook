A phone at 2.4 GHz, one kilometre from a base station in free space, receives a signal 100 dB weaker than
the one sent. That loss is smooth and predictable. On top of it the signal comes in along many paths, off
walls, cars and the ground, and the copies add with phases that change every few centimetres. A receiver
that moves a fraction of a wavelength can pass through a deep fade and out again. With many paths and no
dominant one, the power is more than 10 dB below its mean about 9.5% of the time, and binary phase-shift
keying at a mean SNR of 10 dB has a bit error rate of 0.0233 instead of the $3.87 \cdot 10^{-6}$ of a
channel without fading. To get $10^{-5}$ it needs 44 dB instead of 10 dB.

Fading channels are the models of this behavior and the measures that follow from them. Path loss and
shadowing set the mean power and fix the size of a cell. The spread of path delays decides whether the
channel is flat over a band or selective, and the spread of Doppler shifts decides how long a channel
estimate stays valid. The distribution of the gain gives error rates and two capacities, ergodic and
outage. Diversity, which means several copies that fade independently, is the main defence. Every later
chapter of the volume uses these models: OFDM is designed around the delay spread, pilots around the
coherence time, and space-time codes around diversity.

## What the chapter covers

1. **Path loss and shadowing.** [Free-space path loss](/free-space-path-loss/), the
   [log-distance model](/log-distance-path-loss-model/) with its fitted exponent,
   [log-normal shadowing](/log-normal-shadowing/) and the empirical
   [Okumura-Hata model](/okumura-hata-model/) for urban cells.
2. **Multipath, delay and Doppler.** [Multipath fading](/multipath-fading/), the
   [delay spread](/delay-spread/) and the [coherence bandwidth](/coherence-bandwidth/), the
   [Doppler spread](/doppler-spread/) and the [coherence time](/coherence-time/). The rules of thumb that
   link a spread to a coherence value are not exact, and Fleury's bound says how far they can be off.
3. **Distributions of a flat fading gain.** The [Rayleigh](/rayleigh-fading-channel/),
   [Rician](/rician-fading-channel/) and [Nakagami-m](/nakagami-m-fading-channel/) models, with their
   fade probabilities and error rates.
4. **Capacity and outage.** The [ergodic capacity](/ergodic-capacity/) for codewords that span many
   fades, and the [outage probability](/outage-probability/) and
   [outage capacity](/outage-capacity/) for a codeword inside one fade.
5. **Diversity and combining.** The [diversity order](/diversity-order/) and the three classical
   combiners: [maximal ratio](/maximal-ratio-combining/), [selection](/selection-combining/) and
   [equal gain](/equal-gain-combining/).
6. **Fading in time and its simulators.** The [Clarke model](/clarke-model/), the
   [level crossing rate](/level-crossing-rate/) and average fade duration, and three ways to simulate
   fading: [filtered Gaussian noise](/filtered-gaussian-fading-simulator/),
   [Jakes' simulator](/jakes-fading-simulator/) and the
   [Zheng-Xiao simulator](/zheng-xiao-fading-simulator/).
7. **Wideband, geometric and burst models.** The
   [tapped delay line](/tapped-delay-line-channel-model/), the [WSSUS model](/wssus-channel-model/), the
   [Saleh-Valenzuela model](/saleh-valenzuela-model/) of indoor clusters,
   [geometry-based stochastic models](/geometry-based-stochastic-channel-model/) and the
   [Gilbert-Elliott channel](/gilbert-elliott-channel/) of error bursts.

## A first reading

Read these first, in this order:

1. [Free-space path loss](/free-space-path-loss/)
2. [Multipath fading](/multipath-fading/)
3. [Delay spread](/delay-spread/)
4. [Coherence bandwidth](/coherence-bandwidth/)
5. [Doppler spread](/doppler-spread/)
6. [Coherence time](/coherence-time/)
7. [Rayleigh fading channel](/rayleigh-fading-channel/)
8. [Outage probability](/outage-probability/)
9. [Ergodic capacity](/ergodic-capacity/)
10. [Diversity order](/diversity-order/)
11. [Maximal ratio combining](/maximal-ratio-combining/)
12. [Clarke model](/clarke-model/)
13. [Tapped delay line channel model](/tapped-delay-line-channel-model/)

The empirical path loss models, the simulators and the last group can wait until you need them. Keep two
habits from the start. When you quote a capacity, say whether it is ergodic or outage, and say what the
receiver and the transmitter know about the channel. When you quote a closed form, remember that it holds
for the stated model only; a measured channel needs measured numbers.

## Before you start

The chapter uses probability throughout: the [expected value](/expected-value/),
[Jensen's inequality](/jensens-inequality/), the
[moment generating function](/moment-generating-function/) and the
[central limit theorem](/central-limit-theorem/) of Volume 1. The noise model and the limits it sets are
the [additive white Gaussian noise channel](/additive-white-gaussian-noise-channel/) and
[channel capacity](/channel-capacity/) of Volume 24. From the first chapter of this volume you need the
[Gaussian Q-function](/gaussian-q-function/) and the [bit error rate](/bit-error-rate/). Time correlation
and spectra use [autocorrelation](/autocorrelation/), the
[power spectral density](/power-spectral-density/) and the
[sampling theorem](/sampling-theorem/) of Volume 28. The Gilbert-Elliott channel is a
[Markov chain](/markov-chain/) with a [stationary distribution](/stationary-distribution/) (Volume 17), and
fitting a path loss exponent is a [least squares problem](/least-squares-problem/) (Volume 12).
