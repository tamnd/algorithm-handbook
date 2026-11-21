A Wi-Fi channel indoors has echoes that arrive up to a few hundred nanoseconds after the direct path. At 20
million symbols per second a symbol lasts 50 ns, so every received sample is a mix of several transmitted
ones, and a time-domain equalizer for that channel costs $O(NL)$ work for $N$ samples and $L$ taps.
802.11a cuts the stream into blocks of 64 values, puts each on its own subcarrier with one inverse FFT, and
copies the last 16 samples of each block in front of it. Each 4 μs symbol then sees the channel as a circular
convolution. After one FFT at the receiver, subcarrier $k$ carries $H[k]X[k]$ plus noise, and the equalizer
is a single complex division per subcarrier. The same plan, with other numbers, runs ADSL and VDSL on copper,
LTE and 5G NR in cellular networks, and digital television and radio.

The price of this simple receiver is paid elsewhere. The prefix costs rate, a factor $N/(N+N_{cp})$, which is
0.8 for 802.11a. The receiver needs the gain of every subcarrier. A small frequency offset or phase noise
breaks the orthogonality the FFT relies on. The sum of many independent subcarriers looks Gaussian, so its
peaks are much higher than its mean power and the power amplifier must back off. Most of this chapter is about
these costs and the algorithms that reduce them.

## What the chapter covers

1. **From one carrier to many.** [Multicarrier modulation](/multicarrier-modulation/) splits a wideband
   channel into narrow flat ones. The [cyclic prefix](/cyclic-prefix/) of at least $L-1$ samples turns the
   linear channel into a [circular convolution](/circular-convolution/), and
   [OFDM](/orthogonal-frequency-division-multiplexing/) diagonalizes it with the DFT at a cost of
   $O(N\log N)$ per symbol. [Discrete multitone](/discrete-multitone/) is the real baseband form used on wires,
   with bit loading per tone.
2. **Learning the channel from pilots.** [Comb pilots](/comb-pilot-channel-estimation/) measure $H[k]$ on a
   few subcarriers and interpolate. The [DFT-based estimator](/dft-based-channel-estimation/) projects the
   estimate onto the short impulse responses and keeps only $L_t/N$ of the noise.
   [Two-dimensional Wiener interpolation](/two-dimensional-wiener-pilot-interpolation/) is the best linear
   estimate when the channel statistics are known.
3. **Synchronization and analog impairments.**
   [Inter-carrier interference](/inter-carrier-interference/) is what a frequency offset of a fraction
   $\varepsilon$ of the spacing costs, about $(\pi\varepsilon)^2/3$ of the power. The
   [Schmidl-Cox](/schmidl-cox-synchronization/), [Moose](/moose-frequency-offset-estimator/) and
   [van de Beek](/van-de-beek-estimator/) estimators find the offset from repeated samples, with different
   ranges and variances. [Common phase error correction](/common-phase-error-correction/) and
   [IQ imbalance compensation](/iq-imbalance-compensation/) deal with the oscillator and the mixer.
4. **The peak power problem.** The [peak-to-average power ratio](/peak-to-average-power-ratio/) of $N$
   subcarriers can reach $N$, and its tail follows the rule $1-(1-e^{-\gamma})^N$.
   [Clipping and filtering](/iterative-clipping-and-filtering/), [selected mapping](/selected-mapping/),
   [partial transmit sequences](/partial-transmit-sequence/), [tone reservation](/tone-reservation/) and
   [active constellation extension](/active-constellation-extension/) reduce it at the price of distortion,
   side information, rate or power. [SC-FDMA](/sc-fdma/) spreads the data with a DFT first and saves about
   2 dB for QPSK.
5. **Shaped and filtered multicarrier.** [Filter bank multicarrier](/filter-bank-multicarrier/),
   [GFDM](/generalized-frequency-division-multiplexing/) and
   [UFMC](/universal-filtered-multicarrier/) replace the rectangular pulse by shaped ones to cut the
   out-of-band leakage, each giving up something OFDM has: complex orthogonality, orthogonality itself, or
   the cyclic prefix.
6. **Waveforms for doubly dispersive channels.**
   [OTFS](/orthogonal-time-frequency-space-modulation/) and [AFDM](/affine-frequency-division-multiplexing/)
   place the data so that a channel with delay and Doppler spread acts as a few shifts that the receiver can
   separate.

## A first reading

Read these in order:

1. [Multicarrier modulation](/multicarrier-modulation/)
2. [Cyclic prefix](/cyclic-prefix/)
3. [OFDM](/orthogonal-frequency-division-multiplexing/)
4. [Comb-pilot channel estimation](/comb-pilot-channel-estimation/)
5. [DFT-based channel estimation](/dft-based-channel-estimation/)
6. [Inter-carrier interference](/inter-carrier-interference/)
7. [Schmidl-Cox synchronization](/schmidl-cox-synchronization/)
8. [Peak-to-average power ratio](/peak-to-average-power-ratio/)
9. [Selected mapping](/selected-mapping/)
10. [SC-FDMA](/sc-fdma/)

These give the whole path of one OFDM link: the symbol, the channel estimate, the frequency offset and the
peak power. Discrete multitone can wait unless you work on wireline systems. Of the impairments, the Moose
and van de Beek estimators repeat the idea of Schmidl-Cox with other training, and phase noise and IQ
imbalance can be read when needed. The last two groups, on shaped and doubly dispersive waveforms, build on
everything else and are best left to the end.

## Before you start

The chapter uses the [discrete Fourier transform](/discrete-fourier-transform/) and the
[fast Fourier transform](/fast-fourier-transform/) (Volume 11) throughout, with the
[convolution theorem](/convolution-theorem/). From Volume 28 it uses
circular convolution, the [Wiener filter](/wiener-filter/) and
[spectral leakage](/spectral-leakage/). From this volume it assumes
[intersymbol interference](/intersymbol-interference/), [multipath fading](/multipath-fading/),
[quadrature amplitude modulation](/quadrature-amplitude-modulation/) and
[least squares channel estimation](/least-squares-channel-estimation/). The synchronization entries compare
their variances with the [Cramér-Rao bound](/cramer-rao-bound/) (Volume 33). The tone reservation entry
states its optimum as a [second-order cone program](/second-order-cone-programming/) (Volume 15). Complex
numbers, unitary matrices and the Gaussian distribution are assumed.
