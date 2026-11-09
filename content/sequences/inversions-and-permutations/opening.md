A permutation is a sequence of $n$ distinct items, usually the numbers $1$ to $n$, in some order. Every sort produces one: it is the order in which the input items end up. So the questions of this chapter sit under much of the book: how far a sequence is from sorted, how to move items by a given permutation without a second array, how many permutations have some property, and how to list them, number them and tell two of them apart.

The answers use a small set of tools. The [cycles](/permutation-cycles/) of a permutation describe where each item goes. The [inversions](/inversion/), the pairs of items in the wrong order, measure disorder. The [Lehmer code](/lehmer-code/) turns a permutation into a list of independent digits, and so into a number. Most entries in the chapter use one of these three, and several connect two of them.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **Permutations and their cycles.** The two ways to read a permutation, as positions to values or values to positions, and the [inverse](/permutation-inverse/) that switches them. Every permutation splits into disjoint cycles, and the cycles give its order, its sign and its powers.
2. **Applying a permutation.** Moving the items of an array to new places in linear time with $O(1)$ extra words, by walking one cycle at a time. The same cycles give [any power](/permutation-power/) of a permutation in linear time.
3. **Inversions and descents.** The inversion count is the standard measure of disorder. A random permutation has $n(n-1)/4$ inversions on average. Descents are the inversions between neighbours, and the [parity](/permutation-parity/) of the inversion count is the sign of the permutation.
4. **Counting inversions.** [Counting inversions](/counting-inversions/) in $O(n \log n)$ time with a merge sort or a Fenwick tree, and why the count is the fewest [swaps of neighbours](/sorting-by-adjacent-swaps/) that sort a sequence.
5. **Codes, ranks and successors.** The inversion table, the Lehmer code and the factorial number system, which together [rank and unrank](/permutation-rank-unrank/) permutations in lexicographic order. The [next permutation](/lexicographic-successor/) is one step of this numbering. The [Mahonian numbers](/mahonian-numbers/) count permutations by their number of inversions.
6. **Distances between rankings.** Four ways to measure how far apart two orderings of the same items are: the [Kendall tau distance](/kendall-tau-distance/), the Cayley distance, the Spearman footrule and the Ulam distance. Measures of presortedness apply the same ideas to one sequence and the sorted order.
7. **Sorting with restricted moves.** Prefix flips, reversals and block moves. Finding the fewest moves is NP-hard for each of the three, and the lower bounds and approximations come from counting breakpoints.
8. **Stacks and patterns.** The permutations a stack can produce or sort are exactly those that avoid one pattern of length 3. Pattern avoidance and pattern matching grew out of this result.

Groups 1 to 5 are the core. Groups 6 to 8 build on them and can be read in any order.

## A first reading

For a first reading, take these entries in order: [permutation](/permutation/), [permutation cycles](/permutation-cycles/), [the inverse permutation](/permutation-inverse/), [inversion](/inversion/), [the expected number of inversions](/expected-number-of-inversions/), [counting inversions](/counting-inversions/), [inversion counting by merge sort](/inversion-count-by-merge-sort/), [sorting by adjacent swaps](/sorting-by-adjacent-swaps/), [permutation parity](/permutation-parity/), [the Lehmer code](/lehmer-code/), [ranking and unranking](/permutation-rank-unrank/) and [the Kendall tau distance](/kendall-tau-distance/). Work through the small examples by hand. Most entries use the same two permutations, $3\,1\,4\,5\,2$ and $2\,4\,1\,3\,6\,5$, so the numbers from one entry carry over to the next.

## Before you start

You need [asymptotic notation](/asymptotic-notation/) and the [comparison model](/comparison-model/) from Volume 1, and the idea of a [total order](/total-order/). The probability in the chapter uses [indicator random variables](/indicator-random-variable/) and [linearity of expectation](/linearity-of-expectation/). The counting algorithms build on [merge sort](/merge-sort/), the [Fenwick tree](/fenwick-tree/) and [coordinate compression](/coordinate-compression/). The ranking entries use [lexicographic order](/lexicographic-order/) and [positional number systems](/positional-number-system/), and the power of a permutation uses [binary exponentiation](/binary-exponentiation/). The stack entries need only the [stack](/stack/) itself. The Ulam distance is a [longest increasing subsequence](/longest-increasing-subsequence/) problem, so read that entry in the chapter on subsequences first. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
