To sort is to put items in order. It is one of the oldest tasks given to a computer, and it is still one of the most common. A database sorts rows to answer a query with `ORDER BY` and to join two tables. A compiler sorts symbols. A search engine sorts pages by score. A plotting library sorts points before it draws a line through them. Even when no output is sorted, sorting is often the hidden first step: to find duplicates, to find the median, to group equal keys, to find the closest pair of numbers, you can sort first and then make one scan.

This volume collects what is known about sorting and its near relatives. It starts with the sorts that compare keys, then the sorts that use the digits or the values of keys, then the problem of finding one item by its rank without sorting everything. Then come three settings where the plain model of one processor and one fast memory does not hold: fixed networks of comparators, data too large for main memory, and many processors working at once.

## Why sorting gets a volume of its own

Sorting is small enough to state in one line and rich enough to teach most of the ideas of algorithm design. In this one volume you will meet:

- **Incremental design.** [Insertion sort](/insertion-sort/) grows a sorted prefix one item at a time. Its proof is the first [loop invariant](/loop-invariant/) most people learn.
- **Divide and conquer.** [Merge sort](/merge-sort/) splits, sorts and merges. [Quicksort](/quicksort/) splits around a pivot and needs no merge.
- **Randomization.** [Randomized quicksort](/randomized-quicksort/) runs in $O(n \log n)$ expected time on every input, because the coin flips belong to the algorithm and not to the input.
- **Data structures as algorithms.** [Heapsort](/heapsort/) is a [binary heap](/binary-heap/) used a certain way. [Tree sort](/tree-sort/) is a [binary search tree](/binary-search-tree/) read in order.
- **Lower bounds.** The [comparison sorting lower bound](/comparison-sort-lower-bound/) proves that no comparison sort can beat $\lceil \lg n! \rceil$ comparisons in the worst case. It is the cleanest example of an argument about all algorithms at once.
- **Beating a lower bound by changing the model.** [Counting sort](/counting-sort/) and [radix sort](/radix-sort/) do not compare keys, so the bound does not apply to them.
- **Engineering.** The sorts in real libraries, such as [Timsort](/timsort/) and [introsort](/introsort/), are hybrids. They are chosen by measuring, not only by asymptotic analysis.

## The chapters

**Chapter 4.1, Comparison sorts**, is the heart of the volume. It defines the [sorting problem](/sorting-problem/) and the [comparison model](/comparison-model/). It then builds the main families of sorts one by one: the simple quadratic sorts, Shellsort, merge sort, quicksort and the heap-based sorts. It ends with the lower bound and with the hybrid sorts that libraries ship.

**Chapter 4.2, Distribution sorts**, drops the comparison model. When keys are small integers, strings or numbers spread evenly over a range, a sort can look inside the keys. [Counting sort](/counting-sort/), [radix sort](/radix-sort/) and [bucket sort](/bucket-sort/) run in linear time on such keys.

**Chapter 4.3, Selection and order statistics**, asks for less than a full sort: only the item of rank $k$, such as the median. [Quickselect](/quickselect/) does this in linear expected time, and the [median of medians](/median-of-medians/) in linear worst-case time.

**Chapter 4.4, Sorting networks**, fixes the sequence of comparisons in advance, so that it does not depend on the data. This is how sorting is done in hardware and in SIMD code. The [zero-one principle](/zero-one-principle/) makes such networks easy to prove correct.

**Chapter 4.5, External sorting**, sorts data that does not fit in main memory. The cost that matters is the number of passes over the disk, not the number of comparisons. [External merge sort](/external-merge-sort/) and [replacement selection](/replacement-selection/) are the main tools.

**Chapter 4.6, Parallel sorting**, sorts with many processors. It covers sorts on meshes and hypercubes, and sample sorts for clusters.

## How to read this volume

If this is your first course, read these entries of Chapter 4.1 in this order: [the sorting problem](/sorting-problem/), [comparison sort](/comparison-sort/), [stable sort](/stable-sort/), [insertion sort](/insertion-sort/), [selection sort](/selection-sort/), [merging sorted lists](/merging-sorted-lists/), [merge sort](/merge-sort/), [Lomuto partition](/lomuto-partition/), [quicksort](/quicksort/), [randomized quicksort](/randomized-quicksort/), [heapsort](/heapsort/) and [the lower bound](/comparison-sort-lower-bound/). Then read [counting sort](/counting-sort/) and [radix sort](/radix-sort/) in Chapter 4.2, and [quickselect](/quickselect/) in Chapter 4.3. Do the exercises marked ◦ and • at the end of each of these chapters. That is a complete first unit on sorting.

If you already know the basic sorts, start with the opening page of each chapter. It names the families in the chapter and the order to read them. The entries marked *Advanced* and *Research* in each chapter are the place to go deeper.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too, as [asymptotic notation](/asymptotic-notation/) in Volume 1 and the [binary heap](/binary-heap/) in Volume 3 are; the number is printed with the link.

## What you need first

You should be able to read a short program and follow a proof by induction. From Volume 1 you need [asymptotic notation](/asymptotic-notation/), [loop invariants](/loop-invariant/) and, for the analysis of quicksort, [linearity of expectation](/linearity-of-expectation/). From Volume 3 you need [binary heaps](/binary-heap/) for heapsort and [binary search trees](/binary-search-tree/) for tree sort. Nothing else is assumed.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
