A phone in a kitchen hears "set a timer for ten minutes and add eggs to the list". Before it can act, a chain of programs must run. One finds where speech starts in the audio and turns each hundredth of a second into a short vector of features. A recognizer searches for the word sequence that best explains those vectors, weighing what was heard against what people usually say. The text is then split into tokens, "ten minutes" is read as a duration and "eggs" as an item, and the sentence is parsed into two commands. The reply, "Timer set for ten minutes", is generated as text and spoken by a synthesizer. Each step is a problem with its own algorithms, and most of them must cope with ambiguity: the same sounds fit several word sequences, and the same words fit several structures.

This volume collects those algorithms, from splitting text into tokens to recognizing and synthesizing speech. It has nine chapters. In this edition one of them is written: Chapter 41.1, Tokenization and text normalization, with 22 entries. The other eight are not written yet; each has an opening page that says what it will cover and what to read meanwhile.

## Why natural language and speech gets a volume of its own

A few ideas run through the whole volume:

- **Choose the most probable reading.** Language is ambiguous at every level, so most methods define a probability over the possible outputs and search for the best one. Segmenting "thetabledownthere" into words, tagging a sentence, recognizing an utterance and translating it all take this form, and the search is often a dynamic program such as the [Viterbi algorithm](/viterbi-algorithm/).
- **Models learn from text without labels.** Large amounts of raw text and audio are cheap, and labelled data are not. [Expectation-maximization](/expectation-maximization/) fits word alignments, hidden Markov models and subword vocabularies from raw data, and neural models are first trained to predict the next or a hidden word.
- **The vocabulary is never closed.** New names, words and spellings appear in every new text. A system must decide what its units are and what to do with a unit it has not seen, which is why the volume starts with tokenization and [out-of-vocabulary words](/out-of-vocabulary-word/).
- **Finite-state machines do much of the work.** Tokenizers, morphological analyzers and speech decoding graphs are [finite-state transducers](/finite-state-transducer/), and composing, determinizing and minimizing them are central operations.
- **Quality is measured, not proved.** Few results in the volume are theorems about correctness. Methods are compared by measures on held-out data, such as perplexity, word error rate or translation scores, and a method is better only on the data and measure on which it was tested.

## The chapters

**Chapter 41.1, Tokenization and text normalization**, is written in full. It covers [language identification](/language-identification/) and the [Cavnar-Trenkle method](/cavnar-trenkle-language-identification/), [tokenization](/text-tokenization/) and the [Penn Treebank](/penn-treebank-tokenization/) rules, [sentence boundary detection](/sentence-boundary-detection/) with [Punkt](/punkt-sentence-tokenizer/), [truecasing](/truecasing/), [word segmentation](/word-segmentation/) of text without spaces, [lemmatization](/lemmatization/), [morphological analysis](/morphological-analysis/), [two-level morphology](/two-level-morphology/) and [Morfessor](/morfessor/), and the subword vocabularies: [WordPiece](/wordpiece/), [fast WordPiece](/fast-wordpiece-tokenization/), [byte-level BPE](/byte-level-bpe/), the [unigram language model](/unigram-language-model-tokenization/), [subword regularization](/subword-regularization/), [BPE-dropout](/bpe-dropout/) and the [hardness of optimal tokenization](/optimal-tokenization-hardness/).

**Chapter 41.2, Word and sentence embeddings**, is not written yet. It will cover distributional vectors from counts, word2vec and GloVe, subword and contextual embeddings, sentence encoders and the evaluation of embeddings. Meanwhile, read [latent semantic analysis](/latent-semantic-analysis/) and [embedding](/embedding/) in Volume 25, the [singular value decomposition](/singular-value-decomposition/) in Volume 12 and [tf-idf](/tf-idf/) in Volume 35.

**Chapter 41.3, Language modeling**, is not written yet. It will cover n-gram models and their smoothing, from Good-Turing to Kneser-Ney, neural and recurrent language models, the transformer, pretraining, and the tuning of large models to instructions and preferences. Meanwhile, read the [cross-entropy loss](/cross-entropy-loss/) and [teacher forcing](/teacher-forcing/) in Volume 25 and [Shannon entropy](/shannon-entropy/) in Volume 24.

**Chapter 41.4, Text generation and decoding**, is not written yet. It will cover greedy and beam decoding, sampling with temperature, top-k and nucleus truncation, constrained and speculative decoding, and extractive and abstractive summarization. Meanwhile, read [beam search](/beam-search/) and [A* search](/a-star-search/) in Volume 29 and [inverse transform sampling](/inverse-transform-sampling/) in Volume 17.

**Chapter 41.5, Tagging and information extraction**, is not written yet. It will cover part-of-speech tagging, named entity recognition, chunking, relation and event extraction, coreference and entity linking. Meanwhile, read the [hidden Markov model](/hidden-markov-model/), the [conditional random field](/conditional-random-field/) and [structured prediction](/structured-prediction/) in Volume 25.

**Chapter 41.6, Syntactic and semantic parsing**, is not written yet. It will cover constituency parsing with probabilistic grammars, dependency parsing by transitions and by spanning trees, grammar formalisms beyond context-free, semantic parsing and discourse parsing. Meanwhile, read the [CYK algorithm](/cyk-algorithm/), the [probabilistic context-free grammar](/probabilistic-context-free-grammar/) and the [inside-outside algorithm](/inside-outside-algorithm/) in Volume 9, and the [Edmonds arborescence algorithm](/edmonds-arborescence/) in Volume 7.

**Chapter 41.7, Machine translation and alignment**, is not written yet. It will cover the IBM models and word alignment, phrase-based and syntax-based translation, neural translation with attention, and the automatic evaluation of translations. Meanwhile, read [expectation-maximization](/expectation-maximization/) in Volume 25, [global alignment](/global-alignment/) in Volume 27 and [edit distance](/edit-distance/) in Volume 8.

**Chapter 41.8, Speech analysis and synthesis**, is not written yet. It will cover the source-filter model, cepstral and filter-bank features, pitch and formant tracking, speech coding and modification, and text-to-speech from unit selection to neural vocoders. Meanwhile, read the [short-time Fourier transform](/short-time-fourier-transform/), the [cepstrum](/cepstrum/), [linear predictive coding](/linear-predictive-coding/) and [pitch detection](/pitch-detection/) in Volume 28.

**Chapter 41.9, Speech recognition**, is not written yet. It will cover hidden Markov acoustic models, decoding graphs built from weighted transducers, beam search over lattices, end-to-end models trained with connectionist temporal classification or attention, adaptation, word error rate, and speaker verification and diarization. Meanwhile, read the [Baum-Welch algorithm](/baum-welch-algorithm/) and the [Gaussian mixture model](/gaussian-mixture-model/) in Volume 25 and the [weighted automaton](/weighted-automaton/) in Volume 9.

## How to read this volume

There is no course through the volume yet. Read Chapter 41.1 in the order its opening page gives, and do the exercises marked ◦ at its end. For each other chapter, its opening page lists written entries elsewhere that cover part of its ground. When the volume is complete, the text chapters 41.1 to 41.7 will build on one another roughly in order, and the speech chapters 41.8 and 41.9 will form a pair that leans on the language models of Chapter 41.3.

Each entry stands on its own; its facts box lists what it needs, by entry number.

## What you need first

Chapter 41.1 needs the [Unicode code point](/unicode-code-point/) and [UTF-8](/utf-8/) from Chapter 8.8, [regular expressions](/regular-expression/) and finite-state transducers from Volume 9, the [trie](/trie/) from Volume 3 and [byte-pair encoding](/byte-pair-encoding/) from Volume 24. Its statistical entries use [maximum likelihood estimation](/maximum-likelihood-estimation/), the Viterbi and [forward-backward](/forward-backward-algorithm/) algorithms and expectation-maximization from Volume 25. The rest of the volume will lean on the same probability and on dynamic programming from Volume 2, and the speech chapters on the signal processing of Volume 28.

## The exercises

Chapter 41.1 ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
