Two rules are enough to add natural numbers written as $0$, $s(0)$, $s(s(0))$ and so on: $0 + y \to y$ and $s(x) + y \to s(x + y)$. To compute $s(s(0)) + s(0)$, find a part of the term that matches a left side, replace it by the right side, and repeat: $s(s(0)) + s(0) \to s(s(0) + s(0)) \to s(s(0 + s(0))) \to s(s(s(0)))$. No rule applies to the last term, so it is the answer. Nothing in the process knows about numbers. It only matches trees and replaces them.

This is [term rewriting](/term-rewriting-system/). The same mechanism runs functional programs, simplifies expressions in computer algebra systems, decides equalities in theorem provers, optimizes code in compilers and defines the semantics of languages such as Maude. Two questions come up for every system: whether rewriting always stops, which is [termination](/termination/), and whether the answer depends on which rule is applied where. A system whose answers never depend on the order is [confluent](/confluence/). A system with both properties computes a unique [normal form](/normal-form/) for every term, and so decides equality in the theory its rules describe.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **Terms and matching.** [Terms](/term/), [subterms](/subterm/) and [contexts](/term-context/), and [term matching](/term-matching/) in linear time.
2. **Rewrite systems.** [Rewrite rules](/rewrite-rule/), [abstract reduction systems](/abstract-reduction-system/), normal forms, termination and [string rewriting](/string-rewriting-system/).
3. **Confluence.** [Newman's lemma](/newman-lemma/), [critical pairs](/critical-pair/) and the [critical pair lemma](/critical-pair-lemma/), and the [confluence of orthogonal systems](/orthogonal-confluence-theorem/).
4. **Strategies and evaluation.** [Innermost](/innermost-reduction/) and [outermost reduction](/outermost-reduction/), and [graph reduction](/graph-reduction/), which shares subterms.
5. **Lambda calculus and combinators.** [Beta-reduction](/beta-reduction/), the [Church-Rosser theorem](/church-rosser-theorem/) and [combinatory logic](/combinatory-logic/).
6. **Proving termination.** [Reduction orderings](/well-founded-reduction-ordering/) such as the [lexicographic path ordering](/lexicographic-path-ordering/) and the [Knuth-Bendix ordering](/knuth-bendix-ordering/), [polynomial interpretations](/polynomial-interpretation/) and [dependency pairs](/dependency-pairs/).
7. **Equations and completion.** [Equational theories](/equational-theory/), the [word problem](/word-problem/), [Knuth-Bendix completion](/knuth-bendix-completion/) and [narrowing](/narrowing/).
8. **Rewriting modulo theories.** [Rewriting modulo equations](/rewriting-modulo-equations/) and [AC matching](/ac-matching/).
9. **Matching many patterns.** [Tree pattern matching](/tree-pattern-matching/), the [Hoffmann-O'Donnell automaton](/hoffmann-odonnell-matching/) and [discrimination trees](/discrimination-tree/).
10. **Computation and undecidability.** [Markov algorithms](/markov-algorithm/) and the undecidability of the [word problem](/undecidability-of-word-problem/) and of [termination](/undecidability-of-termination/).

## A first reading

For a first reading, take these fifteen entries in order: [term](/term/), [term matching](/term-matching/), [rewrite rule](/rewrite-rule/), [abstract reduction system](/abstract-reduction-system/), [term rewriting system](/term-rewriting-system/), [normal form](/normal-form/), [termination](/termination/), [confluence](/confluence/), [Newman's lemma](/newman-lemma/), [critical pair](/critical-pair/), [critical pair lemma](/critical-pair-lemma/), [reduction strategy](/reduction-strategy/), [lexicographic path ordering](/lexicographic-path-ordering/), [word problem](/word-problem/) and [Knuth-Bendix completion](/knuth-bendix-completion/). They lead from the definitions to the main algorithm of the field: turning equations into a system that decides them. Readers who come from functional programming can add groups 4 and 5 next; readers who come from automated reasoning can add groups 6 and 8.

## Before you start

Terms are [rooted trees](/rooted-tree/) from Volume 7, and most algorithms here walk them in [preorder](/preorder-traversal/). Matching and the critical pair construction use [substitutions](/substitution/) and the [most general unifier](/most-general-unifier/). Termination arguments rest on [well-founded relations](/well-founded-relation/) and the [lexicographic order](/lexicographic-order/), and the proofs use [structural induction](/structural-induction/). Groups 5 and 10 assume the [lambda calculus](/lambda-calculus/) and [Turing machines](/turing-machine/) from Volume 1; the term indexes of group 9 are [tries](/trie/) over terms. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
