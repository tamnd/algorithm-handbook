1. ◦ The graph $G_1$ has the nodes $0, \dots, 6$ and the nine edges $01, 02, 12, 13, 23, 34, 45, 46, 56$, and node 0 is the source. In [flooding](/flooding/) the source sends in round 1, and a node that first hears the message in round $r$ forwards it in round $r + 1$ on every edge except the one from its parent; if copies arrive in the same round, the smaller sender becomes the parent. How many messages does flooding send on $G_1$, and in which round is the last one sent? How many does the variant send in which every node forwards on all its edges, and how many does the [echo algorithm](/echo-algorithm/) send?

2. ◦ Give the parent and the distance from 0 of every node in the tree that flooding builds on the graph $G_1$ of Exercise 1. Which edges are not in the tree, and how many copies does each of them carry?

3. ◦ On the complete graph $K_{10}$, compare plain flooding with a depth-first token in the KT1 model, where each node knows its neighbours' identifiers from the start. Count the messages of both, and give the time of the token.

4. ◦ A rooted tree has root 0, the children 1 and 2 of node 0, the children 3 and 4 of node 1, and the child 5 of node 4. The values are 4, 9, 2, 7, 1 and 8 at the nodes 0 to 5. A [convergecast](/convergecast/) computes the maximum and the number of values above 5. Give the pair that each non-root node sends, the round in which it sends it, the round in which the root has the answer, and the number of messages.

5. ◦ In the [port-numbering model](/port-numbering/) the 4-cycle $v_0 v_1 v_2 v_3$ has port 1 at $v_0$ and at $v_1$ for the edge $v_0 v_1$, port 1 at $v_2$ and at $v_3$ for the edge $v_2 v_3$, and port 2 on the other two edges. Give a PN algorithm that finds a [maximal matching](/distributed-maximal-matching/) here, its output and its number of rounds.

6. ◦ In [Cole-Vishkin](/cole-vishkin/) a colour bound $b$ becomes $2 \lceil \lg b \rceil$ in each step while $b > 6$, and $T(N)$ is the number of steps from $b = N$. Then three rounds remove the colours 5, 4 and 3. Compute $T(N)$ and the total number of rounds for $N = 100$, $N = 1000$ and $N = 2^{32}$.

7. ◦ On the path $a, b, c, d, e, f, g$, give the best $(\alpha, \beta)$ for which each of the sets $\{a, d, g\}$, $\{b, f\}$ and $\{a, g\}$ is an $(\alpha, \beta)$-[ruling set](/ruling-set/): any two members are at distance at least $\alpha$, and every node is within distance $\beta$ of a member.

8. ◦ On the path $a, b, c, d, e, f$, a distributed algorithm finds the maximal matching $\{bc, de\}$ and outputs all matched nodes as a [vertex cover](/distributed-minimum-vertex-cover/). Check that the matching is maximal, give the size of the cover and of a minimum cover, and compare the ratio with the guarantee.

9. ◦ In the [CONGEST model](/congest-model/) with $B = 19$, a network has a cut of $k = 3$ edges. The nodes on the right must output a 1200-bit string that only the left side holds at the start. In each round each cut edge carries, towards the right, no message or a message of at most $B$ bits. How many rounds are needed?

10. ◦ The [distributed PageRank](/distributed-pagerank/) algorithm runs for $R = \lceil \ln(n^2 K)/\epsilon \rceil$ rounds with at most $mR$ messages. Compute $R$ and the message bound for $n = 100$, $m = 300$, $K = 10$ and $\epsilon = 0.15$.

11. • Run Cole-Vishkin on the oriented 6-ring $v_0, \dots, v_5$ with the identifiers 45, 12, 58, 33, 7 and 20, where $v_i$ compares itself with its successor $v_{i+1}$ and takes $2j + x_j$ for the lowest bit $j$ in which they differ, with $N = 64$. Give the colours after each step and each clean-up round. Then turn the 3-colouring into an [MIS](/distributed-mis/) by letting the classes 0, 1 and 2 join in turn.

12. • In one round of [Linial's algorithm](/linial-algorithm/) with $q = 5$, $d = 2$ and $\Delta = 2$, a node of colour 38 has neighbours of colours 1 and 3. Colour $x$ names the polynomial whose coefficients are the base-5 digits of $x$, and a point $(a, y)$ is the colour $5a + y$. Find the node's polynomial and its values, the points that the neighbours block, and the new colour.

13. • Linial's algorithm repeats its step as long as this lowers the number of colours $m$. Each step uses the least prime $q$ for which some $d$ has $q > \Delta d$ and $q^{d+1} \ge m$, and leaves $q^2$ colours. Then it removes the colours above $\Delta$ one class per round. For $\Delta = 2$ and $N = 10^9$, give the primes $q$, the colour counts, the number of clean-up rounds and the total.

14. • In the [LOCAL model](/local-model/), every node of the cycle $C_7 = v_0 \dots v_6$ must output the number of nodes, which it does not know. List the nodes and the edges of the ball $B_3(v_0)$. Find a graph on 8 nodes in which $v_0$ has the same ball of radius 3, and conclude how many rounds the task needs on $C_7$.

15. • A synchronous BFS from one end of the path $P_9$ runs for 8 pulses and sends 8 messages. Run it on an asynchronous network under [synchronizer](/synchronizer/) α, and under β with the tree rooted at the middle node and at an end. For each, count all messages, the algorithm's own included, and give the bound on the time.

16. • In [Dijkstra-Scholten](/dijkstra-scholten/) with root 0 and the nodes 1, 2 and 3, the following happens, and every message arrives before the next event. Node 0 sends to 1 and to 2 and becomes passive. Node 2 sends to 3, then node 1 sends to 3. Node 1 becomes passive. Node 3 sends to 1. Node 1 becomes passive. Node 2 becomes passive. Node 3 becomes passive. Give the parent of each node each time it is engaged, every signal in order, and the number of basic messages and signals.

17. • Run the echo algorithm on the graph $G_1$ of Exercise 1 from node 0. Give the tree, the number of messages, and the round in which node 0 decides, and compare it with the range $2e$ to $2e + 1$.

18. • Run synchronous [distributed Bellman-Ford](/distributed-bellman-ford/) from node 0 on the weighted edges $01{:}7$, $02{:}1$, $23{:}1$, $31{:}1$, $14{:}1$, $34{:}5$, $45{:}2$ and $25{:}9$. Give the estimates after each round, the last round in which an estimate changes, and the number of messages of the version that sends on every edge for $n - 1$ rounds.

19. • In the [congested clique](/congested-clique-model/) [MST](/distributed-mst/) algorithm of Lotker et al., suppose that every fragment has at least 2 nodes after the first phase and that the least fragment size squares in each phase. Once every fragment has more than $n/2$ nodes only one is left. How many phases does this give for $n = 10^5$ and for $n = 10^9$?

20. • Run the AGLP ruling-set construction with $\alpha = 2$ and $B = 3$ on the 8-cycle $v_0 \dots v_7$ with the identifiers 0, 1, 2, 3, 4, 6, 7, 5. At level $j$, a node still in the set whose bit $j - 1$ is 1 leaves if a neighbour still in the set has bit $j - 1$ equal to 0 and agrees with it on all bits from $j$ up. Give the set after each level and the largest distance from a node to the set.

21. • A graph has the nodes $0, \dots, 7$. Nodes $0, 1, 2, 3$ form a $K_4$ without the edge $23$, nodes $4, 5, 6, 7$ form a $K_4$ without the edge $45$, and the edges $34$ and $25$ join them. A spanning tree rooted at 0 has the edges $01, 02, 03, 34, 46, 47, 65$. Compute every one-respecting cut $w(\delta(v^\downarrow)) = \sum_{u \in v^\downarrow} \deg u - 2|E(v^\downarrow)|$ and say whether the smallest is the [minimum cut](/distributed-min-cut/).

22. • For $n = N = 10^6$, compare [Linial's lower bound](/linial-coloring-lower-bound/) $\frac12 \log^* n - 1$ for 3-colouring a ring with Cole-Vishkin in its plain form and in the form that takes two steps per round, $\lceil T(N)/2 \rceil + 3$ rounds.

23. ★ Run [GHS](/gallager-humblet-spira/) on the path $v_0 \dots v_7$ with edge weights 1, 5, 2, 7, 3, 6, 4 from left to right. Give the fragments, their levels and their cores after each merge, and the final level. Do the same with the weights 1 to 7 in increasing order. What is the largest level that any run on 8 nodes can reach, and why?

24. ★ In the port-numbering model, let $C_6$ and $C_3$ have ports in which every node uses port 1 for the edge to $v_{i+1}$ and port 2 for the edge to $v_{i-1}$. Show that $v_i \mapsto v_{i \bmod 3}$ is a covering map from $C_6$ to $C_3$. Conclude that no PN algorithm can tell every node whether $n$ is even. With identifiers in LOCAL, find the least $r$ for which the ball $B_r(v_0)$ of $C_6$ contains every edge.

25. ★ Place each of these [locally checkable](/locally-checkable-labeling/) problems on cycles with identifiers in the class $O(1)$, $\Theta(\log^* n)$ or $\Theta(n)$, with a reason: (a) maximal matching; (b) labels in $\{0, 1\}$ with no two adjacent 1s; (c) labels in $\{0, 1\}$ with no two adjacent 1s and no three consecutive 0s; (d) an orientation of the edges in which every node has out-degree exactly 1; (e) a proper 4-colouring.

26. ★ Assume that two parties need at least $K$ bits of communication to decide whether two $K$-bit sets are disjoint. A family of CONGEST networks has $n$ nodes, a cut of $k = n/2$ edges, and inputs of $K = n^2/16$ bits on each side that decide the answer. Using the fact that $t$ rounds send at most $2ktB$ bits across a cut, give the lower bound on $t$. What is it for $B = \lceil \log_2 n \rceil$, and which entry has a bound of this form?

27. ★ On the path $v_0 \dots v_7$ with $\alpha = 2$ and $B = 3$, the AGLP construction guarantees that every node is within distance $(\alpha - 1) B = 3$ of the ruling set. Find identifiers, a permutation of $0, \dots, 7$, for which a node really is at distance 3, and give the set after each level.
