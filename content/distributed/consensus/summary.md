## What to remember

- [Consensus](/consensus-problem/) asks for agreement, validity and termination. The first two are [safety properties](/consensus-properties/); termination is a liveness property, and the models make it hard.
- In the [synchronous model](/synchronous-model/) with crashes, consensus is solvable for any $f < n$. [FloodSet](/floodset/) uses $f + 1$ rounds and at most $n(n-1)(f+1)$ messages, and the [round lower bound](/consensus-round-lower-bound/) shows that $f + 1$ rounds are needed in the worst case when $f \le n - 2$.
- The [FLP theorem](/flp-impossibility/) says that no deterministic protocol solves consensus in the [asynchronous model](/asynchronous-model/) if one process may crash. The ways around it are coin flips ([Ben-Or](/ben-or-consensus/)), [failure detectors](/failure-detector/) ([Chandra-Toueg](/chandra-toueg-consensus/)) and [partial synchrony](/partial-synchrony/), which Paxos and Raft need only for progress. Each needs $n > 2f$.
- Any two majorities share a process, and this fact carries the safety proofs of Paxos and Raft. A majority [quorum](/quorum/) has $\lfloor n/2 \rfloor + 1$ members, so $n = 2f + 1$ processes tolerate $f$ crashes. [Flexible Paxos](/flexible-paxos/) shows that only phase 1 and phase 2 quorums must meet, $|Q_1| + |Q_2| > n$.
- [Paxos](/paxos/) is safe in every run and decides once one proposer runs alone with a live majority. One decision costs 4 message delays and $3n + nl$ messages; with phase 1 done ahead of time, as in [Multi-Paxos](/multi-paxos/), it costs 2 delays. [Raft](/raft/) has the same core, with two extra rules: a server with an out-of-date log cannot win an election, and a leader commits by counting copies only for entries of its own term.
- [Total-order broadcast](/total-order-broadcast/) is equivalent to consensus in the asynchronous model with crashes, and it drives a [replicated state machine](/replicated-state-machine/).
- [Two-phase commit](/two-phase-commit/) is always safe but blocks if the coordinator fails after the votes. [Three-phase commit](/three-phase-commit/) removes the blocking only with synchronous rounds and exact crash detection, and it breaks under a partition. [Paxos Commit](/paxos-commit/) removes it by storing each vote on $2F + 1$ acceptors.
- Weaker problems are easier: [approximate agreement](/approximate-agreement/) is solvable asynchronously, and [k-set agreement](/k-set-agreement/) is too exactly when $f < k$.
- [Nakamoto consensus](/nakamoto-consensus/) gives agreement only with high probability. An attacker with a share $q < 1/2$ of the hash power catches up from $z$ blocks behind with probability $(q/p)^z$, where $p = 1 - q$.

## The protocols side by side

| Protocol | Timing model | Faults tolerated | Best case | Messages, best case | Weak point |
|---|---|---|---|---|---|
| [FloodSet](/floodset/) | synchronous | $f < n$ crashes | $f + 1$ rounds | $n(n-1)(f+1)$ | always $f + 1$ rounds |
| [Ben-Or](/ben-or-consensus/) | asynchronous | $n > 2f$ crashes | 1 round | $2n^2$ per round | up to $2^n + 1$ expected rounds |
| [Chandra-Toueg](/chandra-toueg-consensus/) | asynchronous with $\Diamond\mathcal{S}$ | $n > 2f$ crashes | 1 round | $O(n)$ per round, $O(n^2)$ to relay the decision | unbounded until the detector settles |
| [Paxos](/paxos/) | asynchronous, partial synchrony for progress | $n = 2f + 1$ crashes | 4 delays | $3n + nl$ | dueling proposers |
| [Raft](/raft/) | asynchronous, partial synchrony for progress | $n \ge 2f + 1$ crashes | one round trip from the leader | $2(n-1)$ per command | the leader is a bottleneck |
| [Two-phase commit](/two-phase-commit/) | asynchronous, crash-recovery | any number, but may block | 3 delays | $4n$ | blocks on coordinator failure |
| [Three-phase commit](/three-phase-commit/) | synchronous, exact detection | crashes, not partitions | 5 delays | $5n$ | unsafe under partitions |
| [Nakamoto](/nakamoto-consensus/) | bounded delay, open membership | less than half the hash power | $z$ block intervals | $\Theta(n)$ per block | agreement only with high probability |

: The main protocols. $n$ counts processes (acceptors for Paxos, participants for commit), $l$ learners, $f$ faults, and $z$ is the confirmation depth.

## Choosing a method

To replicate a service on a few servers in one data centre, use a leader-based log: [Raft](/raft/) if you want a protocol that is fully specified, [Multi-Paxos](/multi-paxos/) or [Viewstamped Replication](/viewstamped-replication/) if you already have one of them. Five servers survive two crashes. Add a [leader lease](/leader-lease/) only if the clocks have a true drift bound, and plan [log compaction](/log-compaction/) and [membership change](/cluster-reconfiguration/) from the start.

When clients are far from the leader, [Fast Paxos](/fast-paxos/), [EPaxos](/epaxos/) and [Mencius](/mencius/) trade messages or quorum size for fewer delays. When machines are expensive, [Cheap Paxos](/cheap-paxos/) and [Vertical Paxos](/vertical-paxos/) keep only $f + 1$ replicas active in the normal case.

For a transaction across shards, use [two-phase commit](/two-phase-commit/) with the coordinator's decision on a replicated log, the idea of [Paxos Commit](/paxos-commit/). Avoid [three-phase commit](/three-phase-commit/) where the network can partition. Use [Nakamoto consensus](/nakamoto-consensus/) or [proof of stake](/proof-of-stake/) only when membership is open; with a known set, a Byzantine protocol from Chapter 21.6 gives final decisions.
