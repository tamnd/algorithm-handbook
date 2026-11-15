A wafer comes back from the fab, and half of its dies have a defect: a short between two wires, a broken via, a transistor that switches too slowly. The tester has a fraction of a second per die to sort good from bad. It cannot look for defects directly. It applies input patterns and compares the outputs with the outputs of a good chip. The patterns are generated for a fault model, a list of simple faults such as a wire stuck at 0, and their quality is measured as [fault coverage](/fault-coverage/), the fraction of the modelled faults they detect. The numbers matter. Under the [Williams-Brown model](/williams-brown-defect-level/), with a yield of 50 percent and a coverage of 90 percent, about 67,000 of every million shipped chips are bad. With a coverage of 99.9 percent the number falls to about 700.

This chapter extends the test part of chapter 32.7. That chapter treats the [stuck-at fault model](/stuck-at-fault-model/), [fault collapsing](/fault-collapsing/), [automatic test pattern generation](/automatic-test-pattern-generation/) with the [D-algorithm](/d-algorithm/), [PODEM](/podem/) and [SAT-based ATPG](/sat-based-atpg/), [fault simulation](/fault-simulation/), [SCOAP](/scoap/), [scan design](/scan-design/) and [built-in self-test](/built-in-self-test/). This chapter does not repeat them. It adds fault models for shorts and delays, faster generation and simulation, test compression, board, core and memory test, and diagnosis of failed chips.

Two cautions run through it. A test generator is complete only for its fault model: when it reports that every stuck-at fault is detected or proved redundant, that says nothing about a defect the model does not describe. And several formulas here are models, not theorems about chips. The defect level formula assumes random defects. The chance that a signature register hides an error is close to $2^{-k}$ only under a random-error model. Diagnosis returns a ranked list of candidates, and the list can hold several faults that no test tells apart.

## What the chapter covers

1. **Coverage and test quality.** [Fault coverage](/fault-coverage/) and its two related ratios, the [redundant fault](/redundant-fault/), the [Williams-Brown defect level](/williams-brown-defect-level/) and the [N-detect test](/n-detect-test/).
2. **Fault models for defects and delay.** The [bridging fault model](/bridging-fault-model/), [IDDQ testing](/iddq-testing/), the [transition fault model](/transition-fault-model/), the [path delay fault model](/path-delay-fault-model/), the [robust path delay test](/robust-path-delay-test/) and [cell-aware test](/cell-aware-test/).
3. **Test generation and compaction.** The [FAN algorithm](/fan-algorithm/), [static learning](/static-learning/), [recursive learning](/recursive-learning/), [time-frame expansion](/time-frame-expansion/), and [dynamic](/dynamic-test-compaction/) and [static test compaction](/static-test-compaction/).
4. **Fault simulation.** [Parallel fault simulation](/parallel-fault-simulation/), [deductive fault simulation](/deductive-fault-simulation/), [PPSFP](/ppsfp/) and [critical path tracing](/critical-path-tracing/).
5. **Testability and random-pattern test.** The [COP testability measure](/cop-testability-measure/), [test point insertion](/test-point-insertion/), [weighted random pattern testing](/weighted-random-pattern-testing/), the [multiple-input signature register](/multiple-input-signature-register/) and the [signature aliasing probability](/signature-aliasing-probability/).
6. **Scan test and compression.** [Scan chain ordering](/scan-chain-ordering/), [launch-on-capture and launch-on-shift](/launch-on-capture-and-launch-on-shift/), [broadcast scan](/broadcast-scan/), [LFSR reseeding](/lfsr-reseeding/), [embedded deterministic test](/embedded-deterministic-test/) and [X-Compact](/x-compact/).
7. **Board, core and memory test.** [Boundary scan](/boundary-scan/), the [SoC test wrapper and TAM design](/soc-test-wrapper-and-tam-design/), the [memory coupling fault](/memory-coupling-fault/) and the [march test](/march-test/).
8. **Diagnosis.** The [fault dictionary](/fault-dictionary/) and [effect-cause diagnosis](/effect-cause-diagnosis/).

## A first reading

Read these in order:

1. [Fault coverage](/fault-coverage/)
2. [Williams-Brown defect level](/williams-brown-defect-level/)
3. [Bridging fault model](/bridging-fault-model/)
4. [Transition fault model](/transition-fault-model/)
5. [Path delay fault model](/path-delay-fault-model/)
6. [Static learning](/static-learning/)
7. [Static test compaction](/static-test-compaction/)
8. [Parallel fault simulation](/parallel-fault-simulation/)
9. [PPSFP](/ppsfp/)
10. [Multiple-input signature register](/multiple-input-signature-register/)
11. [Launch-on-capture and launch-on-shift](/launch-on-capture-and-launch-on-shift/)
12. [LFSR reseeding](/lfsr-reseeding/)
13. [March test](/march-test/)
14. [Fault dictionary](/fault-dictionary/)

Robust path delay tests, cell-aware test, recursive learning, deductive fault simulation and the aliasing theorem can wait, and so can the SoC wrapper problem, which is a scheduling problem more than a test problem. Embedded deterministic test is easier once LFSR reseeding is clear, since it solves the same kind of linear system over GF(2).

## Before you start

Read chapter 32.7 first, at least the stuck-at fault model, PODEM, fault simulation, scan design and built-in self-test. The [Boolean circuit](/boolean-circuit/) of Volume 1 is the object under test.

Pattern generators and signature registers are the [linear feedback shift register](/linear-feedback-shift-register/) of Volume 12. Their analysis is [GF(2) polynomial arithmetic](/gf2-polynomial-arithmetic/) and the [cyclic redundancy check](/cyclic-redundancy-check/) of Volume 24, and X-Compact borrows the [parity-check matrix](/parity-check-matrix/) of the same volume. Seeds for LFSR reseeding come from [Gaussian elimination over GF(2)](/xor-gaussian-elimination/) in Volume 16, which also has [SAT](/sat/) and [equivalence checking](/equivalence-checking/), the main users of learning. The aliasing theorem uses the [Markov chain](/markov-chain/) of Volume 17.

Static compaction is [graph coloring](/graph-coloring/) (Volume 7) and [set cover](/set-cover/) (Volume 18). Scan chain ordering is an [asymmetric TSP](/asymmetric-tsp/) (Volume 18). Probability in Volume 1, mainly the [union bound](/union-bound/) and the [binomial distribution](/binomial-distribution/), is enough for the random-pattern entries.
