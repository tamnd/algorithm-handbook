1. ◦ In the [pulse-echo model](/pulse-echo-imaging/) with $c = 1540$ m/s, an echo arrives 26 µs after the pulse. How deep is the reflector? What is the highest pulse repetition frequency that lets every echo from depths up to 150 mm return before the next pulse?

2. ◦ [B-mode image formation](/b-mode-image-formation/) maps an envelope $A$, relative to the brightest one, to $d = \max(-D, 20\log_{10} A)$ dB and then to the gray level $\lfloor 255(d + D)/D + 1/2 \rfloor$. With $D = 60$ dB, give the gray levels of $A = 0.5$, $0.05$ and $0.001$.

3. ◦ In fully developed [speckle](/speckle/), the intensity is exponential with mean $\langle I\rangle$. What fraction of the pixels is brighter than $2\langle I\rangle$? What is the ratio of mean to standard deviation of the average of 4 independent looks?

4. ◦ A [synthetic aperture radar](/synthetic-aperture-radar/) on a satellite at $V = 7500$ m/s has a 4 m antenna and a chirp of bandwidth 150 MHz. Give the range resolution, the azimuth resolution and the lowest pulse repetition frequency that samples the Doppler band.

5. ◦ The true phase $(0, 1.5, 3.0, 4.5, 6.0, 7.5)$ is wrapped to $(-\pi, \pi]$. Give the wrapped values and unwrap them by integrating wrapped differences, as in [phase unwrapping](/phase-unwrapping/). Then do the same for the pair $(0, 3.5)$ and say what goes wrong.

6. ◦ A Doppler system has $f_0 = 3$ MHz, $\mathrm{PRF} = 4$ kHz and $c = 1540$ m/s. Using the [Kasai autocorrelation estimator](/kasai-autocorrelation-estimator/), find the aliasing velocity, the phase step between pulses for blood at $0.3$ m/s, and the velocity that the estimator reports for blood at $0.7$ m/s.

7. ◦ Four delayed channels are $s = (2, 1, 1, 0)$. Compute the [coherence factor](/coherence-factor/), the delay-and-sum value, and the weighted value $\mathrm{CF} \cdot \sum s_i$.

8. ◦ With [dynamic receive focusing](/dynamic-receive-focusing/), an element sits 3 mm from the centre of the array and $c = 1.54$ mm/µs. Compute its extra receive delay $(\sqrt{z^2 + x^2} - z)/c$ for foci at $z = 10$ mm and $z = 30$ mm.

9. ◦ A differential interferogram at $\lambda = 5.6$ cm shows three fringes over a subsiding area, as described in [SAR interferometry](/sar-interferometry/). How much has the ground moved along the line of sight?

10. • An airborne SAR has $\lambda = 3$ cm, $V = 200$ m/s, a 1.5 m antenna and a target at $R_0 = 10$ km. Compute the synthetic aperture length $\lambda R_0/L$, the integration time, the Doppler bandwidth, the azimuth FM rate $2V^2/(\lambda R_0)$ and the [range cell migration](/range-cell-migration/) at the ends of the aperture. Compare the migration with the range resolution for a bandwidth of 300 MHz.

11. • One depth sample gives the slow-time samples $(1, i, -1, 1)$. Compute the lag-one autocorrelation $R_1 = \sum_k \overline{x[k]}\, x[k+1]$ and the Kasai velocity for $f_0 = 5$ MHz, $\mathrm{PRF} = 4$ kHz and $c = 1540$ m/s.

12. • An [inverse synthetic aperture radar](/inverse-synthetic-aperture-radar/) at $\lambda = 2$ cm watches a ship turn at $\Omega = 0.02$ rad/s for $1.5$ s. Find the cross-range resolution, the bandwidth that gives the same range resolution, the Doppler frequency of a scatterer 6 m off the axis, and the largest $|x| < 2\rho_r\rho_a/\lambda$ for which the scatterers stay in their range cells.

13. • For two channels with the covariance $R = \begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix}$ and the steering vector $a = (1, 1)$, compute the [Capon beamformer](/capon-beamformer/) weights, check $w^{\mathsf H} a = 1$, and compare its output power with that of delay-and-sum with $w = a/2$.

14. • A 96-element array images to 50 mm at $c = 1.54$ mm/µs. Using [synthetic transmit aperture](/synthetic-transmit-aperture/) with reciprocity, how many distinct traces are there? Compute the frame time and frame rate of synthetic transmit aperture and of [plane-wave compounding](/plane-wave-compounding/) with 7 angles.

15. • [SAFT](/saft/) inspects steel ($c = 5.9$ mm/µs) with a 5 MHz transducer of diameter 6 mm. Give the largest scan step without grating lobes, the span of 21 positions at that step, and the estimated lateral resolution.

16. • The wrapped phases $(0, 2.1, -2.1, 0.5)$ sit at the corners of one pixel loop, in order around the loop. Compute the residue charge. Do the same for $(0, 1, 2, 1)$. Which of the two loops does the [Goldstein branch cut algorithm](/goldstein-branch-cut/) have to connect to a cut?

17. • For the channels $s = (1, 4, -9, 16)$, compute the [delay-multiply-and-sum](/delay-multiply-and-sum/) output directly as $\sum_{i<j} \operatorname{sign}(s_is_j)\sqrt{|s_is_j|}$, then by the $O(M)$ formula, and compare with delay-and-sum.

18. • A 128-element array of pitch 0.3 mm fires a plane wave at $\alpha = 8°$ in tissue at $c = 1.54$ mm/µs. How long does the firing take from the first element to the last? What is the transmit time $(z\cos\alpha + x\sin\alpha)/c$ to the pixel $(x, z) = (5, 20)$ mm?

19. • In [photoacoustic tomography](/photoacoustic-tomography/) a uniform ball of radius 2 mm with $p_0 = 1$ is seen by a detector 25 mm from its centre, with $c = 1.5$ mm/µs. Between which times does the detector see a signal, and what are the extreme values of the N-shaped pulse?

20. • [Diffraction tomography](/diffraction-tomography/) at 2 MHz with $c = 1.5$ mm/µs. Compute $k_0$, the largest spatial frequency covered in transmission and in reflection, and the finest period that each mode can show.

21. ★ The mean of $L$ independent exponential intensities of mean $\langle I\rangle$ has a gamma distribution. Find the probability that a 4-look pixel is brighter than $2\langle I\rangle$, and compare it with one look.

22. ★ Two channels see unit white noise and an interferer of power $P = 100$ with the steering vector $b = (1, i)$, so $R = I + P\,bb^{\mathsf H}$. The look direction is $a = (1, 1)$. Find the Capon output power and its gain $|w^{\mathsf H} b|^2$ on the interferer, and compare both with delay-and-sum.

23. ★ After windowing, one row of a defocused point target has the phase history $e^{i\varphi(k)}$ with $\varphi = (0, 0.5, 1.5, 3.0)$. Run one iteration of [phase gradient autofocus](/phase-gradient-autofocus/) on this single row: phase differences, removal of the mean gradient, integration and removal of the line $a + bk$. Compare the estimate with $\varphi$ minus its best line.

24. ★ A Casorati matrix has one tissue pixel with slow-time samples $(10, 10)$ and one blood pixel with $(0, 1)$. Remove the first singular component, as the [SVD clutter filter](/svd-clutter-filter/) does with $k_1 = 1$. How much power is left in each pixel, and why does the blood lose about half of its power?

25. ★ A spherical detector surface of radius 25 mm surrounds the uniform ball of exercise 19, centred at the origin, with $c = 1.5$ mm/µs. Show that [universal back-projection](/universal-back-projection/), with $b = 2p - 2t\,\partial p/\partial t$ weighted by solid angle, gives exactly $p_0$ at the centre.
