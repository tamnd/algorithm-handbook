Write a running total under a list of numbers. The total of any stretch of the list is now one subtraction: the running total at the end of the stretch minus the running total just before it. That one observation is the whole of this chapter, and it is used everywhere. A spreadsheet that shows sales per day uses it to give the total of any week. An image library uses its grid form, the integral image, to find the mean brightness of any rectangle in four lookups, which is what made real-time face detection possible. A booking system uses the reverse trick, the difference array, to add a passenger to every leg of a trip with two writes instead of one write per leg.

The chapter is short and most of it is at the intro level. Its ideas come back in every later chapter of the volume: a subarray sum is a difference of two prefix sums, and much of Chapter 6.2 is built on that sentence.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Range sums.** The [range sum query](/range-sum-query/) asks for the sums of many ranges of a fixed array. The [telescoping sum](/telescoping-sum/) explains why [prefix sums](/prefix-sums/) answer each query in $O(1)$ time after $\Theta(n)$ preprocessing, and why the method works for any operation that can be undone, such as XOR, but not for the maximum.
2. **Range updates.** The [range update point query](/range-update-point-query/) adds values to ranges. The [difference array](/difference-array/) stores the steps between neighbours, so each range add is two point changes and one prefix-sum pass rebuilds the array.
3. **Two dimensions.** [Two-dimensional prefix sums](/two-dimensional-prefix-sums/) give any rectangle sum with four lookups, and the [two-dimensional difference array](/two-dimensional-difference-array/) adds a value to a rectangle with four writes.
4. **The calculus of finite sums.** The [discrete antiderivative](/discrete-antiderivative/) and the [Abel summation formula](/abel-summation/) are the theory behind the first three groups: sums and differences are inverse operations, as integrals and derivatives are.
5. **When the array changes.** The [partial sums problem](/partial-sums-problem/) mixes updates with prefix-sum queries. A [Fenwick tree](/fenwick-tree/) does both in $O(\log n)$ time, and the [Fredman-Saks lower bound](/fredman-saks-partial-sums-lower-bound/) shows that no structure can be much faster.

## A first reading

For a first reading, take these eight entries in order: [range sum query](/range-sum-query/), [telescoping sum](/telescoping-sum/), [prefix sums](/prefix-sums/), [range update point query](/range-update-point-query/), [difference array](/difference-array/), [two-dimensional prefix sums](/two-dimensional-prefix-sums/), [two-dimensional difference array](/two-dimensional-difference-array/) and [partial sums problem](/partial-sums-problem/). In the last one, read the definition, the examples and the table of known algorithms, and leave the lower bounds for later.

The two entries on the calculus of finite sums are for readers who want closed forms for sums, as in the analysis of algorithms; skip them on a first pass if you only need the techniques. The Fredman-Saks lower bound is a research-level proof in the cell-probe model, and it assumes the rest of the chapter.

## Before you start

You need [arrays](/array/) and the [range query problem](/range-query-problem/) from Volume 3, [asymptotic notation](/asymptotic-notation/) and [proof by induction](/induction/) from Volume 1, and the [inclusion-exclusion principle](/inclusion-exclusion-principle/) for the two-dimensional entries. For the last group you need the [Fenwick tree](/fenwick-tree/) from Volume 3 and, for the lower bound, the [cell-probe model](/cell-probe-model/) from Volume 1. The calculus group uses [finite differences](/finite-differences/), which are explained in Volume 12, but the entries define what they use.
