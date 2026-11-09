To find the largest of $n$ keys, scan them and keep the largest so far. The scan makes $n - 1$ comparisons. No method that learns about the keys only by comparing them can do better, and the proof takes two sentences. Each key other than the maximum must lose at least one comparison, or the algorithm cannot rule it out as the maximum. One comparison has only one loser, so $n - 1$ comparisons are needed.

That argument is a lower bound: a statement about every algorithm for a problem, including the ones nobody has thought of yet. An upper bound needs one good algorithm. A lower bound must defeat all of them, and that is why lower bounds are harder to prove and why, for many problems, the best known lower bound is the trivial one. When the two meet, the problem is settled. [Merge sort](/merge-sort/) uses about $n \lg n$ comparisons and every comparison sort needs $\lg n! \approx n \lg n - 1.44n$; [binary search](/binary-search/) uses $\lceil \lg(n+1) \rceil$ probes and no comparison search can use fewer. No comparison sort can be asymptotically faster than merge sort, and no one needs to look for one.

Every lower bound holds in a model, and it says nothing outside it. The bound for sorting counts comparisons; [counting sort](/counting-sort/) reads the keys as numbers and sorts small integers in linear time. Part of the work in each entry of this chapter is to say exactly what the algorithm may do, so that the bound is honest about what it excludes.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Upper and lower bounds.** The definitions of [upper](/upper-bound/) and [lower bounds](/lower-bound/), [optimality](/optimality/), and the [trivial lower bound](/trivial-lower-bound/) from reading the input.
2. **Counting and decision trees.** The [counting argument](/counting-argument/), the [information-theoretic bound](/information-theoretic-bound/), the [decision tree method](/decision-tree-method/), the optimality of binary search and of [merge sort](/merge-sort-optimality/), and the problem of [element distinctness](/element-distinctness/).
3. **Adversary arguments.** The [adversary argument](/adversary-argument/) and its exact results for the [maximum](/max-finding-lower-bound/), the [maximum and minimum](/max-min-lower-bound/) and the [second largest](/second-largest-lower-bound/).
4. **Reductions and algebraic models.** [Lower bounds by reduction](/reduction-lower-bound/), [Ben-Or's theorem](/ben-or-theorem/) on algebraic computation trees, and the optimality of [Horner's rule](/horners-rule-optimality/) and of the [FFT](/fft-lower-bound/).
5. **Reads, pebbles and block transfers.** [String matching](/string-matching-lower-bound/), the [pebbling](/pebbling-lower-bound/) method for memory traffic, and [external sorting](/external-sorting-lower-bound/).
6. **Randomness and incompressibility.** [Yao's minimax principle](/yao-minimax-principle/) and the [incompressibility method](/incompressibility-method/).
7. **Data structures in the cell-probe model.** [Cell-probe lower bounds](/cell-probe-lower-bound/) for [dictionaries](/static-dictionary-lower-bound/), [partial sums](/dynamic-partial-sums-lower-bound/), [predecessor search](/predecessor-lower-bound/) and [union-find](/union-find-lower-bound/).

## A first reading

For a first reading, take these entries in order: [upper bound](/upper-bound/), [lower bound](/lower-bound/), [algorithm optimality](/optimality/), [trivial lower bound](/trivial-lower-bound/), [counting argument](/counting-argument/), [information-theoretic bound](/information-theoretic-bound/), [decision tree method](/decision-tree-method/), [sorted search lower bound](/sorted-search-lower-bound/), [maximum finding lower bound](/max-finding-lower-bound/), [adversary argument](/adversary-argument/), [maximum and minimum](/max-min-lower-bound/) and [lower bounds by reduction](/reduction-lower-bound/). These give the three methods, counting, adversaries and reductions, that prove most of the lower bounds in later volumes. The last two groups are research topics; read them when a data structure in Volume 3 claims to be optimal.

## Before you start

The chapter uses the [comparison model](/comparison-model/) and the [decision tree model](/decision-tree-model/) of Chapter 1.1, the notation of Chapter 1.2, and [Stirling's approximation](/stirling-approximation/) for $\lg n!$. The entries on algebraic trees, pebbling and cell probes rely on the matching models of Chapter 1.1, and Yao's principle uses [expected values](/expected-value/) from Chapter 1.6. Several examples are algorithms from later volumes, such as merge sort and binary search; you need only their costs.
