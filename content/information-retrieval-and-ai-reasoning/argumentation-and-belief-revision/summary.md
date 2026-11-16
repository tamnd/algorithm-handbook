## What to remember

- An [abstract argumentation framework](/abstract-argumentation-framework/) is a directed graph of attacks. A set is admissible when it is conflict-free and defends its members. Stable extensions are semi-stable, semi-stable ones are preferred, preferred ones are complete, and complete ones are admissible.
- The [grounded extension](/grounded-extension/) is the least fixed point of the characteristic function and the least complete extension. It is unique, and the [counting algorithm](/grounded-extension-algorithm/) finds it in $\Theta(n + m)$ time.
- Preferred extensions always exist; stable extensions may not. Credulous acceptance under preferred semantics is NP-complete, and sceptical acceptance is $\Pi_2^P$-complete, one level above, as shown in the [complexity of preferred semantics](/preferred-semantics-complexity/). In a finite framework without odd cycles, preferred and stable extensions coincide.
- Structured formalisms such as [ABA](/assumption-based-argumentation/) and [ASPIC+](/aspic-plus/) build a framework from rules and then use Dung's semantics.
- The [AGM postulates](/agm-postulates/) constrain revision and contraction, and the [Levi identity](/levi-identity/) and Harper identity turn one into the other. By the [representation theorem](/agm-representation-theorem/), the contractions that satisfy K÷1 to K÷6 are exactly the partial meet contractions, those that satisfy all eight are the transitively relational ones, and the matching revisions come from them by the Levi identity.
- On a finite language an AGM revision chooses the least models of the new formula in a total preorder on worlds that has the old beliefs at the bottom ([Grove](/grove-spheres/), [Katsuno and Mendelzon](/katsuno-mendelzon-revision/)). [Dalal's operator](/dalal-revision/) uses Hamming distance for the preorder.
- [Gärdenfors](/gardenfors-impossibility-theorem/): no non-trivial revision system satisfies both preservation and the Ramsey test.
- The AGM postulates say little about a second revision. Iterated revision revises an epistemic state, such as a ranking of worlds, and the [Darwiche and Pearl postulates](/darwiche-pearl-postulates/) C1 to C4 say how its order may change.
- Update moves each possible world on its own, and [merging](/belief-merging/) combines several bases, by majority with the sum or by arbitration with Gmax.

| Problem | Method | Cost | What is guaranteed |
|---|---|---|---|
| Grounded extension | [counting algorithm](/grounded-extension-algorithm/) | $\Theta(n + m)$ | unique; the least complete extension |
| Credulous acceptance, preferred | admissible [SAT encoding](/argumentation-sat-encoding/), one call | NP-complete | a witness admissible set |
| Sceptical acceptance, preferred | loop of SAT calls, or a [QBF](/qbf/) | $\Pi_2^P$-complete | a counter-extension when the answer is no |
| Stable extensions | stable encoding and blocking clauses | credulous NP-complete, sceptical coNP-complete | may be none |
| Semi-stable extensions | maximize the range in a loop | credulous $\Sigma_2^P$-complete, sceptical $\Pi_2^P$-complete | exist in every finite framework |
| [Dalal revision](/dalal-revision/) | multi-source BFS on the cube | $\Theta(n \cdot 2^n)$ on model sets; entailment $\mathrm{P}^{\mathrm{NP}[O(\log n)]}$-complete | R1 to R6 |
| [PMA update](/possible-models-approach/) | inclusion-minimal change per model | $\Theta(k \cdot n \cdot 2^n)$ on model sets; entailment $\Pi_2^P$-complete | U1 to U8 |
| [Sum merging](/belief-merging/) | Hamming distances added over the bases | $O(m' \cdot n \cdot 2^n)$ on model sets | IC0 to IC8 and Maj |
| [Darwiche-Pearl revision](/darwiche-pearl-postulates/) | shift the ranks of the $\mu$-worlds down and the others up by one | one pass over the ranks | R*1 to R*6 and C1 to C4 |

: Main methods of the chapter. $n$, $m$: arguments and attacks in the argumentation rows, $n$: atoms in the belief rows; $k$: models of the old beliefs; $m'$: bases in the profile.

## Choosing a method

If one cautious answer is enough, compute the grounded extension. It is unique, it is in every complete extension, and the counting algorithm is linear.

If you need every reasonable position, use preferred semantics, or stable semantics when the framework is known to have stable extensions, for example when it has no odd cycles. Credulous preferred acceptance is one SAT call on the admissible encoding. Sceptical preferred acceptance needs a loop of calls or a QBF solver, and on large frameworks this is where the time goes. Semi-stable semantics answers where stable semantics has no extension, at a second-level cost.

If the arguments come from rules, ABA suits logic programs and default reasoning, ASPIC+ suits strict and defeasible rules with preferences, and DeLP answers one query at a time with a dialectical tree. If the disagreement is about values, a value-based framework makes the audience explicit.

For belief change, first decide what the news is. If it corrects beliefs about a static world, revise with an AGM operator given by a preorder on worlds; Dalal's operator fits when every atom counts the same. If it reports a change in the world, update with the PMA or Forbus's operator. If it is one of several equal sources, merge. If revisions come in sequence, keep a ranking and revise it with an operator that satisfies C1 to C4.
