## What to remember

- The [sampling theorem](/sampling-theorem/) recovers a signal band-limited to $B$ from samples at $f_s > 2B$. It fails at $f_s = 2B$ for a sinusoid at $B$. Below the rate, [aliasing](/aliasing/) gives different signals the same samples.
- A [linear time-invariant system](/linear-time-invariant-system/) is a convolution with its impulse response, [BIBO stable](/bibo-stability/) exactly when that response is absolutely summable. An [FIR filter](/fir-filter/) is always stable and has exact linear phase when its taps are symmetric. A causal [IIR filter](/iir-filter/) in lowest terms is stable exactly when its poles are inside the unit circle.
- The DFT turns [circular convolution](/circular-convolution/) into a product, equal to the linear one at length $N + M - 1$ or more. [Overlap-add](/overlap-add-method/) and [overlap-save](/overlap-save-method/) filter a stream this way at $O(\log M)$ operations per output.
- The [Butterworth filter](/butterworth-filter/) is maximally flat, the [bilinear transform](/bilinear-transform/) maps it to digital form after prewarping, and [Parks-McClellan](/parks-mcclellan-algorithm/) gives the minimax linear-phase FIR filter on its frequency grid.
- The [periodogram](/periodogram/) is asymptotically unbiased but not consistent: on white Gaussian noise each bin's standard deviation equals its mean at every length. The [Welch method](/welch-method/) averages segments and trades resolution for variance. [MUSIC](/music-algorithm/) and [ESPRIT](/esprit/) find tones exactly from the exact covariance, and consistently from estimates.
- [Wiener](/wiener-filter/) has the least mean-square error among linear filters. [LMS](/lms-algorithm/) reaches it in the mean for $0 < \mu < 2/\lambda_{\max}$ under the independence assumption, [RLS](/rls-algorithm/) is exact least squares after every sample, and the [Kalman filter](/kalman-filter/) is the exact posterior for linear Gaussian models.
- The sparsest solution of a linear system is NP-hard to find in general. [Basis pursuit](/basis-pursuit/) is exact under the null space property, it and [OMP](/orthogonal-matching-pursuit/) are exact when the coherence is $\mu < 1/(2s - 1)$, and random matrices satisfy the [restricted isometry property](/restricted-isometry-property/) with high probability from $O(s \log(n/s))$ rows.
- YIN outside its exact cases, the musical noise of [spectral subtraction](/spectral-subtraction/), [empirical mode decomposition](/empirical-mode-decomposition/) and the local optima of [Griffin-Lim](/griffin-lim-algorithm/) are judged by measurement.

| Method | Setting | Cost | Guarantee |
|---|---|---|---|
| FIR, direct form | $M$ taps | $\Theta(M)$ per sample | exact, always stable |
| Overlap-add, overlap-save | $M$ taps, FFT length $N$ | $O(\log M)$ per output | exact in exact arithmetic |
| Parks-McClellan | $I$ rounds, grid of $G$ | $O(ILG)$ | minimax on the grid |
| [Polyphase resampling](/polyphase-resampling/) | ratio $L/M$, $K$ taps | at most $\lceil K/L \rceil$ per output | equals upsample, filter, downsample |
| [Lifting scheme](/lifting-scheme/) | $T$ steps | $\Theta(TN)$, in place | exact inverse, also on integers |
| Periodogram | stationary signal | $\Theta(L \log L)$ | asymptotically unbiased, not consistent |
| Welch | $K$ segments of $L$ | $\Theta(KL \log L)$ | variance about $1/K$ as large |
| MUSIC | $m \times m$ covariance | $\Theta(m^3 + Lm)$ | exact on exact covariance |
| [Levinson-Durbin](/levinson-durbin-recursion/) LPC | order $p$, frame $N$ | $O(Np + p^2)$ per frame | stable predictor |
| [YIN](/yin-algorithm/) | frame $W$, lags $T$ | $O(WT)$ per frame | exact in special cases, else measured |
| LMS | $M$ taps | $2M + 1$ multiplies per sample | mean converges iff $0 < \mu < 2/\lambda_{\max}$ |
| RLS | $M$ taps | $O(M^2)$ per sample | exact weighted least squares |
| Kalman | state $n$, data $k$ | $O((n + k)^3)$ per step | exact for linear Gaussian models |
| OMP | $m \times n$, $s$ steps | $\Theta(smn)$ | exact if $\mu < 1/(2s - 1)$ |

: Signal processing methods by cost and guarantee. Costs are worst case in the real RAM.

## Choosing a method

Filter a stream by the direct form when $M$ is small or no delay is allowed, and by overlap-add or overlap-save for longer filters. Use an IIR filter when a sharp response must be cheap and linear phase is not needed. Design FIR filters by Parks-McClellan when the specification is in bands, and IIR filters from an analog prototype through the bilinear transform. To keep peaks while smoothing, use [Savitzky-Golay](/savitzky-golay-filter/); to remove spikes and keep steps, use the [median filter](/median-filter/).

To change the rate, use polyphase resampling. For the spectrum of a long noisy record, use Welch with a window chosen for the side-lobe level needed; for a few tones in a short record, use a subspace method.

For noise with known statistics, use the Wiener filter, or the Kalman filter when a state-space model is known. When they are unknown or drift, adapt: LMS when cost matters and the input is close to white, RLS when speed of convergence matters. For signals sparse in a known basis, recover from random measurements by basis pursuit, or by OMP or [ISTA](/iterative-shrinkage-thresholding/) when time matters more.
