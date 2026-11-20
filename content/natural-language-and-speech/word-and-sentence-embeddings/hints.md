1. $N = 18$, every row sums to 6 and the columns to 7, 7 and 4, so $\operatorname{PMI}(w, c) = \log_2 (18\,\#(w, c) / (6\,\#c))$. The PPMI rows are cat $(0.7776, 0, 0.585)$, dog $(0.3626, 0, 0.585)$ and car $(0, 1.3626, 0)$. Cat-drive, car-pet and car-fur are zero because the pair was never seen and PMI is $-\infty$; dog-drive was seen once, but its PMI $-1.2224$ is negative and is clipped.

2. Five adjacent places give 10 ordered pairs at distance 1, and four places at distance 2 give 8 more, so 18 pairs. The pair (the, sat) occurs twice: the first "the" is two words before "sat" and the second is two words after. The weighted total is $10 \cdot 1 + 8 \cdot \tfrac12 = 14$.

5. The unigram distribution is $(0.9009, 0.0901, 0.0090)$. The powers $100^{3/4} = 31.62$, $10^{3/4} = 5.62$ and $1$ give $(0.8268, 0.1470, 0.0261)$. The rarest word gains most: its probability is multiplied by about 2.9, the middle word's by 1.6, and the frequent word's falls.

7. `<embedding>` has 11 characters, so it has $9 + 8 + 7 + 6 = 30$ n-grams of lengths 3 to 6; with the word itself, 31 rows. `<go>` has the n-grams `<go`, `go>` and `<go>`, which is 3. The trigram `her` is in both `<her>` and `<where>`; the n-gram `<her>` of the short word is not in the long one.

9. Without stop words the context is {sat, bank, river, watched, water}. Gloss 1 shares no word with it; gloss 2 shares river and water. The overlaps are 0 and 2, so the algorithm picks sense 2, the river bank.

12. Write the bigram counts as a table with left words as rows and right words as columns. "The" and "a" occur only on the left, "runs" and "sleeps" only on the right. Merging a word that is only a row with a word that is only a column joins one row and one column of the class table that never meet, so no term of the sum changes.

13. For a rotation by $\theta$, $\operatorname{tr}(W^\top M) = 0.2 \cos\theta + 4 \sin\theta$, which is largest at $\tan\theta = 20$. The residual is $\sum \|x_i\|^2 + \sum \|y_i\|^2 - 2 \operatorname{tr}(W^\top M) = 8.04 - 2\sqrt{16.04}$. For a reflection the trace is at most $|M_{11} - M_{22}| = 2.2$.

14. $r_T(s)$ is the mean of the two largest entries in the row of $s$, and $r_S(t)$ the mean of the two largest in the column of $t$. Target $t_1$ has 0.8, 0.6 and 0.6 in its column, so it is a hub: $r_S(t_1) = 0.7$ is the largest, and CSLS $= 2\cos - r_T - r_S$ pushes it down.

16. The test statistic is $\sum_X s - \sum_Y s = 0.9 - 0.3$. For the p-value, a split has a larger statistic exactly when its three $X$ values sum to more than 0.9; list the 20 subsets of size 3 of the six values and count.

18. In Jacobi form both vectors update from the old values: $q_1 \leftarrow (\hat q_1 + q_2)/2$. In Gauss-Seidel form the new $q_1$ is used at once in the update of $q_2$. Write $e_t$ for the difference from the fixed point and find the map $e_t \mapsto e_{t+1}$.

21. $\operatorname{PMI}(w, c) = \ln \frac{\#(w, c)\, |D|}{\#w\, \#c}$, and the optimum is $\vec w \cdot \vec c = \operatorname{PMI}(w, c) - \ln k$. The first table is a product of its margins, so every PMI is 0. For the second table the matrix has distinct diagonal and off-diagonal entries, so look at its determinant.

22. Each word of A must send its mass $1/2$ to B, so there are two ways to pair the words, and both cost 3. For RWMD send each word to its nearest neighbour in the other document and take the larger of the two directions. For the bound, write the centroid difference as $\sum_{i,j} T_{ij} (x_i - y_j)$ for an optimal flow $T$ and use the triangle inequality.

23. The loss of sentence $i$ is $-\ln \frac{e^{S_{ii}/\tau}}{\sum_j e^{S_{ij}/\tau}}$. As $\tau \to \infty$ every softmax is uniform, so each loss tends to $\ln 3$. As $\tau \to 0$ the loss of row $i$ tends to 0 when $S_{ii}$ is the strict maximum of its row, as it is in every row here, and to infinity when another entry is larger.

24. The frequencies are entity 100, animal 60, dog 50 (its own 30 and puppy's 20), vehicle 40, and the rest their own counts. The lowest common subsumer of dog and cat and of puppy and cat is animal, so both Resnik values are $-\log_2 0.6 = 0.737$. Lin divides by $\operatorname{IC}(c_1) + \operatorname{IC}(c_2)$, which is larger for puppy than for dog.
