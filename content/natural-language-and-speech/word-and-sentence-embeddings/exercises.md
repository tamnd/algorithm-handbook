1. ◦ A [word-context matrix](/word-context-matrix/) has the rows cat, dog and car and the contexts pet, drive and fur, with the counts cat (4, 0, 2), dog (3, 1, 2) and car (0, 6, 0). Compute the [PPMI](/positive-pointwise-mutual-information/) matrix with $\log_2$. Which cells are zero, and why are some of them zero for a different reason than others?

2. ◦ Count the word-context pairs of the sentence "the cat sat on the mat" with a symmetric window of radius 2, each word paired with every other word at distance 1 or 2. How many pairs are there, and how often does the pair (the, sat) occur? With the weight $1/d$ for distance $d$, what is the total weight of all pairs?

3. ◦ Three word vectors are $u = (1, 2, 2)$, $v = (2, 1, 2)$ and $w = (2, -2, 1)$. Compute the three [cosine similarities](/cosine-similarity/). For the unit vectors $\hat u$ and $\hat v$, compute $\|\hat u - \hat v\|^2$ and check it against $2 - 2\cos(u, v)$.

4. ◦ A sentence has 6 tokens. How many (word, context) training pairs does the [skip-gram model](/skip-gram-model/) emit with the fixed window radius $C = 3$? The word2vec tool instead draws the radius of each window uniformly from $\{1, 2, 3\}$. What is the expected number of pairs then?

5. ◦ Three words have the counts 100, 10 and 1. Give the unigram distribution and the noise distribution of [negative sampling](/negative-sampling/), which raises the counts to the power $3/4$, to four decimals. Which word gains the most, relative to its unigram probability?

6. ◦ A vocabulary of four words has the probabilities 0.4, 0.3, 0.2 and 0.1. Build the Huffman tree of [hierarchical softmax](/hierarchical-softmax/) and give the path length of each word. Compare the expected number of binary decisions per word with that of a balanced tree and with the entropy of the distribution in bits.

7. ◦ The [subword skip-gram](/subword-information-embeddings/) represents a word by its character n-grams of lengths 3 to 6, taken from the word with "<" and ">" added, plus the word itself. How many rows of the input matrix does "embedding" use? How many n-grams does "go" have? Which n-gram do "her" and "where" share?

8. ◦ The sentence is split into the items [works] by [authors] such as [Herrick] , [Goldsmith] and [Shakespeare] were read in [schools] , [libraries] and other [public buildings], where brackets mark noun phrases. List every (hyponym, hypernym) pair that the six [Hearst patterns](/hearst-patterns/) extract, with the pattern number.

9. ◦ The target word is "bank" in "He sat on the bank of the river and watched the water." Sense 1 has the gloss "a financial institution that accepts deposits and lends money"; sense 2 has "sloping land beside a body of water such as a river". With the stop list {he, on, the, of, and, a, that, such, as}, run the simplified [Lesk algorithm](/lesk-algorithm/). Give both overlaps and the chosen sense.

10. • Redo Exercise 1 with context distribution smoothing: replace $P(c)$ by $P_\alpha(c) = \#c^{\alpha} / \sum_{c'} \#c'^{\alpha}$ with $\alpha = 0.75$. Give $P_\alpha$ and the new PMI of (cat, pet) and (cat, fur). Which context lost PMI, and why?

11. • In [GloVe](/glove/) with $x_{\max} = 100$ and $\alpha = 3/4$, compute the weight $f(x)$ for $x = 1, 10, 50, 100$ and $500$. A cell with $X = 10$ has the word vector $(0.5, -0.2)$, the context vector $(1.0, 0.4)$ and the biases $0.1$ and $0.2$. Compute its error $\vec w \cdot \vec c + b + \tilde b - \ln X$ and its weighted term of the loss.

12. • The corpus has the sentences "the cat runs", "the dog runs" and "a dog sleeps", with bigrams inside each sentence only. Compute the average mutual information, in nats, of the partition into single words, and after merging cat and dog. Which merges of two single words lose nothing in [Brown clustering](/brown-clustering/), and why?

13. • Map the source vectors $x_1 = (1, 0)$, $x_2 = (0, 1)$, $x_3 = (1, 1)$ to the targets $y_1 = (0, 1)$, $y_2 = (-1, 0.2)$, $y_3 = (-1, 1)$ by the orthogonal $W$ of [cross-lingual mapping](/cross-lingual-embedding-mapping/), without normalizing the vectors. Compute $M = \sum_i y_i x_i^\top$, the angle of the best rotation, $W$ and the residual $\sum_i \|W x_i - y_i\|^2$. Is a reflection better?

14. • Three mapped source words and three target words have the cosine matrix with rows $s_1 = (0.8, 0.3, 0.1)$, $s_2 = (0.6, 0.5, 0.2)$ and $s_3 = (0.6, 0.2, 0.5)$, one column per target. With $K = 2$, compute $r_T$ for each source, $r_S$ for each target and the [CSLS](/cross-domain-similarity-local-scaling/) scores. Compare the translations chosen by plain nearest neighbour and by CSLS.

15. • The gender direction is $g = (1, 0, 0)$. Neutralize nurse $= (0.6, 0, 0.8)$ by [hard debiasing](/hard-debiasing/). Then equalize the pair he $= (0.6, 0.8, 0)$ and she $= (-0.8, 0.6, 0)$. Compute the dot products of doctor $= (0, 0.6, 0.8)$ with he and she before and after.

16. • In the [word embedding association test](/word-embedding-association-test/), the associations $s(w, A, B)$ of the targets are $X$: 0.5, 0.3, 0.1 and $Y$: −0.1, 0.0, 0.4. Compute the test statistic, the effect size with the population and with the sample standard deviation, and the exact p-value over the 20 splits, both with the strict test of the paper and with "$\ge$".

17. • With $a = 10^{-3}$, compute the [SIF](/smooth-inverse-frequency-embedding/) weights $a/(a + p(w))$ of words with the probabilities $0.05$, $0.001$ and $0.0001$. Then remove from the vector $(2, 1)$ its projection on the unit common component $u = (1/\sqrt 2, 1/\sqrt 2)$.

18. • Two words are linked in a lexicon, with original vectors $\hat q_1 = (1, 0)$ and $\hat q_2 = (0, 1)$ and $\alpha = \beta = 1$. Run three sweeps of [retrofitting](/retrofitting-word-vectors/) as Jacobi updates and as Gauss-Seidel updates, from the original vectors. Find the fixed point and the factor by which the error shrinks per sweep in each form.

19. • A [Yarowsky](/yarowsky-algorithm/) decision list for "plant" has the counts (sense A, sense B): manufacturing (5, 0), life (1, 6), species (0, 3) and of (4, 3). With the smoothing $\alpha = 0.1$, compute each score $\ln \frac{c(f, s_f) + \alpha}{c(f, \bar s_f) + \alpha}$, where $s_f$ is the sense with the larger count, and sort the list. Which sense gets an occurrence with the features life, manufacturing and of?

20. • Unit vectors in the plane are at the angles $a = 0°$, $b = 30°$ and $c = 60°$, and the candidates are at $80°$ and $120°$. Find the answer of the question "$a$ is to $b$ as $c$ is to ?" under 3CosAdd and under 3CosMul with shifted cosines and $\varepsilon = 0.001$ ([word analogy](/word-analogy/)). Explain the difference.

21. ★ A corpus gives the 2 × 2 word-context counts $\begin{pmatrix} 6 & 2 \\ 3 & 1 \end{pmatrix}$. By the [shifted-PMI theorem](/sgns-implicit-factorization-theorem/), find the optimal dot products for $k = 1$ and $k = 5$ and the rank of the matrix. Repeat for $\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$ with $k = 1$ and $k = 2$, and give $\sigma(\vec w \cdot \vec c)$ at the optimum for the first cell with $k = 1$.

22. ★ Document A has the words at $(0, 0)$ and $(4, 0)$, document B at $(0, 3)$ and $(1, 0)$, each word with weight $1/2$. Compute the [word mover's distance](/word-movers-distance/), the relaxed bound RWMD and the centroid bound WCD. Which bound is tighter here? Prove that WCD never exceeds WMD.

23. ★ A [SimCSE](/simcse/) batch of three sentences has the cosine matrix $\cos(h_i, h^+_j)$ with rows $(0.9, 0.3, 0.1)$, $(0.2, 0.8, 0.4)$ and $(0.0, 0.5, 0.7)$. Compute the mean loss for $\tau = 1$ and $\tau = 0.05$. Find the limits as $\tau \to \infty$ and $\tau \to 0$, and say what condition on the matrix the second limit needs.

24. ★ A taxonomy has entity above animal and vehicle, dog and cat under animal, puppy under dog, and car and bus under vehicle. The corpus counts are dog 30, cat 10, puppy 20, car 20 and bus 20, and each concept counts its own words and those below it. Compute the information content in bits, the [Resnik similarity](/resnik-similarity/) and the Lin similarity of (dog, cat), (puppy, cat) and (dog, puppy). What does Resnik fail to separate that Lin does?

25. ★ For the data of Exercise 13, compute the unconstrained least squares map $W = (\sum_i y_i x_i^\top)(\sum_i x_i x_i^\top)^{-1}$ and its residual. Compare with the orthogonal map, and show that the least squares map changes the lengths of the source vectors while an orthogonal map keeps every cosine within the source language.
