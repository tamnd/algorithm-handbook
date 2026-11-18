1. ◦ For each of the four combinations of the [steal and force policies](/steal-and-force-policies/), say whether recovery after a system crash needs undo, redo, both or neither, and whether the log must hold before images, after images or both.

2. ◦ Which of these log records can be redone twice with no harm: (a) set $A$ to 70; (b) subtract 30 from $A$; (c) put the bytes $b$ at offset 100 of page $P$; (d) insert a row into the first free slot of page $P$? For the others, say what the [crash recovery problem](/crash-recovery/) entry adds to make redo safe.

3. ◦ After a crash, the log of an [ARIES](/aries-recovery/) system holds: 10 update $T_1$ on $P_1$; 20 update $T_2$ on $P_2$; 30 begin checkpoint; 40 end checkpoint with transaction table $\{T_1{:}10, T_2{:}20\}$ and dirty page table $\{P_1{:}10\}$; 50 update $T_1$ on $P_3$; 60 commit $T_2$; 70 update $T_3$ on $P_1$; 80 update $T_1$ on $P_2$. Give the transaction table and dirty page table after analysis, the LSN where redo starts, the redo records that are skipped without fetching a page, and the order of the undo pass. How many compensation records does it write?

4. ◦ A log device takes $D = 5$ time units per write, and commits arrive at times 0, 1, 3, 4, 7 and 12. Under [group commit](/group-commit/) with no waiting, a write starts whenever the device is free and records are waiting. Give the writes, the records each one holds, and the latency of each commit. Compare with one write per commit.

5. ◦ In [shadow paging](/shadow-paging/), a transaction has written three new pages and two new page table blocks when the system crashes, before the root is switched. What does restart do? What if the crash comes just after the root switch?

6. ◦ A fuzzy [checkpoint](/checkpointing/) holds the dirty page table $\{P_1{:}40, P_2{:}25, P_3{:}60\}$ and two active transactions, both losers, whose first log records are at 15 and 50. No page is dirtied after the checkpoint. At which LSN does redo start, and how far back does undo read the log?

7. ◦ Say which rule of [write-ahead logging](/write-ahead-logging/) each event breaks, if any, and give a crash that shows the harm: (a) the stable log ends at LSN 100 and the buffer writes a page with pageLSN 120; (b) a commit returns while its commit record is still in the log tail in memory; (c) the stable log ends at 150 and the buffer writes a page with pageLSN 140.

8. • In exercise 3, the system crashes again during undo, just after it has written the compensation record 90 for record 80, the compensation record 100 for record 70 and the end record 110 of $T_3$. Give the undoNext field of each compensation record, and the work of the next restart. How many compensation records are written over both restarts?

9. • After analysis, the dirty page table is $\{P_1{:}30, P_2{:}60, P_3{:}80\}$, and the pages on disk have pageLSN 40, 50 and 10. The log from the redo point holds updates 30 and 40 on $P_1$, 50 and 60 and 70 on $P_2$, 80 on $P_3$ and 90 on $P_1$. For each record, say whether redo skips it without fetching the page, fetches the page and skips it, or applies it.

10. • A system redoes only the updates of winners, then undoes the losers with logical undo records such as "subtract 5 from $x$". Page $P$ holds $x$ and $y$, and the log holds 10, $T_1$ adds 5 to $x$ on $P$, and 20, $T_2$ adds 3 to $y$ on $P$, with $T_2$ committed and $T_1$ a loser. Page $P$ reached the disk with neither change. Show that this recovery leaves $x$ wrong, and that repeating history, as ARIES does, gives the right state.

11. • Under no-steal and no-force, design a recovery that reads the log forward once. Which records does it need, which transactions does it redo, and what does no-steal demand from the buffer pool?

12. • A hot page is changed by 1000 committed transactions per second. Count the writes of that page per second under force, and under no-force with the page written once per checkpoint, every 60 seconds. What does no-force pay instead?

13. • Commits arrive at the times $0, 1, 2, \ldots$, one per millisecond, and a log write takes $D = 8$ ms. Under group commit with no waiting, find the number of records in each write in the steady state and the largest latency. Compare with the bound of the group commit entry.

14. • Name the commit point of a transaction under shadow paging, under write-ahead logging, and under no-steal with force. For each, give a crash just before and just after the commit point, and say what restart does.

15. • ARIES starts analysis at the begin_checkpoint record named by the master record, not at the end_checkpoint record. Give a log in which starting at end_checkpoint leaves a dirty page or an active transaction out of the tables, and say what goes wrong in redo or undo.

16. ★ A loser has $u$ update records. Prove that, however many times the system crashes during recovery, ARIES writes at most $u$ compensation records for it in total. Show that a scheme that undoes compensation records as if they were updates can write an unbounded number.

17. ★ Assume that a page write is atomic and that a page's pageLSN is set together with each change applied to it. Prove that the redo pass of ARIES, with its pageLSN test, gives the same state whether it runs once or is interrupted by crashes and rerun any number of times.

18. ★ Two commits arrive at times 0 and 0.1, and $D = 10$. Find the largest latency when the first write starts at once, and when the device waits until 0.1. Then show that every waiting policy with a fixed wait $\tau > 0$ can be made worse than writing at once by some arrival sequence, and that writing at once can be made close to twice the best latency by another.
