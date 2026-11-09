This is the first volume of *The Handbook of Algorithms*. The handbook is the printed form of a site of algorithm entries, and its volumes follow the areas of the site: foundations here, then techniques, data structures, sorting, searching, graphs, strings and the rest, each area one volume. A volume is divided into chapters, and a chapter into groups of entries, read in order. Every entry has a number with three parts, the volume, the chapter and its place in the chapter, so the third entry of Chapter 1.2 is 1.2.3. When an entry mentions another one, the number follows the link, and you can find the other entry in this volume or on the shelf.

The heading of an entry says what kind of entry it is, such as a definition, a theorem, an algorithm or a model, and its level, from Intro through Core and Advanced to Research. A one-line summary follows, and then a facts box. The box gives the costs of an algorithm, the model in which they are measured, the problem it solves, and under *Needs* the entries to read first. Then come the statement, the explanation, a proof or an analysis, and for many algorithms a tested implementation in Python. Each chapter opens with a page that tells you what the chapter covers and which entries to read first, and it closes with a summary, exercises in three bands and notes on history and further reading. Hints to the exercises are in an appendix at the end of the volume.

This volume holds the tools that the other volumes use to state and prove what their algorithms do. It says what a step of computation is, how to measure running time and memory, how to solve the recurrences that recursive algorithms produce, how to prove a program correct, how to average costs over a sequence of operations or over random choices, and how to show that no algorithm can do better.

## Why foundations get a volume of their own

Every claim in this handbook has the form "this algorithm, in this model, costs this much, and here is why". The pieces of that sentence are the subject of this volume:

- **A model.** A cost is a count of steps, and the count depends on what a step is. The [random-access machine](/random-access-machine/) and the [comparison model](/comparison-model/) are the two models used most; the volume also gives the models for memory hierarchies, for data structures and for complexity theory.
- **A measure.** [Asymptotic notation](/asymptotic-notation/) states a cost up to a constant factor, and [worst-case analysis](/worst-case-analysis/) says which inputs the cost is about.
- **A calculation.** Loops become sums, recursion becomes a [recurrence](/recurrence-relation/), and the [master theorem](/master-theorem/) solves the most common recurrences at a glance.
- **A proof.** A [loop invariant](/loop-invariant/) proves that a loop does what it should; [induction](/induction/) proves the rest.
- **Two kinds of average.** [Amortized cost](/amortized-cost/) averages over a sequence of operations and needs no probability. [Expected cost](/expected-value/) averages over random inputs or random choices, and [tail bounds](/chernoff-bound/) say how far a single run may stray from the mean.
- **A limit.** A [lower bound](/lower-bound/) holds for every algorithm, so it tells you when to stop looking for a faster one.

## The chapters

**Chapter 1.1, Models of computation**, defines the machines that algorithms run on in theory: the [random-access machine](/random-access-machine/) with its cost rules, the [word RAM](/word-ram/), the comparison and [decision tree](/decision-tree-model/) models, the [external memory model](/external-memory-model/), the [Turing machine](/turing-machine/) and [Boolean circuits](/boolean-circuit/). Each model makes some operations cheap and others impossible, and the chapter shows how that choice changes what can be proved.

**Chapter 1.2, Asymptotic analysis**, gives the notation $O$, $\Omega$ and $\Theta$, the sums and logarithms that running times are made of, the ladder of [common growth rates](/common-growth-rates/), and [Stirling's approximation](/stirling-approximation/). The [doubling hypothesis](/doubling-hypothesis/) checks an analysis against a timed program.

**Chapter 1.3, Recurrences**, solves the equations that describe recursive algorithms: by unrolling, by the [recursion tree](/recursion-tree-method/), by [substitution](/substitution-method/), by the [master theorem](/master-theorem/) and by the [Akra-Bazzi theorem](/akra-bazzi-theorem/). It also treats [linear recurrences](/linear-recurrences-with-constant-coefficients/) such as the Fibonacci numbers.

**Chapter 1.4, Correctness and invariants**, is about proof. It starts from [specifications](/specification/), [preconditions](/precondition/) and [postconditions](/postcondition/), proves loops correct with [invariants](/loop-invariant/) and [variant functions](/variant-function/), and builds up to [Hoare logic](/hoare-logic/) and the [weakest precondition](/weakest-precondition/). It also covers the practical side: [property-based testing](/property-based-testing/) and [certifying algorithms](/certifying-algorithms/).

**Chapter 1.5, Amortized analysis**, bounds the total cost of a sequence of operations when a few of them are expensive. The [aggregate](/aggregate-method/), [accounting](/accounting-method/) and [potential](/potential-method/) methods are shown on the binary counter and on [dynamic arrays](/array-doubling/). The same methods give the bounds for splay trees and Fibonacci heaps in Volume 3.

**Chapter 1.6, Probabilistic analysis**, gives the probability that randomized algorithms and average-case analyses need: [indicator variables](/indicator-random-variable/) and [linearity of expectation](/linearity-of-expectation/), the [union bound](/union-bound/), [Markov's](/markov-inequality/) and [Chebyshev's](/chebyshev-inequality/) inequalities, the classic processes of [balls into bins](/balls-into-bins/) and the [coupon collector](/coupon-collector-problem/), the [Chernoff bound](/chernoff-bound/) and martingales.

**Chapter 1.7, Lower bounds**, proves limits for all algorithms at once, by [counting](/counting-argument/), by [adversary arguments](/adversary-argument/) and by [reductions](/reduction-lower-bound/). Its results include the exact costs of finding the [maximum](/max-finding-lower-bound/) and the [second largest](/second-largest-lower-bound/), the optimality of binary search and merge sort, and lower bounds for data structures in the [cell-probe model](/cell-probe-model/).

## How to read this volume

This volume is a reference as much as a course: most readers come to it from a later volume, to look up a tool when an entry uses it. If you want a first course instead, read these entries in this order: [asymptotic notation](/asymptotic-notation/), [random-access machine](/random-access-machine/), [comparison model](/comparison-model/), [worst-case analysis](/worst-case-analysis/), [logarithms](/logarithms/), [geometric series](/geometric-series/), [harmonic series](/harmonic-series/), [induction](/induction/), [loop invariant](/loop-invariant/), [recurrence relation](/recurrence-relation/), [recursion tree method](/recursion-tree-method/), [master theorem](/master-theorem/), [amortized cost](/amortized-cost/), [potential method](/potential-method/), [expected value](/expected-value/), [linearity of expectation](/linearity-of-expectation/), [lower bound](/lower-bound/) and [decision tree method](/decision-tree-method/). Do the ◦ exercises of each chapter as you go. That is enough to follow the analyses in every later volume.

The chapters need not be read in their printed order. Chapter 1.2 is used by all the others, and Chapter 1.4 can be read at any time. Chapter 1.1 is easier after Chapter 1.2, and the second half of Chapter 1.1, on Turing machines and circuits, matters mostly for complexity theory. The entries marked *Advanced* and *Research*, such as the [Azuma-Hoeffding inequality](/azuma-inequality/) or the cell-probe lower bounds, are for readers who meet them in a paper or in a later volume.

## What you need first

You should be able to read a short program in a language such as Python and follow a proof by induction; Chapter 1.4 explains induction, but the earlier chapters use it. School algebra is needed throughout, with logarithms and exponents. Chapter 1.2 uses limits of sequences and a few simple integrals, and Chapter 1.6 uses counting with [binomial coefficients](/binomial-coefficient/). A few examples refer to algorithms from later volumes, such as [merge sort](/merge-sort/), [quicksort](/quicksort/) and [binary search](/binary-search/); you need only their names and their costs, and the entries give both. Nothing else is assumed.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
