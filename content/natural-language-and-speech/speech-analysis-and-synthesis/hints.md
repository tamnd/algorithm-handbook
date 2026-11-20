1. $m(1500) \approx 1290.6$ mel. The low octave spans $607.4 - 344.2 = 263.3$ mel and the high one $2840.0 - 2146.1 = 694.0$ mel. A filter bank spaced evenly in mels puts about 2.6 times as many filters in the high octave as in the low one, though in Hz the low filters are far narrower.

3. $y = (2, 2.1, 0.2, -2.8)$. The gain is $|1 - 0.95e^{-i\omega}|$: $0.05$, or $-26.02$ dB, at 0 Hz and $1.95$, or $+5.80$ dB, at the Nyquist frequency. It equals 1 when $\cos\omega = \alpha/2 = 0.475$, that is $\omega = 1.0758$ rad, or 2739.6 Hz.

5. A tube closed at one end resonates at $F_k = (2k-1)c/4L$. With $c/4L = 350/0.56 = 625$ Hz the resonances are 625, 1875 and 3125 Hz, close to the formants of a neutral vowel.

7. $(3.6, 1.2, 4.8, 2.4)$ rounds to $(4, 1, 5, 2)$, which is 12 frames. Without the factor there are 10.

9. The mean is 3.9. The squared deviations sum to 8.9, so $s = \sqrt{8.9/9} \approx 0.994$ and the half-width is $1.96 \times 0.994/\sqrt{10} \approx 0.62$. With ten ratings the score is known only to about $\pm 0.6$.

11. $m(8000) \approx 2840.0$, so the edges are at 0, 710, 1420, 2130 and 2840 mel, which are 0, 614.3, 1767.8, 3933.6 and 8000 Hz. Filter $j$ runs from edge $j-1$ to edge $j+1$, so the third filter is the widest: from 1767.8 to 8000 Hz, 6232.2 Hz at its base.

13. The denominator is $2(1 + 4) = 10$. Pad to $(2, 2, 2, 2, 5, 9, 9, 9, 9)$. The deltas are $(0.6, 1.7, 2.1, 1.8, 0.8)$; the largest is at the middle, where the sequence rises fastest.

16. $C = -e^{-0.0628} \approx -0.93910$, $B = 2e^{-0.0314}\cos(0.3142) \approx 1.84329$, $A \approx 0.09582$. Evaluate $A/(1 - Bz^{-1} - Cz^{-2})$ at $z = e^{i\pi/10}$; its magnitude is about 5.09. The choice of $A$ gives gain 1 at 0 Hz, not at the resonance.

19. $4 \cdot \tfrac{1}{2} - \ln 2 \approx 1.307$, which favours speech. It is zero when $\gamma/2 = \ln 2$, at $\gamma = 2\ln 2 \approx 1.386$.

20. Count by the number of pieces $k$. The letter sizes from $\{1, 2\}$ summing to 4 give one way for $k = 2$, three for $k = 3$ and one for $k = 4$. The phone sizes from $\{0, 1\}$ summing to 3 give $\binom{k}{3}$ ways. The total is $0 + 3 + 4 = 7$. With one letter each, $k = 4$ and there are $\binom{4}{3} = 4$ ways.

22. $k_1 = 1/2$ and $E_1 = 3/4$; then $k_2 = (0.1 - 0.5 \cdot 0.5)/E_1 = -1/5$, $a = (3/5, -1/5)$ and $E_2 = E_1(1 - k_2^2) = 18/25$. The poles have $r^2 = 0.2$, so $r \approx 0.447$, and $\cos\theta = 0.6/(2r)$. This gives about 1064 Hz with a bandwidth near 2050 Hz, far too wide for a formant; the usual bandwidth test rejects it.

23. The expected advance of bin 10 is $2\pi \cdot 10 \cdot 256/1024 = 5\pi$. The true advance is $2\pi \cdot 160 \cdot 256/16000$; reduce both modulo $2\pi$ and take the difference. Each radian of deviation is $16000/(2\pi \cdot 256) \approx 9.95$ Hz, and the deviation must lie in $(-\pi, \pi]$; the limit is $f_s/2H_a$. A 190 Hz tone lies 33.75 Hz above the centre, outside the range, so the deviation wraps.

24. The score of a vector $y$ is $\langle t, y\rangle^2/\langle y, y\rangle$. The adaptive search picks $a_2$ with gain 1. The fixed search on the residual $(1, -1, -2)$ then picks $f_2$ with gain $-1$, which leaves error 5. For the joint search, ask which pair spans a plane that contains $t$.

26. $W$ has rows $(1, 0)$, $(0, 1)$ and $(-1, 1)$. Then $W^\top \Sigma^{-1} W = \begin{pmatrix} 1+s & -s \\ -s & 1+s \end{pmatrix}$, with determinant $1 + 2s$, and the right-hand side is $(0, 2)$. The solution is $c = (2s, 2 + 2s)/(1 + 2s)$. The jump $2/(1 + 2s)$ shrinks toward 0, and $c$ tends to $(1, 1)$.
