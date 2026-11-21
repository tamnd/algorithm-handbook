An air traffic radar sends a pulse of a microsecond or more and listens for the echo. A light echo from an
aircraft at 50 km comes back after a third of a millisecond, many orders of magnitude weaker than the
pulse that left. The receiver must say whether the echo is there, how far away the aircraft is and how fast
it moves, while noise, rain, hills and other aircraft also send energy back. The
[radar range equation](/radar-range-equation/) gives the signal to noise ratio of the echo: it falls as
$1/R^4$, so twice the range costs 12.04 dB. Everything in the chapter is a way to get the most out of that
small echo.

The algorithms are those of a communication receiver in a new setting. The
[matched filter](/matched-filter/) gives the largest output signal to noise ratio in white noise, and the
output depends only on the energy of the pulse, not on its shape. So the radar is free to choose the shape
for other ends: a long pulse with a wide band gives both the energy of a long pulse and the range
resolution $c/(2B)$ of a short one. That is [pulse compression](/pulse-compression/). The
[ambiguity function](/ambiguity-function/) shows what the shape costs: its volume is the square of the
energy for every waveform, so lowering it in one place raises it somewhere else. The detectors follow
the [Neyman-Pearson](/neyman-pearson-lemma/) criterion: the largest probability of detection at a fixed
false alarm rate. Speed comes from the phase of the echo over many pulses, measured with the
[fast Fourier transform](/fast-fourier-transform/).

## What the chapter covers

The chapter is in five groups, read in order.

1. **The radar equation and the target.** The [radar range equation](/radar-range-equation/), the
   [Swerling target models](/swerling-target-models/) for echoes that fluctuate, and the
   [Albersheim equation](/albersheim-equation/), a fitted formula for the signal to noise ratio that a
   steady target needs, close to the exact values over most of its stated range and not outside it.
2. **Detection with a constant false alarm rate.** [CFAR detection](/cfar-detection/) sets the threshold
   from the cells around the one under test. [Cell-averaging CFAR](/cell-averaging-cfar/) keeps the false
   alarm rate exactly when the noise is homogeneous and exponential, and
   [ordered-statistic CFAR](/ordered-statistic-cfar/) resists other targets in the window.
3. **Pulse compression and frequency modulation.** [Pulse compression](/pulse-compression/), the
   [ambiguity function](/ambiguity-function/), the [linear FM pulse](/linear-frequency-modulation-pulse/)
   and its [range-Doppler coupling](/range-doppler-coupling/),
   [nonlinear FM](/nonlinear-frequency-modulation/), the
   [stepped frequency waveform](/stepped-frequency-waveform/) and [FMCW radar](/fmcw-radar/), the usual
   radar of cars.
4. **Phase codes and frequency codes.** [Phase-coded waveforms](/phase-coded-waveform/),
   [Barker codes](/barker-code/), the [Frank code](/frank-code/), [Costas arrays](/costas-array/) and the
   [mismatched filter](/mismatched-filter-design/) that lowers the sidelobes of a fixed code.
5. **Doppler processing and joint sensing.** [Moving target indication](/moving-target-indication/),
   [range-Doppler processing](/range-doppler-processing/),
   [space-time adaptive processing](/space-time-adaptive-processing/) for a radar on an aircraft, and
   [integrated sensing and communication](/integrated-sensing-and-communication/), where one signal
   carries data and senses the scene.

## A first reading

Read these in order:

1. [Radar range equation](/radar-range-equation/)
2. [Pulse compression](/pulse-compression/)
3. [Linear FM pulse](/linear-frequency-modulation-pulse/)
4. [Ambiguity function](/ambiguity-function/)
5. [Phase-coded waveform](/phase-coded-waveform/)
6. [Barker code](/barker-code/)
7. [Swerling target models](/swerling-target-models/)
8. [CFAR detection](/cfar-detection/)
9. [Cell-averaging CFAR](/cell-averaging-cfar/)
10. [Moving target indication](/moving-target-indication/)
11. [Range-Doppler processing](/range-doppler-processing/)
12. [FMCW radar](/fmcw-radar/)

They give the link budget, the two main families of waveforms, the detector and the Doppler processing of a
pulse radar, and the radar of a car. On a first pass, skip the advanced entries: the frequency and phase
codes after Barker, the mismatched filter, ordered-statistic CFAR and space-time adaptive processing. The
[Albersheim equation](/albersheim-equation/) is short and useful as soon as the Swerling models are read.

## Before you start

The chapter needs complex numbers, the Fourier transform and some probability. From Volume 28 you need the
[matched filter](/matched-filter/), [signal detection](/signal-detection/),
[autocorrelation](/autocorrelation/), [window functions](/window-functions/) and
[beamforming](/beamforming/). The [discrete Fourier transform](/discrete-fourier-transform/) and the
[fast Fourier transform](/fast-fourier-transform/) are in Volume 11. The detection entries use the
[Neyman-Pearson lemma](/neyman-pearson-lemma/) of Volume 33, and ordered-statistic CFAR uses
[binary search](/binary-search/) from Volume 5. Space-time adaptive processing solves its linear system
with the [Cholesky decomposition](/cholesky-decomposition/) of Volume 12, and the mismatched filter solves
a [least squares problem](/least-squares-problem/) from the same volume. The last entry assumes
[OFDM](/orthogonal-frequency-division-multiplexing/) from Chapter 44.5.
