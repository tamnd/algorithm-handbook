1. $H = (0.5,\ 1+0.5j,\ 1.5,\ 1-0.5j)$. Subcarrier 0 is weakest, with $|H[0]|^2 = 0.25$, so its SNR is
   $2.5$ (about 4 dB). A prefix of $L - 1 = 1$ sample is enough.

3. The samples are $(0,\ 1+j,\ 0,\ 1-j)$ with mean power 1 and peak 2, so the PAPR is 2 (3.01 dB). Of the
   16 blocks, 4 have PAPR 4, 4 have PAPR 2 and 8 have PAPR 1. The rule gives $1-(1-e^{-6.31})^{16} \approx
   0.0287$.

5. Moose measures the phase $2\pi\varepsilon(N+G)/N = 2\pi \cdot 0.875$, which wraps to $-2\pi\cdot 0.125$,
   and returns $-0.1$. Van de Beek measures $2\pi\varepsilon$ and wraps $0.7$ to $-0.3$. Schmidl-Cox measures
   $\pi\varepsilon = 0.7\pi$, inside $(-\pi, \pi)$, and returns 0.7, the right value.

6. $D \le N/L = 12.8$, so $D = 12$, or $D = 8$ as a power of two with overhead $1/8$. With all subcarriers
   as pilots the gain is $10\log_{10}(256/20) = 11.07$ dB. With 32 comb pilots and 20 taps it is only
   $10\log_{10}(32/20) = 2.04$ dB.

8. $\mu = 0.99240 - 0.08682j$ and $\nu = 0.00760 - 0.08682j$. Then $|\nu|^2/|\mu|^2 = \tan^2(5°) =
   0.007654$, an image rejection of 21.16 dB.

13. At offset $t = j/D$ from the left pilot the weights are $1-t$ and $t$, so the variance is
    $\sigma^2((1-t)^2 + t^2)$. Sum over $j = 0, \dots, D-1$ with $\sum j = D(D-1)/2$ and
    $\sum j^2 = D(D-1)(2D-1)/6$. The values are $3/4$, $11/16$ and $43/64$, and the limit is $2/3$.

15. The pilot covariance is $\begin{pmatrix}1.1 & 0.6561\\ 0.6561 & 1.1\end{pmatrix}$ and the cross term
    is $0.81$ for both pilots, so each weight is $0.81/1.7561 = 0.4612$ and the error is
    $1 - 2(0.4612)(0.81) = 0.2528$. Linear interpolation gives $0.2580$; one pilot gives weight
    $0.81/1.1 = 0.7364$ and error $0.4035$.

17. $E|I_0|^2 = \frac{1}{N^2}\left(N + 2\sum_{d=1}^{N-1}(N-d)e^{-\sigma^2 d/2}\right)$, since
    $\phi[n]-\phi[m]$ is Gaussian with variance $\sigma^2|n-m|$. For $N = 1024$ it is $0.98315$, against
    $0.98293$ from the approximation, so the ICI is $0.01685$ and the signal to ICI ratio is 17.66 dB. At
    $N = 2048$ the ICI is $0.03328$, about twice as much.

19. $U \ge \log(10^{-4})/\log(0.110) = 4.17$, so $U = 5$, which gives $0.110^5 \approx 1.6\times 10^{-5}$.
    The candidates are rotations of the same data, so their peaks are not independent, and the rule
    $1-(1-e^{-\gamma})^N$ is itself only approximate.

21. The prefix needs at least 5 μs, so the useful part needs at least 45 μs and $\Delta f \le 22.2$ kHz.
    The ICI bound $(\pi\varepsilon)^2/3 \le 0.01$ gives $\varepsilon \le 0.0551$, so
    $\Delta f \ge 1000/0.0551 = 18.1$ kHz. For example $\Delta f = 20$ kHz gives an overhead of
    $5/55 = 9.1$ percent and $\varepsilon = 0.05$, with ICI $0.0082$.

22. The values $S(m+\varepsilon)$ for $m = 0, \dots, N-1$ are the DFT of the sequence
    $e^{j2\pi\varepsilon n/N}/N$, up to the scale of the transform. Apply
    [Parseval's theorem](/parsevals-theorem/). The power that leaves the subcarrier is all in the others; none
    is lost.

23. Introduce $t$ and minimize $t$ subject to $|x[m] + (F_R^H C)[m]| \le t$ for every $m$. Each constraint
    bounds the norm of a vector of two real numbers that is affine in $(C, t)$, which is a second-order cone.
    A kernel method returns a feasible $C$, so its peak is at least the optimum.

24. In one run with seed 11 and 4000 trials, the measured variance was $3.35\times 10^{-4}$, against
    $3.32\times 10^{-4}$ from the formula. The formula is a small-error approximation, and a finite number of
    runs leaves a sampling error of a few percent.

25. Time samples of the channel come every $D_t T_s$ seconds and the Doppler spectrum occupies
    $[-f_D, f_D]$. The frequency samples come every $D_f\Delta f$ hertz and the delay profile has length
    $\tau_{\max}$. The bounds are $D_t \le 14$ and $D_f \le 14.18$.
