Unless an exercise says otherwise, the loops are the second-order digital PLL of the chapter, with the
detector output $e_k$, the update $s_k = s_{k-1} + K_ie_k$, $\psi_{k+1} = \psi_k + K_pe_k + s_k$, and a detector
gain of 1. The SNR is $E_s/N_0$ per symbol, and phases are in radians.

1. ◦ Design a [phase-locked loop](/phase-locked-loop/) with $B_LT = 0.01$ and $\zeta = 1/\sqrt2$ by the rule
$K_p = \tfrac83 B_LT$, $K_i = \tfrac{32}{9}(B_LT)^2$, and check the stability conditions $0 < K_p < 2$,
$K_i > 0$, $2K_p + K_i < 4$. What phase error does the loop leave for a constant frequency offset of $0.002$
rad per symbol, and for a frequency ramp of $10^{-6}$ rad per symbol squared? What error would a first-order
loop with the same $K_p$ and a sine detector leave for the frequency offset?

2. ◦ A residual frequency offset of $0.002$ cycles per symbol is left uncorrected. How far does it turn the
constellation over a block of 64 symbols, and does a noiseless QPSK point stay inside its decision region? For
16-QAM, whose corner points tolerate $0.2946$ rad, after how many symbols do the first decisions go wrong?
([Carrier recovery](/carrier-recovery/).)

3. ◦ Compute the [modified Cramér-Rao bound](/modified-cramer-rao-bound/) $1/(2N\,\mathrm{SNR})$ on the carrier
phase for $N = 64$ known symbols at $E_s/N_0 = 8$ dB, as a variance and as a standard deviation in degrees.
How many symbols would a standard deviation of $1°$ need?

4. ◦ For [frequency offset estimation](/frequency-offset-estimation/) from $N = 64$ samples at 5 dB, compute the
bound $3/(2\pi^2\,\mathrm{SNR}\,N(N^2 - 1))$ in cycles per symbol squared, its standard deviation, and that
standard deviation in hertz at 1 million symbols per second.

5. ◦ A [frame synchronizer](/frame-synchronization/) searches for a 31-symbol sync word with a normalized
correlation whose false-alarm probability per position is $(1 - \lambda)^{L-1}$. Which threshold $\lambda$
gives $10^{-4}$? A hard-decision detector instead demands an exact match of all 31 bits; with what probability
does random data match the word at one position?

6. ◦ Compute the squaring loss of the [squaring loop](/squaring-loop/) at $E_s/N_0 = 8$ dB for BPSK,
$1 + N_0/2$, and for QPSK, $1 + 4.5N_0 + 6N_0^2 + 1.5N_0^3$, with $E_s = 1$. Then give the predicted phase
variances $B_LT\,N_0\,L$ for $B_LT = 0.01$.

7. ◦ The carrier phase is $\theta = 2.5$ rad and a [Costas loop](/costas-loop/) starts at the estimate $0$.
List the lock points of the BPSK, QPSK and 8-PSK loops that lie in $(-\pi, \pi]$, and give the one nearest to
the start in each case.

8. ◦ A cubic [Farrow interpolator](/farrow-interpolator/) uses the samples $x_{-1}, x_0, x_1, x_2 = 2, -1, 0, 3$ at
the times $-1, 0, 1, 2$. Compute the coefficients $c_0, \ldots, c_3$ of the Lagrange cubic
$y(\mu) = c_0 + c_1\mu + c_2\mu^2 + c_3\mu^3$ and the interpolated value at $\mu = 0.25$, by
[Horner's rule](/horner-rule/).

9. • Show that the closed loop has the characteristic polynomial $z^2 + (K_p + K_i - 2)z + (1 - K_p)$. For the
design value $B_LT = 0.03$, compute $K_p$ and $K_i$ and the exact noise bandwidth
$B_LT = \tfrac12\sum_k h_k^2$, where $h_k$ is the response of $\psi$ to a unit impulse in the phase.

10. • A first-order loop has the loop SNR $\rho = 4$ and $B_LT = 0.01$. Compute the mean number of symbols
between [cycle slips](/cycle-slip/) from $\pi^2\rho I_0(\rho)^2/(2B_LT)$ and from the approximation
$\pi e^{2\rho}/(4B_LT)$. A QPSK loop with a fourth-power detector behaves as if $\rho$ were divided by $16$:
repeat the computation for a loop SNR of $40$.

11. • The samples $r = 1,\ 0.6 + 0.8j,\ -0.3 + 0.9j,\ -0.9 + 0.2j,\ -0.7 - 0.6j$ come from a tone in noise.
Compute the phase differences $\arg(r_{t+1}\bar r_t)$, the weights $6(t + 1)(N - 1 - t)/(N(N^2 - 1))$ of the
[Kay estimator](/kay-frequency-estimator/), and the estimate in radians and in cycles per sample. Compare with
the unweighted mean of the differences.

12. • A noiseless tone with $\nu = 0.12$ cycles per symbol enters the
[Luise and Reggiannini estimator](/luise-reggiannini-estimator/) with $L = 8$ and $N = 32$. What does it
return, and why? What is the largest $L$ for which it returns $0.12$?

13. • A [Gardner detector](/gardner-timing-error-detector/) sees the real samples $y_{k-1} = 0.9$,
$y_{k-1/2} = 0.2$ and $y_k = -1.1$. Compute $e_k = y_{k-1/2}(y_{k-1} - y_k)$. For a raised cosine with
$\beta = 0.35$, compute $A = 4\sin(\pi\beta/2)/(\pi(4 - \beta^2))$, the gain $K_D = 2\pi A$ and the first-order
gain $K_p = 4B_LT/((1 + 2B_LT)K_D)$ for $B_LT = 0.01$. Repeat the last two for the
[Mueller and Müller detector](/mueller-muller-timing-recovery/), with $K_D = 2\cos(\pi\beta)/(1 - 4\beta^2)$.

14. • The four partial sums of the [Oerder and Meyr estimator](/oerder-meyr-timing-estimation/) are
$P_0, P_1, P_2, P_3 = 100, 80, 70, 95$. Compute $X = (P_0 - P_2) + j(P_3 - P_1)$ and the delay
$\hat\tau = -\arg X/(2\pi)$ in symbol periods.

15. • The sync word is $s = (+1, +1, -1)$, $E_s = N_0 = 1$, and the received samples are
$y = (0.9, -0.2, 1.1, 0.8, -1.0, 2.6, 1.9, -0.4)$. For each offset $\mu = 0, \ldots, 5$, compute the correlation
$\sum_i s_iy_{\mu+i}$ and the [Massey metric](/massey-frame-synchronization/)
$\sum_i s_iy_{\mu+i} - \tfrac12\sum_i \ln\cosh(2y_{\mu+i})$. Which offsets do the two rules pick, and why do they
differ?

16. • A Barker-13 preamble is received with a residual frequency offset of $0.1$ rad per symbol. By how much
does the peak of [preamble correlation detection](/preamble-correlation-detection/) shrink, using the factor
$|\sin(L\Delta\phi/2)/(L\sin(\Delta\phi/2))|$, and what is that in decibels of correlation power?

17. • For [symbol timing recovery](/symbol-timing-recovery/) with a raised cosine of roll-off $0.35$, compute
$\xi = \tfrac1{12} + \beta^2(\tfrac14 - \tfrac2{\pi^2})$ and the timing bound
$1/(8\pi^2\xi L_0\,\mathrm{SNR})$ for $L_0 = 200$ symbols at 12 dB. What loop bandwidth corresponds to this
block length?

18. • The [Rife and Boorstyn estimator](/rife-boorstyn-frequency-estimator/) with $N = 32$ and a grid of $K = 128$
points is stopped at the best grid point. Treat the grid error as uniform over one grid step and compute its
variance in rad$^2$. Compare it with the bound $6/(\mathrm{SNR}\,N(N^2 - 1))$ at 10 dB, and with the measured
ratio of $12.1$ (seed 2, 400 tones).

19. ★ Derive the stability conditions of exercise 9 from the Jury test for a quadratic. Find the gains that put
both poles at $z = 0$, compute the phase errors for an input $\theta_k = 0.5 + 0.1k$ from $\psi_0 = s_{-1} = 0$,
and compute the noise bandwidth of this loop. Why is it not used for tracking in noise?

20. ★ The unweighted estimator averages the $N - 1$ phase differences of a tone, which telescopes to
$(\arg r_{N-1} - \arg r_0)/(N - 1)$. At high SNR each phase has the variance $1/(2\,\mathrm{SNR})$. Find the
ratio of its variance to the bound $6/(\mathrm{SNR}\,N(N^2 - 1))$, and evaluate it for $N = 32$.

21. ★ A known word of length $L$ is correlated against pure circular Gaussian noise, and
$\rho = |\sum_i \bar c_ir_i|^2/(\sum_i|c_i|^2\sum_i|r_i|^2)$. Show that $\rho$ has the Beta$(1, L - 1)$
distribution, so $P(\rho > \lambda) = (1 - \lambda)^{L-1}$, and compute $\lambda$ for $L = 63$ and a
false-alarm probability of $10^{-5}$.

22. ★ [Decision-directed carrier recovery](/decision-directed-carrier-recovery/) for 64-QAM on the grid
$\{\pm1, \pm3, \pm5, \pm7\}^2$ with boundaries at the even integers keeps every noiseless decision right only
while the phase error is small. Find the largest such error, which point sets it, and the second smallest
tolerance among the points.
