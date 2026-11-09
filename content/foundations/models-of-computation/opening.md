A running time is a count of steps, and a count of steps means nothing until you say what a step is. Sorting $n$ integers takes $\Omega(n \log n)$ steps when the only way to learn about the keys is to compare two of them. It takes $O(n)$ steps when the keys are small integers and the machine can use a key as an address, as [counting sort](/counting-sort/) does. Both statements are true; they are about different machines. In the same way, sorting a billion records on disk is not limited by comparisons at all but by the number of times a block of data moves between the disk and main memory. A model of computation fixes what the machine can do and what each operation costs, and every bound in this handbook is a bound in some model.

This chapter collects the models. Most entries of the handbook use one of them, the [word RAM](/word-ram/), without saying so. The others matter when the word RAM gives the wrong answer: when numbers grow without limit, when memory is not flat, when you want a lower bound that holds for every algorithm, or when the question is what can be computed at all.

## What the chapter covers

The chapter is in six groups, read in order.

1. **The random access machine.** The [RAM](/random-access-machine/), its [unit-cost](/unit-cost-model/) and [logarithmic-cost](/logarithmic-cost-model/) rules, the [word RAM](/word-ram/) that bounds a word to $w \ge \lg n$ bits, and the variants: the [real RAM](/real-ram/) of computational geometry and the [pointer machine](/pointer-machine/).
2. **Models that count only queries.** The [comparison model](/comparison-model/) and the [decision tree model](/decision-tree-model/), the linear and algebraic decision trees, and the [cell-probe model](/cell-probe-model/). These are the settings of most lower bounds in Chapter 1.7.
3. **Memory that is not flat.** The [memory hierarchy](/memory-hierarchy/), the [external memory model](/external-memory-model/) with its parameters $M$ and $B$, and the [cache-oblivious model](/cache-oblivious-model/).
4. **Turing machines.** The [Turing machine](/turing-machine/) and its multitape form, the simulation theorems that make polynomial time the same on each of these machines, the [equivalence of RAMs and Turing machines](/ram-turing-equivalence/), and the nondeterministic, probabilistic and alternating machines.
5. **Circuits and non-uniform models.** [Boolean circuits](/boolean-circuit/), [non-uniform computation](/non-uniform-computation/) and [branching programs](/branching-program/).
6. **Other models of computation.** The [lambda calculus](/lambda-calculus/), [register machines](/register-machine/), [cellular automata](/cellular-automaton/) and the Blum-Shub-Smale machine, and one model from physics.

## A first reading

For a first reading, take these entries in order: [random access machine](/random-access-machine/), [unit-cost model](/unit-cost-model/), [logarithmic-cost model](/logarithmic-cost-model/), [word RAM](/word-ram/), [comparison model](/comparison-model/), [decision tree model](/decision-tree-model/), [memory hierarchy](/memory-hierarchy/), [external memory model](/external-memory-model/), [Turing machine](/turing-machine/) and [nondeterministic Turing machine](/nondeterministic-turing-machine/). That is enough to read every cost in the handbook. The entries marked *Advanced* and *Research*, such as the algebraic computation tree, the bit-probe model and the Blum-Shub-Smale machine, are needed only for particular lower bounds or for complexity theory, and can wait until a later entry sends you to them.

## Before you start

You need [asymptotic notation](/asymptotic-notation/) and [logarithms](/logarithms/) from Chapter 1.2; the first RAM entries use nothing else. A few entries lean on ideas from other volumes: the hard-disk model uses a [priority queue](/priority-queue/) from Volume 3, and the entries on nondeterministic and Blum-Shub-Smale machines refer to [NP-completeness](/np-complete/). You can read them with only the names of these ideas and come back later.
