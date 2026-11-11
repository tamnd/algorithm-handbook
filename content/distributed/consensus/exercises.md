1. ◦ A group of $n = 9$ processes uses majority quorums. How many processes are in a quorum, how many minimal quorums are there, and how many crashes can the group survive with some quorum still alive?

2. ◦ Ballots are pairs (round, process id), compared first by round. Put the ballots $(3, 1)$, $(2, 7)$, $(3, 0)$, $(2, 5)$ and $(4, 0)$ in increasing order, and name the process that owns the largest one.

3. ◦ A run of Paxos has 5 acceptors, 3 learners and one proposer, and nothing fails. How many messages are sent and how many message delays pass before the learners learn the value? Answer again for the case in which phase 1 is already done.

4. ◦ FloodSet runs with $n = 6$ processes and tolerates $f = 2$ crashes. How many rounds does it take, and what is the largest number of messages it can send?

5. ◦ For $n = 7$ processes, give the largest number of faulty processes for which consensus is solvable in each setting: (a) synchronous rounds with crashes; (b) partial synchrony with crashes; (c) asynchronous with crashes and a deterministic protocol; (d) asynchronous with crashes and coin flips; (e) synchronous rounds with Byzantine faults and no signatures.

6. ◦ Two-phase commit runs with 5 participants and no failures. How many messages does it send, after how many message delays does a participant learn the decision, and how many forced writes happen before the decision is known? Give the first two numbers for three-phase commit as well.

7. ◦ A proof-of-work puzzle succeeds with probability $p = 2^{-20}$ per hash. What is the expected number of hashes, and what is the probability that $2^{20}$ hashes are not enough? Give the second answer to three decimals.

8. ◦ A leader holds a lease of $T = 5$ seconds, and the clocks have a drift bound of $\rho = 50$ parts per million. For how long may the leader serve reads on its own clock, and how large is the safety margin?

9. ◦ Given total-order broadcast, each process broadcasts its input and decides the value of the first message it delivers. Which property of total-order broadcast gives agreement, and which gives validity?

10. • Five Raft servers have logs whose last entries are, as (term, index): A $(3, 7)$, B $(2, 9)$, C $(3, 5)$, D $(3, 7)$ and E $(1, 4)$. Each server votes for itself and for any candidate whose log is at least as up to date as its own. Which servers can win an election, and which voters does each winner need?

11. • Sixteen nodes form a $4 \times 4$ grid, and a quorum is one full row together with one full column. How large is a quorum, and how does it compare with a majority? What is the smallest number of crashes that leaves no quorum alive, and how many does a majority quorum system survive?

12. • Five replicas get the votes 3, 1, 1, 1 and 1, so $V = 7$. Choose the smallest write threshold $w$ with $2w > V$ and then the smallest read threshold $r$ with $r + w > V$. List the minimal write quorums, and find the smallest number of crashes that makes writes impossible.

13. • A quorum system must give every two quorums a common member and must keep some quorum alive after any $f$ crashes. Show that it needs at least $2f + 1$ members.

14. • Flexible Paxos runs on 7 acceptors with counting quorums. Choose $q_1$ and $q_2$ so that the steady state survives 4 crashed acceptors. How many crashes does a leader change then survive?

15. • Fast Paxos runs on $n = 8$ acceptors with majority classic quorums. What is the classic quorum size, and what is the smallest fast quorum size? If both kinds of quorum must have the same size, what is that size?

16. • Ben-Or's algorithm runs with $n = 7$ and $f = 3$. How many messages does a process wait for in each phase, how many equal reports does it need before it proposes a value, and how many equal proposals does it need to decide? Explain why two different values are never proposed in the same round.

17. • Take $n = 10$ processes in synchronous rounds with up to $f = 5$ crashes. (a) How many rounds does FloodSet take? (b) How many rounds does an early-stopping algorithm take in a run with one actual crash? (c) How many rounds does FloodMin take for 2-set agreement? (d) Is 2-set agreement solvable with the same $f$ in the asynchronous model?

18. • Six processes have inputs 1 to 6. Each one waits for the values of $n - f = 4$ processes, its own included, and decides the smallest value it has. Which values can be decided? Give a run in which three different values are decided.

19. • The approximate agreement algorithm runs with $n = 7$ and $t = 2$. The correct inputs span 64, and the target is $\varepsilon = 0.5$. Is $n$ large enough? How many rounds and how many messages are needed?

20. • A group moves from the configuration $\{1, 2, 3\}$ to $\{2, 3, 4\}$. Show that a direct switch is unsafe, and list the minimal quorums of the joint configuration, in which a quorum must hold a majority of each.

21. • In Nakamoto's analysis, an attacker with a share $q = 0.25$ of the hash power is $z$ blocks behind. With what probability does it ever catch up from $z = 6$? What is the smallest $z$ that brings this below 0.001?

22. ★ A Paxos run has three acceptors. $A_1$ last accepted $x$ in ballot $(1, 1)$, $A_2$ last accepted $y$ in ballot $(2, 2)$, and $A_3$ has accepted nothing. A proposer starts ballot $(3, 0)$. Which value must it propose if its promises come from $A_1$ and $A_3$, and which if they come from $A_2$ and $A_3$? Show that neither $x$ nor $y$ can have been chosen yet.

23. ★ Fast Paxos runs on 5 acceptors with $q_c = 3$ and $q_f = 4$. In fast round 0, $A_0$ and $A_1$ vote $x$, $A_2$ and $A_3$ vote $y$, and the coordinator hears nothing from $A_4$. Which values may the coordinator send in round 1? Could $x$ have been chosen in round 0?

24. ★ Show that the rule "trust the process with the smallest id that is not suspected" turns an eventually perfect failure detector into $\Omega$.

25. ★ Show that FloodSet with $f = n - 1$ is still correct when it stops after $f$ rounds instead of $f + 1$.

26. ★ Show that no consensus algorithm for $n = 4$ processes with an eventually perfect failure detector tolerates $f = 2$ crashes.
