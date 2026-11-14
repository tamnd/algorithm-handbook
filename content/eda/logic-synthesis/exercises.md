In these exercises a minterm of $x_1, \ldots, x_n$ is numbered with $x_1$ as the high bit, and a cube is written in positional notation, as on the [sum of products](/sum-of-products/) page.

1. ◦ Over $x_1, x_2, x_3, x_4$, write the cube $x_1 \bar{x}_3$ in positional notation and list the minterms it covers. How many cubes over four variables contain the minterm 5?

2. ◦ Find all [prime implicants](/prime-implicant/) of $f = \sum m(0, 1, 2, 3, 5, 7)$ over $x_1, x_2, x_3$, say which are essential, and give a minimum sum of products.

3. ◦ Is the multiplexer $f = x_1 x_2 + \bar{x}_1 x_3$ a [unate function](/unate-function/)? For each variable, say whether $f$ is positive unate, negative unate or binate in it, with a pair of input vectors as a witness for each binate variable.

4. ◦ Divide $F = abx + aby + cx + cy + z$ by $D = x + y$ with [algebraic division](/algebraic-division/). Give the quotient and the remainder, and the literal count of $F$ before and after the rewrite $F = (x + y)Q + R$.

5. ◦ List every [kernel](/algebraic-kernel/) of $F = abd + abe + cd + ce$ with all of its cokernels. Use them to write $F$ as a product of two sums, and compare the literal counts.

6. ◦ Draw the decomposition chart of the majority function $\mathrm{MAJ}(x_1, x_2, x_3)$ with the bound set $\{x_1, x_2\}$, and count its distinct columns $\mu$. How many functions $h_i$ does an [Ashenhurst-Curtis decomposition](/ashenhurst-curtis-decomposition/) with this bound set need?

7. ◦ The [and-inverter graph](/and-inverter-graph/) page gives the 8-bit truth tables 240, 204 and 170 for $a$, $b$ and $c$. Give the truth table of $a \wedge \neg(b \wedge c)$ as a number, and the number of AND nodes it takes.

8. ◦ Let $e = (a, b)$, $f = (c, d)$ and $o = (e, f)$ be two-input gates over the inputs $a, b, c, d$. List the [$k$-feasible cuts](/k-feasible-cut/) of $o$ for $k = 4$ and for $k = 3$, counting the trivial cut $\{o\}$.

9. ◦ A data flow graph has unit-delay operations $v_1 = a \cdot b$, $v_2 = c \cdot d$, $v_3 = v_1 + v_2$, $v_4 = e \cdot f$, $v_5 = v_3 + v_4$ and $v_6 = g + h$. Give the [ASAP and ALAP](/asap-alap-scheduling/) start steps for the latency bound $L = 4$, and the mobility of each operation.

10. ◦ In a [retiming](/retiming/), a gate $v$ has three fanin edges with no register and two fanout edges with one register each. What are the register counts of these edges after the retiming with $r(v) = 1$ and $r = 0$ elsewhere? Is $r(v) = 2$ legal?

11. • Find all prime implicants of $f = \sum m(0, 4, 5, 7, 8, 9, 11, 15)$ over four variables. Show that no prime is essential, and use [Petrick's method](/petricks-method/) to find every cover with the fewest cubes.

12. • Minimize $f = \sum m(0, 1, 2, 5, 6, 7, 8, 9, 10, 14)$ over four variables: find the essential primes, the minterms they leave, and a minimum sum of products. Is the minimum unique?

13. • Let $f = \sum m(2, 3, 6, 7, 9, 13)$ with the [don't-care](/dont-care-condition/) set $d(1, 5, 11)$ over four variables. Give a minimum sum of products without the don't-cares and with them, and the literal counts.

14. • A [Boolean network](/boolean-network/) has the nodes $y = ad + ae + bd + be$ and $z = cd + ce + f$. Build the rows of the kernel-cube matrix, find the rectangle of largest value for [kernel extraction](/kernel-extraction/), and give the network and the literal count after the extraction. Does a second round save anything?

15. • Show that every implicant of the parity function of $n \ge 1$ inputs is a minterm. How many cubes and literals does a minimum sum of products of 4-input parity have?

16. • $\mathrm{XOR}(x_1, x_2, x_3)$ and $\mathrm{MAJ}(x_1, x_2, x_3)$ are both 1 on four rows, so counting rows does not tell them apart. Show that they are not equivalent under any permutation and negation of the inputs and negation of the output, the NPN form of [Boolean matching](/boolean-matching/).

17. • A supergate of an AIG has six leaves at the levels 0, 0, 0, 0, 2 and 3. What is the least level of a tree of two-input ANDs over these leaves, and which pairs does [AIG balancing](/aig-balancing/) join?

18. • A library has INV of area 2 with pattern INV($x$), NAND2 of area 3 with pattern NAND($x$, $x$), AND2 of area 4 with pattern INV(NAND($x$, $x$)) and NAND3 of area 4 with pattern NAND($x$, INV(NAND($x$, $x$))), in either input order. Run [tree covering](/tree-covering-technology-mapping/) on the subject tree $o = \mathrm{INV}(\mathrm{NAND}(\mathrm{INV}(\mathrm{NAND}(a, b)), c))$ and give the least area. What changes if AND3 of area 5 with pattern INV(NAND($x$, INV(NAND($x$, $x$)))) is added?

19. • A chain of two-input AND gates computes the AND of 9 inputs, $g_1 = (x_1, x_2)$ and $g_i = (g_{i-1}, x_{i+1})$ for $i = 2, \ldots, 8$. What depth does [FlowMap](/flowmap/) give with $K = 3$? What depth does it give for a network of four 3-input AND gates that computes the same function?

20. • A machine has 5 states, coded with 3 state bits. How many injective codes are there, and how many classes remain when codes that differ only by a permutation and complementation of the bits are counted once, as on the [state assignment](/state-assignment/) page? Check your formula on 4 states with 2 bits.

21. • In a network over $a, b, c, d$, the node $y = ab$ feeds the two outputs $z_1 = y + c$ and $z_2 = y d$. Give the [observability don't-care](/observability-dont-care/) set of $y$ as a cube, and say whether $y$ may be replaced by the wire $a$.

22. • For the data flow graph of exercise 9 with $L = 3$, with multiplies and ALU operations on separate unit types, compute the distribution graphs of [force-directed scheduling](/force-directed-scheduling/) for both types. What is the least number of units at $L = 3$, and the least latency with one multiplier and one ALU?

23. ★ Let $F$ be the product $(a_1 + b_1 + c_1)(a_2 + b_2 + c_2) \cdots (a_k + b_k + c_k)$ multiplied out. Count its distinct kernels and its pairs of cokernel and kernel, and check the numbers for $k = 3$. Generalize to sums of $s$ literals.

24. ★ Let $y_1 = ab$ and $y_2 = ac$ over the inputs $a, b, c$, with the one output $z = y_1 + y_2$. Find $\mathrm{ODC}(y_1)$ and $\mathrm{ODC}(y_2)$, show that changing both nodes inside their full sets at once can change $z$, and give compatible don't-care sets for the order $y_1, y_2$.

25. ★ Write a program that counts the classes of 3-input functions under permutation and negation of the inputs (NP) and under NPN. The [Boolean matching](/boolean-matching/) page gives one of the two numbers.

26. ★ A ring of three gates with delay 3 each has two registers on its edges, and no host. Show that the least clock period over all retimings is 6, although the bound $\max(\max_i d_i, \lceil \sum_i d_i / W \rceil)$ gives only 5.

27. ★ Show that the majority of three inputs needs 4 AND nodes in an and-inverter graph and give such a graph. How many nodes does a [majority-inverter graph](/majority-inverter-graph/) need?
