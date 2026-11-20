1. ◦ For each of the four combinations of the [steal and force policies](/steal-and-force-policies/), say whether recovery after a system crash needs undo, redo, both or neither, and whether the log must hold before images, after images or both.

2. ◦ Which of these log records can be redone twice with no harm: (a) set $A$ to 70; (b) subtract 30 from $A$; (c) put the bytes $b$ at offset 100 of page $P$; (d) insert a row into the first free slot of page $P$? For the others, say what the [crash recovery problem](/crash-recovery/) entry adds to make redo safe.

3. ◦ After a crash, the log of an [ARIES](/aries-recovery/) system holds: 10 update $T_1$ on $P_1$; 20 update $T_2$ on $P_2$; 30 begin checkpoint; 40 end checkpoint with transaction table $\{T_1{:}10, T_2{:}20\}$ and dirty page table $\{P_1{:}10\}$; 50 update $T_1$ on $P_3$; 60 commit $T_2$; 70 update $T_3$ on $P_1$; 80 update $T_1$ on $P_2$. Give the transaction table and dirty page table after analysis, the LSN where redo starts, the redo records that are skipped without fetching a page, and the order of the undo pass. How many compensation records does it write?

4. ◦ A log device takes $D = 5$ time units per write, and commits arrive at times 0, 1, 3, 4, 7 and 12. Under [group commit](/group-commit/) with no waiting, a write starts whenever the device is free and records are waiting. Give the writes, the records each one holds, and the latency of each commit. Compare with one write per commit.

5. ◦ In [shadow paging](/shadow-paging/), a transaction has written three new pages and two new page table blocks when the system crashes, before the root is switched. What does restart do? What if the crash comes just after the root switch?

6. ◦ A fuzzy [checkpoint](/checkpointing/) holds the dirty page table $\{P_1{:}40, P_2{:}25, P_3{:}60\}$ and two active transactions, both losers, whose first log records are at 15 and 50. No page is dirtied after the checkpoint. At which LSN does redo start, and how far back does undo read the log?

7. ◦ Say which rule of [write-ahead logging](/write-ahead-logging/) each event breaks, if any, and give a crash that shows the harm: (a) the stable log ends at LSN 100 and the buffer writes a page with pageLSN 120; (b) a commit returns while its commit record is still in the log tail in memory; (c) the stable log ends at 150 and the buffer writes a page with pageLSN 140.

8. ◦ Run the recovery of [undo/redo logging](/undo-redo-logging/) on this log, with no checkpoint: 1 $\langle$START $T_1\rangle$; 2 $\langle T_1, A, 10, 11\rangle$; 3 $\langle$START $T_2\rangle$; 4 $\langle T_2, B, 20, 21\rangle$; 5 $\langle$COMMIT $T_1\rangle$; 6 $\langle T_2, C, 30, 31\rangle$; 7 $\langle T_2, A, 11, 12\rangle$; then a crash. On disk at the crash, $A = 12$, $B = 20$ and $C = 31$. Give the work of the undo pass and of the redo pass, the final values, and the record that recovery appends to the log. Would the result change if the disk had held $A = 10$, $B = 21$ and $C = 30$?

9. ◦ A transaction writes update 1, sets savepoint $S_1$, writes update 2, sets savepoint $S_2$, writes updates 3 and 4, rolls back to $S_2$, writes one more update, rolls back to $S_1$ and commits. Number the log records in order, as in the [savepoint](/savepoint/) entry, with nothing logged for a savepoint. Give each [compensation log record](/compensation-log-record/) with the update it undoes and its undoNextLSN. Which updates remain at the commit, and which of $S_1$ and $S_2$ can still be the target of a rollback after the second one?

10. ◦ A [differential file](/differential-file/) holds $n = 1000$ changed keys, and its Bloom filter has $m = 8000$ bits. With the estimate $p \approx (1 - e^{-kn/m})^k$ for the false-positive rate, compute $p$ for $k = 1$, $3$ and $6$ hash functions, and find the best whole number $k$. With that $k$, about how many of $100\,000$ lookups of unchanged keys read the differential file for nothing?

11. • In exercise 3, the system crashes again during undo, just after it has written the compensation record 90 for record 80, the compensation record 100 for record 70 and the end record 110 of $T_3$. Give the undoNext field of each compensation record, and the work of the next restart. How many compensation records are written over both restarts?

12. • After analysis, the dirty page table is $\{P_1{:}30, P_2{:}60, P_3{:}80\}$, and the pages on disk have pageLSN 40, 50 and 10. The log from the redo point holds updates 30 and 40 on $P_1$, 50 and 60 and 70 on $P_2$, 80 on $P_3$ and 90 on $P_1$. For each record, say whether redo skips it without fetching the page, fetches the page and skips it, or applies it.

13. • A system redoes only the updates of winners, then undoes the losers with logical undo records such as "subtract 5 from $x$". Page $P$ holds $x$ and $y$, and the log holds 10, $T_1$ adds 5 to $x$ on $P$, and 20, $T_2$ adds 3 to $y$ on $P$, with $T_2$ committed and $T_1$ a loser. Page $P$ reached the disk with neither change. Show that this recovery leaves $x$ wrong, and that repeating history, as ARIES does, gives the right state.

14. • Under no-steal and no-force, design a recovery that reads the log forward once. Which records does it need, which transactions does it redo, and what does no-steal demand from the buffer pool?

15. • A hot page is changed by 1000 committed transactions per second. Count the writes of that page per second under force, and under no-force with the page written once per checkpoint, every 60 seconds. What does no-force pay instead?

16. • Commits arrive at the times $0, 1, 2, \ldots$, one per millisecond, and a log write takes $D = 8$ ms. Under group commit with no waiting, find the number of records in each write in the steady state and the largest latency. Compare with the bound of the group commit entry.

17. • Name the commit point of a transaction under shadow paging, under write-ahead logging, and under no-steal with force. For each, give a crash just before and just after the commit point, and say what restart does.

18. • ARIES starts analysis at the begin_checkpoint record named by the master record, not at the end_checkpoint record. Give a log in which starting at end_checkpoint leaves a dirty page or an active transaction out of the tables, and say what goes wrong in redo or undo.

19. • A fuzzy archive copy, as in the [media recovery](/media-recovery/) entry, begins when the dirty page table is $\{P_1{:}40, P_2{:}55\}$ and the log ends at 60. A transaction $T$, active then, wrote its first update at 30 on page $P_3$, and the buffer stole $P_3$ to disk at 35, before the copy began. $T$ never commits, and the disk fails later. (a) At which LSN must redo of the restored copy start, and why not at 60? (b) Show that undoing $T$ needs a log record from before that LSN, and say how far back the archived log must reach.

20. • A counter $x = 50$ sits on page $P$. Under [multi-level recovery](/multi-level-recovery/), $T_1$ runs the operation ADD$(x, 10)$ and releases its page lock when the operation ends, keeping a logical lock that commutes with other additions; $T_2$ then runs ADD$(x, -20)$ and commits; the system crashes before $T_1$ commits. (a) Redo repeats history. What does undoing $T_1$ by the before image of its page write give, and what is the right value? (b) $T_1$'s next operation, an insert into a B+ tree, was cut off after it had split a leaf but before it placed the key. Why must this operation be undone physically, page by page, and not by its logical inverse, a delete of the key?

21. • Under [instant restart](/instant-restart/), suppose the system opened to new transactions before it had reacquired the locks of the losers. A loser $T_2$ wrote $x$ on page $P$, and the buffer stole $P$ to disk before the crash. Give a run in which a new transaction reads a value that never commits, even though every page is redone on first access. Then show how the reacquired lock on $x$ prevents it.

22. ★ A loser has $u$ update records. Prove that, however many times the system crashes during recovery, ARIES writes at most $u$ compensation records for it in total. Show that a scheme that undoes compensation records as if they were updates can write an unbounded number.

23. ★ Assume that a page write is atomic and that a page's pageLSN is set together with each change applied to it. Prove that the redo pass of ARIES, with its pageLSN test, gives the same state whether it runs once or is interrupted by crashes and rerun any number of times.

24. ★ Two commits arrive at times 0 and 0.1, and $D = 10$. Find the largest latency when the first write starts at once, and when the device waits until 0.1. Then show that every waiting policy with a fixed wait $\tau > 0$ can be made worse than writing at once by some arrival sequence, and that writing at once can be made close to twice the best latency by another.

25. ★ Show that the estimate $(1 - e^{-kn/m})^k$ of the differential file entry, as a function of a real $k > 0$, is smallest at $k = (m/n)\ln 2$, and that the smallest value is $2^{-k} = (2^{-\ln 2})^{m/n} \approx 0.6185^{m/n}$. Check the value for $m = 10n$ against the entry.
