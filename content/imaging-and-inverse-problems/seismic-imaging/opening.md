Seismic imaging maps the inside of the Earth from waves recorded at its surface. In exploration, a source such as an air gun or a vibrating truck sends sound into the ground, and thousands of receivers record the reflections from rock layers kilometres below; in earthquake seismology the sources are the earthquakes themselves. The data sets are large, often terabytes for one survey, and the physics is the wave equation in a medium whose velocities are themselves unknown. Seismic imaging has long been one of the main industrial uses of large parallel computers.

The work falls into two steps that feed each other. Velocity analysis estimates how fast waves travel at each depth, from the curvature of reflections in the data. Migration then moves each recorded reflection back to the point in the Earth where it happened, using that velocity model. The methods range from ray-based Kirchhoff migration to reverse time migration, which solves the full wave equation. Full waveform inversion fits the whole recorded wavefield by nonlinear least squares; it can resolve fine detail, but its objective has many local minima, and an initial model that is too far off leads to cycle skipping.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Models of the data.** The convolutional model of a seismic trace, the exploding reflector model and Geiger's method for locating earthquakes.
2. **Processing.** Normal moveout correction, common midpoint stacking, semblance velocity analysis, the Dix formula, the parabolic Radon transform, surface-related multiple elimination, and predictive and minimum entropy deconvolution.
3. **Migration.** Seismic migration and the imaging condition, Kirchhoff, Stolt, phase-shift, split-step Fourier and finite-difference migration, reverse time migration and least-squares migration.
4. **Inversion.** Traveltime tomography, full waveform inversion, the adjoint-state method for its gradient, and cycle skipping.
5. **Passive methods.** Seismic interferometry, which builds virtual sources from ambient noise.

## What to read meanwhile

The physics is the [wave equation](/wave-equation/) of Volume 12, solved by the [finite difference method](/finite-difference-method/); travel times obey the [eikonal equation](/eikonal-equation/), solved by the [fast marching method](/fast-marching-method/), also in Volume 12. Predictive deconvolution is [linear prediction](/linear-prediction/) of Volume 28, computed with the [Levinson-Durbin algorithm](/levinson-durbin-algorithm/) of Volume 11. Stolt and phase-shift migration work in the Fourier domain with the [fast Fourier transform](/fast-fourier-transform/). Full waveform inversion is a [nonlinear least squares](/nonlinear-least-squares/) problem, as treated in Volume 38, and the adjoint-state method computes its gradient in the same way as reverse-mode [automatic differentiation](/automatic-differentiation/) in Volume 25. Traveltime tomography can be linearized and solved with the [Kaczmarz method](/kaczmarz-method/) or [Tikhonov regularization](/tikhonov-regularization/) of Volume 12.
