A speech recognizer hears a stretch of audio and must write the words. The classical view treats this as decoding a noisy channel: choose the word sequence W that maximizes P(W) times P(audio | W), where a language model gives the first factor and an acoustic model the second. Between the two sits a pronunciation lexicon that spells each word in phones. The search over all word sequences is the hard part, and most of the algorithms of the chapter are ways to organize it.

The chapter follows the field's two eras. In the first, hidden Markov models with Gaussian mixtures or neural networks score the audio, and weighted finite-state transducers combine model, lexicon and grammar into one graph that a beam search walks. In the second, a single network maps audio to characters or pieces, trained with connectionist temporal classification, a transducer loss or attention. The chapter ends with adaptation, evaluation and the related task of telling speakers apart.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Acoustic models.** The source-channel formulation, dynamic time warping with the Sakoe-Chiba band, GMM-HMM models, triphones and state tying, Viterbi training, MMI and lattice-free MMI training, and hybrid DNN-HMM models.
2. **Decoding graphs.** The pronunciation lexicon, WFST composition, determinization, weight pushing and the HCLG graph.
3. **Search.** Beam search, token passing, stack decoding, word lattices, confusion networks, lattice rescoring and shallow fusion.
4. **End-to-end models.** Connectionist temporal classification and its prefix beam search, the RNN transducer, listen-attend-spell, joint CTC-attention, the conformer, wav2vec 2.0 and SpecAugment.
5. **Adaptation and evaluation.** Vocal tract length normalization, MLLR and MAP adaptation, forced alignment, keyword spotting and word error rate.
6. **Speakers.** Speaker verification, the GMM-UBM, i-vectors, x-vectors, PLDA scoring, the equal error rate and speaker diarization.

## What to read meanwhile

The hidden Markov model and its algorithms are in Volume 25: the [hidden Markov model](/hidden-markov-model/), the [Viterbi algorithm](/viterbi-algorithm/), the [forward-backward algorithm](/forward-backward-algorithm/), the [Baum-Welch algorithm](/baum-welch-algorithm/), [expectation-maximization](/expectation-maximization/) and the [Gaussian mixture model](/gaussian-mixture-model/). The speaker models use [linear discriminant analysis](/linear-discriminant-analysis/), [factor analysis](/factor-analysis/) and the [ROC curve](/roc-auc/), and diarization uses [agglomerative clustering](/agglomerative-clustering/) and [spectral clustering](/spectral-clustering/), all in Volume 25. The front end starts with the [short-time Fourier transform](/short-time-fourier-transform/) (Volume 28).

Decoding graphs are built from the [weighted automaton](/weighted-automaton/) and the [finite-state transducer](/finite-state-transducer/) with [NFA determinization](/nfa-determinization/) and [DFA minimization](/dfa-minimization/) (Volume 9). For the search, read [beam search](/beam-search/) and [A* search](/a-star-search/) in Volume 29, and [shortest paths in a DAG](/dag-shortest-paths/) and [k shortest paths](/k-shortest-paths/) in Volume 7 for lattices. Word error rate is an [edit distance](/edit-distance/) (Volume 8), and dynamic time warping is close to [Needleman-Wunsch alignment](/needleman-wunsch/) (Volume 27).
