A phone in a moving car receives a video stream. A base station sends the data on
hundreds of subcarriers at once, each carrying a point of a QAM constellation. Copies of the signal bounce off buildings and
arrive microseconds apart, and the car's speed makes their sum fade dozens of times a second. The phone must find each frame, correct an oscillator a few parts per million
off, estimate the channel from pilot symbols, undo it, and decide which points were sent. The base
station picks a constellation and a code rate for each user and shares its power and subcarriers among
them.

This volume collects the algorithms that send data over a physical channel and recover it: modulation,
synchronization, fading, equalization, OFDM, MIMO, multiple access, resource allocation and radar.
It has nine chapters and 259 entries.

## Why communications gets a volume of its own

A few ideas run through the whole volume:

- **Detection is a decision under noise.** The [MAP rule](/symbol-detection/) minimizes the probability of
  error, and with equal priors it is the maximum likelihood rule; in white Gaussian noise that is the
  [minimum distance detector](/minimum-distance-detector/). Error rates are written with the
  [Gaussian Q-function](/gaussian-q-function/), and each closed form is exact only for its stated model:
  the usual [bit error rate](/bit-error-rate/) formulas for Gray-labelled QAM and PSK are high-SNR
  approximations, and union and Chernoff bounds are bounds.
- **Capacity is a limit, not a design.** By the [Shannon-Hartley theorem](/shannon-hartley-theorem/) a band
  of width $B$ carries at most $B \log_2(1 + S/N)$ bits per second, that is $\tfrac12 \log_2(1 + \mathrm{SNR})$
  per real dimension, and every rate below it is achievable. A fading channel has two measures that must be
  kept apart, the [ergodic capacity](/ergodic-capacity/) for codewords that span many fades and the
  [outage capacity](/outage-capacity/) for one fade per codeword. The
  [SNR gap approximation](/snr-gap-approximation/) for practical codes is a design rule.
- **The channel must be learned and undone.** [Channel estimation](/channel-estimation/) uses pilots,
  equalizers remove the intersymbol interference, and the choice is between cost and optimality. The
  [zero-forcing](/zero-forcing-equalizer/) and [MMSE](/mmse-linear-equalizer/) equalizers are linear and
  suboptimal; the [Viterbi equalizer](/viterbi-equalizer/) finds the maximum likelihood sequence.
- **A cyclic prefix makes the channel circular.** A [prefix](/cyclic-prefix/) at least as long as the
  channel memory turns linear convolution into circular convolution, so
  [OFDM](/orthogonal-frequency-division-multiplexing/) needs one complex tap per subcarrier. The price is a
  high peak-to-average power ratio and a sensitivity to frequency offset, which causes
  [inter-carrier interference](/inter-carrier-interference/).
- **Antennas multiply the rate.** In Rayleigh fading with the channel known at the receiver, the
  [MIMO capacity](/mimo-capacity/) grows like $\min(N_t, N_r) \log_2 \mathrm{SNR}$ at high SNR. Maximum
  likelihood [MIMO detection](/mimo-detection/) is NP-hard in general, so receivers use linear detectors,
  which are suboptimal, or tree searches whose cost depends on the SNR.
- **Sharing the medium is a resource problem.** Some allocation problems have exact solutions, such as [water-filling](/water-filling-power-allocation/) over
  parallel Gaussian channels; many others are NP-hard, such as
  [weighted sum rate maximization](/weighted-sum-rate-maximization/), and their heuristics are measured.
- **Simulated rates are measurements.** A simulated error rate holds for its model, seed and number of
  trials, and the entries state them.

## The chapters

**Chapter 44.1, Modulation and detection** (39 entries), maps bits to waveforms. It starts from
[digital modulation](/digital-modulation/), the [signal space](/signal-space-representation/) and the
[constellations](/signal-constellation/) of [PSK](/phase-shift-keying/) and
[QAM](/quadrature-amplitude-modulation/), then covers [symbol detection](/symbol-detection/), error rates
and [Gray labelling](/gray-labeling/), [pulse shaping](/pulse-shaping/) under the
[Nyquist criterion](/nyquist-isi-criterion/) with [raised-cosine](/raised-cosine-filter/) filters, constant
envelope schemes such as [MSK](/minimum-shift-keying/), [noncoherent detection](/noncoherent-detection/),
[soft demapping](/soft-demapping/), coded modulation by [TCM](/trellis-coded-modulation/) and
[BICM](/bit-interleaved-coded-modulation/), [probabilistic shaping](/probabilistic-constellation-shaping/)
and [faster-than-Nyquist signaling](/faster-than-nyquist-signaling/).

**Chapter 44.2, Synchronization** (22 entries), aligns the receiver with the transmitter in phase,
frequency, symbol timing and frame. It covers the [phase-locked loop](/phase-locked-loop/) and the
[Costas loop](/costas-loop/), with their acquisition and lock ranges and [cycle slips](/cycle-slip/);
timing recovery by the [Gardner detector](/gardner-timing-error-detector/), the
[Mueller and Muller detector](/mueller-muller-timing-recovery/) and the
[Farrow interpolator](/farrow-interpolator/); [frame synchronization](/frame-synchronization/); and
frequency estimators such as [Kay's](/kay-frequency-estimator/), which reaches the Cramér-Rao bound only
above a threshold SNR. The [modified Cramér-Rao bound](/modified-cramer-rao-bound/) is looser but easy
to compute.

**Chapter 44.3, Fading channels** (29 entries), models the radio channel: [path loss](/free-space-path-loss/)
and [shadowing](/log-normal-shadowing/), [multipath fading](/multipath-fading/) with its
[delay spread](/delay-spread/), [Doppler spread](/doppler-spread/) and coherence times, the
[Rayleigh](/rayleigh-fading-channel/), [Rician](/rician-fading-channel/) and
[Nakagami](/nakagami-m-fading-channel/) channels, the [Clarke model](/clarke-model/) and its simulators,
and the [WSSUS model](/wssus-channel-model/). It defines the [diversity order](/diversity-order/) and covers
[maximal ratio combining](/maximal-ratio-combining/), [selection combining](/selection-combining/) and the
[outage probability](/outage-probability/).

**Chapter 44.4, Channel estimation and equalization** (28 entries), covers
[least squares](/least-squares-channel-estimation/) and [LMMSE](/lmmse-channel-estimation/) estimation from
pilots, linear equalizers, the [decision feedback equalizer](/decision-feedback-equalizer/), whose wrong
decisions propagate, [blind equalization](/blind-equalization/) with the
[constant modulus algorithm](/constant-modulus-algorithm/), [frequency-domain equalization](/frequency-domain-equalization/),
[Tomlinson-Harashima precoding](/tomlinson-harashima-precoding/), sequence detection by the Viterbi
equalizer, and [turbo equalization](/turbo-equalization/), which works well in practice without a general
convergence theorem. By the [canonical MMSE-DFE theorem](/mmse-dfe-canonical-theorem/), the unbiased
MMSE-DFE reaches capacity under ideal assumptions.

**Chapter 44.5, OFDM and multicarrier** (25 entries), builds on the [cyclic prefix](/cyclic-prefix/). It
covers [OFDM](/orthogonal-frequency-division-multiplexing/), [discrete multitone](/discrete-multitone/) and
[SC-FDMA](/sc-fdma/); the [peak-to-average power ratio](/peak-to-average-power-ratio/) and its reduction by
clipping, [selected mapping](/selected-mapping/) and tone reservation, each trading its own costs;
[Schmidl-Cox synchronization](/schmidl-cox-synchronization/), with the offset ranges its entry states;
[pilot-based channel estimation](/comb-pilot-channel-estimation/); and newer waveforms such as
[filter bank multicarrier](/filter-bank-multicarrier/) and [OTFS](/orthogonal-time-frequency-space-modulation/).

**Chapter 44.6, MIMO communications** (37 entries), uses many antennas at both ends. It covers the
[MIMO channel](/mimo-channel-model/) and its [capacity](/mimo-capacity/), [SVD precoding](/svd-precoding/)
with water-filling when the transmitter knows the channel, the [Alamouti code](/alamouti-code/), the only
complex [orthogonal space-time block code](/orthogonal-space-time-block-codes/) of rate one, and the
[diversity-multiplexing tradeoff](/diversity-multiplexing-tradeoff/), a high-SNR result. Detection runs from
[zero-forcing](/zero-forcing-mimo-detector/) and [MMSE](/mmse-mimo-detector/) detectors and
[V-BLAST](/v-blast/) to the [K-best detector](/k-best-detector/) and the
[list sphere decoder](/list-sphere-decoder/). [Massive MIMO](/massive-mimo/) brings
[channel hardening](/channel-hardening/) and [favorable propagation](/favorable-propagation/), which hold
under the stated channel models, and [pilot contamination](/pilot-contamination/), which limits them;
[dirty paper coding](/dirty-paper-coding/) gives the MIMO broadcast capacity region.

**Chapter 44.7, Multiple access and spread spectrum** (31 entries), shares one medium among many users. It
covers [FDMA](/frequency-division-multiple-access/), [TDMA](/time-division-multiple-access/) and
[OFDMA](/orthogonal-frequency-division-multiple-access/); spreading by
[direct sequence](/direct-sequence-spread-spectrum/) and [CDMA](/code-division-multiple-access/) with
[m-sequences](/maximal-length-sequence/), [Gold sequences](/gold-sequences/) and
[Zadoff-Chu sequences](/zadoff-chu-sequence/), limited by the [Welch bound](/welch-bound/); the
[near-far problem](/near-far-problem/) that arises without power control; [multiuser detection](/multiuser-detection/),
whose optimum form is [NP-hard](/multiuser-detection-np-hardness/), with the
[decorrelating detector](/decorrelating-detector/) and [successive interference cancellation](/successive-interference-cancellation/);
the [rake receiver](/rake-receiver/); the [MAC capacity region](/mac-capacity-region/) and
[NOMA](/non-orthogonal-multiple-access/); and [coded slotted ALOHA](/coded-slotted-aloha/).

**Chapter 44.8, Link adaptation and resource allocation** (26 entries), fits the transmission to the
channel. It covers [link adaptation](/link-adaptation/) and [adaptive modulation](/adaptive-modulation/),
[hybrid ARQ](/hybrid-arq/), [spectrum sensing](/spectrum-sensing/) by the [energy detector](/energy-detector/),
[Foschini-Miljanic power control](/foschini-miljanic-power-control/), which converges when the targets are
feasible, and [Yates's theorem](/standard-interference-function/) behind it; [max-rate scheduling](/max-rate-scheduling/)
and [multiuser diversity](/multiuser-diversity/); [water-filling](/water-filling-power-allocation/) and
[bit loading](/bit-loading/) by the [Hughes-Hartogs](/hughes-hartogs-algorithm/) and
[Levin-Campello](/levin-campello-algorithm/) algorithms; [OFDMA allocation](/ofdma-resource-allocation/); and
[interference alignment](/interference-alignment/).

**Chapter 44.9, Radar waveforms and detection** (22 entries), turns the receiver into a sensor. It covers
the [radar range equation](/radar-range-equation/), [Swerling targets](/swerling-target-models/),
[pulse compression](/pulse-compression/) and the [ambiguity function](/ambiguity-function/), whose volume is
fixed; chirps, [Barker codes](/barker-code/) and other codes; [CFAR detection](/cfar-detection/), which keeps
its false alarm rate only under its assumed clutter statistics; Doppler processing from
[MTI](/moving-target-indication/) to [STAP](/space-time-adaptive-processing/); [FMCW radar](/fmcw-radar/);
and [integrated sensing and communication](/integrated-sensing-and-communication/).

## How to read this volume

Chapter 44.1 comes first; the others assume its constellations, detectors and error rates. Chapters 44.2
and 44.3 can then be read in either order. Chapter 44.4 needs the fading models of 44.3, and 44.5 needs
44.4 for the channel and its estimation. Chapter 44.6 uses 44.3, and 44.7 and 44.8 draw on 44.5 and 44.6. Chapter 44.9 needs only 44.1 and the matched filter,
except for its last entry, which uses OFDM.

For a first course, take these entries in order: [Gaussian Q-function](/gaussian-q-function/),
[signal constellation](/signal-constellation/), [symbol detection](/symbol-detection/),
[bit error rate](/bit-error-rate/), [Nyquist criterion](/nyquist-isi-criterion/),
[Shannon-Hartley theorem](/shannon-hartley-theorem/), [phase-locked loop](/phase-locked-loop/),
[Rayleigh fading](/rayleigh-fading-channel/), [maximal ratio combining](/maximal-ratio-combining/),
[channel estimation](/channel-estimation/), [MMSE equalizer](/mmse-linear-equalizer/),
[cyclic prefix](/cyclic-prefix/), [OFDM](/orthogonal-frequency-division-multiplexing/),
[MIMO capacity](/mimo-capacity/), [Alamouti code](/alamouti-code/), [CDMA](/code-division-multiple-access/),
[water-filling](/water-filling-power-allocation/), [link adaptation](/link-adaptation/),
[pulse compression](/pulse-compression/) and [CFAR detection](/cfar-detection/). The learning path *Communications and radar*
goes through the volume step by step.

Each entry stands on its own; its facts box lists what it needs, by entry number.

## What you need first

From Volume 28 you need the [matched filter](/matched-filter/), the [sampling theorem](/sampling-theorem/),
[discrete convolution](/discrete-convolution/), [FIR filters](/fir-filter/),
[autocorrelation](/autocorrelation/), [signal detection](/signal-detection/) and the
[Kalman filter](/kalman-filter/). The [discrete Fourier transform](/discrete-fourier-transform/) and the
[fast Fourier transform](/fast-fourier-transform/) are in Volume 11. From Volume 24 come the
[AWGN channel](/additive-white-gaussian-noise-channel/), [channel capacity](/channel-capacity/), and the
codes the receivers decode: [convolutional codes](/convolutional-code/) on a [trellis](/trellis/), the
[BCJR algorithm](/bcjr-algorithm/), [turbo codes](/turbo-code/) and [LDPC codes](/ldpc-code/). The
[Viterbi algorithm](/viterbi-algorithm/) and [Bayes' theorem](/bayes-theorem/) are in Volume 25, the
[Cramér-Rao bound](/cramer-rao-bound/) and the [Neyman-Pearson lemma](/neyman-pearson-lemma/) in Volume 33,
and [least squares](/least-squares-problem/) and the [Cholesky decomposition](/cholesky-decomposition/) in
Volume 12. Sphere decoding is the [Schnorr-Euchner enumeration](/schnorr-euchner-enumeration/) of Volume 10.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
