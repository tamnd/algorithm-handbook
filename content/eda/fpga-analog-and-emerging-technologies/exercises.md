1. ◦ An [island-style FPGA](/island-style-fpga/) has an $8 \times 8$ array of logic blocks, $W = 30$ tracks per channel, wire segments of length 1, and a switch block with $F_s = 3$ at each of the $9 \times 9$ crossings of the channels. Count the wire segments and the switches of all switch blocks together. How many switches would a full crossbar have in one switch block inside the array, against the $6W$ of the usual pattern?

2. ◦ A planar [switch block](/fpga-switch-block/), in which track $i$ of a side meets only track $i$ of the other sides, has $W = 2$. Route the four nets $TR$, $RB$, $BL$ and $LT$, or show that no routing exists. Then do the same for the three nets $TL$, $LB$ and $BT$. Use the view of the planar pattern as an [edge coloring](/edge-coloring/) of the graph of the nets on the four sides.

3. ◦ For a placed netlist, every route of each of 33 nets must use a track of one of 4 channel pieces that form a cut. A binary search with a heuristic router succeeds at $W = 12$ and fails at $W = 11$. What do these facts say about the [minimum channel width](/minimum-channel-width/)? Would an exact router that fails at $W = 11$ prove that the minimum is 12?

4. ◦ [Chortle-crf](/chortle-crf/) maps a single OR gate of 10 inputs into lookup tables with $K = 4$. Give a lower bound on the number of tables from the count of their inputs, and a mapping that meets it.

5. ◦ In the [Pelgrom model](/pelgrom-mismatch-model/) with $A_{VT} = 4$ mV·µm and the distance term left out, find $\sigma(\Delta V_T)$ for a pair of transistors with $W = 2$ µm and $L = 0.5$ µm. What gate area gives $\sigma = 1$ mV? If only $W$ is doubled, what is $\sigma$?

6. ◦ Two devices A and B are each made of 3 unit cells. Show that no [common-centroid layout](/common-centroid-layout/) of them exists in a row of 6 cells, and none in an array of 2 rows and 3 columns. Why does an array of 2 rows and 4 columns with 4 cells each not run into the same obstacle?

7. ◦ On 4 lines, how many gates has the NCT library, and how many the MCT library of [reversible logic synthesis](/reversible-logic-synthesis/)? A reversible function on 4 lines has $f(0) = 15$. Give a lower bound on the number of gates of any circuit for it.

8. ◦ For [qubit mapping](/qubit-mapping/), the circuit $\mathrm{CNOT}(a, b)$, $\mathrm{CNOT}(a, c)$, $\mathrm{CNOT}(a, d)$ runs on the line $q_0 - q_1 - q_2 - q_3$. Show that every initial mapping needs a SWAP, and give a mapping and one SWAP that run the circuit.

9. ◦ Using the counts of the [determinant decision diagram](/determinant-decision-diagram/) entry for its row order, give the number of terms and of DDD vertices for a tridiagonal matrix of order 5, and for dense matrices of orders 4, 5 and 6. From which order on does the dense DDD have fewer vertices than the determinant has terms?

10. • [FPGA packing](/fpga-packing/) with $K = 2$, $N = 2$, $I = 3$, where every net that a BLE reads comes from outside the netlist. (a) The BLEs $a, b, c, d$ read $\{1, 2\}$, $\{3, 4\}$, $\{5, 6\}$ and $\{1, 2\}$. Give the bounds $\lceil n/N \rceil$ and $\lceil p/I \rceil$ and the least number of clusters. (b) The BLEs read $\{1, 2\}$, $\{2, 3\}$, $\{3, 4\}$ and $\{4, 5\}$. Draw the graph of the legal pairs, find the least number of clusters by a [maximum matching](/maximum-matching/), and show how a packer that first pairs $b$ with $c$ does worse.

11. • In [T-VPack](/t-vpack/) with $K = 4$, so $G = 5$, two BLEs can join a cluster. $b_1$ has criticality 0.9 to the cluster and shares 1 net with it; $b_2$ has criticality 0.5 and shares 4 nets. Which one has the higher attraction for $\lambda = 0.75$ and for $\lambda = 0.25$? For which $\lambda$ do they tie?

12. • A temperature of [timing-driven annealing placement](/fpga-timing-driven-annealing-placement/) ends with the acceptance rate $R_{acc} = 0.3$, the range limit $R = 10$ and $R_{max} = 10$. Give the factor $\alpha$ for the next temperature, the new $R$ and the new criticality exponent $CE$. A move with $\lambda = 0.5$ changes the timing cost by $-2$ with $T_{prev} = 10$ and the bounding box cost by $+3$ with $BB_{prev} = 100$; give $\Delta C$ and say whether it is accepted. A move with $\Delta C = 0.05$ at temperature $0.02$: with what probability is it accepted?

13. • In one dimension, a movable cell $x$ has two-pin nets to fixed pins at 0 and 6 and is on a three-pin net with fixed pins at 3 and 9. With the clique model of weight $1/(p-1)$ and the quadratic wirelength used by [HeAP](/heap-fpga-placement/), find the position of $x$. The spreading step then gives the cell an anchor at 5, with the term $\beta (x - 5)^2$ and $\beta = 2$. Where does the next solve put $x$?

14. • In [SAT-based FPGA routing](/sat-based-fpga-routing/) with the disjoint switch pattern, each net keeps one track number along its global route, and two nets conflict when their routes share a channel piece. Five nets have the conflict graph $C_5$. Find the least $W$ for which the formula is satisfiable. At $W = 2$ the solver reports UNSAT: what is proved, and what is not?

15. • A current mirror has $A_\beta = 1\%$·µm and $A_{VT} = 5$ mV·µm, the [Pelgrom](/pelgrom-mismatch-model/) terms are independent, and the current error is $\Delta I / I = \Delta\beta/\beta - 2 \Delta V_T / V_{ov}$. Find $\sigma(\Delta I/I)$ for $WL = 4$ µm² and $V_{ov} = 0.2$ V, the area that gives 1%, and the area that gives 1% at $V_{ov} = 0.4$ V. What does this say to an [analog sizing](/analog-circuit-sizing/) tool?

16. • Cells: a pair $a, a'$ of size $1 \times 1$, a self-symmetric cell $s$ of size $2 \times 1$ and a free cell $f$ of size $1 \times 1$ (width by height). Take $\Gamma^+ = (a, f, s, a')$ and $\Gamma^- = (s, a, f, a')$. Test whether the pair is a [symmetric-feasible sequence pair](/symmetric-feasible-sequence-pair/), repair $\Gamma^-$, list the relations of the repaired pair, and give the width and height of SYM-PACK. How many orders $\Gamma^-$ pass the test for this $\Gamma^+$?

17. • An [ASF-B*-tree](/asf-b-star-tree/) holds a pair $a$ of $1 \times 1$ cells, a self-symmetric cell $s$ of size $2 \times 1$ and a pair $b$ of $1 \times 2$ cells. The root is $s$, $a$ is the right child of $s$, and $b$ is the left child of $a$. Pack the tree and give the area. Then count the ASF-B*-trees for a group of one pair and two self-symmetric cells, out of the 30 labeled binary trees on 3 nodes.

18. • On 2 lines $a$ (bit 0) and $b$ (bit 1), $f = [3, 1, 2, 0]$ swaps 00 and 11. Run the basic form of [transformation-based synthesis](/transformation-based-reversible-synthesis/) and count its gates against the bound $(n - 1)2^n + 1$. Check that $\mathrm{CNOT}(a \to b)$, $\mathrm{NOT}(a)$, $\mathrm{CNOT}(b \to a)$, $\mathrm{CNOT}(a \to b)$, applied in this order, also computes $f$.

19. • Prove that $f(x) = x - 1 \bmod 2^n$ needs exactly $n$ multiple-control Toffoli gates: show the lower bound, and show that $\mathrm{NOT}(0)$, $T(\{0\}; 1)$, $T(\{0, 1\}; 2)$, …, $T(\{0, \ldots, n-2\}; n-1)$, applied in this order, computes $f$.

20. • A copper [through-silicon via](/through-silicon-via/) has $R = 2$ µm, $L = 40$ µm and $t_{ox} = 0.2$ µm. Find its resistance and its liner capacitance, and the number of 1 fF gate inputs that the capacitance equals. For a TSV of radius 1.5 µm, by what factor is the radial stress at 4.5 µm from the center smaller than at the wall? By what factor does an ideal stack of 4 tiers shrink the planar distances of a [3D IC](/three-dimensional-integrated-circuit/)?

21. • Six cells $a, \ldots, f$ of unit area go on $L = 3$ tiers with $\varepsilon = 0$, two per tier. The nets are $ab$, $bc$, $cd$, $de$ and $ef$. Find the least span cost of [tier partitioning](/tier-partitioning/). Add the net $fa$ and find it again; how many nets does your assignment cut?

22. • On the line $q_0 - q_1 - q_2 - q_3$, the logical qubits $a, b, c, d$ start on $q_0, \ldots, q_3$, and the circuit is $\mathrm{CNOT}(a, d)$ then $\mathrm{CNOT}(b, d)$. Run one forward pass of [SABRE](/sabre-qubit-mapping/) with $W = 0.5$, $\delta = 0.001$ and an extended set of one gate: score the candidate SWAPs at each step and give the SWAPs it inserts. Is the count optimal from this start, and for a free start?

23. ★ For a [universal switch block](/universal-switch-block/) with $W = 3$: (a) show that the four nets $RB$, $RL$, $BL$, $BL$ meet the density condition, and that the planar pattern cannot route them; (b) show that no requirement with fewer nets is a failure of the planar pattern at $W = 3$; (c) show that in a universal block with exactly $6W$ switches every terminal has exactly one switch to each other side, so the switches between any two sides form a perfect matching of their terminals.

24. ★ On the line $q_0 - q_1 - q_2 - q_3$, a circuit applies one CNOT to each of the six pairs of $a, b, c, d$, in the order $ab$, $ac$, $ad$, $bc$, $bd$, $cd$. Find the least number of SWAPs over all initial mappings, with a proof of the lower bound and a schedule that meets it.

25. ★ In the chain model of [thermal-driven 3D floorplanning](/thermal-driven-3d-floorplanning/), one stack of unit area has $L$ layers, layer 1 next to the sink, with powers $p_1, \ldots, p_L$, a base resistance $R_b$ and a resistance $R_k \ge 0$ below layer $k$. The rise of layer $k$ is $R_b P + \sum_{i \le k} R_i S_i$, with $P$ the total power and $S_i = \sum_{j \ge i} p_j$. Show that the top layer is the hottest, and that placing the powers in decreasing order from the sink minimizes it. Evaluate the best and worst order for the powers 1, 3 and 5 with $R_b = 1/2$ and $R_k = 1$.

26. ★ Show that [tier partitioning](/tier-partitioning/) with the span cost stays NP-hard for $L = 3$, unit areas and $\varepsilon = 0$, by a reduction from minimum bisection. You may use several copies of one net.

27. ★ In an [ASF-B*-tree](/asf-b-star-tree/) with one self-symmetric cell and $n - 1$ pairs, show that exactly $3/(n + 2)$ of the $n! \, C_n$ labeled binary trees on $n$ nodes are ASF-B*-trees, where $C_n$ is the Catalan number. Check the value 18 of 30 for $n = 3$.
