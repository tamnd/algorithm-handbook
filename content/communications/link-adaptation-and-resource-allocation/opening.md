A wireless channel changes all the time. A phone carried behind a building can lose 20 dB, a subcarrier
that falls into a fade carries nothing, and a neighbour that starts to transmit raises the interference. A
link designed for the worst case wastes most of its capacity, and one designed for the average case fails
whenever the channel is below it. This chapter is about the algorithms that follow the channel: they choose
the rate, the power, the bits on each subcarrier and the user to serve, from reports of the channel that
are always a little late and a little wrong.

Most of these decisions are small optimization problems, solved again every millisecond. Some have exact
and fast solutions. [Water-filling](/water-filling-power-allocation/) maximizes the rate of parallel
Gaussian channels with a sort and a sum, and the [Hughes-Hartogs](/hughes-hartogs-algorithm/) greedy
rule is optimal for integer [bit loading](/bit-loading/) because each extra bit costs twice the one before.
[Max-rate scheduling](/max-rate-scheduling/) maximizes the total throughput of every slot, and the
[Foschini-Miljanic iteration](/foschini-miljanic-power-control/) finds the least powers that meet a set of
SINR targets whenever such powers exist. Others are hard: [weighted sum rate maximization](/weighted-sum-rate-maximization/)
with interference is NP-hard, and OFDMA allocation with rate targets is a mixed integer program. For those,
the algorithms find stationary points or good heuristics, and their quality is measured.

Two simplifications run through the chapter. The [SNR gap](/snr-gap-approximation/) replaces the error
rate formulas of real constellations by a single loss against capacity, which turns the problems into ones
about $\log_2(1 + \mathrm{SNR}/\Gamma)$. And the channel is assumed known at the transmitter, which in
practice means a report, an [outer loop](/outer-loop-link-adaptation/) to correct its bias, and
[hybrid ARQ](/hybrid-arq/) to repair the blocks that fail anyway. The last group of entries,
[spectrum sensing](/spectrum-sensing/), asks a different question: whether a band is free to use at all.

## What the chapter covers

1. **Matching the rate to the channel.** [Link adaptation](/link-adaptation/), the
   [SNR gap approximation](/snr-gap-approximation/), [adaptive modulation](/adaptive-modulation/) with
   variable rate and power, and [effective SNR mapping](/effective-snr-mapping/) for frequency selective
   channels.
2. **Retransmission and the outer loop.** [Hybrid ARQ](/hybrid-arq/),
   [Chase combining](/chase-combining/) and [outer loop link adaptation](/outer-loop-link-adaptation/).
3. **Power over parallel channels.** [Water-filling](/water-filling-power-allocation/),
   [truncated channel inversion](/truncated-channel-inversion/) and
   [energy-efficient power allocation](/energy-efficient-power-allocation/).
4. **Bit loading.** [Bit loading](/bit-loading/) and its algorithms: [Hughes-Hartogs](/hughes-hartogs-algorithm/),
   [Levin-Campello](/levin-campello-algorithm/) and [Chow-Cioffi-Bingham](/chow-cioffi-bingham-algorithm/).
5. **Scheduling many users.** [Multiuser diversity](/multiuser-diversity/),
   [max-rate scheduling](/max-rate-scheduling/), [OFDMA resource allocation](/ofdma-resource-allocation/)
   and [weighted sum rate maximization](/weighted-sum-rate-maximization/).
6. **Power control under interference.** [Foschini-Miljanic](/foschini-miljanic-power-control/),
   [Yates's standard interference functions](/standard-interference-function/),
   [max-min SINR](/max-min-sinr-power-control/), [geometric programming](/geometric-programming-power-control/)
   and [interference alignment](/interference-alignment/).
7. **Sensing the spectrum.** [Spectrum sensing](/spectrum-sensing/), the [energy detector](/energy-detector/)
   and [cyclostationary feature detection](/cyclostationary-feature-detection/).

## A first reading

Read these in order:

1. [Link adaptation](/link-adaptation/)
2. [SNR gap approximation](/snr-gap-approximation/)
3. [Hybrid ARQ](/hybrid-arq/)
4. [Water-filling power allocation](/water-filling-power-allocation/)
5. [Bit loading](/bit-loading/)
6. [Hughes-Hartogs algorithm](/hughes-hartogs-algorithm/)
7. [Multiuser diversity](/multiuser-diversity/)
8. [Max-rate scheduling](/max-rate-scheduling/)
9. [Foschini-Miljanic power control](/foschini-miljanic-power-control/)
10. [Energy detector](/energy-detector/)

These cover one example of each kind of decision: the rate, the repair, the power, the bits, the user and
the band.

## Before you start

You need the [Q-function](/gaussian-q-function/), [QAM](/quadrature-amplitude-modulation/),
[spectral efficiency](/spectral-efficiency/) and the [bit error rate](/bit-error-rate/) of chapter 44.1, and
the [Rayleigh fading channel](/rayleigh-fading-channel/), [maximal ratio combining](/maximal-ratio-combining/)
and [ergodic capacity](/ergodic-capacity/) of chapter 44.3. [Channel capacity](/channel-capacity/) and the
[channel coding theorem](/channel-coding-theorem/) are in Volume 24. The power problems use the
[KKT conditions](/kkt-conditions/), [Lagrangian duality](/lagrangian-duality/) and
[geometric programming](/geometric-programming/) of Volume 15, and power control uses the
[Perron-Frobenius theorem](/perron-frobenius-theorem/) and [fixed-point iteration](/fixed-point-iteration/)
of Volume 12. Detection in the last group is the [Neyman-Pearson lemma](/neyman-pearson-lemma/) of Volume
33 applied to [signal detection](/signal-detection/). Fairer schedulers, such as
[proportional-fair scheduling](/proportional-fair-scheduling/), are in Volume 26.
