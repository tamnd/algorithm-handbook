## What to remember

- **Two questions.** A decoder either searches for the mode $\arg\max_y p(y \mid x)$ or draws a sample. Sampling takes one model call per token. The mode is hard in the worst case: undecidable for recurrent networks, and NP-hard even for a [hidden Markov model](/hidden-markov-model/). [Greedy decoding](/greedy-decoding/) and [beam search](/beam-search/) are heuristics for the mode, and no constant bounds how far greedy can fall below it.
- **The score favors short outputs.** Each token adds a term $\le 0$ to the log probability, so [length normalization](/length-normalization/) divides by $|Y|^\alpha$ or by the GNMT penalty $((5 + |Y|)/6)^\alpha$, with $\alpha$ tuned on data.
- **Truncation reshapes one step.** [Temperature](/temperature-sampling/) draws from $q_T \propto e^{z/T}$; [top-k](/top-k-sampling/) keeps the $k$ most probable tokens in $O(|V| + k \log k)$; [nucleus sampling](/nucleus-sampling/) keeps the smallest set of mass at least $p$; [typical sampling](/typical-sampling/) keeps the tokens whose surprisal is closest to the entropy $H$, and can drop the most probable token. Each samples exactly from the reshaped distribution, not the model.
- **The mode can be bad.** On one translation model the empty output was the mode for over half of the test sentences (Stahlberg and Byrne 2019), an observation, not a theorem. [Minimum Bayes risk decoding](/minimum-bayes-risk-decoding/) chooses the candidate with the best expected utility over samples, with $O(N^2)$ utility calls for $N$ samples; [self-consistency](/self-consistency-decoding/) is the same rule with the 0-1 loss, a plurality vote.
- **Exact sampling, faster.** [Speculative decoding](/speculative-decoding/) accepts a draft token with probability $\min(1, p/q)$ and otherwise draws from the normalized $\max(0, p - q)$. The output has exactly the target's law. With acceptance rate $\alpha = 1 - \mathrm{TV}(p, q)$, independent acceptances give $(1 - \alpha^{\gamma + 1})/(1 - \alpha)$ tokens per step. [Stochastic beam search](/stochastic-beam-search/) draws $k$ distinct outputs exactly, by the Gumbel-top-k trick.
- **Memory.** The [key-value cache](/key-value-cache/) holds $2Lndg/h$ numbers per sequence ($L$ layers, $n$ positions, width $d$, $g$ of $h$ heads).
- **Exposure bias.** A model that never recovers from an error can make of order $T^2 \varepsilon$ mistakes in $T$ steps, against $T\varepsilon$ under [teacher forcing](/teacher-forcing/), a worst case.
- **Summaries.** With fixed sentence scores and no redundancy, extractive selection under a word budget $K$ is the 0-1 [knapsack problem](/knapsack-problem/), solved in $O(nK)$; with pairwise redundancy it is NP-hard (McDonald 2007). The scores of [Luhn](/luhn-summarization/), [LexRank](/lexrank/) and [TextRank](/textrank/) are heuristics.
- **Metrics are measured.** [ROUGE](/rouge/) and [BERTScore](/bertscore/) are exact functions of their inputs; their agreement with human judgment is measured.

## The main methods side by side

| Method | Kind | Cost per step | What is guaranteed |
|---|---|---|---|
| [Greedy decoding](/greedy-decoding/) | deterministic search | one call, $O(\lvert V \rvert)$ argmax | the greedy rule only; no bound against the mode |
| Beam search with length normalization | heuristic search | $k$ calls and a top-$k$ over $k\lvert V \rvert$ | none; often more probable than greedy |
| [Top-k](/top-k-sampling/) and [nucleus](/nucleus-sampling/) | truncated sampling | one call, $O(\lvert V \rvert + k \log k)$ or a sort | an exact draw from the truncated distribution |
| [Grid beam search](/grid-beam-search/) | constrained search | at most $k(c + 1)$ calls | every output holds the constraints; exact only with an unbounded beam |
| [Stochastic beam search](/stochastic-beam-search/) | Gumbel-top-k | $k$ calls | $k$ outputs sampled exactly without replacement |
| [Minimum Bayes risk](/minimum-bayes-risk-decoding/) | reranking | $O(N^2)$ utility calls in all | the best candidate under the sample estimate of the risk |
| [Speculative decoding](/speculative-decoding/) | exact sampling | $\gamma$ draft calls, one target pass | the law of the target model |
| Knapsack selection | dynamic programming | $O(nK)$ in all | the best extract without redundancy |
| [LexRank](/lexrank/) | graph centrality | $O(n^2)$ per power step | the stationary vector; summary quality is measured |

: Decoders and summarizers. Here $V$ is the vocabulary, $k$ the beam width or the number of kept tokens, $c$ the number of constraint tokens, $N$ the number of samples, $\gamma$ the draft length, $n$ the number of sentences and $K$ the word budget.

## Choosing a method

- For translation, use beam search with a small beam and length normalization, or minimum Bayes risk over samples when the extra time is affordable.
- For open-ended writing, sample with a temperature below 1 and nucleus or top-k truncation. Add a repetition penalty if the model loops.
- For structured output, such as JSON, use grammar-constrained decoding; masking token by token changes the distribution.
- To speed up a large model without changing its output law, use a key-value cache and speculative decoding.
- For an extract under a word budget, score sentences with LexRank or TextRank, select by knapsack or maximal marginal relevance, and check with ROUGE and with people.
