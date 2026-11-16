A complexity class collects the decision problems that one kind of machine can solve within one bound on a resource. P is the problems a deterministic Turing machine decides in polynomial time, NP those it can verify in polynomial time, and PSPACE those it decides in polynomial space. Classes let you state what a problem needs without naming an algorithm, and they let you compare resources: time against space, determinism against guessing, randomness against none, uniform machines against circuits.

Few of the relations between classes are proved. The hierarchy theorems show that more time or more space solves more problems, and Savitch's theorem shows that nondeterminism saves at most a square in space. But whether P equals NP, or P equals PSPACE, is open. Proof methods that work the same with any oracle, and proofs of a certain natural form, cannot settle these questions, and part of this chapter explains why.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Time and space classes.** P, NP and coNP, L and NL, PSPACE, EXPTIME and NEXPTIME, with the time and space hierarchy theorems, Savitch's theorem and the Immerman-Szelepcsényi theorem.
2. **Randomized and quantum classes.** RP, coRP, ZPP, BPP, PP and BQP, with Adleman's theorem and the Sipser-Gács theorem.
3. **Circuits and parallel classes.** P/poly, NC, AC0 and TC0, and the Karp-Lipton theorem.
4. **Hierarchies and counting.** The polynomial hierarchy, the Boolean hierarchy, Toda's theorem and the Valiant-Vazirani theorem.
5. **Proof systems.** Interactive proofs, Arthur-Merlin games, IP = PSPACE, MIP = NEXP and the PCP theorem.
6. **Search classes and barriers.** FP, FNP, TFNP, PLS and PPAD, and the relativization, natural proofs and algebrization barriers.

## What to read meanwhile

The machine models behind the classes are written in Volume 1: the [Turing machine](/turing-machine/), the [nondeterministic Turing machine](/nondeterministic-turing-machine/), the [probabilistic Turing machine](/probabilistic-turing-machine/), the [alternating Turing machine](/alternating-turing-machine/) and the [Boolean circuit](/boolean-circuit/), with [non-uniform computation](/non-uniform-computation/) and [space complexity](/space-complexity/). The class NP itself is defined in Chapter 39.2, by the [polynomial-time verifier](/polynomial-time-verifier/), and [Ladner's theorem](/ladners-theorem/) there shows that NP has problems neither in P nor NP-complete, if P ≠ NP.

Complete problems for PSPACE are written in other volumes: [QBF](/qbf/) in Volume 16, [regular expression equivalence](/regex-equivalence-pspace-completeness/) in Volume 9 and [STRIPS plan existence](/strips-plan-existence-pspace-complete/) in Volume 29. For randomness and circuits, read [hardness versus randomness](/hardness-versus-randomness/) in Volume 17. For PCPs, read [Håstad's 3-bit PCP](/hastad-3bit-pcp/) in Volume 18.
