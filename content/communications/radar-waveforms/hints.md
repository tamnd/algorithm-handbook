1. The signal to noise ratio is proportional to $\sigma/R^4$. A tenth of the cross section gives 10 dB, and
twice the range costs $40\log_{10} 2 = 12.04$ dB, so 7.96 dB at 80 km. For 13 dB the range grows by
$10^{7/40}$, to 59.85 km. The unambiguous range is $c/(2\,\mathrm{PRF}) = 75$ km.

3. $\tau = 10^{4/24} - 1 = 0.4678$ and $\alpha = 11.23$, against $\ln 10^4 = 9.21$: 0.86 dB higher. For
$N = 8$ at $10^{-2}$, $\tau = 10^{1/4} - 1 = 0.7783$, the sum is 16 and the threshold is 12.45, so 11 is not
detected and 13 is.

6. $f_b = 2RB/(cT_c) = 1.5$ MHz and the resolution is $c/(2B) = 1.0$ m. A complex rate of 10 MHz allows
beats up to 10 MHz, which is 200 m. At 77 GHz, $\lambda = 3.896$ mm, so 15 m/s gives $2v/\lambda = 7.70$ kHz.

10. $P(\Gamma(4, 1) > x) = e^{-x}(1 + x + x^2/2 + x^3/6)$; set it to $10^{-6}$ by bisection, which gives
$x = 21.35$. For case 2, solve $P(\Gamma(4, 1) > 21.35/(1 + S)) = 0.9$: $S = 10.51$ dB. Albersheim gives
7.96 dB for $N = 4$, about 0.3 dB below the exact steady value, and the fluctuation loss is
$10.51 - 8.25 = 2.26$ dB.

12. The test cell is exponential with mean $1 + S$, so
$P_d = E[e^{-\tau \Sigma/(1 + S)}]$, a product of the moment generating functions of the reference cells:
$P_d = (1 + \tau/(1 + S))^{-15} (1 + \tau(1 + I)/(1 + S))^{-1}$ with $\tau = 1.3714$. It gives 0.845, 0.543
and 0.119.

13. $T$ solves $(4 + T)(3 + T)(2 + T) = 2400$, so $T = 10.41$. The sorted window is
$(0.4, 0.8, 1.2, 9.0)$, so the OS threshold is $10.41 \cdot 1.2 = 12.50$, while the CA threshold is
$2.1623 \cdot 11.4 = 24.65$. OS detects 15 and CA does not. The mean thresholds are
$T(1/4 + 1/3 + 1/2) = 11.28$ and $4 \cdot 2.1623 = 8.65$.

15. The up-chirp moves the peak by $-\Delta R$ and the down-chirp by $+\Delta R$, so $R = 12\,011.25$ m and
$\Delta R = 11.25$ m. From $\Delta R = v f_c T/B$, $v = 150$ m/s, and the up-chirp shows the target closer,
so it approaches. The resolution is 75 m, so the shift is 0.15 of a cell.

19. $r = (4, -1, 0, 1)$ and $e = (1, -1, 1, 1)$. The solution of $Rg = e$ is
$g = (\tfrac17, -\tfrac17, \tfrac27, \tfrac27)$, $p = \tfrac67$ and $h = (\tfrac16, -\tfrac16, \tfrac13, \tfrac13)$.
The output is $(\tfrac16, 0, 0, 1, -\tfrac16, 0, \tfrac13)$: ISL $\tfrac16 = 1/p - 1$ ($-7.78$ dB), PSL
$-9.54$ dB, loss $\tfrac{9}{10}$ (0.46 dB). The matched filter has ISL $\tfrac14$ ($-6.02$ dB) and PSL
$-12.04$ dB, so the peak sidelobe got worse.

20. The mean variance is $\sigma^2 E[1/|d|^2]$ and the constant modulus value is $\sigma^2/E[|d|^2]$, so the
penalty is $E[|d|^2]\,E[1/|d|^2] \ge 1$ by Jensen's inequality for $1/x$. For 16-QAM with levels
$\pm 1, \pm 3$, $E[|d|^2] = 10$ and $E[1/|d|^2] = \tfrac{17}{90}$, so the penalty is $\tfrac{17}{9}$, or
2.76 dB.

21. $\alpha_N = N(e^{L/N} - 1) = L + L^2/(2N) + \dots$ with $L = \ln(1/P_{fa})$, and each term falls with $N$.
The needed signal to noise ratio is $\tau/(0.9^{-1/N} - 1) - 1$, against 21.14 dB for known noise. The loss
is 0.501 dB at $N = 61$ and 0.493 dB at $N = 62$.

22. Let $Y_1 \le \dots \le Y_N$ be the sorted reference cells. The spacings $Y_{m+1} - Y_m$ are independent
and exponential with rate $N - m$, so $E[e^{-sY_k}] = \prod_{m=0}^{k-1} (N - m)/(N - m + s)$. The test cell
is exponential, so $P_{fa} = E[e^{-TY_k}]$.

23. Write $\chi(\tau, \nu)$ as the Fourier transform in $t$ of $g_\tau(t) = u(t)\overline{u(t - \tau)}$.
By Parseval, $\int |\chi(\tau, \nu)|^2 d\nu = \int |u(t)|^2 |u(t - \tau)|^2 dt$, and integrating over $\tau$
gives $\left(\int |u|^2\right)^2 = E^2$.

24. Each term $a_{n+k}a_n$ is $\pm 1$, and there are $N - k$ of them. For the periodic sum, let $d$ be the
number of terms equal to $-1$; the product of all the terms is $(\prod_n a_n)^2 = 1$, so $d$ is even and
$c[k] = N - 2d \equiv N \pmod 4$. If $N \equiv 2 \pmod 4$ and $N > 2$, the Barker condition forces
$r[2] = r[N - 2] = 0$, so $c[2] = 0$, a contradiction.

25. With $f_t = f_s = f$, entry $pM + m$ of the steering vector is $z^{p + m}$ with $z = e^{j2\pi f}$, and
$p + m$ takes only the values $0, \dots, M + P - 2$. For distinct $z$ the vectors of powers form a
Vandermonde matrix, so $M + P - 1$ patches already span the space.
