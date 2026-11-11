## What to remember

- The [consistency models](/consistency-models/) form a chain: linearizable, sequential, causal, PRAM, with [eventual consistency](/eventual-consistency/) at the weak end. By the [CAP theorem](/cap-theorem/), no register in an asynchronous network that loses messages is both linearizable and available. By [PACELC](/pacelc/), even with no failures, a sequentially consistent store has $|W| + |R| \ge d$ for message delay $d$.
- [Session guarantees](/session-guarantees/) cost each client $2n$ integers. Read your writes, monotonic reads and monotonic writes together give PRAM, and with writes follow reads they give causal consistency.
- [State machine replication](/state-machine-replication/) runs the same commands in the same order everywhere. [Chain replication](/chain-replication/) spends $2n$ messages and $n + 1$ delays on an update and 2 of each on a query. [Primary-backup](/primary-backup-replication/) spends $2(n-1)$ server messages plus request and reply, and 4 delays.
- Every read quorum meets every write quorum in at least $R + W - N$ replicas, so $R + W > N$ makes reads see the last write and $2W > N$ makes writes meet. A write survives $N - W$ crashes and a read $N - R$. [ABD](/quorum-replication/) builds an atomic register from majorities in two round trips and needs $n \ge 2f + 1$. A [sloppy quorum](/sloppy-quorum/) gives up the intersection.
- [Last-writer-wins](/last-writer-wins/) converges because the max of stamps is a join, but it drops concurrent writes, and a fast clock beats a later write. A delete must leave a [tombstone](/tombstone/), which may be dropped only when every replica has it.
- [Anti-entropy](/anti-entropy/) spreads a write to all $n$ replicas in $\Theta(\log n)$ rounds. Under pull, the fraction still missing it goes from $p$ to $p^2$ per round. A Merkle comparison with $d$ differing keys over $B$ buckets visits at most $1 + 2d \log_2 B$ nodes.
- A state-based object whose states form a [join-semilattice](/join-semilattice/), whose updates are inflationary and whose merge is the join, is strongly eventually consistent. So is an op-based object whose concurrent operations commute under causal delivery. This is the [CRDT convergence theorem](/crdt-convergence-theorem/).
- For text, [operational transformation](/operational-transformation/) on arbitrary paths needs [TP1 and TP2](/tp1-tp2-conditions/), and no transformation function on the classical parameters meets both. Sequence CRDTs give each character an identity instead. [Logoot](/logoot/) and [LSEQ](/lseq/) can interleave concurrent words, while [RGA](/rga/) keeps forward-typed runs together.

| Type | State | Concurrent conflict | Re-add after remove | Time | Space |
|---|---|---|---|---|---|
| [G-counter](/g-counter/) | $n$ counts, merge by entrywise max | none | (no remove) | $\Theta(n)$ | $\Theta(n)$ |
| [PN-counter](/pn-counter/) | two g-counters $P$ and $N$ | none; the value may go below 0 | (no remove) | $\Theta(n)$ | $\Theta(n)$ |
| [LWW-Register](/lww-register/) | value and stamp $(c, r)$ | larger stamp wins, others lost | (no remove) | $\Theta(1)$ | $\Theta(v)$ |
| [MV-Register](/mv-register/) | at most $n$ (value, version vector) pairs | all kept as siblings | (no remove) | $\Theta(n^3)$ | $\Theta(n^2)$ |
| [G-Set](/g-set/) | a set, merge by union | none | no remove | $\Theta(m)$ expected | $\Theta(m)$ |
| [2P-Set](/two-phase-set/) | added set $A$, removed set $R$ | remove wins | no | $\Theta(m)$ expected | $\Theta(m)$ |
| [LWW-Element-Set](/lww-element-set/) | add and remove stamp per element | later stamp, bias on ties | yes | $\Theta(m)$ expected | $\Theta(m)$ |
| [OR-Set](/or-set/) | unique tags, or dots and a version vector | add wins | yes | $\Theta(k)$ | $\Theta(k)$ |

: The basic CRDTs of the chapter, with the bounds stated in their entries, for $n$ replicas, $m$ entries in a received state, $k$ tags of one element and a value of size $v$.

## Choosing a method

If clients must never see an old value, keep one order. Use a replicated log for a general state machine, chain replication when reads dominate, and ABD for a register with no leader. Each of these stops answering on one side of a partition.

If the store must stay writable everywhere, choose the merge with care. Last-writer-wins is right only when losing a concurrent write is acceptable. When it is not, use an MV-register and let the application merge the siblings, or a CRDT whose merge already means what the application wants: counters for counts, the OR-Set when a re-add after a remove should stick, the 2P-Set when a removed item must stay removed. Add session guarantees so a user sees their own writes. Run anti-entropy with tombstones whatever else is in place, since read repair and hinted handoff miss keys that nobody reads.

For shared text, OT through a central server, as in Jupiter, needs only TP1 and is well understood. Peer-to-peer editors are better served by a sequence CRDT. RGA and YATA keep concurrent typing together but keep tombstones, while Logoot and LSEQ keep no tombstones but can interleave.
