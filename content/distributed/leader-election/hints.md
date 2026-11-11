1. The election messages make $2 + 1 + 6 + 1 + 4 + 1 = 15$ hops, the announcement adds 6, and the total is 21. The identifier 6 wins.

3. (a) 4 rounds and $2md = 2 \cdot 12 \cdot 4 = 96$ messages. (b) $2 \cdot 12 \cdot 3 = 72$ messages. The corner holding 8 is at distance 4 from the corner holding 9, so it never hears of 9, and two processes believe they are the leader.

4. The survivors are 9, 7, 8, 6 after round 1, then 9 and 8, then 9 alone. Four rounds cost $2n = 16$ each, 64 messages, and the announcement makes 72.

6. Process 3 noticing gives $3 + 2 + 1 = 6$ ELECTION, 3 OK and 4 COORDINATOR, 13 in all. Process 5 noticing gives 1 ELECTION and 4 COORDINATOR, 5 in all.

10. The smallest identifier, 3, wins. Its token goes round once, so 4 messages are sent, and the election ends after $n \cdot 3 = 12$ rounds.

12. In Franklin's algorithm only the process holding $n$ survives round 1, and one last round follows, $4n$ messages in all. Chang-Roberts sends $2n - 1$ in the first direction and $n(n+1)/2$ in the other: 32, 15 and 36 at $n = 8$.

14. Peterson sends $3 \cdot 16 + 8 = 56$ messages, and $p_0$, which holds 2, receives its own final value 9 and is the leader. Dolev-Klawe-Rodeh adds the found trip, 64 in all, and $p_1$, which holds 9, becomes the leader.

16. The centre wakes the 6 leaves, each leaf reports at once, and the centre reports to the leaf it hears from last. Both reports on that link cross, so the centre and that leaf are saturated.

21. Two processes that both keep their own identifiers must be more than $d$ apart, since otherwise the larger one reaches the smaller. On a path of 9 this allows at most $\lceil 9/3 \rceil = 3$ of them, reached for example by 1, 2, 5, 3, 4, 8, 6, 7, 9.

22. In round 1 the survivors are the local maxima, which are the processes at odd positions. Show that, read round the ring, their values minus $n/2$ form the bit-reversal ring of size $n/2$. Induction on $k$ then gives $k$ rounds of $2n$ messages with at least two candidates, and one last round of $2n$.

23. With three active processes the largest draw is unique with probability $5/9$, shared by two with probability $1/3$ and by all three with probability $1/9$. From two active processes it is unique with probability $2/3$. Solve the two linear equations for the expected rounds; the answers are $27/16$ for $n = 3$ and $2$ for $n = 2$.

24. All processes of an anonymous ring are in the same state after every round, by induction on rounds. A ring of size $2n$ is then in the same states as a ring of size $n$, so their outputs agree, and one of them is wrong.

25. A port-preserving automorphism would have to swap $b$ and $c$, which needs $b$ and $c$ to give the middle link the same number. When their numbers differ, every process has a different view, and the inner process whose middle port is 1 can win.

26. Phase 0 always costs 12 messages. The phase-1 candidates are the local maxima, and there are two of them exactly when 3 and 4 sit opposite each other.
