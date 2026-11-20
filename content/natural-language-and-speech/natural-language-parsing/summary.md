## What to remember

- Over $n$ words there are $(n+1)^{n-1}$ dependency trees and $n^{n-1}$ with one child of the root. The projective ones number 1, 3, 12, 55, 273 for $n = 1, \ldots, 5$, about 21% of all trees at $n = 5$ and a vanishing share as $n$ grows.
- PARSEVAL compares the multisets of labelled brackets: $F_1 = 2m/(|B(p)| + |B(g)|)$, summed over the corpus before dividing. Attachment scores count words with the right head (UAS) or the right head and label (LAS); since every word has one head, precision equals recall.
- Probabilistic CKY returns the exact best tree of a PCFG in $O(g n^3)$ time. A parser in $O(g n^{3-\varepsilon})$ would give Boolean matrix multiplication in $O(m^{3-\varepsilon/3})$ (Valiant–Lee). For latent-variable grammars the best tree is NP-hard, and parsers use max-rule decoding instead.
- A plain treebank grammar is weak. Parent annotation lifts $F_1$ from 72.62 to 76.81 in Klein and Manning's measurements; latent symbols learned by split-merge EM reach 90.7 on the development set, at the cost of local optima.
- For arc-factored scores the best tree is exact and cubic or better: the Eisner algorithm gives the best projective tree in $\Theta(n^3)$, Chu-Liu-Edmonds the best tree of any shape in $O(n^3)$, or $O(n^2)$ with Tarjan's implementation. With sibling scores the projective problem stays $O(n^3)$, while the non-projective one becomes NP-hard.
- Transition parsers use a linear number of moves ($2n$ for arc-standard and arc-hybrid, between $n$ and $2n$ for arc-eager) and choose them greedily or with a beam, so they are fast but approximate. Arc-standard, arc-eager and arc-hybrid build only projective trees; the swap move adds the others at $2n + 2k$ moves with $k \le n(n-1)/2$ swaps.
- A* parsing returns the exact Viterbi tree when its outside estimate is consistent (admissible and monotone); its worst case is no better than the chart, and the gain is measured, not proved.
- Meaning brings harder problems: the best Smatch mapping is NP-hard, so the hill-climbing score is a lower bound, and entailment in propositional logic is coNP-complete.

## The main methods side by side

| Method | Output | Time for $n$ words | Exact? |
|---|---|---|---|
| Probabilistic CKY | best tree of a PCFG | $O(g n^3)$ | yes |
| A* parsing | best tree of a PCFG | cubic worst case, fewer items in practice | yes, with a consistent estimate |
| Span-based chart | best binary tree for span scores | $\Theta(n^3 + n^2 L)$ | yes, for the span scores |
| Eisner algorithm | best projective dependency tree | $\Theta(n^3)$ | yes, arc-factored |
| Chu-Liu-Edmonds | best dependency tree of any shape | $O(n^3)$; $O(n^2)$ (Tarjan) | yes, arc-factored |
| Arc-standard, arc-eager, arc-hybrid | projective dependency tree | $O(n)$ moves | no, greedy or beam |
| Swap system | any dependency tree | $2n + 2k$ moves, $k \le n(n-1)/2$ | no, greedy or beam |

: Parsing algorithms of the chapter. $g$ is the grammar size and $L$ the number of labels; the time of a transition parser is the number of moves times the cost of one classifier call.

## Choosing a method

For phrase-structure trees, a span-based parser with a neural encoder and a cubic chart is the usual choice in recent work: it needs no grammar and is exact for its scores. A treebank PCFG with parent annotation or latent symbols is the choice when a probabilistic grammar is wanted, for example to compute inside probabilities or to sample trees.

For dependency trees, decide first whether crossing arcs matter. For English with head-rule conversions every tree is projective, and the Eisner algorithm is exact; for languages with free word order, Chu-Liu-Edmonds is exact and no slower. If the treebank requires one child of the root, use the single-root version rather than deleting extra arcs afterwards. A biaffine scorer with either decoder is a strong default. When speed matters most, a transition parser with a dynamic oracle parses in linear time; use swap or a graph parser if the language has many crossing arcs.

Report scores with the standard conventions: the COLLINS.prm settings for PARSEVAL, and a stated rule on punctuation for attachment scores. Numbers computed under different conventions cannot be compared.
