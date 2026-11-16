Take eight short documents and the query "sorted array search". Document 1 is "binary search finds a key in a sorted array", document 2 is "merge sort merges two sorted runs into one sorted array", and document 8 is "the sorted array of ids is compressed with gap encoding". A Boolean AND of the three terms returns document 1 alone, because only it holds all three. A user who wanted to read about sorted arrays would also like documents 2 and 8, and a Boolean OR returns five documents in no useful order. A ranking model gives each document a score and sorts by it. [BM25](/bm25/) with its usual parameters gives document 1 the score 3.03, document 2 1.89, document 8 1.63, document 7 ("search engines rank documents ...") 1.27 and document 4 0.69. The order now says something: all three query terms beat two, and the rare term "search" counts for more than the common term "sorted".

Every model in this chapter answers the same question, how to score a document for a query, and they answer it from different starting points. Some start from geometry, with documents as vectors and the angle as the score. Some start from probability, either the probability that the document is relevant or the probability that a model of the document generates the query. Some learn the score from judged examples or from clicks, and some learn the vectors themselves with neural encoders. Two facts hold across all of them. First, the formulas have parameters, and their values and the gains of one model over another are measured on test collections, not proved. Second, the few theorems, such as the [probability ranking principle](/probability-ranking-principle/), hold only under their stated assumptions, and the entries say which ones.

## What the chapter covers

1. **Boolean and vector space retrieval.** The [Boolean model](/boolean-retrieval-model/), [tf-idf](/tf-idf/) weights, the [vector space model](/vector-space-model/) with the cosine, and [pivoted length normalization](/pivoted-length-normalization/).
2. **Relevance feedback.** [Relevance feedback](/relevance-feedback/) from judged documents, the [Rocchio algorithm](/rocchio-algorithm/), and [pseudo-relevance feedback](/pseudo-relevance-feedback/) from the top of a first ranking.
3. **Probabilistic relevance models.** The probability ranking principle, the [binary independence model](/binary-independence-model/), the [two-Poisson model](/two-poisson-model/), BM25, [BM25F](/bm25f/) for documents with fields, and [divergence from randomness](/divergence-from-randomness/).
4. **Language models for retrieval.** The [query likelihood model](/query-likelihood-model/), [Jelinek-Mercer smoothing](/jelinek-mercer-smoothing/), [Dirichlet prior smoothing](/dirichlet-prior-smoothing/), and the [relevance model RM3](/relevance-model-rm3/).
5. **Rank fusion.** The [rank aggregation](/rank-aggregation/) problem, the [Borda count](/borda-count/), [CombSUM and CombMNZ](/combmnz/), [reciprocal rank fusion](/reciprocal-rank-fusion/), [Markov chain aggregation](/markov-chain-rank-aggregation/) and [Kemeny aggregation](/kemeny-rank-aggregation/).
6. **Learning to rank.** The [Ranking SVM](/ranking-svm/), [RankBoost](/rankboost/), [RankNet](/ranknet/), [LambdaRank](/lambdarank/), [LambdaMART](/lambdamart/), [ListNet](/listnet/), and [unbiased learning to rank](/unbiased-learning-to-rank/) from click logs.
7. **Neural retrieval.** The [dual encoder](/dual-encoder-retrieval/), [dense passage retrieval](/dense-passage-retrieval/), [SPLADE](/splade/), [ColBERT](/colbert/), [cross-encoder reranking](/cross-encoder-reranking/) and [retrieval-augmented generation](/retrieval-augmented-generation/).

## A first reading

Read these first, in this order:

1. [tf-idf](/tf-idf/)
2. [Vector space model](/vector-space-model/)
3. [Rocchio algorithm](/rocchio-algorithm/)
4. [Probability ranking principle](/probability-ranking-principle/)
5. [Binary independence model](/binary-independence-model/)
6. [BM25](/bm25/)
7. [Query likelihood model](/query-likelihood-model/)
8. [Dirichlet prior smoothing](/dirichlet-prior-smoothing/)
9. [Rank aggregation](/rank-aggregation/)
10. [Reciprocal rank fusion](/reciprocal-rank-fusion/)
11. [RankNet](/ranknet/)
12. [LambdaMART](/lambdamart/)
13. [Dual encoder retrieval](/dual-encoder-retrieval/)
14. [Cross-encoder reranking](/cross-encoder-reranking/)

That path covers one model of each kind and the main line from term weights through BM25 to learned and neural scores. Skip at first the two-Poisson model and divergence from randomness, which explain where BM25-like weights come from but are not needed to use them, and the Markov chain and Kemeny entries, which matter when the fused lists disagree strongly. Read the proofs in the probability ranking principle and Kemeny entries closely: they show exactly where the guarantees stop.

## Before you start

The scores are computed over the [inverted index](/inverted-index/) of Volume 20 and the [posting lists](/posting-list/) of Chapter 35.1, and the fast top-$k$ methods there, such as [WAND](/wand/) and [MaxScore](/maxscore/), need the per-term score bounds that BM25 provides. The vector models use the [cosine similarity](/cosine-similarity/) and [maximum inner product search](/maximum-inner-product-search/) of Volume 5. The probabilistic models use the [Poisson distribution](/poisson-distribution/) of Volume 1 and [maximum likelihood estimation](/maximum-likelihood-estimation/) of Volume 25. Rank fusion measures disagreement with the [Kendall tau distance](/kendall-tau-distance/) and the [Spearman footrule](/spearman-footrule/) of Volume 6, Kemeny aggregation is a [feedback arc set](/feedback-arc-set-problem/) problem of Volume 7, and the Markov chain method needs [stationary distributions](/stationary-distribution/) from Volume 17. The learning-to-rank entries specialize [learning to rank](/learning-to-rank/), the [support vector machine](/support-vector-machine/), [AdaBoost](/adaboost/), [gradient boosting](/gradient-boosting/) and the [cross-entropy loss](/cross-entropy-loss/) of Volume 25. Every model here is judged by the metrics of Chapter 35.3, above all [nDCG](/normalized-discounted-cumulative-gain/). You should be comfortable with logarithms, conditional probability, sums over sets, and gradients of simple functions.
