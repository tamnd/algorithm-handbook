A comparison sort learns about its input only by asking questions of one kind: is this item smaller than that one? It never looks inside a key. This sounds like a strong restriction, but it is what makes a sort general. The same comparison sort can order integers, strings, dates, or records by any rule you give it, as long as the rule is a [total order](/total-order/). That is why the sort in nearly every standard library is a comparison sort.

This chapter is the longest of the volume. It holds the sorts every programmer should know, the variations that show why the standard ones are built as they are, and the theory that says how fast any comparison sort can be.

## What the chapter covers

The chapter is in nine groups, read in order.

1. **The problem and the rules.** What sorting is, what a comparison sort may do, and how its cost is counted. Two properties come up again and again: a sort is *in place* if it needs only a little memory beyond the array, and *stable* if it keeps equal keys in their input order.
2. **The simple sorts.** [Insertion sort](/insertion-sort/), [selection sort](/selection-sort/) and their relatives. They take quadratic time, but insertion sort is still the fastest sort for very short arrays, so the fast sorts use it as a base case.
3. **Insertion with gaps.** [Shellsort](/shell-sort/) and [library sort](/library-sort/) let items move in long steps.
4. **Merge sort.** Divide, sort the halves, merge. $\Theta(n \log n)$ on every input, and stable.
5. **Quicksort.** Partition around a pivot, then sort each side. The fastest general sort in practice, with care in choosing the pivot.
6. **Sorting with heaps and trees.** [Heapsort](/heapsort/) sorts in place in $\Theta(n \log n)$ worst-case time.
7. **How many comparisons.** The [lower bound](/comparison-sort-lower-bound/) of $\lceil \lg n! \rceil$ comparisons, and the algorithm that gets closest to it.
8. **Input that is already partly sorted.** How to measure disorder and sort faster when there is little of it.
9. **The sorts that libraries use.** [Introsort](/introsort/), [Timsort](/timsort/) and the Java library sort, built from the parts above.

## A first reading

For a first reading, take these twelve entries in order: [the sorting problem](/sorting-problem/), [comparison sort](/comparison-sort/), [stable sort](/stable-sort/), [insertion sort](/insertion-sort/), [selection sort](/selection-sort/), [merging sorted lists](/merging-sorted-lists/), [merge sort](/merge-sort/), [Lomuto partition](/lomuto-partition/), [quicksort](/quicksort/), [randomized quicksort](/randomized-quicksort/), [heapsort](/heapsort/) and [the comparison sorting lower bound](/comparison-sort-lower-bound/). Each one is marked *Intro* or *Core* in its heading. Skip the proofs on a first pass if you like, but come back to them: the proofs of insertion sort, merge sort and the lower bound are models for many proofs later in the book.

## Before you start

You need [asymptotic notation](/asymptotic-notation/) and [loop invariants](/loop-invariant/) from Volume 1. For quicksort's expected time you need [indicator random variables](/indicator-random-variable/) and [linearity of expectation](/linearity-of-expectation/). For heapsort you need the [binary heap](/binary-heap/) from Volume 3. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
