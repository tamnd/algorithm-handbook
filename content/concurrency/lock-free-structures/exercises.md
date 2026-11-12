1. ◦ Two threads each add one to a shared counter twice, and each increment is a plain read followed by a plain write of the value plus one. The counter starts at 0. There are 70 ways to interleave the eight steps. How many end with the counter at 4, at 3 and at 2? Can it end below 2? Then say why the same program with each increment done by a [compare-and-swap](/compare-and-swap/) loop always ends at 4.

2. ◦ Give the strongest progress condition that holds for each of these: a push on the [Treiber stack](/treiber-stack/); an enqueue on the [Lamport queue](/lamport-spsc-queue/); an enqueue and a dequeue on the [Herlihy-Wing queue](/herlihy-wing-queue/); an operation under [flat combining](/flat-combining/); a scan of the [Afek snapshot](/afek-atomic-snapshot/); a thief on the [Chase-Lev deque](/chase-lev-deque/) that calls steal again after every ABORT. Choose from [wait-free](/wait-freedom/), [lock-free](/lock-freedom/), [obstruction-free](/obstruction-freedom/) and blocking.

3. ◦ Three threads A, B and C share a FIFO queue that starts empty. Times are integers, and each operation runs over the interval given. Decide whether each history is [linearizable](/linearizability/); if it is, give the order.
   H1: A runs enq(x) over $[0, 4]$; B runs enq(y) over $[1, 2]$ and then deq returning x over $[3, 6]$; C runs deq returning y over $[5, 7]$.
   H2: A runs enq(x) over $[0, 1]$; B runs enq(y) over $[2, 5]$; C runs deq returning y over $[3, 4]$; A runs deq returning x over $[6, 7]$.

4. ◦ One thread works alone on an empty Treiber stack. It calls push(a), push(b), pop, pop, pop. Count the shared memory steps of each call as the entry counts them, and give the total. What does each pop return?

5. ◦ The [Vyukov bounded queue](/vyukov-bounded-mpmc-queue/) has $N = 4$ cells, starts with seq $= [0, 1, 2, 3]$ and enqPos $=$ deqPos $= 0$. One thread runs enq(a), enq(b), enq(c), enq(d), deq, deq, enq(e). Give seq, enqPos and deqPos at the end. What do enq(f) and then enq(g) return?

6. ◦ Give the [consensus number](/consensus-number/) of each object: an atomic snapshot object; a swap register; a stack; 3-register assignment; a register with load-linked and store-conditional; a queue with a peek operation that reads the head without removing it.

7. ◦ For width $w = 8$, give the depth, the number of balancers and the number of shared memory steps per call of the [bitonic counting network](/bitonic-counting-network/). Do the same for the periodic network of the [counting network](/counting-network/) entry. Which of these outputs counts, seen on four wires after quiescence, have the step property: $(3, 3, 2, 2)$, $(3, 2, 3, 2)$, $(2, 2, 2, 2)$, $(4, 3, 3, 2)$, $(3, 3, 3, 2)$?

8. ◦ A [Harris list](/harris-linked-list/) holds head, 3, 7, tail. A call delete(7) has marked the next pointer of node 7 in line L17 and then stalls before line L18. Now insert(9) runs alone to the end. Which CAS steps does it make, and what is the list after it? Then delete(7) resumes. What does its CAS in line L18 do, what does the SEARCH that follows change, and what does delete(7) return?

9. ◦ The Lamport queue has $N = 4$ slots. Suppose head and tail were stored $\bmod N$ instead of as unbounded counters. The producer enqueues four items and the consumer has done nothing. What do head and tail hold, and what does the next dequeue return? Show that keeping them $\bmod 2N$ is enough to tell a full queue from an empty one.

10. • $n$ threads each add one to a shared counter with a CAS loop: read the counter, then CAS it from the value read to that value plus one, and retry on failure. Show that a thread makes at most $n$ attempts and that all threads together make at most $n(n + 1)/2$. Give a schedule that reaches this total.

11. • In the dequeue of the [Michael-Scott queue](/michael-scott-queue/), an EMPTY result is linearized at line L13, the read of h.next, and not at the return. Give a run in which linearizing it at the return in line L16 would be wrong.

12. • Delete line L8 from the Michael-Scott enqueue, so that an enqueuer never moves a lagging Tail. Show that the queue is then not lock-free. Which other line of the code still moves Tail on behalf of a stalled thread, and why does it not save lock-freedom?

13. • Two producers share a Lamport queue with $N = 4$ that starts empty, and both call enq at once. Give an interleaving of lines L1 to L4 in which an item is lost. What does the consumer see after both enqueues return OK?

14. • A single balancer with two output wires is used as a counter: a token that leaves on wire $i$ takes the next value of a counter that hands out $i, i + 2, i + 4, \ldots$. Show that this counter is [quiescently consistent](/quiescent-consistency/) but not linearizable. Give the run.

15. • On the values $0, \ldots, 7$, with arithmetic $\bmod 8$, decide whether each set of [read-modify-write](/read-modify-write/) functions is interfering in the sense of Theorem B of that entry: {add 1, swap 0}; {and 6, or 1}; {add 1, xor 1}; {add 2, xor 1}. For each interfering set, say which pair commutes and which overwrites.

16. • Three threads try to solve consensus with one [fetch-and-add](/fetch-and-add/) register that starts at 0. Thread $i$ adds $2^i$ and decides on the input of the thread that went first, as it can read it off the returned value. Show that this works for any two of the threads, and find a case where the third cannot decide. Which theorem says that no other use of FAA helps?

17. • A [split-ordered list](/split-ordered-list/) uses words of $W = 8$ bits, the hash $h(k) = k$, and $s = 4$ buckets, all initialized. It holds the keys 3, 6, 9, 12 and 14. Write the list in order, dummy nodes included. The table then doubles to 8 buckets, and contains(14) runs. Which bucket does it need, which dummy node goes in, and where? Last, with $s = 16$ and only bucket 0 initialized, which dummy nodes are inserted, in which order, by an operation on a key in bucket 15?

18. • A Chase-Lev deque starts with an array of size 4 and is empty. The owner pushes ten items with no thief running. At which pushes does the array grow, how many steps does each push take, and what is the total? What is the size of the array at the end?

19. • A Chase-Lev deque holds one item x, with top $= 5$ and bottom $= 6$. The owner calls pop and one thief calls steal at the same time, on a machine with sequential consistency. List every pair of results that can occur. What are top and bottom at the end in each case?

20. • Threads A, B and C call enq(a), enq(b) and enq(c) on an empty Herlihy-Wing queue, and their FAA steps take slots 0, 1 and 2 in that order. C stores its item first; A and B stall between L1 and L2. A dequeue then runs alone. What does it return, and after how many steps? Give a linearization of the four operations, and say why enq(a) cannot be linearized at its FAA.

21. ★ Run the Vyukov queue with a single cell, $N = 1$. One thread alone calls enq(a), enq(b) and then deq. Follow seq, enqPos and deqPos step by step. What goes wrong? Which part of the cell protocol in the entry's proof fails, and what bound on $N$ does the proof need?

22. ★ The Chase-Lev pop needs a full fence between lines L6 and L7, even on x86, where a load may pass an earlier store of the same thread that is still in its store buffer. Take a deque with x0 and x1, top $= 0$ and bottom $= 2$. Remove the fence and find a run with the owner and one thief in which the same item is returned twice. Give top and bottom at the end.

23. ★ A counter for $n$ threads keeps one single-writer register $c_i$ per thread. Thread $i$ adds $v$ by writing $c_i + v$ to $c_i$, and a read returns the sum of $c_0, \ldots, c_{n-1}$, read one at a time. Show that the read is linearizable when every $v$ is 1, but not when $v$ may be any positive number: for $n = 3$, find a read that returns a value the counter never held. How does an [atomic snapshot](/atomic-snapshot/) fix it?

24. ★ The simple double collect scan reads all $n$ registers twice and returns if no sequence number changed; otherwise it starts again with two fresh collects. Suppose the other threads write $k$ times in all while one scan runs. Show that the scan returns after at most $2n(k + 1)$ reads, and that this bound is reached for every $n$ and $k$. Why does this not make the scan wait-free?

25. ★ In the Afek snapshot, a scan returns after at most $n$ iterations of $2n$ reads. For each $n \ge 2$, give a schedule in which a scan takes exactly $2n^2$ reads. How many updates must the other threads complete during it, and whose view does the scan return?
