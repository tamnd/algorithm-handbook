Take $c = 3 \times 10^8$ m/s throughout. Powers are square-law outputs in units of the mean noise power
unless an exercise says otherwise.

1. ◦ A radar gets an echo signal to noise ratio of 20 dB from a target of $\sigma = 1$ m$^2$ at 40 km. Use
the [radar range equation](/radar-range-equation/) to find the signal to noise ratio for a target of
0.1 m$^2$ at 40 km and for 1 m$^2$ at 80 km, and the range at which the 1 m$^2$ target gives 13 dB. What is
the unambiguous range at a pulse repetition frequency of 2 kHz?

2. ◦ One pulse goes through a square-law detector with $P_{fa} = 10^{-6}$. Give the threshold. For a
[Swerling 1](/swerling-target-models/) target, compute $P_d$ at a mean signal to noise ratio of 20 dB, and
the signal to noise ratio needed for $P_d = 0.5$.

3. ◦ [Cell-averaging CFAR](/cell-averaging-cfar/) uses $N = 24$ reference cells at $P_{fa} = 10^{-4}$. Find
the factor $\tau$ on the sum and the factor $\alpha = N\tau$ on the mean, and compare $\alpha$ with the
factor $\ln(1/P_{fa})$ of a detector that knows the noise power, in dB. Then take $N = 8$ and
$P_{fa} = 10^{-2}$, with the reference cells $(2, 1, 3, 2, 1, 2, 4, 1)$. Is a cell under test of 11
detected? One of 13?

4. ◦ A [pulse compression](/pulse-compression/) radar sends a linear chirp of length $T = 40\ \mu$s over
$B = 25$ MHz. Give the range resolution, the time bandwidth product and the compression ratio in dB, the
blind zone, and the approximate 3 dB width of the compressed pulse.

5. ◦ A [stepped frequency waveform](/stepped-frequency-waveform/) has $N = 32$ steps of $\Delta f = 2$ MHz
and a pulse interval of 50 μs. Give the range resolution, the unambiguous range, the longest pulse that
keeps the steps contiguous, and the time for one profile. Where does a target at 100 m appear? At a
carrier of 9 GHz, by how much does a target moving at 10 m/s shift the profile, in metres and in bins?

6. ◦ An [FMCW radar](/fmcw-radar/) sweeps $B = 150$ MHz in $T_c = 20\ \mu$s at 77 GHz. Find the beat
frequency of a target at 30 m, the range resolution, and the largest range for a complex sampling rate of
10 MHz. What Doppler shift does a target at 15 m/s give?

7. ◦ The [Barker code](/barker-code/) of length 5 is $(1, 1, 1, -1, 1)$. Compute its aperiodic
autocorrelation, its peak sidelobe level in dB and its merit factor $N^2/(2\sum_{k \ge 1} |r[k]|^2)$.

8. ◦ A radar at 10 GHz uses [moving target indication](/moving-target-indication/) at a PRF of 1 kHz. Give
the first blind speed. A target at 3.75 m/s has a Doppler shift of PRF/4; give the power response of the
two-pulse and the three-pulse cancellers at that shift. For clutter with a Gaussian spectrum of standard
deviation 5 Hz, compute the improvement factors of the two cancellers.

9. ◦ A [range-Doppler map](/range-doppler-processing/) at 10 GHz uses $P = 64$ pulses at a PRF of 5 kHz.
Give the Doppler bin width, the velocity per bin, the unambiguous velocity and the unambiguous range. In
which bin is a target at 20 m/s, and where does a target at 45 m/s appear?

10. • For $N = 4$ noncoherently integrated square-law pulses and $P_{fa} = 10^{-6}$, write a short program to
find the threshold and the signal to noise ratio per pulse for $P_d = 0.9$ on a
[Swerling 2](/swerling-target-models/) target. The exact value for a steady target is 8.25 dB. Compare both
with the [Albersheim equation](/albersheim-equation/) for $N = 4$, and give the fluctuation loss.

11. • For a Swerling 1 target and one pulse, [cell-averaging CFAR](/cell-averaging-cfar/) gives
$P_d = (1 + \tau/(1 + S))^{-N}$. With $N = 8$ and $P_{fa} = 10^{-4}$, find the signal to noise ratio for
$P_d = 0.9$, the value for a detector that knows the noise power, and the CFAR loss.

12. • A [CFAR](/cfar-detection/) detector averages $N = 16$ cells at $P_{fa} = 10^{-6}$, and the Swerling 1
target has the 23.15 dB that gives $P_d = 0.9$. One reference cell holds a second Swerling 1 target with a
mean power $I$ above the noise. Derive $P_d$ as a function of $I$ and compute it for $I$ of 10, 20 and
30 dB.

13. • [Ordered-statistic CFAR](/ordered-statistic-cfar/) with $N = 4$ and $k = 3$ is designed for
$P_{fa} = 10^{-2}$. Find $T$. With the reference cells $(1.2, 0.4, 9.0, 0.8)$, give the OS threshold and the
cell-averaging threshold at the same $P_{fa}$, and decide for a cell under test of 15. Give the mean
threshold of each in pure noise.

14. • For the rectangular pulse of length $T$ and unit energy, write the
[ambiguity function](/ambiguity-function/) in closed form. Integrate $|\chi|^2$ over $\nu$ first and then
over $\tau$, and check that the volume is $E^2$.

15. • A radar at 3 GHz sends an up-chirp and then a down-chirp, each of $T = 50\ \mu$s over $B = 2$ MHz. The
up-chirp places a target at 12 000.0 m and the down-chirp at 12 022.5 m. Use
[range-Doppler coupling](/range-doppler-coupling/) to find the range and the radial speed, and say whether
the target approaches. How large is the shift against the range resolution?

16. • The [Barker code](/barker-code/) of length 7 is $(1, 1, 1, -1, -1, 1, -1)$. Show that its periodic
autocorrelation is $(7, -1, \dots, -1)$, so it is a
[maximal length sequence](/maximal-length-sequence/) up to sign. Then compute the peak sidelobe of the
aperiodic autocorrelation for each of its seven cyclic shifts, as a
[phase-coded waveform](/phase-coded-waveform/) would use them.

17. • Write the [Frank code](/frank-code/) of 9 chips as phases in units of $2\pi/3$. Check that its periodic
autocorrelation is zero at every nonzero shift, and compute the magnitudes of its aperiodic sidelobes and its
peak sidelobe level in dB.

18. • Build the Welch [Costas array](/costas-array/) $f(i) = 2^i \bmod 5$ for $i = 1, \dots, 4$, and check
the Costas property by listing the differences $f(i + h) - f(i)$ for each $h$. Show that $(2, 1, 4, 3)$ is
not a Costas array. Then prove that the Welch construction gives a Costas array for every prime $p$ and
primitive root $g$.

19. • For the Barker code $s = (1, 1, -1, 1)$, design the least squares
[mismatched filter](/mismatched-filter-design/) of length $L = 4$ with the peak at $c = 3$, in exact
fractions. Give the output, the ISL, the PSL and the loss, and compare with the matched filter. Which
measure got worse?

20. • In OFDM radar, [integrated sensing and communication](/integrated-sensing-and-communication/) divides
each received symbol by the data symbol $d$, so the noise on that subcarrier has variance
$\sigma^2/|d|^2$. Show that the mean noise variance over random data is at least the value for constant
modulus symbols of the same mean power, and compute the penalty in dB for square 16-QAM.

21. ★ For cell-averaging CFAR at $P_{fa} = 10^{-6}$, show that $\alpha_N = N(P_{fa}^{-1/N} - 1)$ falls to
$\ln(1/P_{fa})$ as $N$ grows. Find the smallest $N$ for which the CFAR loss of exercise 11, at
$P_d = 0.9$ for a Swerling 1 target, is below 0.5 dB.

22. ★ Prove the false alarm probability $\prod_{m=0}^{k-1} (N - m)/(N - m + T)$ of
[ordered-statistic CFAR](/ordered-statistic-cfar/) in independent exponential noise, using the spacings of
the order statistics of exponential variables.

23. ★ Prove the volume property $\iint |\chi(\tau, \nu)|^2\, d\tau\, d\nu = E^2$ of the
[ambiguity function](/ambiguity-function/) for every pulse of finite energy.

24. ★ Show that the aperiodic autocorrelation of a binary sequence satisfies $r[k] \equiv N - k \pmod 2$,
and that its periodic autocorrelation satisfies $c[k] \equiv N \pmod 4$. Use these to prove that a
[Barker code](/barker-code/) of even length $N > 2$ has $N$ divisible by 4.

25. ★ In [space-time adaptive processing](/space-time-adaptive-processing/) with $M$ elements, $P$ pulses
and clutter on the ridge $f_t = f_s$, show that every clutter steering vector lies in a space of dimension
$M + P - 1$, and that the clutter covariance of enough distinct patches has exactly that rank.
