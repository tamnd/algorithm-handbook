A data structure is a way of laying out data in memory together with the operations that read and change it. The same set of numbers can sit in an array, in a linked list, in a search tree, in a hash table or in a heap, and each layout makes some operations fast and others slow. Choosing the structure is often the larger part of choosing the algorithm: [Dijkstra's algorithm](/dijkstra/) is the same few lines with a list, a [binary heap](/binary-heap/) or a [Fibonacci heap](/fibonacci-heap/), and its running time changes with each.

This volume starts with the plain sequences, arrays, linked lists, stacks and queues, the base of all the rest. Then come the dictionaries: hash tables, search trees and balanced search trees. Then the structures for one task each: heaps, disjoint sets, range queries, strings and space. The last five chapters change the rules: answers that may be slightly wrong, old versions that must stay readable, memory counted in bits, data on disk, and many threads at once.

## The ideas this volume teaches

Most structures in the volume use a few ideas:

- **An abstract type and its implementations.** A [stack](/stack/), a [queue](/queue/), a [dictionary](/dictionary/) and a [priority queue](/priority-queue/) are defined by their operations and the laws those operations obey. Each type has several implementations with different costs.
- **Contiguous or linked.** An [array](/array/) finds the item at position $i$ in $O(1)$ time but inserts in the middle in $\Theta(n)$. A [linked list](/linked-list/) inserts after a node it holds in $O(1)$ but needs $\Theta(i)$ steps to reach position $i$.
- **Amortized cost.** A [dynamic array](/dynamic-array/) sometimes copies all its items, yet a run of $m$ appends costs $O(m)$. Splay trees, Fibonacci heaps and union-find are analysed the same way, usually with the [potential method](/potential-method/).
- **Randomness.** A hash function drawn from a [universal family](/universal-hash-family/) makes collisions rare for every set of keys. Random priorities make a [treap](/treap/) balanced in expectation.
- **Balance by local repair.** A [search tree](/binary-search-tree/) answers in time proportional to its height. The [AVL tree](/avl-tree/) and the [red-black tree](/red-black-tree/) keep the height $O(\log n)$ by a few [rotations](/tree-rotation/) after each update.
- **Precompute for a query family.** A [segment tree](/segment-tree/), a [Fenwick tree](/fenwick-tree/) or a [sparse table](/sparse-table/) stores aggregates of chosen ranges so that every range query is answered from a few of them.
- **Sharing instead of copying.** [Path copying](/path-copying/) makes a new version of a tree by copying one root-to-leaf path and sharing the rest, so every old version stays valid.
- **The cost model decides.** On disk, the cost is the number of blocks moved, and a [B-tree](/b-tree/) with nodes the size of a block wins. In succinct structures it is the number of bits, and with threads it is waiting.

## The chapters

**Chapter 3.1, Linear structures**, is the foundation of the volume. It sets the [array](/array/) beside the [linked list](/linked-list/), defines the [stack](/stack/), the [queue](/queue/) and the [deque](/deque/), and shows how arrays grow ([dynamic array](/dynamic-array/)) and wrap around ([circular buffer](/circular-buffer/)). It ends with stacks at work, such as the [monotonic stack](/monotonic-stack/), and with the [move-to-front](/move-to-front-heuristic/) rule.

**Chapter 3.2, Hashing**, builds the [hash table](/hash-table/): [hash functions](/hash-function/), collision resolution by [separate chaining](/separate-chaining/) and [open addressing](/open-addressing/). [Universal hashing](/universal-hashing/) gives expected bounds for every input, [cuckoo hashing](/cuckoo-hashing/) gives worst-case constant lookups, and [perfect hashing](/perfect-hashing/) stores a fixed set with no collisions.

**Chapter 3.3, Search trees**, introduces the [binary search tree](/binary-search-tree/) and the operations of an [ordered set](/ordered-set/): search, insert, delete, floor, ceiling and rank. It studies random trees and the [optimal static tree](/optimal-bst-dynamic-programming/), then turns to the [splay tree](/splay-tree/) and the [skip list](/skip-list/), which reach logarithmic cost without explicit balance rules.

**Chapter 3.4, Balanced trees**, gives the rules that keep a search tree of height $O(\log n)$: the [AVL tree](/avl-tree/), the [red-black tree](/red-black-tree/) and its source, the [2-3-4 tree](/two-three-four-tree/), the randomized [treap](/treap/), and newer designs such as the [scapegoat tree](/scapegoat-tree/) and the [WAVL tree](/wavl-tree/).

**Chapter 3.5, Heaps**, implements the [priority queue](/priority-queue/). The [binary heap](/binary-heap/) gives every operation in $O(\log n)$ time inside an array. The [binomial heap](/binomial-heap/), [pairing heap](/pairing-heap/) and [Fibonacci heap](/fibonacci-heap/) add fast melding and fast decrease-key, which speeds up shortest paths and minimum spanning trees.

**Chapter 3.6, Disjoint sets**, keeps a partition of $n$ elements under union and find. With [union by rank](/union-by-rank/) and [path compression](/path-compression/), $m$ operations take $O(m\,\alpha(n))$ time, where $\alpha$ is the inverse Ackermann function, and [Tarjan's bound](/union-find-amortized-bound/) shows that this algorithm can do no better.

**Chapter 3.7, Range query structures**, answers questions about a range of an array, such as its sum or minimum, while the array changes. The [Fenwick tree](/fenwick-tree/) and the [segment tree](/segment-tree/) take $O(\log n)$ per operation, the [sparse table](/sparse-table/) answers a static minimum in $O(1)$, and [Mo's algorithm](/mo-algorithm/) reorders offline queries.

**Chapter 3.8, String structures**, stores sets of strings so that searches cost time in proportion to the length of the key. It covers the [trie](/trie/), the [radix tree](/radix-tree/) and the [ternary search tree](/ternary-search-tree/), the [rope](/rope/) for editing long texts, and suffix structures.

**Chapter 3.9, Spatial structures**, indexes points and shapes in two or more dimensions: the [k-d tree](/kd-tree/), the [quadtree](/quadtree/) family, the [R-tree](/r-tree/) and its variants for databases, and [space-filling curves](/space-filling-curve/) that map the plane to a line.

**Chapter 3.10, Probabilistic structures**, trades exact answers for space. The [Bloom filter](/bloom-filter/) and its successors answer membership with a small, controlled rate of false positives, and sketches such as [Flajolet-Martin](/flajolet-martin-sketch/) and count-min estimate counts in a stream.

**Chapter 3.11, Persistent structures**, keeps every past version of a structure. It covers [path copying](/path-copying/), the [fat node](/fat-node/) and [node copying](/node-copying/) methods, the [theorem of Driscoll, Sarnak, Sleator and Tarjan](/dsst-persistence-theorem/), and the purely functional structures of functional languages, such as the [banker's queue](/banker-queue/) and the [finger tree](/finger-tree/).

**Chapter 3.12, Succinct structures**, stores objects in space close to the information-theoretic minimum and still answers queries fast. Its base is the [bit vector](/bit-vector/) with [rank and select](/rank-select-problem/), on which trees in $2n + o(n)$ bits and the [wavelet tree](/wavelet-tree/) are built.

**Chapter 3.13, External memory structures**, counts block transfers between a fast small memory and a slow large one. The [B-tree](/b-tree/) and the [B+ tree](/b-plus-tree/) are the indexes of databases and file systems; the [buffer tree](/buffer-tree/), the [B^ε-tree](/b-epsilon-tree/) and the [LSM tree](/log-structured-merge-tree/) make writes cheap; [cache-oblivious](/cache-oblivious-b-tree/) layouts work for every block size at once.

**Chapter 3.14, Concurrent structures**, lets many threads use one structure. It starts with the [concurrent queue](/concurrent-queue/) and the [two-lock queue](/two-lock-queue/), then treats hash tables, counters, trees and priority queues that limit waiting.

## How to read this volume

If this is your first course, read these entries in this order. From Chapter 3.1: [array](/array/), [linked list](/linked-list/), [stack](/stack/), [queue](/queue/), [dynamic array](/dynamic-array/) and [circular buffer](/circular-buffer/). From Chapter 3.2: [hash function](/hash-function/), [hash table](/hash-table/), [separate chaining](/separate-chaining/), [linear probing](/linear-probing/) and [universal hashing](/universal-hashing/). From Chapter 3.3: [binary search tree](/binary-search-tree/) and [BST deletion](/bst-deletion/). From Chapter 3.4: [tree rotation](/tree-rotation/), [AVL tree](/avl-tree/) and [red-black tree](/red-black-tree/). From Chapter 3.5: [priority queue](/priority-queue/) and [binary heap](/binary-heap/). From Chapter 3.6: [disjoint-set forest](/disjoint-set-forest/) and [path compression](/path-compression/). From Chapter 3.7: [Fenwick tree](/fenwick-tree/) and [segment tree](/segment-tree/). From Chapter 3.8: [trie](/trie/). From Chapter 3.10: [Bloom filter](/bloom-filter/). With the ◦ and • exercises of these chapters, that is a complete first unit on data structures.

Chapter 3.1 comes first: every later chapter uses its arrays, linked nodes and resizing. Chapters 3.2 to 3.5 are the core, best read in order. Chapters 3.6 to 3.10 depend on the core but hardly on each other, and Chapters 3.11 to 3.14 each add a new cost model. Each chapter's opening names its groups and their order, and the entries marked *Advanced* and *Research* go deeper.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too, such as the [potential method](/potential-method/) in Volume 1 and [binary search](/binary-search/) in Volume 5.

## What you need first

You should be able to read a short program and follow a proof by induction. From Volume 1 you need [asymptotic notation](/asymptotic-notation/), the [random-access machine](/random-access-machine/), [loop invariants](/loop-invariant/), [amortized cost](/amortized-cost/) with the [potential method](/potential-method/), and, for hashing and the randomized structures, [linearity of expectation](/linearity-of-expectation/). The [external memory model](/external-memory-model/), the [cache-oblivious model](/cache-oblivious-model/) and the [cell-probe model](/cell-probe-model/) of Volume 1 are needed only for the chapters and lower bounds that use them. From Volume 5 you need [binary search](/binary-search/), and from Volume 7 the vocabulary of [rooted trees](/rooted-tree/) and [binary trees](/binary-tree/). Chapter 3.14 assumes the basic ideas of shared-memory concurrency: threads, locks and atomic instructions such as compare-and-swap.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
