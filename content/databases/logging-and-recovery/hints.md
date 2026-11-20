1. Steal with no-force needs undo and redo, so before and after images. Steal with force needs only undo and before images. No-steal with no-force needs only redo and after images. No-steal with force needs neither, but only if the force of all pages at commit is atomic, which it is not on a plain disk.

2. Records (a) and (c) set a value and can be redone twice. Records (b) and (d) depend on the state they find: a second subtraction gives a wrong value, and a second insert takes another slot. The pageLSN of each page tells redo whether the change is already there.

3. Analysis gives the transaction table $\{T_1{:}80, T_3{:}70\}$, with $T_2$ ended, and the dirty page table $\{P_1{:}10, P_2{:}80, P_3{:}50\}$. Redo starts at 10 and skips 20 without a fetch, since $P_2$ has recLSN 80. Undo processes 80, 70, 50 and 10 in that order and writes four compensation records. A script that runs the three passes on this log checked the tables.

4. The writes are $[0, 5]$ with $T_1$, $[5, 10]$ with the commits at 1, 3 and 4, $[10, 15]$ with the commit at 7, and $[15, 20]$ with the commit at 12. The latencies are 5, 9, 7, 6, 8 and 8. With one write per commit they are 5, 9, 12, 16, 18 and 18. A script that simulates both policies checked these numbers.

6. Redo starts at 25, the smallest recLSN, which is older than the checkpoint. Undo follows each loser back to its first record, so it reads back to 15.

7. (a) breaks the WAL rule: after a crash the page holds a change whose log record, with its before image, is lost, so it cannot be undone. (b) breaks the commit rule: a crash loses a transaction that the client was told had committed. (c) is allowed.

8. The undo pass reads backwards and restores the before images of $T_2$: record 7 sets $A = 11$, record 6 sets $C = 30$, record 4 sets $B = 20$. The redo pass reads forwards and applies the after images of $T_1$: record 2 sets $A = 11$. The result is $A = 11$, $B = 20$, $C = 30$, and recovery appends $\langle$ABORT $T_2\rangle$. The disk state does not matter, since every item that a logged update touched is set from the log.

9. The log is 1, 2, 3, 4 (updates), 5 (CLR for 4, undoNext 3), 6 (CLR for 3, undoNext 2), 7 (update), 8 (CLR for 7, undoNext 6, the prevLSN of 7), then the walk jumps from the CLR 6 to its undoNext 2, and 9 (CLR for 2, undoNext 1), then 10 the commit. Only update 1 remains. $S_1$ is still valid; $S_2$, set after it, is gone.

10. $p \approx 11.75\%$ for $k = 1$, $3.06\%$ for $k = 3$ and $2.16\%$ for $k = 6$. The best whole number is $k = 6$, just ahead of $k = 5$ ($2.17\%$), near $(m/n)\ln 2 \approx 5.55$. About 2160 of the lookups read the differential file needlessly. A script computed the values.

11. The compensation record 90 has undoNext 50, the prevLSN of record 80; record 100 has none, since 70 was the first record of $T_3$. The next restart finds $T_1$ with last record 90, redoes the compensation records, and continues the undo of $T_1$ at 50 and then 10. That writes two more, so four in all, as without the second crash.

12. Record 30 and record 40 fetch $P_1$ and are skipped, since its pageLSN is 40. Record 50 is skipped without a fetch, since it is older than the recLSN 60 of $P_2$. Records 60 and 70 are applied, since the pageLSN of $P_2$ is 50. Record 80 is applied to $P_3$. Record 90 is applied to $P_1$.

13. Redo of record 20 alone sets $y$ and makes the pageLSN 20. The logical undo of record 10 then subtracts 5 from $x$, which never had the 5 added, so $x$ ends 5 too low. Repeating history redoes 10 and 20 first, so the undo removes a change that is really there.

16. Each write holds the 8 commits that arrived during the previous write. A commit that arrives 1 ms after a write starts waits 7 ms and then 8 ms, so the largest latency is 15 ms, below the bound $2D = 16$. A script simulated the first 1000 commits.

19. (a) Redo starts at 40, the smallest recLSN of the pages dirty when the copy began: the copy of $P_1$ may lack the changes from 40 on, which were only in the buffer. (b) The copy of $P_3$ holds $T$'s update of 30, and undo needs that record's before image, so the archived log must reach back to the first record of every transaction active when the copy began, here 30.

20. (a) After redo, $x = 40$. The before image of $T_1$'s write is 50, which erases $T_2$'s committed $-20$. The right value is 30, which the logical inverse ADD$(x, -10)$ gives, since additions commute. (b) A logical inverse assumes that its operation finished; a half-done insert has no key to delete and leaves the split behind. $T_1$ still held the page locks of the cut-off operation, so no one else has changed those pages, and physical undo of them is safe.

21. A new transaction fixes $P$, which is redone, and reads $x$ as written by $T_2$; then $T_2$ is rolled back, and the new transaction has read a value that never committed. With $T_2$'s lock on $x$ reacquired from the log, the new transaction's lock request waits, and in instant restart it makes $T_2$ roll back first.

22. A compensation record is redone but never undone, and its undoNext skips the update it undid. So each update is undone at most once over all restarts.

24. Writing at once gives latencies 10 and 19.9; waiting until 0.1 gives 10.1 and 10. A single commit arriving alone pays $D + \tau$ under the waiting policy and $D$ when written at once. For writing at once, a second commit just after a write starts pays almost $2D$, while a policy that knew it was coming would pay about $D$.

25. With $q = e^{-kn/m}$, the logarithm of the estimate is $k \ln(1 - q) = -(m/n)\ln q \,\ln(1 - q)$. This is symmetric under $q \leftrightarrow 1 - q$, and it is smallest at $q = 1/2$, that is, at $k = (m/n)\ln 2$. Then the estimate is $(1/2)^k$. For $m = 10n$ this is $0.6185^{10} \approx 0.0082$, as in the entry.
