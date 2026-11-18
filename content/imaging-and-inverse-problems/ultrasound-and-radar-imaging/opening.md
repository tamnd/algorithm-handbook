Ultrasound and radar form images from echoes. A transducer or an antenna sends a pulse, the scene reflects it, and the time of each echo gives a distance. An array of receivers, or a single receiver moved along a path, turns these distances into an image by delaying and adding the recorded signals so that echoes from one point add up in phase. Medical ultrasound does this with a probe of a hundred or more elements; synthetic aperture radar does it with one antenna carried by an aircraft or satellite, and gets a resolution set by the length of the path rather than the size of the antenna.

Both fields work with coherent, complex-valued signals, which brings speckle, the grainy pattern of interfering echoes, and wrapped phases, which must be unwrapped before they can be read as distances or velocities. The chapter covers the image formation algorithms, from time-domain back-projection, which makes the fewest approximations but is slow, to the frequency-domain range-Doppler, chirp scaling and omega-k algorithms, which are fast under stated approximations, and the adaptive beamformers that trade robustness for resolution.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Ultrasound image formation.** The pulse-echo imaging model, dynamic receive focusing, B-mode image formation, synthetic transmit aperture imaging, the synthetic aperture focusing technique, the total focusing method and coherent plane-wave compounding.
2. **Beamforming and flow.** The Capon beamformer, delay-multiply-and-sum beamforming, the coherence factor, the Kasai autocorrelation estimator for blood velocity and the SVD clutter filter.
3. **Synthetic aperture radar.** SAR and its image formation, range cell migration, the range-Doppler, chirp scaling, omega-k and polar format algorithms, time-domain and fast factorized back-projection, phase gradient autofocus and inverse SAR.
4. **Interferometry and phase unwrapping.** SAR interferometry, phase unwrapping, the Goldstein branch cut algorithm and least-squares phase unwrapping.
5. **Speckle and wave-based imaging.** Speckle in coherent imaging, diffraction tomography, photoacoustic tomography and universal back-projection.

## What to read meanwhile

Delay-and-sum is written up in Volume 28 as [delay-and-sum beamforming](/delay-and-sum-beamforming/), with [beamforming](/beamforming/) in general and the [MUSIC algorithm](/music-algorithm/) for direction finding. Pulse compression is a [matched filter](/matched-filter/), also in Volume 28, and the frequency-domain SAR algorithms are built on the [fast Fourier transform](/fast-fourier-transform/) and the [nonuniform FFT](/nonuniform-fft/) of Volume 11, with [sinc interpolation](/sinc-interpolation/) from Volume 28 for resampling. Least-squares phase unwrapping solves a discrete [Poisson equation](/poisson-equation/) of Volume 12, and the SVD clutter filter uses the [singular value decomposition](/singular-value-decomposition/) there. The [wave equation](/wave-equation/) of Volume 12 is the model behind diffraction and photoacoustic tomography.
