## What to remember

- **Term weights have three parts.** A term counts more if it is frequent in the document, rare in the collection, and in a short document. [tf-idf](/tf-idf/), the cosine of the [vector space model](/vector-space-model/), [pivoted length normalization](/pivoted-length-normalization/) and [BM25](/bm25/) differ in how they combine the three. BM25's length factor $1 - b + b\,|d|/\mathrm{avgdl}$ is the pivoted normalizer with pivot avgdl and slope $b$.
- **The probability ranking principle is a theorem with hypotheses.** Sorting by the probability of relevance maximizes expected utility when relevance is judged per document, the probabilities are correct, and the utility adds a decreasing weight per relevant document. With duplicates in the collection, another order can do better.
- **BM25 is a tuned approximation.** It comes from the [binary independence model](/binary-independence-model/) and the [two-Poisson model](/two-poisson-model/), but its form and its parameters $k_1$ and $b$ are justified by measurement, not derivation.
- **Language models need smoothing.** The [query likelihood model](/query-likelihood-model/) gives probability 0 to a document that misses one query term. [Jelinek-Mercer](/jelinek-mercer-smoothing/) and [Dirichlet](/dirichlet-prior-smoothing/) smoothing mix in the collection model, which acts like an idf weight and a length correction.
- **Feedback changes the query, not the scoring function.** [Rocchio](/rocchio-algorithm/) moves the query toward judged relevant documents; [pseudo-relevance feedback](/pseudo-relevance-feedback/) and [RM3](/relevance-model-rm3/) take the top documents as relevant, and the query can drift.
- **Fusion rules are cheap and mostly heuristic.** [Borda](/borda-count/), [CombMNZ](/combmnz/) and [reciprocal rank fusion](/reciprocal-rank-fusion/) are near-linear. The [Kemeny](/kemeny-rank-aggregation/) consensus is the principled target, and it is NP-hard already for four lists. Footrule aggregation is within a factor 2 of it; reciprocal rank fusion has no guarantee.
- **Learning to rank optimizes a surrogate.** The [Ranking SVM](/ranking-svm/), [RankBoost](/rankboost/) and [RankNet](/ranknet/) bound the number of misordered pairs. [LambdaRank](/lambdarank/) and [LambdaMART](/lambdamart/) weight the pairs by the change of nDCG, which works well in measurements but is not the gradient of nDCG.
- **Neural retrieval trades cost for interaction.** A [dual encoder](/dual-encoder-retrieval/) precomputes the document vectors and needs one encoder call per query; a [cross-encoder](/cross-encoder-reranking/) needs one call per candidate and only reranks. Their effectiveness is measured, never guaranteed.

## The main models side by side

| Model | Score from | Parameters | Needs training data | Query cost |
|---|---|---|---|---|
| [Boolean model](/boolean-retrieval-model/) | set operations | none | no | merge of posting lists |
| Vector space with tf-idf | cosine of weighted vectors | weighting scheme | no | one pass over the postings |
| BM25 | saturated tf times idf | $k_1$, $b$ | no, tuned on judgments | one pass over the postings |
| [Divergence from randomness](/divergence-from-randomness/) | information content of tf | normalization $c$ | no, tuned on judgments | one pass over the postings |
| Query likelihood, Dirichlet | smoothed log probability | $\mu$ | no, tuned on judgments | one pass over the postings |
| LambdaMART | boosted trees on features | trees, depth, rate | graded labels | features and trees per candidate |
| Dual encoder ([DPR](/dense-passage-retrieval/)) | inner product of learned vectors | encoder weights | question-passage pairs | one encoding and a vector search |
| [SPLADE](/splade/) | inner product of learned sparse vectors | encoder weights, sparsity penalty | query-passage pairs | one encoding and an inverted index pass |
| [ColBERT](/colbert/) | sum of maximum token similarities | encoder weights | query-passage pairs | token search and exact rerank |
| Cross-encoder | joint transformer reading | encoder weights | query-passage pairs | one transformer pass per candidate |

: Ranking models by what their score is built from and what they cost. "Tuned on judgments" means the parameters are set by measurement on judged queries. The effectiveness of every row is measured, not proved.

## Choosing a method

- For a first ranking with no training data, use BM25 with $k_1$ near 1.2 and $b = 0.75$, or query likelihood with Dirichlet smoothing, and tune on judged queries if you have them.
- For documents with a title and a body, use [BM25F](/bm25f/), not a sum of per-field BM25 scores.
- For short queries that miss related words, add pseudo-relevance feedback or RM3, and check that it helps.
- To merge runs from systems whose scores are not comparable, use reciprocal rank fusion or Borda. Use CombSUM or CombMNZ only after normalizing the scores. For a few items, solve Kemeny exactly or improve a cheap answer by local Kemenization.
- With hand-made features and graded labels, use LambdaMART. With click logs, correct the position bias with [unbiased learning to rank](/unbiased-learning-to-rank/) before training.
- With raw text and training pairs, retrieve with a dual encoder or SPLADE, rerank the top few hundred with a cross-encoder. Reranking cannot recover what the first stage missed.
