A cell tower serves hundreds of phones on a few tens of megahertz, a GPS receiver hears a dozen
satellites on the same carrier, and thousands of sensors may wake up at once to report a reading. In each
case many transmitters share one channel, and the receiver must separate them. Multiple access is the set of
methods that decide how the channel is shared, and spread spectrum is the family of signals that lets users
share a band without dividing it.

There are three ways to share. The first is to divide the channel into parts that do not overlap: bands in
[FDMA](/frequency-division-multiple-access/), slots in [TDMA](/time-division-multiple-access/), sets of
subcarriers in [OFDMA](/orthogonal-frequency-division-multiple-access/). The users then never interfere,
and the cost is the guard bands and guard times and the rate lost when the parts do not match the users'
needs. The second is to let every user send over the whole band at once, each with its own spreading code,
as in [CDMA](/code-division-multiple-access/). The receiver correlates with one code and collects that user,
but it also collects a little of every other user, and a strong user can swamp a weak one: this is the
[near-far problem](/near-far-problem/). The third is to give up on separating the users at the transmitter
and to decode them jointly at the receiver, as in [superposition coding](/superposition-coding/) and
[NOMA](/non-orthogonal-multiple-access/). The [MAC capacity region](/mac-capacity-region/) shows that this
is where the largest sum rates are.

Most of the chapter is about the algorithms that make the second and third ways work: generating spreading
codes with good correlations, finding the code phase, tracking it, combining multipath, and detecting many
users at once. The [optimum multiuser detector](/optimum-multiuser-detector/) is
[NP-hard](/multiuser-detection-np-hardness/) in the number of users, so the practical detectors are linear
filters and cancellers whose performance is proved only in special cases and is otherwise measured.

## What the chapter covers

1. **Sharing by frequency and time.** [FDMA](/frequency-division-multiple-access/),
   [TDMA](/time-division-multiple-access/) and [OFDMA](/orthogonal-frequency-division-multiple-access/),
   with their guard overheads and their rates against the capacity of the shared channel.
2. **Spreading the signal.** The [processing gain](/processing-gain/),
   [frequency hopping](/frequency-hopping-spread-spectrum/), the [m-sequence](/maximal-length-sequence/),
   [direct-sequence spreading](/direct-sequence-spread-spectrum/) and
   [code-division multiple access](/code-division-multiple-access/).
3. **Spreading sequences and their limits.** [Gold sequences](/gold-sequences/),
   [OVSF codes](/ovsf-codes/), the [Zadoff-Chu sequence](/zadoff-chu-sequence/), the
   [Welch bound](/welch-bound/) on cross-correlation and the [Kasami sequences](/kasami-sequences/), whose
   small set is the best possible among binary sets of its size and period.
4. **Acquisition, tracking and multipath.** [Serial search](/serial-search-code-acquisition/),
   [parallel code phase search](/parallel-code-phase-search/) by FFT, the
   [delay-locked loop](/delay-locked-loop/) and the [rake receiver](/rake-receiver/).
5. **Multiuser detection.** The [near-far problem](/near-far-problem/), the
   [problem of multiuser detection](/multiuser-detection/), the [decorrelator](/decorrelating-detector/),
   the [MMSE detector](/mmse-multiuser-detector/), [SIC](/successive-interference-cancellation/) and
   [PIC](/parallel-interference-cancellation/), the [optimum detector](/optimum-multiuser-detector/) and the
   proof that it is [NP-hard](/multiuser-detection-np-hardness/).
6. **Capacity and non-orthogonal access.** The [MAC capacity region](/mac-capacity-region/),
   [superposition coding](/superposition-coding/), [NOMA](/non-orthogonal-multiple-access/) and
   [SCMA](/sparse-code-multiple-access/).
7. **Random access with coding.** [Coded slotted ALOHA](/coded-slotted-aloha/) and
   [unsourced random access](/unsourced-random-access/).

## A first reading

Read these in order:

1. [Frequency-division multiple access](/frequency-division-multiple-access/)
2. [Time-division multiple access](/time-division-multiple-access/)
3. [Processing gain](/processing-gain/)
4. [Maximal-length sequence](/maximal-length-sequence/)
5. [Direct-sequence spread spectrum](/direct-sequence-spread-spectrum/)
6. [Code-division multiple access](/code-division-multiple-access/)
7. [Near-far problem](/near-far-problem/)
8. [Decorrelating detector](/decorrelating-detector/)
9. [Successive interference cancellation](/successive-interference-cancellation/)
10. [MAC capacity region](/mac-capacity-region/)

The first two entries set up the baseline of orthogonal sharing. The next four build a CDMA link from the
ground up. The last four show why CDMA needs more than a matched filter, and what the best receiver can
reach in principle.

## Before you start

The chapter assumes the Gaussian channel and its [capacity](/channel-capacity/), the
[energy per bit](/energy-per-bit-to-noise-density-ratio/) and the [Q-function](/gaussian-q-function/) of
chapter 44.1. The [matched filter](/matched-filter/), [autocorrelation](/autocorrelation/) and
[cross-correlation](/cross-correlation/) are treated in Volume 28 and used throughout. The
[fast Fourier transform](/fast-fourier-transform/) is used for acquisition. Spreading codes are built from
[linear feedback shift registers](/linear-feedback-shift-register/) and
[primitive polynomials](/primitive-polynomial/). Small matrix inverses appear in multiuser detection; for
the hardness proof you need [maximum cut](/maximum-cut/) and [NP-hardness](/np-hard/). For random access,
read [slotted ALOHA](/slotted-aloha/) first; the error-correcting codes behind the capacity results are in
Volume 24.
