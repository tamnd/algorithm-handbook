1. [Flooding](/flooding/) sends $2m - n + 1 = 18 - 7 + 1 = 12$ messages. The last ones go between nodes 5 and 6 in round 5, which is $e + 1$ for the eccentricity $e = 4$ of node 0. Forwarding on all edges sends $2m = 18$, and so does the [echo algorithm](/echo-algorithm/).

4. The leaves send in round 1: node 2 sends $(2, 0)$, node 3 sends $(7, 1)$ and node 5 sends $(8, 1)$. Node 4 sends $(8, 1)$ in round 2, and node 1 sends $(9, 3)$ in round 3. The root has $(9, 3)$ after round 3, the height of the tree, with $n - 1 = 5$ messages.

6. In [Cole-Vishkin](/cole-vishkin/), for $N = 100$ the bounds are $100, 14, 8, 6$, so $T = 3$ and 6 rounds. For $N = 1000$ they are $1000, 20, 10, 8, 6$, and for $N = 2^{32}$ they are $2^{32}, 64, 12, 8, 6$; both give $T = 4$ and 7 rounds.

9. In [CONGEST](/congest-model/), each cut edge has $2^{B+1} = 2^{20}$ possible contents per round, so after $t$ rounds the right side can be in at most $2^{20 \cdot 3 \cdot t}$ states. It needs $2^{1200}$ different states, so $t \ge 20$.

11. The bound goes $64, 12, 8, 6$, so there are three steps. The colours are $1, 2, 0, 2, 1, 0$, then $1, 3, 2, 0, 1, 0$, then $2, 1, 3, 0, 1, 0$. The classes 5 and 4 are empty, and in the round of class 3 node $v_2$ takes the free colour 2, which gives $2, 1, 2, 0, 1, 0$ after 6 rounds. Class 0 puts $v_3$ and $v_5$ into the [MIS](/distributed-mis/), class 1 adds $v_1$, and class 2 adds nothing: $\{v_1, v_3, v_5\}$.

12. In [Linial's algorithm](/linial-algorithm/), $38 = 3 + 2 \cdot 5 + 1 \cdot 25$, so $p(a) = 3 + 2a + a^2$, with the values $3, 1, 1, 3, 2$ at $a = 0, \dots, 4$. The constant polynomial 1 blocks $a = 1$ and $a = 2$, and the constant 3 blocks $a = 0$ and $a = 3$. The least free point is $(4, 2)$, so the new colour is $5 \cdot 4 + 2 = 22$.

13. From $m = 10^9$ the least prime is $q = 17$ (with $d = 7$), which leaves 289 colours. Then $q = 7$ with $d = 2$ leaves 49, and $q = 5$ with $d = 2$ leaves 25. No prime below 5 works, so the loop stops after three rounds. Removing the colours 24 down to 3 takes 22 rounds, 25 in total.

14. In the [LOCAL model](/local-model/), $B_3(v_0)$ has all seven nodes and the six edges other than $v_3 v_4$, which joins two nodes at distance 3. Put a new node between $v_3$ and $v_4$ to get an 8-cycle in which $v_0$ has the same ball, so 3 rounds are not enough. $B_4(v_0)$ contains $v_3 v_4$, so 4 rounds, which is $D + 1$, suffice.

15. Under [synchronizer](/synchronizer/) α the run sends $8$ algorithm messages, $8$ ACKs and $2m P = 16 \cdot 8 = 128$ SAFE messages, 144 in all, in time at most $3P = 24$. Under β it sends $8 + 8 + 2(n - 1)P = 144$ messages for either root, in time at most $P(2h + 2)$: 80 with $h = 4$ and 144 with $h = 8$. On a tree $2m = 2(n - 1)$, so here β saves nothing and α is faster.

16. In [Dijkstra-Scholten](/dijkstra-scholten/), nodes 1 and 2 are engaged with parent 0. Node 3 is engaged with parent 2, and the later message from 1 gets an immediate signal. The signals are $3 \to 1$, $1 \to 0$, $1 \to 3$ (node 1 was engaged again, with parent 3), $3 \to 2$ and $2 \to 0$, and then node 0 announces termination. There are 5 basic messages and 5 signals.

18. In [Bellman-Ford](/distributed-bellman-ford/), the estimates of nodes 0 to 5 are $0, 7, 1, \infty, \infty, \infty$ after round 1, then $0, 7, 1, 2, 8, 10$, then $0, 3, 1, 2, 7, 10$, then $0, 3, 1, 2, 4, 9$, and $0, 3, 1, 2, 4, 6$ after round 5, the last change. The full version sends $2m(n - 1) = 2 \cdot 8 \cdot 5 = 80$ messages.

23. In [GHS](/gallager-humblet-spira/), follow the minimum outgoing edges: two fragments of the same level merge when they share one, and a fragment of a lower level is absorbed. With the weights 1, 5, 2, 7, 3, 6, 4, the level-1 fragments are $v_0 v_1$, $v_2 v_3$, $v_4 v_5$ and $v_6 v_7$; then the edges of weight 5 and 6 make two level-2 fragments, and the edge of weight 7 makes one of level 3 with that edge as its core. With increasing weights only $v_0$ and $v_1$ share a minimum edge, every other node points left and is absorbed, and the final level is 1. A fragment of level $L$ has at least $2^L$ nodes, so no run on 8 nodes passes level 3.

24. The map is onto, keeps degrees, and sends the edge from port 1 of $v_i$ to port 2 of $v_{i+1}$ to the same kind of edge in $C_3$. By the [covering lemma](/port-numbering/) $v_i$ in $C_6$ and $v_{i \bmod 3}$ in $C_3$ are in the same state after every round, so they give the same output, although one cycle is even and the other odd. In $C_6$ only $v_3$ is at distance 3 from $v_0$, so every edge has an end within distance 2 and $r = 3$.

25. A [maximal matching](/distributed-maximal-matching/) of a cycle is an MIS of its line graph, which is again a cycle; an MIS of a cycle leaves gaps of one or two nodes and gives a 3-colouring in $O(1)$ more rounds. So (a) and (c), which is exactly an MIS, are $\Theta(\log^* n)$. (b) is $O(1)$: everyone outputs 0. (d) forces the whole cycle to point one way, a global choice, so it is $\Theta(n)$ like 2-colouring. (e) is $\Theta(\log^* n)$ like every fixed number of colours from 3 up.

26. Simulate the network: the two sides exchange what crosses the cut, so $2ktB \ge K$ and $t \ge K/(2kB) = (n^2/16)/(nB) = n/(16B)$. With $B = \lceil \log_2 n \rceil$ this is $\Omega(n/\log n)$, the form of the [diameter lower bound](/diameter-lower-bound-distributed/).

27. In the [ruling-set](/ruling-set/) construction, a node is far from the set only if its representative leaves at several levels in a row, each time moving one step further. The identifiers $0, 1, 2, 4, 3, 5, 6, 7$ do it: the set is $\{v_0, v_2, v_3, v_4, v_5, v_6\}$ after level 1, $\{v_0, v_2, v_3, v_4, v_5\}$ after level 2 and $\{v_0, v_2, v_4\}$ after level 3, and $v_7$ is at distance 3 from $v_4$.
