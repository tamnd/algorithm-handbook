## What to remember

- A **tokenizer** is specified in one of three ways: by rules, as in [Penn Treebank tokenization](/penn-treebank-tokenization/); by a vocabulary and an encoding rule, as in [WordPiece](/wordpiece/); or by an objective. With a fixed vocabulary whose longest piece has length $L$, the tokenization with the fewest tokens is a shortest path on the $n + 1$ positions, found in $O(nL)$ time.
- An [out-of-vocabulary](/out-of-vocabulary-word/) token is one the training text never had. The [Good-Turing](/good-turing-estimation/) estimate of the chance that the next token is new is $N_1/N$, the share of tokens whose type occurs once. Heaps' law and Zipf's law are measured, not proved.
- **Sentence boundaries** come from a decision at each period. [Punkt](/punkt-sentence-tokenizer/) needs no labels: it scores each word type by a scaled likelihood ratio and calls it an abbreviation when $S \ge 0.3$. For a type never seen without a period, $\log \lambda = 2k \ln(0.99/p) > 0$, so a frequent ordinary word can pass the threshold.
- **Word segmentation** of a string of $n$ characters has $2^{n-1}$ candidate splits, but under a unigram model the best one is found by [dynamic programming](/word-segmentation/) in $O(nL)$ time. [Maximum matching](/maximum-matching-segmentation/) takes the longest dictionary word at each step in $O(nm)$ time; it does not always give the fewest words.
- **Morphology is finite-state.** The analyses of a word form a regular relation, computed by a [finite-state transducer](/finite-state-transducer/). Rewrite rules that do not apply to their own output, and cascades of them, are regular (Kaplan and Kay). [Two-level](/two-level-morphology/) rules work on same-length relations, which are closed under intersection; general regular relations are not.
- **Subword methods are greedy or probabilistic.** Each BPE merge lowers the token count of the training corpus by exactly the non-overlapping count of the merged pair. WordPiece merges the pair with the largest gain in unigram log likelihood. The [unigram model](/unigram-language-model-tokenization/) is trained by EM, which never lowers the likelihood, and then pruned by a heuristic. None of them is proved to give the best vocabulary of its size.
- **Coverage.** A vocabulary with every single character, or with all 256 bytes as in [byte-level BPE](/byte-level-bpe/) ($256 + K$ units after $K$ merges), encodes every input with no unknown token.
- **Optimal is hard.** Choosing a vocabulary of $K$ pieces, or $K$ merges, that gives the fewest tokens is NP-complete, by reduction from max-2-SAT ([Whittington, Bachmann and Pimentel](/optimal-tokenization-hardness/)). With one merge, the greedy choice is the best merge.

## The main methods side by side

| Method | Kind | Encoding time | What is guaranteed |
|---|---|---|---|
| [Penn Treebank rules](/penn-treebank-tokenization/) | rules | $O(n)$ | the output of the rules, nothing more |
| [Maximum matching](/maximum-matching-segmentation/) | greedy, dictionary | $O(nm)$ | a total segmentation; not the fewest words |
| [Unigram word segmentation](/word-segmentation/) | dynamic programming | $O(nL)$ | the most probable split under the model |
| [Cavnar-Trenkle](/cavnar-trenkle-language-identification/) | rank distance | $O(n + G \log G)$ profile, $O(kL)$ compare | none; accuracy is measured |
| [Punkt](/punkt-sentence-tokenizer/) | unsupervised statistics | $O(n)$ expected | none; error rates are measured |
| [WordPiece](/wordpiece/) | greedy merges | $O(n^3)$ per word, as in the BERT code | longest match at each position |
| [Fast WordPiece](/fast-wordpiece-tokenization/) | trie with failure links | $O(n)$ per word | the WordPiece output (condition in the entry) |
| [Byte-level BPE](/byte-level-bpe/) | greedy merges on bytes | $O(nb)$ | every byte string is covered |
| [Unigram LM](/unigram-language-model-tokenization/) | EM and pruning | $O(nm)$ Viterbi | the most probable segmentation under the model |

: The main methods of the chapter. Here $n$ is the length of the input (for WordPiece, of one word), $m$ the length of the longest dictionary word or piece, $L$ the length of the longest word in the model or the profile length, $G$ the number of distinct n-grams of the input, $k$ the number of languages and $b$ the length of the longest pre-token in bytes.

## Choosing a method

- For English text that feeds a tool trained on the Penn Treebank, use its rules, so that the tokens match. For other languages, start from the [Unicode word rules](/unicode-text-segmentation/).
- To split sentences without labeled data, train Punkt on a large text of the same kind, and check the abbreviations it learns.
- For Chinese or Japanese, maximum matching is a fast baseline; with word counts, use the unigram dynamic program.
- For a neural model, use a subword method. Byte-level BPE never fails on any input; the unigram model gives a probability to every segmentation; WordPiece with fast encoding suits large-scale serving.
- To make a model robust to segmentation, train with [subword regularization](/subword-regularization/) or BPE-dropout, and encode deterministically at test time.
