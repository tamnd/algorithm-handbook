A sorting network sorts by a plan made before it sees the data. It is a list of [comparators](/comparator/), each of which takes two positions and puts the smaller item in the first and the larger in the second. The list depends only on the number of items $n$. A comparison sort such as [merge sort](/merge-sort/) chooses its next comparison from the answers so far; a network cannot. In exchange, comparators that touch different positions can run at the same time, and the whole sort has no branches.

This matters wherever many equal operations run at once or the pattern of work must not depend on the data. A SIMD unit sorts 8 or 16 numbers in registers with a small network, one layer of comparators per pair of minimum and maximum instructions. GPU sorts merge blocks with Batcher's networks. Switching hardware routes packets through comparator circuits. In secure computation a sort must not reveal the data through its memory accesses, and a network is the simplest sort with that property. In theory, the depth of a network is the parallel time of sorting, and the question of the smallest depth led to one of the hardest constructions in algorithms.

A network has two costs. Its [size](/network-size/) is the number of comparators, the work on one processor. Its [depth](/network-depth/) is the number of layers, the time when each layer runs in one step.

## What the chapter covers

The chapter is in six groups, read in order.

1. **The model.** The [comparator](/comparator/), the [sorting network](/sorting-network/), and its two costs, [size](/network-size/) and [depth](/network-depth/). The simple sorts of Chapter 4.1 give networks of size $n(n-1)/2$.
2. **Proving that a network sorts.** The [zero-one principle](/zero-one-principle/): a network sorts every input if it sorts every input of zeros and ones. Deciding whether a given network sorts is still hard in the worst case, as [sorting network verification](/sorting-network-verification/) shows.
3. **Bitonic sorting.** A [bitonic sequence](/bitonic-sequence/) goes up and then down. The [bitonic merger](/bitonic-merger/) sorts it in $\lg n$ layers, and [bitonic sort](/bitonic-sort/) is the merge sort built on it.
4. **Odd-even merging.** A [merging network](/merging-network/) merges two sorted lists. Batcher's [odd-even merge sort](/odd-even-merge-sort/) uses fewer comparators than bitonic sort in the same depth $\tfrac12 \lg n (\lg n + 1)$. The [pairwise sorting network](/pairwise-sorting-network/) matches it exactly.
5. **The best networks for small inputs.** The [minimum size](/minimum-size-sorting-network/) and the [minimum depth](/minimum-depth-sorting-network/) for small $n$, the [trade-off](/depth-size-tradeoff/) between them, and [Green's network](/green-filter/) of 60 comparators for 16 inputs.
6. **Depth $O(\log n)$.** The [depth lower bound](/sorting-network-depth-lower-bound/) of $\lceil \lg n \rceil$, the [halver](/halver/), and the [AKS network](/aks-sorting-network/), which reaches depth $O(\log n)$ and size $O(n \log n)$.

## A first reading

For a first reading, take these eleven entries in order: [comparator](/comparator/), [sorting network](/sorting-network/), [network size](/network-size/), [network depth](/network-depth/), [the zero-one principle](/zero-one-principle/), [bitonic sequence](/bitonic-sequence/), [bitonic merger](/bitonic-merger/), [bitonic sort](/bitonic-sort/), [merging network](/merging-network/), [odd-even merge sort](/odd-even-merge-sort/) and [the depth lower bound](/sorting-network-depth-lower-bound/). Work through the example tables of bitonic sort and odd-even merge sort by hand: a network is easiest to understand by running it. The proof of the zero-one principle is short and is used everywhere else, so read it closely. Leave the searches for optimal small networks, verification, halvers and the AKS network for a second pass.

## Before you start

You need the [comparison model](/comparison-model/) and [asymptotic notation](/asymptotic-notation/) from Volume 1, and from Chapter 4.1 the [sorting problem](/sorting-problem/), [merging sorted lists](/merging-sorted-lists/), [merge sort](/merge-sort/) and the [comparison sorting lower bound](/comparison-sort-lower-bound/). The proofs are by induction and by counting zeros. For the AKS network you need [bipartite graphs](/bipartite-graph/) and the idea of an expander; for verification, the class [co-NP-complete](/co-np-complete/). The parallel uses of networks are taken up again in [parallel sorting](/parallel-sorting-problem/), Chapter 4.6. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
