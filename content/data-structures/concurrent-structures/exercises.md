1. ◦ For each history, say whether it is linearizable, [sequentially consistent](/sequential-consistency/) and [quiescently consistent](/quiescent-consistency/). (a) A queue, empty. $A$ calls enq$(x)$, which returns; then, with nothing pending, $B$ calls deq() and gets EMPTY. (b) A counter at 0. $A$ invokes getAndIncrement() and stays pending. Meanwhile $B$ calls and gets 2, and after $B$ has returned, $C$ calls and gets 0. Then $A$ returns 1. (c) A queue, empty. $A$'s enq$(x)$ and $B$'s enq$(y)$ overlap in time. After both have returned, $C$ calls deq() and gets $y$.

2. ◦ Two registers $x = y = 0$. Thread 1 runs $x \leftarrow 1$; $y \leftarrow 1$. Thread 2 runs $r_1 \leftarrow y$; $r_2 \leftarrow x$. List the outcomes $(r_1, r_2)$ that sequential consistency allows, and the one it forbids.

3. ◦ A [concurrent hash table](/concurrent-hash-table/) has $L = 4$ locks, capacity 8 and $h(k) = k$. For the keys 3, 7, 12, 14, 21 and 30, give the bucket and the lock of each. Which of the six puts can run at the same time as a put of 7? Give the buckets after the capacity doubles to 16, and check that no key changes its lock.

4. ◦ A [sloppy counter](/sloppy-counter/) has $p = 4$ cores and threshold $S = 5$, and starts at 0. Core 0 increments 7 times, core 1 4 times, core 2 12 times and core 3 3 times, with no reads in between. Give the local counts and the global count at the end, the value of an approximate read, its error, and the number of times the global lock was taken. Compare the error with the bound $p(S - 1)$.

5. ◦ A [Disruptor](/disruptor-ring-buffer/) ring has $N = 8$ slots, one producer, consumer $A$ and consumer $B$ that depends on $A$. The cursor is 12, $A.seq = 9$ and $B.seq = 4$. The producer claims sequence 13. Can it publish now? Which events does $B$ take in its next batch? After that batch, up to which sequence can the producer publish without waiting, and in which slot does that last event go?

6. ◦ The [fine-grained concurrent heap](/fine-grained-concurrent-heap/) fills the slots in the order $rev(1), rev(2), \ldots$. Give $rev(n)$ for $n = 1, \ldots, 15$, and the slot of the 11th item. Then insert 3, 8, 1, 6, 2, one at a time, into an empty heap, and give the slots. Finally do one delete-min alone, and give the item it returns and the slots after it.

7. ◦ A [diffracting tree](/diffracting-tree/) has width 4, all toggles at 0 and all wire counters at 0. Six tokens pass one after another, and none finds a partner in a prism. Give the wire and the value of each. Then tokens with ids 3 and 8 meet in the root's prism, and each finds no partner below the root; after them a token with id 2 passes alone. Give the three values, and check that the nine values are $0, \ldots, 8$.

8. ◦ In a one-lock [concurrent queue](/concurrent-queue/) each critical section takes 50 ns. What is the largest number of calls per second, whatever the number of threads? With a fair ticket lock and $p = 8$ threads, how long can one call wait for the lock? For the [two-lock queue](/two-lock-queue/) with the same critical sections, give the largest number of calls per second when half the calls are enqueues, and when 90% are enqueues.

9. • A [combining tree](/combining-tree/) of width 4 has a root and two leaves. Threads $A$ (id 0) and $B$ (id 1) share leaf 0, and $C$ (id 2) and $D$ (id 3) share leaf 1. The counter is 0. All four precombine in the order $A, B, C, D$, then $B$ and $D$ deposit, then $A$ and $C$ combine, and $C$ reaches the root before $A$. Give the value that each thread returns, the number of steps at the root, and a linearization order.

10. • A [combining funnel](/combining-funnel/) sits in front of a counter that holds 10. Threads $A$, $B$, $C$, $D$ add 1, 2, 3 and 4. On layer 0, $B$ captures $A$ and $D$ captures $C$; on layer 1, $D$ captures $B$. A captured thread gets as offset its capturer's sum just before the capture. Give each thread's sum, the single fetch-and-add on the counter, the value each thread returns, and the order in which the calls are linearized.

11. • A two-lock queue is empty: only the sentinel $s$. Thread $A$ calls enq(1) and stops right after line L3, holding the tail lock. Thread $B$ calls deq(). Thread $C$ calls enq(2). Then $A$ resumes. Say which thread waits for which, what $B$ returns, where head and tail point after each call returns, and give the linearization points.

12. • An [LCRQ](/lcrq/) starts with one ring of $R = 4$ cells. Alone, one call after another, enqueue $a, b, c, d$, dequeue twice, then enqueue $e, f, g$, then dequeue until EMPTY. Say which ticket and cell each call uses, which enqueue closes the ring and why, where $g$ goes, and in which order the items come out. What is the head counter of the first ring at the end?

13. • A [Ctrie](/ctrie/) uses $W = 2$, 4-bit hashes and $hash(k) = k$, with the low two bits as the first group. Insert 5, 1, 9, 13 and 2. Draw the trie with the bitmaps of the C-nodes, and find the position of the branch of key 2 in the root by population count. How many I-nodes does a lookup of 13 read? Then remove 1, 9 and 13, and give the trie after the tomb is cleaned.

14. • A [B-link tree](/blink-tree/) with capacity 3 has leaves $L = [10, 20]$, high key 20, and $R = [30, 40, 50]$, high key $+\infty$, under the root $[(20, L), (+\infty, R)]$. A search for 55 reads the root and stalls. Then insert(45), insert(60) and insert(55) run to the end, each split moving the upper half into a new right sibling. Give the leaves with their high keys. When the search resumes, which nodes does it read, how many right links does it follow, and what does it return?

15. • A [MultiQueue](/multiqueue/) has three heaps holding $\{1, 6\}$, $\{2, 5\}$ and $\{3, 4\}$. Each delete-min picks two distinct heaps uniformly at random and removes the smaller top. Find the expected rank of the first delete-min, and of the second.

16. • Model a [SprayList](/spraylist/) for $p = 4$ threads by an ideal skip list, in which the nodes of level $h$ are those whose rank is a multiple of $2^h$. With $H = 2$, $L = 8$ and $D = 1$, the spray jumps $j_2, j_1, j_0$ nodes, each uniform in $\{0, \ldots, 8\}$, on levels 2, 1 and 0. Give the landing rank as a function of the jumps (a spray that never leaves the head lands on rank 1). Find the largest landing rank, the expected landing rank, the probability of landing on rank 1, and the most likely ranks.

17. • A sloppy counter runs on $p = 48$ cores. Find the largest threshold $S$ for which an approximate read is never more than 1000 below the true count. With this $S$, $10^6$ increments are spread as evenly as possible over the cores. How often is the global lock taken, and what does an approximate read return at the end?

18. ★ Prove that quiescent consistency is compositional: a history $H$ is quiescently consistent if each subhistory $H|o$ on one object is. Why does the same argument fail for sequential consistency?

19. ★ Show that a counter that is only quiescently consistent, such as a diffracting tree, still solves wait-free consensus for two threads. Conclude that it cannot be built from read and write registers alone.

20. ★ A MultiQueue has $c$ heaps, and the $c$ smallest items are the tops of the $c$ heaps. Prove that a delete-min with two distinct uniform choices returns an item of expected rank $(c + 1)/3$, and that a delete-min with one uniform choice gives $(c + 1)/2$.

21. ★ Remove the sentinel from the two-lock queue: head and tail point to the first and the last item, and both are nil when the queue is empty. Show that an enqueue on a one-item queue and a dequeue of that item must write the same field, and give a schedule of one enqueue and one dequeue, each holding its own lock, that loses an item.

22. ★ Call a counter read *quiescently exact* if, whenever no call is pending, it returns the number of completed increments. Show that the approximate read of a sloppy counter is not quiescently exact for any $S \ge 2$, and that for $S = 1$ the approximate read is linearizable.
