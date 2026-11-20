Many tasks in language processing give a label to each word. A part-of-speech tagger marks "book" as a noun in "read the book" and as a verb in "book a flight". A named entity recognizer marks "Paris Hilton" as a person and "Paris" in "flights to Paris" as a place. Information extraction goes on from the labels to facts: who works for which company, which drug treats which disease. These labels feed search engines, question answering, and the building of databases from text.

The labels of neighbouring words depend on each other, so the methods model whole sequences. Hidden Markov models and conditional random fields score a sequence of labels, and the Viterbi algorithm finds the best one by dynamic programming. Spans are encoded as tags with the BIO scheme, and span measures decide when a predicted span counts as right. Coreference resolution links the mentions that refer to the same entity, and sentiment analysis labels the opinion a text expresses.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Part-of-speech tagging.** The task, the universal tagset, the HMM tagger and its Bayesian form, and the Brill tagger.
2. **Sequence labeling models.** Sequence labeling, maximum entropy Markov models and the label bias problem, the structured perceptron, the BiLSTM-CRF and the semi-Markov CRF.
3. **Spans and entities.** BIO encoding, chunking, named entity recognition, span F1 and entity linking.
4. **Relations and opinions.** Relation extraction, distant supervision, the DIPRE bootstrapping method and sentiment analysis.
5. **Coreference.** Mention-pair and span-ranking models, the Hobbs algorithm, centering theory and the B-cubed measure.

## What to read meanwhile

The models of this chapter are in Volume 25: the [hidden Markov model](/hidden-markov-model/), the [Viterbi algorithm](/viterbi-algorithm/), the [forward-backward algorithm](/forward-backward-algorithm/), the [Baum-Welch algorithm](/baum-welch-algorithm/), the [conditional random field](/conditional-random-field/), [structured prediction](/structured-prediction/), the [perceptron](/perceptron/) and [logistic regression](/logistic-regression/). The [hidden semi-Markov model](/hidden-semi-markov-model/) is the generative cousin of the semi-Markov CRF. For evaluation, read [precision and recall](/precision-and-recall/) and the [confusion matrix](/confusion-matrix/) there too.

A [naive Bayes classifier](/naive-bayes-classifier/) (Volume 25) is the classical first method for sentiment analysis. Taggers need tokens and sentences first: Chapter 41.1 has [tokenization](/text-tokenization/), [sentence boundary detection](/sentence-boundary-detection/), [truecasing](/truecasing/), which improves entity recognition on text without case, and [lemmatization](/lemmatization/).
