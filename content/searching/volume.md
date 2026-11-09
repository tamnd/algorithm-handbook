To search is to find an item in a collection, or a value with some property, or to learn that there is none. It is the most common thing a program does with data it has stored. A database looks up a row by its key. A compiler looks up a name in its symbol table. A version control tool searches its history for the first commit that broke a test. A chess program asks whether it has seen a position before. A search engine looks for pages that are nearly the same as one it has just fetched, and a system built on text embeddings looks for the passages whose vectors are nearest to a question.

This volume collects the methods for these tasks. It starts with the scan and with binary search on a sorted array, then turns binary search from arrays to answers: a search over the values of a parameter, guided by a yes-or-no test. Then come hashing, which finds a key in constant expected time by computing where it should be; fractional cascading, which finds one key in many sorted lists at once; and similarity search, which asks not for an equal key but for the nearest ones.

## Why searching gets a volume of its own

Searching is where the cost of an algorithm depends most clearly on what is known about the data. The same question costs $n$ steps on an unordered array, $\lg n$ on a sorted one, and a constant on a hash table, and each step down needs more preparation. In this one volume you will meet:

- **Invariants that make code correct.** [Binary search](/binary-search/) is short and easy to get wrong. Its half-open range and loop invariant are the model for many other loops.
- **Lower bounds.** The [search lower bound](/search-lower-bound/) shows that no comparison method beats binary search, and the same decision-tree argument returns in other volumes.
- **Searching for an answer instead of an item.** [Binary search on the answer](/binary-search-on-answer/) solves an optimization problem with a [monotone](/monotone-predicate/) yes-or-no test. [Ternary search](/ternary-search/) and [golden-section search](/golden-section-search/) find the peak of a unimodal function, and [parametric search](/parametric-search/) runs a test algorithm on an unknown value.
- **Probability as a design tool.** [Universal hashing](/universal-hashing-lemma/) gives constant expected search time for every set of keys, because the randomness is in the choice of the function and not in the input.
- **Sharing work between searches.** [Fractional cascading](/fractional-cascading-bridge/) copies a fraction of each list into its neighbor, so that after one binary search each further list costs a constant.
- **Approximation.** In high dimensions no exact method for nearest neighbors is much faster than the scan. [Locality-sensitive hashing](/locality-sensitive-hashing/) and graph indexes such as [HNSW](/hnsw/) give up a little accuracy to answer in far less time.

## The chapters

**Chapter 5.1, Sequential and binary search**, is the base of the volume. It covers [linear search](/linear-search/) and its refinements, binary search with its boundary forms, [exponential search](/exponential-search/) and [interpolation search](/interpolation-search/), halving on rotated arrays and sorted matrices, the lower bound of $\lceil \lg(n+1) \rceil$ comparisons, and the layouts that make binary search fast on a real processor.

**Chapter 5.2, Search on answers**, searches over the possible values of the answer instead of over stored items. A monotone test turns an optimization problem into a binary search. Unimodal functions are searched by ternary, Fibonacci and golden-section search, ratios are optimized by [Dinkelbach's method](/dinkelbach-algorithm/), and the chapter ends with parallel binary search and parametric search.

**Chapter 5.3, Hashing search**, studies the cost of a search in a hash table. It starts with direct addressing and [perfect hashing](/perfect-hash-function/), then gives the expected search time of [chaining](/chaining-expected-search-time/) and of [open addressing](/open-addressing-expected-probes/), with the clustering that makes linear probing slower at high load. It ends with [Zobrist hashing](/zobrist-hashing/) for game positions and with tables that grow.

**Chapter 5.4, Fractional cascading**, solves one problem: find the place of the same key in many sorted lists. The bridges between the lists cut the cost from $O(k \log n)$ to $O(\log n + k)$. The chapter also covers updates and the lower bound that stops the idea from extending to planar maps.

**Chapter 5.5, Similarity search**, is the largest chapter. It defines [metric spaces](/metric-space/) and the similarities of vectors and sets, states the [nearest neighbor](/nearest-neighbor-search/) and range problems, and covers the exact metric trees, locality-sensitive hashing, the [MinHash](/minhash/) and SimHash sketches, exact similarity joins, the graph indexes behind modern vector search, and compressed vectors.

## How to read this volume

If this is your first course, read these entries in this order: [linear search](/linear-search/), [binary search](/binary-search/), the [lower bound query](/lower-bound-query/), [exponential search](/exponential-search/) and the [search lower bound](/search-lower-bound/) in Chapter 5.1; [monotone predicate](/monotone-predicate/), [binary search on the answer](/binary-search-on-answer/) and [ternary search](/ternary-search/) in Chapter 5.2; [simple uniform hashing](/simple-uniform-hashing/), the [expected search time of chaining](/chaining-expected-search-time/) and [primary clustering](/primary-clustering/) in Chapter 5.3; and [nearest neighbor search](/nearest-neighbor-search/), the [vantage-point tree](/vantage-point-tree/), [locality-sensitive hashing](/locality-sensitive-hashing/) and [MinHash](/minhash/) in Chapter 5.5. Do the exercises marked ◦ and • at the end of these chapters. That is a complete first unit on searching. Fractional cascading can wait until you meet range trees and segment trees.

If you already know binary search and hash tables, start with the opening page of each chapter. It names the groups in the chapter and the order to read them. The entries marked *Advanced* and *Research* in each chapter are the place to go deeper.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to read a short program and follow a proof by induction. From Volume 1 you need [asymptotic notation](/asymptotic-notation/), [loop invariants](/loop-invariant/), the [comparison model](/comparison-model/) and, for hashing and the randomized methods, [expected values](/expected-value/) and [linearity of expectation](/linearity-of-expectation/). From Volume 3 you need [arrays](/array/), [hash tables](/hash-table/), the [binary heap](/binary-heap/) and [binary search trees](/binary-search-tree/). Chapter 5.5 also uses the [Euclidean distance](/euclidean-distance/), the [dot product](/dot-product/) and the [edit distance](/edit-distance/), which its opening page points to. Nothing else is assumed.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
