1. ◦ A model over the tokens a, b and `</s>` gives, at the empty prefix, $p(a) = 0.55$ and $p(b) = 0.45$; after a, $p(a) = 0.4$, $p(b) = 0.3$, $p(\text{</s>}) = 0.3$; after b, $p(\text{</s>}) = 0.7$, $p(a) = 0.2$, $p(b) = 0.1$; after any two tokens, `</s>` has probability 1. List the six outputs with their probabilities. What does [greedy decoding](/greedy-decoding/) return, and what is the mode? Does a [beam search](/beam-search/) of width 2 find the mode? Which output has the best log probability divided by its length, counting `</s>` as a token?

2. ◦ The logits of three tokens are $z = (3, 1, 0)$. Give the distribution of [temperature sampling](/temperature-sampling/) at $T = 0.5$, $T = 1$ and $T = 2$, to four decimals. What are the limits as $T \to 0$ and as $T \to \infty$?

3. ◦ A step gives the probabilities $(0.35, 0.20, 0.15, 0.12, 0.08, 0.06, 0.04)$ to seven tokens. Give the renormalized distribution of [top-k sampling](/top-k-sampling/) with $k = 3$, and the set kept by [nucleus sampling](/nucleus-sampling/) with $p = 0.8$, with its mass.

4. ◦ The reference is "the cat sat on the mat" and the candidate is "the cat was on the mat". Compute the [ROUGE](/rouge/)-1 recall, the ROUGE-2 recall and the ROUGE-L recall, precision and F with $\beta = 1$.

5. ◦ The source of a [pointer-generator network](/pointer-generator-network/) is "Macron visited Paris , Macron said", with attention $(0.3, 0.05, 0.4, 0.05, 0.15, 0.05)$ over the six positions. At this step $p_{\mathrm{gen}} = 0.7$, $P_{\mathrm{vocab}}(\text{Paris}) = 0.1$ and $P_{\mathrm{vocab}}(\text{said}) = 0.2$, and "Macron" is not in the vocabulary. Compute $P(\text{Macron})$, $P(\text{Paris})$ and $P(\text{said})$.

6. ◦ A decoder has $L = 40$ layers, width $d = 5120$ and $h = 40$ heads. Its [key-value cache](/key-value-cache/) stores 2 bytes per number. How much memory does one sequence of 4096 tokens need with $g = 8$ key-value heads, and how much with full multi-head attention?

7. ◦ For [speculative decoding](/speculative-decoding/), the target gives $p = (0.5, 0.3, 0.2)$ and the draft $q = (0.4, 0.4, 0.2)$ over the tokens a, b, c. Compute the acceptance rate $\alpha$ and the residual distribution. With independent acceptances, how many tokens does a step with $\gamma = 3$ draft tokens yield on average?

8. ◦ Each sampled answer is A with probability 0.5, B with 0.3 and C with 0.2, independently. A vote of three samples, as in [self-consistency](/self-consistency-decoding/), breaks ties uniformly at random. What is the probability that the vote returns A?

9. • In [Luhn's method](/luhn-summarization/), a sentence of 16 words has significant words (S) and others (x) in the pattern S x x S x x x x S S x x x x x S. Find its clusters and its score for the gap limits $g = 3$, $g = 4$ and $g = 5$. Does a larger gap limit always give a larger score?

10. • A [LexRank](/lexrank/) graph has four sentences; the cosine is above the threshold for the pairs 1–2, 1–3, 1–4 and 3–4, and every node has a self-loop. Find the stationary vector of the row-normalized matrix $B$ (that is, $d = 0$), and then solve $p = [\frac{d}{n}U + (1 - d)B]^{\mathsf T} p$ exactly for $d = 0.15$. Does the damping change the ranking?

11. • Three candidate translations A, B and C have model probabilities 0.4, 0.35 and 0.25. Their similarities are 0.2 for A and B, 0.3 for A and C, 0.9 for B and C, and 1 for a candidate with itself. Using the three candidates as the evidence, which candidate does [minimum Bayes risk decoding](/minimum-bayes-risk-decoding/) choose, and with what expected utility?

12. • Five sentences have lengths $(12, 9, 8, 7, 5)$ words and scores $(10, 8, 6, 6, 3)$, and the budget is 20 words. Find the best extract by the knapsack formulation of [automatic summarization](/automatic-summarization/). What does the greedy rule by score per word return?

13. • In [diverse beam search](/diverse-beam-search/) with groups of one hypothesis each, the first group has just chosen "the". The second group's candidates have scores the $-0.5$, a $-0.9$ and this $-1.6$. For which $\lambda$ does the second group choose a? With $\lambda = 0.5$, a third group has the same candidate scores; what does it choose, and for which $\lambda$ would it choose this?

14. • [Grid beam search](/grid-beam-search/) must include the phrases "New York" and "visa", with beam $k = 4$ and at most $n = 12$ steps. How many cells does the grid have, and what is the bound on model calls? Compare with a plain beam search of the same width. How does the bound change if a third phrase of five tokens is added?

15. • A model gives the first token a, b, c probabilities $(0.5, 0.3, 0.2)$. Two tokens are drawn without replacement, as [stochastic beam search](/stochastic-beam-search/) does at one step. What is the probability of the ordered pair (a, b), of the set {a, b}, and that a is among the two?

16. • [Contrastive search](/contrastive-search/) has three candidates with probabilities 0.5, 0.3 and 0.2 and largest cosine similarities 0.9, 0.2 and 0.1 to the context. Which candidate does it choose for $\alpha = 0.4$ and for $\alpha = 0.6$? For which ranges of $\alpha$ does each candidate win?

17. • The language is {aa, bb}. A model gives the first token a with probability 0.9 and b with 0.1; after a it gives a with 0.05, and after b it gives b with 0.9; after two tokens it ends. What law does [grammar-constrained decoding](/grammar-constrained-decoding/) with a token mask sample from, and what is the model's law conditioned on the language?

18. • For the distribution of Exercise 3, compute the entropy in nats and the set kept by [typical sampling](/typical-sampling/) with $\tau = 0.4$ and with $\tau = 0.5$. Compare with nucleus sampling at $p = 0.4$.

19. • The model of Exercise 6 has 13 billion parameters, stored at 2 bytes each, and $g = 8$. How many bytes of cache does one token add? At how many cached tokens does the cache equal the weights, and how many sequences of 4096 tokens fit below that?

20. ★ The target is $p = (0.5, 0.3, 0.2)$ and the draft $q = (0.2, 0.3, 0.5)$. Compute the law of the first token that speculative decoding outputs, case by case, and check that it is $p$. Then, with $\alpha = 0.7$ and a draft call that costs 0.1 of a target call, find the draft length $\gamma$ that gives the largest expected speed up, and the speed up.

21. ★ Four sentences have relevance $(1.0, 0.8, 0.8, 0.3)$ and pairwise similarities 0.6 for 1–2 and 1–3, 0 for 1–4, 0.1 for 2–3 and 0.2 for 2–4 and 3–4. A summary of two sentences scores the sum of the relevances minus their similarity. Find the best pair by brute force, and the pair chosen by [maximal marginal relevance](/maximal-marginal-relevance/) with $\lambda = 0.5$.

22. ★ The referent is a large brown dog with a red collar. The distractors are a large black dog with a red collar, a small brown cat with a red collar, a small brown dog with a blue collar and a large brown cat with a blue collar. Run the [incremental algorithm](/incremental-algorithm-referring-expressions/) with the preference order colour, size, collar, type, and find the length of the shortest distinguishing description.

23. ★ A model makes an error with probability $\varepsilon = 0.02$ after a correct token, and with probability $\beta$ after a wrong one. For $T = 50$ tokens, compute the expected number of wrong tokens when the model generates freely, for $\beta = 0.5$ and for $\beta = 1$. Compare with the count under teacher forcing, and relate the two cases to [exposure bias](/exposure-bias/).

24. ★ Each sample is correct with probability 0.4, and wrong samples spread over three other answers with probability 0.2 each. Ties in the vote are broken uniformly at random. Find the smallest number of samples $m$ for which the vote is correct with probability at least 0.9.
