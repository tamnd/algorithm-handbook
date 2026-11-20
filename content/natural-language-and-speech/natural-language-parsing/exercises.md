1. ◦ Over $n = 3$ words, how many [dependency trees](/dependency-tree/) are there, how many have one child of the root, and how many are [projective](/projective-dependency-tree/)? Write the non-projective ones as head lists $(h_1, h_2, h_3)$, with 0 for the root.

2. ◦ Convert the tree (S (NP (DT the) (NN dog)) (VP (VBD chased) (NP (DT a) (NN cat)))) to a dependency tree with the [head rules](/head-rules/) "the head of S is its VP, the head of VP is its verb, the head of NP is its last noun". Give the head list.

3. ◦ The sentence "John saw Mary today" has the gold head list $(2, 0, 2, 2)$. Write the oracle transition sequence of [arc-standard parsing](/arc-standard-parsing/) and of [arc-eager parsing](/arc-eager-parsing/) for it, starting from the stack holding only the root, and count the moves of each.

4. ◦ The gold analysis of "she gave him a book ." has heads $(2, 0, 2, 5, 2, 2)$ with labels nsubj, root, iobj, det, obj, punct. A parser outputs heads $(2, 0, 2, 5, 3, 2)$ with labels nsubj, root, obj, det, obj, punct. Compute the [attachment scores](/attachment-score/) UAS and LAS, first counting the full stop and then without it.

5. ◦ The gold tree of "the old man left the room after the talk" is (S (NP the old man) (VP left (NP the room) (PP after (NP the talk)))), with preterminals omitted. A parser outputs (S (NP the old man) (VP left (NP the room (SBAR after (NP the talk))))). Compute labelled precision, recall and $F_1$ under the [PARSEVAL measures](/parseval-measures/), and the same with labels ignored.

6. ◦ In [combinatory categorial grammar](/combinatory-categorial-grammar/), give *John* and *Mary* the category NP and *likes* the category (S\NP)/NP. Derive "John likes Mary" by application only, and then by type raising *John* and composing it with *likes* first. Which category does "John likes" get in the second derivation?

7. ◦ [Unify](/feature-structure-unification/) [CAT np, AGR [NUM sg]] with [AGR [PER 3, NUM sg]], and then with [AGR [NUM pl]]. Give the result or say why it fails.

8. ◦ The gold AMR is (s / see-01 :ARG0 (g / girl) :ARG1 (b / boy)) and the test AMR is (x / see-01 :ARG0 (y / boy) :ARG1 (z / girl)). Find the best [Smatch](/smatch/) mapping and the score. Is the best mapping unique?

9. • A [treebank](/treebank/) has three trees: (S (NP (DT the) (NN dog)) (VP (VBD barked))), (S (NP (PRP she)) (VP (VBD saw) (NP (DT the) (NN dog)))) and (S (NP (PRP she)) (VP (VBD barked))). Read off the maximum likelihood PCFG and compute the probabilities of the trees of "the dog saw the dog" and "she barked".

10. • A PCFG has the rules S → NP VP (1), VP → V NP (0.7), VP → VP PP (0.3), NP → NP PP (0.2), PP → P NP (1), NP → she (0.2), NP → fish (0.4), NP → forks (0.2), V → eats (1), P → with (1). Find both trees of "she eats fish with forks" with their probabilities, the tree [constituency parsing](/constituency-parsing/) returns, and its posterior probability given the sentence.

11. • The arc scores $s(h, d)$ over three words are 1 except $s(0, 1) = 3$, $s(0, 2) = 10$, $s(2, 3) = 10$ and $s(3, 1) = 10$. Find the best tree, the best projective tree that the [Eisner algorithm](/eisner-algorithm/) returns, and the best projective tree with one child of the root. Which of them does the [Chu-Liu-Edmonds algorithm](/mst-dependency-parsing/) return?

12. • The arc scores over three words are given below (row: head, column: dependent). Find the best tree without a constraint on the root, and the best tree with exactly one child of the root.

| $s(h, d)$ | 1 | 2 | 3 |
|---|---|---|---|
| 0 | 9 | 8 | 3 |
| 1 | – | 2 | 1 |
| 2 | 1 | – | 5 |
| 3 | 1 | 4 | – |

13. • Take the non-projective tree $(3, 0, 2)$ of exercise 11. Give its projective order (the order of an inorder walk of the tree), the number of swaps the [swap system](/swap-transition-system/) needs, and the oracle transition sequence. Check the length against $2n + 2k$.

14. • A [span-based parser](/span-based-constituency-parsing/) over four words, with fenceposts 0 to 4, has span scores $s(0,2) = 3$, $s(1,3) = 4$, $s(2,4) = 2$, $s(0,3) = 1$ and $s(1,4) = 3$, and 0 for all other spans. How many binary trees are there over four words? Run the chart and give the best tree and its score.

15. • A [semantic role labeller](/semantic-role-labeling/) has six candidate argument spans over a six-word sentence, with scores [1, 2]: 3, [2, 4]: 5, [3, 5]: 4, [5, 6]: 2, [1, 3]: 4 and [6, 6]: 1. Choose a set of non-overlapping spans of largest total score by [weighted interval scheduling](/weighted-interval-scheduling/).

16. • A Smatch mapping sends each of $m$ test variables to a different gold variable or to nothing. Show that with $n$ gold variables there are $\sum_k \binom{m}{k}\binom{n}{k} k!$ mappings, and compute the number for $m = n = 4$.

17. • Write the Eisner algorithm over the counting semiring (sums and products of counts in place of max and plus) and use it to count the projective trees for $n = 1, \ldots, 6$. Then change the program so that the root takes exactly one child, and count again.

18. • Over two words, the arc weights are $w(0,1) = 1$, $w(0,2) = 2$, $w(1,2) = 3$ and $w(2,1) = 4$, and the weight of a tree is the product of its arc weights. Compute the sum $Z$ of the weights of all trees by listing them, and again as the determinant of the $2 \times 2$ Laplacian of the [matrix-tree theorem](/matrix-tree-theorem/).

19. • Show that deciding entailment between two formulas of propositional logic, the logical core of [natural language inference](/natural-language-inference/), is coNP-hard, by a reduction from the tautology problem.

20. ★ Show that the number of projective dependency trees over $n$ words is $\frac{1}{2n+1}\binom{3n}{n}$, and that the number with one child of the root is $\frac{1}{n}\binom{3n-2}{n-1}$. Check both against the counts of exercise 17.

21. ★ Prove that [A* parsing](/a-star-parsing/) with a consistent outside estimate pops every item with its best inside score, so the first goal item popped is the Viterbi parse. Where does the proof use consistency rather than admissibility alone?

22. ★ Show how to find the best dependency tree with exactly one child of the root by $n$ runs of Chu-Liu-Edmonds, prove it correct, and give its cost. Check your method on exercise 12.

23. ★ Show that computing the Smatch score exactly is NP-hard, by a reduction from a graph problem in which the instance triples carry no information.

24. ★ Draw the root at position 0, to the left of the words. Prove that a dependency tree has no two crossing arcs if and only if the words below each node form a contiguous span.
