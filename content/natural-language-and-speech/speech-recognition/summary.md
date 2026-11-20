## What to remember

- **The source-channel rule.** The classical recognizer picks the $W$ that maximizes $P(O \mid W)\,P(W)$: an acoustic model, a [pronunciation lexicon](/pronunciation-lexicon/) and a language model. In practice the language model score is scaled and a word insertion penalty is added, so the rule is tuned on data.
- **WER is a measurement.** The [word error rate](/word-error-rate/) is $(S + D + I)/N$ from a minimal edit alignment. It can exceed 1, it is not symmetric in reference and hypothesis, and the WER of a corpus is not the mean of the sentence WERs.
- **HMM algorithms are exact; HMM training is not.** The forward sum, the Viterbi path and [forced alignment](/forced-alignment/) are exact for the model. EM and [Viterbi training](/viterbi-training/) never lower their likelihood but reach only a stationary point. A state with self-loop $a$ gives a geometric duration with mean $1/(1 - a)$.
- **Context needs tying.** With 45 phones there are $45^3 = 91125$ [triphones](/triphone-model/), most unseen. A [phonetic decision tree](/phonetic-decision-tree-state-tying/) grown greedily ties their states and gives a model for every context.
- **Pruned search is approximate.** [Time-synchronous beam search](/time-synchronous-beam-search/) and [token passing](/token-passing/) are the same Viterbi search, exact only without pruning. [Stack decoding](/stack-decoding/) is exact with an admissible estimate and no limit on the stack. A [word lattice](/word-lattice/) keeps the alternatives, and its arc posteriors take $O(N + E)$ by forward-backward.
- **Transducers build the graph.** $HCLG = \min(\det(H \circ C \circ L \circ G))$, with disambiguation symbols so that $L \circ G$ can be determinized. [Determinization](/weighted-determinization/) terminates on inputs with the twins property and can still blow up exponentially.
- **CTC sums are exact; CTC decoding is not.** [CTC](/connectionist-temporal-classification/) sums over all alignments in $\Theta(T(U + K))$. The most likely path is not the most likely labeling, and [prefix beam search](/ctc-prefix-beam-search/) and [shallow fusion](/shallow-fusion/) with $+\lambda \log p_{\text{lm}}$ are approximate.
- **Speaker decisions are likelihood ratios.** [Verification](/speaker-verification/) compares a score with a threshold. The [equal error rate](/equal-error-rate/) depends only on the order of the scores, and its two conventions, the nearest point and the ROC convex hull, can differ on small sets. [PLDA](/plda-scoring/) gives the exact log-likelihood ratio of its two-covariance model.

## The main methods side by side

| Method | Kind | Time | What is guaranteed |
|---|---|---|---|
| [Dynamic time warping](/dynamic-time-warping/) | dynamic programming | $\Theta(nm)$ | the least-cost warp; with a band, only within the band |
| [Forced alignment](/forced-alignment/) | Viterbi | $\Theta(TS)$ | the best state path for the model |
| [Viterbi training](/viterbi-training/) | hard EM | $\Theta(kTN^2)$ for $k$ rounds | best-path likelihood never decreases |
| [Beam search](/time-synchronous-beam-search/) | pruned Viterbi | $O(nkV \log k)$ | exact only without pruning |
| [Stack decoding](/stack-decoding/) | best-first | $O(V^2n^2\log(Vn) + Vn^2L)$ | exact with an admissible estimate and no stack limit |
| [Word lattice](/word-lattice/) | forward-backward | $O(N + E)$ | exact arc posteriors |
| [Confusion network](/confusion-network/) | clustering of arcs | $O(N^2 + E^3)$ | heuristic; lowers expected word errors in practice |
| [Composition](/weighted-transducer-composition/) | product construction | $O(pq + mn)$ | exact |
| [Weight pushing](/weight-pushing/) | shortest distance | $O(nm)$ | exact; same path weights |
| [MMI training](/maximum-mutual-information-training/) | discriminative | $\Theta(T(N + E + P))$ per utterance | exact objective and gradient; not concave |
| [CTC](/connectionist-temporal-classification/) | sum over alignments | $\Theta(T(U + K))$ | exact sum and gradient |
| [CTC prefix search](/ctc-prefix-beam-search/) | beam search | $O(TWK)$ | exact only with a full beam |
| [GMM-UBM](/gmm-ubm-speaker-verification/) | likelihood ratio | $O(TMd)$ | none; threshold tuned |
| [PLDA scoring](/plda-scoring/) | Gaussian model | $O(d^3 + Nd^2)$ | exact LLR under the model |

: The main methods of the chapter, with the costs given in the entries. $T$ is the number of frames, $n$ and $m$ the sequence lengths, $N$ and $E$ the states and arcs of a lattice; the other letters are defined in each entry.

## Choosing a method

- For a few words from one speaker on a small device, dynamic time warping against stored templates is enough.
- To place known words in time, use forced alignment with an HMM model; it is the usual first step for training and for corpus work.
- For a recognizer trained on hundreds of hours with a fixed lexicon, a hybrid or LF-MMI model with an HCLG graph is a well-tested choice, and its lattices support rescoring and keyword search.
- With thousands of hours, use an end-to-end Conformer with CTC or a transducer; the transducer suits streaming, attention suits whole utterances. Add SpecAugment, and wav2vec 2.0 pretraining when labeled speech is scarce.
- For speakers, use x-vectors with PLDA or cosine scoring, and report the EER with its convention together with a detection cost.
