[Binary search](/binary-search/) is about ten lines long, and it is easy to get wrong. A loop bound that is off by one, an update `lo ← mid` where `lo ← mid + 1` was needed, and the program loops forever on some inputs or misses a key that is there. In 2006 Joshua Bloch reported that the binary search in the Java library, which had been in use for years, failed on arrays of more than about a billion items: the sum `lo + hi` overflowed. Tests on small arrays could not find the error. An argument could have found it, by asking what has to be true of `lo`, `hi` and `mid` at each step and checking that each line keeps it true.

This chapter is about such arguments. A program is correct when it does what its specification says on every input the specification allows, and the chapter gives the tools for showing that: specifications, induction, loop invariants and variant functions, the invariants of data structures, and the formal systems that make the arguments checkable by a machine. It also covers testing, which cannot prove correctness but finds most errors at a small cost.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Saying what a program must do.** A [specification](/specification/) with its [precondition](/precondition/) and [postcondition](/postcondition/), and the [assertion](/assertion/) at one point of a program.
2. **Induction and other proof methods.** [Mathematical induction](/induction/), [structural induction](/structural-induction/), the [well-ordering principle](/well-ordering-principle/) and [well-founded relations](/well-founded-relation/), [proof by contradiction](/proof-by-contradiction/) and the [cut-and-paste argument](/cut-and-paste-argument/) for optimal solutions.
3. **Invariants and termination.** The [loop invariant](/loop-invariant/), the [variant function](/variant-function/) and the [termination proof](/termination-proof/), and what [correctness](/correctness/) of an algorithm means.
4. **Data structures and contracts.** The [representation invariant](/representation-invariant/), the [abstraction function](/abstraction-function/) and [design by contract](/design-by-contract/).
5. **Checking programs by running them.** [Property-based testing](/property-based-testing/), [differential testing](/differential-testing/), [symbolic execution](/symbolic-execution/) and [certifying algorithms](/certifying-algorithms/).
6. **Hoare logic.** The [Hoare triple](/hoare-triple/), [partial](/partial-correctness/) and [total correctness](/total-correctness/), [Hoare logic](/hoare-logic/), the [weakest precondition](/weakest-precondition/) and [Floyd's method](/floyd-inductive-assertions/).
7. **Deriving and analyzing programs.** Dijkstra's [guarded commands](/guarded-commands/), the [refinement calculus](/refinement-calculus/), [separation logic](/separation-logic/) and [abstract interpretation](/abstract-interpretation/).

## A first reading

For a first reading, take these entries in order: [specification](/specification/), [precondition](/precondition/), [postcondition](/postcondition/), [induction](/induction/), [structural induction](/structural-induction/), [invariant](/invariant/), [loop invariant](/loop-invariant/), [variant function](/variant-function/), [correctness](/correctness/), [proof by contradiction](/proof-by-contradiction/), [cut-and-paste argument](/cut-and-paste-argument/) and [representation invariant](/representation-invariant/). These are the tools that the proofs in the later volumes use, usually without naming them. The testing entries are short and practical, and you can read them at any time. The last two groups, from Hoare logic on, are for readers who want to see the arguments made formal; most of their entries are marked *Advanced* or *Research*.

## Before you start

The chapter assumes no earlier chapter. You should be able to read simple pseudocode with loops and arrays, and to follow a proof written in words. The examples come from algorithms that later volumes treat in full, such as [insertion sort](/insertion-sort/), binary search and [Euclid's algorithm](/euclidean-algorithm/); the entries explain all you need of them. Abstract interpretation uses the idea of a fixed point of a monotone function on a lattice, which its entry introduces.
