1. ◦ In [IBM Model 1](/ibm-model-1/), the target is "the house" with a null word and the source is "das Haus". The table has $t(\text{das} \mid \text{NULL}) = 0.1$, $t(\text{das} \mid \text{the}) = 0.6$, $t(\text{das} \mid \text{house}) = 0.1$, $t(\text{Haus} \mid \text{NULL}) = 0.1$, $t(\text{Haus} \mid \text{the}) = 0.1$ and $t(\text{Haus} \mid \text{house}) = 0.7$. How many alignments are there? Compute $p(f \mid e)$ as a multiple of $\varepsilon$, the posterior probability that "das" links to "the", and the best alignment.

2. ◦ Hand alignments have the sure links $S = \{(1,1), (2,2), (3,4)\}$ and the possible links $P = S \cup \{(2,3), (3,3)\}$. Compute the [alignment error rate](/alignment-error-rate/) of $A_1 = \{(1,1), (2,2), (2,3), (3,4)\}$ and of $A_2 = \{(1,1), (2,3), (3,3)\}$.

3. ◦ Compute the clipped precisions $p_1, \ldots, p_4$, the brevity penalty and [BLEU](/bleu/) for the candidate "a cat is on the mat" against the single reference "the cat is on the mat".

4. ◦ Without shifts, [TER](/translation-edit-rate/) is the word edit distance over the reference length. Compute it for the hypothesis "the cat sat" against the reference "the cat sat on the mat", and again with the two sentences exchanged.

5. ◦ Which of these word orders can an [inversion transduction grammar](/inversion-transduction-grammar/) produce one to one: 2 1 4 3, 3 4 1 2, 2 4 1 3, 4 3 2 1, 3 1 4 2, 1 3 2 4?

6. ◦ A source $f_1 f_2 f_3$ and a target $e_1 e_2 e_3$ have the links $f_1$–$e_1$, $f_2$–$e_3$ and $f_3$–$e_2$. List all phrase pairs consistent with the alignment, as [phrase-pair extraction](/phrase-pair-extraction/) defines them.

7. ◦ A phrase-based decoder covers the source spans $(0, 2)$, $(4, 6)$, $(2, 4)$ and $(6, 7)$ of a 7-word sentence, in this order (fenceposts). Give the orientation of each phrase in the [lexicalized reordering model](/lexicalized-reordering-model/), taking the start of the sentence as the end of a phrase before the first.

8. ◦ A [log-linear model](/log-linear-translation-model/) has the features $h_1 = \log p(e)$, $h_2 = \log p(f \mid e)$ and $h_3$ the number of words. The candidates have the feature vectors A $(-4, -3, 3)$, B $(-5, -2.5, 4)$ and C $(-6, -1.8, 5)$. Which candidate wins with the weights $(1, 1, 0)$, which with $(1, 1, 0.5)$, and which with $(2, 2, 1)$? Which of these weight vectors gives the [noisy channel model](/noisy-channel-translation-model/)?

9. • Run two rounds of EM for IBM Model 1, with $t(f \mid e)$ and no null word, on the corpus ("the house", "la maison") and ("the flower", "la fleur"), starting from the uniform table over the three French words. Give $t(\text{la} \mid \text{the})$ and $t(\text{maison} \mid \text{house})$ after each round.

10. • With the [Gale-Church](/gale-church-alignment/) costs ($c = 1$, $s^2 = 6.8$, priors 0.89 for 1-1, 0.089 for 2-1 and 0.0099 for 1-0, and the program form $\bar l = (l_1 + l_2/c)/2$, $\delta = (c\,l_1 - l_2)/\sqrt{s^2 \bar l}$), compute the cost of the 1-1 bead (100 | 110). A 40-character sentence follows the 100-character one. Compare the 2-1 bead (100 + 40 | 110) with the 1-1 bead followed by a 1-0 bead for the short sentence, and say which the alignment prefers.

11. • For one source sentence, [minimum error rate training](/minimum-error-rate-training/) has three candidates with features $(h_1, h_2)$ and errors: A $(-2, -3)$ with 2 errors, B $(-3, -1)$ with 1 error, C $(-5, 0)$ with 3 errors. The weights are $w = (1, \gamma)$. Find the upper envelope of the three lines in $\gamma$, the winning candidate on each interval, and the set of $\gamma$ with the fewest errors.

12. • A test set has two sentences. The first hypothesis is "the cat sat" with the reference "the cat sat on the mat"; the second is "a dog ran in the park and then it slept for an hour" with the reference "a dog ran in the park". Compute corpus BLEU, and the brevity penalty the first sentence would get on its own. What does the example show?

13. • Compute [chrF](/chrf/) with character orders 1 and 2 for the hypothesis "cat" against the reference "cats", with $\beta = 2$ and with $\beta = 1$. Which error costs more under $\beta = 2$, a missing character or an extra one?

14. • TER allows block shifts. Compute the edit distance and the TER of the hypothesis "b c a" against the reference "a b c", and check that the shift satisfies the constraints of the greedy search.

15. • In [fast_align](/fast-align/) with tension $\lambda = 4$, take $m = 2$ source words, $l = 4$ target words and the source position $j = 1$. Compute the distortion probabilities of the target positions $i = 1, \ldots, 4$, leaving out the null word, and show that the normalizer is $(1 + e^{-1})^2$.

16. • In a chart cell, [cube pruning](/cube-pruning/) combines one rule with two sorted lists of child items, each with scores 0, $-1$, $-3$. The language model adds a junction score that is $-3$ for the combinations (1, 1) and (2, 1), $-4$ for (1, 2), and 0 for the rest (indices from 1). Run cube pruning with $k = 2$ and with $k = 3$ pops. Which items does it return, and what is the best item of the grid?

17. • The sentence pair "er hat das Buch gelesen" / "he has read the book" has the links er–he, hat–has, das–the, Buch–book and gelesen–read. Write the [hierarchical](/hierarchical-phrase-based-translation/) rule obtained by replacing "das Buch" / "the book" with a gap in the phrase pair "hat das Buch gelesen" / "has read the book", and the rule with two gaps for the whole sentence pair that replaces "er" / "he" as well.

18. • With [dot-product attention](/multiplicative-attention/), the decoder state is $(1, 0)$ and the encoder states are $(2, 0)$, $(0, 1)$ and $(1, 1)$. Compute the attention weights and the context vector.

19. • References for one source are "a b" and "b a", each with probability 1/2. A [non-autoregressive](/non-autoregressive-translation/) model with independent positions is fitted to them by maximum likelihood. What are its two position distributions, and with what probability does it output a string that is neither reference? What changes if the training targets are distilled to "a b" only?

20. ★ Prove that the log-likelihood of IBM Model 1 is a concave function of the translation table, and conclude that every fixed point of EM in the interior attains the global maximum value. Show that on the corpus ("a b", "x y"), ("a b", "x x"), without a null word, more than one table attains it.

21. ★ Show that the number $a_n$ of separable permutations has the generating function $A(x)$ solving $A^2 - (1 - x)A + x = 0$, and compute $a_7$.

22. ★ Show that finding the best translation under IBM Model 1 with a bigram language model, with free word order, is NP-hard, by a reduction from the Hamilton cycle problem.

23. ★ Prove that along a line $w + \gamma d$ each candidate of an $n$-best list is the model's choice on one interval of $\gamma$ or on none, and derive the $O(n \log n)$ envelope computation that makes the MERT line search exact.

24. ★ For a one-to-one alignment given by a permutation $\pi$ of $n$ positions, show that the consistent phrase pairs are the intervals of positions that $\pi$ maps to intervals. Prove that all $n(n+1)/2$ intervals qualify only when $\pi$ is the identity or the reversal ($n \ge 3$), and count the pairs for 2 4 1 3.
