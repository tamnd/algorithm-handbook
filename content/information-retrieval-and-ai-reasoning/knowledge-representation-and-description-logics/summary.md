## What to remember

- **Open world, every model.** A [description logic](/description-logic/) knowledge base is read under the [open-world assumption](/open-world-assumption/): a statement holds if it holds in every model, it is false if it fails in every model, and otherwise it is unknown. Without the [unique name assumption](/unique-name-assumption/), two names may denote one object. This matters once number restrictions or nominals are present.
- **One problem underneath.** With negation, [subsumption](/concept-subsumption/) $C \sqsubseteq D$ is unsatisfiability of $C \sqcap \neg D$, and [instance checking](/instance-checking/) and [classification](/ontology-classification/) reduce to satisfiability too. In EL there is no negation, and subsumption is decided directly.
- **The cost of ALC.** Satisfiability in [ALC](/alc-description-logic/) is PSPACE-complete without a TBox and [EXPTIME-complete with general TBoxes](/alc-general-tbox-exptime/). With a TBox, the [tableau](/alc-tableau-algorithm/) is sound, complete and terminating only with [blocking](/tableau-blocking/). Subset blocking suffices for ALC; inverse roles need equality or pairwise blocking. SROIQ, the logic of OWL 2 DL, is N2EXPTIME-complete.
- **Small languages are fast.** [EL](/el-description-logic/) subsumption with general TBoxes is polynomial, and [completion rules](/el-classification/) classify a whole TBox in $O(n^3)$ time. [DL-Lite](/dl-lite/) query answering is first-order rewritable, so its data complexity is in AC0. Adding $\forall$ or inverse roles to EL makes subsumption EXPTIME-complete again.
- **Measured, not proved.** Practical reasoners such as the [hypertableau](/hypertableau/) calculus are fast on real ontologies, but no theorem says so: their worst-case bounds are above the complexity of the problem, and their speed is a measurement on benchmarks.
- **Change without listing non-effects.** The [frame problem](/frame-problem/) of Volume 29 is solved in the [situation calculus](/situation-calculus/) by [successor state axioms](/successor-state-axioms/), one per fluent. [STRIPS](/strips/) is the special case with a complete initial state under the [closed-world assumption](/closed-world-assumption/) and unconditional effects. [Regression](/situation-calculus-regression/) is the logical form of the [goal regression](/goal-regression/) of [classical planning](/classical-planning/). The [event calculus](/event-calculus/) solves the same problem on a time line by minimizing events and effects with circumscription.
- **Compile once, query often.** [Knowledge compilation](/knowledge-compilation/) moves the hard work offline. Queries are then polynomial in the size of the compiled form, but that size can be exponential in the input. On a smooth [d-DNNF](/d-dnnf/), model counting is one linear pass.

| Method | Problem | Cost | What is guaranteed |
|---|---|---|---|
| ALC tableau, no TBox | concept satisfiability | $2^{O(n^2)}$ time; polynomial space depth-first | decides a PSPACE-complete problem |
| ALC tableau with blocking | satisfiability with a general TBox | $2^{2^{O(n)}}$ time, $2^{O(n)}$ space; $2^{O(n)}$ time with global caching | sound, complete, terminating |
| [Structural subsumption](/structural-subsumption/) | subsumption in FL$^-$ | $O(n \log n)$ | complete only for small languages |
| EL completion rules | classification of an EL TBox | $O(n^3)$ time, $O(n^2)$ space | all subsumptions between names |
| [PerfectRef](/perfectref-rewriting/) | conjunctive queries over DL-Lite | rewriting exponential in the query; AC0 in the data | certain answers on a consistent knowledge base |
| Regression | projection after $n$ actions | $O(nq + n^2 m)$ expected, shared DAG of size $O(q + nm)$ | equivalent query about $S_0$ |
| d-DNNF compiler and count | model counting | compilation exponential in the worst case; count $O(s)$ after smoothing in $O(sn)$ | exact count |
| [SDD](/sentential-decision-diagram/) apply | conjunction, disjunction | $O(st)$ without compression | canonical form for a fixed vtree when compressed |

: Main methods of the chapter. $n$: size of the concept and TBox, of the TBox, or number of actions, as the row says; $q$: query nodes; $m$: size of the successor state formulas of one action; $s$, $t$: circuit or SDD sizes.

## Choosing a method

Pick the smallest language that says what you need. If the ontology needs only conjunction and existential restrictions, as many medical ontologies do, use EL and completion rules. If the data is large and lives in a database, and the ontology is a hierarchy with domains and ranges, use DL-Lite and rewrite queries with PerfectRef. Use a tableau or hypertableau reasoner only when you need negation, disjunction, universal restrictions or the full constructor set of SROIQ, and expect its speed to depend on the ontology.

For actions, use the situation calculus with successor state axioms when plans are sequences of actions, and regression when the query is about the end of a known sequence. Use the event calculus when events have times, or when several events and observations are spread over a narrative.

For a fixed propositional knowledge base that receives many queries, compile it. Choose the target from the [compilation map](/knowledge-compilation-map/): d-DNNF for counting and probabilities, an OBDD or SDD when the knowledge base grows by conjunction or when equivalence must be tested. Measure the compiled size on real inputs first.
