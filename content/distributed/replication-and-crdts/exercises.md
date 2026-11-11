1. ◦ A store runs between two data centres with message delay $d = 80$ ms. By the bound $|W| + |R| \ge d$ of [PACELC](/pacelc/), if reads take $|R| = 1$ ms, how long must a write take for the store to be sequentially consistent? For a linearizable register with at least two readers and two writers and delay uncertainty $u = 20$ ms, what are the lower bounds on $|R|$ and $|W|$?

2. ◦ Three commands act on an integer that starts at $2$: $a$ adds 3, $b$ doubles, and $c$ subtracts 1. Three replicas of a [state machine](/state-machine-replication/) receive the commands in different orders. Compute the final value for all six orders. How many different final values are there, and which pair of commands commutes?

3. ◦ A service has $n = 5$ servers. Count the messages and message delays of one update under [chain replication](/chain-replication/), counting the client's request and reply, and do the same for [primary-backup replication](/primary-backup-replication/). For which $n$ do the two take the same number of delays?

4. ◦ A [leaderless](/leaderless-replication/) store has $N = 5$ replicas. For each pair $(R, W)$ in $(1, 5)$, $(2, 3)$, $(3, 3)$, $(2, 4)$ and $(3, 2)$, say whether every read meets the last write, whether every two writes meet, the least overlap of a read and a write quorum, and how many crashed replicas reads and writes each survive.

5. ◦ Which of these are joins of a [join-semilattice](/join-semilattice/) on their set: (a) the maximum on the integers; (b) addition on the natural numbers; (c) bitwise OR on 4-bit strings; (d) the mean rounded up, $\lceil (x + y)/2 \rceil$, on the integers? For (c), name the order and compute $0101 \sqcup 0011$. For (d), find three numbers that break associativity.

6. ◦ A [g-counter](/g-counter/) on three replicas holds $(3,0,1)$ at $A$, $(1,2,0)$ at $B$ and $(0,2,4)$ at $C$. What is the merged state and its value? What would a reader get who added up the three local values instead?

7. ◦ A [PN-counter](/pn-counter/) on replicas $A$, $B$, $C$ has these states, written as $P$ then $N$: $A$ holds $P = (2,0,0)$, $N = (0,0,1)$; $B$ holds $P = (1,3,0)$, $N = (0,1,0)$; $C$ holds $P = (0,0,2)$, $N = (0,0,1)$. Give the value at each replica, the state and value after $A$ merges $B$, and the value after all three have merged.

8. ◦ Four replicas write a [LWW-register](/lww-register/) at the same time. Stamps are pairs (clock, replica id), compared by clock, then by id. The writes are red at $(3, B)$, blue at $(3, A)$, green at $(2, C)$ and black at $(1, D)$. Which value survives anti-entropy, and how many writes are lost?

9. ◦ [Logoot](/logoot/) positions, with base 100, are $c = \langle(5,1,1)\rangle$, $r = \langle(5,1,1),(4,2,9)\rangle$, $d = \langle(5,1,1),(4,3,7)\rangle$, $t = \langle(5,2,3)\rangle$ and $s = \langle(6,2,1)\rangle$. Sort them and read the word. Give a position of length 2 that lies between $d$ and $t$.

10. • Three processes run on a register store. Process 1 does $w(x)1$ then $w(x)2$. Process 2 does $r(x)2$ then $w(y)1$. Process 3 does $r(y)1$ then $r(x)1$. Is the history PRAM? Is it [causally consistent](/causal-consistency/)? If process 3's second read returns 2 instead, is the history sequentially consistent?

11. • In [session guarantees](/session-guarantees/), a client has write vector $(2,1,0)$ and read vector $(1,1,1)$ over servers $A$, $B$, $C$. Three servers have version vectors $S_1 = (2,1,1)$, $S_2 = (2,0,3)$ and $S_3 = (1,1,1)$. Which servers may serve a read under [read your writes](/read-your-writes/), which under [monotonic reads](/monotonic-reads/), and what is the read vector after a read at $S_1$?

12. • Sixteen servers form a $4 \times 4$ grid, and a quorum is one full row plus one full column. Give the size $c$ of a quorum, the least overlap of two quorums, and the load. Compare the load with that of majorities on 16 servers, with the bound $\max(1/c, c/n)$ of Naor and Wool, and with $1/\sqrt{n}$, all from [quorum intersection](/quorum-intersection/).

13. • Five servers hold 3, 2, 2, 1 and 1 votes, $V = 9$ in all. In weighted [quorum replication](/quorum-replication/), list every pair $(r, w)$ with $r + w = V + 1$ and $2w > V$. For $r = 4$ and $w = 6$, give the fewest servers in a read quorum and in a write quorum. If the 3-vote server and one 2-vote server crash, can the store still read, and can it write?

14. • Each of five replicas is down with probability $0.1$, independently. Find the probability that the store cannot answer when it needs (a) a majority, (b) all five replicas for a write, and (c) one replica for a read.

15. • Two replicas compare a Merkle tree over 16 buckets numbered 0 to 15, binary with depth 4. Buckets 2, 3 and 13 differ. During [anti-entropy](/anti-entropy/), how many tree nodes does the comparison visit, counting each node of both trees once? Compare with the bound $1 + 2d\log_2 B$.

16. • A fraction $p = 0.2$ of $n = 4000$ replicas lacks an update. Using the recurrences of anti-entropy, find the fraction that lacks it after one round of pull, push and push-pull. How many rounds of pull bring the fraction below $10^{-6}$?

17. • In [set reconciliation](/set-reconciliation/) with an invertible Bloom lookup table, Alice holds 5 and Bob holds 9 and 12 that the other lacks, and all shared elements cancel. The hashes give $5 \mapsto \{0,1,2\}$, $9 \mapsto \{1,3,4\}$ and $12 \mapsto \{2,4,5\}$ in a table of six cells. Write the (count, keySum) of each cell after Bob subtracts his table, with keySums XORed. Peel the table. Which cells look pure from their keySum but are not?

18. • By the [CALM theorem](/calm-theorem/), which of these queries can run without coordination: (a) is there a path from $s$ to $t$; (b) is vertex $v$ unreachable from $s$; (c) does the input hold at least 10 facts; (d) does it hold exactly 10; (e) the join of two relations; (f) the set difference of two relations?

19. • An [MV-register](/mv-register/) on replicas $A$, $B$, $C$ holds $\{x(1,0,0)\}$. $B$ merges it and writes $y$, while $C$, which has not seen $x$, writes $z$. A replica then merges all three states. Which pairs remain? If $A$ next writes after that merge, what is the version vector of its write?

20. • A set starts empty. Replica $a$ adds $x$ at stamp 1. Replica $b$ sees the add and removes $x$ at stamp 5. At the same time, replica $c$ sees the add and adds $x$ again at stamp 3. After all have merged, is $x$ in the [OR-Set](/or-set/), the [2P-Set](/two-phase-set/), and the [LWW-Element-Set](/lww-element-set/) with add bias? What changes if $c$'s add carries stamp 7?

21. • In the optimized OR-Set with dots and version vectors over replicas $a$ and $b$, replica $a$ holds $E = \{(x,2,a)\}$ with $V = (2,1)$, and replica $b$ holds $E = \{(x,1,a), (y,1,b), (z,2,b)\}$ with $V = (1,2)$. Merge them. Which elements remain, and what is $V$? Check that the merge in the other direction gives the same.

22. ★ A store must tolerate $f = 2$ Byzantine servers with threshold quorums. For dissemination quorums, whose overlaps must hold $f + 1$ servers, and masking quorums, whose overlaps must hold $2f + 1$, find the least $n$, the quorum size $q$ at that $n$, and the overlap $2q - n$.

23. ★ A Merkle comparison over $B = 16$ buckets in a binary tree finds $d = 4$ differing buckets. Which placements of the four buckets give the fewest and the most visited nodes, and what are the two counts? How far is the maximum from the bound $1 + 2d\log_2 B$?

24. ★ A sender in a [delta-state CRDT](/delta-state-crdt/) ships only its newest delta and ignores acknowledgements. In a g-counter, replica $A$ makes deltas $\{A \mapsto 5\}$ and then $\{A \mapsto 6\}$, and the first is lost on the way to $B = (2,3,0)$. In a [g-set](/g-set/), $A$ adds $e$ and then $f$, and the delta $\{e\}$ is lost. Give $B$'s state after each, and say which run breaks the causal delta-merging condition and what $A$ should have sent.

25. ★ In a [causal tree](/causal-tree/), atoms are $H(1,0)$ under the root, $i(2,0)$ under $H$, $e(3,0)$ under $H$, $o(3,1)$ under $H$, $y(4,0)$ under $e$ and $!(4,1)$ under $i$, with ids (clock, site) and larger ids first among siblings. Write the weave. Show that [RGA](/rga/) gives the same text, and give the text after $o$ is deleted.

26. ★ [Operational transformation](/operational-transformation/) uses the classical rules on positions with insert ties broken by site id. On the text "abc", let $a = \mathrm{ins}(2, x, 1)$ and $b = \mathrm{del}(1)$. Check [TP1](/tp1-tp2-conditions/) for $a$ and $b$. Then take $c = \mathrm{ins}(1, z, 3)$ and transform $c$ along both paths. Does TP2 hold? Check TP2 again on "ab" with $a = \mathrm{ins}(1, x, 1)$, $b = \mathrm{ins}(1, y, 2)$ and $c = \mathrm{del}(0)$.
