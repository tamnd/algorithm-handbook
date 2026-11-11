1. ◦ A system has $n = 10$ processes. Give the largest number of Byzantine faults it can tolerate in each setting: (a) synchronous broadcast without signatures; (b) synchronous broadcast with unforgeable signatures; (c) synchronous consensus with strong validity and signatures; (d) the phase queen algorithm; (e) the version of Rabin's algorithm that needs $n \ge 8t + 1$; (f) a masking quorum system with quorums of equal size.

2. ◦ The oral messages algorithm OM(2) runs with $n = 8$ generals. How many messages are sent in each of its rounds, and how many in total?

3. ◦ A replicated service has $n = 10$ replicas and tolerates the largest $f$ with $n \ge 3f + 1$. How large is a quorum certificate, how many replicas do two certificates share at least, and how many of those are honest at least? How many matching replies does a client need?

4. ◦ Bracha's reliable broadcast runs with $n = 7$ and $t = 2$. How many ECHO messages make an honest process send READY, how many READY messages make it send READY without enough echoes, and how many READY messages make it deliver? What is the largest number of messages the honest processes send?

5. ◦ With $n = 7$ replicas and an honest leader, count the messages for one decision in PBFT, in one view of basic HotStuff, and in one round of Tendermint without gossip. Give the message delays of PBFT and Tendermint.

6. ◦ The system must tolerate $t = 3$ Byzantine faults without signatures. Give the smallest $n$, the number of rounds and the bound on messages for the phase king algorithm, and the same three numbers for the phase queen algorithm.

7. ◦ The Dolev-Strong algorithm runs with $n = 6$ processes and no faults. How many messages are sent, and how many signatures do they carry in total? How many rounds does it take when it is set up for $t = 4$?

8. ◦ A Byzantine quorum system has $n = 13$ servers with quorums of equal size and $f = 3$. Give the smallest quorum size for a dissemination system and for a masking system, and the overlap of two quorums in each. What is the largest $f$ each kind could tolerate with 13 servers?

9. ◦ A deterministic synchronous Byzantine agreement algorithm is set up for $t = 4$ with $n = 20$. How many rounds does it need in its worst run? An early-stopping algorithm runs when only one process is actually faulty; by which round can it stop?

10. • OM(1) runs with $n = 5$ generals. The commander is a traitor and sends ATTACK to lieutenants 1 and 2 and RETREAT to lieutenants 3 and 4, who are loyal. What does each lieutenant obey, and why does agreement hold? How many messages are sent?

11. • A masking quorum system has $n = 9$ servers, $f = 2$ and quorums of 7. A client reads from 7 servers and gets the pair (timestamp 5, $x$) from 4 servers, (6, $y$) from 2 servers and (4, $z$) from 1. Which value does the read return? Explain why $y$ cannot be the value of a completed write.

12. • The phase queen algorithm runs with $n = 5$, $t = 1$. Process $p_5$ is faulty, and the honest inputs are $p_1 = 0$, $p_2 = 0$, $p_3 = 1$, $p_4 = 1$. In every round $p_5$ sends 1 to $p_1$ and $p_2$ and 0 to $p_3$ and $p_4$. The queen of phase $k$ is $p_k$. Give each honest value after phase 1, the decision, and the number of messages the honest processes send.

13. • Rabin's algorithm as given in its entry runs with $n = 25$ and $t = 3$. Compute $L$, $H$ and $G$. A process counts 17 copies of 1 in a round. What does it set its value to when the coin is 0, and when the coin is 1? Does it decide?

14. • Interactive consistency is solved by running one Dolev-Strong instance per process in parallel, with $n = 7$ and $t = 2$. How many rounds does it take, and how many messages are sent when nothing fails?

15. • In the Feldman-Micali algorithm with $n = 7$ and $t = 2$, a process receives, in the second round of graded consensus, the proposal 1 from 4 processes, $\bot$ from 2 and 0 from 1. What value and grade does it get, and does it decide? If the coin is common with probability $1/4$, what bound does the entry give on the expected iteration of the last decision?

16. • A HotStuff replica has its lock on a node $b$ with a precommit certificate of view 5. In view 8 it receives three proposals, each with a parent equal to the node of the certificate it carries: (a) a node that extends $b$, with a certificate of view 6; (b) a node on a branch that conflicts with $b$, with a certificate of view 7; (c) a node that conflicts with $b$, with a certificate of view 4. For which does it vote?

17. • In PBFT with $n = 7$, the primary stops. How many messages does the view change send, counting VIEW-CHANGE and NEW-VIEW? How many VIEW-CHANGE messages make an honest replica join a view change before its own timer expires, and how many does the new primary need?

18. • Someone claims a deterministic Byzantine broadcast algorithm for $n = 100$ and $t = 40$ in which correct processes send at most 150 messages in every run. Which part of the Dolev-Reischuk bound rules it out, and what number does it give? What is the bound on messages from correct processes for Dolev-Strong with $n = 100$?

19. • Bracha's asynchronous agreement runs with $n = 7$ and $t = 2$. How many values does a process wait for in a step? How many equal bits mark a value in step 2? In step 3, what does a process do with three copies of $(d, 1)$ and two unmarked values (the symbol ?), and what does it do with two copies of $(d, 0)$ and three unmarked values?

20. • A Byzantine replicated service has $n = 7$ replicas. A client gets the reply $x$ from 2 replicas and $y$ from 3. Which reply can it accept, and why is 2 matching replies not enough?

21. • Bracha's reliable broadcast runs with $n = 6$ and $t = 2$, so $n = 3t$. The sender is honest and the two faulty processes are silent. Show that no honest process delivers.

22. ★ A variant of PBFT with $n = 4$ and $f = 1$ treats a request as prepared after the pre-prepare and $f$ matching prepares, and commits after $2f$ matching commits, so a quorum has 2 replicas. Give a run with a faulty primary in which two honest replicas commit different requests at the same sequence number.

23. ★ The Dolev-Strong algorithm with $n = 4$ and $t = 2$ is stopped after $t$ rounds instead of $t + 1$. The sender and one other process are faulty. Give a run in which the two honest processes output different values, and show that the third round prevents it.

24. ★ Show that no algorithm solves consensus with strong validity among $n = 4$ processes with $t = 2$, even with unforgeable signatures and synchronous rounds.

25. ★ The phase queen algorithm runs with $n = 8$ and $t = 2$, which is $n = 4t$, and all six honest processes start with 1. Pick the faulty processes and their messages so that the honest processes decide different values.

26. ★ In the graded consensus of the Feldman-Micali algorithm with $n = 7$ and $t = 2$, prove that if one honest process gets grade 2 for $w$, then every honest process gets grade at least 1 for $w$.
