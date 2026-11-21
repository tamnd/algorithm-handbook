1. The squared gains are 4 and 0.25. For $P = 10$ the water level is $\mu = 7.125$, the powers are 6.875 and
   3.125, and $C = \log_2 28.5 + \log_2 1.78125 = 5.666$ bits, against 5.562 with equal power. For $P = 1$
   only the strong mode is used, $C = \log_2 5 = 2.322$, against 1.755.

3. $H^HH = \begin{pmatrix} 1 & 0.8 \\ 0.8 & 1 \end{pmatrix}$ and $[(H^HH)^{-1}]_{kk} = 1/0.36 = 2.778$, a
   noise enhancement of 4.44 dB, so the ZF SNR is 3.6 (5.56 dB). For MMSE, $P_{kk} = 1.1/0.57 = 1.930$ and
   the SINR is $1/(0.1 \cdot 1.930) - 1 = 4.18$ (6.21 dB).

5. Liang's rate $(m+1)/(2m)$ gives $3/4$ for 3 antennas, $2/3$ for 6 and $5/8$ for 8. The bound
   $2^{b(r-1)}$ with $r = N_t$ gives $2^3 = 8$ states for two antennas at 3 bits and $2^{4} = 16$ for three
   antennas at 2 bits.

8. The limit is $\beta_{jjk}^2/\sum_{l\ne j}\beta_{jlk}^2$: $1/0.04 = 25$, or $\log_2 26 = 4.70$ bits per
   channel use, and $1/0.03 = 33.3$, or $\log_2 34.3 = 5.10$ bits.

11. To first order, $\log_2\det(I + (\rho/N_t)HH^H) \approx (\rho/N_t)\,\mathrm{tr}(HH^H)/\ln 2$, and
    $\mathbb{E}\,\mathrm{tr}(HH^H) = N_tN_r$. Substituting $\lambda_{\min} = t$ and $\lambda_{\max} = t + u$
    gives $\mathbb{E}[\lambda_{\min}] = 1/2$, so $\mathbb{E}[\lambda_{\max}] = 4 - 1/2 = 3.5$. The gain is
    $3.5/2 = 1.75$, or 2.43 dB.

13. $(H^HH)^{-1}$ has diagonal $(1.25, 1)$, so stream 2 goes first with factor 1. After cancelling it, stream
    1 sees $\|h_1\|^2 = 1$, factor 1. Linear ZF has factors 1.25 and 1. The other order gives 1.25 for stream
    1 and $1/1.25 = 0.8$ for stream 2, so its worst factor is 1.25 against 1.

15. With $K = 1$: $x_3 = +1$ (0.81), then $x_2 = -1$ (1.0), then $x_1 = -1$ (1.0), total 2.81 for
    $(-1, -1, +1)$. With $K = 2$ the second survivor $x_3 = -1$ (1.21) leads to $(-1, +1, -1)$ with metric
    1.21, which is the ML vector.

16. Size reduction gives $b_2 = (-0.1, 0.2)$; the Lovász condition fails, so swap; size reduction with
    $\mu = -2$ gives $(0.8, 0.4)$, orthogonal to $(-0.1, 0.2)$. So $T = \begin{pmatrix} -1 & -1 \\ 1 & 2
    \end{pmatrix}$ with determinant $-1$. The factors go from $(21.25, 25)$ to $(20, 1.25)$.

17. $HH^H = \begin{pmatrix} 1 & 0.6 \\ 0.6 & 1 \end{pmatrix}$. MRT gives each user $5/(1 + 1.8) = 1.79$ and a
    sum rate of 2.96 bits; ZF gives 3.2 each and 4.14 bits; RZF with $\alpha = 0.2$ gives 3.5 each and 4.34
    bits.

20. $S = 1 + 0.1 + 1/(\tau p) = 1.15$ and $\sum\beta + 1/p = 1.1 + 0.1 = 1.2$, so the constant is 1.38. The
    limit is 100, and $M/(1.38 + 0.01M) = 50$ gives $M = 138$.

22. The Alamouti code gives one symbol per use on a scalar channel with gain $\|H\|_F^2$, a sum of $2N_r$
    unit exponentials. The outage event $\log_2(1 + \rho\|H\|_F^2/2) < r\log_2\rho$ needs
    $\|H\|_F^2 \lesssim \rho^{r-1}$, which has probability about $\rho^{-2N_r(1-r)}$. For $N_r = 1$ this is
    $d^*$; for $N_r = 2$, compare $4 - 4r$ with $4 - 3r$.

23. Factor $\det(I + \rho h_1h_1^H + \rho h_2h_2^H) = \det(A)\,(1 + \rho h_1^HA^{-1}h_1)$ with
    $A = I + \rho h_2h_2^H$ and $\det A = 1 + \rho\|h_2\|^2$. Decoding stream 1 by MMSE and then stream 2
    with no interference loses nothing.

24. The water-filling capacity is $\sum_i\log_2(\mu\sigma_i^2/N_0)$ with $\mu = (P + N_0\sum_i\sigma_i^{-2})/n$
    once all modes are on. Its difference from $\sum_i\log_2(1 + P\sigma_i^2/(nN_0))$ tends to 0 because
    $\mu/(P/n) \to 1$. At low SNR water-filling uses only $\sigma_1$.

25. In one run with seed 25, the vector error rates were 0.080 for ZF, 0.0325 for MMSE, 0.0105 for ZF V-BLAST
    and 0 for ML out of 2000 uses. ML has diversity 4 and the others less, and MMSE beats ZF at this SNR.
