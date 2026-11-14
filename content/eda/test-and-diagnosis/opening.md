Manufacturing test decides, for each chip that comes off the line, whether it has a defect. It is not verification: the design is taken as correct, and the question is whether this copy of it was built right. A tester applies patterns and compares the responses with the expected ones; its time is costly, so the aims are few patterns, high detection and easy access to internal logic. Defects are physical and varied, so tests are generated for fault models, and the quality of a test set is measured by its fault coverage, which counts modelled faults only. When chips fail, diagnosis reasons back from the failing responses to the likely defects.

The core of the subject is in the chapter on timing, verification and test; this chapter extends it. Test generation is NP-complete, so complete methods take exponential time in the worst case; the learning and search methods here make them much faster on real circuits. Several formulas here are models: the probability that an $n$-bit signature register hides an error is close to $2^{-n}$ under a model of random error streams, and the Williams-Brown defect level $1 - Y^{1-T}$ links yield $Y$ and fault coverage $T$ to the fraction of bad chips shipped.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Fault models and measures.** Bridging, transition and path delay faults, robust path delay tests, redundant faults, IDDQ testing, cell-aware test, N-detect tests, fault coverage and the Williams-Brown defect level.
2. **Faster test generation.** The FAN algorithm, static and recursive learning, time-frame expansion for sequential circuits, and dynamic and static test compaction.
3. **Faster fault simulation.** Parallel fault simulation, parallel-pattern single-fault propagation, deductive fault simulation and critical path tracing.
4. **Design for test.** The COP testability measure, test point insertion, weighted random patterns, the multiple-input signature register and its aliasing probability, scan chain ordering, launch-on-capture and launch-on-shift, boundary scan, and test wrappers and access mechanisms for systems on chip.
5. **Test compression.** LFSR reseeding, broadcast scan, embedded deterministic test and X-Compact.
6. **Memory test and diagnosis.** March tests and memory coupling faults, fault dictionaries and effect-cause diagnosis.

## What to read meanwhile

Start with the written core: the [stuck-at fault model](/stuck-at-fault-model/), [automatic test pattern generation](/automatic-test-pattern-generation/), the [D-algorithm](/d-algorithm/), [PODEM](/podem/), [SAT-based ATPG](/sat-based-atpg/), [fault simulation](/fault-simulation/), [SCOAP](/scoap/), [scan design](/scan-design/) and [built-in self-test](/built-in-self-test/). Path delay tests rest on [static timing analysis](/static-timing-analysis/) and [false paths](/false-path/).

From other volumes: the [linear feedback shift register](/linear-feedback-shift-register/) (Volume 12) for pattern generators and signatures; [Gaussian elimination over GF(2)](/xor-gaussian-elimination/) (Volume 16) for LFSR reseeding; [set cover](/set-cover/) (Volume 18) for static compaction; the [traveling salesman problem](/traveling-salesman-problem/) (Volume 15) for scan chain ordering; and [bounded model checking](/bounded-model-checking/) (Volume 16), which unrolls a circuit in time as time-frame expansion does.
