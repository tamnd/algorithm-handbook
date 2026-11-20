A recorded word is a sequence of numbers, sixteen thousand of them per second at a common sampling rate. Very little of that detail matters for what was said. A speaker's voice is well described by a source, the buzz of the vocal folds or the hiss of air, passed through a filter, the shape of the throat and mouth. The source sets the pitch and the filter sets the vowel. Speech analysis recovers these two parts, frame by frame, as a short vector of features. Speech synthesis runs the other way: from text to features, and from features back to a waveform.

The chapter covers both directions. The analysis half builds the features that speech recognizers and speaker models use. The synthesis half follows text-to-speech from concatenating recorded units, through statistical models that generate feature tracks, to neural networks that produce the waveform sample by sample or in parallel.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Framing and detection.** The source-filter model, pre-emphasis, zero-crossing rate, endpoint detection and voice activity detection.
2. **Spectral features.** The mel filter bank, mel-frequency cepstral coefficients, perceptual linear prediction, delta features, cepstral mean normalization and RASTA filtering.
3. **Pitch, formants and enhancement.** Cepstral pitch detection, RAPT, pYIN, formant tracking and the Ephraim-Malah noise suppressor.
4. **Coding and modification.** Code-excited linear prediction, the phase vocoder and PSOLA for changing pitch and duration.
5. **Classical text-to-speech.** Text normalization for speech, grapheme-to-phoneme conversion, formant synthesis, unit selection, HMM-based synthesis and maximum likelihood parameter generation.
6. **Neural synthesis.** Tacotron, FastSpeech, WaveNet, HiFi-GAN, VITS, language models over neural codec tokens, and the mean opinion score used to judge them.

## What to read meanwhile

Most of the analysis tools are in the signal processing chapter of Volume 28: the [short-time Fourier transform](/short-time-fourier-transform/), the [cepstrum](/cepstrum/), [linear predictive coding](/linear-predictive-coding/), [pitch detection](/pitch-detection/), [autocorrelation](/autocorrelation/), the [power spectral density](/power-spectral-density/), [FIR filters](/fir-filter/) and [IIR filters](/iir-filter/). For noise, read [spectral subtraction](/spectral-subtraction/) and the [Wiener filter](/wiener-filter/) there. The [discrete Fourier transform](/discrete-fourier-transform/) and the [fast Fourier transform](/fast-fourier-transform/) are in Volume 11, the [Levinson-Durbin recursion](/levinson-durbin-recursion/) that solves for the predictor coefficients is in Volume 12, and the [filter bank](/filter-bank/) and the [discrete cosine transform](/discrete-cosine-transform/), the last step of the cepstral coefficients, are in Volume 24. A classical statistical voice activity detector is a [likelihood ratio test](/likelihood-ratio-test/) (Volume 33).

For synthesis, the [hidden Markov model](/hidden-markov-model/) and the [variational autoencoder](/variational-autoencoder/) are in Volume 25. The first step of text-to-speech splits and normalizes text, as in [text tokenization](/text-tokenization/) and the [Penn Treebank tokenization](/penn-treebank-tokenization/) in Chapter 41.1.
