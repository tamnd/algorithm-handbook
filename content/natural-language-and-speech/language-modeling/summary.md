## What to remember

- A **language model** is a distribution over sentences, $P(w_1 \ldots w_n) = \prod_i P(w_i \mid w_1 \ldots w_{i-1})$, with an end marker. [Perplexity](/perplexity/) on $N$ held-out tokens is $P(w_1 \ldots w_N)^{-1/N}$; the uniform model over $V$ has perplexity $|V|$. Compare perplexities only over the same tokens.
- An [n-gram model](/n-gram-language-model/) by maximum likelihood gives zero to unseen n-grams. Each smoothing method is an estimator that moves mass to them and still sums to 1, and is judged by held-out perplexity. [Laplace](/laplace-smoothing/) gives $(c + 1)/(c(h) + |V|)$ and takes too much mass when $|V|$ is large.
- **Good-Turing** puts $N_1/N$ on all unseen types together and replaces a count $r$ by $r^* = (r+1) N_{r+1}/N_r$. The raw $N_r$ have gaps; [simple Good-Turing](/simple-good-turing/) fits a line to $\log N_r$ against $\log r$.
- **Discounting.** [Absolute discounting](/absolute-discounting/) subtracts $D = N_1/(N_1 + 2N_2)$ from each seen count. [Katz](/katz-backoff/) backs off with a weight $\alpha(h)$ that makes each row sum to 1, [Witten-Bell](/witten-bell-smoothing/) gives the lower order the weight $T(h)/(c(h) + T(h))$, and [Kneser-Ney](/kneser-ney-smoothing/) uses continuation counts in the lower order. Training takes $\Theta(nN)$ hash operations and a query $\Theta(n)$. [Stupid backoff](/stupid-backoff/) uses the factor 0.4 and gives scores, not probabilities.
- **Pruning.** [Stolcke pruning](/entropy-based-ngram-pruning/) removes each n-gram whose removal changes the model by less than a threshold in relative entropy, at $\Theta(nE)$ for $E$ explicit n-grams.
- **Attention** is $\operatorname{softmax}(QK^\top/\sqrt{d_k})\,V$, at $\Theta(n^2 d)$ for $n$ tokens; without a position code it is blind to word order. [FlashAttention](/flashattention/) computes the same output with $\Theta(N)$ extra memory and $\Theta(N^2 d^2/M)$ transfers for a fast memory of $M$ numbers, optimal up to a constant. [Grouped-query attention](/grouped-query-attention/) shrinks the key-value cache by the factor $h/g$.
- The [selective scan](/selective-state-space-model/) composes the affine maps $h \mapsto \alpha_t h + \beta_t$, an associative operation, so it runs in linear work and $\Theta(\log L)$ depth, with no term in $L^2$.
- **Scaling laws are fits.** A [scaling law](/neural-scaling-law/) such as the Chinchilla fit has the form $L = E + A/N^\alpha + B/D^\beta$ with compute $C \approx 6ND$. They hold over the measured range only, and what large models can do is measured too.
- **Preferences.** The objective $\mathbb{E}_\pi[r] - \beta\, \mathrm{KL}(\pi \,\|\, \pi_{\text{ref}})$ has the optimum $\pi^* \propto \pi_{\text{ref}}\, e^{r/\beta}$. [DPO](/direct-preference-optimization/) reaches the same optimum, under the conditions of the entry, with a logistic loss on log-ratios. [LoRA](/low-rank-adaptation/) trains $r(d + k)$ numbers instead of $dk$.

## The main methods side by side

| Method | Kind | Cost | What is guaranteed |
|---|---|---|---|
| Laplace | add a constant | $\Theta(1)$ per query | a proper distribution |
| Good-Turing | counts of counts | $\Theta(T)$ after counting | unseen mass $N_1/N$; needs smoothed $N_r$ |
| Katz backoff | discount and back off | $\Theta(n)$ per query | a proper distribution |
| Interpolated Kneser-Ney | discount, continuation counts | $\Theta(nN)$ build, $\Theta(n)$ query | a proper distribution; quality measured |
| Stupid backoff | relative frequency, factor 0.4 | $\Theta(n)$ per query | none; scores are not normalized |
| Scaled dot-product attention | softmax over keys | $\Theta(n^2 d)$ | each output in the convex hull of the values |
| FlashAttention | tiled, online softmax | $\Theta(n^2 d)$, $\Theta(n^2 d^2/M)$ transfers | the exact attention output |
| Selective scan | linear recurrence | $\Theta(L)$ work, $\Theta(\log L)$ depth | the same states as the sequential loop |
| DPO | logistic loss on preference pairs | $\Theta(mnc)$ per batch | the RLHF optimum, under the entry's conditions |
| LoRA | low-rank update | $\Theta(dk + r(d+k))$ per token | no inference cost after merging |

: The main methods of the chapter. Here $n$ is the model order or the sequence length, $N$ the number of training tokens, $T$ the number of types, $d$ the vector size, $M$ the size of fast memory, $L$ the sequence length of the scan, $m$ the pairs in a batch and $c$ the cost per token of the network.

## Choosing a method

- For an n-gram model, use interpolated modified Kneser-Ney. Use Witten-Bell when the counts of counts are too sparse to set the discounts.
- For web-scale n-gram tables in translation, use stupid backoff; prune a Katz or Kneser-Ney model by relative entropy when it must fit in memory.
- For a neural model, use a decoder-only transformer trained by causal language modeling, with rotary positions or ALiBi, grouped-query attention for fast decoding and FlashAttention for long inputs. Use masked language modeling or replaced token detection for an encoder that only reads text.
- To adapt a model with little memory, use LoRA. To fit preferences, DPO needs no reward model or sampling; RLHF with PPO can use a reward model on new samples.
