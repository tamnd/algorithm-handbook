Freeing heap memory by hand leads to two kinds of bugs: memory freed too early and then used through a dangling pointer, and memory never freed at all. A garbage collector removes both. It treats the heap as a directed graph whose vertices are objects and whose edges are pointers, and it frees every object that no path from the roots reaches; the roots are the stacks, the registers and the global variables. Java, C#, Go, JavaScript and most functional languages depend on one.

Two families of methods divide the field. A tracing collector finds the live objects by a graph search from the roots and reclaims everything else. Reference counting keeps a count of incoming pointers in each object and frees the object when the count drops to zero, but it cannot free a cycle by itself. Every design trades three costs against each other: total time, extra memory, and the length of the pauses the program sees. A copying collector does work proportional to the live data only, but keeps half its space empty. A generational collector uses the observation that most objects die young. A concurrent collector runs beside the program and needs a barrier on pointer writes or reads to stay correct.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Garbage and reachability.** Roots, reachability, the mutator and the collector, precise and conservative collection, and stop-the-world collection.
2. **Tracing.** Mark-and-sweep with lazy sweeping and Schorr-Waite marking in constant extra space, copying with Cheney's breadth-first scan, mark-compact with the two-finger and Lisp 2 algorithms, and the trade of heap size against collection time.
3. **Reference counting.** Deferred and weighted reference counting, and cycle collection by trial deletion.
4. **Generations.** The generational hypothesis, remembered sets and card marking, the train algorithm, and Beltway.
5. **Incremental and concurrent collection.** Tricolor marking, incremental-update and snapshot-at-the-beginning write barriers, read barriers, Baker's real-time collector, parallel and on-the-fly collection, and production collectors: Boehm-Demers-Weiser, Immix, Garbage-First, Shenandoah, ZGC and C4.
6. **Weak references and finalization.** References that do not keep an object alive, ephemerons, and code run when an object dies.

## What to read meanwhile

Tracing is graph search. Read [graph reachability](/graph-reachability/), [depth-first search](/depth-first-search/) and [breadth-first search](/breadth-first-search/) in Volume 7; Cheney's collector is breadth-first search that uses the copied objects as its queue.

Chapter 22.3 solves a close problem: when a lock-free data structure removes a node, when may it be freed? [Safe memory reclamation](/safe-memory-reclamation/) states the problem, and [hazard pointers](/hazard-pointers/), [epoch-based reclamation](/epoch-based-reclamation/) and [lock-free reference counting](/lock-free-reference-counting/) answer it without tracing the heap. The barriers of concurrent collectors rest on the atomic operations of Chapter 22.2, such as [compare-and-swap](/compare-and-swap/).
