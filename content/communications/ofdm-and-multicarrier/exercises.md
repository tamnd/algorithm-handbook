1. ◦ A two-tap channel $h = (1, -0.5)$ is used with [OFDM](/orthogonal-frequency-division-multiplexing/) on
   $N = 4$ subcarriers, with $H[k] = \sum_n h[n]e^{-j2\pi kn/N}$. Compute the four gains $H[k]$. Which
   subcarrier is weakest, and what is its SNR when the SNR before the channel is 10 dB? What is the shortest
   [cyclic prefix](/cyclic-prefix/) that makes the channel circular?

2. ◦ An OFDM system samples at 10 MHz with $N = 512$ and $N_{cp} = 64$. Find the subcarrier spacing, the
   length of one symbol with its prefix, the rate factor and the SNR loss in dB that the prefix costs, and the
   longest channel, in taps, that the prefix covers.

3. ◦ Take $N = 4$ BPSK subcarriers with $X = (1, 1, -1, -1)$ and the unitary inverse DFT. Write the four time
   samples and the [peak-to-average power ratio](/peak-to-average-power-ratio/) at these Nyquist samples.
   Then list how many of the 16 BPSK blocks have PAPR 4, 2 and 1. Finally evaluate the rule
   $1-(1-e^{-\gamma})^N$ for $N = 16$ at 8 dB.

4. ◦ A frequency offset of $\varepsilon = 0.25$ subcarrier spacings hits an OFDM symbol with $N = 64$.
   Compute $|S(\varepsilon)|^2$, the power of the [inter-carrier interference](/inter-carrier-interference/),
   the approximation $(\pi\varepsilon)^2/3$, and the ratio of the useful power $|S(\varepsilon)|^2$ to the
   ICI in dB. What offset in hertz is this at a spacing of 15 kHz?

5. ◦ The true offset is $\varepsilon = 0.7$ spacings, with $N = 64$ and $G = N_{cp} = 16$. What does each
   estimator return: the [Moose estimator](/moose-frequency-offset-estimator/) on two symbols $N + G$ samples
   apart, the [van de Beek estimator](/van-de-beek-estimator/), and the fractional part of
   [Schmidl-Cox](/schmidl-cox-synchronization/)? Which of them is right?

6. ◦ A channel has $L = 20$ taps and the symbol has $N = 256$ subcarriers. What is the largest spacing $D$ of
   [comb pilots](/comb-pilot-channel-estimation/), and the largest power of two below it, with its pilot
   overhead? With a preamble in which all 256 subcarriers carry pilots, by how many dB does the
   [DFT-based estimator](/dft-based-channel-estimation/) that keeps 20 taps lower the error of least squares?
   And with the comb of spacing 8 alone?

7. ◦ [Selected mapping](/selected-mapping/) with $U = 8$ runs on $N = 256$ subcarriers oversampled $L = 4$
   times. How many bits of side information does it send, and how many inverse FFTs of which size does it
   compute? Answer the same for [partial transmit sequences](/partial-transmit-sequence/) with $V = 4$
   subblocks and $W = 4$ phase factors, and give the number of candidates it compares. How many inverse FFTs
   would selected mapping need to compare as many candidates?

8. ◦ An IQ mixer has gain mismatch $g = 1$ and phase mismatch $\varphi = 10°$, so that
   $\mu = (1 + ge^{-j\varphi})/2$ and $\nu = (1 - ge^{j\varphi})/2$. Compute $\mu$, $\nu$ and the image
   rejection $|\mu|^2/|\nu|^2$ in dB, the ratio that
   [IQ imbalance compensation](/iq-imbalance-compensation/) improves on.

9. ◦ [Active constellation extension](/active-constellation-extension/) is applied to 16-QAM. Sort the 16
   points by how they may move, and count each kind.

10. • Zero padding sends $N$ samples followed by $N_{cp} \ge L-1$ zeros. Show that if the receiver adds the
    last $N_{cp}$ received samples onto the first $N_{cp}$ (overlap-add), the result is the circular
    convolution of the data block with $h$, so the usual one-tap equalizer applies.

11. • With $N = 8$, $N_{cp} = 3$ and a channel of $L = 2$ taps, how many samples early can the receiver start
    its FFT window without causing intersymbol interference? If it starts one sample early, what factor
    multiplies $X[2]$ after the FFT?

12. • Let $S(\varepsilon) = \frac{1}{N}\sum_{n=0}^{N-1} e^{j2\pi\varepsilon n/N}$. Show that
    $1-|S(\varepsilon)|^2 = \frac{(\pi\varepsilon)^2}{3}\left(1-\frac{1}{N^2}\right) + O(\varepsilon^4)$.

13. • Comb pilots with spacing $D$ give least squares estimates with independent noise of variance
    $\sigma^2$, and the receiver interpolates linearly between neighbouring pilots. Averaged over the $D$
    positions of a gap (the pilot itself included), show that the noise variance of the estimate is
    $\sigma^2(2D^2+1)/(3D^2)$. Evaluate it for $D = 2, 4, 8$ and give the limit.

14. • Show that the DFT-based estimator, which transforms the least squares estimate to the time domain,
    keeps the first $L_t$ taps and transforms back, is an orthogonal projection, and that its error per
    subcarrier is $L_t N_0/N$ when the preamble fills all subcarriers. A receiver with $N = 128$ keeps 17
    taps for a channel of 6 taps. What does it lose in dB against keeping exactly 6?

15. • The frequency correlation of a channel is $r(d) = 0.9^{|d|}$ for subcarriers $d$ apart, with
    $E|H[k]|^2 = 1$. Pilots at $k = 0$ and $k = 4$ give $H[k]$ plus noise of variance 0.1. Find the
    [Wiener](/two-dimensional-wiener-pilot-interpolation/) weights for $H[2]$ and their error. Compare with
    linear interpolation, weights $(0.5, 0.5)$, and with the Wiener estimate from the pilot at 0 alone.

16. • With $\mu$ and $\nu$ as in exercise 8 for any $g$ and $\varphi$, show that $|\mu|^2 - |\nu|^2 =
    g\cos\varphi$, and that for $g = 1$ the ratio $|\nu|^2/|\mu|^2$ is $\tan^2(\varphi/2)$.

17. • Model phase noise as a random walk, $\phi[n] = \phi[n-1] + w[n]$ with $w[n]$ Gaussian of variance
    $\sigma^2$. The common phase term is $I_0 = \frac{1}{N}\sum_n e^{j\phi[n]}$. Write $E|I_0|^2$ as a single
    sum, and evaluate it exactly for $N = 1024$ and $\sigma^2 = 10^{-4}$. Compare with
    $1 - \sigma^2 N/6$. After [common phase error correction](/common-phase-error-correction/), what is the
    remaining ICI and the signal to ICI ratio? What happens to the ICI when $N$ doubles?

18. • Write a program that estimates $\Pr(\text{PAPR} > \gamma)$ for $N = 16$ QPSK subcarriers, with
    oversampling $L = 1$ and $L = 4$ (zero padding in the middle of the spectrum), from 20000 random blocks.
    Print the estimates at 6, 7 and 8 dB beside the rule $1-(1-e^{-\gamma})^N$. What is the largest PAPR that
    can occur?

19. • At 8 dB the rule gives $\Pr(\text{PAPR} > \gamma) = 0.110$ for $N = 64$. Treating the $U$ candidates of
    selected mapping as independent, find the smallest $U$ that brings the probability below $10^{-4}$, and
    the probability it gives. Why is this only a rule of thumb?

20. • For $N = 64$, $G = N_{cp} = 16$ and an SNR of 10 dB, evaluate the variance and the range of the
    Schmidl-Cox estimator, of Moose with $G = 16$ and with $G = 0$, and of van de Beek, using the formulas
    with the factor $1 + 1/(2\,\mathrm{SNR})$. Which estimator would you use if the offset may reach 0.45
    spacings?

21. • Design an OFDM numerology for a maximum delay of 5 μs with a prefix overhead of at most 10 percent and
    an ICI power below 0.01 for a worst frequency error of 1 kHz, treated as a fixed offset. Find the range
    of allowed subcarrier spacings, and check one choice.

22. ★ Prove that for any real $\varepsilon$, $\sum_{m=0}^{N-1}|S(m+\varepsilon)|^2 = 1$, with $S$ as in
    exercise 12. What does this say about where the power of a subcarrier goes under a frequency offset?

23. ★ Write optimal [tone reservation](/tone-reservation/) as a convex problem: with reserved set $R$,
    choose the values $C$ on the reserved tones to minimize the peak $\max_m |x[m] + (F_R^H C)[m]|$. Show
    that the problem is a [second-order cone program](/second-order-cone-programming/), and that the peak
    reached by any iterative kernel method is never below its optimum.

24. ★ Simulate the Schmidl-Cox frequency estimate for $N = 64$ at an SNR of 10 dB with $\varepsilon = 0.2$
    and known timing, over a few thousand runs with a seeded generator. Compare the measured variance with
    the formula $\frac{1}{\pi^2(N/2)\mathrm{SNR}}\left(1 + \frac{1}{2\,\mathrm{SNR}}\right)$, and explain
    why the two need not agree exactly.

25. ★ A rectangular pilot grid has one pilot every $D_t$ symbols and every $D_f$ subcarriers. Using the
    sampling theorem in time and in frequency, show that the grid can follow the channel when
    $D_t T_s \le 1/(2f_D)$ and $D_f \le 1/(\tau_{\max}\Delta f)$. Evaluate both bounds for $f_D = 500$ Hz,
    $T_s = 1/14$ ms, $\tau_{\max} = 4.7$ μs and $\Delta f = 15$ kHz.

26. ★ Take $h = (1, 1)$ and $N = 4$. Show that CP-OFDM cannot recover $X[2]$ for any equalizer, while
    zero-padded OFDM recovers all four values without noise. What property of the zero-padded channel matrix
    makes the difference?
