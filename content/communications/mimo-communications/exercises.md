1. ◦ A $2 \times 2$ channel is $H = \mathrm{diag}(2, 0.5)$ with $N_0 = 1$. Use
   [water-filling](/water-filling-power-allocation/) to find the powers and the capacity for $P = 10$ and for
   $P = 1$, and compare each with equal power on the two antennas. This is what
   [SVD precoding](/svd-precoding/) does for a channel that is already diagonal.

2. ◦ The [Alamouti code](/alamouti-code/) sends BPSK symbols $s_1 = 1$ and $s_2 = -1$ over one receive
   antenna with $h_{11} = 1$ and $h_{12} = j$, without noise. With antenna 1 sending $s_1, -s_2^*$ and
   antenna 2 sending $s_2, s_1^*$, compute $y_{11}$ and $y_{12}$, the combiner outputs
   $z_1 = h_{11}^*y_{11} + h_{12}y_{12}^*$ and $z_2 = h_{12}^*y_{11} - h_{11}y_{12}^*$, and the decisions.

3. ◦ Take $H = \begin{pmatrix} 1 & 0.8 \\ 0 & 0.6 \end{pmatrix}$, unit-norm columns with correlation 0.8,
   and $E_s/N_0 = 10$ dB. Find the noise enhancement of the
   [zero-forcing detector](/zero-forcing-mimo-detector/) in dB, its post-detection SNR, and the SINR of the
   [MMSE detector](/mmse-mimo-detector/) after bias removal, $1/((N_0/E_s)P_{kk}) - 1$ with
   $P = (H^HH + (N_0/E_s)I)^{-1}$.

4. ◦ Draw the [diversity-multiplexing tradeoff](/diversity-multiplexing-tradeoff/) of a $4 \times 2$ i.i.d.
   Rayleigh channel: give its corner points and $d^*(0.5)$ and $d^*(1.5)$.

5. ◦ What is the largest rate of a complex
   [orthogonal design](/orthogonal-space-time-block-codes/) with entries $0$, $\pm s_k$, $\pm s_k^*$ for
   3, 6 and 8 transmit antennas? How many states does a
   [space-time trellis code](/space-time-trellis-codes/) need at least for full diversity on two antennas at 3
   bits per channel use, and on three antennas at 2 bits per channel use?

6. ◦ A [massive MIMO](/massive-mimo/) cell has $M = 64$ antennas and $K = 8$ users with $\beta_k = 1$. With the
   approximation $\mathrm{SINR} \approx Mp/((K-1)p + 1)$ for maximal ratio combining, find the SINR and the
   rate per user at $p = 1$ and at $p = 10$. What is the mean SNR of zero forcing at $p = 1$?

7. ◦ With $M = 64$ antennas and $h \sim \mathcal{CN}(0, R)$, find the standard deviation of
   $\|h\|^2/\mathbb{E}\|h\|^2$ when $R = I$ and when $R$ has four nonzero eigenvalues equal to 16. Does a
   keyhole channel harden? Use [channel hardening](/channel-hardening/).

8. ◦ Under the [pilot contamination](/pilot-contamination/) limit with matched filtering, what rate does a
   user get as $M \to \infty$ if its own large-scale gain is 1 and one other cell reuses its pilot with gain
   0.2? And with three other cells at gain 0.1 each?

9. ◦ For the [golden code](/golden-code/), compute $|\det X|^2$ for the symbols $(a, b, c, d) = (1, 1, 1, 0)$
   and $(2, 1, 0, 0)$, and check that both are at least the minimum $1/5$.

10. • For $H = \mathrm{diag}(\sigma_1, \sigma_2)$ with $\sigma_1 \ge \sigma_2$, show that water-filling puts
    power on the weaker mode exactly when $P > N_0(1/\sigma_2^2 - 1/\sigma_1^2)$, and state the general rule
    for $n$ modes. At what power does the second mode of exercise 1 switch on?

11. • Show that at low SNR the ergodic capacity with channel knowledge at the receiver is
    $\rho N_r/\ln 2$ to first order, and that beamforming on the strongest singular vector gives
    $\rho\,\mathbb{E}[\lambda_{\max}(HH^H)]/\ln 2$. For $2 \times 2$ i.i.d. Rayleigh fading, the unordered
    eigenvalues of $HH^H$ have the joint density proportional to $(\lambda_1 - \lambda_2)^2e^{-\lambda_1-\lambda_2}$.
    Find $\mathbb{E}[\lambda_{\max}]$ and the gain of channel knowledge at the transmitter in dB.

12. • Show that the zero-forcing noise factor of stream $k$ is $[(H^HH)^{-1}]_{kk} = 1/\|P^\perp_k h_k\|^2$,
    where $P^\perp_k$ projects onto the orthogonal complement of the other columns. Explain from this why
    the factor is at least $1/\|h_k\|^2$.

13. • Run zero-forcing [V-BLAST](/v-blast/) on $H = \begin{pmatrix} 1 & 0.5 \\ 0 & 1 \end{pmatrix}$. Which
    stream does it detect first, and what are the noise factors of the two streams? Compare with linear zero
    forcing and with the other order, and check that V-BLAST maximizes the smallest SNR.

14. • Show that $(H^HH + \sigma^2I)^{-1}H^H = H^H(HH^H + \sigma^2I)^{-1}$. Which side is cheaper for $n$
    streams and $m$ receive antennas, and which form remains valid when $n > m$?

15. • A real BPSK system after QR decomposition has $R = \begin{pmatrix} 2 & 1 & 0.5 \\ 0 & 1.5 & 1 \\ 0 &
    0 & 1 \end{pmatrix}$ and $z = Q^Ty = (-1.5, 0.5, 0.1)$, with metric $\|z - Rx\|^2$. Run the
    [K-best detector](/k-best-detector/) with $K = 1$ and $K = 2$, from the last row up, and compare with the
    ML vector.

16. • Run the two-dimensional [LLL algorithm](/lll-algorithm/) with $\delta = 3/4$ on the basis
    $b_1 = (1, 0)$, $b_2 = (0.9, 0.2)$. Give the reduced basis, the unimodular matrix, and the zero-forcing
    noise factors $[(B^TB)^{-1}]_{kk}$ before and after, as used in
    [lattice reduction aided detection](/lattice-reduction-aided-detection/).

17. • Two single-antenna users are served by $M = 2$ antennas with $h_1^H = (1, 0)$ and
    $h_2^H = (0.6, 0.8)$, total power $P = 10$ and $N_0 = 1$. Compute the SINR of each user and the sum rate
    for [maximum ratio transmission](/maximum-ratio-transmission/),
    [zero-forcing precoding](/zero-forcing-precoding/) and
    [regularized zero forcing](/regularized-zero-forcing-precoding/) with $\alpha = KN_0/P$, each scaled to
    total power $P$.

18. • In the [Kronecker model](/kronecker-channel-model/) with $R_t = R_r = \begin{pmatrix} 1 & r \\ r & 1
    \end{pmatrix}$, compute the high-SNR capacity loss $-\log_2\det R_t - \log_2\det R_r$ for $r = 0.5$ and
    $r = 0.9$. What is the rank of $H$ when $r = 1$?

19. • Two users in line of sight are at $0°$ and $10°$ from a half-wavelength uniform linear array. Compute
    the normalized inner product $|g_1^Hg_2|/M$ for $M = 8$ and $M = 32$, and say what it means for
    [favorable propagation](/favorable-propagation/).

20. • Two cells with one user each share a pilot of length $\tau = 2$, $p = 10$, gain 1 to the own base station
    and 0.1 across. Using the finite-$M$ formula of the pilot contamination entry, which here reduces to
    $\mathrm{SINR}(M) = M/(1.38 + 0.01M)$, check the constant 1.38 and find the $M$ at which the SINR reaches
    half of its limit.

21. • Write a program that estimates the ergodic capacity of a $2 \times 2$ i.i.d. Rayleigh channel at
    10 dB with equal power, and the mean of $\lambda_{\max}(HH^H)$, from 20000 draws with a seeded generator.
    Compare with 5.549 bits and with the exact value from exercise 11.

22. ★ Using outage, show that the Alamouti code reaches the optimal tradeoff $2(1 - r)$ on the $2 \times 1$
    channel, and that on the $2 \times 2$ channel its curve $4(1 - r)$ lies below $d^*(r)$ for every
    $0 < r \le 1$.

23. ★ For two streams $H = [h_1\ h_2]$ and SNR $\rho$, let $\mathrm{SINR}_1 = \rho h_1^H(I + \rho h_2h_2^H)^{-1}h_1$
    be the MMSE SINR of stream 1 with stream 2 as interference. Prove that
    $\log_2(1 + \mathrm{SINR}_1) + \log_2(1 + \rho\|h_2\|^2) = \log_2\det(I + \rho HH^H)$, and explain what it
    says about MMSE nulling with successive cancellation.

24. ★ For a fixed channel of full rank $n$, prove that the capacity gain of water-filling over equal power
    tends to 0 as $P \to \infty$, and that at low SNR the ratio of the two capacities tends to
    $n\sigma_1^2/\sum_i\sigma_i^2$.

25. ★ Simulate uncoded 4-QAM on a $4 \times 4$ i.i.d. Rayleigh channel at $E_s/N_0 = 15$ dB per stream and
    measure the vector error rate of zero forcing, MMSE, zero-forcing V-BLAST and exhaustive ML (256
    candidates) over 2000 channel uses with a seeded generator. Order the detectors and explain the order.

26. ★ Write a space-time block code as $X = \sum_k (A_k\,\mathrm{Re}\,s_k + B_k\,\mathrm{Im}\,s_k)$. Show
    that $XX^H = (\sum_k|s_k|^2)I$ for all symbols implies that the ML metric $\|Y - HX\|_F^2$ is a sum of
    terms each depending on one $s_k$, so ML decoding is symbol by symbol.
