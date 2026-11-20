1. The first line gives 13 tokens: We, 'll, pay, `$`, 5, (, cash, ), --, wo, n't, you, ?. The second gives 8: I, met, Dr., Smith, at, 5, p.m, and a final period. Only the last period of a line is split off, so "Dr." stays whole, while "p.m." loses its period to the sentence end: the rules cannot see that the period does both jobs.

3. Boxes gives boxe and box; wolves gives wolve and wolf; studies, as a verb, gives studie (by s and by es to e), study and studi.

4. Forward: theme, nu. Backward: menu, then the, so the, menu. Both have two words, no unknown characters and no one-character words, so the rule reaches its last step and keeps the backward result, the menu.

5. Twelve bytes: c, a, f and the space take one byte each, é takes two (C3 A9), and each of the two Chinese characters takes three. Byte-level BPE starts from these 12 byte tokens. $50{,}257 = 256 + 50{,}000 + 1$: the bytes, the merges, and one end-of-text token.

7. Seven segmentations: b u g s 0.0001, b u gs 0.001, b ug s 0.002, b ugs 0.005, bu g s 0.0005, bu gs 0.005 and bug s 0.015. Viterbi returns bug s; $P(\text{bugs}) = 0.0286$, and the posterior of bug s is $0.015/0.0286 = 75/143 \approx 0.524$.

8. $\operatorname{oop}(P, Q) = 1 + 4 + 2 + 6 = 13$, and $\operatorname{oop}(Q, P) = 2 + 1 + 6 + 6 + 6 + 4 = 25$. The distance is not symmetric when the profiles have different lengths.

11. Three segmentations: nowhere man with probability $9/3600 = 0.0025$, no where man with $630/216000 \approx 0.00292$ and now here man with $0.002$. The dynamic program returns no where man; forward maximum matching takes the longest word, nowhere, and returns nowhere man.

14. The forward values are 1, 0.1, 0.06, 0.176 and 0.0286. The expected uses are $75/143 \approx 0.524$ for bug and $8/13 \approx 0.615$ for s, and the expected number of pieces is $609/286 \approx 2.129$. The M step gives s the probability $176/609 \approx 0.289$.

18. BPE merges t a, the most frequent pair (5). With $N = 24$, the gains are 0.8066 for t ##a, 3.7500 for t ##e and 4.6308 for k ##a, so WordPiece merges k ##a, which has count 4: every k is followed by ##a.

20. Take $V$ = {a, b, ab, $b^m$} and the word $a b^m$: greedy takes ab and then $m - 1$ single b's, while a, $b^m$ is two tokens. For the bound, greedy uses at most $n$ tokens and any tokenization uses at least $n/L$.

21. BPE merges c c (count 9) and then b cc (count 5), leaving 36, 27 and then 22 tokens. The merges c b and then c cb leave 20, the least over all pairs of merges. The pieces bccb and cccb leave 12. As in the entry's example, greedy BPE is not optimal, and the best direct vocabulary beats the best sequence of merges.

22. Run the two transducers in step on the same pair of symbols at a time; the product automaton accepts the intersection, and same length is what lets each step read one symbol on each tape. For the second part take $\{(a^n, b^n c^k)\}$ and $\{(a^n, b^k c^n)\}$, both regular; their intersection is $\{(a^n, b^n c^n)\}$, whose range is not regular, while the range of a regular relation is regular.

23. Write $\log P(x) = \log \sum_s P(s)$ and multiply and divide by the old posterior $q(s)$. Jensen gives a lower bound that equals $\log P(x)$ at the old parameters, and the M step maximizes it: with the constraint that the probabilities sum to 1, the maximizer is the expected count of each piece divided by the expected total.

24. Each non-overlapping replacement removes one token, and the merge makes exactly that many replacements. For the second part, take aaa three times and bc four times: a a has 6 overlapping occurrences but saves only 3 tokens, while b c saves 4. For the third, the word abcd five times leaves 15 tokens after the best merge and 5 with the one piece abcd.
