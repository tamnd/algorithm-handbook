## What to remember

- Correctness is relative to a [specification](/specification/): a [precondition](/precondition/) $P$ on the input and a [postcondition](/postcondition/) $Q$ that relates the output to the input. A program is correct if every run that starts in $P$ stops in $Q$. A program that never stops is [partially correct](/partial-correctness/) for every specification; [total correctness](/total-correctness/) adds termination.
- [Induction](/induction/) proves $P(n)$ for all $n$ from $P(0)$ and $P(n) \Rightarrow P(n+1)$. Strong induction may use all of $P(0), \ldots, P(n)$; [structural induction](/structural-induction/) runs over the constructors of lists and trees; induction over any [well-founded relation](/well-founded-relation/) works the same way.
- A [loop invariant](/loop-invariant/) needs three checks: it holds before the first test (initialization), each pass keeps it (maintenance), and it with the negated loop condition implies the postcondition (termination). An invariant that is too weak fails the third check; one that is too strong fails the first or the second.
- A loop stops if a [variant function](/variant-function/) takes values in a well-founded set, such as $\mathbb N$, and decreases in every pass. Lexicographic pairs handle loops where one counter may grow while another falls.
- A data structure is correct if its constructors establish the [representation invariant](/representation-invariant/), each operation preserves it, and each operation acts on the [abstract value](/abstraction-function/) as the specification says.
- The Hoare triple $\{P\}\,S\,\{Q\}$ is valid when $P \Rightarrow \mathrm{wp}(S, Q)$. For an assignment, $\mathrm{wp}(x \leftarrow E, Q) = Q[E/x]$, so proofs of straight-line code are computed backwards from the postcondition.
- Testing finds errors and does not prove their absence. Its strength grows with the property tested: compare with a second implementation, check a stated property on random inputs, or check a [certificate](/certifying-algorithms/) that proves the answer correct for this input.

## Tools and what each one asks you to prove

| Tool | What you prove | Typical use |
|---|---|---|
| [Induction](/induction/) | $P(0)$, and $P(n) \Rightarrow P(n+1)$ | formulas, recurrences |
| [Structural induction](/structural-induction/) | the claim for each constructor, given it for the parts | trees, lists, expressions |
| [Loop invariant](/loop-invariant/) | initialization, maintenance, termination | every iterative algorithm |
| [Variant function](/variant-function/) | bounded below and decreasing in each pass | termination |
| [Representation invariant](/representation-invariant/) | established by constructors, kept by every operation | heaps, search trees |
| [Proof by contradiction](/proof-by-contradiction/) | the negation leads to a false statement | optimality, lower bounds |
| [Cut-and-paste argument](/cut-and-paste-argument/) | replacing a part of an optimal solution cannot help | dynamic programming, greedy |
| [Weakest precondition](/weakest-precondition/) | $P \Rightarrow \mathrm{wp}(S, Q)$ | straight-line code, derivations |
| [Certifying algorithm](/certifying-algorithms/) | the checker accepts only correct answers | graph algorithms, libraries |

: The proof tools of the chapter. The first four prove a program correct once; the certificate in the last row proves each single answer correct when the program runs.

## Writing correctness proofs

- Write the invariant before the loop. Most loops are written to keep a property true, and naming it first makes the code shorter and the proof almost automatic.
- State the invariant with the exact index ranges, such as "$A[0 \ldots i-1]$ is sorted", and check the empty range at initialization.
- Prove termination separately. A loop with a correct invariant can still run forever, and a bound on the variant also bounds the number of passes.
- Check the boundary cases that the invariant allows: an empty array, a single item, equal keys, the largest integer.
- When a full proof is too costly, put the invariant into the code as an [assertion](/assertion/) and test it on many generated inputs.
