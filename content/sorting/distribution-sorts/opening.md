A comparison sort never looks inside a key, and so it needs about $n \lg n$ comparisons. A distribution sort does look inside. It reads a digit, a character, or the value of the key itself, and uses it as an array index to send the item to a bucket. One such step costs $O(1)$ per item and does work that a comparison cannot do, so the $\Omega(n \log n)$ [lower bound](/comparison-sort-lower-bound/) does not apply. On keys of the right kind these sorts run in linear time.

The right kind is common. A database sorts 32-bit integer keys and hash values. A graphics program sorts points by an integer depth code. A suffix array construction sorts pairs of integer ranks in every round. A text index sorts millions of words and URLs that share long prefixes. In each of these, a [radix sort](/radix-sort/) or a string sort beats the best comparison sort, often by a wide margin.

The price is generality. A distribution sort must know something about its keys: that they are integers in a small range, that they have digits, that they are spread evenly over an interval. When the assumption fails, the sort becomes slow or wrong. Much of this chapter is about what each method assumes and what it costs when the assumption is false.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Sorting by the value of the key.** The idea of a [distribution sort](/distribution-sort/), the [integer sorting](/integer-sorting/) problem, and the two simplest methods. [Counting sort](/counting-sort/) counts the keys of each value and turns the counts into positions with a prefix sum; it is stable and takes $\Theta(n + k)$ time for keys in $\{0, \ldots, k-1\}$. [Pigeonhole sort](/pigeonhole-sort/) puts the items in one list per value.
2. **Radix sort.** [LSD radix sort](/radix-sort/) sorts large keys one digit at a time, from the least significant digit up, with a stable counting sort for each digit. It takes $\Theta(d(n + b))$ time for $d$ digits in base $b$, and the [time bound](/radix-sort-time-bound/) says how to choose $b$.
3. **Bucket sort and random keys.** [Bucket sort](/bucket-sort/) cuts an interval into $n$ buckets. Under the [uniform input model](/uniform-input-model/) its expected time is $\Theta(n)$, and in the worst case it is $\Theta(n^2)$.
4. **Strings, from the first character.** [String sorting](/string-sorting/) counts characters read. [MSD radix sort](/msd-radix-sort/) reads each string only up to its distinguishing prefix. [American flag sort](/american-flag-sort/) does the same in place, and [radix exchange sort](/radix-exchange-sort/) works on bits.
5. **Radix quicksort and tries.** [Multikey quicksort](/multikey-quicksort/) partitions three ways on one character and runs in $O(n \log n + D)$ expected time, which is optimal over an alphabet that can only be compared. [Burstsort](/burstsort/) uses a trie of buckets to make good use of the cache.
6. **Engineered distribution sorts.** [Flashsort](/flashsort/), [proxmap sort](/proxmap-sort/) and [spreadsort](/spreadsort/) combine a linear map, a counting pass and a comparison sort for the remaining work.
7. **How fast can integers be sorted.** [Han's algorithm](/han-integer-sort/) sorts $n$ word-sized integers in $O(n \log \log n)$ time, and the randomized [Han-Thorup algorithm](/han-thorup-integer-sort/) in $O(n \sqrt{\log \log n})$ expected time.

## A first reading

For a first reading, take these nine entries in order: [distribution sort](/distribution-sort/), [counting sort](/counting-sort/), [radix sort](/radix-sort/), [the radix sort time bound](/radix-sort-time-bound/), [the uniform input model](/uniform-input-model/), [bucket sort](/bucket-sort/), [string sorting](/string-sorting/), [MSD radix sort](/msd-radix-sort/) and [three-way radix quicksort](/three-way-radix-quicksort/). Counting sort and radix sort are the ones to know well: they are short, they appear inside many other algorithms, and the proof that radix sort works shows why stability matters. Leave the engineered sorts and the two research entries for later. The proof of [bucket sort's expected time](/bucket-sort-expected-linear/) is a good first exercise with indicator variables; read it when you meet them.

## Before you start

You need [stable sorting](/stable-sort/), [insertion sort](/insertion-sort/), [quicksort](/quicksort/) and [three-way quicksort](/three-way-quicksort/) from Chapter 4.1. From Volume 1 you need [asymptotic notation](/asymptotic-notation/), the [word RAM](/word-ram/) as the machine model, and for bucket sort the [uniform distribution](/uniform-distribution/), [indicator random variables](/indicator-random-variable/) and [linearity of expectation](/linearity-of-expectation/). Counting sort uses [prefix sums](/prefix-sums/), radix sort uses [positional number systems](/positional-number-system/), and the string sorts use [lexicographic order](/lexicographic-order/). Burstsort is built on the [trie](/trie/) of Volume 3.
