## What to remember

- A rewrite step matches the left side of a rule at some position, by a substitution, and replaces that subterm by the same instance of the right side. Everything else in the chapter is about the relation these steps generate.
- Termination and confluence together give each term exactly one normal form, so a convergent system decides its equational theory by normalizing both sides and comparing.
- Newman's lemma: a terminating system is confluent if it is locally confluent. The critical pair lemma: local confluence holds if every critical pair is joinable. So confluence of a finite terminating system is decidable.
- Without termination, the critical pairs do not settle confluence. Orthogonal systems, left-linear with no critical pairs, are confluent anyway; the lambda calculus and combinatory logic are the main examples.
- Strategies matter: innermost reduction can loop on a term that has a normal form, and outermost reduction can repeat work that sharing in a graph avoids.
- Termination is undecidable, so it is proved by a reduction ordering, an interpretation, or a decomposition such as dependency pairs. No reduction ordering orients commutativity, which is why such equations are built into matching.
- Knuth-Bendix completion turns equations into a convergent system when it succeeds; it can also fail on an equation it cannot orient, or run forever.
- String rewriting can simulate Turing machines, so the word problem, termination and confluence are undecidable for finite rewrite systems in general.

| Task | Method | Time |
|---|---|---|
| Match one pattern | Term matching | $\Theta(m + n)$ |
| Normalize, call by value | Innermost reduction | $O((n + k m) r m)$ |
| Normalize, call by name | Outermost reduction | $O((k + 1) N r m)$ |
| Find all occurrences of a pattern | Tree pattern matching | $O(n m^{1/2} \operatorname{polylog} m)$ |
| Match a fixed pattern set | Hoffmann-O'Donnell | $\Theta(n + P)$ best, $O(q S^r r P + n^2 F)$ worst |
| Retrieve candidate rules | Discrimination tree | $O(n + P + k n)$ |
| Retrieve from a term index | Substitution tree | $O(S n)$ |
| Make equations convergent | Knuth-Bendix completion | $O(k N r^3 m^3)$ |
| Solve an equation to depth $D$ | Narrowing | $O((r M)^{D+1} M^2)$ |
| Check size-change termination | Size-change graphs | $O(k F^2 3^{p^2} p^4)$ |

: Costs of the main algorithms of the chapter. In most rows $n$ is the size of the subject term, $m$ the size of a pattern or rule side, $r$ the number of rules and $k$ the number of steps, iterations or candidates; the other letters are defined on each entry.

## Using rewriting in practice

To decide an equational theory, first try completion with an LPO or KBO whose precedence follows the intended direction of the rules. If an equation like commutativity cannot be oriented, switch to rewriting modulo that theory or to unfailing completion. If completion keeps adding rules of the same shape, the theory may need a richer signature or another ordering.

For termination proofs, try a path ordering first, since it is fast and often enough for programs that recurse on smaller arguments. Use polynomial or matrix interpretations when a rule duplicates or rearranges arguments, and dependency pairs for anything larger; termination tools combine all three automatically.

For evaluation, use innermost reduction with sharing when the system is terminating, and an outermost or needed strategy when some subterms may not have a normal form. With many rules, index the left sides in a discrimination tree, or compile them into a matching automaton when the rule set is fixed.
