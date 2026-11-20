1. Each of the 2 source words has 3 choices, so there are $3^2 = 9$ alignments. $p(f \mid e) = \frac{\varepsilon}{9}(0.1 + 0.6 + 0.1)(0.1 + 0.1 + 0.7) = 0.08\,\varepsilon$. The posterior of das–the is $0.6/0.8 = 3/4$, and the best alignment is das–the, Haus–house, each word choosing its best link alone.

2. $A_1$: $|A_1 \cap S| = 3$ and $|A_1 \cap P| = 4$, so $\mathrm{AER} = 1 - 7/7 = 0$; it contains $S$ and lies inside $P$. $A_2$: $|A_2 \cap S| = 1$ and $|A_2 \cap P| = 3$, so $\mathrm{AER} = 1 - 4/6 = 1/3$.

3. $p_1 = 5/6$, $p_2 = 4/5$, $p_3 = 3/4$, $p_4 = 2/3$; the lengths are equal, so the brevity penalty is 1, and $\mathrm{BLEU} = (1/3)^{1/4} \approx 0.760$.

5. Yes for 2 1 4 3, 3 4 1 2, 4 3 2 1 and 1 3 2 4; no for 2 4 1 3 and 3 1 4 2, the two patterns that separable permutations avoid.

6. Five pairs: $f_1$/$e_1$, $f_2$/$e_3$, $f_3$/$e_2$, $f_2 f_3$/$e_2 e_3$ and the whole sentence pair. A pair such as $f_1 f_2$ fails, because its target span $e_1 \ldots e_3$ contains $e_2$, which links to $f_3$ outside.

7. Monotone (it starts at 0), discontinuous, swap (it ends at 4, where the previous phrase started), discontinuous.

9. After round 1, $t(\text{la} \mid \text{the}) = 1/2$ and $t(\text{maison} \mid \text{house}) = 1/2$. After round 2, $t(\text{la} \mid \text{the}) = 3/5$ and $t(\text{maison} \mid \text{house}) = 4/7$. The shared word "the" pulls "la" towards itself, which leaves "maison" to "house".

11. The lines are $-2 - 3\gamma$, $-3 - \gamma$ and $-5$. A wins for $\gamma < 1/2$, B for $1/2 < \gamma < 2$, and C for $\gamma > 2$. The fewest errors, 1, hold on the open interval $(1/2, 2)$.

12. The sums are $m = (9, 7, 5, 3)$ and $t = (16, 14, 12, 10)$, with $c = 16 > r = 12$, so the brevity penalty is 1 and corpus BLEU is $(135/3840)^{1/4} = \sqrt 3 / 4 \approx 0.433$. On its own the first sentence would get $e^{1 - 6/3} = e^{-1}$. The long second hypothesis hides the short first one.

16. With $k = 2$ it pops (1, 1) with $-3$ and (2, 1) with $-4$. The best item is (2, 2) with $-2$, which it finds only with $k = 3$; even then it misses (1, 3) and (3, 1) with $-3$, which beat (2, 1).

20. Each factor $\sum_i t(f_j \mid e_i)$ is linear in $t$, its logarithm is concave, and a sum of concave functions is concave over the convex set of tables. For the corpus, the likelihood depends only on $s(x) = t(x \mid a) + t(x \mid b)$ and equals $s^3(2 - s)/16$, maximal at $s = 3/2$; both $t(x \mid a) = t(x \mid b) = 3/4$ and $t(x \mid a) = 1$, $t(x \mid b) = 1/2$ give $27/256$.

21. A separable permutation of size at least 2 is a direct sum or a skew sum. Let $D$ count those that are not direct sums; by symmetry the skew sums are counted by $A - D$, so $D = x + (A - D)$, and $A = D/(1 - D)$. Eliminating $D$ gives the equation, and its coefficients are 1, 2, 6, 22, 90, 394, 1806, so $a_7 = 1806$.

22. Make one target word per city and give each source word a single translation, so that $p(f \mid e)$ is the same for every order of the same words. Fix one city $v$, give the source one word for each other city, and let the bigram model give probability only to bigrams along edges, where the sentence start and end stand for $v$. A target sentence then has nonzero probability exactly when its order is a Hamilton cycle through $v$, so deciding whether the best translation has nonzero probability decides the Hamilton cycle problem (Knight 1999).

23. The score of a candidate along the line is $a + \gamma b$, and the model's choice is the upper envelope of these lines, a convex piecewise linear function; each line touches it on an interval or not at all. Sort the lines by slope and sweep with a stack, as for a convex hull, then sort the breakpoints of all sentences and sum the errors interval by interval.

24. A source interval maps to target positions $\pi(I)$; the pair is consistent exactly when these form an interval $J$, since then no link reaches into $J$ from outside $I$. If every pair of neighbours maps to neighbours, $\pi$ moves by $\pm 1$ at each step, and injectivity forces one sign throughout. For 2 4 1 3 only the 4 single positions and the whole sentence work, 5 pairs.
