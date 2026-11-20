1. ◦ The sentence "Bank of America Merrill Lynch hired John Smith" has the spans "Bank of America" (ORG), "Merrill Lynch" (ORG) and "John Smith" (PER). Write its tags in IOB2, in IOB1 and in BIOES, as defined in [BIO encoding](/bio-encoding/).

2. ◦ The gold tags of "Alice met Bob in New York" are B-PER O B-PER O B-LOC I-LOC, and a tagger outputs B-PER O I-PER O B-LOC B-LOC. Read the predicted spans with the CoNLL rule and compute the precision, recall and [span F1](/span-f1-score/). What are the scores for a stricter reader that drops every span that starts with an I tag?

3. ◦ With two entity types, how many tags does IOB2 use? Count the valid IOB2 sequences of length $n = 0, 1, 2, 3, 4$, and the number of invalid tag strings of length 4.

4. ◦ Map the Penn Treebank tags of "The/DT dogs/NNS have/VBP eaten/VBN in/IN Paris/NNP ./." to the twelve tags of Petrov, Das and McDonald and to the 17 tags of Universal Dependencies (see [universal POS tagset](/universal-pos-tagset/)). Which two words get different tags in the two sets, apart from the period?

5. ◦ An [HMM tagger](/hmm-part-of-speech-tagger/) has the tags N and V, with start probabilities N 0.7 and V 0.3 and transitions $N \to N$ 0.3, $N \to V$ 0.7, $V \to N$ 0.6, $V \to V$ 0.4. The emissions are: they, N 0.2 and V 0; can, N 0.1 and V 0.2; fish, N 0.3 and V 0.2. Find the best tag sequence of "they can fish" and its joint probability, and the probability of the words.

6. ◦ The gold entities are {1, 2, 3} and {4, 5}, and a system outputs {1, 2} and {3, 4, 5}. Compute the [B-cubed](/b-cubed-metric/) precision and recall, and the MUC recall and precision.

7. ◦ A document has five mentions. How many partitions into entities are there, how many antecedent forests (each mention picks one earlier mention or none), and how many pairs does a [mention-pair model](/mention-pair-model/) classify if it scores all of them?

8. ◦ A [Brill tagger](/brill-tagger/) corpus has the current tags and gold tags "to/TO race/NN(VB) the/DT", "to/TO dinner/NN(NN) ./.", "to/TO run/NN(VB) a/DT" and "to/TO school/NN(NN) ./.", with the gold tag in parentheses. Compute the good and bad counts and the score of the rule "change NN to VB when the previous tag is TO", and of the rule "change NN to VB when the previous tag is TO and the next tag is DT".

9. • A model has paths from a start state through either A, A2, A3 or one of B, B2, B3, or B, B2, D, or B, C, E. States A, A2 and C have one successor each. For an input, the factors are 0.6 for A and 0.4 for B at the first step; 0.05 for $A \to A2$, 0.9 for $B \to B2$ and 0.1 for $B \to C$ at the second; and 1 for $A2 \to A3$, 0.9 for $B2 \to B3$, 0.1 for $B2 \to D$ and 1 for $C \to E$ at the third. A [maximum entropy Markov model](/maximum-entropy-markov-model/) normalizes the factors leaving each state; a CRF multiplies them along each path and divides by their sum. Find the best path and its probability under each. Explain the result by the [label bias problem](/label-bias-problem/).

10. • A [structured perceptron](/structured-perceptron/) tagger uses emission features (word, tag) and transition features (previous tag, tag), with a start tag. On "the dog barks" with gold D N V it predicts D V V. Which feature weights change in the update, and by how much? If the data are separable with margin $\delta = 0.5$ and every feature difference has norm at most $R = 3$, how many mistakes can training make at most?

11. • A trigram HMM tagger uses the 45 tags of the Penn Treebank. How many steps does Viterbi take for a 20-word sentence, counting one step per pair of a state and a predecessor? How many if a tag dictionary allows at most 3 tags for every word?

12. • A [semi-Markov CRF](/semi-markov-crf/) labels "John Smith said" with segments of PER of length at most 2 and segments of O of length 1. The segment scores are: John PER 2, John Smith PER 5, Smith PER 2, Smith said PER $-2$, said PER $-1$, and 1 for each one-token O segment; there are no transition scores. List the labeled segmentations, find the best, and say what a linear-chain model would need to express the score of "John Smith" as a unit.

13. • A mention-pair classifier gives the probabilities $p(1, 2) = 0.7$, $p(1, 3) = 0.2$, $p(2, 3) = 0.4$, $p(1, 4) = 0.8$, $p(2, 4) = 0.3$ and $p(3, 4) = 0.6$, and links above 0.5. Find the entities with closest-first linking and with best-first linking.

14. • The gold entities are {a, b, c, d, e} and {f, g}. Compute MUC and B-cubed precision, recall and F1 for three outputs: everything in one entity; {a, b, c, d, e}, {f}, {g}; and {a, b}, {c, d, e}, {f, g}. Which score cannot tell the last two apart?

15. • In [entity linking](/entity-linking/), the text "Jordan scored 40 as the Bulls won" has the candidates Michael Jordan (local score 0.4) and Jordan the country (0.6) for "Jordan", and Chicago Bulls (0.5) and the animal (0.55) for "Bulls". The coherence of Michael Jordan with Chicago Bulls is $\psi$, and every other pair has coherence 0. Find the local choice and the global choice for $\psi = 0.8$, and the value of $\psi$ above which the global choice changes.

16. • Apply [centering theory](/centering-theory/), with subject above object above other, to: U1 "John went to the store." U2 "He saw Bob there." U3 "Bob greeted him." U4 "Bob was in a hurry." Give the Cf list, Cb and Cp of each utterance and the transition into U2, U3 and U4.

17. • In [DIPRE](/dipre/), one group of three occurrences on different sites shares the url prefix `http://www.` (11 characters), the prefix `<i>` (3), the middle `</i> by ` (8) and the suffix `, ` (2). A group of two occurrences from one directory shares the url prefix `http://www.sf.org/books/` (24), the prefix `<li>` (4), the middle ` - ` (3) and the suffix `</li>` (5). Which patterns are accepted with $t = 2000$, and with $t = 1000$?

18. • In the [span-ranking model](/span-ranking-coreference/), a span has the antecedent scores 0 for the dummy, 1.0 for $j_1$, 2.0 for $j_2$ and $-0.5$ for $j_3$. The gold antecedents are $j_1$ and $j_3$. Compute the antecedent distribution, the loss, and the antecedent chosen by the decoder.

19. ★ A tag chain over A and B, with no information in the words, has start probabilities A 0.8 and B 0.2 and transitions $A \to A$ 0.5, $A \to B$ 0.5, $B \to A$ 0.9, $B \to B$ 0.1. For three positions, find the Viterbi sequence and the sequence of most probable tags at each position, with the probability of each sequence and the expected number of correct tags.

20. ★ Four mentions have pair scores $s(1, 2) = 2$, $s(1, 3) = 1$, $s(2, 3) = 1$, $s(1, 4) = -3$, $s(2, 4) = 1$ and $s(3, 4) = -2$. A partition scores the sum of $s$ over the pairs inside its entities. Find the best partition by checking all of them, and the partition that closest-first linking (link to the nearest earlier mention with a positive score) gives after the transitive closure, with its score. Relate this to [correlation clustering](/correlation-clustering/).

21. ★ In the collapsed sampler of [Bayesian HMM tagging](/bayesian-hmm-tagging/) with $k = 2$, $\alpha = 1/2$, $\beta = 1/10$ and four word types, the current tagging is "the/1 dog/2 barks/1" and "the/1 cat/2", with tag 0 for the sentence boundary. Compute the conditional probability that "dog" gets tag 1. What does the sampler give without the correction for $a = t$?

22. ★ A token classifier gives "John Smith said" the probabilities O 0.5, B-PER 0.4, I-PER 0.1 for John; O 0.3, B-PER 0.1, I-PER 0.6 for Smith; and O 0.9, B-PER 0.05, I-PER 0.05 for said. The gold span is "John Smith" (PER). Give the tags of the independent argmax and of the best sequence in which I-PER follows only B-PER or I-PER, and the span F1 of each under the CoNLL reading rule.
