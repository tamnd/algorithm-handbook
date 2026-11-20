A database promises that a committed transaction stays committed and that an unfinished one leaves no trace. Both promises must hold even if the power fails in the middle of a write. Main memory is lost in such a crash, and the disk keeps whatever had reached it, which may be some of the changes of a transaction and not others. Recovery is the work, during normal operation and after a restart, that turns this mixture back into a correct state.

The difficulty is speed. Writing every changed page at commit, and nothing before, would make recovery easy and the system slow. Real systems let the buffer manager write pages when it likes and keep a log of changes instead, and the log must be written in the right order and kept short. This chapter gives the rules that make that safe and the algorithms that use them, from the first crash to the loss of a whole disk and the mistakes of a user.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **The problem and the buffer choices.** The [crash recovery problem](/crash-recovery/), with the commit point and the two repairs, undo and redo. The [steal and force policies](/steal-and-force-policies/) of the buffer manager, and which repairs each combination needs.
2. **Updating out of place.** [Shadow paging](/shadow-paging/), which commits by one atomic switch of a root pointer and needs no undo or redo of page contents, and the [differential file](/differential-file/), which keeps all changes apart from a read-only main file.
3. **The write-ahead log.** [Write-ahead logging](/write-ahead-logging/), with its WAL rule and commit rule; [undo/redo logging](/undo-redo-logging/), the classic algorithm with before and after images; the [log sequence number](/log-sequence-number/) that each page carries; and the choice between [physiological](/physiological-logging/) and [logical](/logical-logging/) records.
4. **Keeping the log cheap.** [Checkpointing](/checkpointing/) and the [fuzzy checkpoint](/fuzzy-checkpoint/), which bound the log that restart reads without stopping the system, and [group commit](/group-commit/), which shares one log write among many commits.
5. **ARIES and its refinements.** [ARIES recovery](/aries-recovery/), with its analysis, redo and undo passes, and the [compensation log records](/compensation-log-record/) that make a second crash during recovery harmless. [Savepoints](/savepoint/) use the same records for partial rollback, [multi-level recovery](/multi-level-recovery/) undoes whole operations by their inverses, and [instant restart](/instant-restart/) opens the database before redo and undo are done.
6. **When the disk is lost, or the data is wrong.** [Media recovery](/media-recovery/) from an archive copy and the log, and [point-in-time recovery](/point-in-time-recovery/), which stops the replay before a mistake.
7. **Logging for main memory and new storage.** [Command logging](/command-logging/) for deterministic in-memory systems, and [write-behind logging](/write-behind-logging/) for non-volatile memory.

## A first reading

For a first reading, take these ten entries in order: the crash recovery problem, the steal and force policies, write-ahead logging, undo/redo logging, the log sequence number, checkpointing, group commit, ARIES recovery, the compensation log record and media recovery. Together they give the problem, the two rules of the log, the classic algorithm, the one used in practice, and the step from a crash to the loss of a disk.

Shadow paging is worth reading next for the contrast, since it reaches atomicity with no log of page contents at all. Physiological and logical logging explain what the records of ARIES really hold, and the fuzzy checkpoint gives the proof of the checkpoint that ARIES takes. The differential file, multi-level recovery, instant restart, command logging and write-behind logging can wait until the basic picture is clear.

## Before you start

You need the [ACID properties](/acid-properties/) and the strict schedules of [strict two-phase locking](/strict-two-phase-locking/) from Chapter 40.5: recovery assumes that no transaction reads or overwrites a change that is not committed. The pages and buffers are those of the [B+ tree](/b-plus-tree/) and of the [external memory model](/external-memory-model/), from Volumes 3 and 1, and the differential file uses the [Bloom filter](/bloom-filter/) of Volume 3. Write-behind logging assumes [multiversion concurrency control](/multiversion-concurrency-control/), also from Chapter 40.5.

Logging is not only a database idea. The [undo log](/undo-log/) and the [redo log](/redo-log/) of transactional memory, in Volume 22, are the same two repairs in main memory. The [log-structured merge tree](/log-structured-merge-tree/) of Volume 3 writes a log first and builds its index from it later, much as a differential file does. When the log is replicated across machines, committing a record is a consensus problem, solved by [Paxos](/paxos/) or [Raft](/raft/) in Volume 21, and committing across several databases uses [two-phase commit](/two-phase-commit/).
