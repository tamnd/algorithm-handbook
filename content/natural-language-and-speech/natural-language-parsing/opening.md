The sentence "I saw the man with the telescope" has two readings: either the telescope is how I saw him, or the man has it. A parser makes such structure explicit. A constituency parser builds a tree of phrases, a noun phrase "the man with the telescope" or a verb phrase "saw the man" followed by "with the telescope". A dependency parser links each word to the word it modifies. Natural language grammars are ambiguous on a scale that programming languages are not, and a long sentence can have thousands of trees, so a parser for language must score its trees and pick the best one.

Parsing is a meeting point of algorithms and linguistics. The chart algorithms of Volume 9 carry over with probabilities, dependency parsing reduces to finding a maximum spanning arborescence or to a sequence of shift-reduce moves, and neural scorers now replace hand-written features. Beyond syntax, semantic parsing maps sentences to meaning representations, and discourse parsing finds the relations between sentences.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Constituency parsing.** Treebanks, constituency parsing and the PARSEVAL measures, parent annotation, lexicalized and latent-variable PCFGs, head rules, A* parsing and span-based neural parsing.
2. **Dependency parsing by graphs.** Dependency trees and projectivity, the Eisner algorithm, maximum spanning tree parsing, the biaffine scorer and attachment scores.
3. **Dependency parsing by transitions.** The arc-standard, arc-eager and arc-hybrid systems, the swap transition, dynamic oracles and the Chen-Manning neural parser.
4. **Grammar formalisms and induction.** Combinatory categorial grammar and supertagging, tree-adjoining grammar, unification of feature structures, and the dependency model with valence.
5. **Meaning and discourse.** Semantic parsing, abstract meaning representation and the Smatch measure, semantic role labeling, natural language inference and rhetorical structure theory.

## What to read meanwhile

Volume 9 has the parsing algorithms for context-free grammars: the [CYK algorithm](/cyk-algorithm/), the [Earley parser](/earley-parser/), [chart parsing](/chart-parsing/), [GLR parsing](/glr-parsing/), [left-corner parsing](/left-corner-parsing/) and [shift-reduce parsing](/shift-reduce-parsing/), along with the [probabilistic context-free grammar](/probabilistic-context-free-grammar/) and the [inside-outside algorithm](/inside-outside-algorithm/) that trains one. Graph-based dependency parsing needs a maximum spanning arborescence, which is the [minimum arborescence](/minimum-arborescence/) problem with negated weights, solved by the [Edmonds arborescence algorithm](/edmonds-arborescence/); it also uses the [matrix-tree theorem](/matrix-tree-theorem/) to sum over all trees, both in Volume 7.

A* parsing uses the search of [A* search](/a-star-search/) in Volume 29. Neural parsers are trained as in [structured prediction](/structured-prediction/) in Volume 25. Parsers start from tokens: the [Penn Treebank tokenization](/penn-treebank-tokenization/) of Chapter 41.1 is the one most English treebanks use.
