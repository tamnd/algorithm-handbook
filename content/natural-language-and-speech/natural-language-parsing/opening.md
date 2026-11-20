The sentence "astronomers saw stars with ears" has two trees under a small grammar: in one the stars have the ears, in the other the astronomers used ears to see. A parser has to choose. Programming languages are designed so that each program has one tree; natural language is not, and a sentence of 40 words can have thousands of trees under a treebank grammar. So a parser for language does two jobs at once: it finds the trees a sentence allows, and it scores them and returns the best.

Parsers sit inside many systems. Relation extraction and question answering read who did what to whom off a dependency tree, grammar checkers and machine translation systems use tree structure to move words, and semantic parsers turn questions into database queries. The chapter shows that the main parsing problems have exact algorithms of cubic cost: probabilistic CKY for phrase structure, Eisner's algorithm for projective dependency trees, and a maximum spanning arborescence for all dependency trees. It also shows the fast greedy parsers that most systems use in practice, which give up the guarantee for linear time.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Trees, treebanks and scores.** The two kinds of tree: [dependency trees](/dependency-tree/), with $(n+1)^{n-1}$ possible trees over $n$ words, and the [projective](/projective-dependency-tree/) ones without crossing arcs. A [treebank](/treebank/) gives the gold trees; [PARSEVAL](/parseval-measures/) and the [attachment scores](/attachment-score/) measure a parser against it.
2. **Constituency parsing.** [Constituency parsing](/constituency-parsing/) with a treebank grammar and its refinements: [head rules](/head-rules/), [parent annotation](/parent-annotation/), [lexicalized](/lexicalized-pcfg/) and [latent-variable](/latent-variable-pcfg/) grammars. [A* parsing](/a-star-parsing/) finds the same best tree with less work, and [span-based parsing](/span-based-constituency-parsing/) drops the grammar and scores spans.
3. **Graph-based dependency parsing.** The arc-factored [dependency parsing](/dependency-parsing/) problem, solved exactly by the [Eisner algorithm](/eisner-algorithm/) for projective trees and by [Chu-Liu-Edmonds](/mst-dependency-parsing/) for all trees, with scores from the [biaffine parser](/biaffine-dependency-parser/).
4. **Transition-based dependency parsing.** [Arc-standard](/arc-standard-parsing/), [arc-eager](/arc-eager-parsing/) and [arc-hybrid](/arc-hybrid-parsing/) systems, the [swap system](/swap-transition-system/) for crossing arcs, [dynamic oracles](/dynamic-oracle/) for training, and the neural [Chen-Manning parser](/chen-manning-parser/).
5. **Richer grammars and grammar induction.** [Feature structures](/feature-structure-unification/), [combinatory categorial grammar](/combinatory-categorial-grammar/), [tree-adjoining grammar](/tree-adjoining-grammar/), [supertagging](/supertagging/), and the [dependency model with valence](/dependency-model-with-valence/), which learns a grammar from raw text.
6. **Meaning and discourse.** [Semantic role labelling](/semantic-role-labeling/), [AMR](/abstract-meaning-representation/) and its metric [Smatch](/smatch/), [semantic parsing](/semantic-parsing/), [natural language inference](/natural-language-inference/) and [rhetorical structure theory](/rhetorical-structure-theory/).

## A first reading

For a first pass, read these in order:

1. [Dependency tree](/dependency-tree/)
2. [Projective dependency tree](/projective-dependency-tree/)
3. [Treebank](/treebank/)
4. [PARSEVAL measures](/parseval-measures/)
5. [Constituency parsing](/constituency-parsing/)
6. [Parent annotation](/parent-annotation/)
7. [Dependency parsing](/dependency-parsing/)
8. [Eisner algorithm](/eisner-algorithm/)
9. [MST dependency parsing](/mst-dependency-parsing/)
10. [Arc-standard parsing](/arc-standard-parsing/)
11. [Arc-eager parsing](/arc-eager-parsing/)
12. [Semantic role labelling](/semantic-role-labeling/)

This gives both kinds of tree, one exact method for each, and the two classic transition systems. The latent-variable grammar, A* parsing, the swap system, dynamic oracles and the whole of group 5 can wait for a second reading. Group 6 can be read on its own after group 1; its entries depend on the trees and the scores, not on the parsing algorithms.

## Before you start

The chapter assumes [context-free grammars](/context-free-grammar/) and [parse trees](/parse-tree/), and the chart algorithms of Volume 9: the [CYK algorithm](/cyk-algorithm/), [probabilistic context-free grammars](/probabilistic-context-free-grammar/), [probabilistic CKY](/probabilistic-cky/), the [inside-outside algorithm](/inside-outside-algorithm/) and [shift-reduce parsing](/shift-reduce-parsing/). Dependency parsing uses [rooted trees](/rooted-tree/) and, from Volume 7, [arborescences](/arborescence/), [Edmonds' algorithm](/edmonds-arborescence/) and the [matrix-tree theorem](/matrix-tree-theorem/). From Volume 25 you need [expectation-maximization](/expectation-maximization/), [structured prediction](/structured-prediction/) and [precision and recall](/precision-and-recall/). [A* search](/a-star-search/) is used once, in group 2. Within this volume, [sequence labelling](/sequence-labeling/) and [word embeddings](/word-embedding/) come up in the neural parsers and in role labelling.
