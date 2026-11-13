1. ◦ How many unrooted binary [phylogenetic trees](/phylogenetic-tree/) are there on 7 taxa, and how many [rooted](/rooted-and-unrooted-trees/) binary trees on 6 taxa? How many inner vertices, edges and inner edges does an unrooted binary tree on 7 taxa have? Explain why the two counts are equal.

2. ◦ Write down the nontrivial [splits](/splits-of-a-tree/) of the unrooted trees `(A,(B,C),(D,(E,(F,G))));` and `(A,(B,(C,D)),(E,(F,G)));` given in [Newick format](/newick-format/). What is their [Robinson-Foulds distance](/robinson-foulds-distance/), and what is the largest possible value for two binary trees on 7 taxa?

3. ◦ The rooted tree `(((1,2),3),((4,5),6));` has the states A, C, A, G, C, G at the leaves 1 to 6. Run [Fitch's algorithm](/fitch-algorithm/): give the set at each inner node, the score, and one labeling that reaches it. Is the site [parsimony-informative](/parsimony-informative-site/)?

4. ◦ Two aligned sequences of 100 sites differ at 30 of them. Give their [Jukes-Cantor](/jukes-cantor-model/) distance and its approximate standard error. What happens if they differ at 75 sites?

5. ◦ Check the [four-point condition](/four-point-condition/) for the matrix with $D_{AB} = 5$, $D_{AC} = 11$, $D_{AD} = 8$, $D_{BC} = 12$, $D_{BD} = 9$ and $D_{CD} = 5$. If it is a [tree metric](/tree-metric/), give the split of its tree and the length of every edge. Then change $D_{AD}$ to 9 and check again.

6. ◦ Run [neighbor-joining](/neighbor-joining/) on the matrix of Exercise 5. Give the row sums, the six values of $Q$, the pair that is joined first and the lengths of its two new edges. Does the output match your tree from Exercise 5?

7. ◦ Root the tree `((A:2,B:8):1,E:5,(C:3,D:6):2);` by [midpoint rooting](/midpoint-rooting/). Which leaf-to-leaf path is the longest, where does the root go, and what is the rooted tree in Newick format?

8. ◦ Take the rooted trees $T_1 =$ `(((A,B),C),(D,E));`, $T_2 =$ `(((A,B),D),(C,E));` and $T_3 =$ `((A,(B,C)),(D,E));`. Give their [strict consensus](/strict-consensus/) and their [majority-rule consensus](/majority-rule-consensus/). Then give the size of a [maximum agreement subtree](/maximum-agreement-subtree/) of $T_1$ and $T_3$, and their [rooted SPR distance](/spr-distance/).

9. ◦ On the rooted tree `(((A,B),C),(D,E));` a binary character has state 1 at A, C and D and state 0 at B and E. Give its score under Fitch parsimony, [Camin-Sokal parsimony](/camin-sokal-parsimony/) (the root has state 0 and changes go only from 0 to 1) and [Dollo parsimony](/dollo-parsimony/) (state 1 arises once and can then be lost).

10. ◦ Three species have the rooted tree $((A,B),C)$, and the branch between the two speciations is 1 coalescent unit long. With what probability does the gene tree of one locus match the species tree, and with what probability is it each of the two others, by the formula of [incomplete lineage sorting](/incomplete-lineage-sorting/)? Separately, for a sample of 4 gene copies under the [Kingman coalescent](/kingman-coalescent/), give the expected time to the most recent common ancestor and the expected total branch length, and convert the first into generations for a diploid population of 10,000 individuals.

11. ◦ For each case below, give the guarantee that its entry states. The possible answers are: exact for its objective; NP-hard; statistically consistent under the stated model; converges only in the limit; or no guarantee, with inputs on which it fails. (a) Fitch's algorithm on a fixed rooted binary tree. (b) Finding a most parsimonious tree over all trees. (c) Neighbor-joining on Jukes-Cantor distances, for sequences that evolved under the Jukes-Cantor model on a binary tree. (d) [UPGMA](/upgma/) on the tree metric of a tree that has no clock. (e) Maximum parsimony on four taxa in the Felsenstein zone of [long-branch attraction](/long-branch-attraction/). (f) The Markov chain of [Bayesian inference](/bayesian-phylogenetic-inference/), run for a finite number of steps. (g) [ASTRAL](/astral/) on true gene trees drawn from the [multispecies coalescent](/multispecies-coalescent/).

12. • Run the [Sankoff algorithm](/sankoff-algorithm/) on the tree and the states of Exercise 3, with cost 1 for a transition (A and G, or C and T) and cost 2 for a transversion. Give the cost table at each inner node, the score and the best root states. Does the labeling you found in Exercise 3 reach this score?

13. • A matrix on five taxa has $D_{AB} = 2$, $D_{AC} = 4$, $D_{BC} = 8$, $D_{AD} = D_{BD} = 7$, $D_{CD} = 12$, $D_{AE} = D_{BE} = 10$, $D_{CE} = 7$ and $D_{DE} = 10$. Run UPGMA and [WPGMA](/wpgma/) on it and give the order of the joins and the height of each node. Why do the two trees differ, and why could they not differ if the matrix were an [ultrametric](/ultrametric/)?

14. • A star tree joins three leaves to one inner node, and every edge has Jukes-Cantor length $t$ with $e^{-4t/3} = 1/2$. Using [Felsenstein's pruning algorithm](/felsenstein-pruning/) with the root at the inner node, compute the [likelihood](/phylogenetic-likelihood/) of the site patterns AAA, AAC and ACG. Check that the probabilities of all 64 patterns add up to 1.

15. • Under the Jukes-Cantor model, let $p(t)$ be the probability that the two ends of a branch of length $t$ differ. Show that $1 - \frac43 p(t) = e^{-4t/3}$ and that this quantity multiplies along a path: two branches of lengths $s$ and $t$ in a row act like one branch of length $s + t$. Conclude that the Jukes-Cantor correction applied to the expected proportion of differences gives back the path length, so the corrected distances tend to a tree metric as the number of sites grows.

16. • Show that for four taxa the neighbor-joining criterion is $Q(i, j) = -(D_{ik} + D_{il} + D_{jk} + D_{jl})$, where $k$ and $l$ are the other two taxa. Deduce that $Q(A, B) = Q(C, D)$, and that on a tree metric with split $AB \mid CD$ the minimum of $Q$ is reached exactly at the two cherries when the inner edge is longer than 0.

17. • Prove that every ultrametric satisfies the four-point condition. Then take the unrooted tree with split $AB \mid CD$, pendant edges of lengths 1, 10, 1 and 10 to A, B, C and D, and an inner edge of length 2. Write down its tree metric, show that it is not an ultrametric, and show that UPGMA returns the wrong unrooted tree on it while neighbor-joining returns the right one.

18. • Five taxa $a, b, c, d, e$ have four binary characters: $c_1$ is 1 on $\{a, b\}$, $c_2$ on $\{a\}$, $c_3$ on $\{c, d\}$ and $c_4$ on $\{c\}$, and 0 elsewhere. Check the [four-gamete condition](/four-gamete-condition/) for each pair and build the rooted [perfect phylogeny](/perfect-phylogeny/) with the root in state 0000, as [Gusfield's algorithm](/gusfield-perfect-phylogeny/) would. Then add $c_5$, which is 1 on $\{a, c\}$. Which pairs now fail, and what is the largest set of characters that fit one tree, found as a [maximum clique](/maximum-clique/) of the compatibility graph of [character compatibility](/character-compatibility/)?

19. • The species tree is $((a,b),c)$ and the gene tree is $((a_1,(b_1,c_1)),(a_2,c_2))$, where $a_1$ and $a_2$ are two gene copies from species $a$, and $c_1$ and $c_2$ two from species $c$. Compute the [LCA reconciliation](/lca-reconciliation/): the image of each inner node of the gene tree, the nodes that are duplications, and the number of losses. Then tell the story of the gene family that these events describe, and check that it has the same number of losses.

20. • Show that the unrooted trees `((A,B),C,(D,E));` and `(B,C,(D,(A,E)));` share no nontrivial split, so their Robinson-Foulds distance is as large as it can be on five taxa, yet one [SPR move](/subtree-prune-and-regraft/) turns one into the other. Prove that one [NNI](/nearest-neighbor-interchange/) changes exactly one split, so the NNI distance is at least half the Robinson-Foulds distance, and find the NNI distance of these two trees.

21. • Under the uniform prior on rooted binary trees on four taxa, what is the prior probability that $\{A, B\}$ is a cluster of the tree? What is it under the [Yule model](/yule-model/)? What does this say about the posterior clade probabilities reported by Bayesian programs?

22. • The tree `((A:1,B:1):0.5,C:2);` has a trait with the values 4, 6 and 1 at A, B and C. Compute the two standardized [independent contrasts](/phylogenetic-independent-contrasts/), the estimate at the root and the estimate $\hat\sigma^2$ of the rate. Check the root estimate against the generalized least squares formula with the covariance matrix of Brownian motion on this tree.

23. • Four sampled sequences over four sites in order are 0000, 1100, 0110 and 1011. Find the pairs of sites that fail the four-gamete test, and compute the lower bound $R_M$ of Hudson and Kaplan on the number of recombinations in any history of the sample, as defined in [ancestral recombination graph inference](/ancestral-recombination-graph-inference/).

24. • Take $m$ binary characters, none of them constant. Prove that some tree has parsimony score exactly $m$ if and only if the characters are pairwise compatible, and that the tree is then a perfect phylogeny. This ties [maximum parsimony](/maximum-parsimony/) to perfect phylogeny.

25. ★ Let $D$ be within $\varepsilon$ of the tree metric of a binary tree on four taxa with split $AB \mid CD$ and inner edge $e$, entry by entry. Prove that neighbor-joining returns $AB \mid CD$ whenever $\varepsilon < e/2$, whatever the lengths of the pendant edges. Give a matrix with $\varepsilon = e/2$ on which it can return a wrong tree. Then use Exercise 15 to show that neighbor-joining on Jukes-Cantor distances is statistically consistent for four taxa under the Jukes-Cantor model.

26. ★ Under the multispecies coalescent, take a rooted species tree on four taxa whose unrooted form is $AB \mid CD$ with inner edge of length $t$ in coalescent units. Do this for both rooted shapes, the caterpillar $(((A,B),C),D)$ and the balanced $((A,B),(C,D))$, and say which branch lengths make up $t$ in each. Prove that the unrooted gene tree of one locus is $AB \mid CD$ with probability $1 - \frac23 e^{-t}$ and each other quartet with probability $\frac13 e^{-t}$.

27. ★ Prove that the expected number of cherries of a Yule tree with $n \ge 3$ leaves is $n/3$. Use the forward process, in which the leaf that splits next is uniform among the current leaves.

28. ★ Let $X = A \cup B$ with $|A| = a \ge 2$ and $|B| = b \ge 2$. Prove that exactly $(2a-3)!!\,(2b-3)!!$ unrooted binary trees on $X$ have the split $A \mid B$. Under the uniform prior on unrooted binary trees on six taxa, what is the prior probability of a given split with two taxa on one side? With three on each side?

29. ★ A population of $N$ gene copies has a Kingman genealogy, and a sample of $n \ge 2$ copies is drawn from it at random without replacement. Using the uniform root split proved on the [Kingman coalescent](/kingman-coalescent/) page, prove that the sample has the same most recent common ancestor as the whole population with probability $1 - \frac{2(N - n)}{(n+1)(N-1)}$, and find the limit as $N \to \infty$.
