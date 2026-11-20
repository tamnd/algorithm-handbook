1. ◦ Apply the rules of [Penn Treebank tokenization](/penn-treebank-tokenization/) to the line `We'll pay $5 (cash) -- won't you?` and list the tokens. Then do the same for `I met Dr. Smith at 5 p.m.` What happens to the abbreviation at the end of the second line?

2. ◦ A model is trained on the text "to be or not to be that is the question" and tested on "to sleep or not to sleep". What share of the test tokens are [out of vocabulary](/out-of-vocabulary-word/)? What share of the test types? What does the Good-Turing estimate $N_1/N$ computed on the training text say about the chance that the next token is new?

3. ◦ List the strings that the suffix rules of the WordNet [lemmatizer](/lemmatization/) produce for the noun "boxes", the noun "wolves" and the verb "studies". Leave out the exception list and the form itself, and stop before the check against WordNet.

4. ◦ The dictionary is {the, them, theme, me, men, menu, nu}. Segment "themenu" by forward and by backward [maximum matching](/maximum-matching-segmentation/). Which result does the bidirectional rule choose, and at which step of its tie rule is the choice made?

5. ◦ How many bytes does the string "café 日本" take in [UTF-8](/utf-8/) (with one space)? How many base tokens does [byte-level BPE](/byte-level-bpe/) start from on it, before any merge? The GPT-2 vocabulary has 50,257 units; split this number into its three parts.

6. ◦ The vocabulary is {un, ##aff, ##able, u, ##n, ##a, ##ff, ##ab, ##le}. Encode "unaffable" with the [WordPiece](/wordpiece/) encoder of the BERT code and count the lookups in $V$. What does it return for "nab"?

7. ◦ A [unigram model](/unigram-language-model-tokenization/) gives the pieces b, u, g and s probability 0.1 each, bu 0.05, ug 0.2, bug 0.15, gs 0.1 and ugs 0.05. List the segmentations of "bugs" with their probabilities. Which one does the Viterbi pass return, what is $P(\text{bugs})$, and what is the posterior probability of the Viterbi segmentation?

8. ◦ With profile length $L = 6$, a language profile is $Q$ = (e, t, a, o, n, h) and a short text gives the profile $P$ = (t, h, e, x), ranks from 0. Compute the [out-of-place distance](/cavnar-trenkle-language-identification/) $\operatorname{oop}(P, Q)$ and also $\operatorname{oop}(Q, P)$, with the penalty $L$ for a missing n-gram.

9. • The vocabulary is {a, b, ab, ba, aba, bab}. Find the fewest tokens for "ababab" and for "abababa", and the number of tokenizations that reach the minimum in each case. Set up the computation as a shortest path, as in [tokenization](/text-tokenization/), and count paths in the same pass.

10. • Every single character counts as a word, and the dictionary also holds aaa and aaaa. Segment $a^6$ by forward and by backward maximum matching. Show that both give more words than the fewest possible, so the bidirectional rule cannot repair this case.

11. • A unigram model has the counts no 10, now 8, where 7, here 6, he 5, man 9, nowhere 1 and a 14, a total of 60. List the segmentations of "nowhereman" into these words, find the most probable one by the [word segmentation](/word-segmentation/) dynamic program, and compare it with the result of forward maximum matching with the same words as dictionary.

12. • The training corpus of [subword tokenization](/subword-tokenization/) is aaaa three times and aab twice. Count the pair a a with overlaps and without. Make the first BPE merge and count the tokens before and after it. Which count gives the drop in the number of tokens, and why?

13. • A vocabulary holds every string of length at most 3 over the alphabet. In how many ways can a string of 8 characters be split into pieces of the vocabulary? Give the recurrence, and compare with the $2^{7}$ splits when every length is allowed.

14. • For the model of Exercise 7 and a corpus of the single word "bugs", run the [forward-backward](/forward-backward-algorithm/) pass. Give the expected number of uses of bug and of s, and the expected number of pieces in the segmentation. What probability does one M step of EM give to s?

15. • The BPE merge list is (a, b), (ab, c), (b, c). Give the distribution of the segmentation of "abc" under [BPE-dropout](/bpe-dropout/) with $p = 0.1$. Which segmentation in it can plain BPE never produce for this word?

16. • In [subword regularization](/subword-regularization/) the sampler draws $s$ with probability proportional to $P(s)^a$. What distribution does it give at $a = 0$? For the word "hugs" with the model of the unigram entry, which has seven segmentations, compare the probability of hug s at $a = 0$ and at $a = 1$.

17. • In [Punkt](/punkt-sentence-tokenizer/), take $p = C(\bullet)/N = 0.25$ and a word type with no internal period that occurs $k$ times, always followed by a period. Find the least $k$ that makes it an abbreviation when its length is 3, 4 and 5 characters.

18. • A corpus has the words ta 5, te 3 and ka 4. Which pair does BPE merge first? Which pair does WordPiece merge first, by the likelihood gain? Give the three gains.

19. • The vocabulary is {a, ##a}. How many lookups does the WordPiece encoder of the BERT code make on the word $a^n$? Give the count for $n = 10$, the order of the total number of characters it hashes, and the number of steps that [fast WordPiece](/fast-wordpiece-tokenization/) needs on the same word.

20. ★ Show that the greedy longest-match encoder can use far more tokens than the fewest possible, even when $V$ holds every single character: for each $m \ge 2$ give a vocabulary and a word on which it uses $m$ tokens and the optimum uses 2. Then prove that its count is never more than $L$ times the optimum, where $L$ is the length of the longest piece of $V$.

21. ★ The corpus is bccb 4 times, abcc once and cccb 4 times, and $K = 2$. Run greedy BPE with counts without overlaps. Then find the least number of tokens over all sequences of two merges, and over all vocabularies of two extra pieces with the best tokenization of each word. Compare with the example in the [hardness entry](/optimal-tokenization-hardness/).

22. ★ Prove that same-length regular relations are closed under intersection, the fact on which [two-level morphology](/two-level-morphology/) rests. Then show that regular relations in general are not: give two regular relations whose intersection has a range that is not a regular language.

23. ★ Prove that one EM step for the [unigram language model](/unigram-language-model-tokenization/) never lowers the log likelihood of the corpus. Use Jensen's inequality on the posterior over segmentations, and say where the M step uses the fact that the piece probabilities must sum to 1.

24. ★ Prove that for $K = 1$ the merge that leaves the fewest tokens is the pair with the largest count without overlaps. Give a corpus on which the pair with the largest count with overlaps is a worse merge. Then show that the best vocabulary of one extra piece can give far fewer tokens than the best single merge.
