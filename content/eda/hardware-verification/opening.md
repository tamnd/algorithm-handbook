Hardware verification checks that a design does what its specification says before it is manufactured, while a bug can still be fixed by editing a file rather than by making new masks. Two approaches share the work. Simulation runs the design on generated stimuli and compares it with a reference model. It scales to whole chips, but it shows only that the cases it ran are right, so coverage metrics are used to judge when to stop. Formal verification proves a property, or the equivalence of two versions, for all inputs. Equivalence checking, which compares a register-transfer description with the netlist that synthesis made from it, is a routine step of design flows.

Formal proof has a price. Combinational equivalence is coNP-complete for circuits, yet SAT solvers and structural hashing decide it on large designs in practice; sequential equivalence needs the reachable states and is much harder. BDD-based methods depend on the variable order, and no order keeps the BDD of a multiplier small, which is why arithmetic circuits get algebraic methods of their own. Processors are checked against their instruction set by abstraction, with uninterpreted functions in place of the datapath.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Stimulus and coverage.** Constrained random stimulus generation and its BDD-based form, coverage-directed test generation, and code, FSM, functional and observability-based coverage.
2. **Assertions.** Assertion-based verification and the synthesis of assertion checkers into monitor circuits.
3. **Equivalence checking.** The miter circuit, cutpoint-based equivalence checking, latch mapping, the product machine, sequential equivalence checking, signal correspondence and safe replaceability.
4. **Symbolic methods.** Symbolic simulation, symbolic trajectory evaluation and its generalized form, Coudert and Madre's image computation, and the partitioned transition relation.
5. **Arithmetic and processors.** Algebraic verification of arithmetic circuits, Taylor expansion diagrams, Burch-Dill flushing and positive equality.
6. **Clock domains and debugging.** Clock domain crossing verification, the mean time between failures of a synchronizer, and SAT-based design debugging.

## What to read meanwhile

Most of the machinery is in Volume 16. For combinational equivalence read [Boolean equivalence checking](/boolean-equivalence-checking/), [CDCL](/cdcl/) and the [Tseitin transformation](/tseitin-transformation/), then [binary decision diagrams](/binary-decision-diagram/), [variable ordering](/variable-ordering/) and the [multiplier lower bound](/multiplier-bdd-lower-bound/). For sequential designs read [symbolic reachability](/symbolic-reachability/), [bounded model checking](/bounded-model-checking/), [k-induction](/k-induction/) and [IC3](/ic3-pdr/), with [safety properties](/safety-property/) and [linear temporal logic](/linear-temporal-logic/) for what assertions say. Coudert and Madre's constrain operator is in [generalized cofactor](/generalized-cofactor/), the solution counts behind weighted random generation in [BDD satisfy-count](/bdd-satisfy-count/), and the logic of processor verification in [EUF satisfiability](/euf-satisfiability/).

In this volume, [SAT sweeping](/sat-sweeping/) on the [and-inverter graph](/and-inverter-graph/) is the core of combinational equivalence checking in tools such as ABC, and [SAT-based ATPG](/sat-based-atpg/) builds the same kind of miter to find tests. The algebraic methods start from [Gröbner bases](/groebner-basis/) (Volume 11).
