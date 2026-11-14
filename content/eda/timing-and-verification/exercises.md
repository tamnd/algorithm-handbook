1. ◦ An [RC tree](/rc-tree/) is a ladder of four sections driven at its root: resistor $R_1$ from the root to node 1, then $R_2$ to node 2, $R_3$ to node 3 and $R_4$ to node 4, with a capacitor $C_i$ to ground at node $i$. Take every $R_i = 1$ and every $C_i = 1$. Give the [Elmore delay](/elmore-delay/) at each of the four nodes.

2. ◦ In an RC tree, node 1 hangs from the root through $R_1 = 1$ and has $C_1 = 1$. Two children hang from node 1: node 2 through $R_2 = 2$ with $C_2 = 1$, and node 3 through $R_3 = 1$ with $C_3 = 3$. Give the Elmore delays at nodes 1, 2 and 3. Then add a capacitance of 2 at node 2 and give the new Elmore delay at node 3, which is not on the path to node 2.

3. ◦ A [timing graph](/timing-graph/) has inputs $a$, $b$, $c$ with arrival times 0, 1 and 0, a gate output $G_1$ and an output $y$. The edges and delays are $a \to G_1$: 2, $b \to G_1$: 3, $G_1 \to y$: 4 and $c \to y$: 1, and the required time at $y$ is 8. Give the [arrival times, required times](/arrival-and-required-time/) and slacks at all five vertices, and the critical path.

4. ◦ A path launches at a register clocked at time 0 and is captured at a register whose clock arrives at 1.5. The period is $T = 8$, the longest path delay 8.6, the shortest 0.4, the setup time 0.3 and the hold time 0.2. Give the [setup and hold](/setup-and-hold-constraints/) slacks and the least period that meets setup. Can a slower clock fix the hold check?

5. ◦ An [H-tree](/h-tree-clock/) of order 3 fills a square of side $D = 16$. How many ends does it have, what is its total wire length, and what is the path length from the centre to each end?

6. ◦ A multiplexer computes $z = ab + \bar a c$ with the gates $p = \mathrm{AND}(a_1, b)$, $\bar a = \mathrm{NOT}(a_2)$, $q = \mathrm{AND}(\bar a, c)$ and $z = \mathrm{OR}(p, q)$, where $a_1$ and $a_2$ are the two branches of the stem $a$. List the input vectors $abc$ that detect the [stuck-at faults](/stuck-at-fault-model/) $a$/0 and $a$/1 on the stem.

7. ◦ Three rectangles lie on one layer: $R_1 = [0, 4] \times [0, 2]$, $R_2 = [7, 9] \times [0, 2]$ and $R_3 = [6, 8] \times [4, 6]$. The spacing rule is "distance at least 3". Give the Euclidean distance of each pair. Which pairs violate the rule? Which does a [design rule checker](/design-rule-checking/) report if it measures only between edges whose projections overlap?

8. ◦ In a [corner-stitched](/corner-stitching/) plane, space is cut into maximal horizontal strips. How many space tiles are there for one solid square $[3, 5) \times [2, 4)$ in the world $[0, 8) \times [0, 6)$? For two solid squares $[1, 2) \times [1, 2)$ and $[3, 4) \times [1, 2)$ in the world $[0, 5) \times [0, 3)$? Compare the second count with the bound $3n + 1$.

9. ◦ A [floating random walk](/floating-random-walk-capacitance/) returns one sample per walk, and the samples have a standard deviation 4 times the capacitance $C$ being estimated. How many walks give a standard error of 1 percent of $C$? If a walk takes 5 jumps on average, how many jumps is that?

10. • Use [logical effort](/logical-effort/) on the path NAND3, then NOR2, then an inverter, with electrical effort $H = 45$ and no branching. Take $g = 5/3$ for both gates and $p = 3$, 2 and 1. Find the path effort $F$, the best stage effort, the least delay $D$, and the input capacitance of each gate, from the output back, in units of the path's input capacitance.

11. • A path of $N$ inverters, each with parasitic delay 1, must drive a path effort $F = 1000$. Compute the least delay $N F^{1/N} + N$ for $N = 3, 4, 5, 6, 7$ and say which $N$ is best. Is the best stage effort near 4?

12. • In [van Ginneken's algorithm](/van-ginneken-buffer-insertion/), a node has the candidate (load, required time) pairs $(2, 30)$, $(5, 34)$ and $(9, 40)$. A buffer has input capacitance 1 and delay $2 + 1 \cdot \text{load}$. Add the buffered candidates, prune, and give the list. A driver with resistance 2 drives the node directly, so the slack measure is $q - 2C$: which candidate wins? Separately, prune the list $(5, 20)$, $(3, 18)$, $(4, 22)$, $(6, 21)$, $(2, 10)$.

13. • [Tsay's merge](/tsay-zero-skew/) joins subtree A (delay 2, load 1) and subtree B (delay 0, load 1) by a wire of length $L = 4$ with resistance and capacitance 1 per unit length. Find the fraction $x$ of the wire from A to the tapping point that gives equal Elmore delays, the common delay, and the load of the merged tree, all as exact fractions.

14. • Two registers form a loop: the path from register 1 to register 2 has longest delay 6 and shortest delay 2, and the path back has longest delay 10 and shortest delay 3. Setup and hold times are 0. Find the least period with zero skew, and the least period with [clock skew scheduling](/clock-skew-scheduling/), with the clock arrival difference $c_1 - c_2$ that reaches it. Check both hold constraints.

15. • In [statistical timing](/statistical-static-timing-analysis/), two independent arrival times are $N(10, 1)$ and $N(11, 1)$. Use Clark's formulas to find the mean and standard deviation of their max to three decimals. Do the same for two independent $N(10, 1)$.

16. • A ladder of two sections has $R_1 = R_2 = 1$ and $C_1 = C_2 = 1$, with the output at the far end. Compute the first six moments of its transfer function, fit the two-pole model of [asymptotic waveform evaluation](/asymptotic-waveform-evaluation/), and give its poles. Compare the 50 percent delay of the one-pole model, $3 \ln 2$, with the exact 50 percent delay.

17. • A chain of three gates has delay $(1 + x_1) + (1 + x_2 / x_1) + (1 + 27 / x_2)$, where the first gate has size 1 and $x_1$, $x_2$ are the sizes of the next two. Find the least delay with continuous sizes. With sizes from $\{1, 2, 4, 8\}$, find the least delay, and the least area $1 + x_1 + x_2$ that meets a delay target of 13 and of 14. ([Gate sizing](/gate-sizing/).)

18. • Compute the [SCOAP](/scoap/) controllabilities $CC0/CC1$ of $\bar a$, $p$, $q$ and $z$, and the observabilities $CO$ of every line, for the multiplexer of exercise 6. Inputs have $CC0 = CC1 = 1$ and the output has $CO = 0$.

19. • The circuit $y = \mathrm{AND}(a_1, b)$, $z = \mathrm{OR}(a_2, y)$, where $a_1$ and $a_2$ are the branches of the stem $a$, has 12 single stuck-at faults. Collapse them by structural equivalence and give the number of classes. Which faults are redundant, and what function does the circuit compute? Group the faults by the function of the faulty circuit.

20. • A [built-in self-test](/built-in-self-test/) feeds an 8-input AND gate with independent uniform random patterns. How many patterns are needed so that the output stuck-at-0 fault is detected with probability at least 0.99?

21. • In [multiple patterning](/multiple-patterning-decomposition/), the conflict graph is the wheel with a hub joined to the five vertices of a 5-cycle. How many masks are needed with no conflict and no stitch? If the conflict graph is just the 5-cycle and only two masks are available, what is the least number of conflict edges left inside a mask, and which problem does this count come from?

22. ★ A two-level circuit has an inverter on each input, AND gates fed by inputs or their complements, and one OR gate at the output. Show that deciding whether the output stuck-at-1 fault is detectable is NP-complete, and that the output stuck-at-0 fault can be decided in linear time. What does this say about statements that fault detection is easy for two-level circuits?

23. ★ A circuit has inputs $a$ and $s$. Let $x = s\ ?\ P(a) : a$ and $y = s\ ?\ x : Q(x)$, where $P$ and $Q$ are buffers of delay 5 and each multiplexer has delay 1 from every input; $a$ and $s$ arrive at 0. Give the topological delay that [static timing analysis](/static-timing-analysis/) reports for $y$, and the true delay. Explain the gap as a [false path](/false-path/).

24. ★ In van Ginneken's algorithm, two pruned lists of sizes $a$ and $b$ meet at a branch, where loads add and required times take the min. Show that a pruned list sorted by load has strictly increasing required times, and that the pruned merged list has at most $a + b - 1$ pairs. Give an example where the bound is reached with $a = b = 2$.

25. ★ The space tiles of a corner-stitched plane with $n$ solid tiles number at most $3n + 1$. Show that this bound is reached for every $n$: take the solid squares $[2i + 1, 2i + 2)^2$ for $i = 0, \dots, n - 1$ in the world $[0, 2n + 1)^2$ and count the strips. Explain why these strips are maximal and no two of them can be one tile, and give the total number of tiles, solid and space.

26. ★ Redo exercise 14 with the shortest delays $1/2$ from register 1 to register 2 and $1$ back. Find the least period and the skew that reaches it, and show that no smaller period works by adding the constraints along a loop.
