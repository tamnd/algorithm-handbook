A database promises that a committed transaction stays committed and that an unfinished one leaves no trace. Both promises must hold even if the power fails in the middle of a write. Main memory is lost in such a crash, and the disk keeps whatever had reached it, which may be some of the changes of a transaction and not others. Recovery is the work, during normal operation and after a restart, that turns this mixture back into a correct state.

The difficulty is speed. Writing every changed page at commit, and nothing before, would make recovery easy and the system slow. Real systems let the buffer manager write pages when it likes and keep a log of changes instead, and the log must be written in the right order and kept short. This chapter gives the rules that make that safe and the algorithms that use them.

## What the chapter covers

The chapter is in four groups, read in order.

1. **The problem and the buffer choices.** The [crash recovery problem](/crash-recovery/), with the commit point and the two repairs, undo and redo. The [steal and force policies](/steal-and-force-policies/) of the buffer manager, and which repairs each combination needs.
2. **Two ways to make updates atomic.** [Shadow paging](/shadow-paging/), which commits by one atomic switch of a root pointer and needs no undo or redo of page contents, and [write-ahead logging](/write-ahead-logging/), with its WAL rule and commit rule.
3. **Keeping the log cheap.** [Checkpointing](/checkpointing/), from consistent to fuzzy checkpoints, which bounds the log that restart reads, and [group commit](/group-commit/), which shares one log write among many commits.
4. **The full algorithm.** [ARIES recovery](/aries-recovery/), with its analysis, redo and undo passes, log sequence numbers on pages, and compensation records that make a second crash during recovery harmless.

The entries on log sequence numbers, compensation log records and fuzzy checkpoints as separate topics, undo/redo logging, physiological and logical logging, command logging, write-behind logging, multi-level recovery, savepoints, media and point-in-time recovery, the differential file and instant restart are not written yet. The ARIES and checkpointing entries describe several of them briefly.

## A first reading

For a first reading, take the entries in the order of the chapter: the crash recovery problem, the steal and force policies, shadow paging, write-ahead logging, checkpointing, group commit and ARIES recovery. There are only seven, and each one uses the ones before it.

If time is short, read the crash recovery problem, the steal and force policies, write-ahead logging and ARIES. Shadow paging is worth reading for the contrast, since it reaches atomicity with no log of page contents at all, and group commit matters most if you care about the commit rate of a real system.

## Before you start

You need the [ACID properties](/acid-properties/) and the strict schedules of [strict two-phase locking](/strict-two-phase-locking/) from Chapter 40.5: recovery assumes that no transaction reads or overwrites a change that is not committed. The pages and buffers are those of the [B+ tree](/b-plus-tree/) and of the [external memory model](/external-memory-model/), from Volumes 3 and 1.

Logging is not only a database idea. The [undo log](/undo-log/) and the [redo log](/redo-log/) of transactional memory, in Volume 22, are the same two repairs in main memory. The [log-structured merge tree](/log-structured-merge-tree/) of Volume 3 writes a log first and builds its index from it later. When the log is replicated across machines, committing a record is a consensus problem, solved by [Paxos](/paxos/) or [Raft](/raft/) in Volume 21, and committing across several databases uses [two-phase commit](/two-phase-commit/).
