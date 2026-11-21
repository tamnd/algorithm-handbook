1. ◦ A channel has $L = 3$ taps and the training block is $x = (1, 1, 1, -1, 1, 1)$. Write the $4 \times 3$
pilot matrix $X$ of [least squares channel estimation](/least-squares-channel-estimation/), with rows
$(x[n], x[n-1], x[n-2])$ for $n = 2, \ldots, 5$, and compute $X^TX$. For the samples
$v = (1.35, -0.85, 0.25, 1.85)$, find $\hat h$ and the mean squared error of the estimator in terms of $N_0$.

2. ◦ The channel is $h = (1, -0.8)$. Give the first four taps of the infinite-length
[zero-forcing equalizer](/zero-forcing-equalizer/) and its noise gain $\sum_k |c_k|^2$, also in dB.

3. ◦ A single-carrier block of $N = 4$ symbols with a cyclic prefix crosses the channel $h = (1, 1)$, with
$E_s = 1$ and $N_0 = 0.1$. How long must the prefix be? Compute the four DFT values $H_k$, say why the
zero-forcing form of [frequency-domain equalization](/frequency-domain-equalization/) fails, and compute the
MMSE error $J$ and the unbiased SINR $1/J - 1$ in dB.

4. ◦ Run [Tomlinson-Harashima precoding](/tomlinson-harashima-precoding/) for 2-PAM (modulo into $[-2, 2)$)
on the channel $f = (1, 0.9)$ with the symbols $a = (-1, +1, -1, +1)$. Give the transmitted values $x_n$,
the noiseless received samples $y_n = x_n + 0.9x_{n-1}$, and the decisions after the receiver's modulo.

5. ◦ The channel $h = (1, -2.5, 1)$ has its zeros at $2$ and $0.5$. Find the minimum-phase channel $f$
with $|F| = |H|$ on the unit circle and $f_0 > 0$, which the
[whitened matched filter](/whitened-matched-filter/) produces. Check that $\|f\|^2 = \|h\|^2$, and compare
the noise gain $1/f_0^2$ of a zero-forcing DFE with one feedforward tap on $f$ and on $h$.

6. ◦ Count the trellis states and the branches per symbol of the [Viterbi equalizer](/viterbi-equalizer/)
for 8-PSK on a channel with $L = 4$ taps. How many states does delayed decision-feedback sequence
estimation with $\mu = 1$ keep? How many does
[reduced-state sequence estimation](/reduced-state-sequence-estimation/) keep for 16-QAM on $L = 3$ taps
with partitions of sizes $J_1 = 4$ and $J_2 = 2$, against the full trellis?

7. ◦ Compute the dispersion constant $R_2 = E|a|^4/E|a|^2$ of the
[constant modulus algorithm](/constant-modulus-algorithm/) for 4-PAM with points $\{\pm1, \pm3\}$ and for
8-PAM with points $\{\pm1, \pm3, \pm5, \pm7\}$, and again after scaling each alphabet to unit energy.

8. ◦ In the [soft interference cancellation equalizer](/soft-interference-cancellation-equalizer/) with
$h = (1, 0.5)$, $\sigma^2 = 0.5$ and the window $(y_n, y_{n+1})$, the neighbours are known exactly:
$x_{n-1} = +1$ and $x_{n+1} = -1$. For $y_n = 1.7$ and $y_{n+1} = -0.1$, compute the extrinsic LLR
$L_e(x_n)$.

9. • Take $L = 2$ and $N_p = 4$ BPSK pilots, so $X$ has $m = 3$ rows. Show that no $\pm1$ sequence gives
orthogonal columns. Among the 16 sequences, find the smallest value of $\mathrm{tr}((X^TX)^{-1})$, how many
sequences reach it and how many make $X^TX$ singular. Compare with the bound $L^2N_0/T$.

10. • Prove that the error covariance of [LMMSE channel estimation](/lmmse-channel-estimation/),
$(R_h^{-1} + X^HX/N_0)^{-1}$, is never larger, in the positive semidefinite order, than the LS error
covariance $N_0(X^HX)^{-1}$. Evaluate both mean squared errors for $R_h = \frac12 I_2$, $X^HX = 4I_2$ and
$N_0 = 0.1$.

11. • Run [Kalman channel tracking](/kalman-channel-tracking/) on one tap with the static model ($a = 1$,
$Q = 0$), prior variance $P_0$ and pilots of unit modulus. Show that after $n$ pilots the error variance is
$1/(1/P_0 + n/N_0)$, the same as the LMMSE estimate from all $n$ pilots at once. Give the value for
$P_0 = 1$, $N_0 = 0.1$, $n = 9$, and say what happens to the Kalman gain.

12. • For one tap with $f_DT = 0.004$, the AR(1) model has $a = J_0(2\pi f_DT)$ and $q = 1 - a^2$. With a
pilot of unit modulus at every symbol and $N_0 = 0.1$, find the steady-state predicted and filtered error
variances of the Kalman filter, and show that both are close to $\sqrt{qN_0}$ when $q \ll N_0$.

13. • On $h = (1, -0.8)$ with $E_s = 1$ and $N_0 = 0.1$, compute the output SNR in dB of the infinite-length
zero-forcing equalizer, the unbiased SINR of the infinite-length
[MMSE linear equalizer](/mmse-linear-equalizer/), the SNR of the infinite-length ZF-DFE, the unbiased SNR
of the infinite-length MMSE-DFE, and the matched filter bound.

14. • Take $h = (1, 1)$ and BPSK. Show that the infinite-length zero-forcing equalizer does not exist, and
compute the infinite-length MMSE error for $N_0 = 0.1$, $E_s = 1$. Then show that the minimum squared
distance of the [Viterbi equalizer](/viterbi-equalizer/) is $8 = 4\|h\|^2$, so that sequence detection loses
nothing in distance on this channel.

15. • A two-tap equalizer for $h = (1, 0.5)$ sees $r_n = (y_n, y_{n-1})$ with $E_s = 1$ and $N_0 = 0.1$,
and is trained by LMS for the delay 0, as in [adaptive equalization](/adaptive-equalization/). Find the
input correlation matrix, its eigenvalues, the largest step size for convergence of the mean taps, the
Wiener taps and the minimum mean squared error.

16. • Two subchannels see the same input with no noise: $y_1 = (1, 1, -1, 2)$ and $y_2 = (1, -2, 2, -1)$,
from 2-tap subchannels. Use the cross relation $h_2 * y_1 = h_1 * y_2$ to recover $(h_1, h_2)$ up to a
scalar, as a linear system in four unknowns. What is its rank?

17. • A [fractionally spaced equalizer](/fractionally-spaced-equalizer/) has one tap on each of the two
subchannels $h_1 = (1, 2)$ and $h_2 = (1, -1)$. Find the taps $(c_1, c_2)$ that force the combined
response $c_1h_1 + c_2h_2$ to $(1, 0)$ and to $(0, 1)$. Which delay has the smaller noise gain
$c_1^2 + c_2^2$?

18. • Check the finite form of the [canonical MMSE-DFE theorem](/mmse-dfe-canonical-theorem/) for
$h = (1, 0.5)$, $E_s = 1$, $N_0 = 0.1$ and a block of $m = 2$ symbols with the full $3 \times 2$ convolution
matrix. Compute $\varepsilon_1$, $\varepsilon_2$ and $\sum_k\log_2(E_s/\varepsilon_k)$, and explain why the
rate per symbol exceeds the infinite-length value 3.4963 bits.

19. • A blind [per-survivor processing](/per-survivor-processing/) receiver for BPSK starts from the estimate
$\hat f_0$. Show that the receiver started from $-\hat f_0$ gives, at every step, the same metrics with
every path negated, and that the LMS updates keep this symmetry. Conclude what a blind start cannot
decide.

20. ★ For a real two-tap channel with $R_0 = h_0^2 + h_1^2$, $R_1 = h_0h_1$, $E_s = 1$ and $a = R_0 + N_0$,
prove that the infinite-length MMSE linear equalizer has $J_{\mathrm{LE}} = N_0/\sqrt{a^2 - 4R_1^2}$ and the
infinite-length MMSE-DFE has $J_{\mathrm{DFE}} = 2N_0/(a + \sqrt{a^2 - 4R_1^2})$. Show that
$J_{\mathrm{DFE}} < J_{\mathrm{LE}}$ unless $R_1 = 0$, and that on $h = (1, 1)$ the ratio
$J_{\mathrm{LE}}/J_{\mathrm{DFE}}$ grows like $1/(2\sqrt{N_0})$ as $N_0 \to 0$.

21. ★ Find the [water-filling](/water-filling-power-allocation/) input spectrum for $h = (1, -0.8)$,
$N_0 = 0.1$ and power $E_s = 1$: the water level $K$, the band where the spectrum is positive and the
capacity in bits per symbol. Compare with the rate $\log_2(G/N_0)$ of the MMSE-DFE with a white input, and
say what the canonical theorem needs to reach capacity here.

22. ★ For real BPSK and a combined response $g = (g_1, g_2)$, the constant modulus cost is
$J(g) = E(q^2 - 1)^2$ with $q = g_1a_1 + g_2a_2$. Show that $J = 3s^2 - 2(g_1^4 + g_2^4) - 2s + 1$ with
$s = g_1^2 + g_2^2$. Find every stationary point, classify each one and give its cost. Explain why the
false minima of CMA, as in the entry's example on $h = (1, 0.5)$, must come from the finite equalizer and
not from the cost itself.

23. ★ Show that the subchannel pairs $h_1 = (1, -1, -2)$, $h_2 = (1, -3, 2)$ and $h'_1 = (2, 1, -1)$,
$h'_2 = (2, -3, 1)$ give the same second-order statistics of the two outputs for every white input. Find
the common zero and state the general construction. Why does this not contradict the
[Tong-Xu-Kailath method](/tong-xu-kailath-identification/)?

24. ★ A [channel-shortening equalizer](/channel-shortening-equalizer/) with two taps $w$ acts on
$h = (1, 0.5, 0.25)$, and the target window holds 2 consecutive taps of $c = h * w$ starting at the delay
$\Delta$. Maximize the shortening SNR (window energy over wall energy) over $w$ and $\Delta \in \{0, 1, 2\}$
as a generalized eigenvalue problem. Give the best $\Delta$, $w$ up to scale and the ratio in dB, and
compare with no equalizer.
