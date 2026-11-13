A signal is a sequence of samples: the pressure at a microphone, the voltage of an antenna, a sensor reading taken at regular times. Signal processing filters such sequences, measures their frequencies, and recovers what noise hides. It runs in every phone call, audio player, radio receiver and radar.

The theory rests on a few facts. A band-limited signal is determined by samples taken at more than twice its highest frequency, which is why audio CDs sample at 44.1 kHz for hearing that ends near 20 kHz; frequencies above half the sampling rate fold back as aliases. A linear time-invariant system is described completely by its impulse response, and its output is the convolution of the input with that response. The Fourier transform turns convolution into multiplication, so the fast Fourier transform filters a block of $n$ samples in $O(n \log n)$ time, and the overlap-add and overlap-save methods do the same for a stream. Filters are finite (FIR), always stable and easy to make linear-phase, or recursive (IIR), sharper for the same cost but stable only when their poles lie inside the unit circle.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Sampling.** The sampling theorem, the Nyquist rate, aliasing, sinc interpolation, and sample-rate conversion with polyphase filters.
2. **Systems and transforms.** LTI systems, impulse and frequency response, the z-transform, transfer functions, stability, and the discrete-time Fourier transform.
3. **Filters.** FIR and IIR filters, Butterworth design and the bilinear transform, the Parks-McClellan algorithm, Savitzky-Golay smoothing, and FFT convolution.
4. **Spectra and time-frequency analysis.** Windows and spectral leakage, the periodogram and Welch's method, MUSIC and ESPRIT, the short-time Fourier transform, wavelets, the Hilbert transform and pitch detection.
5. **Estimation and adaptive filters.** Correlation, the matched filter, linear prediction, the Wiener and Kalman filters, LMS and RLS adaptation, and beamforming.
6. **Sparse recovery.** Compressed sensing, basis pursuit, orthogonal matching pursuit, iterative shrinkage-thresholding and phase retrieval.

## What to read meanwhile

Chapter 11.3 has the transforms: the [discrete Fourier transform](/discrete-fourier-transform/), the [fast Fourier transform](/fast-fourier-transform/), [convolution](/convolution/) and the [convolution theorem](/convolution-theorem/), [Parseval's theorem](/parseval-theorem/) and the [fast wavelet transform](/fast-wavelet-transform/). Chapter 24.3 has [filter banks](/filter-bank/), [subband coding](/subband-coding/) and the [modified discrete cosine transform](/modified-discrete-cosine-transform/) of audio coders.

Linear prediction solves a Toeplitz system by the [Levinson-Durbin recursion](/levinson-durbin-recursion/), and the Parks-McClellan algorithm runs the exchange of the [Remez algorithm](/remez-algorithm/) on cosine polynomials. The Kalman filter solves the linear Gaussian case of [filtering](/filtering/) in Chapter 25.5; the [extended Kalman filter](/extended-kalman-filter/) is its nonlinear form. LMS is [stochastic gradient descent](/stochastic-gradient-descent/) on the squared error, and iterative shrinkage-thresholding is the [proximal gradient method](/proximal-gradient-method/), accelerated in [FISTA](/fista/). The [reconstruction filter](/reconstruction-filter/) and [antialiasing](/antialiasing/) entries of Chapter 28.1 apply sampling theory to images.
