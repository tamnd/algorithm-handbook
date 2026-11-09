## What to remember

- A **context-free grammar** rewrites one nonterminal at a time. Its derivations are recorded by **parse trees**, and a grammar is **ambiguous** when some string has two of them. Ambiguity is a property of the grammar; a few languages, the inherently ambiguous ones, have no unambiguous grammar at all.
- **Pushdown automata** accept exactly the context-free languages. The **deterministic** ones accept a smaller class, and by [Knuth's theorem](/knuth-lr-theorem/) it is exactly the class of languages with LR(k) grammars.
- To prove a language is **not context-free**, use the [pumping lemma](/cfl-pumping-lemma/), often after intersecting with a regular language. Context-free languages are closed under union, concatenation, star and intersection with regular languages, but not under intersection or complement.
- **Emptiness and finiteness** take linear time and **membership** takes cubic time, but **ambiguity, equivalence** and emptiness of an intersection are undecidable.
- **General parsing is cubic.** [CYK](/cyk-algorithm/) needs Chomsky normal form; [Earley](/earley-parser/) takes any grammar and is quadratic on unambiguous ones and linear on many grammars of programming languages. Valiant's algorithm is faster in theory, and [Lee's theorem](/valiant-lee-theorem/) shows that a much faster general parser would give faster Boolean matrix multiplication.
- **Linear-time parsing needs a restricted grammar.** Top-down [LL(1)](/ll1-parsing/) parsing chooses a production from one token of lookahead and cannot handle left recursion. Bottom-up [LR](/lr-parsing/) parsing shifts tokens and reduces handles, and accepts more grammars; [LALR](/lalr-parsing/) is the usual compromise between table size and power.
- **Expressions** have their own short methods: the [shunting-yard algorithm](/shunting-yard-algorithm/) and [Pratt parsing](/pratt-parsing/) handle precedence and associativity from a table of operators, without a grammar in normal form.

## The main algorithms side by side

| Task | Method | Time | Grammars |
|---|---|---|---|
| Is $L(G)$ empty? | [Emptiness](/cfg-emptiness-problem/) | $O(g)$ | all |
| Is $L(G)$ finite? | [Finiteness](/cfg-finiteness-problem/) | $O(g)$ | all |
| Normal form | [Chomsky normal form conversion](/chomsky-normal-form-conversion/) | $O(g^2)$ | all |
| Remove left recursion | [Left-recursion removal](/left-recursion-removal/) | $O(g^2)$ | all |
| Parse | [CYK](/cyk-algorithm/) | $\Theta(n^3 g)$ | Chomsky normal form |
| Parse | [Earley](/earley-parser/) | $O(n^3 G)$ | all; $O(n^2 G)$ if unambiguous |
| Recognize | [Valiant](/valiant-algorithm/) | $O(g n^{\omega})$ | Chomsky normal form |
| Parse | [GLR](/glr-parsing/) | $O(n^{p+1})$ | all |
| Parse | [LL(1)](/ll1-parsing/) | $O(n)$ | LL(1) |
| Parse | [Recursive descent](/recursive-descent-parsing/) | $O(n)$ | LL(1), written by hand |
| Parse | [LR(0)](/lr0-parsing/), [SLR](/slr-parsing/), [LALR](/lalr-parsing/), [canonical LR](/canonical-lr-parsing/) | $O(n)$ | LR(0) $\subset$ SLR(1) $\subset$ LALR(1) $\subset$ LR(1) |
| Parse expressions | [Shunting yard](/shunting-yard-algorithm/), [Pratt](/pratt-parsing/) | $\Theta(n)$ | operator tables |
| Parse | [Packrat](/packrat-parsing/) | $O(g n)$ | parsing expression grammars |
| Most probable parse | [Probabilistic CKY](/probabilistic-cky/) | $\Theta(n^3 g)$ | probabilistic, Chomsky normal form |

: The main algorithms of the chapter. Here $n$ is the length of the input, $g$ and $G$ are the size of the grammar as each entry measures it, $\omega$ is the exponent of matrix multiplication, and $p$ is the length of the longest right side of a production, or 2 if all are shorter.

## Choosing a parser

- For a language you design, write an LL(1) grammar and a recursive-descent parser by hand, with a Pratt parser or a precedence table for expressions. This is what most production compilers do, because the code is easy to read and to give good error messages.
- If the grammar is given and large, use a parser generator for LALR(1) or LR(1) grammars (Chapter 9.4), and resolve the conflicts it reports by changing the grammar or by declaring precedence.
- If the grammar is ambiguous on purpose, as in natural language, or comes from users, use Earley or GLR, and keep all parses in a [shared packed parse forest](/shared-packed-parse-forest/). For natural language, rank the parses with a [probabilistic grammar](/probabilistic-context-free-grammar/).
- Use CYK when you need the simplest correct general algorithm, or when the grammar is already in Chomsky normal form.
- Before you trust a grammar for a programming language, check it for ambiguity with the conflicts of an LR generator: no general algorithm can decide ambiguity, but an LR(1) grammar is never ambiguous.
