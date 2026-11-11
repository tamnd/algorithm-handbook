1. A quorum has 5 processes. There are $\binom{9}{5} = 126$ minimal quorums, and the group survives 4 crashes.

3. There are $3n + nl = 15 + 15 = 30$ messages and 4 delays: PREPARE, PROMISE, ACCEPT, ACCEPTED. With phase 1 done, only ACCEPT and ACCEPTED remain, so $n + nl = 20$ messages and 2 delays.

5. (a) 6, any $f < n$. (b) 3, since $n > 2f$. (c) None: by FLP not even one crash. (d) 3. (e) 2, since $n > 3f$.

6. Two-phase commit sends $4n = 20$ messages, a participant learns the decision after 3 delays, and $n + 1 = 6$ forced writes come before the decision. Three-phase commit sends $5n = 25$ messages and takes 5 delays.

10. Compare the last terms first and the lengths only on a tie. A and D get all five votes. C gets only B, E and itself, which is exactly a majority, so it can win, but only with both B and E. B gets only E and itself, and E only itself.

11. Any 3 crashes miss some row and some column, and that row and column form a live quorum. Four crashes with one in each row leave no full row.

12. Look for the sets of weight at least 4. The heavy replica with one light replica makes four such sets, and the four light replicas make the fifth.

16. Each phase waits for $n - f = 4$ messages. A process proposes $v$ only if more than $n/2$ of its reports carry $v$, so all 4 of them must. Two sets of more than $n/2$ reports share a sender, and that sender sent only one report in the round.

20. The old majority $\{1, 2\}$ and the new majority $\{3, 4\}$ are disjoint. A joint quorum needs 2 of $\{1, 2, 3\}$ and 2 of $\{2, 3, 4\}$, and $\{2, 3\}$ already has both.

22. A proposer takes the value with the largest ballot among its promises, so it proposes $x$ in the first case and $y$ in the second. If $x$ had been chosen in ballot $(1, 1)$, the safety invariant of Paxos would force every proposal in a larger ballot to be $x$, yet ballot $(2, 2)$ proposed $y$. For $y$ to be chosen, two acceptors must have accepted it in ballot $(2, 2)$, but the last ballot of $A_1$ is smaller and $A_3$ accepted nothing.

23. Any fast quorum of 4 meets $\{A_0, A_1, A_2, A_3\}$ in at least 3 acceptors, but only two of these voted for each value. So neither value passes the O4 test, and the coordinator may send any proposed value. A value needs 4 votes in a fast round, and each value has at most 3 possible votes.

24. After some time, every crashed process is suspected for ever by every correct process, and no correct process is suspected. From then on, every correct process trusts the correct process with the smallest id.

25. If each of the $n - 1$ rounds has a crash, then only one process is left, and it agrees with itself. Otherwise some round has no crash, and after it all live processes hold the same set.

26. Split the processes into two pairs. If one pair crashes at the start, the other pair must decide alone, and with inputs 0 on one side and 1 on the other the pairs decide 0 and 1. Now delay all messages between the pairs instead of crashing them. The detector may suspect the other pair for a finite time, so neither pair can tell the two runs apart, and they decide differently.
