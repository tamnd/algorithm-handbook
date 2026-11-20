## What to remember

- **Fragments must put the relation back together.** A horizontal fragmentation by minterm predicates is complete and disjoint, and the union rebuilds the relation. A vertical fragmentation keeps the key in every fragment, so the join on the key rebuilds it. Choosing fragments and placing them are heuristics in practice: the [data allocation problem](/data-allocation-problem/) is NP-complete with capacities, even with two sites, and NP-hard without them.
- **Distributed plans count bytes.** Finding the cheapest plan is NP-hard already on one site. Semijoins can shrink a relation before it is shipped, and a tree query has a full reducer of $2(r-1)$ semijoins, but a cyclic query may have none. The [parallel hash join](/parallel-hash-join/) sends at most $n$ tuples in one round, and one heavy key still lands on one node.
- **Copies must look like one copy.** One-copy serializability is the goal, and it is stronger than serializability of the copies: a history can have no conflicts on any copy and still not be 1SR. Testing it is NP-complete in general, so protocols guarantee it by construction.
- **Eager schemes deadlock, lazy group schemes reconcile.** In the analytical model of Gray, Helland, O'Neil and Shasha, eager deadlocks and lazy group reconciliations grow as $N^3$ and lazy master deadlocks as $N^2$ in the number of nodes. These are estimates from a simple model, not measurements.
- **Read-one-write-all needs every copy, or a perfect failure detector.** Plain ROWA blocks a write when one copy is down. The available-copies form keeps writing, and it is correct only when "no response" always means a crash; it is not safe under network partitions.
- **Ordering in advance removes two-phase commit.** Calvin fixes a global order of each batch of transactions and runs them deterministically, so all replicas reach the same state and no participant can vote no. Transactions whose read sets depend on data need a reconnaissance step first.
- **Snapshot isolation spreads well and is still not serializable.** Clock-SI takes snapshots from local clocks and waits out the skew, and Percolator takes them from a timestamp oracle. Both allow write skew.
- **Some guarantees need no coordination.** Read committed, read atomic and the session guarantees can be had while partitioned; preventing lost updates, preventing write skew and recency cannot. An invariant can be kept without coordination exactly when it is invariant confluent.

## The protocols side by side

| Protocol | Guarantee | Messages for $r$ reads and $w$ writes | Main cost |
|---|---|---|---|
| [Primary copy locking](/primary-copy-locking/) | 1SR | at most $3r + w(2n + 1)$ | the primary of an item is a single point of failure |
| [Read-one-write-all](/read-one-write-all/) | 1SR | $2r + 2wn$ when every read succeeds at once | a write needs all $n$ copies up |
| [Calvin](/calvin-deterministic-transactions/) | serializable, deterministic | at most $p(p - 1)$ between $p$ partitions | batches add latency; read and write sets needed in advance |
| [Clock-SI](/clock-si/) | snapshot isolation | $2r$ for remote reads, 3 per commit participant | waits for clock skew and for commits in progress |
| [Percolator](/percolator-transactions/) | snapshot isolation | $2r + 4w + 4$ | a central oracle; locks cleaned up lazily |
| [RAMP-Fast](/ramp-transactions/) | read atomic | writes $4k$, reads $2k$ to $4k$ for $k$ items | no lost-update prevention; last writer wins |

: The transaction protocols of the chapter with the message counts their entries prove, without the atomic commit protocol where the entry counts it apart. Here $n$ is the number of copies of an item. The guarantees are theorems under each entry's failure model; all throughput figures in the entries are measurements.

## Choosing a design

Partition first, replicate second. If the workload has a natural key, such as a warehouse or a customer, partition on it so that most transactions stay on one node; Schism finds such a key from a trace when none is obvious. Then the choice of protocol matters only for the transactions that cross nodes.

For transactions that need serializability, use locking with two-phase commit when transactions are short and their read sets are unknown, and a deterministic design such as Calvin when the read and write sets can be known before the run. For read-heavy work across regions, snapshot isolation is cheaper, but check the application for write skew. When availability during partitions matters more than isolation, keep to the highly available levels and test each invariant for confluence: those that pass need no coordination, and only the others need a coordinated path.
