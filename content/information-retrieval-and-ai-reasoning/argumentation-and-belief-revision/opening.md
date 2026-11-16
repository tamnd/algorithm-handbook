Three people plan a trip. One says: "Take the train, it is the cheapest way." Call that argument $a$. A second says: "There is a rail strike today", which is argument $b$, and $b$ attacks $a$. A third says: "The strike was called off this morning", argument $c$, which attacks $b$. Nobody attacks $c$, so $c$ stands. Then $b$ falls, and $a$ is back. The accepted set is $\{a, c\}$, and no step of this used what the arguments say: only who attacks whom.

Now change the story. You believed that the train runs and that it is cheap. A message says the train does not run today. You must give something up, and the question is what. You should drop "the train runs", keep "the train is cheap", and not throw away beliefs that have nothing to do with trains. Logic alone does not say which beliefs to keep. You need a principle of minimal change.

These two stories are the two halves of this chapter. Argumentation decides which of several conflicting arguments to accept. Belief revision decides how to change a body of beliefs when new information contradicts it. Both are forms of [nonmonotonic reasoning](/nonmonotonic-reasoning/): adding information can remove conclusions. Both come with postulates that say what a good answer is, and with algorithms whose cost depends on which postulates you ask for.

## What the chapter covers

1. **Abstract frameworks and Dung's semantics.** A framework is a [directed graph](/directed-graph/) of attacks. [Admissible sets](/admissible-set/), [complete](/complete-extension/), [grounded](/grounded-extension/), [preferred](/preferred-extension/) and [stable](/stable-extension-argumentation/) extensions are the standard answers to "which arguments can be held together?"
2. **Computing extensions and their cost.** The grounded extension takes linear time. Labellings and semi-stable semantics refine the picture. The [acceptance problems](/argument-acceptance-problem/) for the other semantics are NP-complete or worse, and [SAT encodings](/argumentation-sat-encoding/) are how solvers attack them.
3. **Structured and value-based argumentation.** [Assumption-based argumentation](/assumption-based-argumentation/), [ASPIC+](/aspic-plus/) and [defeasible logic programming](/defeasible-logic-programming/) build arguments from rules. [Value-based frameworks](/value-based-argumentation/) let an audience rank the values that arguments promote.
4. **The AGM theory of belief change.** The [AGM postulates](/agm-postulates/), the [Levi identity](/levi-identity/), [partial meet contraction](/partial-meet-contraction/), [epistemic entrenchment](/epistemic-entrenchment/) and the [representation theorem](/agm-representation-theorem/) that ties them together.
5. **Revision on possible worlds.** [Grove's spheres](/grove-spheres/), the [Katsuno and Mendelzon](/katsuno-mendelzon-revision/) form of the postulates, [Dalal's operator](/dalal-revision/), and the [impossibility theorem of Gärdenfors](/gardenfors-impossibility-theorem/).
6. **Iterated revision, update and merging.** [Ordinal conditional functions](/ordinal-conditional-functions/), the [Darwiche and Pearl postulates](/darwiche-pearl-postulates/), [belief update](/belief-update/), the [possible models approach](/possible-models-approach/) and [belief merging](/belief-merging/).

## A first reading

For a short path through the chapter, read these in order.

- [Abstract argumentation framework](/abstract-argumentation-framework/): arguments, attacks, conflict-free sets and defence.
- [Admissible set](/admissible-set/) and [complete extension](/complete-extension/): the two conditions that every other semantics builds on.
- [Grounded extension](/grounded-extension/): the least fixed point of the characteristic function, unique and computable in polynomial time.
- [Preferred extension](/preferred-extension/) and [stable extension](/stable-extension-argumentation/): the maximal positions, and the ones that attack everything outside.
- [Grounded extension algorithm](/grounded-extension-algorithm/): the linear-time counting method.
- [Argument acceptance problem](/argument-acceptance-problem/): credulous and sceptical questions and their complexity.
- [Belief revision](/belief-revision/) and [AGM postulates](/agm-postulates/): expansion, contraction, revision and the rules they obey.
- [Grove spheres](/grove-spheres/) and [Katsuno-Mendelzon revision](/katsuno-mendelzon-revision/): revision as choosing the most plausible worlds.
- [Dalal revision](/dalal-revision/): a concrete operator with a known cost.
- [Darwiche-Pearl postulates](/darwiche-pearl-postulates/): what changes when you revise twice.

## Before you start

The argumentation half uses [directed graphs](/directed-graph/) from Volume 7 and the least fixed point of a monotone function, as in the [Knaster and Tarski theorem](/knaster-tarski-theorem/) of Volume 16. The complexity results lean on [SAT](/sat/), [Horn satisfiability](/horn-sat/) and [quantified Boolean formulas](/qbf/), all in Volume 16. The classes NP, coNP and the second level of the polynomial hierarchy appear by name; the chapter's own entry on the [complexity of preferred semantics](/preferred-semantics-complexity/) shows where the second level comes from.

The link to logic programming matters too. Stable extensions match [stable models](/stable-model-semantics/), the grounded extension matches the [well-founded semantics](/well-founded-semantics/), and default rules behave as in [default logic](/default-logic/). These are in chapter 35.6.

The belief revision half needs propositional logic: formulas, models, entailment and the consequence operator $\mathrm{Cn}$. Over $n$ atoms there are $2^n$ worlds, and most examples work directly on sets of worlds. Dalal's operator and merging measure change by the [Hamming distance](/hamming-distance/) of Volume 24. The ranking views connect to [System Z](/system-z/) and [rational closure](/rational-closure/) in chapter 35.6, which rank worlds in the same way to answer default queries.
