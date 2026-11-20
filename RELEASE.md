The Handbook of Algorithms, edition 0.43.0: the written areas of [algorithm.tamnd.com](https://algorithm.tamnd.com)
as books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/algorithm` v0.43.0](https://github.com/tamnd/algorithm/releases/tag/v0.43.0)
(`3a1b64f389c36ce619d8bc88f9e941cd8c7379fd`); the edition number follows the release of the site.

| | Volume | Entries | Pages |
|---|---|---:|---:|
| 0 | Guide and Index | the whole set | 2,279 |
| 1 | Foundations | 204 | 1,000 |
| 2 | Techniques | 208 | 1,123 |
| 3 | Data structures | 427 | 3,140 |
| 4 | Sorting | 156 | 910 |
| 5 | Searching | 115 | 646 |
| 6 | Sequences | 120 | 596 |
| 7 | Graphs | 685 | 3,693 |
| 8 | Strings | 259 | 1,632 |
| 9 | Automata and parsing | 270 | 1,604 |
| 10 | Number theory | 238 | 1,438 |
| 11 | Algebra | 328 | 2,122 |
| 12 | Numerical | 463 | 3,004 |
| 13 | Geometry | 280 | 1,796 |
| 14 | Combinatorics | 174 | 877 |
| 15 | Optimization | 301 | 1,766 |
| 16 | Logic and constraints | 325 | 2,106 |
| 17 | Randomized | 141 | 840 |
| 18 | Approximation | 213 | 1,309 |
| 19 | Online and streaming | 195 | 1,135 |
| 20 | Parallel | 128 | 897 |
| 21 | Distributed | 281 | 2,060 |
| 22 | Concurrency | 155 | 2,240 |
| 23 | Cryptography | 389 | 3,128 |
| 24 | Compression and coding | 220 | 1,741 |
| 25 | Machine learning | 419 | 2,982 |
| 26 | Systems | 346 | 2,550 |
| 27 | Biology | 468 | 3,346 |
| 28 | Graphics and signals | 594 | 4,817 |
| 29 | Games and search | 205 | 1,592 |
| 30 | Quantum | 152 | 1,582 |
| 31 | CAD | 374 | 3,027 |
| 32 | Electronic design automation | 358 | 2,690 |
| 33 | Statistics and inference | 276 | 2,168 |
| 34 | Compilers and program analysis | 272 | 2,793 |
| 35 | Information retrieval and AI reasoning | 276 | 1,716 |
| 36 | Control | 279 | 2,334 |
| 37 | Robotics | 264 | 2,135 |
| 38 | Computer vision | 277 | 2,593 |
| 39 | Complexity | 284 | 1,225 |
| 40 | Databases | 296 | 2,420 |
| 41 | Natural language and speech | 299 | 2,157 |
| 42 | Algorithmic game theory | 6 | 102 |
| 43 | Scientific computing | 3 | 91 |
| 45 | Security and privacy | 2 | 75 |
| 46 | Imaging and inverse problems | 1 | 61 |
| | **All** | **11,726** | **85,538** |

- **Volume 41, Natural language and speech**, now has all nine of its chapters written, 299 entries in all (22 in
  0.42.0). Eight new chapters: *Word and sentence embeddings* (32 entries: count vectors and PMI, word2vec, GloVe
  and subword vectors, contextual and sentence embeddings, bias tests, word senses), *Language modeling* (41:
  n-gram smoothing from Laplace to modified Kneser-Ney, neural and recurrent models, attention and the
  transformer, pretraining, fine-tuning and preference training, scaling laws), *Text generation and decoding*
  (29: greedy and beam decoding, sampling and truncation, constrained, speculative and minimum Bayes risk decoding,
  summarization and its metrics), *Tagging and information extraction* (26: HMM, MEMM and CRF taggers, named
  entities, relation extraction, coreference and entity linking), *Syntactic and semantic parsing* (33: PCFG and
  span-based constituency parsing, transition-based and graph-based dependency parsing, grammar formalisms,
  semantic parsing and meaning representations), *Machine translation and alignment* (36: the IBM and HMM
  alignment models, phrase-based and hierarchical translation, neural translation with attention, evaluation by
  BLEU, chrF, TER and COMET), *Speech analysis and synthesis* (36: the source-filter model, cepstral and mel
  features, pitch, formants and voice activity, noise reduction, coding by CELP, grapheme-to-phoneme conversion,
  concatenative, parametric and neural synthesis) and *Speech recognition* (44: HMM acoustic models, decoding graphs from weighted transducers,
  discriminative training, CTC, transducer and attention models, speaker recognition and diarization). The
  introduction of the volume is rewritten for the complete volume.
- **Volume 0, Guide and Index**, covers the whole set of 11,726 entries and has a new learning path, *Natural
  language and speech*, in six stages from text and probability to speech.
- The other volumes have the same entries under the same numbers as in 0.42.0. The entries have the corrections
  that the site made up to its release v0.43.0, among them those found while writing edition 0.42.0 in Volume 40
  and Chapters 8.8 and 41.1.
- A tag-like word written as bare text in an entry, such as the sentence markers `<s>` and `</s>`, is now set as
  code; before, it was read as an HTML tag, dropped from the PDF and left the EPUB malformed.
- Volume 44 (Communications) is not built: the site has only short pages for it so far. Volume 0 lists its
  chapters.

**Files.** For each volume `NN-area`: `handbook-of-algorithms-0.43.0-NN-area.pdf`, `.epub`, and `-tex.tar.gz`
(`main.tex`, `body.tex`, `handbook.sty` and the figures; compile `main.tex` with XeLaTeX or tectonic).
`…-all-pdf.zip` and `…-all-epub.zip` hold every volume; `SHA256SUMS` lists the checksums.

Entry and statement numbers (such as 4.1.12 and Lemma 4.1.12.2) belong to this edition. The entries are the text of
the site; the learner pages were drafted by agents and checked as described in `content/PROVENANCE.md`. Text
CC BY-SA 4.0, code MIT. Report errors in an entry at https://github.com/tamnd/algorithm/issues and errors in the
books at https://github.com/tamnd/algorithm-handbook/issues.
