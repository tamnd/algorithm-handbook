## What to remember

- Mutual exclusion is a safety property: at most one process is in its critical section. On top of it sits a progress property, in increasing strength: deadlock freedom (if some process tries, some process enters), starvation freedom (every process that tries enters), bounded bypass $b$, and FCFS order after a bounded doorway. FCFS with deadlock freedom gives starvation freedom.
- Two processes need only three read/write registers. Peterson's algorithm raises a flag, writes $turn \leftarrow j$, and waits while $flag[j] \land turn = j$; it is FCFS with bypass 1. The flag must be written first, and on x86 a fence must follow the doorway, because a store buffer lets a later read pass an earlier write.
- With reads and writes, deadlock freedom for $n$ processes needs $n$ registers (Burns and Lynch); the Burns-Lamport algorithm meets the bound with single-writer bits but lets processes starve. The bakery algorithm uses $2n$ registers, is FCFS with bypass $n - 1$, and works with safe registers, but its tickets have no bound.
- Without contention, Lamport's fast algorithm makes 5 writes and 2 reads per passage, whatever $n$. Under contention, no algorithm from reads and writes bounds the steps of the winner.
- On a multiprocessor the cost of a lock is its number of remote memory references (RMRs) per passage: unbounded for TAS and TTAS locks, up to $n + 2$ for the ticket lock in the CC model, $O(1)$ for queue locks. With reads, writes and conditional primitives such as CAS alone, some passage needs $\Omega(\log n)$ RMRs; swap and fetch-and-add escape this bound.
- Spinning for the cost $C$ of a context switch, then blocking, costs at most $2 \min(w, C)$ for a wait $w$; a random threshold gets $e/(e-1) \approx 1.58$.
- A deadlock needs all four Coffman conditions. With single-unit resources it is exactly a cycle in the wait-for graph; with several units a cycle is not enough, and graph reduction decides in $O(mn^2)$ time for $n$ processes and $m$ resource types, like the banker's safety test.
- Lock ordering prevents deadlock: if every process takes locks in increasing order of a strict partial order, and any two locks held together are comparable, the wait-for graph has no cycle.

| lock | primitives | registers | steps alone | progress | bypass | CC RMRs | DSM RMRs |
|---|---|---|---|---|---|---|---|
| [Peterson](/peterson-algorithm/), $n = 2$ | read, write | 3 | 4 | FCFS | 1 | $O(1)$ | $\infty$ |
| [filter](/filter-lock/) | read, write | $2n - 1$ | $(n-1)(n+2) + 1$ | starvation free | $\infty$ | $O(n^3)$ | $\infty$ |
| [tournament](/tournament-lock/) | read, write | $< 6n$ | $4\lceil \log_2 n \rceil$ | starvation free | $\infty$ | $\Theta(\log n)$ | $\infty$ |
| [bakery](/lamport-bakery-algorithm/) | safe registers | $2n$, unbounded | $3n + 1$ | FCFS | $n - 1$ | $O(n)$ | $\infty$ |
| [Lamport fast](/lamport-fast-mutex/) | read, write | $n + 2$ | 7 | deadlock free | $\infty$ | $\infty$ | $\infty$ |
| [TTAS](/spin-lock/) | test-and-set | 1 | 3 | deadlock free | $\infty$ | $\infty$ | $\infty$ |
| [ticket](/ticket-lock/) | fetch-and-add | 2 | 3 | FCFS | 0 | $n + 2$ | $\infty$ |
| [MCS](/mcs-lock/) | swap, CAS | 1 + a node each | 4 | FCFS | 0 | 8 | 4 |
| [CLH](/clh-lock/) | swap | $n + 2$ | 4 | FCFS | 0 | 5 | $\infty$ |

: Locks for $n$ processes. Steps alone: shared accesses of one passage without contention. Bypass: entries of others after the doorway ($\infty$ for filter and tournament when $n \ge 3$). RMRs: worst case per passage.

## Choosing a lock

In real code, use the mutex of the language or the operating system: it spins briefly, then blocks, and it has the right fences. The algorithms from reads and writes teach reasoning about interleavings; on modern processors each one needs fences.

In a kernel, where the holder is not descheduled, spin locks fit short critical sections: TTAS with exponential backoff at low contention, the ticket lock when FIFO order matters, a queue lock when many processors contend. Prefer MCS when memory is distributed and CLH on cache-coherent machines. On a NUMA machine, a cohort lock keeps the lock on one node for a while, at the price of strict fairness.

To wait for a condition on shared data, use a condition variable, and under Mesa semantics, the usual one, test the condition in a while loop. When code takes several locks, fix a lock order. Detection suits systems that can abort a victim, such as databases; the banker's algorithm needs maximum claims in advance.
