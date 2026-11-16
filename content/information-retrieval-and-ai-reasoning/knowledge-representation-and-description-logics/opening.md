A clinic keeps two kinds of knowledge about families. The first kind is general: a parent is a person with a child who is a person, and a mother is a female parent. The second kind is about named people: Ann is a female person, Bob is a person, and Bob is a child of Ann. In a [description logic](/description-logic/) the general part is a TBox,

$$\mathit{Parent} \equiv \mathit{Person} \sqcap \exists \mathit{hasChild}.\mathit{Person}, \qquad \mathit{Mother} \equiv \mathit{Parent} \sqcap \mathit{Female},$$

and the facts form an ABox. Nobody wrote down that Ann is a mother, yet a reasoner derives it: Bob is a person and a child of Ann, so Ann is a parent, and she is female. A second question is less obvious. The data says nothing about the children of a third person, Carl. A database answers that Carl is not a parent. A description logic answers that it does not know, because a fact that is missing from the data may still be true. This is the [open-world assumption](/open-world-assumption/), and much of the chapter follows from it. An answer is what holds in every model of the knowledge base, so a reasoner must rule out all the ways the world could be. It cannot simply look up one table.

The chapter is about such reasoners and the price of their answers. The price depends on which constructors the language allows. [ALC](/alc-description-logic/) has negation, disjunction and both kinds of role restriction. In ALC, deciding whether a concept can have an instance is PSPACE-complete without a TBox and EXPTIME-complete with general TBoxes. [EL](/el-description-logic/) drops negation, disjunction and the universal restriction, and then the hierarchy of a large medical ontology is computed in polynomial time. [DL-Lite](/dl-lite/) restricts the language further, so that a query over an ontology becomes an ordinary database query over the data. The same trade-off returns in the last group, where a propositional knowledge base is compiled once into a form that answers later queries fast. Between the two sits the problem of change: how to say what holds after an action without listing everything that the action leaves alone.

## What the chapter covers

1. **Knowledge as structures.** [Semantic networks](/semantic-network/) and [frames](/frame-knowledge-representation/) are the early graph and record forms of knowledge, with inheritance along is-a links. Description logics give them a formal meaning, and an [ontology](/ontology-knowledge-representation/) is a shared vocabulary written in one.
2. **ALC and knowledge bases.** ALC is the basic logic. A knowledge base splits into a [TBox and an ABox](/tbox-and-abox/), read under the open-world assumption and usually without the [unique name assumption](/unique-name-assumption/).
3. **Reasoning problems.** [Concept satisfiability](/concept-satisfiability/), [subsumption](/concept-subsumption/), [instance checking](/instance-checking/) and [classification](/ontology-classification/) reduce to one another, and satisfiability is the problem the algorithms decide.
4. **Tableaux and the cost of ALC.** The [tableau algorithm](/alc-tableau-algorithm/) builds a model or finds a clash, and [blocking](/tableau-blocking/) makes it stop when the TBox has cycles. The [PSPACE theorem](/alc-pspace-completeness/) and the [EXPTIME theorem](/alc-general-tbox-exptime/) give the cost, and [Schild's correspondence](/alc-modal-k-correspondence/) carries results over from modal logic. The [hypertableau calculus](/hypertableau/) and [SROIQ](/sroiq/), the logic of OWL 2 DL, show where practical reasoners go.
5. **Logics with cheap reasoning.** [Structural subsumption](/structural-subsumption/) handles small languages, EL has [classification by completion rules](/el-classification/), and DL-Lite has [ontology-mediated query answering](/ontology-mediated-query-answering/) by [PerfectRef rewriting](/perfectref-rewriting/).
6. **Actions and change.** The [situation calculus](/situation-calculus/) uses [successor state axioms](/successor-state-axioms/) and [regression](/situation-calculus-regression/), and the [event calculus](/event-calculus/) works on a time line.
7. **Knowledge compilation.** [Knowledge compilation](/knowledge-compilation/) moves the hard work offline. [d-DNNF](/d-dnnf/) and [sentential decision diagrams](/sentential-decision-diagram/) are target languages, and the [knowledge compilation map](/knowledge-compilation-map/) compares them.

## A first reading

Read these first, in this order:

1. [Description logic](/description-logic/)
2. [ALC](/alc-description-logic/)
3. [TBox and ABox](/tbox-and-abox/)
4. [Open-world assumption](/open-world-assumption/)
5. [Concept satisfiability](/concept-satisfiability/)
6. [Concept subsumption](/concept-subsumption/)
7. [Tableau algorithm for ALC](/alc-tableau-algorithm/)
8. [Blocking](/tableau-blocking/)
9. [EL description logic](/el-description-logic/)
10. [EL classification by completion rules](/el-classification/)
11. [DL-Lite](/dl-lite/)
12. [Situation calculus](/situation-calculus/)
13. [Successor state axioms](/successor-state-axioms/)
14. [Knowledge compilation](/knowledge-compilation/)
15. [d-DNNF](/d-dnnf/)

That path gives one expressive logic with its decision procedure, one tractable logic, one way to describe change and one way to move reasoning offline. Skip at first the two complexity theorems, the hypertableau calculus, SROIQ, PerfectRef and the compilation map. Come back to them when you need to know why a reasoner is slow on a particular ontology, or which compiled form to choose.

## Before you start

Strict inheritance in a semantic network is [graph reachability](/graph-reachability/) in a [graph](/graph/), as in Volume 7. ALC is a notation for the multimodal logic K, so the [Kripke structures](/kripke-structure/) of Volume 16 are its models, and [bisimulation](/bisimulation/) from the same chapter shows what ALC cannot say. The hardness proofs use [QBF](/qbf/) from Volume 16 and the [alternating Turing machine](/alternating-turing-machine/) of Volume 1; the classes PSPACE, EXPTIME and coNP are used by name only. The tableau searches with [chronological backtracking](/chronological-backtracking/) from Volume 2. EL completion computes a least fixed point with Horn rules, close to a [Datalog](/datalog/) program of Volume 26. Situations and events build on the [closed-world assumption](/closed-world-assumption/), the [frame problem](/frame-problem/) and [classical planning](/classical-planning/) of Volume 29, and the event calculus uses [circumscription](/circumscription/) from Chapter 35.6. Knowledge compilation starts from [SAT](/sat/), [CNF](/conjunctive-normal-form/), [DPLL](/dpll/) and [ordered BDDs](/ordered-binary-decision-diagram/) in Volume 16. You should be comfortable with first-order formulas, their models, and proofs by induction on formulas.
