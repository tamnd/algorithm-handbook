Three servers hold copies of a bank's ledger. A client asks one of them to move money, and that server crashes before it tells the others. A second server, unsure whether the first is dead or slow, starts to act on its own. If the two servers make different choices, the ledger now has two histories. Consensus is the problem of making a group of processes choose one value and stick to it, even when some of them crash and the network delays messages for an unknown time. Strongly consistent databases, lock services and configuration stores all solve it, most of them with one of a handful of protocols found in this chapter.

The chapter has two kinds of entries. The theory says exactly what is possible: with synchronous rounds consensus takes $f + 1$ rounds, and in a fully asynchronous system no deterministic protocol solves it at all, even with one crash. The practice shows how real protocols live with that result: they never break safety, and they make progress once the network behaves for long enough.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **Models of time and failure.** The [synchronous model](/synchronous-model/), the [asynchronous model](/asynchronous-model/), [partial synchrony](/partial-synchrony/) and [crash failures](/crash-failure/). The [two generals problem](/two-generals-problem/) shows what lost messages do.
2. **The problem and its tools.** The [consensus problem](/consensus-problem/) and its [correctness conditions](/consensus-properties/), the [quorum](/quorum/) and the [ballot number](/ballot-number/).
3. **Bounds and impossibility.** [FloodSet](/floodset/) and the [round lower bound](/consensus-round-lower-bound/) for synchronous systems, the [FLP theorem](/flp-impossibility/) for asynchronous ones, and [Ben-Or's randomized algorithm](/ben-or-consensus/).
4. **Failure detectors.** The [failure detector](/failure-detector/) classes, the [eventually perfect detector](/eventually-perfect-failure-detector/), [Omega](/omega-failure-detector/), the [Chandra-Toueg algorithm](/chandra-toueg-consensus/) and the [weakest failure detector for consensus](/weakest-failure-detector-consensus/).
5. **Paxos and the replicated log.** [Paxos](/paxos/), [total-order broadcast](/total-order-broadcast/), the [replicated state machine](/replicated-state-machine/), [Multi-Paxos](/multi-paxos/) and [Raft](/raft/).
6. **Running a replicated service.** The [view change](/view-change/), [Viewstamped Replication](/viewstamped-replication/), [Zab](/zab/), [split brain](/split-brain/), the [leader lease](/leader-lease/), [log compaction](/log-compaction/) and [cluster reconfiguration](/cluster-reconfiguration/).
7. **Variants of Paxos.** [Flexible](/flexible-paxos/), [Fast](/fast-paxos/), [Generalized](/generalized-paxos/), [Cheap](/cheap-paxos/) and [Vertical Paxos](/vertical-paxos/), with [EPaxos](/epaxos/) and [Mencius](/mencius/).
8. **Atomic commit.** The [atomic commit problem](/atomic-commit/), [two-phase commit](/two-phase-commit/), [three-phase commit](/three-phase-commit/) and [Paxos Commit](/paxos-commit/).
9. **Weaker agreement.** [Approximate agreement](/approximate-agreement/), its [standard algorithm](/approximate-agreement-algorithm/) and [k-set agreement](/k-set-agreement/).
10. **Blockchains.** [Proof of work](/proof-of-work/), [Nakamoto consensus](/nakamoto-consensus/) and [proof of stake](/proof-of-stake/).

## A first reading

For a first reading, take these twelve entries in order: [the asynchronous model](/asynchronous-model/), [crash failures](/crash-failure/), [the consensus problem](/consensus-problem/), [quorums](/quorum/), [FloodSet](/floodset/), [the FLP theorem](/flp-impossibility/), [failure detectors](/failure-detector/), [Paxos](/paxos/), [total-order broadcast](/total-order-broadcast/), [the replicated state machine](/replicated-state-machine/), [Raft](/raft/) and [two-phase commit](/two-phase-commit/). They give you the models, the problem, one easy algorithm, the one impossibility result that shapes the rest, the protocol that gets around it, the log built from it, and the commit protocol that every database uses. Run Paxos by hand on three acceptors and two competing proposers before you read Raft. The safety argument of both is the same quorum argument, and it is easier to see without the log.

Skip the variants of Paxos on a first pass; each one assumes you know Paxos and Multi-Paxos well. The [weakest failure detector](/weakest-failure-detector-consensus/) proof and the [round lower bound](/consensus-round-lower-bound/) are the hardest proofs here and can wait. The blockchain group stands apart: it uses a different failure model and gives only probabilistic agreement, so read it after the [Byzantine](/byzantine-failure-model/) chapter.

## Before you start

The correctness conditions are [safety](/safety-property/) and [liveness](/liveness-property/) properties in the sense of Volume 16, and the proofs use [induction](/induction/) on rounds and ballots. Ben-Or's algorithm needs the idea of a [randomized algorithm](/randomized-algorithm/), and the proof-of-work entries use the [geometric distribution](/geometric-distribution/). Nothing else is assumed beyond comfort with message diagrams.

Several entries borrow from later chapters of this volume. Total-order broadcast uses the [total order](/total-order/) of Chapter 21.3, the leader lease uses [clock drift](/clock-drift/) from the same chapter, and Flexible Paxos and Zab build on [quorum intersection](/quorum-intersection/) and [primary-backup replication](/primary-backup-replication/) from Chapter 21.4. Look these up when you reach them.
