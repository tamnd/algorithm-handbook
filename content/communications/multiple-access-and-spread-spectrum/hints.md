1. $G_p = 3.84 \times 10^6 / 15 \times 10^3 = 256$, or $10\log_{10}256 = 24.08$ dB. The margin is
$24.08 - 7 - 2 = 15.08$ dB: the jammer may be about 15 dB stronger than the signal.

6. The request uses $1/2 + 1/4 + 1/8 + 1/8 = 1$ of the tree, so it fits exactly. One assignment is
$C_{2,0}$, $C_{4,2}$, $C_{8,6}$ and $C_{8,7}$: no code is an ancestor of another. The code $C_{4,1} = (1, 1, -1, -1)$
blocks its children $C_{8,2}$ and $C_{8,3}$ (and its ancestors $C_{2,0}$ and $C_{1,0}$).

7. The exponents are $0, 3, 2, 4, 2, 3, 0$. Since 7 is prime and the roots differ, the cross-correlation
has magnitude $\sqrt 7 \approx 2.646$ at every lag, while the autocorrelation is 7 at lag 0 and 0 elsewhere.

10. The period is $1000010010110011111000110111010$. It has 16 ones and 15 zeros. Of the 16 runs, 8 have
length 1, 4 length 2, 2 length 3, one run of zeros has length 4 and one run of ones has length 5. The
two-valued autocorrelation follows from the shift-and-add property: $s \oplus s[\tau]$ is another shift of
$s$, which has one more 1 than 0.

14. $R = (1 - \rho)I + \rho\,\mathbf 1\mathbf 1^\top$ has eigenvalues $1 + 2\rho$ (once) and $1 - \rho$
(twice), so it is positive definite for $-1/2 < \rho < 1$. By the Sherman-Morrison formula,
$(R^{-1})_{kk} = (1 + \rho)/((1 - \rho)(1 + 2\rho))$, and the near-far resistance is its inverse,
$(1 - \rho)(1 + 2\rho)/(1 + \rho)$. At $\rho = 1/4$ it is $9/10$, a loss of 0.46 dB.

15. The matched filter has signal 1, interference $\rho^2 = 0.25$ and noise $0.25$: SINR 2 (3.01 dB). The
decorrelator has $(1 - \rho^2)/\sigma^2 = 3$ (4.77 dB). The MMSE detector has
$\frac{1}{\sigma^2}\bigl(1 - \rho^2A_2^2/(A_2^2 + \sigma^2)\bigr) = 4 \cdot 0.8 = 3.2$ (5.05 dB). The single
user has $1/\sigma^2 = 4$ (6.02 dB).

17. $E[T] = (2 + (2 - P_d)(q - 1)(1 + KP_{fa}))/(2P_d) = (2 + 1.05 \cdot 2045 \cdot 2)/1.9 = 2261.3$ dwells.
With $P_{fa} = 0$ it is $1131.2$: the false alarms double the mean time.

19. The bounds are $R_1 \le \log_2 21 = 4.392$, $R_2 \le \log_2 6 = 2.585$ and
$R_1 + R_2 \le \log_2 26 = 4.700$. Decoding user 2 first, with user 1 as noise, gives the corner
$(4.392, 0.308)$; decoding user 1 first gives $(2.115, 2.585)$. The pair $(2.350, 2.350)$ meets all three
bounds, so it lies on the face between the corners and is reached by time sharing between them.

20. The strong user decodes and removes the weak user's signal, then has $\log_2(1 + 0.1 \cdot 50) = \log_2 6 = 2.585$.
The weak user treats the strong user's signal as noise: $\log_2(1 + 4.5/1.5) = 2$. With time sharing the
weak user needs the fraction $t = 2/\log_2 6 = 0.774$ of the time, and the strong user gets
$0.226 \log_2 51 = 1.284$, about half of its NOMA rate.

21. Slot 4 holds only D, so D is decoded and its copy is removed from slot 1. Slot 1 then holds only A; removing
A's copy from slot 2 leaves B; removing B from slot 3 leaves C. The order is D, A, B, C, and all four packets
are recovered from four slots. With single copies, slot 1 holds A and D and is lost, so only B and C get through.

22. For unit vectors the inner product of $(0, 1, \varphi)$ and $(1, \varphi, 0)$ is
$\varphi/(1 + \varphi^2) = 1/\sqrt5$, and by symmetry every pair of lines meets at the same angle. The bound
is $(6 - 3)/(3 \cdot 5) = 1/5$, so $c_{\max} = 1/\sqrt5$ meets it. The sum of $v v^\top$ over the six unit
vectors is $2I = (K/N)I$.

23. With $S = [s_1, \ldots, s_K]$, the total is $\|S^\top S\|_F^2 = \|SS^\top\|_F^2 = \sum_i\lambda_i^2$ over
the $N$ eigenvalues of $SS^\top$, whose sum is $\operatorname{tr}(S^\top S) = K$. By Cauchy-Schwarz
$\sum_i\lambda_i^2 \ge K^2/N$, with equality when all $\lambda_i = K/N$. Removing the $K$ diagonal terms
leaves $K(K - 1)$ terms that sum to at least $K^2/N - K$, so the largest is at least
$(K - N)/(N(K - 1))$.

24. Each row of $W$ sums to 2, so $D = 3$ and $R = I + W/3$; Gershgorin's discs are centred at 1 with
radius $2/3$, so $R$ is positive definite. Then $b^\top Rb = 4 + \frac23(4 - 2c)$ for a cut of size $c$:
$20/3$, $4$ and $4/3$ for $c = 0, 2, 4$. The minimum is at $\pm(1, -1, 1, -1)$, the maximum cut.

25. The eigenvalues are $1 + (K - 1)\rho$ once and $1 - \rho$ with multiplicity $K - 1$. The second is in
$(0, 2)$ for $0 \le \rho < 1$; the first needs $\rho < 1/(K - 1)$. For $K = 5$ the iteration converges
exactly when $\rho < 1/4$.

26. With $\Lambda_1 = 0$, $\Lambda'(p) = 2\Lambda_2p + O(p^2)$, so the map is $f(p) = 2G\Lambda_2 p + O(p^2)$
near 0. Small erasure probabilities shrink only if the slope $2G\Lambda_2$ is below 1. For
$\Lambda = x^2$, $f(p) = 1 - e^{-2Gp} < 2Gp \le p$ for all $p > 0$ when $G \le 1/2$, and for $G > 1/2$ a
fixed point above 0 exists, so $G^* = 1/2$ exactly.
