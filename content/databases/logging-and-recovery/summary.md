## What to remember

- After a crash, recovery must leave the effects of exactly the **committed** transactions. Each transaction commits at one atomic event on stable storage, its commit point; in a logging system, that is the commit record reaching the stable log.
- **Steal** lets a page with uncommitted changes go to disk, so recovery needs undo. **No-force** lets commit return before the changed pages are written, so recovery needs redo. Steal with no-force is the fastest choice and needs both. **Shadow paging** needs neither, since it never overwrites a page in use.
- **Write-ahead logging** has two rules. The WAL rule: the log record of a change is on stable storage before the page it changes. The commit rule: all of a transaction's records are stable before its commit returns. Redo applies a record $r$ only if the page's pageLSN $<$ lsn($r$), so each change is applied once, even one that is not idempotent.
- **Undo/redo logging** keeps a before and an after image in each record. In the classic form, where aborts are not logged, recovery undoes the losers backwards first and then redoes the winners; the other order can leave a loser's value in place.
- A **physical** record names bytes, a **physiological** record names a page and an operation inside it, and a **logical** record names an operation on the database. Logical undo is correct only if the inverse commutes with the operations of other transactions.
- A **checkpoint** bounds the log that restart reads. A fuzzy checkpoint writes only the transaction table and the dirty page table, so redo may start before the checkpoint, at the smallest recLSN. **Group commit** makes one log write durable for many commit records; with no waiting, no commit waits more than about $2D$ for a write time $D$.
- **ARIES** runs analysis, redo and undo. Redo repeats history, the changes of losers included, and undo then rolls back the losers in one backward sweep, writing a **compensation log record** for each change it undoes. A compensation record is redone but never undone, so each update is undone at most once over any number of crashes. ARIES is correct under the WAL rule and its other rules.
- **Media recovery** restores an archive copy and replays the log from the copy's start LSN; a checkpoint does not shorten that replay. **Point-in-time recovery** stops the replay just before the first commit after the target time and rolls back the transactions still open there.
- **Command logging** logs only the requests of a deterministic system, and recovery replays them from a transaction-consistent snapshot. **Write-behind logging** writes the data to non-volatile memory first and logs only ranges of commit timestamps, so restart needs no redo and no undo. Their gains are measurements.

## The methods side by side

| Method | Undo | Redo | Commit costs | Restart reads |
|---|---|---|---|---|
| [No-steal, force](/steal-and-force-policies/) | none | none | write all changed pages | nothing, if the force is atomic |
| [Shadow paging](/shadow-paging/) | none | none | write new pages, table blocks and the root | the root |
| [Undo/redo logging](/undo-redo-logging/) | before images, first | after images, second | one log write | back to the oldest start in the checkpoint list |
| WAL with [fuzzy checkpoints](/fuzzy-checkpoint/) | from the log | from the log | one log write | the log from the smallest recLSN |
| [ARIES](/aries-recovery/) | logical or physical, with CLRs | repeats history | one log write, shared by [group commit](/group-commit/) | from the smallest recLSN |
| [Instant restart](/instant-restart/) | on demand, per loser | on demand, per page | as ARIES | analysis only, before opening |
| [Command logging](/command-logging/) | none | replay of requests | one small record per transaction | the log since the snapshot |
| [Write-behind logging](/write-behind-logging/) | none | none | persist the data, then a timestamp record | the last log record |

: The recovery methods of the chapter. The log methods move work from commit time to restart time. Instant restart does the same work as ARIES, in a different order.

## How to choose

Almost every general-purpose system uses ARIES or a close variant: steal and no-force, physiological redo, fuzzy checkpoints and group commit. Shadow paging, as copy-on-write, suits embedded stores with one writer at a time. Choose the checkpoint interval from the restart time you can accept, since redo reads the log from the oldest recLSN. Never acknowledge a commit before its record is durable; group commit recovers most of the speed. Keep archive copies and the archived log on other devices than the database. Command logging pays only when every transaction is deterministic, and write-behind logging only on byte-addressable non-volatile memory, not on disks or SSDs.
