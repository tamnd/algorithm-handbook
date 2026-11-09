A hospital emergency room does not treat patients in the order they arrive. Each patient gets a priority, and the next one seen is the most urgent of those waiting. A shortest-path program works the same way: of all the vertices it has reached, it next settles the one nearest to the source. Both need a [priority queue](/priority-queue/), a store that takes items with keys and always gives back the one with the smallest key.

A sorted list would do, but each insert would cost linear time. A heap does less work. It keeps the items in a tree in which every parent has a key at most those of its children. That rule, the [heap property](/heap-property/), says nothing about two siblings or two cousins, so the tree is far from sorted. Yet it puts a smallest key at the root, and after an insert or a removal it can be repaired along one path from the root to a leaf. In the [binary heap](/binary-heap/) the tree is complete and lives in an array, the children of position $i$ are at $2i$ and $2i + 1$, and each path has $\lfloor \lg n \rfloor$ edges. So insert and extract-min cost $O(\log n)$ with no pointers at all.

Most of the chapter is about what else a heap can be asked to do, and what each extra operation costs. Lowering a key, merging two heaps, serving both ends, or keys that are small integers each lead to a different structure. The table in the summary puts the main ones side by side.

## What the chapter covers

The chapter is in nine groups, read in order.

1. **The type and the order.** The [priority queue](/priority-queue/) as an abstract type, the [heap property](/heap-property/), and the idea of a [heap](/heap/) as a set of heap-ordered trees.
2. **The binary heap.** [Sift-up](/sift-up/) and [sift-down](/sift-down/), the [binary heap](/binary-heap/) built from them, and the operations that change or remove one key: extract-max, increase-key, [decrease-key](/decrease-key/) and [delete](/heap-delete/).
3. **Building a heap.** [Floyd's method](/floyd-heap-construction/) builds a heap of $n$ keys in $\Theta(n)$ time, where [repeated insertion](/heap-construction-by-insertion/) takes $\Theta(n \log n)$ in the worst case.
4. **Array heaps at work.** The [d-ary heap](/d-ary-heap/), the [indexed priority queue](/indexed-priority-queue/), the [top M](/top-m-problem/) items of a stream, the [tournament tree](/tournament-tree/) and the [weak heap](/weak-heap/).
5. **Both ends at once.** The [double-ended priority queue](/double-ended-priority-queue/) and three array heaps for it: the [min-max heap](/min-max-heap/), the [deap](/deap/) and the [interval heap](/interval-heap/).
6. **Heaps that merge.** The [leftist](/leftist-heap/), [skew](/skew-heap/), [randomized](/randomized-heap/), [binomial](/binomial-heap/) and [pairing](/pairing-heap/) heaps, all made of linked trees. Each melds two heaps in $O(\log n)$ time or less, in the worst case, amortized or expected.
7. **Small integer keys.** The [bucket queue](/bucket-queue/), the [radix heap](/radix-heap/) and the [calendar queue](/calendar-queue/), which index by the key itself.
8. **Fast decrease-key.** The [Fibonacci heap](/fibonacci-heap/) and the heaps that came after it, from the [rank-pairing heap](/rank-pairing-heap/), which gets the same bounds with a simpler structure, to the [Brodal queue](/brodal-queue/), whose bounds hold in the worst case.
9. **Beyond the exact heap.** The [soft heap](/soft-heap/), which may raise a few keys on purpose, and the [kinetic heap](/kinetic-heap/), whose keys move with time.

## A first reading

For a first reading, take these eleven entries in order: [priority queue](/priority-queue/), [heap property](/heap-property/), [sift-up](/sift-up/), [sift-down](/sift-down/), [binary heap](/binary-heap/), [decrease-key](/decrease-key/), [Floyd's heap construction](/floyd-heap-construction/), [d-ary heap](/d-ary-heap/), [indexed priority queue](/indexed-priority-queue/), [leftist heap](/leftist-heap/) and [binomial heap](/binomial-heap/). Then read the [Fibonacci heap](/fibonacci-heap/) if you need its bound for a graph algorithm. The proof that Floyd's method is linear is short and worth knowing well. Group 5 can wait until you need both ends, and groups 8 and 9 are research material: the entries there are worth a look for their ideas, but no ordinary program needs them.

## Before you start

You need [asymptotic notation](/asymptotic-notation/) and [loop invariants](/loop-invariant/) from Volume 1, and, for the array layout, the [complete binary tree](/complete-binary-tree/) of Volume 7. The amortized bounds of groups 6 and 8 use [amortized cost](/amortized-cost/) and the [potential method](/potential-method/), also from Volume 1. The [queue](/queue/) of Chapter 3.1 is the type that the priority queue changes. The uses come from other volumes: [heapsort](/heapsort/) in Volume 4, and [Dijkstra's algorithm](/dijkstra/) and [Prim's algorithm](/prim/) in Volume 7. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
