Two threads share a lock-free stack whose top node is $A$. The first thread reads $top = A$ and is about to read $A.next$. Before it can, the second thread pops $A$ and frees it. The first thread now reads freed memory, and if the allocator has already handed $A$ out again, its compare-and-swap on $top$ may even succeed against the wrong node. A lock would rule this out, because nobody frees a node while another thread holds the lock. A lock-free structure has no such moment, so it needs a separate rule for when an unlinked node may be freed. This chapter is about those rules.

Every scheme here answers the same question in a different way: how does the thread that retires a node learn that no other thread can still reach it? Reference counts ask each node. Hazard pointers ask each thread to publish the nodes it holds. Epochs and grace periods wait until every thread has finished the operations it was running. The answers differ in what a read of a node costs, how many retired nodes wait to be freed, and what happens when a thread stops in the middle of an operation and never comes back. The ERA theorem of Sheffi and Petrank shows that no scheme can be easy to add to a structure, robust to stopped threads and usable for every common structure, all at once.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **The problem.** The [use after free](/use-after-free/), the [ABA problem](/aba-problem/), the statement of [safe memory reclamation](/safe-memory-reclamation/) with its measures, and the retire-then-free pattern of [deferred reclamation](/deferred-reclamation/).
2. **Tags and type-stable pools.** [Tagged pointers](/tagged-pointers/) and [type-stable memory](/type-stable-memory/), which stop ABA without ever giving memory back.
3. **Grace periods.** The [quiescent state](/quiescent-state/), the [grace period](/grace-period/) and [read-copy-update](/read-copy-update/).
4. **Epochs.** [Epoch-based reclamation](/epoch-based-reclamation/), [quiescent-state-based reclamation](/quiescent-state-based-reclamation/) and [DEBRA](/debra/).
5. **Protecting pointers.** [Hazard pointers](/hazard-pointers/), [pass the buck](/pass-the-buck/) and [drop the anchor](/drop-the-anchor/).
6. **Eras and intervals.** [Hazard eras](/hazard-eras/) and [interval-based reclamation](/interval-based-reclamation/), which publish eras instead of pointers.
7. **Reference counts.** [Lock-free reference counting](/lock-free-reference-counting/) and [Hyaline](/hyaline/), which counts references to batches.
8. **Restarting readers.** [Optimistic access](/optimistic-access/) and [neutralization-based reclamation](/neutralization-based-reclamation/), which let threads read without protection and send them back to the root when a reclaimer needs them gone.

## A first reading

For a first reading, take these nine entries in order: [use after free](/use-after-free/), [the ABA problem](/aba-problem/), [safe memory reclamation](/safe-memory-reclamation/), [deferred reclamation](/deferred-reclamation/), [tagged pointers](/tagged-pointers/), [the grace period](/grace-period/), [epoch-based reclamation](/epoch-based-reclamation/), [hazard pointers](/hazard-pointers/) and [lock-free reference counting](/lock-free-reference-counting/). They give you the problem, the oldest fix, and the three basic answers: wait for a grace period, publish what you hold, or count references. Run the example of epoch-based reclamation and the example of hazard pointers by hand on the same stack $top \to A \to B$, and then stop one thread in the middle of a pop. Under epochs the garbage grows with every retire; under hazard pointers it stays at most $nR$. That one experiment explains most of the chapter.

Read-copy-update and QSBR come next if you work on read-mostly data or in a kernel. The remaining entries are refinements of the three answers, each trading a little of one measure for another. DEBRA, pass the buck, drop the anchor, Hyaline, optimistic access and neutralization-based reclamation come from research papers published between 2002 and 2021 and can wait. Type-stable memory matters mainly as a requirement of other schemes, so read it when an entry asks for it.

## Before you start

You need the [compare-and-swap](/compare-and-swap/) operation, [lock-freedom](/lock-freedom/) and [wait-freedom](/wait-freedom/), and the two structures used in almost every example, the [Treiber stack](/treiber-stack/) and the [Michael and Scott queue](/michael-scott-queue/). All of them are in Chapter 22.2. The entries on lists use the [Harris linked list](/harris-linked-list/) from the same chapter, and read-copy-update starts from the [readers-writers problem](/readers-writers-problem/) of Chapter 22.1.

From outside this volume, you need to know what a free list and reference counting are, as in any course on memory allocation. The proofs reason about interleavings on a sequentially consistent memory. Several entries mention store-load fences, which matter on real hardware, but no entry depends on a particular memory model.
