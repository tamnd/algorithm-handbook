Two programs solve the same problem. On 1,000 items the first takes a millisecond and the second takes ten. On a million items the first takes about 17 minutes and the second about 20 seconds. The second program is not faster by a constant: its running time grows like $n \lg n$, the first one's like $n^2$, and for large inputs the growth wins over any constant. Asymptotic analysis is the language for statements of this kind. It describes a running time by its order of growth and ignores the constant factors that change from one machine and one compiler to another.

Every cost in this handbook is written in this language. When an entry says that [merge sort](/merge-sort/) takes $\Theta(n \log n)$ time in the worst case, each part of that sentence has a precise meaning, and this chapter gives it: what $n$ measures, which inputs the bound is about, what is being counted, and what $\Theta$ allows and forbids.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Cost as a function of size.** [Asymptotic notation](/asymptotic-notation/) ($O$, $\Omega$, $\Theta$, $o$, $\omega$), [input size](/input-size/), [time](/time-complexity/) and [space complexity](/space-complexity/), and the difference between [worst-case](/worst-case-analysis/) and [best-case analysis](/best-case-analysis/).
2. **Logarithms and sums.** The tools for turning a loop into a formula: [logarithms](/logarithms/), the [arithmetic](/arithmetic-series/) and [geometric series](/geometric-series/), [integral bounds for sums](/integral-bounds-for-sums/) and the [harmonic series](/harmonic-series/).
3. **The common growth rates.** The ladder of [common growth rates](/common-growth-rates/) from constant to factorial, one entry per rung, ending with [polynomial time](/polynomial-time/), the formal meaning of "efficient".
4. **Sharper statements.** [Comparing growth by limits](/comparing-growth-by-limits/), [tilde notation](/tilde-notation/), which keeps the leading constant, [Stirling's approximation](/stirling-approximation/) for $n!$, notation with several variables, and [asymptotic optimality](/asymptotic-optimality/).
5. **Checking by experiment.** How to time a program and read its growth rate from the data, with the [doubling hypothesis](/doubling-hypothesis/).
6. **Functions that grow very slowly.** The [iterated logarithm](/iterated-logarithm/) and the [inverse Ackermann function](/inverse-ackermann-function/), which appear in the costs of some data structures.

## A first reading

For a first reading, take these entries in order: [asymptotic notation](/asymptotic-notation/), [input size](/input-size/), [time complexity](/time-complexity/), [space complexity](/space-complexity/), [worst-case analysis](/worst-case-analysis/), [logarithms](/logarithms/), [arithmetic series](/arithmetic-series/), [geometric series](/geometric-series/), [order of growth](/order-of-growth/), [common growth rates](/common-growth-rates/), [polynomial time](/polynomial-time/) and [harmonic series](/harmonic-series/). The entries on single growth rates, such as [linear time](/linear-time/) or [cubic time](/cubic-time/), are short and can be read as needed. Leave the fourth group and the last one for a second pass, except [tilde notation](/tilde-notation/), which some later chapters use for exact counts.

## Before you start

The chapter assumes school algebra and the idea of a limit of a sequence. One entry, [integral bounds for sums](/integral-bounds-for-sums/), uses simple integrals. Proofs in the chapter use [mathematical induction](/induction/), which Chapter 1.4 explains. A few examples refer to algorithms from later volumes, such as [binary search](/binary-search/) and [insertion sort](/insertion-sort/); you need only their names and costs to follow the examples.
