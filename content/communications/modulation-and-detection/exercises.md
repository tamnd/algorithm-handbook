Unless an exercise says otherwise, the channel is the AWGN model of the chapter: coherent detection, perfect
synchronization, and complex noise $\mathcal{CN}(0, N_0)$ on each symbol, or real noise of variance
$\sigma^2 = N_0/2$ on a real signal.

1. ◦ Compute the bit error rate of BPSK, $Q(\sqrt{2E_b/N_0})$, at $E_b/N_0 = 6$ dB, using the
[Gaussian Q-function](/gaussian-q-function/). Then compute the Chernoff bound $\tfrac12 e^{-E_b/N_0}$ at the same
point. By what factor does the bound exceed the exact value?

2. ◦ Find the $E_b/N_0$ in decibels at which BPSK reaches $P_b = 10^{-6}$. Use $Q^{-1}(10^{-6}) = 4.7534$.

3. ◦ A channel is 1 MHz wide and has an SNR of 20 dB. Give its capacity by the
[Shannon-Hartley theorem](/shannon-hartley-theorem/). Then give the smallest $E_b/N_0$, in decibels, at which
any scheme can work reliably at a [spectral efficiency](/spectral-efficiency/) of 3 bits/s/Hz.

4. ◦ A link uses 16-QAM with a rate-$2/3$ code and root raised cosine pulses with roll-off $\beta = 0.35$, in a
band 5 MHz wide. Give the spectral efficiency, the symbol rate and the information bit rate. If the receiver
measures $E_s/N_0 = 12$ dB, what is the [$E_b/N_0$](/energy-per-bit-to-noise-density-ratio/) per information
bit?

5. ◦ On $[0, 2)$, let $s_1(t) = 1$ on $[0, 1)$ and $0$ elsewhere, $s_2(t) = 1$ on $[0, 2)$, and
$s_3(t) = 1$ on $[0, 1)$ and $-1$ on $[1, 2)$. Apply the [Gram-Schmidt process](/gram-schmidt-process/) in the
order $s_1, s_2, s_3$ to find an orthonormal basis, and give the coordinates of the three signals in the
[signal space](/signal-space-representation/). Check that $\int_0^2 (s_2 - s_3)^2\,dt$ equals the squared
distance between their coordinate vectors.

6. ◦ The 32-point cross constellation takes the 36 points $(x, y)$ with $x, y \in \{\pm1, \pm3, \pm5\}$ and
removes the four corners $(\pm5, \pm5)$. Compute its average energy, its $d_{\min}^2/E_s$ and its
peak-to-average power ratio, and compare the last two with 16-QAM, which has $0.4$ and $1.8$
([signal constellation](/signal-constellation/)).

7. ◦ A 16-QAM receiver uses the points $\{\pm1, \pm3\}^2$ and the per-axis Gray labels $00, 01, 11, 10$ for
the levels $-3, -1, 1, 3$, with the first two bits from the in-phase axis. The
[minimum-distance detector](/minimum-distance-detector/) receives $y = -1.4 + 2.3j$. Which point and which four
bits does it decide?

8. ◦ A [raised cosine](/raised-cosine-filter/) pulse with $\beta = 0.25$ carries 2.4 million symbols per second.
What band does it occupy at baseband and on a carrier? Compute $h(T/2)$ for the normalized pulse
$h(t) = \mathrm{sinc}(t/T)\cos(\pi\beta t/T)/(1 - (2\beta t/T)^2)$.

9. ◦ At $E_b/N_0 = 10$ dB, compute $P_b$ for coherent BPSK, [DPSK](/differential-phase-shift-keying/),
coherent BFSK and [noncoherent](/noncoherent-detection/) BFSK, using $Q(\sqrt{2\gamma_b})$,
$\tfrac12 e^{-\gamma_b}$, $Q(\sqrt{\gamma_b})$ and $\tfrac12 e^{-\gamma_b/2}$.

10. • BPSK sends $\pm1$ with $P(+1) = 0.8$ and $P(-1) = 0.2$ in real noise of variance $\sigma^2 = 0.25$. Find
the MAP threshold of [symbol detection](/symbol-detection/) and the probability of error with it, and compare
with the probability of error of the threshold $0$.

11. • For unit-energy 8-PSK at $E_s/N_0 = 15$ dB, compute the full union bound
$\sum_{k=1}^{7} Q(d_k/\sqrt{2N_0})$ with $d_k = 2\sin(\pi k/8)$, and the nearest-neighbour approximation
$2Q(d_1/\sqrt{2N_0})$. The exact [symbol error rate](/symbol-error-rate/) is $2.3395 \times 10^{-3}$. Which
terms of the bound matter?

12. • Compute the exact symbol error rate of square 16-QAM at $E_s/N_0 = 18$ dB, and the
[bit error rate](/bit-error-rate/) with [Gray labeling](/gray-labeling/) by the approximation $P_s/4$.

13. • A BPSK receiver samples $y_k = a_k + 0.3a_{k-1} - 0.2a_{k-2} + w_k$, with independent equiprobable
$a_k = \pm1$ and real noise of standard deviation $0.3$, and decides by the sign of $y_k$. Compute the worst-case
eye opening and the exact probability of error, and compare with the channel without
[intersymbol interference](/intersymbol-interference/).

14. • Show that $p(t) = \mathrm{sinc}(t/T)\,\mathrm{sinc}(\beta t/T)$ with $0 < \beta \le 1$ satisfies the
[Nyquist ISI criterion](/nyquist-isi-criterion/), and give its bandwidth. Compute $p(1.5T)$ for
$\beta = 0.5$.

15. • For the raised cosine with $\beta = 0.35$ and BPSK without noise, compute the worst-case
[eye](/eye-diagram/) opening $g(\delta) - \sum_{m \ne 0}|g(\delta + m)|$ at the timing offsets
$\delta = 0.1T$, $0.2T$ and $0.3T$. Compare with $\beta = 0.25$ ($0.652$, $0.289$, $-0.069$) and $\beta = 0.5$
($0.785$, $0.535$, $0.261$).

16. • Gray QPSK uses the points $(\pm1 \pm j)/\sqrt2$, where bit $b_0$ is $0$ for a positive real part and $b_1$
is $0$ for a positive imaginary part. The channel is $y = hx + w$ with $h = 0.8e^{j0.5}$ and $N_0 = 0.5$. For
$y = 0.3 - 0.9j$, compute the two LLRs $\ln(P(b = 0 \mid y)/P(b = 1 \mid y))$ by
[soft demapping](/soft-demapping/) over the four points, and check them against
$2\sqrt2\,\mathrm{Re}(\bar h y)/N_0$ and $2\sqrt2\,\mathrm{Im}(\bar h y)/N_0$.

17. • 4-PAM uses the levels $-3, -1, 1, 3$ with the Gray labels $00, 01, 11, 10$. For $y = 0.4$ and real noise of
variance $1$ ($N_0 = 2$), compute the exact LLRs of both bits and their
[max-log](/max-log-demapping/) values, and say which bit loses more by the approximation.

18. • GSM sends 270.833 kbit/s with [GMSK](/gaussian-minimum-shift-keying/) and $BT = 0.3$. Give the 3 dB
bandwidth $B$ of the Gaussian filter, its standard deviation $\sigma = \sqrt{\ln 2}/(2\pi B)$ in microseconds
and in bit periods, and the first spectral null of plain [MSK](/minimum-shift-keying/) at the same rate. If the
frequency pulse is truncated to $L = 4$ bit periods, how many pulses does the
[Laurent decomposition](/laurent-decomposition/) have, and how long is its main pulse $c_0$?

19. • In modified duobinary [partial response](/partial-response-signaling/), the precoder is
$p_k = b_k \oplus p_{k-2}$, the symbols are $a_k = 2p_k - 1$, and the channel gives $c_k = a_k - a_{k-2}$.
Starting from $p_{-1} = p_{-2} = 0$, encode the bits $1, 0, 1, 1, 0, 0, 1$, list $c_k$, and check that the rule
$\hat b_k = 1$ if $c_k \ne 0$ recovers the bits symbol by symbol.

20. ★ A ternary signal takes the values $-1, 0, 1$ with the priors $1/4, 1/2, 1/4$ in real noise with
$\sigma = 0.5$. Find the MAP thresholds and the probability of error, and compare with the ML thresholds
$\pm 0.5$.

21. ★ The 4+12 [APSK](/amplitude-and-phase-shift-keying/) constellation has 4 points on a ring of radius $r_1$
at the angles $\pi/4 + k\pi/2$ and 12 points on a ring of radius $r_2 = \gamma r_1$ at the angles
$\pi/12 + k\pi/6$, with unit average energy. Find the ring ratio $\gamma$ at which the nearest distance on the
inner ring equals that on the outer ring. Give $r_1$, $r_2$, $d_{\min}^2$ and the peak power, and check that the
distance between the rings is not smaller.

22. ★ For binary [faster-than-Nyquist signaling](/faster-than-nyquist-signaling/) with sinc pulses, an error
event $e$ has $d^2(\tau) = \sum_{i,j} e_ie_j\,\mathrm{sinc}((i - j)\tau)$, and the isolated error $e = (1)$ has
$d^2 = 1$. Find the $\tau$ at which the events $(1, -1)$ and $(1, -1, 1)$ fall to $d^2 = 1$, and explain why
they do not set Mazo's limit.

23. ★ Put a Maxwell-Boltzmann distribution $P(x) \propto e^{-\nu x^2}$ on 4-ASK $\{\pm1, \pm3\}$. Find $\nu$ such
that the entropy is $1.75$ bits, the probabilities, and the average energy. How many decibels of energy does it
save against uniform 4-ASK with the same spacing, and what does it give up?
([Probabilistic constellation shaping](/probabilistic-constellation-shaping/).)

24. ★ A [constant composition distribution matcher](/constant-composition-distribution-matching/) of length
$n = 4$ uses the composition with two 1s, one 3 and one 5, and indexes the sequences in lexicographic order
from 0. How many sequences are there, how many input bits $k$ does it take, and what is its rate loss against
the entropy of the composition? Which sequence does the input $101$ give, and what is the index of
$(3, 1, 5, 1)$? Compare the average energy with a uniform choice of $1, 3, 5$.
