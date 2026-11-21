1. The rows are $(1, 1, 1)$, $(-1, 1, 1)$, $(1, -1, 1)$ and $(1, 1, -1)$, and $X^TX = 4I$. So
$\hat h = X^Tv/4 = (1.075, 0.525, -0.275)$, and the error is $N_0\,\mathrm{tr}((X^TX)^{-1}) = 3N_0/4$,
which meets the bound $L^2N_0/T = 9N_0/12$.

3. The prefix needs at least $L - 1 = 1$ sample. $H_k = 1 + e^{-j2\pi k/4}$ gives $2$, $1 - j$, $0$ and
$1 + j$, so the zero-forcing tap $1/H_2$ does not exist. The MMSE error is
$J = \frac14\sum_k N_0/(|H_k|^2 + N_0) = \frac14(0.1/4.1 + 2 \cdot 0.1/2.1 + 1) = 0.2799$, an unbiased
SINR of 4.10 dB.

4. $x = (-1, 1.9, 1.29, -0.161)$: at $n = 2$ the value $-1 - 1.71 = -2.71$ is below $-2$, so 4 is added.
The samples are $y = (-1, 1, 3, 1)$, and the modulo folds $3$ to $-1$, so the decisions are $a$.

5. Reflect the zero at 2 to $1/2$: $f = \gamma(1 - 0.5z^{-1})^2$, and $|1 - 2e^{-j\omega}| =
2|1 - 0.5e^{-j\omega}|$ gives $\gamma = 2$, so $f = (2, -2, 0.5)$. Both energies are 8.25. The noise gain
falls from 1 to 0.25, a gain of 6.02 dB.

9. The inner product of the two columns is a sum of three terms $\pm1$, so it is odd. Then
$X^TX = \begin{pmatrix} 3 & c \\ c & 3\end{pmatrix}$ with $c \in \{\pm1, \pm3\}$ and the trace of the
inverse is $6/(9 - c^2)$. Twelve sequences have $c = \pm1$ and reach $3/4$; four have $c = \pm3$ and are
singular. The bound $2N_0/3$ is not reached by any $\pm1$ block of this length.

12. Here $a = 0.999842$ and $q = 3.158 \times 10^{-4}$. The predicted variance solves
$P = a^2PN_0/(P + N_0) + q$, a quadratic with the root $P \approx \sqrt{qN_0} + q(1 - N_0)/2$. The values
are $0.005763$ (predicted) and $0.005449$ (filtered), against $\sqrt{qN_0} = 0.005620$.

13. ZF: noise gain $1/(1 - 0.64)$, SNR 3.6 or 5.56 dB. MMSE-LE: $J = N_0/\sqrt{1.74^2 - 1.6^2} = 0.1462$,
unbiased SINR 5.84 or 7.66 dB. ZF-DFE: the geometric mean of $|H|^2$ is $h_0^2 = 1$ for a minimum-phase
channel, so the SNR is $1/N_0$, 10.00 dB. MMSE-DFE: $G = (1.74 + 0.6838)/2 = 1.2119$, $J = 0.0825$,
unbiased SNR 11.12 or 10.46 dB. MFB: $1.64/0.1$, 12.15 dB.

16. The system $b * y_1 - a * y_2 = 0$ has five equations in $(a_0, a_1, b_0, b_1)$ and rank 3, so its null
space is one-dimensional and spanned by $(1, 2, 1, -1)$: $h_1 = (1, 2)$ and $h_2 = (1, -1)$, up to a
scalar.

18. $A = H^TH/N_0 + I = \begin{pmatrix} 13.5 & 5 \\ 5 & 13.5\end{pmatrix}$, $\det A = 157.25$, so
$\varepsilon_1 = 13.5/157.25 = 0.08585$ and $\varepsilon_2 = 1/13.5 = 0.07407$. The sum is
$\log_2 157.25 = 7.297$ bits, or 3.648 per symbol. The last sample $0.5x_1 + w$ carries energy of $x_1$
with no interference from a following symbol; this edge gain per symbol vanishes as $m$ grows.

20. $|H|^2 + N_0 = a + 2R_1\cos\omega$. Use $\frac{1}{2\pi}\int d\omega/(a + b\cos\omega) =
1/\sqrt{a^2 - b^2}$ and the geometric mean $(a + \sqrt{a^2 - b^2})/2$ of $a + b\cos\omega$, with
$b = 2R_1$. The inequality is $\sqrt{a^2 - b^2} < (a + \sqrt{a^2 - b^2})/2$, that is,
$\sqrt{a^2 - b^2} < a$. On $(1, 1)$, $a^2 - b^2 = 4N_0 + N_0^2$, so $J_{\mathrm{LE}} \approx \sqrt{N_0}/2$
while $J_{\mathrm{DFE}} \approx N_0$.

21. The spectrum is $(K - N_0/|H|^2)^+$ with $|H|^2 = 1.64 - 1.6\cos\omega$, which is 0.04 at
$\omega = 0$. Solve for $K$ numerically: $K = 1.2252$, and the spectrum is zero for $|\omega| < 0.2286$, so
about 92.7% of the band is used. The capacity is 3.661 bits, against 3.599 bits for the white input. The
water-filling spectrum vanishes on an interval, so $\ln S_x$ is not integrable and the theorem must be
applied to an MMSE-DFE on the used band alone.

22. For independent $\pm1$ symbols, $Eq^4 = 3s^2 - 2\sum g_i^4$. Setting the gradient to zero gives
$g_i(3s - 2g_i^2 - 1) = 0$. The origin is a maximum with $J = 1$; $(\pm1, 0)$ and $(0, \pm1)$ are minima
with $J = 0$; $(\pm\frac12, \pm\frac12)$ are saddles with $J = \frac12$ and Hessian eigenvalues 8 and $-4$.
A finite equalizer restricts $g$ to the subspace $\{h * c\}$, where new local minima can appear.

23. $h_i = b_i * (1, -2)$ with $b_1 = (1, 1)$, $b_2 = (1, -1)$, and $h'_i = b_i * (2, -1)$. The factor
$2 - z^{-1}$ has the same magnitude as $1 - 2z^{-1}$ on the circle, and since it is common to both
subchannels, the cross spectra $H_iH_j^*\sigma^2$ do not change. The identifiability condition of the
method is exactly that the subchannels have no common zero.

24. Write $c = Hw$ with $H$ of size $4 \times 2$. The ratio $w^TAw/w^TBw$ is largest at the top generalized
eigenvalue of $(A, B)$. The best is $\Delta = 0$ with $w \propto (1, -0.3959)$ and the ratio 80.83, or
19.08 dB, against 20 (13.01 dB) for $w = (1, 0)$.
