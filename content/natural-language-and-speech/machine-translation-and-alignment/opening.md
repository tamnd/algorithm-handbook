Give a program three sentence pairs, "das Haus" with "the house", "das Buch" with "the book" and "ein Buch" with "a book", and no dictionary. After a few rounds of counting, it believes that "Haus" means "house" and "Buch" means "book", because "das" is explained by "the" in two pairs and leaves nothing else for "Haus" to mean. This is [IBM Model 1](/ibm-model-1/) learning by expectation-maximization, and it is how statistical translation started: from a [parallel corpus](/parallel-corpus/) of human translations, learn which words and phrases correspond, then search for the target sentence that a model scores best.

Translation keeps its algorithms busy at every step. Sentence alignment is a dynamic program like edit distance. Word alignment is EM over hidden links. Phrase extraction is a scan for blocks consistent with the links. Decoding with free reordering is NP-hard, so decoders use beams and cube pruning, and give up the guarantee of the best answer. Neural models replaced the phrase tables around 2015, but they kept the parallel corpus, the beam search and the metrics, and the translation tables that alignment learns are still bilingual dictionaries.

## What the chapter covers

The chapter is in six groups, read in order.

1. **The problem and its data.** [Machine translation](/machine-translation/) as a search problem, the [noisy channel model](/noisy-channel-translation-model/), and [sentence alignment](/sentence-alignment/) of a parallel corpus, with the length-based [Gale-Church method](/gale-church-alignment/).
2. **Word alignment.** The [word alignment](/word-alignment/) problem and its [error rate](/alignment-error-rate/); [IBM Model 1](/ibm-model-1/), [Model 2](/ibm-model-2/), the [HMM model](/hmm-alignment-model/), [fast_align](/fast-align/) and [Model 3](/ibm-model-3/); and [grow-diag-final](/grow-diag-final-symmetrization/), which merges the two directions.
3. **Evaluation.** [BLEU](/bleu/), [chrF](/chrf/), [translation edit rate](/translation-edit-rate/) and the learned metric [COMET](/comet-metric/).
4. **Phrase-based translation.** [Phrase-pair extraction](/phrase-pair-extraction/), the [log-linear model](/log-linear-translation-model/), the [phrase-based model](/phrase-based-translation-model/) and its [lexicalized reordering](/lexicalized-reordering-model/), [stack decoding](/phrase-based-stack-decoding/), and [minimum error rate training](/minimum-error-rate-training/).
5. **Translation with synchronous grammars.** [Synchronous CFGs](/synchronous-context-free-grammar/), [inversion transduction grammars](/inversion-transduction-grammar/), [hierarchical phrase-based translation](/hierarchical-phrase-based-translation/), [cube pruning](/cube-pruning/) and [GHKM rule extraction](/ghkm-rule-extraction/).
6. **Neural translation.** The [encoder-decoder model](/encoder-decoder-model/) with [additive](/additive-attention/) and [multiplicative attention](/multiplicative-attention/), and the methods built on it: [back-translation](/back-translation/), [multilingual translation](/multilingual-neural-translation/), [sequence-level distillation](/sequence-level-knowledge-distillation/), [minimum risk training](/minimum-risk-training/) and [non-autoregressive translation](/non-autoregressive-translation/).

## A first reading

For a first pass, read these in order:

1. [Machine translation](/machine-translation/)
2. [Parallel corpus](/parallel-corpus/)
3. [Noisy channel translation model](/noisy-channel-translation-model/)
4. [Word alignment](/word-alignment/)
5. [IBM Model 1](/ibm-model-1/)
6. [HMM alignment model](/hmm-alignment-model/)
7. [BLEU](/bleu/)
8. [Phrase-pair extraction](/phrase-pair-extraction/)
9. [Phrase-based translation model](/phrase-based-translation-model/)
10. [Phrase-based stack decoding](/phrase-based-stack-decoding/)
11. [Encoder-decoder model](/encoder-decoder-model/)
12. [Additive attention](/additive-attention/)
13. [Back-translation](/back-translation/)

This path goes from the data through alignment and the classic phrase-based system to neural translation. Model 3, fast_align, GHKM, cube pruning and non-autoregressive translation can wait. A reader who cares only about neural systems can go from the first four entries straight to group 6, reading BLEU on the way.

## Before you start

The statistical side needs [Bayes' theorem](/bayes-theorem/), [maximum likelihood estimation](/maximum-likelihood-estimation/), [expectation-maximization](/expectation-maximization/) and the [hidden Markov model](/hidden-markov-model/) with the [Viterbi algorithm](/viterbi-algorithm/), from Volume 25, together with [n-gram language models](/n-gram-language-model/) from this volume. Sentence alignment and TER use [edit distance](/edit-distance/), and the decoders use [beam search](/beam-search/) and a [priority queue](/priority-queue/). Group 5 assumes [context-free grammars](/context-free-grammar/) and the [CYK algorithm](/cyk-algorithm/) of Volume 9; a synchronous grammar of rank 1 relates to the [finite-state transducers](/finite-state-transducer/) of the same volume. Group 6 assumes the [recurrent neural network language model](/recurrent-neural-network-language-model/) and the [transformer](/transformer/) of the language modelling chapter, [cross-entropy loss](/cross-entropy-loss/) and [knowledge distillation](/knowledge-distillation/) from Volume 25, and [byte-pair encoding](/byte-pair-encoding/) for the vocabulary.
