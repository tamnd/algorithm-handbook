Two threads add 1 to a shared counter that holds 0. Each addition is a read followed by a write, and if both threads read before either writes, the counter ends at 1, not 2. This is a [race condition](/race-condition/), and the usual cure is to make the read and the write a *critical section*: a piece of code that at most one process runs at a time. Every operating system kernel, database lock manager and thread library is built on this cure, and the algorithms that give it are older than most of computer science. Dijkstra stated the problem in 1965. His conditions still define it: the processes share memory, nothing is assumed about their relative speeds, and a process that stops in its remainder section, outside the protocol, must not block the others.

The chapter studies that problem in three ways. First as a puzzle: how to build a lock from plain reads and writes, which needs ingenuity, and how much memory and how many steps that takes. Then as engineering: how to build a lock from the atomic instructions of real machines so that waiting processes do not flood the memory system. And last as the source of new failures: once processes hold locks, they can wait for each other in a cycle, and the chapter ends with the theory of deadlock.

Each entry fixes its model: $n$ asynchronous processes, the shared primitives allowed (atomic reads and writes, [test-and-set](/test-and-set/), fetch-and-add, swap or compare-and-swap), and the memory model, which is sequential consistency unless the entry says otherwise. Each states its progress property and its bypass, the number of times other processes can enter while one waits. The code of the entries runs in simulators that interleave the steps of the processes one at a time and, for small cases, try every schedule, so the claims of safety and progress are checked as well as proved. Python threads are not used: a run with threads shows only the schedules that the interpreter happens to pick.

## What the chapter covers

1. **What goes wrong.** [Race conditions](/race-condition/), [critical sections](/critical-section/), and the three failures of waiting: [deadlock](/deadlock/), [livelock](/livelock/) and [starvation](/starvation/).
2. **The mutual exclusion problem.** The [problem](/mutual-exclusion-problem/) itself, the [mutex](/mutex/) interface, and the progress properties [deadlock freedom](/deadlock-freedom/) and [starvation freedom](/starvation-freedom/), with bounded bypass and first-come, first-served (FCFS) order.
3. **Two processes with reads and writes.** [Dekker's algorithm](/dekker-algorithm/), the first solution, and [Peterson's algorithm](/peterson-algorithm/), the standard one: three registers, bypass 1.
4. **Many processes with reads and writes.** The [filter lock](/filter-lock/), the [bakery algorithm](/lamport-bakery-algorithm/) and the [tournament lock](/tournament-lock/); the historical line from Dijkstra to [Eisenberg and McGuire](/eisenberg-mcguire-algorithm/); and the costs, from the [lower bound](/mutual-exclusion-lower-bounds/) of $n$ registers to [Lamport's fast algorithm](/lamport-fast-mutex/) with 7 steps per passage when there is no contention.
5. **Spin locks from atomic instructions.** The [spin lock](/spin-lock/) family, the [ticket lock](/ticket-lock/), the measure of [remote memory references](/rmr-complexity/), and the queue locks of [Anderson](/anderson-lock/), [Mellor-Crummey and Scott](/mcs-lock/) and [Craig, Landin and Hagersten](/clh-lock/), which reach $O(1)$ RMRs per passage.
6. **Semaphores, condition variables and monitors.** The blocking primitives: the [semaphore](/semaphore/), the [condition variable](/condition-variable/) with Hoare and Mesa semantics, the [monitor](/monitor/) and the [reentrant lock](/reentrant-lock/).
7. **Classic synchronization problems.** The [bounded buffer](/bounded-buffer-problem/), [readers and writers](/readers-writers-problem/), the [sleeping barber](/sleeping-barber-problem/) and the [cigarette smokers](/cigarette-smokers-problem/), with the [readers-writer lock](/readers-writer-lock/) of real libraries.
8. **Deadlock.** The [resource allocation graph](/resource-allocation-graph/), the four [Coffman conditions](/coffman-conditions/), and the three ways to deal with deadlock: [prevention](/deadlock-prevention/) by [lock ordering](/lock-ordering/), avoidance by the [banker's algorithm](/banker-algorithm/), and [detection](/deadlock-detection/). The [dining philosophers](/dining-philosophers-problem/) test all three.

## A first reading

Read these in order:

1. [race condition](/race-condition/)
2. [critical section](/critical-section/)
3. [deadlock](/deadlock/)
4. [mutual exclusion problem](/mutual-exclusion-problem/)
5. [starvation freedom](/starvation-freedom/)
6. [Peterson's algorithm](/peterson-algorithm/)
7. [bakery algorithm](/lamport-bakery-algorithm/)
8. [test-and-set](/test-and-set/)
9. [spin lock](/spin-lock/)
10. [ticket lock](/ticket-lock/)
11. [MCS lock](/mcs-lock/)
12. [semaphore](/semaphore/)
13. [condition variable](/condition-variable/)
14. [lock ordering](/lock-ordering/)

That path gives the problem, one proof of mutual exclusion in full, the FCFS idea, the hardware locks that real systems use, the blocking primitives, and the one rule that prevents most deadlocks in practice. Skip at first the historical algorithms of Dijkstra, Knuth, Eisenberg and McGuire, Kessels, Szymański and Burns and Lamport; they matter for the history and for the lower bounds, not for daily use. The [cohort lock](/cohort-lock/), [Fischer's algorithm](/fischer-algorithm/) and the [Chandy-Misra algorithm](/chandy-misra-algorithm/) can wait too.

## Before you start

You need to read pseudocode and to follow a proof by contradiction and an invariant. The deadlock entries use graphs: [directed graphs](/directed-graph/), [bipartite graphs](/bipartite-graph/) and [cycle detection](/cycle-detection/) from Volume 7. The bounded buffer uses a [queue](/queue/), and lock coupling walks a [linked list](/linked-list/), both from Volume 3. [Sequential consistency](/sequential-consistency/), from the chapter on concurrent structures in Volume 3, is the memory model that most entries assume. The words safety and liveness come from Volume 16, where [safety properties](/safety-property/), [liveness properties](/liveness-property/) and [fairness](/fairness/) are defined; mutual exclusion is a safety property, and both progress properties are liveness properties. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
