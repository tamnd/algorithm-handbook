Words that occur in the same contexts tend to mean similar things: "coffee" and "tea" both follow "a cup of", and "doctor" and "nurse" both appear near "hospital". This is the distributional hypothesis, and it turns meaning into geometry. Count the contexts of each word, or train a model to predict them, and each word becomes a vector of a few hundred numbers; similar words get nearby vectors, and some relations show up as directions, as in the analogy king − man + woman ≈ queen. Sentences and paragraphs can be embedded the same way.

Embeddings are the input layer of nearly every modern system for language. Search engines compare query and document vectors, translation systems map the vectors of two languages onto each other, and classifiers start from pretrained vectors when labeled data is scarce. The same vectors also carry the biases of the text they were trained on, which can be measured and partly removed.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Counting contexts.** The distributional hypothesis, the word-context matrix, pointwise mutual information and its positive form, and Brown clustering.
2. **Predicting contexts.** Word embeddings from skip-gram and continuous bag of words, negative sampling and the hierarchical softmax, skip-gram with negative sampling as an implicit matrix factorization, GloVe, and skip-gram with subword information.
3. **Using and aligning vectors.** Word analogies, retrofitting to a lexicon, cross-lingual mappings and the CSLS criterion for nearest neighbours.
4. **Context and sentences.** Contextual embeddings and ELMo, sentence embeddings, paragraph vectors, smooth inverse frequency weighting, Sentence-BERT, SimCSE and the word mover's distance.
5. **Bias.** The word embedding association test and hard debiasing.
6. **Word senses and relations.** Word sense disambiguation, the Lesk and Yarowsky algorithms, Resnik similarity and Hearst patterns.

## What to read meanwhile

Counting methods are low-rank approximations of a matrix. Read [latent semantic analysis](/latent-semantic-analysis/) and [embedding](/embedding/) in Volume 25, the [singular value decomposition](/singular-value-decomposition/) in Volume 12, and [tf-idf](/tf-idf/) in Volume 35 for the weighting of counts. The prediction methods are trained by [stochastic gradient descent](/stochastic-gradient-descent/) (Volume 15) and [backpropagation](/backpropagation/), with a [softmax regression](/softmax-regression/) output, both in Volume 25.

To compare and search vectors, read [cosine similarity](/cosine-similarity/) and [locality-sensitive hashing](/locality-sensitive-hashing/) in Volume 5. Sentence vectors used for search are covered by [dual-encoder retrieval](/dual-encoder-retrieval/) and [dense passage retrieval](/dense-passage-retrieval/) in Volume 35, and [latent Dirichlet allocation](/latent-dirichlet-allocation/) in Volume 25 gives a probabilistic view of word co-occurrence by topics.
