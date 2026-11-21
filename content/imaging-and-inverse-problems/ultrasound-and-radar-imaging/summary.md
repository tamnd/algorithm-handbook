## What to remember

- An echo at time $t$ comes from depth $z = ct/2$. A focused beam is about $\lambda F$ wide. In radar the range resolution after pulse compression is $c/(2B)$.
- Fully developed speckle has a Rayleigh amplitude with mean over standard deviation $\sqrt{\pi/(4 - \pi)} = 1.91$ and an exponential intensity with ratio $1$. Averaging $L$ independent looks raises the ratio by $\sqrt L$.
- Transmit focusing costs firings. Synthetic transmit aperture and the total focusing method use $M$ firings and cost $O(M^2 n^2)$; plane-wave compounding uses $N$ angles at $O(NMn^2)$. SAFT needs a scan step of at most $\lambda/4$ to avoid grating lobes.
- Capon uses $w = R^{-1}a/(a^{\mathsf H}R^{-1}a)$, which keeps a unit gain in the look direction and minimizes the output power. The coherence factor $|\sum s_i|^2/(M\sum|s_i|^2)$ has the mean $1/M$ on noise. Delay-multiply-and-sum costs $O(M)$ per pixel through $((\sum r_i)^2 - \sum r_i^2)/2$.
- Kasai's estimator gives $v = \frac{c\,\mathrm{PRF}}{4\pi f_0}\arg R_1$ and aliases beyond $v_a = c\,\mathrm{PRF}/(4f_0)$. The SVD clutter filter separates tissue and blood exactly only when they are orthogonal in space and time.
- A SAR antenna of length $L$ gives an azimuth resolution of about $L/2$, a far-field estimate, and needs $\mathrm{PRF} > 2V/L$. Range cell migration, about $\lambda^2 R_0 f^2/(8V^2)$ at Doppler frequency $f$, must be corrected.
- Back-projection is exact for any known path up to interpolation, at $O(P n^2)$ for $P$ pulses. The FFT algorithms are fast but assume a straight path (range-Doppler, chirp scaling, omega-k) or plane waves (polar format). Phase gradient autofocus is a heuristic.
- An interferogram gives height through the height of ambiguity $h_{2\pi} = \lambda R \sin\theta/(pB_\perp)$, with $p = 2$ for repeat-pass data. Unwrapping by integration is exact when every true difference is below $\pi$ (Itoh's condition). Least-squares unwrapping is a Poisson problem and is not congruent, the $L^1$ problem is a minimum cost flow, and the $L^0$ problem is NP-hard.
- Universal back-projection is exact for a closed spherical detector surface in 3D. Diffraction tomography holds for weak scatterers (the Born approximation) and covers spatial frequencies up to $\sqrt2 k_0$ in transmission and $2k_0$ in reflection.

| Method | Setting | Time | Status |
|---|---|---|---|
| [Plane-wave compounding](/plane-wave-compounding/) | $N$ angles, $M$ elements | $O(NMn^2)$ | delay-and-sum per angle |
| [Total focusing method](/total-focusing-method/) | full matrix capture | $O(M^2 n^2)$ | transmit and receive focus at every pixel |
| [Delay-multiply-and-sum](/delay-multiply-and-sum/) | $M$ elements | $O(Mn^2)$ | nonlinear, homogeneous of degree 1 |
| [SAR back-projection](/sar-backprojection/) | any known path | $O(P(n^2 + FN\log(FN)))$ | exact up to range interpolation |
| [Fast factorized back-projection](/fast-factorized-backprojection/) | path close to a line | $O(N^2\log N)$ | approximate, set by polar grid sampling |
| [Range-Doppler algorithm](/range-doppler-algorithm/) | straight path, stripmap | $O(MN(\log(MN) + K))$ | approximate at wide beams |
| [Chirp scaling algorithm](/chirp-scaling-algorithm/) | straight path, stripmap | $O(MN\log(MN))$ | approximate, no interpolation |
| [Omega-k algorithm](/omega-k-algorithm/) | straight path, constant speed | $O(MN(\log(MN) + K))$ | exact up to stationary phase and interpolation |
| [Polar format algorithm](/polar-format-algorithm/) | spotlight | $O(MN(\log(MN) + K))$ | exact under the plane-wave approximation |
| [Phase gradient autofocus](/phase-gradient-autofocus/) | after any of the above | $O(IMN\log N)$ | heuristic phase estimate |

: Beamformers and SAR focusing algorithms, with the costs of the entries: $n \times n$ pixels, $M$ elements or pulses, $N$ range samples, $P$ pulses, $K$ interpolator taps, $F$ the upsampling factor, $I$ iterations.

## Choosing a method

For a standard ultrasound frame, dynamic receive focusing is enough. When the frame rate matters, use plane-wave compounding: nine angles at 60 mm take 0.70 ms instead of 9.97 ms for 128 focused lines. In nondestructive testing, where the part does not move, use the total focusing method. Add an adaptive beamformer when clutter and side lobes limit the image more than noise does.

For blood flow, use Kasai's estimator on focused data with a PRF set by the deepest vessel and the fastest flow. On plane-wave ensembles, filter the clutter with the SVD first; its cut-off ranks are chosen from the data, not by a theorem.

For SAR, use back-projection when the path is not straight or as the reference, and its fast factorized form for large images. On a straight stripmap path, the range-Doppler algorithm is the simplest, chirp scaling avoids interpolation, and omega-k stays accurate at wide beams. For spotlight data, use the polar format algorithm on scenes small enough for its plane-wave approximation. Run phase gradient autofocus when the motion data are not good to a fraction of a wavelength.

For interferometry, unwrap with branch cuts when the result must be congruent, and with least squares when a smooth answer is enough.
