## What to remember

- **Counts first.** The [word-context matrix](/word-context-matrix/) counts each word with the words near it. Weighting by $\mathrm{PMI}(w, c) = \log \frac{P(w, c)}{P(w) P(c)}$ and clipping at 0 gives [PPMI](/positive-pointwise-mutual-information/). Context counts raised to the power $0.75$ lower the PMI of rare contexts.
- **Prediction is cheap only with a trick.** A full softmax costs $\Theta(dV)$ per training pair. [Hierarchical softmax](/hierarchical-softmax/) on a Huffman tree costs $O(d(H + 1))$ on average, with $H$ the entropy of the words in bits, and [negative sampling](/negative-sampling/) $O(k(d + \log V))$ with $k$ noise words from the unigram distribution to the power $3/4$.
- **What negative sampling fits.** If every dot product $\vec w \cdot \vec c$ is a free parameter, the expected skip-gram objective with $k$ negatives is maximized at $\vec w \cdot \vec c = \mathrm{PMI}(w, c) - \log k$ ([the theorem](/sgns-implicit-factorization-theorem/)). Trained vectors of small dimension only approximate it.
- **Aligning two spaces has a closed form.** The orthogonal $W$ that minimizes $\sum_i \|W \vec x_i - \vec y_i\|^2$ is $W = UV^\top$ from the SVD $U \Sigma V^\top$ of $M = \sum_i \vec y_i \vec x_i^\top$. [CSLS](/cross-domain-similarity-local-scaling/) scores a pair by $2\cos(W\vec x, \vec y) - r_T(W\vec x) - r_S(\vec y)$, which lowers the score of hub targets.
- **Transport between documents.** The [word mover's distance](/word-movers-distance/) is the optimum of a transportation problem and a metric. The centroid distance and the relaxed distance are lower bounds, in $O(dp)$ and $O(dp^2)$ time; neither is always the tighter one.
- **Scores are measurements.** Analogy accuracy, similarity correlations and the [association test](/word-embedding-association-test/) measure vectors on chosen word lists. The test has an exact p-value over $\binom{2n}{n}$ splits and an effect size with $|d| \le 2$. [Hard debiasing](/hard-debiasing/) makes the projection of neutral words on the bias direction exactly 0; it lowers the bias that such tests measure, not bias in every sense.
- **Senses.** [Lesk](/lesk-algorithm/) counts gloss overlaps, [Yarowsky](/yarowsky-algorithm/) grows a decision list from seeds, and [Resnik similarity](/resnik-similarity/) is the information content $-\log P(c)$ of the most informative common subsumer, so $0 \le \mathrm{sim}(a, b) \le \min(\mathrm{IC}(a), \mathrm{IC}(b))$.
- **Sentence vectors.** [SIF](/smooth-inverse-frequency-embedding/) averages word vectors with the weight $a/(a + p(w))$ and removes the first principal component. [Sentence-BERT](/sentence-bert/) and [SimCSE](/simcse/) train encoders; their gains are measured.

## The main methods side by side

| Method | Kind | Cost | What is guaranteed |
|---|---|---|---|
| [PPMI](/positive-pointwise-mutual-information/) | counts and weighting | one pass over the text | the exact weighted matrix |
| [Brown clustering](/brown-clustering/) | greedy merges | $O(N + V^4)$ | each merge keeps the most mutual information; not the best partition |
| [Skip-gram with negative sampling](/negative-sampling/) | SGD on a logistic loss | $O(k(d + \log V))$ per pair | the shifted-PMI optimum when dot products are free |
| [Hierarchical softmax](/hierarchical-softmax/) | tree of binary decisions | $O(d(H + 1))$ per pair on average | a normalized distribution over words |
| [GloVe](/glove/) | weighted least squares | $O(NK + TMd)$ | none beyond a local fit; quality is measured |
| [Orthogonal mapping](/cross-lingual-embedding-mapping/) | SVD | $O(nd^2 + d^3)$ | the exact optimum over orthogonal $W$ |
| [Retrofitting](/retrofitting-word-vectors/) | Jacobi sweeps | $O(T(V + E)d)$ | convergence; the minimizer of $\Psi$ for symmetric weights |
| [Word mover's distance](/word-movers-distance/) | transportation problem | $O(p^3 \log p)$ quoted | the exact distance, a metric |
| [SimCSE](/simcse/) | contrastive training | $O(n^2 d)$ per batch | none; quality is measured |

: The main methods of the chapter. Here $d$ is the dimension, $V$ the vocabulary size, $N$ the number of tokens, $K$ the window radius, $M$ the number of nonzero counts, $T$ the number of epochs or sweeps, $E$ the number of lexicon links, $p$ the number of distinct words in two documents, and $n$ the number of dictionary pairs or sentences.

## Choosing a method

- On a large corpus, train skip-gram with negative sampling or GloVe. On a small one, PPMI with a truncated SVD is a fair baseline.
- With many rare words or a rich morphology, use the [subword skip-gram](/subword-information-embeddings/), which gives a vector to any string.
- With a lexicon such as WordNet, retrofit trained vectors to it.
- To map two languages, fit an orthogonal map on a seed dictionary and retrieve with CSLS rather than plain nearest neighbours.
- For a sense from a fixed inventory with no training data, start with Lesk; with a few seeds and much raw text, use Yarowsky.
- For sentence vectors with no training, use SIF. With an encoder to fine-tune, use Sentence-BERT or SimCSE. Use the word mover's distance only to rerank a short list.
- Report the test sets with any analogy, similarity or bias score, since the numbers depend on them.
