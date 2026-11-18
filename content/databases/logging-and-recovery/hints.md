1. Steal with no-force needs undo and redo, so before and after images. Steal with force needs only undo and before images. No-steal with no-force needs only redo and after images. No-steal with force needs neither, but only if the force of all pages at commit is atomic, which it is not on a plain disk.

2. Records (a) and (c) set a value and can be redone twice. Records (b) and (d) depend on the state they find: a second subtraction gives a wrong value, and a second insert takes another slot. The pageLSN of each page tells redo whether the change is already there.

3. Analysis gives the transaction table $\{T_1{:}80, T_3{:}70\}$, with $T_2$ ended, and the dirty page table $\{P_1{:}10, P_2{:}80, P_3{:}50\}$. Redo starts at 10 and skips 20 without a fetch, since $P_2$ has recLSN 80. Undo processes 80, 70, 50 and 10 in that order and writes four compensation records. A script that runs the three passes on this log checked the tables.

4. The writes are $[0, 5]$ with $T_1$, $[5, 10]$ with the commits at 1, 3 and 4, $[10, 15]$ with the commit at 7, and $[15, 20]$ with the commit at 12. The latencies are 5, 9, 7, 6, 8 and 8. With one write per commit they are 5, 9, 12, 16, 18 and 18. A script that simulates both policies checked these numbers.

6. Redo starts at 25, the smallest recLSN, which is older than the checkpoint. Undo follows each loser back to its first record, so it reads back to 15.

7. (a) breaks the WAL rule: after a crash the page holds a change whose log record, with its before image, is lost, so it cannot be undone. (b) breaks the commit rule: a crash loses a transaction that the client was told had committed. (c) is allowed.

8. The compensation record 90 has undoNext 50, the prevLSN of record 80; record 100 has none, since 70 was the first record of $T_3$. The next restart finds $T_1$ with last record 90, redoes the compensation records, and continues the undo of $T_1$ at 50 and then 10. That writes two more, so four in all, as without the second crash.

9. Record 30 and record 40 fetch $P_1$ and are skipped, since its pageLSN is 40. Record 50 is skipped without a fetch, since it is older than the recLSN 60 of $P_2$. Records 60 and 70 are applied, since the pageLSN of $P_2$ is 50. Record 80 is applied to $P_3$. Record 90 is applied to $P_1$.

10. Redo of record 20 alone sets $y$ and makes the pageLSN 20. The logical undo of record 10 then subtracts 5 from $x$, which never had the 5 added, so $x$ ends 5 too low. Repeating history redoes 10 and 20 first, so the undo removes a change that is really there.

13. Each write holds the 8 commits that arrived during the previous write. A commit that arrives 1 ms after a write starts waits 7 ms and then 8 ms, so the largest latency is 15 ms, below the bound $2D = 16$. A script simulated the first 1000 commits.

16. A compensation record is redone but never undone, and its undoNext skips the update it undid. So each update is undone at most once over all restarts.

18. Writing at once gives latencies 10 and 19.9; waiting until 0.1 gives 10.1 and 10. A single commit arriving alone pays $D + \tau$ under the waiting policy and $D$ when written at once. For writing at once, a second commit just after a write starts pays almost $2D$, while a policy that knew it was coming would pay about $D$.
