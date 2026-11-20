A language model gives a probability to every string of words, or equivalently to each next word given the words before it. After "I would like a cup of", the word "tea" should get a high probability and "elephant" a low one. Such a model is the core of speech recognition, machine translation, spelling correction and text prediction, and in its largest neural forms it has become a general tool that answers questions and writes text from a prompt.

The chapter traces two lines. The first is the n-gram model, which counts word sequences and must decide how much probability to give to sequences it never saw; smoothing methods such as Kneser-Ney answer that question and remain strong baselines. The second is the neural model, from the feed-forward and recurrent models to the transformer, with its attention layers, positional encodings and the training methods of the large pretrained models. Perplexity measures both on held-out text.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **n-gram models and smoothing.** Language models, perplexity, Laplace and Good-Turing estimation, Katz backoff, deleted interpolation, absolute discounting, Witten-Bell, Kneser-Ney and its modified form, stupid backoff and entropy pruning.
2. **Other classical models.** Cache models and maximum entropy language models.
3. **Neural language models.** The neural probabilistic language model, recurrent models and noise-contrastive estimation.
4. **The transformer.** Scaled dot-product and multi-head attention, grouped-query attention, FlashAttention, sinusoidal and rotary position encodings, ALiBi, and selective state space models as an alternative.
5. **Pretraining.** Causal and masked language modeling, BERT, replaced token detection, GPT and scaling laws.
6. **Using and aligning large models.** In-context learning, chain-of-thought prompting, instruction tuning, LoRA, reinforcement learning from human feedback, preference reward models and direct preference optimization.

## What to read meanwhile

The smoothing ideas appear in information retrieval: [Jelinek-Mercer smoothing](/jelinek-mercer-smoothing/), [Dirichlet prior smoothing](/dirichlet-prior-smoothing/) and the [query likelihood model](/query-likelihood-model/) in Volume 35 treat each document as a small unigram model. Perplexity is an exponentiated [cross-entropy loss](/cross-entropy-loss/) (Volume 25); [Shannon entropy](/shannon-entropy/) and the [entropy rate](/entropy-rate/) of a source are in Volume 24. Chapter 41.1 of this volume uses unigram models of words and pieces throughout, for example in [word segmentation](/word-segmentation/) and the [unigram language model tokenization](/unigram-language-model-tokenization/).

For the neural models, read [backpropagation through time](/backpropagation-through-time/), the [vanishing gradient problem](/vanishing-gradient-problem/), [layer normalization](/layer-normalization/), [AdamW](/adamw/), [teacher forcing](/teacher-forcing/), [label smoothing](/label-smoothing/) and [knowledge distillation](/knowledge-distillation/) in Volume 25. The fine-tuning of large models by human preferences uses [proximal policy optimization](/ppo/) and the [policy gradient theorem](/policy-gradient-theorem/), also in Volume 25.
