## What to remember

- **Viterbi is exact and linear in the length.** For a first-order model with $k$ tags, [Viterbi](/viterbi-algorithm/) finds the best tag sequence in $O(nk^2)$ time and $O(nk)$ space; for order $m$ it takes $O(nk^{m+1})$, so a trigram tagger with 45 tags does $45^3 = 91125$ steps per word. It is exact for HMMs and linear-chain CRFs. Posterior decoding maximizes the expected number of correct tags instead.
- **Spans become tags.** With $|T|$ entity types the [BIO encoding](/bio-encoding/) uses $2|T| + 1$ tags. Valid IOB2 sequences and sets of non-overlapping typed spans are in bijection. The [span F1](/span-f1-score/) is $2\mathrm{TP}/(2\mathrm{TP} + \mathrm{FP} + \mathrm{FN})$, summed over the corpus; a span with a wrong boundary counts once as a false positive and once as a false negative.
- **Local normalization causes label bias.** A [maximum entropy Markov model](/maximum-entropy-markov-model/) normalizes each step, so a state with one successor passes on all its mass whatever the input says. This is a property of every locally normalized model. A [conditional random field](/conditional-random-field/) has one normalizer per sentence and avoids it; training an MEMM needs only $O(Nk)$ score evaluations per gradient, against forward-backward for a CRF.
- **The perceptron bound.** On data separable with margin $\delta$, where every feature difference has norm at most $R$, the [structured perceptron](/structured-perceptron/) makes at most $R^2/\delta^2$ mistakes, whatever the order of the examples. Each epoch costs $\Theta(nk^2)$ for decoding. The averaged weights gave clear gains in Collins's experiments, a measurement.
- **Segments.** A [semi-Markov CRF](/semi-markov-crf/) labels segments of length at most $L$ in $O(nLk^2)$ time; with $L = 1$ it is the linear-chain CRF.
- **Coreference is clustering.** $n$ mentions have $B_n$ partitions, a [Bell number](/bell-numbers/), and $n!$ antecedent forests. The best partition under pairwise scores is [correlation clustering](/correlation-clustering/), NP-hard. The [mention-pair model](/mention-pair-model/) links greedily in $O(n^2 d)$ and takes the transitive closure. Scores disagree: MUC counts links, [B-cubed](/b-cubed-metric/) counts mentions, and the CoNLL score averages MUC, B-cubed and CEAF-e.
- **Global choices are hard.** Choosing the entities of all mentions together in [entity linking](/entity-linking/), with pairwise coherence, is NP-hard by reduction from maximum cut; a chain of coherence terms is solved by dynamic programming in $O(kc^2)$.
- **Measured, not proved.** Tagging accuracies near 97%, NER F1 above 90 on CoNLL-2003 and coreference F1 near 67 for the first end-to-end model are measurements on one test set, as are the gains of each part of the [BiLSTM-CRF](/bilstm-crf/).

## The main methods side by side

| Method | Kind | Decoding time | What is guaranteed |
|---|---|---|---|
| [HMM tagger](/hmm-part-of-speech-tagger/) | generative, counted | $\Theta(nk^{m+1})$ for order $m$ | the most probable tags under the model |
| [Brill tagger](/brill-tagger/) | learned rewrite rules | one pass per rule | each rule cut the training errors by at least the threshold when chosen |
| [MEMM](/maximum-entropy-markov-model/) | locally normalized | $O(nk^2)$ | exact decoding; label bias |
| [Structured perceptron](/structured-perceptron/) | global, mistake-driven | $O(nk^2)$ | at most $R^2/\delta^2$ mistakes on separable data |
| Linear-chain CRF, [BiLSTM-CRF](/bilstm-crf/) | globally normalized | $O(nk^2)$ | exact decoding and exact gradients |
| [Semi-Markov CRF](/semi-markov-crf/) | segment model | $O(nLk^2)$ | exact over segments of length at most $L$ |
| [Mention-pair model](/mention-pair-model/) | pair classifier and greedy linking | $O(n^2 d)$ | none; the closure can join incompatible mentions |
| [Span-ranking](/span-ranking-coreference/) | neural, pruned spans | $O(nK)$ pairs after pruning | none; F1 is measured |
| [DIPRE](/dipre/) | bootstrapped patterns | one scan of the pages per round | none; the loop stops |

: The main methods of the chapter. Here $n$ is the number of tokens (for coreference, of mentions), $k$ the number of tags, $L$ the longest segment, $d$ the number of features of a pair and $K$ the number of antecedents kept per span.

## Choosing a method

- For fast tagging, a trigram HMM with a tag dictionary is a strong baseline. With labeled data and rich features, train a CRF or a structured perceptron; the perceptron is simpler and needs no normalizer.
- For named entities and chunks, use BIO tags with a CRF layer, on top of a BiLSTM or a pretrained encoder. Decode with the forbidden transitions removed, so that every output is a valid span set, and report span F1, not token accuracy.
- If spans need features of the whole span, use a semi-Markov model.
- For coreference, use a span-ranking model where data allow it; the mention-pair model with best-first linking is a transparent baseline. Report MUC, B-cubed and CEAF-e, not one of them alone.
- To fill a knowledge base, link the entities first, then extract relations. Distant supervision gives cheap training data with noisy labels; DIPRE needs only seeds but can drift to wrong patterns, so set its threshold high.
