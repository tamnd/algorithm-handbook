A distributed database stores one logical database on many machines. It splits tables into fragments and places them near the users or the work, keeps copies so that the data survives the loss of a machine, and runs queries and transactions that touch several sites. Each of these steps is harder than on one machine. A join may have to ship data across a network that is far slower than a disk. A transaction must commit at every site or at none, and the copies must agree on the order of the updates while messages are delayed and machines fail.

The subject matters because almost every large system is now distributed, and the cost of coordination decides what it can promise. Strong guarantees, such as one-copy serializability, need rounds of messages that limit both speed and availability. Weaker guarantees avoid them, and the art is to know exactly which invariants still hold.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Fragmentation and allocation.** Horizontal and vertical fragmentation of tables, the bond energy algorithm, the data allocation problem and workload-driven partitioning with Schism.
2. **Distributed query processing.** The distributed query processing problem, semijoin programs in SDD-1, the parallel hash join and the shared-nothing architecture.
3. **Replication.** Eager and lazy replication, read-one write-all, primary copy locking, and one-copy serializability as the correctness criterion.
4. **Distributed transactions.** Deterministic transactions in Calvin, the Percolator protocol, Clock-SI, and deadlock detection across sites by the edge chasing of Chandy, Misra and Haas.
5. **Weak isolation and coordination avoidance.** Highly available transactions, RAMP transactions and invariant confluence, which says when an invariant can be kept with no coordination at all.

## What to read meanwhile

Commit across sites is [two-phase commit](/two-phase-commit/) and the [atomic commit problem](/atomic-commit/), and agreement among replicas is the [consensus problem](/consensus-problem/), solved by [Paxos](/paxos/) and [Raft](/raft/), all in Volume 21. The same volume has [Lamport clocks](/lamport-clocks/), [vector clocks](/vector-clocks/), [chain replication](/chain-replication/), [CRDTs](/crdt/) and the [last-writer-wins register](/lww-register/). [Consistent hashing](/consistent-hashing/) in Volume 26 places data on machines.

In this volume, the [semijoin](/semijoin/), the [Bloom join](/bloom-join/) and the [Grace hash join](/grace-hash-join/) of Chapter 40.3 are the local pieces of distributed joins, and [strict two-phase locking](/strict-two-phase-locking/) and [snapshot isolation](/snapshot-isolation/) of Chapter 40.5 are the schedulers that distributed systems extend. Deadlocks across sites are cycles in a [wait-for graph](/wait-for-graph/), found by [deadlock detection](/deadlock-detection/) in Volume 22.
