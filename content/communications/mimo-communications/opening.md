A Wi-Fi access point with four antennas, talking to a laptop with four antennas, can send four streams at
once on the same frequency. Each receive antenna hears a different mix of the four, and the receiver
untangles them because it knows the mixing matrix $H$. In i.i.d. Rayleigh fading at 20 dB, the ergodic
capacity of this $4 \times 4$ link is 22.1 bits per channel use, against 5.9 for one antenna at each end:
the capacity grows like $\min(N_t, N_r)\log_2 \rho$, so the extra antennas multiply the rate instead of
adding a little SNR. The same matrix also gives diversity. If the antennas carry copies of one symbol in
the right pattern, the error probability falls like $\rho^{-N_tN_r}$ instead of $\rho^{-1}$. Cellular base
stations push the idea further. A 5G base station in the 3.5 GHz band often has 64 antennas and serves several
users at once on the same resources.

Every algorithm in the chapter answers one of three questions about $y = Hx + w$. Without channel knowledge
at the transmitter, how should the symbols be spread over antennas and time? At the receiver, how can the
symbol vector be found when exact maximum likelihood is a closest vector search? With channel knowledge at
the transmitter, how should the signal be precoded, for one user or for many? Large arrays then change the
answers, because the law of large numbers makes simple methods nearly optimal.

## What the chapter covers

1. **The MIMO channel and its capacity.** The [MIMO channel model](/mimo-channel-model/) and the
   [Kronecker model](/kronecker-channel-model/) of antenna correlation. The [capacity](/mimo-capacity/)
   with channel knowledge at both ends is reached by [SVD precoding](/svd-precoding/) with water-filling. At
   the receiver only, equal power is optimal in i.i.d. Rayleigh fading, and
   [spatial multiplexing](/spatial-multiplexing/) turns the $\min(N_t, N_r)$ slope into independent streams.
2. **Space-time codes for diversity.** The [Alamouti code](/alamouti-code/) and
   [orthogonal space-time block codes](/orthogonal-space-time-block-codes/), the
   [rank and determinant criteria](/rank-and-determinant-criteria/),
   [space-time trellis codes](/space-time-trellis-codes/), the
   [diversity-multiplexing tradeoff](/diversity-multiplexing-tradeoff/) and the
   [golden code](/golden-code/) that reaches it on two antennas.
3. **Detecting the streams.** The [MIMO detection](/mimo-detection/) problem, the linear
   [zero-forcing](/zero-forcing-mimo-detector/) and [MMSE](/mmse-mimo-detector/) detectors,
   [V-BLAST](/v-blast/) and [D-BLAST](/d-blast/), the tree searches of the [K-best detector](/k-best-detector/)
   and the [list sphere decoder](/list-sphere-decoder/), and
   [lattice reduction aided detection](/lattice-reduction-aided-detection/).
4. **Relaxation and message passing.** [Semidefinite relaxation](/semidefinite-relaxation-detection/),
   [approximate message passing](/amp-mimo-detection/) and
   [expectation propagation](/expectation-propagation-detection/), for large or hard instances.
5. **Precoding and the broadcast channel.** [Maximum ratio transmission](/maximum-ratio-transmission/),
   [codebook-based precoding](/codebook-based-precoding/), [zero-forcing](/zero-forcing-precoding/) and
   [regularized zero-forcing](/regularized-zero-forcing-precoding/) precoding,
   [block diagonalization](/block-diagonalization/), [vector perturbation](/vector-perturbation-precoding/),
   [dirty paper coding](/dirty-paper-coding/) and [weighted MMSE](/weighted-mmse-precoding/) precoding.
6. **Large arrays.** [Massive MIMO](/massive-mimo/), [channel hardening](/channel-hardening/),
   [favorable propagation](/favorable-propagation/) and [pilot contamination](/pilot-contamination/), then
   [cell-free massive MIMO](/cell-free-massive-mimo/), [hybrid beamforming](/hybrid-beamforming/) and
   [reconfigurable intelligent surfaces](/reconfigurable-intelligent-surface/).

## A first reading

1. [MIMO channel model](/mimo-channel-model/)
2. [MIMO capacity](/mimo-capacity/)
3. [Spatial multiplexing](/spatial-multiplexing/)
4. [SVD precoding](/svd-precoding/)
5. [Alamouti code](/alamouti-code/)
6. [Rank and determinant criteria](/rank-and-determinant-criteria/)
7. [MIMO detection](/mimo-detection/)
8. [Zero-forcing MIMO detector](/zero-forcing-mimo-detector/)
9. [MMSE MIMO detector](/mmse-mimo-detector/)
10. [V-BLAST](/v-blast/)
11. [Maximum ratio transmission](/maximum-ratio-transmission/)
12. [Zero-forcing precoding](/zero-forcing-precoding/)
13. [Massive MIMO](/massive-mimo/)

This path gives the capacity, one diversity code, the standard receivers and the standard precoders. The
diversity-multiplexing tradeoff and the golden code can wait until the rank criterion is familiar. Of the
detectors, the tree searches matter when you need near-ML performance, and the relaxation and message
passing detectors are research topics. Dirty paper coding and weighted MMSE are needed for the theory of the
broadcast channel rather than for a first design.

## Before you start

The chapter uses the [singular value decomposition](/singular-value-decomposition/), the
[pseudoinverse](/pseudoinverse/), the [QR decomposition](/qr-decomposition/) and
[Tikhonov regularization](/tikhonov-regularization/) from Volume 12, and the
[law of large numbers](/law-of-large-numbers/) and the [Chernoff bound](/chernoff-bound/) from Volume 1.
[Channel capacity](/channel-capacity/) and the [AWGN channel](/additive-white-gaussian-noise-channel/) are
in Volume 24. From this volume it assumes the [Rayleigh fading channel](/rayleigh-fading-channel/),
[maximal ratio combining](/maximal-ratio-combining/), [diversity order](/diversity-order/),
[outage probability](/outage-probability/) and [water-filling](/water-filling-power-allocation/). The
detectors build on the [closest vector problem](/closest-vector-problem/), the
[LLL algorithm](/lll-algorithm/) and [Schnorr-Euchner enumeration](/schnorr-euchner-enumeration/) of
Volume 10, and the relaxation and message passing detectors on
[semidefinite programming](/semidefinite-programming/) (Volume 15) and
[belief propagation](/belief-propagation/) (Volume 25).
