A file server gets a request: key $K_W$ wants to read the payroll file. Two different questions hide in it. The first is whether this request is allowed: does the requester hold the right, and who gave it? The second is what happens to the data afterwards. A program that may read the payroll file may also copy it into a public log, branch on a salary and print the result, or make a lock bit flicker in a pattern that another process can read. Access control answers the first question and information flow control answers the second. This chapter treats both, because the second grew out of the limits of the first.

The chapter is about models with exact statements. Some decide one access in constant time, some answer a safety question that is undecidable in general, and some bound in bits what an attacker can learn. Each entry says which of its claims are proved and which are measured. Keep the difference when you read.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **Principles and the access matrix.** The [principle of least privilege](/principle-of-least-privilege/), the [reference monitor](/reference-monitor/) that must see every access, and the [access control matrix](/access-control-matrix/) it checks. [Access control lists](/access-control-list/) and [capability lists](/capability-list/) store the same matrix by columns and by rows.
2. **Who sets the policy.** [Discretionary](/discretionary-access-control/) and [mandatory](/mandatory-access-control/) access control, [roles](/role-based-access-control/), [separation of duty](/separation-of-duty/), [role mining](/role-mining-problem/) and [attributes](/attribute-based-access-control/).
3. **Multilevel and commercial models.** The [Bell-LaPadula model](/bell-lapadula-model/) and its [basic security theorem](/basic-security-theorem/), the [Biba](/biba-integrity-model/) integrity model, the [Chinese Wall](/chinese-wall-model/) and [Clark-Wilson](/clark-wilson-model/) models.
4. **Safety of protection systems.** The [Harrison-Ruzzo-Ullman model](/harrison-ruzzo-ullman-model/), the [undecidability of its safety question](/hru-safety-undecidability/), and the [Take-Grant model](/take-grant-model/), where the same question takes linear time.
5. **Authorization across organizations.** [Relationship-based access control](/relationship-based-access-control/), [trust management](/trust-management/) and [authorization logic](/authorization-logic/).
6. **Enforcement by monitors.** The [security automaton](/security-automaton/), the theorem that [execution monitors enforce only safety properties](/em-enforceable-policies-theorem/), and the [inline reference monitor](/inline-reference-monitor/).
7. **Information flow and noninterference.** The [lattice model](/denning-lattice-model/), [implicit flows](/implicit-flow/), [noninterference](/noninterference/), [termination-insensitive noninterference](/termination-insensitive-noninterference/), [hyperproperties](/hyperproperty/) and the [security type system](/security-type-system/).
8. **Dynamic information flow control.** The [no-sensitive-upgrade](/no-sensitive-upgrade/) check, [secure multi-execution](/secure-multi-execution/) and [faceted execution](/faceted-execution/).
9. **Releasing and measuring information.** [Declassification](/declassification/), the [decentralized label model](/decentralized-label-model/), [quantitative information flow](/quantitative-information-flow/), [min-entropy leakage](/min-entropy-leakage/), the [min-capacity bound](/min-entropy-leakage-bound/) and [g-leakage](/g-leakage/).
10. **Confinement and covert channels.** [Covert channels](/covert-channel/), the [confinement problem](/confinement-problem/) and the [shared resource matrix](/shared-resource-matrix/) method.

Groups 1 to 5 are about access, groups 6 to 10 about flow. Group 6 sits between them: a monitor can enforce access rules of one run, and the theorem there explains why it cannot enforce noninterference.

## A first reading

For a first pass, read these twelve entries in order.

1. [Reference monitor](/reference-monitor/)
2. [Access control matrix](/access-control-matrix/)
3. [Capability list](/capability-list/)
4. [Role-based access control](/role-based-access-control/)
5. [Bell-LaPadula model](/bell-lapadula-model/)
6. [Basic security theorem](/basic-security-theorem/)
7. [HRU safety undecidability](/hru-safety-undecidability/)
8. [Security automaton](/security-automaton/)
9. [Implicit flow](/implicit-flow/)
10. [Noninterference](/noninterference/)
11. [Security type system](/security-type-system/)
12. [Min-entropy leakage](/min-entropy-leakage/)

This path gives the matrix, one way to fill it, one model with its theorem and its critique, the limit on deciding safety, the limit on monitors, and the core of information flow with one measure of leakage. On a first pass you can skip the commercial models of group 3, group 5, the dynamic monitors of group 8, and g-leakage. Come back to [covert channels](/covert-channel/) once you have read noninterference, because a proof of noninterference for a whole system rules out every covert channel inside its model, and the entries on channels say what is left outside.

## Before you start

The entries assume a few ideas from other volumes.

- Undecidability and reductions: the [Turing machine](/turing-machine/) (Volume 1), the [halting problem](/halting-problem/) and [Rice's theorem](/rice-theorem/) (Volume 39). The HRU result and the undecidability of noninterference are reductions from them.
- Complexity classes: [NP-complete](/np-complete/), [co-NP](/co-np/) and [PSPACE](/pspace/) problems (Volume 39), and [set cover](/set-cover/) (Volume 18) for separation of duty and role mining.
- Properties of runs: [safety properties](/safety-property/) and [liveness properties](/liveness-property/) (Volume 16), and [deterministic finite automata](/deterministic-finite-automaton/) (Volume 9) for security automata.
- Program reasoning: [Hoare triples](/hoare-triple/) (Volume 1), [type systems](/type-system/) and [self-composition](/self-composition/) (Volume 34).
- Graph search: [breadth-first search](/breadth-first-search/) and [transitive closure](/transitive-closure/) (Volume 7), used by Take-Grant, ReBAC and the shared resource matrix.
- Cryptography and logic for group 5: the [digital signature](/digital-signature/) (Volume 23) and [Datalog](/datalog/) (Volume 40).
- Information theory for group 9: [Shannon entropy](/shannon-entropy/) and [channel capacity](/channel-capacity/) (Volume 24).
