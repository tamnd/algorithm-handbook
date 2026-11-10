## What to remember

- **Clauses keep satisfiability, not truth.** [Prenex form](/prenex-normal-form/) is equivalent to the formula, but [Skolemization](/skolemization/) replaces each $\exists y$ by a new function of the universal variables before it, and the result is only equisatisfiable. That is enough for a refutation: to prove $\varphi$ from $\Gamma$, refute the clauses of $\Gamma \wedge \neg \varphi$.
- **A most general unifier is unique up to renaming** and exists whenever any unifier does ([the unification theorem](/mgu-existence-theorem/)). Every other unifier is an instance of it, so a prover loses nothing by using only the most general one.
- **The occurs check is what makes unification sound.** A variable $x$ cannot be unified with a term that contains $x$, such as $f(x)$. Prolog leaves the check out for speed and can then derive false answers.
- **Representation decides the cost of unification.** [Robinson's algorithm](/robinson-unification/) is exponential on terms stored as trees, because the bound terms can double at each step. On a [term DAG](/term-dag/) with union-find, [Martelli-Montanari](/martelli-montanari-unification/) and [Huet](/huet-unification/) take $O(N\,\alpha(N))$ time, and [Paterson-Wegman](/paterson-wegman-unification/) takes $O(N)$.
- **Resolution plus factoring is refutation complete.** [Herbrand's theorem](/herbrand-theorem/) gives a finite unsatisfiable set of ground instances, and the [lifting lemma](/lifting-lemma/) turns each ground step into a first-order one. Binary resolution without factoring is not complete.
- **Restrictions trade completeness for speed.** Unit and input resolution refute the same sets and are complete only for [Horn clauses](/horn-clause/). Linear resolution, hyperresolution, ordered resolution and set of support (when the clauses outside the support are satisfiable) stay complete for all clause sets.
- **Prolog is SLD resolution with a fixed search.** [SLD resolution](/sld-resolution/) is complete for every selection rule, but Prolog's depth-first search over the clauses in program order can loop where a refutation exists.
- **Unification modulo theories and with binders loses the single answer.** Commutativity and AC are finitary, associativity is infinitary, and higher-order unification is undecidable, from third order (Huet and Lucchesi) and already at second order (Goldfarb). [Patterns](/pattern-unification-problem/) and [nominal terms](/nominal-unification-problem/) get back decidability and most general unifiers.

## Resolution strategies side by side

| Strategy | What each step must use | Refutation complete for |
|---|---|---|
| [Robinson resolution](/robinson-resolution/) | any two clauses, with factoring | all clause sets |
| [Unit resolution](/unit-resolution/) | a unit clause as one parent | Horn sets |
| [Input resolution](/input-resolution/) | an input clause as one parent | Horn sets (same sets as unit) |
| [Linear resolution](/linear-resolution/) | the last center as one parent | all clause sets |
| [Set of support](/set-of-support/) | a parent derived from the support $T$ | sets where $S \setminus T$ is satisfiable |
| [Hyperresolution](/hyperresolution/) | a nucleus and positive electrons, at once | all clause sets |
| [Ordered resolution](/ordered-resolution/) | the largest or selected literal | all clause sets |
| [SLD resolution](/sld-resolution/) | the goal and a program clause | definite programs and queries |

: The restrictions of resolution in this chapter, with the clauses each step must involve and the sets on which the restriction still finds a refutation whenever one exists.

## Choosing a method

- To unify a few small terms, as in a teaching prover or a type checker for a small language, use Robinson's algorithm with the occurs check. When terms share structure or grow deep, as in type inference, use union-find on a term DAG: Paterson-Wegman is linear, but Huet's almost-linear algorithm has smaller constants.
- For a general first-order prover, use ordered resolution with selection, and superposition when the problem has equality. Delete subsumed clauses and rewrite with [demodulation](/demodulation/) eagerly, and keep the clauses in a [term index](/term-indexing/).
- When the axioms are known to be consistent and only the goal is new, put the negated goal in the [set of support](/set-of-support/); the search then stays near the goal.
- For Horn clauses, use unit resolution or forward chaining by [hyperresolution](/hyperresolution/) to saturate, and [SLD resolution](/sld-resolution/) to answer queries. Write Prolog programs so that the base clauses come first and recursive calls come last.
- For terms with commutative or AC symbols, unify modulo the theory instead of adding its axioms. For terms with bound variables, stay inside [pattern unification](/miller-pattern-unification/) or [nominal unification](/urban-nominal-unification/) when you can, and fall back on [Huet's pre-unification](/huet-pre-unification/) only when you must.
