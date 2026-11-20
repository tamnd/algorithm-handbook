1. ◦ Use the [mel scale](/mel-scale/) $m(f) = 2595 \log_{10}(1 + f/700)$. Compute $m(1500)$. How many mels does the band from 250 to 500 Hz span, and how many does the band from 4000 to 8000 Hz span? Both bands are one octave wide.

2. ◦ Count the sign changes in the frame $(0.3, -0.1, -0.2, 0.4, 0.0, -0.5, 0.2, 0.1, -0.3, 0.6)$, with a zero sample counted as positive, and give the [zero-crossing rate](/zero-crossing-rate/) as changes per pair of neighbouring samples.

3. ◦ Apply [pre-emphasis](/pre-emphasis/) $y[n] = x[n] - 0.95\,x[n-1]$, with $x[-1] = 0$, to $x = (2, 4, 4, 1)$. Give the gain of the filter in dB at 0 Hz and at the Nyquist frequency, and the frequency at which the gain is exactly 1 when $f_s = 16$ kHz.

4. ◦ A recording of 2.5 s at 16 kHz is cut into frames of 400 samples with a hop of 160 samples, and only whole frames are kept. How many frames are there?

5. ◦ In the [source-filter model](/source-filter-model/), treat the vocal tract as a uniform tube of length 14 cm, closed at the glottis and open at the lips, with the speed of sound 350 m/s. Give the first three resonances.

6. ◦ A [WaveNet](/wavenet/) stack has two blocks, each with dilated causal convolutions of kernel size 2 and dilations $1, 2, 4, \ldots, 256$. How many past samples does one output see, counting itself? How many milliseconds is that at 16 kHz?

7. ◦ The [FastSpeech](/fastspeech/) length regulator gets the durations $(3, 1, 4, 2)$ and the speed factor $\alpha = 1.2$, which multiplies each duration before rounding to the nearest integer. Give the new durations and the number of mel frames.

8. ◦ A [neural codec](/neural-codec-language-model/) makes 50 frames per second, each with 4 codebook indices from codebooks of 1024 entries. What is its bit rate? If a [language model](/language-model/) predicts one frame per step, how many sequential steps does 10 s of speech take, and how many would a sample-by-sample model take at 24 kHz?

9. ◦ Ten listeners rate a system $4, 5, 3, 4, 4, 5, 2, 4, 3, 5$. Give the [mean opinion score](/mean-opinion-score/), the sample standard deviation and the half-width of the normal 95% interval $1.96\,s/\sqrt{n}$.

10. • The inverse filter of a [linear predictor](/linear-predictive-coding/) at $f_s = 8$ kHz has the quadratic factor $1 - 1.2z^{-1} + 0.81z^{-2}$. Find the pole radius, and the frequency and bandwidth of the resonance, as [formant estimation](/formant-estimation/) does.

11. • A [mel filter bank](/mel-filter-bank/) has $M = 3$ triangular filters with edges equally spaced in mels from 0 to 8000 Hz ($f_s = 16$ kHz). Give the five edge frequencies in Hz. Which filter is the widest, and how wide is it?

12. • A signal is multiplied by $g = 10$. The [MFCCs](/mel-frequency-cepstral-coefficients/) use $M = 40$ filters on the power spectrum, the natural logarithm and the orthonormal DCT-II. Which coefficients change, and by how much?

13. • Compute [delta features](/delta-features/) with $\Theta = 2$, $d_t = \sum_{\theta=1}^{2} \theta (c_{t+\theta} - c_{t-\theta}) / (2 \sum_{\theta=1}^{2} \theta^2)$, for the sequence $c = (2, 2, 5, 9, 9)$, repeating the first and last values beyond the edges.

14. • A [cepstral pitch detector](/cepstral-pitch-detection/) at $f_s = 16$ kHz searches pitches from 60 to 400 Hz. Give the smallest and largest quefrency, in whole samples, that it looks at. The peak is at $q = 123$: what is the pitch, and how far apart in Hz are the pitches of neighbouring quefrencies there?

15. • In [RAPT](/rapt-pitch-tracker/) the local cost of a voiced candidate at lag $k$ with correlation $C$ is $d = 1 - C(1 - \mathrm{LAG\_WT} \cdot k/K)$. Take $K = 160$ and $\mathrm{LAG\_WT} = 0.3$ at 8 kHz. Compare a candidate at lag 40 with $C = 0.9$ and one at lag 80 with $C = 0.95$. How large must $C$ be at lag 80 to tie with the first?

16. • The [formant synthesizer](/formant-synthesis/) of Klatt uses the resonator $y[n] = A x[n] + B y[n-1] + C y[n-2]$ with $C = -e^{-2\pi b T}$, $B = 2e^{-\pi b T}\cos(2\pi F T)$ and $A = 1 - B - C$. Compute $A$, $B$ and $C$ for $F = 500$ Hz, $b = 100$ Hz at 10 kHz, and the gain of the resonator at 500 Hz.

17. • [PSOLA](/psola/) analysis has pitch marks at samples 0, 100, 210 and 330. The local period at a mark is the mean of the intervals on each side, and each segment is a Hann window of $2P + 1$ samples centred on the mark. Give $P$ and the segment length at the marks 100 and 210.

18. • In [HMM-based synthesis](/hmm-based-speech-synthesis/) the state durations have means $(5, 10, 5)$ and variances $(4, 9, 1)$, and the phone must last 26 frames. With the rule $d_k = m_k + \rho v_k$, find $\rho$ and the three durations.

19. • In the [likelihood-ratio detector](/likelihood-ratio-vad/) the log ratio of one frequency bin is $\gamma\xi/(1 + \xi) - \ln(1 + \xi)$, where $\gamma$ is the a posteriori and $\xi$ the a priori SNR. Evaluate it for $\gamma = 4$, $\xi = 1$. For $\xi = 1$, what $\gamma$ makes it zero?

20. • In [joint-sequence G2P](/joint-sequence-g2p/), each graphone has 1 or 2 letters and 0 or 1 phones. In how many ways can a word of 4 letters with a pronunciation of 3 phones be split into graphones? How many if each graphone has exactly 1 letter?

21. • In [VITS](/vits/), two text tokens are aligned to four frames; each token takes at least one frame and token 0 comes first. The log-likelihoods of frames 1 to 4 are $(-1, -1, -3, -5)$ under token 0 and $(-4, -3, -1, -1)$ under token 1. Find the best alignment by monotonic alignment search and its score. How many alignments are there?

22. ★ Run the [Levinson-Durbin recursion](/levinson-durbin-recursion/) by hand on the autocorrelation $r = (1, 0.5, 0.1)$ for a predictor of order 2, giving each reflection coefficient, each error and the final predictor. Find the poles of $A(z)$ and, at 8 kHz, their frequency and bandwidth. Would formant estimation report this pole pair as a formant?

23. ★ A [phase vocoder](/phase-vocoder/) has $f_s = 16000$, an FFT of $N = 1024$ and analysis hop $H_a = 256$. Bin 10 is centred at 156.25 Hz. For a 160 Hz tone, give the measured phase advance of bin 10 wrapped to $(-\pi, \pi]$, the deviation from the expected advance, and the frequency estimate. What range of offsets from the bin centre is recovered correctly? What does it estimate for a 190 Hz tone seen in bin 10?

24. ★ [CELP](/code-excited-linear-prediction/) with filtered vectors (take the filter as the identity): target $t = (0, -2, -2)$, adaptive codebook $a_1 = (0, -1, 1)$, $a_2 = (-1, -1, 0)$, fixed codebook $f_1 = (-1, 0, -1)$, $f_2 = (0, 1, 0)$. Search the adaptive codebook, then the fixed codebook on the residual, each with its best gain. Give the choices and the squared error. Then find the best pair with both gains optimized together.

25. ★ [Unit selection](/unit-selection-synthesis/) for three targets has candidates $A_1, A_2$; $B_1, B_2$; $C_1$, with target costs $A_1 = 0$, $A_2 = 1$ and 0 for the rest. The join costs are $A_1B_1 = 1$, $A_1B_2 = 2$, $A_2B_1 = 3$, $A_2B_2 = 0$, $B_1C_1 = 5$, $B_2C_1 = 0$. What does a beam of width 1 return, and at what cost? What does the full Viterbi search return?

26. ★ [Parameter generation](/maximum-likelihood-parameter-generation/) for $T = 2$ frames of one coefficient: the static means are $0$ and $2$ with variance 1, and one delta $\Delta c = c_2 - c_1$ has mean 0 and precision $s$. Write $W$, the matrix $W^\top \Sigma^{-1} W$ and the right-hand side, and solve for $c$. Give $c$ for $s = 1$ and $s = 2$. What happens to the jump $c_2 - c_1$ as $s$ grows?
