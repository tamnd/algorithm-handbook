## What to remember

- [Type soundness](/type-soundness/) is progress plus preservation: a closed well-typed term is a value or takes a step, and a step keeps its type. It is proved for one stated calculus. A sound checker that always halts rejects some safe programs, such as `if true then 0 else false`.
- In the [simply typed lambda calculus](/simply-typed-lambda-calculus/), each typable term has one type, checking with annotations takes $O(n)$ time with shared types, and every reduction ends. Its types are the formulas of intuitionistic implicational logic ([Curry-Howard](/curry-howard-correspondence/)), and deciding whether a type has a closed term is PSPACE-complete.
- In the [Hindley-Milner type system](/hindley-milner-type-system/), every typable term has a principal type scheme, and [algorithm W](/algorithm-w/) finds it (Damas and Milner 1982). [Typability is DEXPTIME-complete](/ml-typability-dexptime-completeness/) (1990). Types can reach $2^{2^{\Omega(n)}}$ nodes as trees and $2^{\Omega(n)}$ as DAGs, but without `let` inference takes $O(n\,\alpha(n))$ time with union-find. Real programs nest `let` shallowly, and inference on them is fast.
- Inference becomes undecidable with [polymorphic recursion](/polymorphic-recursion-undecidability/), which is equivalent to semi-unification, and for [System F](/system-f/) without annotations ([Wells 1994](/system-f-inference-undecidability/)). Rank-2 System F is decidable, rank 3 and above is not. [Bidirectional checking](/bidirectional-type-checking/) needs annotations only where a synthesized type meets an expected one.
- The [value restriction](/value-restriction/) generalizes a `let` only when its right side is a syntactic value; without it, `ref` cells make a program go wrong. OCaml also generalizes variables that occur only covariantly.
- [Type classes](/type-classes/) compile either by [dictionary passing](/dictionary-passing-translation/), one record argument per constraint, or by [monomorphization](/monomorphization/), one copy per instance. Monomorphization ends when there is no polymorphic recursion, but $k$ doubling levels can need $2^{k+1} - 1$ copies.
- [Subtyping](/subtyping/) is contravariant in function arguments, covariant in results, and invariant for mutable cells. [Row unification](/row-polymorphism/) keeps principal types for extensible records. Subtyping of [recursive types](/recursive-types/) takes $O(n^2)$ time. [Gradual typing](/gradual-typing/) replaces equality by a consistency relation that is not transitive and blames a cast when a value fails it.
- Checking [refinement types](/refinement-types/) is decidable exactly when validity in the predicate logic is decidable. [Liquid types](/liquid-types/) finds the strongest conjunction of given qualifiers after finitely many solver queries. [Dependent types](/dependent-types/) need normalization to decide definitional equality.
- [Linear types](/linear-types/) force exactly one use by dropping weakening and contraction, affine types drop only contraction, and [borrow checking](/borrow-checking/) adds lifetimes computed from liveness. It rejects some safe programs.

| Method | Problem | Time | Guarantee |
|---|---|---|---|
| Church-style STLC checking | checking | $O(n)$ with shared types | exact |
| Algorithm W | ML inference | $2^{2^{O(n)}}$ worst, $\Theta(n)$ best | principal type |
| Algorithm J | ML inference | $2^{O(n)}$ worst, $O(n\,\alpha(n))$ without `let` | principal type |
| Constraint generation and solving | ML and extensions | $O(n)$ generation, $2^{O(n)}$ solving | principal type for ML |
| Bidirectional checking | annotated terms | $O(n)$ with shared types | sound; complete for normal forms |
| Monomorphization | compiling polymorphism | one copy per instance | ends without polymorphic recursion |
| Dictionary passing | compiling type classes | one argument per constraint | coherent without overlap or ambiguity |
| Refinement checking | annotated terms | one solver query per subtyping step | decidable iff the logic is |
| Liquid SOLVE | refinement inference | at most $\lvert C\rvert (1 + \sum \lvert Q^\star\rvert) \max \lvert Q^\star\rvert$ queries | strongest liquid type |
| Borrow checking (RFC 2094) | reference safety | lifetimes $\times$ points additions, plus dataflow | conservative |

: Main methods. $n$ is the number of nodes of the term, $C$ the set of liquid constraints and $Q^\star$ the qualifier instances at one unknown refinement.

## Choosing a method

For a language with ML-style polymorphism and no annotations, use Hindley-Milner inference. Write it as algorithm J with levels for speed, or as constraint generation and solving to add type classes, rows or units of measure, or to report errors well. Keep the value restriction, in its relaxed form if the language has covariant data. Ask for signatures where the program needs polymorphic recursion or higher-rank types, and check those parts bidirectionally.

To compile polymorphism, monomorphize when speed of the output matters and the program has no polymorphic recursion, and pass dictionaries when code size or separate compilation matters. To mix typed and untyped code with run-time guarantees, use gradual typing with casts; erasing the types gives optional typing with no guarantee.

When ordinary types are too weak, add only what states the property. Effects bound what code may do, linear or affine types and borrowing control aliasing, refinement types with an SMT solver check bounds and nonzero divisors, and liquid types infers the refinements of loops and helpers. Dependent types state full specifications, at the cost of proofs that the programmer writes.
