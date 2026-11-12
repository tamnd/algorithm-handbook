A program asks for blocks of many sizes and frees them in an order no one can predict. The allocator behind `malloc` and `free` must answer each request at once and may not move a block once it has handed it out. It pays in two currencies: time per request, and memory wasted. Waste comes in two forms. Internal fragmentation is space lost inside a block, as when a request for 33 bytes is rounded up to 48. External fragmentation is free memory broken into pieces too small for the next request.

Robson showed that every online allocator can be forced by some sequence of requests to use more memory than the live data by a factor that grows with the logarithm of the ratio between the largest and the smallest block. Even when all lifetimes are known in advance, the best placement is NP-hard to find. So allocators are judged on real programs, and the good ones exploit how programs behave: most requests are small, a few sizes dominate, and many objects of one size are created and freed together.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The problem.** The allocator interface, internal and external fragmentation, the online and offline problems, Robson's bound, and Knuth's fifty-percent rule.
2. **Free lists and fits.** Free lists, boundary tags, immediate and deferred coalescing, and the sequential fits: first, next, best and worst fit.
3. **Size classes and buddies.** Size classes and segregated free lists, the buddy system with its Fibonacci and lazy variants, bitmap allocators, and TLSF, which allocates and frees in constant time for real-time systems.
4. **Allocation without general free.** Stack and bump-pointer allocation, arenas and regions, memory pools, the slab allocator, and compaction.
5. **Allocators in practice.** dlmalloc and the multithreaded allocators Hoard, tcmalloc, jemalloc and mimalloc, with thread-local buffers and lock-free allocation.

## What to read meanwhile

A free list is a [linked list](/linked-list/) threaded through the free blocks, often a [doubly linked list](/doubly-linked-list/) with a [sentinel node](/sentinel-node/), and a bitmap allocator is a [bit vector](/bit-vector/); all are in Volume 3. The fits share their names and greedy rules with [bin packing](/bin-packing/) in Chapter 18.1: compare [first fit](/first-fit-bin-packing/), [best fit](/best-fit-bin-packing/) and [next fit](/next-fit-bin-packing/). The difference is that items in a bin never leave, while blocks in a heap are freed and leave holes.

For why an allocator that keeps related objects close is faster, read the [memory hierarchy](/memory-hierarchy/) entry of Volume 1. Concurrent allocators meet the problems of Chapter 22.3: start with [safe memory reclamation](/safe-memory-reclamation/), [type-stable memory](/type-stable-memory/) and [compare-and-swap](/compare-and-swap/). Freeing memory without an explicit call is the subject of the next chapter, on garbage collection.
