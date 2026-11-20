## What to remember

- **Source and filter.** Speech is an excitation passed through the vocal tract. A pole $r e^{\pm i\theta}$ of the all-pole filter is a formant at $F = \theta f_s / 2\pi$ with bandwidth $B = -f_s \ln r / \pi$. The [Levinson-Durbin recursion](/levinson-durbin-recursion/) solves the Toeplitz normal equations of [linear prediction](/linear-predictive-coding/) exactly.
- **The standard front end.** Frames of 25 ms every 10 ms, [pre-emphasis](/pre-emphasis/), a window, an FFT, a [mel filter bank](/mel-filter-bank/) of 23 to 40 triangles, the logarithm and a DCT give 13 [MFCCs](/mel-frequency-cepstral-coefficients/); with [deltas](/delta-features/) and delta-deltas the vector has 39 numbers. A gain on the signal moves only $c_0$, by $2\sqrt{M} \ln |g|$ with the orthonormal DCT and $M$ filters.
- **Normalization is exact for offsets, approximate for channels.** [Cepstral mean normalization](/cepstral-mean-normalization/) and [RASTA](/rasta-filtering/) remove a constant added to every frame exactly. A real channel is removed only if it is short compared with the frame.
- **Pitch tracking has a dynamic program at its end.** The [cepstral detector](/cepstral-pitch-detection/) picks one peak per frame. [RAPT](/rapt-pitch-tracker/) and [pYIN](/pyin/) choose a path through candidates; the path is optimal for their costs, and the costs are heuristic.
- **Speech in noise is a statistical test.** When the densities of noise and of speech are known, a likelihood ratio threshold is the best frame test ([Neyman-Pearson](/neyman-pearson-lemma/)); the [likelihood-ratio detector](/likelihood-ratio-vad/) builds one from a Gaussian model of each bin. The [Ephraim-Malah estimator](/ephraim-malah-estimator/) is optimal only under its Gaussian model.
- **Analysis by synthesis.** [CELP](/code-excited-linear-prediction/) tries every codebook entry through the synthesis filter and keeps the one with the largest $\langle t, y \rangle^2 / \langle y, y \rangle$. Searching the two codebooks in turn is not jointly optimal.
- **Search inside synthesis.** [Unit selection](/unit-selection-synthesis/) is a Viterbi search in $\Theta(nK^2)$, exact without pruning. [Parameter generation](/maximum-likelihood-parameter-generation/) solves a banded positive definite system, so its answer is unique. The duration rule of [HMM synthesis](/hmm-based-speech-synthesis/) sets $d_k = m_k + \rho v_k$.
- **Neural synthesis trades sequential steps.** [WaveNet](/wavenet/) needs one step per sample; [Tacotron](/tacotron/) one per frame; [FastSpeech](/fastspeech/), [HiFi-GAN](/hifi-gan/) and [VITS](/vits/) compute all frames at once. Their quality is a [mean opinion score](/mean-opinion-score/), a measurement of listeners on a 1 to 5 scale, and scores from different tests cannot be compared.

## The main methods side by side

| Method | Kind | Time | What is guaranteed |
|---|---|---|---|
| [Mel filter bank](/mel-filter-bank/) | fixed transform | $O(W + N \log N + MN)$ per frame | a fixed map; recognition accuracy is measured |
| [MFCC](/mel-frequency-cepstral-coefficients/) | fixed transform | $O(T(N \log N + MN + KM))$ | a gain changes only $c_0$ |
| [Cepstral pitch](/cepstral-pitch-detection/) | peak picking | $O(M \log M)$ per frame | one clear peak under its harmonic model; accuracy measured |
| [RAPT](/rapt-pitch-tracker/) | candidates and DP | $O(F(Kn + C^2))$ | best path for heuristic costs |
| [pYIN](/pyin/) | candidates and HMM | $O(F(WT + NT + MJ))$ | Viterbi path exact for the model |
| [Likelihood-ratio VAD](/likelihood-ratio-vad/) | statistical test | $O(F N \log N)$ | none; threshold tuned |
| [CELP](/code-excited-linear-prediction/) | analysis by synthesis | $O(S(Q + C)L^2 + SLp)$ | best entry of each codebook in turn |
| [PSOLA](/psola/) | overlap-add | $O(MP + K)$ | none; quality judged by listening |
| [Unit selection](/unit-selection-synthesis/) | Viterbi | $\Theta(nK^2)$ | least total cost without pruning |
| [MLPG](/maximum-likelihood-parameter-generation/) | banded linear system | $O(TDb^2)$ | the unique maximizer |
| [Joint-sequence G2P](/joint-sequence-g2p/) | EM on graphones | $\Theta(nmHk)$ per word and iteration | likelihood never decreases |

: The main methods of the chapter, with the costs given in the entries. $N$ is the FFT length, $W$ the frame length, $M$ the number of filters (for the cepstral detector, the FFT length), $K$ the coefficients kept, $T$ or $F$ the number of frames.

## Choosing a method

- For recognizer features, use log mel filter bank energies for a neural network and MFCCs with deltas and mean normalization for Gaussian mixtures. Try PLP or RASTA when the channel varies.
- For pitch, use pYIN or RAPT on whole recordings, since both look at the frames on either side; use a one-frame method such as the cepstral detector only when there is no time to wait.
- For voice activity, energy and zero crossings suffice in quiet rooms; use the likelihood-ratio detector in stationary noise.
- To change duration or pitch of a recording, use PSOLA for a single voice with good pitch marks and the phase vocoder for music or mixed sounds.
- For synthesis today, use a duration-based acoustic model such as FastSpeech, or VITS, with a parallel vocoder such as HiFi-GAN. Formant synthesis still suits experiments that control each parameter.
