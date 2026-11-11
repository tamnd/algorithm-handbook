1. (a) 3, since $n > 3t$. (b) 9, any $t < n$. (c) 4, since $n > 2t$. (d) 2, since $n > 4t$. (e) 1, since $8t + 1 \le 10$. (f) 2, since $n \ge 4f + 1$.

2. The rounds carry $7$, $7 \cdot 6 = 42$ and $7 \cdot 6 \cdot 5 = 210$ messages, so 259 in total.

5. PBFT sends $2n(n-1) = 84$ messages in 3 delays. A basic HotStuff view sends $8(n-1) = 48$. Tendermint sends $2n(n-1) + (n-1) = 90$ in 3 delays.

8. Dissemination: quorums of 9, overlap at least 5. Masking: quorums of 10, overlap at least 7. With 13 servers, dissemination tolerates up to $f = 4$ and masking up to $f = 3$.

10. Each loyal lieutenant ends with ATTACK, ATTACK, RETREAT, RETREAT: its own value from the commander and three relayed ones. No value has a strict majority, so the majority function gives the default RETREAT to all four. The commander sends 4 messages and the lieutenants 12, so 16.

12. In phase 1 every honest count is 3, below the test $mult > 3.5$, so all take the majority of the queen $p_1$, which sees three 1s and sends 1. In phase 2 every honest process counts at least four 1s and keeps 1, so all decide 1. Each phase costs 20 values and 5 queen messages, 50 in all.

13. $L = 12 + 3 + 1 = 16$, $H = 19$, $G = 22$. With coin 0 the threshold is 16 and the process keeps 1; with coin 1 it is 19 and the process sets 0. It does not decide, since $17 < 22$.

16. The rule is to vote if the node extends the locked node or the certificate's view is above the lock's view. It votes for (a), which extends $b$, and for (b), since $7 > 5$ shows that a quorum has moved past the lock. It refuses (c).

21. A READY from echoes needs more than $(6 + 2)/2 = 4$ ECHO messages, so 5, but only the 4 honest processes echo. The other way to send READY needs $t + 1 = 3$ READY messages, and none is ever sent.

22. The faulty primary $p_0$ gives request $m$ to $p_1$ and $m'$ to $p_2$ and $p_3$, all at sequence number 1. It supplies the one extra prepare and commit that $p_1$ needs for $m$, while $p_2$ and $p_3$ supply them to each other for $m'$. Two quorums of 2 among 4 replicas need not share an honest replica, while two quorums of 3 share two replicas, so at least one honest replica.

23. In round 1 the sender signs 1 and gives it only to the faulty $p_2$, which adds its signature and sends the chain only to the honest $p_3$ in round 2. After two rounds $p_3$ outputs 1 and $p_4$, which received nothing, outputs $\bot$. With a third round $p_3$ relays the chain with three distinct signatures, and $p_4$ accepts it; a value that first appears in round 3 needs three signers, so one honest signer, which relayed it in time to everyone.

24. Split the processes into $A = \{p_1, p_2\}$ and $B = \{p_3, p_4\}$. If $B$ is faulty but runs the correct code with input 1, strong validity forces $A$ with inputs 0 to decide 0; symmetrically $B$ decides 1 when $A$ is faulty and runs the code with input 0. In the run with no faults, $A$ inputs 0 and $B$ inputs 1, each half sees exactly what it saw before, and the two halves disagree. Signatures do not help, because the faulty processes only sign their own messages.

25. Make $p_2$ and $p_3$ faulty, the queens of phases 2 and 3. While the honest processes agree, the faulty ones send the other bit in round 1, so every honest count is $6 = n/2 + t$, which fails the strict test and makes everyone follow the queen. The queen $p_2$ sends 0 to all in phase 2, and in phase 3 the queen $p_3$ sends 0 to $p_4, p_5, p_6$ and 1 to $p_1, p_7, p_8$.

26. Grade 2 means at least $n - t = 5$ proposals of $w$, so at least 3 from honest processes, which send the same proposal to all; every honest process therefore counts at least $3 = t + 1$ proposals of $w$. An honest process proposes a value only after 5 copies of it in round 1, and two sets of 5 senders share an honest one, so no honest process proposes a value other than $w$. Any other value has at most 2 proposals, so $w$ is the most frequent and gets grade at least 1.
