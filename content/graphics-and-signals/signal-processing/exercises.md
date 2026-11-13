1. ◦ Compute the [discrete convolution](/discrete-convolution/) of $x = (1, 2, 3)$ with $h = (1, -1)$, and the [circular convolution](/circular-convolution/) of the two sequences padded to length 3. What is the smallest length at which the circular result equals the linear one?

2. ◦ A converter samples at 48 kHz with no anti-alias filter in front of it. Tones at 30 kHz, 50 kHz and 100 kHz reach its input. At what frequencies between 0 and 24 kHz do they appear in the samples? Use [aliasing](/aliasing/).

3. ◦ Which of the impulse responses $h[n] = 1/(n + 1)$ and $h[n] = 1/(n + 1)^2$, for $n \ge 0$ and zero before, give a [BIBO stable](/bibo-stability/) system? For the unstable one, give a bounded input whose output is unbounded.

4. ◦ The two-point average $y[n] = \tfrac12 (x[n] + x[n-1])$ is an [FIR filter](/fir-filter/). Find its [frequency response](/frequency-response/), its magnitude at $\omega = \pi/2$ and at $\omega = \pi$, and its group delay.

5. ◦ Find the poles of $H(z) = 1/(1 - 1.5 z^{-1} + 0.56 z^{-2})$. Is the causal [IIR filter](/iir-filter/) with this [transfer function](/transfer-function/) stable?

6. ◦ A filter has $M = 33$ taps. With the cost per output sample of the [overlap-add method](/overlap-add-method/), $(N \log_2 N + N)/(N - M + 1)$, which FFT length $N$ among 64, 128, 256, 512 and 1024 is cheapest, and what does it cost? Compare with the direct form.

7. ◦ A [Butterworth filter](/butterworth-filter/) with cutoff $\Omega_c$ must be at least 40 dB down at $2\Omega_c$. What is the least order $N$, and how far down is the response at $2\Omega_c$ with that order?

8. ◦ A noncausal [Wiener filter](/wiener-filter/) works on DFT bins. In one bin the signal power is 9 and the noise power is 1; in another both are 1. Give the gain and the mean-square error of the estimate in each bin.

9. ◦ The pulse $s = (1, 2, -1)$ is to be found in white noise of variance $\sigma^2$. Give the impulse response of the [matched filter](/matched-filter/) and its output SNR at the end of the pulse. What SNR does the averaging filter $(1, 1, 1)$ give at the same sample?

10. ◦ A uniform line of $M = 8$ sensors at half-wavelength spacing is steered to broadside by [delay-and-sum beamforming](/delay-and-sum-beamforming/). At what angle from broadside is the first null of its beam pattern?

11. ◦ Among all solutions of $x_1 + 2x_2 = 2$, find the one of least $\ell_1$ norm, as [basis pursuit](/basis-pursuit/) would, and the one of least $\ell_2$ norm. Which one is sparse?

12. • The [sampling theorem](/sampling-theorem/) needs $f_s > 2B$ for a sinusoid at frequency $B$. Show that at $f_s = 2B$ the samples of $\cos(2\pi B t + \varphi)$ depend only on $\cos\varphi$. Give two different sinusoids at $B$ with the same samples, and one whose samples are all zero.

13. • A record of 1024 samples is split into segments of 256 samples with 50% overlap for the [Welch method](/welch-method/). How many segments are there? How many does Bartlett's method, with no overlap, use?

14. • The periodic Hann window of length $N = 12$ is used in a [short-time Fourier transform](/short-time-fourier-transform/). For which hops $R \in \{3, 4, 5, 6\}$ do the shifted windows add to a constant (the COLA condition), and what is the constant?

15. • Find the weights of the [Savitzky-Golay filter](/savitzky-golay-filter/) that fits a quadratic to 7 points ($m = 3$, $p = 2$) and returns the value at the center. What is its noise gain $\sum c_i^2$?

16. • The FIR filter $1 - 2.5 z^{-1} + z^{-2}$ has a zero outside the unit circle. Find the [minimum phase](/minimum-phase/) filter with the same magnitude response, and compare the partial energies $\sum_{k \le n} h[k]^2$ of the two filters.

17. • The input of a two-tap [LMS](/lms-algorithm/) filter has correlation matrix $R = \begin{bmatrix} 1 & 0.9 \\ 0.9 & 1 \end{bmatrix}$. For which step sizes $\mu$ does the mean of the taps converge? Which $\mu$ makes the fastest and the slowest mode decay at the same rate, and what is that rate per sample?

18. • Audio at 22.05 kHz is converted to 16 kHz by [polyphase resampling](/polyphase-resampling/). Give the factors $L$ and $M$ in lowest terms. With a prototype low-pass filter of $K = 24L$ taps at the upsampled rate, about how many multiplies does each output sample cost?

19. • Apply a [median filter](/median-filter/) of window 3 and a moving average of window 3 to $x = (1, 1, 1, 9, 1, 5, 5, 5)$, at the interior samples $n = 1, \ldots, 6$. What happens to the spike and to the step in each output?

20. • A Haar step by the [lifting scheme](/lifting-scheme/) computes $d[i] = x[2i+1] - x[2i]$ and then $s[i] = x[2i] + \lfloor d[i]/2 \rfloor$. Apply it to $x = (3, 7, 1, 1, 6, 2, 9, 4)$, write the inverse steps, and check that they give $x$ back exactly. How do the $s[i]$ relate to the pair averages?

21. • Run the first steps of the [YIN algorithm](/yin-algorithm/) on $x[n] = \sin(\pi n/2)$ with a frame of $W = 8$ samples starting at $n = 0$ and lags up to $T = 4$. Give $d(\tau)$ and $d'(\tau)$ for $\tau = 0, \ldots, 4$, the lag chosen with threshold 0.1, and the pitch for a sample rate $f_s$.

22. • Three unit vectors in the plane at angles 0°, 120° and 240° form the columns of a $2 \times 3$ matrix $A$. Find the coherence $\mu$ of $A$, the largest $s$ for which the condition $\mu < 1/(2s-1)$ of [orthogonal matching pursuit](/orthogonal-matching-pursuit/) holds, and the spark of $A$. Give a 2-sparse $x$ for which $Ax$ also has a 1-sparse solution.

23. • Use [Prony's method](/prony-method/) with $p = 2$ to fit $x[t] = h_1 z_1^t + h_2 z_2^t$ to the four samples $x = (2, 3, 5, 9)$. Give the prediction coefficients, the roots $z_1, z_2$ and the amplitudes.

24. ★ For white Gaussian noise each interior bin of a [periodogram](/periodogram/) is exponential with mean $\sigma^2$, so it exceeds three times its mean with probability $e^{-3} \approx 0.05$. If $K$ independent periodograms are averaged, what is that probability as a function of $K$? What is the least $K$ that brings it below $10^{-3}$?

25. ★ The Cesàro means of the Fourier series of a square wave that jumps between $-1$ and $1$ are its convolutions with the Fejér kernel. Prove that they never leave $[-1, 1]$, so that the overshoot of the [Gibbs phenomenon](/gibbs-phenomenon/) disappears. What is the price paid near the jump?

26. ★ The continuous Hann window on $[0, T]$ is $w(t) = \tfrac12 - \tfrac12 \cos(2\pi t/T)$. Write its Fourier transform as a sum of three shifted sinc functions and show that its side lobes fall like $1/f^3$. How many dB per octave is that, against the rectangular window? Use [window functions](/window-functions/) for the definitions.

27. ★ A [Kalman filter](/kalman-filter/) tracks the random walk $x_t = x_{t-1} + q_t$ from $y_t = x_t + r_t$, with noise variances $q$ and $r$. Find the steady-state prior variance $P^-$ and gain $K$, show that the steady filter is an exponential moving average, and find the limits of $K$ as $r \to 0$ and as $q/r \to 0$. Check your formula with $q = r = 1$.

28. ★ A stationary signal has autocorrelation $r[k] = \rho^{|k|}$ with $|\rho| < 1$. Show that for every order $p \ge 1$ the [linear prediction](/linear-prediction/) normal equations give $a_1 = \rho$ and $a_2 = \cdots = a_p = 0$, with prediction error $1 - \rho^2$. What does this say about the reflection coefficients that the Levinson-Durbin recursion produces?
