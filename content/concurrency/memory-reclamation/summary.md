## What to remember

- Freeing an unlinked node at once causes a [use after free](/use-after-free/), and reusing its address causes the [ABA problem](/aba-problem/). If $n$ threads may each stop while holding $K$ nodes, any safe scheme keeps at least $nK$ retired nodes in the worst case.
- A [tagged pointer](/tagged-pointers/) with a $w$-bit tag fails only if the word changes a multiple of $2^w$ times between a read and its compare-and-swap. It needs [type-stable](/type-stable-memory/) nodes.
- After a [grace period](/grace-period/), every node removed before it began can be freed. [Epoch-based reclamation](/epoch-based-reclamation/) frees a node with tag $r$ once the epoch reaches $r + 2$; one step is not enough. Reads are free, but a thread stopped in an operation that announced $e$ keeps the epoch at most $e + 1$ forever.
- [Hazard pointers](/hazard-pointers/) cost a write, a fence and a re-read per node read. With $R = 2nK$, a scan frees at least $R - nK$ nodes, and at most $nR = O(n^2 K)$ nodes wait, even when threads stop.
- [Hazard eras](/hazard-eras/) and [interval-based reclamation](/interval-based-reclamation/) write only when the clock moved. Their bounds, $n(R + nKL)$ and $n(R + nL)$, depend on $L$, the nodes alive in one era or interval.
- [Lock-free reference counting](/lock-free-reference-counting/) frees at once but costs a fetch-and-add per read, never frees cycles and is not robust. [Hyaline](/hyaline/) counts references to batches of $n + 1$ nodes instead.
- [Optimistic access](/optimistic-access/), [neutralization-based reclamation](/neutralization-based-reclamation/) and DEBRA+ combine cheap reads with bounded garbage, such as $nR$ for $R > nK$, at the price of read phases that can restart at any point.
- By the ERA theorem, no scheme is easy to integrate, robust and widely applicable at once. Epochs give up robustness, hazard pointers applicability, and restart schemes ease of integration.

## The schemes side by side

| Scheme | Extra cost per node read | Unfreed nodes | A stopped thread holds | Progress |
|---|---|---|---|---|
| [Reference counts](/lock-free-reference-counting/) | fetch-and-add on the node, re-read | no bound | all reachable from its nodes | read lock-free |
| [Hazard pointers](/hazard-pointers/) | write, fence, re-read | $nR$, $R > nK$ | $K$ nodes and its list | read lock-free, scan wait-free |
| [Pass the buck](/pass-the-buck/) | write, check read | $n(R + G) + G$, $G = nK$ | one value per guard | read lock-free, Liberate wait-free |
| [Drop the anchor](/drop-the-anchor/) | anchor write and check per $K$ nodes | $nR$, $R > n(K + 1)$ | $K + 1$ nodes | queue stays lock-free |
| [Epochs](/epoch-based-reclamation/) | none; a fence per operation | no bound | all later retires | BEGIN lock-free, rest wait-free |
| [QSBR](/quiescent-state-based-reclamation/) | none | no bound | all later retires | wait-free |
| [RCU](/read-copy-update/) | none, or private-word writes | no bound with call_rcu | all later versions | readers never wait; synchronize blocks |
| [DEBRA](/debra/), DEBRA+ | none | no bound; $n(T + 3(n + 1) + 3nK)$ | all; bounded with signals | $O(1)$ steps per operation |
| [Hazard eras](/hazard-eras/) | clock read; write and fence if it moved | $n(R + nKL)$ | $KL$ nodes | read lock-free, scan wait-free |
| [IBR](/interval-based-reclamation/) | epoch read; write and fence if it moved | $n(R + nL)$ | nodes meeting its interval | read lock-free, scan wait-free |
| [Hyaline-1](/hyaline/), -1S | none; era read in -1S | no bound; bounded | all; $(n + 1)B$ | ENTER, LEAVE wait-free; RETIRE lock-free |
| [Optimistic access](/optimistic-access/) | warning-bit read, no fence | $nR$, $R > nK$ | $K$ nodes | $n$ restarts per $R$ retires |
| [NBR](/neutralization-based-reclamation/) | none; $K$ writes per write phase | $nR$, $R > nK$ | $K$ nodes | structure stays lock-free |

: The schemes of the chapter, with a thread allowed to stop inside an operation. $n$ counts threads, $K$ pointers per thread, $R$ the retire list length that starts a scan, $T$ the bag size that starts neutralization, $L$ the nodes alive in one era or interval, $B$ the nodes born up to a stopped thread's era.

## Choosing a method

For read-mostly data in a program that controls its threads, use [QSBR](/quiescent-state-based-reclamation/) if threads have natural quiescent points, such as the end of a request, and [epochs](/epoch-based-reclamation/) otherwise. Both stop reclaiming while a thread blocks inside an operation.

In a library whose callers may be preempted, use a robust scheme: [hazard pointers](/hazard-pointers/) when an operation touches few nodes, as in stacks and queues. For long traversals, [hazard eras](/hazard-eras/) and [IBR](/interval-based-reclamation/) remove most writes, and [NBR](/neutralization-based-reclamation/) all of them if the read phase can restart.

Use [reference counting](/lock-free-reference-counting/) when nodes must go back at once and there are no cycles, and [tagged pointers](/tagged-pointers/) with at least 32 bits of tag when memory never needs to shrink.
