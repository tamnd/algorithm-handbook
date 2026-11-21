A digital radio link with 64-QAM maps each group of six bits to one of 64 points in the plane, shapes each
point into a pulse, and puts the pulses on a carrier. The receiver gets their sum, blurred by the channel and
buried in thermal noise. It has to decide which of the 64 points was sent, or, if a decoder follows, how sure
it is of each of the six bits. Modulation is the choice of points and pulses; detection is the decision.
For the standard model, coherent detection in additive white Gaussian noise with perfect synchronization,
both are exact in a way that few parts of engineering are: the symbol error rate of PAM, QPSK or square QAM
is a short sum of values of one function, the [Gaussian Q-function](/gaussian-q-function/), and that of any
other constellation is bounded by such sums.

The chapter starts from the [signal space](/signal-space-representation/), where every waveform is a vector
and the noise is the same in every direction, so the best detector is the
[minimum-distance detector](/minimum-distance-detector/) when the symbols are equally likely. From there it
goes three ways. The first is bandwidth: pulses that overlap without interfering at the sampling instants, as
the [Nyquist criterion](/nyquist-isi-criterion/) requires. The second is the power amplifier: signals with a
constant envelope, such as [GMSK](/gaussian-minimum-shift-keying/) in GSM. The third is the code: soft bit
reliabilities for a decoder, and constellations that are shaped to come close to the
[Shannon-Hartley](/shannon-hartley-theorem/) limit. Throughout, keep apart what is exact (the symbol error rate
of PAM, QPSK and square QAM in the stated model), what is an approximation (the Gray bit error rate of
M-PSK and M-QAM, good at high SNR) and what is a bound (union and Chernoff bounds).

## What the chapter covers

1. **Signals, noise and limits.** The [Q-function](/gaussian-q-function/),
   [digital modulation](/digital-modulation/), [$E_b/N_0$](/energy-per-bit-to-noise-density-ratio/), the
   [signal space](/signal-space-representation/), [constellations](/signal-constellation/), the
   [Shannon-Hartley theorem](/shannon-hartley-theorem/) and [spectral efficiency](/spectral-efficiency/).
2. **The basic constellations.** [PAM](/pulse-amplitude-modulation/), [PSK](/phase-shift-keying/),
   [QAM](/quadrature-amplitude-modulation/) and [FSK](/frequency-shift-keying/).
3. **Detection and error rates.** [Symbol detection](/symbol-detection/) by MAP and ML, the
   [minimum-distance detector](/minimum-distance-detector/), the [symbol error rate](/symbol-error-rate/),
   [Gray labeling](/gray-labeling/) and the [bit error rate](/bit-error-rate/).
4. **Pulses and intersymbol interference.** [Intersymbol interference](/intersymbol-interference/), the
   [Nyquist criterion](/nyquist-isi-criterion/), [pulse shaping](/pulse-shaping/), the
   [raised cosine](/raised-cosine-filter/) and [root raised cosine](/root-raised-cosine-filter/) filters, and
   the [eye diagram](/eye-diagram/).
5. **Controlled intersymbol interference.** [Partial-response signaling](/partial-response-signaling/) and
   [faster-than-Nyquist signaling](/faster-than-nyquist-signaling/).
6. **Constant envelope and noncoherent reception.** [Offset QPSK](/offset-qpsk/),
   [continuous-phase modulation](/continuous-phase-modulation/), [MSK](/minimum-shift-keying/),
   [GMSK](/gaussian-minimum-shift-keying/), the [Laurent decomposition](/laurent-decomposition/),
   [noncoherent detection](/noncoherent-detection/) and [DPSK](/differential-phase-shift-keying/).
7. **Soft bits and coded modulation.** [Soft demapping](/soft-demapping/),
   [max-log demapping](/max-log-demapping/), [trellis-coded modulation](/trellis-coded-modulation/),
   [BICM](/bit-interleaved-coded-modulation/) and [multilevel coding](/multilevel-coding/).
8. **Shaping.** [APSK](/amplitude-and-phase-shift-keying/),
   [probabilistic constellation shaping](/probabilistic-constellation-shaping/) and
   [constant composition distribution matching](/constant-composition-distribution-matching/).

## A first reading

Read these in order:

1. [Gaussian Q-function](/gaussian-q-function/)
2. [Signal space representation](/signal-space-representation/)
3. [Signal constellation](/signal-constellation/)
4. [Quadrature amplitude modulation](/quadrature-amplitude-modulation/)
5. [Symbol detection](/symbol-detection/)
6. [Symbol error rate](/symbol-error-rate/)
7. [Gray labeling](/gray-labeling/)
8. [Bit error rate](/bit-error-rate/)
9. [Nyquist ISI criterion](/nyquist-isi-criterion/)
10. [Root raised cosine filter](/root-raised-cosine-filter/)
11. [Shannon-Hartley theorem](/shannon-hartley-theorem/)
12. [Soft demapping](/soft-demapping/)

They give the path from a waveform to a bit decision and its error rate, the pulses of a real modem, the
limit, and the interface to a decoder. On a first pass, skip the constant-envelope group except
[MSK](/minimum-shift-keying/), and the shaping group, and come back to
[TCM](/trellis-coded-modulation/) and [BICM](/bit-interleaved-coded-modulation/) after the codes of Volume 24.

## Before you start

The chapter assumes probability and a little linear algebra. From Volume 24 you need the
[AWGN channel](/additive-white-gaussian-noise-channel/) and [channel capacity](/channel-capacity/), and for
the coded group the [convolutional code](/convolutional-code/), the [trellis](/trellis/) and
[maximum-likelihood sequence estimation](/maximum-likelihood-sequence-estimation/). From Volume 28 you need
[discrete convolution](/discrete-convolution/), the [sampling theorem](/sampling-theorem/) and the
[matched filter](/matched-filter/). The [Gram-Schmidt process](/gram-schmidt-process/) and the
[log-sum-exp trick](/log-sum-exp-trick/) are in Volume 12, [Bayes' theorem](/bayes-theorem/) and the
[Viterbi algorithm](/viterbi-algorithm/) in Volume 25, and the [Gray code](/gray-code/) in Volume 14. The
shaping entries use [Shannon entropy](/shannon-entropy/) and [arithmetic coding](/arithmetic-coding/) from
Volume 24 and the [Kullback-Leibler divergence](/kullback-leibler-divergence/) from Volume 33.
