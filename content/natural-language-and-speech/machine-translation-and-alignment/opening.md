To learn to translate from examples, a system first needs to know which parts of a sentence correspond to which parts of its translation. Given millions of sentence pairs such as "the house is small" and "das Haus ist klein", the IBM models learn by expectation maximization that "house" goes with "Haus", without any dictionary. From word alignments came phrase tables, and from phrase tables the statistical systems that were in wide use before neural translation. Neural encoder-decoder models with attention replaced them, but alignment, search and evaluation remain the same problems in new forms.

The chapter is about these algorithms: aligning sentences and words in a parallel corpus, building and searching a translation model, training it towards a quality measure, and scoring the output. Some of the questions are old and exact, such as how to align two documents by sentence length with dynamic programming; others, such as how well a measure like BLEU tracks human judgment, are matters of measurement.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Parallel text and alignment.** Machine translation, parallel corpora, sentence alignment and the Gale-Church method, word alignment, IBM models 1 to 3, HMM alignment, fast_align, the grow-diag-final heuristic and the alignment error rate.
2. **Statistical translation.** The noisy channel model, phrase extraction, the phrase-based model, lexicalized reordering, log-linear models and minimum error rate training, stack decoding and cube pruning.
3. **Translation with grammars.** Hierarchical phrase-based translation, synchronous context-free grammars, inversion transduction grammars and GHKM rule extraction.
4. **Neural translation.** The encoder-decoder model, additive and multiplicative attention, multilingual translation, back-translation, sequence-level knowledge distillation, non-autoregressive translation and minimum risk training.
5. **Evaluation.** BLEU, chrF, TER and COMET.

## What to read meanwhile

Word alignment is an exercise in [expectation maximization](/expectation-maximization/), and HMM alignment uses the [hidden Markov model](/hidden-markov-model/) with the [forward-backward algorithm](/forward-backward-algorithm/), all in Volume 25. Sentence alignment is a dynamic program like [global alignment](/global-alignment/) and the [Needleman-Wunsch algorithm](/needleman-wunsch/) of Volume 27, and TER is a kind of [edit distance](/edit-distance/) (Volume 8). Decoders use [beam search](/beam-search/) and [A* search](/a-star-search/) from Volume 29.

Synchronous grammars are parsed with the chart methods of Volume 9, such as the [CYK algorithm](/cyk-algorithm/). Sequence-level distillation builds on [knowledge distillation](/knowledge-distillation/) in Volume 25. The subword vocabularies that neural translation depends on are written: start with [subword tokenization](/subword-tokenization/) and [byte-pair encoding](/byte-pair-encoding/), and read [BPE-dropout](/bpe-dropout/) and [subword regularization](/subword-regularization/), which were tested on translation.
