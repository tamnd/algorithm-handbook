1. IOB2 starts every span with B: B-ORG I-ORG I-ORG B-ORG I-ORG O B-PER I-PER. IOB1 uses B only where a span directly follows another span of the same type: I-ORG I-ORG I-ORG B-ORG I-ORG O I-PER I-PER. BIOES marks the last token of a span with E (and a single-token span with S): B-ORG I-ORG E-ORG B-ORG E-ORG O B-PER E-PER.

2. Under the CoNLL rule an I tag after O opens a span, so the predicted spans are Alice, Bob, New and York. Two of them match the gold, so $P = 2/4$, $R = 2/3$ and $F_1 = 4/7$. The strict reader drops Bob: $P = 1/3$, $R = 1/3$, $F_1 = 1/3$.

3. There are $2L + 1 = 5$ tags. Let $a_n$ count valid sequences; the counts are 1, 3, 11, 41 and 153 (an I-X tag may follow only B-X or I-X). Of the $5^4 = 625$ strings, 472 are invalid.

5. Viterbi gives N V N with probability $0.7 \cdot 0.2 \cdot 0.7 \cdot 0.2 \cdot 0.6 \cdot 0.3 = 441/125000 = 0.003528$; the next best is N V V with 0.001568. The forward algorithm gives $P(\text{they can fish}) = 3031/500000 = 0.006062$. "They" must be N, since its emission under V is 0.

9. Key idea: in the MEMM each state passes on all its probability mass, whatever the input says about its successors. A and A2 have one successor each, so the A path keeps 0.6 even though $A \to A2$ scores only 0.05. The MEMM picks A A2 A3 with 0.6, against 0.324 for B B2 B3. In the CRF the path products are 0.03, 0.324, 0.036 and 0.04, with sum 0.43, so B B2 B3 wins with $162/215 \approx 0.754$ and the A path has $3/43 \approx 0.070$.

10. The update adds the gold features and subtracts the predicted ones: $+1$ for (dog, N), (D, N) and (N, V), and $-1$ for (dog, V), (D, V) and (V, V). The emissions of "the" and "barks" and the start transition cancel. Novikoff's bound gives at most $R^2/\delta^2 = 9/0.25 = 36$ mistakes.

13. Closest first: mention 2 links to 1 (0.7); mention 3 has no score above 0.5 and starts an entity; mention 4 links to its nearest candidate above 0.5, which is 3. The entities are {1, 2} and {3, 4}. Best first links 4 to 1 (0.8), giving {1, 2, 4} and {3}.

14. Key idea: MUC counts links, so splitting off one mention and splitting a group in two each cost one link. Merging all: MUC $P = 5/6$, $R = 1$, $F_1 = 10/11$; B-cubed $P = 29/49$, $R = 1$, $F_1 = 29/39$. Splitting f from g: MUC $P = 1$, $R = 4/5$, $F_1 = 8/9$; B-cubed $R = 6/7$, $F_1 = 12/13$. Splitting ab from cde: MUC the same as before, 8/9; B-cubed $R = 23/35$, $F_1 = 23/29$. MUC cannot tell the two splits apart, and it ranks the merge above both.

17. Specificity is the product of the four lengths. Group A: $11 \cdot 3 \cdot 8 \cdot 2 = 528$, times $n = 3$ gives 1584. Group B: $24 \cdot 4 \cdot 3 \cdot 5 = 1440$, times $n = 2$ gives 2880. With $t = 2000$ only B is accepted; with $t = 1000$ both are. The general pattern with many sites loses to the narrow one from a single directory.

19. Key idea: maximizing the probability of the whole sequence and maximizing the expected number of correct tags are different objectives. The sequence A B A (probability 0.36) beats every other sequence, so it is the Viterbi output. The marginals of A are 0.8, 0.58 and 0.668, so posterior decoding outputs A A A, which has probability only 0.2. The expected number of correct tags is $0.8 + 0.58 + 0.668 = 2.048$ for A A A and $0.8 + 0.42 + 0.668 = 1.888$ for A B A.

20. Key idea: the transitive closure adds pairs that no link decision looked at. There are 15 partitions of four mentions; the best is {1, 2, 3}, {4} with score $2 + 1 + 1 = 4$, and the next best scores 2. Closest-first linking makes the links $2 \to 1$, $3 \to 2$ and $4 \to 2$, which put all four in one entity, with score $2 + 1 + 1 - 3 + 1 - 2 = 0$. Correlation clustering optimizes the partition score directly and is NP-hard in general.

21. Key idea: when "dog" gets tag $t$ it adds one transition $a \to t$ and one $t \to b$; if $a = t$, the first one is already in the counts when the second is scored. Here $a = b = 1$. After removing "dog", $n_{1,\text{dog}} = 0$, $n_1 = 3$ emissions, $n_{1,1} = 0$, $n_{1,2} = 1$, $n_{1,0} = 1$, so $n_1 = 2$ transitions out of tag 1. For $t = 1$: $\frac{0.1}{3.4} \cdot \frac{0.5}{3.5} \cdot \frac{1.5}{4.5} = 1/714$. For $t = 2$: $\frac{0.1}{1.4} \cdot \frac{1.5}{3.5} \cdot \frac{0.5}{2.5} = 3/490$. Normalizing gives $P(t = 1) = 35/188 \approx 0.186$, which equals the ratio of the exact marginal likelihoods. Without the correction the last factor for $t = 1$ is $0.5/3.5$, and $P(t = 1)$ drops to $5/56 \approx 0.089$.

22. The argmax tags are O I-PER O. The CoNLL rule reads the lone I-PER as the span "Smith", which is wrong: $F_1 = 0$. The best valid sequence is B-PER I-PER O, with score $0.4 \cdot 0.6 \cdot 0.9 = 0.216$, against $0.5 \cdot 0.3 \cdot 0.9 = 0.135$ for O O O. It finds "John Smith" and gets $F_1 = 1$.
