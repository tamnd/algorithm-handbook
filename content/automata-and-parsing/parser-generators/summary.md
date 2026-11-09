## What to remember

- A parser generator turns a grammar into tables and checks the grammar while doing so. A conflict in the table is the generator's way of saying the grammar is outside its class.
- Nullable, FIRST and FOLLOW come first, in that order, and each is a least fixed point. With a graph view and an SCC search, all three take $O(|G| \cdot |\Sigma|)$ time.
- A grammar is LL(1) exactly when the PREDICT sets of the alternatives of each nonterminal are disjoint. For $k \ge 2$ the strong LL(k) grammars are a smaller class than the LL(k) grammars, and left recursion rules out LL(k) for every $k$.
- The LR(0) automaton of item sets is the skeleton of every LR table. SLR(1), LALR(1) and canonical LR(1) differ only in the lookaheads on which they reduce, and the sets shrink in that order.
- The LR(0) collection can be exponential in the size of the grammar, so table construction is measured against the output size, not only against $|G|$.
- DeRemer and Pennello compute LALR(1) lookaheads with four relations on nonterminal transitions and two SCC traversals, without building the LR(1) collection.
- Yacc settles shift-reduce conflicts by precedence and associativity, and otherwise by shifting; a rule takes the precedence of its last terminal unless `%prec` says otherwise.
- Default reductions and displacement packing make LR tables small, at the price of detecting some errors one or more reductions late.
- When no deterministic table exists, GLL parses every context-free grammar in $O(n^3)$ time for a fixed grammar, and parser combinators trade tables for ordinary functions.

| Construction | Time | Space | Accepts |
|---|---|---|---|
| Nullable, FIRST, FOLLOW | $O(\lvert G\rvert \cdot \lvert\Sigma\rvert)$ | $O(\lvert V\rvert \cdot \lvert\Sigma\rvert)$ | every grammar |
| LL(1) table | $O(\lvert G\rvert \cdot \lvert\Sigma\rvert)$ | $\lvert V\rvert(\lvert\Sigma\rvert + 1)$ cells | LL(1) grammars |
| Canonical LR(1) table | $O(N g^3 \sigma^2)$ build | $O(N(g + \sigma))$ | LR(1) grammars |
| LALR lookaheads (DeRemer-Pennello) | $O(X g \sigma)$ | $O(X g)$ relations | LALR(1) grammars |
| Yacc | $O(Q g^3 \sigma^2)$ build, $O(n)$ parse | $O(Q g)$ table | LALR(1) with precedence |
| Parsing table lookup | $O(1)$ | $\Theta(N \sigma)$ | any deterministic table |
| GLL parsing | $O(g^3 n^2 + g^2 n^3)$ | $O(g^2 n^2)$ | every context-free grammar |

: Costs of the main constructions. $N$ is the number of table rows or LR(1) states, $Q$ the number of LR(0) states, $X$ the number of nonterminal transitions of the LR(0) automaton, $g$ the grammar size, $\sigma$ the number of terminals and $n$ the input length.

## Choosing a method

For a new language with a grammar that changes, start with an LALR(1) generator such as yacc or Bison, or with an LL(1) or LL(*) tool if you want the generated code to look like recursive descent. Read every conflict report; a conflict settled by the default shift changes the language silently. Use precedence declarations for operators and nothing else. If the grammar is LR(1) but not LALR(1), a minimal LR(1) method such as IELR(1) gives an LALR-sized table that accepts it.

Keep the canonical LR(1) collection for small grammars or for teaching; on real grammars it has many times more states than LALR(1). For an ambiguous grammar, or one that is assembled from parts at run time, use GLL, GLR or memoized parser combinators, and expect to pick a tree from a forest. For an editor, choose a method with an incremental mode, since the work after an edit should follow the size of the change, not of the file.
