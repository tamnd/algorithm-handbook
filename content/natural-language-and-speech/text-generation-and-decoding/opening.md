A language model gives a probability to each next token, but it does not say which text to produce. Taking the most probable token at each step is fast and often dull or repetitive. Searching for the most probable whole sequence with a beam is better for translation, yet for open-ended writing the most probable text is often short and bland, a fact known as the inadequacy of the mode. Sampling gives variety, and the methods that cut off the unlikely tail of the distribution, such as top-k and nucleus sampling, keep it from drifting into nonsense. Decoding is the set of algorithms that turn a model into text, and the choice of decoder can matter as much as the choice of model.

Decoding is also where most of the cost of a large model is paid. Caching the attention keys and values, and letting a small model propose tokens that a large one checks, make generation faster. The chapter will also cover the older pipeline of natural language generation and the summarization methods that pick or write the important sentences of a text, with the measures used to score them.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Search.** Autoregressive decoding, greedy decoding, beam search and its diverse, stochastic and grid-constrained variants, length normalization, minimum Bayes risk decoding, the inadequacy of the mode, and grammar-constrained decoding.
2. **Sampling.** Temperature, top-k, nucleus and typical sampling, contrastive search, repetition penalties and self-consistency.
3. **Speed.** Speculative decoding and the key-value cache.
4. **Training for generation.** Exposure bias and scheduled sampling.
5. **Generation and summarization.** The generation pipeline and referring expressions; Luhn's method, TextRank, LexRank and the pointer-generator network; and the ROUGE and BERTScore measures.

## What to read meanwhile

[Beam search](/beam-search/) and [A* search](/a-star-search/) are in Volume 29. The methods for sampling from a discrete distribution, such as [inverse transform sampling](/inverse-transform-sampling/) and [rejection sampling](/rejection-sampling/), are in Volume 17. [Teacher forcing](/teacher-forcing/), the training method whose mismatch with free-running generation is called exposure bias, is in Volume 25.

The graph methods of summarization rank sentences as [PageRank](/pagerank/) (Volume 7) ranks pages, by [power iteration](/power-iteration/) (Volume 12). Volume 35 has [maximal marginal relevance](/maximal-marginal-relevance/), which trades relevance against redundancy when choosing sentences, [query-biased snippets](/query-biased-snippet/), a small form of extractive summary, and [retrieval-augmented generation](/retrieval-augmented-generation/), which feeds retrieved passages to a generator.
