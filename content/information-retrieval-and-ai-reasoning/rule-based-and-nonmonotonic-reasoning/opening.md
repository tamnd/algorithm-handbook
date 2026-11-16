Write down two rules and one fact:

```
flies(X) :- bird(X), not abnormal(X).
abnormal(X) :- penguin(X).
bird(tweety).
```

Nothing says that Tweety is a penguin, so `abnormal(tweety)` cannot be derived, and `flies(tweety)` follows. Now add the fact `penguin(tweety)`. Then `abnormal(tweety)` holds, the first rule is blocked, and `flies(tweety)` is gone. One more premise took a conclusion away. Classical logic never does this: whatever follows from a set of formulas also follows from any larger set. Reasoning that can withdraw conclusions is [nonmonotonic](/nonmonotonic-reasoning/), and it is how people use rules of thumb, closed lists and defaults.

The chapter has two roots. The first is the rule-based expert system of the 1970s and 1980s: a [production system](/production-system/) with a working memory of facts and a few hundred or thousand if-then rules, run by forward or backward chaining. Its algorithms are about speed, matching many rules against many facts after every change. The second root is logic. From 1980 on, circumscription, default logic and autoepistemic logic tried to give rules with exceptions a precise meaning, and logic programming gave one through [negation as failure](/negation-as-failure/). The two roots met in [stable models](/stable-model-semantics/) and in [answer set programming](/answer-set-programming/), where a program with negation describes a search problem and a solver finds its solutions.

The costs are known exactly. Deduction from propositional Horn rules takes linear time. With negation, a program can have no stable model, one, or many, and deciding whether one exists is NP-complete. Default logic, autoepistemic logic and disjunctive programs sit one level higher, at $\Sigma_2^p$. Between these sits the [well-founded model](/well-founded-semantics/), which every normal program has, which takes polynomial time to compute, and which may leave some atoms undefined.

## What the chapter covers

1. **Production systems.** The recognize-act cycle, [forward](/forward-chaining/) and [backward chaining](/backward-chaining/), [conflict resolution](/conflict-resolution-strategy/), the incremental matchers [Rete](/rete-algorithm/) and [TREAT](/treat-algorithm/), and the [certainty factors](/certainty-factors/) of MYCIN.
2. **Negation as failure and stable models.** The [completion](/clark-completion/), the [reduct](/gelfond-lifschitz-reduct/), stable models and [stratified programs](/stratified-logic-program/).
3. **The well-founded model.** Its definition, the [alternating fixpoint](/alternating-fixpoint/) that computes it, and [SLG resolution](/slg-resolution/), which answers queries with tables.
4. **Theorems about stable models.** [Fages' theorem](/fages-theorem/), [loop formulas](/loop-formulas/), the [splitting set theorem](/splitting-set-theorem/), [strong equivalence](/strong-equivalence/) and the [NP-completeness](/stable-model-np-completeness/) of existence.
5. **Answer set programming.** [Choice rules](/choice-rule/), [grounding](/answer-set-grounding/), the [smodels](/smodels-algorithm/) search, [conflict-driven solving](/conflict-driven-answer-set-solving/), and [disjunctive programs](/disjunctive-logic-program/) with their [$\Sigma_2^p$-completeness](/disjunctive-asp-sigma2-completeness/).
6. **Nonmonotonic logics.** [Circumscription](/circumscription/), the [Yale shooting problem](/yale-shooting-problem/), [default logic](/default-logic/) and its [extensions](/default-extension/), [autoepistemic logic](/autoepistemic-logic/), and the [complexity of default logic](/default-logic-complexity/).
7. **Conditionals and ranked worlds.** [System P](/system-p/), [rational closure](/rational-closure/) and [System Z](/system-z/).
8. **Abduction, diagnosis and truth maintenance.** [Abduction](/abductive-reasoning/) and [abductive logic programming](/abductive-logic-programming/), [consistency-based diagnosis](/consistency-based-diagnosis/) and [Reiter's hitting set tree](/reiter-hs-tree/), and the [justification-based](/justification-based-truth-maintenance/) and [assumption-based](/assumption-based-truth-maintenance/) truth maintenance systems.

## A first reading

Read these first, in this order:

1. [Nonmonotonic reasoning](/nonmonotonic-reasoning/)
2. [Forward chaining](/forward-chaining/)
3. [Negation as failure](/negation-as-failure/)
4. [Gelfond-Lifschitz reduct](/gelfond-lifschitz-reduct/)
5. [Stable model semantics](/stable-model-semantics/)
6. [Well-founded semantics](/well-founded-semantics/)
7. [Fages' theorem](/fages-theorem/)
8. [Answer set programming](/answer-set-programming/)
9. [Default logic](/default-logic/)
10. [Circumscription](/circumscription/)
11. [Consistency-based diagnosis](/consistency-based-diagnosis/)

That path goes from rules to the main semantics of negation, then to the programming method built on it, and ends with the two classic logics and one application. Skip at first the second-level complexity proofs, SLG resolution, autoepistemic logic, TREAT and the assumption-based truth maintenance system. Come back to the group on conditionals when you want a semantics for defaults that does not depend on how the rules are written.

## Before you start

The chapter leans on logic from Volume 16. Rules are [Horn clauses](/horn-clause/), and their propositional case is decided by the linear-time [forward chaining for Horn-SAT](/horn-sat-forward-chaining/). Prolog-style [logic programming](/logic-programming/) runs by [SLD resolution](/sld-resolution/) and, with negation, by [SLDNF resolution](/sldnf-resolution/). Least models are [fixed points](/fixed-point/) given by the [Knaster-Tarski theorem](/knaster-tarski-theorem/). Answer set solvers reuse [DPLL](/dpll/), [CDCL](/cdcl/) and [unit propagation](/unit-propagation/), and the hardness proofs reduce from [3-SAT](/3-sat/) and [QBF](/qbf/). From Volume 26 you need [Datalog](/datalog/) and [semi-naive evaluation](/semi-naive-evaluation/), which a grounder uses. Diagnosis computes the minimal [hitting sets](/hitting-set/) of Volume 18. Backward chaining is a [depth-first search](/depth-first-search/), and its failures are undone by [chronological backtracking](/chronological-backtracking/) of Volume 2. The [frame problem](/frame-problem/) of Volume 29 is the setting of the Yale shooting problem. The link between stable models and the [stable extensions](/stable-extension-argumentation/) of argumentation frameworks is in Chapter 35.7. You should be comfortable with propositional logic, truth tables and proofs by induction.
