Exercises 1, 11 to 13, 19, 22 and 25 use the training corpus of four sentences "a b c", "a b", "c b" and "b". Each sentence is padded with `<s>` in front and ends with `</s>`, so the vocabulary for prediction is {a, b, c, `</s>`}, there are 12 predicted tokens, and the bigram counts are taken within sentences.

1. ◦ Give the maximum likelihood estimates of the [bigram model](/n-gram-language-model/) for the corpus above. Compute the probabilities of the sentences "a b", "b c" and "a b c" and of "c a". Which bigram makes the last one impossible?

2. ◦ A model gives a held-out text of 5 words the total log probability $-20$ in bits, counting the end marker as one of the 5 predictions. Find the cross-entropy per token and the [perplexity](/perplexity/). Another model splits the same text into 9 subword tokens and gives it the same total probability. What is its perplexity per token, and why can the two numbers not be compared?

3. ◦ Treat the letters of "abracadabra" as tokens. Give the counts of counts $N_r$, the [Good-Turing](/good-turing-estimation/) estimate of the chance that the next letter is new, and $r^*$ for $r = 1$ and $r = 2$. What goes wrong at $r = 2$?

4. ◦ In a corpus of $N = 20$ tokens, $c(a\,b) = 3$, $c(a) = 6$, $c(c) = 5$ and the bigram "a c" never occurs. Compute the [stupid backoff](/stupid-backoff/) scores $S(b \mid a)$ and $S(c \mid a)$. Why can these scores not be summed to check the model?

5. ◦ One query $q = (1, 0, 1, 0)$ attends to the keys $(1, 1, 1, 1)$, $(0, 0, 1, 0)$ and $(-1, 0, 0, 0)$ with the values $(1, 0)$, $(0, 1)$ and $(2, 2)$. Compute the scaled scores, the weights to five decimals and the output of [scaled dot-product attention](/scaled-dot-product-attention/).

6. ◦ Compute the [sinusoidal positional encodings](/sinusoidal-positional-encoding/) of positions 1 and 2 for $d = 4$, with the base 10,000, to six decimals.

7. ◦ A [multi-head attention](/multi-head-attention/) layer has $d = 768$ and $h = 12$ heads. Give the head size, the number of weights of the four projections without and with biases, and the number of attention scores the layer computes for one sequence of 128 tokens.

8. ◦ [LoRA](/low-rank-adaptation/) with rank $r = 8$ adapts a $4096 \times 4096$ matrix. How many numbers does it train, and what share of the full matrix is that? How many does it train when it adapts $W^Q$ and $W^V$ in each of 32 layers?

9. ◦ A [cache language model](/cache-language-model/) gives the static model the weight 0.9 and a unigram cache of the last 50 words the weight 0.1. A word has static probability 0.001 and occurred 3 times in the last 50 words. Compute its probability, and the factor by which the cache raised it.

10. • Counts of counts of a trigram model are $n_1 = 120$, $n_2 = 40$, $n_3 = 20$ and $n_4 = 10$. Compute the three discounts of [modified Kneser-Ney](/modified-kneser-ney-smoothing/). Check that $D_1 < 1$, $D_2 < 2$ and $D_{3+} < 3$, so no seen count drops to zero.

11. • For the corpus above, compute the discount $D = n_1/(n_1 + 2 n_2)$ from the bigram counts of counts, the continuation unigram distribution, and the rows of the interpolated bigram model of [Kneser-Ney](/kneser-ney-smoothing/) for the histories a and c. Check that each row sums to 1.

12. • For the corpus above, build the interpolated bigram model of [Witten-Bell](/witten-bell-smoothing/), interpolating the unigram with the uniform distribution on the 4 tokens and the bigram with that unigram. Give the rows for `<s>` and c, and the probability of the sentence "c a" under Witten-Bell and under the Kneser-Ney model of Exercise 11.

13. • For the corpus above, build a backoff bigram model in the style of [Katz](/katz-backoff/), with an absolute discount of $1/2$ on every seen bigram and the maximum likelihood unigram as the lower order. Compute $\alpha(h)$ for the histories `<s>`, a, b and c and the full rows. Explain why the row for c is uniform.

14. • A [neural probabilistic language model](/neural-probabilistic-language-model/) has $|V| = 20{,}000$, two words of history, word vectors of size 50, 200 hidden units and direct connections from the word vectors to the output. Count its parameters, part by part.

15. • In [DPO](/direct-preference-optimization/) with $\beta = 0.1$, the policy gives the preferred response the log probability $-12$ and the other $-15$; the reference gives both $-14$. Compute the implicit reward margin, the loss and the weight $\sigma(-\text{margin})$ that scales the gradient.

16. • One query has the scores $(1, 3, 2, 4)$ against four keys with the scalar values $(1, 2, 3, 4)$. Run the online softmax of [FlashAttention](/flashattention/) with blocks of two keys. Give $m$, $\ell$ and the output after each block, and check the result against the full softmax.

17. • A scalar [selective scan](/selective-state-space-model/) has the steps $h_t = \alpha_t h_{t-1} + \beta_t$ with $\alpha = (1/2, 1/2, 1/4, 1)$, $\beta = (1, 2, 0, 1)$ and $h_0 = 0$. Compute the states one by one. Then compute the pairs $p_{12}$, $p_{34}$ and $p_{14} = p_{34} \circ p_{12}$ under the associative operator, and check that $p_{14}$ gives $h_4$.

18. • In [noise-contrastive estimation](/noise-contrastive-estimation/) with $k = 10$ noise samples, a data word has model score $u = 0.002$ and noise probability $q = 0.0005$. Compute the posterior that the word came from the data and the loss term of this word.

19. • Using the models of Exercises 11 and 12, compute the perplexity per predicted token of the sentence "a b c", of the sentence "c a", and of the two sentences taken together. Which model is better on each?

20. • A [scaling law](/neural-scaling-law/) has the Chinchilla form $L(N, D) = E + A/N^{\alpha} + B/D^{\beta}$ with $E = 1.69$, $A = 406.4$, $B = 410.7$, $\alpha = 0.34$ and $\beta = 0.28$. Compute $L$ for $N = 10^9$ parameters and $D = 2 \times 10^{10}$ tokens, and the compute $C \approx 6ND$.

21. ★ A [language model](/language-model/) emits `</s>` at step $i$, after $i - 1$ tokens, with probability $q_i$, whatever the tokens. For $q_i = 2^{-i}$, find the total probability of the finite sentences. For $q_i = 1/(i + 1)$, show that the model is tight, give the chance that a sentence has exactly $i$ tokens, and show that the expected length is infinite.

22. ★ For the corpus above with $D = 5/9$, compute $P(a \mid c)$ by interpolated [absolute discounting](/absolute-discounting/) with the maximum likelihood unigram, and by Kneser-Ney. Explain the difference from the contexts in which a occurs. State the condition on a word $w$ under which Kneser-Ney gives it less lower-order mass than the unigram.

23. ★ A [preference reward model](/preference-reward-model/) is fitted to comparisons among three responses: A beat B 3 times and lost once, B beat C 3 times and lost once, and A beat C 4 times and never lost. Fit the Bradley-Terry strengths by maximum likelihood, normalized to sum 1. Give the centered log strengths and the fitted chance of each win. What happens to the estimate if C never wins?

24. ★ With the law of Exercise 20 and $C = 6ND$, find the compute-optimal $N$ and $D$ for $C = 1.2 \times 10^{20}$, with the formula for $N_{\text{opt}}$. Give the loss and the ratio $D/N$, and compare with the rule of 20 tokens per parameter of Exercise 20.

25. ★ [Entropy-based pruning](/entropy-based-ngram-pruning/) is applied to the model of Exercise 13. Compute the new $\alpha'(c)$ after removing the bigram "c b", the new $p(b \mid c)$, the relative entropy $D$ (in nats) with $p(c) = 1/6$, and $e^D - 1$. Compare with the cost of removing "c `</s>`" instead.
