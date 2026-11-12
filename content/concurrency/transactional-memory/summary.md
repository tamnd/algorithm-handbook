## What to remember

- Two concurrent [transactions](/transaction/) [conflict](/transaction-conflict/) when they access one location and at least one writes it. Locks kept per stripe add false conflicts: with $s$ stripes, two words share one with probability about $1/s$.
- Serializability of the committed transactions is too weak: a doomed transaction can read a state that no serial order produces, then divide by zero or loop for ever as a [zombie](/zombie-transactions/). [Opacity](/opacity/) asks that every transaction, aborted and live ones included, read the values of one serial order that respects real time.
- With invisible reads, checking the whole read set after each read costs $r(r+1)/2$ checks for a writer that reads $r$ words. A [global version clock](/global-version-clock/) cuts this to one check per read. A 64-bit clock at $10^9$ commits per second lasts about 584 years.
- An STM chooses a [redo log](/redo-log/) or an [undo log](/undo-log/), finds conflicts at the access or at commit, and locks at the first write or at commit. With invisible reads, read-write conflicts show up only at validation.
- [Privatization](/privatization-safety/) fails in two ways: a committed transaction can still be writing back, and a doomed transaction can write in place and roll back. TL2, TinySTM and SwissTM are unsafe in their basic form; NOrec and hardware transactions are safe.
- A [contention manager](/contention-management/) affects progress, never safety. Polite, Karma and Polka can livelock. [Greedy](/greedy-contention-manager/) commits every transaction after a bounded delay, with makespan within a factor $s(s+1)+2$ of optimal for $s$ shared objects; a later analysis gives $O(s)$, the best order for deterministic work-conserving managers.
- [Best-effort HTM](/best-effort-htm/) may abort a transaction that runs alone, so software must provide a fallback: a lock that each hardware transaction reads, as in [lock elision](/transactional-lock-elision/), or an STM, as in [hybrid TM](/hybrid-transactional-memory/). Intel has disabled [TSX](/intel-tsx/) by microcode on many processors.
- By the [disjoint-access-parallel lower bound](/disjoint-access-parallel-stm-lower-bound/), a strictly serializable TM cannot be disjoint-access parallel and also have read-only transactions that are invisible and always commit. Practical STMs share a global clock or lock, or let readers abort.
- A transaction that calls [retry](/retry-and-orelse/) sleeps until a location it read changes; an orElse waits on the union of both branches' read sets. [Transactional boosting](/transactional-boosting/) and [open nesting](/open-nested-transactions/) work on abstract operations, with abstract locks and inverses.

## The software designs side by side

| Design | Shared metadata | Read validation | Writes | Progress | Privatization safe |
|---|---|---|---|---|---|
| [DSTM](/dstm/) | locator per object, status word per transaction | whole read table at every open: $r(r+1)/2$ checks, $r$ more at commit | private copy acquired at open; commit by one CAS on the status | obstruction-free, not lock-free | not discussed |
| [TL2](/tl2/) | versioned lock per stripe, global clock | each read against $rv$; read set once at commit | redo log, locks at commit | blocking, deadlock-free, can livelock | no |
| [TinySTM](/tinystm/) | versioned lock per stripe, global clock | each read against the snapshot, extended instead of aborting | lock at first write; redo or undo log | blocking, not obstruction-free | no |
| [SwissTM](/swisstm/) | write lock and read lock per word, global clock | as TinySTM; read set at commit | redo log; write lock at first write, read locks at commit | blocking, deadlock-free | no |
| [NOrec](/norec/) | one global sequence lock | by value, only when the lock has moved | redo log; one writer commits at a time | blocking, livelock-free | yes |
| [Multi-version](/multi-version-stm/) | version list per word, global clock, commit lock | none for read-only transactions; writers at commit | new versions pushed under the commit lock | read-only transactions never abort | not discussed |
| Best-effort HTM | cache lines and the coherence protocol | none: a conflicting access aborts | held in the cache until commit | none without a fallback | yes |

: The main designs. $r$ counts the objects or words read and $rv$ is the clock value at the start; "not discussed" means the entry does not say.

## Choosing a method

On hardware with a working HTM, use lock elision for existing lock code with short critical sections. For transactions larger than the cache, use a hybrid with NOrec as the software path.

For a pure STM with few writers and short transactions, NOrec is the default: it has the lowest cost per read and is privatization safe without fences. When many threads write disjoint data at once, its serialized write-back becomes the bottleneck; TL2 or TinySTM scale better, with a quiescence fence after each privatizing transaction. Choose SwissTM when short and long transactions run together, and a multi-version STM when long read-only transactions keep aborting.
