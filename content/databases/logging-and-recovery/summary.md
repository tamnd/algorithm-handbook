## What to remember

- After a crash, recovery must leave the effects of exactly the **committed** transactions. Each transaction commits at one atomic event on stable storage, its commit point; in a logging system, that is the commit record reaching the stable log.
- **Steal** lets a page with uncommitted changes go to disk, so recovery needs undo. **No-force** lets commit return before the changed pages are written, so recovery needs redo. Steal and no-force are the fastest choices in normal operation and need both repairs. No-steal with force needs neither in principle, but forcing several pages is not atomic, so it still needs some other mechanism.
- **Shadow paging** writes changed pages to free slots and commits by one atomic switch of the root pointer. It needs no undo and no redo of page contents, but it scatters pages, copies page table blocks at each commit, and does not support record-level locking by itself.
- **Write-ahead logging** has two rules. The WAL rule: the log record of a change is on stable storage before the page it changes. The commit rule: all of a transaction's records are on stable storage before its commit returns. Records must be applied idempotently; a pageLSN on each page tells redo which changes the page already has.
- A **checkpoint** bounds the log that restart reads. A fuzzy checkpoint writes only the transaction table and the dirty page table, so redo may start before the checkpoint, at the smallest recLSN. The master record is written after the end of the checkpoint is on stable storage.
- **Group commit** makes one log write durable for many commit records. Under load, a write holds about $\lambda D$ records for commit rate $\lambda$ and write time $D$, and with no waiting no commit waits more than about $2D$. Throughputs depend on the device and are measurements.
- **ARIES** runs analysis, redo and undo. Redo repeats history, the changes of losers included, and undo then rolls back the losers in one backward sweep, writing a compensation record for each change it undoes. ARIES is correct under the WAL rule and its other rules, and a crash during recovery only repeats work: compensation records are redone and never undone, so the log grows by a bounded amount.

## The methods side by side

| Method | Undo | Redo | Commit costs | Restart reads |
|---|---|---|---|---|
| [No-steal, force](/steal-and-force-policies/) | none | none | write all changed pages | nothing, if the force is atomic |
| [Shadow paging](/shadow-paging/) | none | none | write new pages, table blocks and the root | the root |
| [WAL](/write-ahead-logging/), steal and no-force | from the log | from the log | one log write | the whole log |
| WAL with [checkpoints](/checkpointing/) | from the log | from the log | one log write | the log from the redo point |
| [Group commit](/group-commit/) | as WAL | as WAL | one log write shared by many | as WAL |
| [ARIES](/aries-recovery/) | logical or physical, with CLRs | repeats history | one log write | from the smallest recLSN |

: The recovery methods of the chapter. The log methods move work from commit time to restart time; checkpoints and group commit reduce the two costs that remain.

## How to choose

Almost every general-purpose system uses write-ahead logging with steal and no-force, fuzzy checkpoints and group commit, in the form of ARIES or close to it. Use it unless there is a strong reason not to. Shadow paging, in its copy-on-write form, suits embedded stores with one writer at a time, where a simple and fast restart matters more than write throughput. Choose the checkpoint interval from the restart time you can accept, since redo reads the log from the oldest recLSN. Never acknowledge a commit before its record is durable; group commit gets most of the speed of breaking that rule without breaking it.
