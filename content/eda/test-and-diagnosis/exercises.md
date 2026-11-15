1. ◦ A collapsed fault list has $|\Phi| = 12{,}000$ faults. A test set detects 11,280 of them. The tool proves 240 faults [redundant](/redundant-fault/) and classes 120 more as untestable because of a constraint of the test setup. Give the [fault coverage](/fault-coverage/) and its two related ratios, the one that credits proved redundancy and the one over the testable faults.

2. ◦ A process has yield $Y = 0.75$. Give the [Williams-Brown defect level](/williams-brown-defect-level/) in parts per million for a fault coverage $T = 0.98$, and the least coverage that keeps the defect level at or below 200 ppm.

3. ◦ The circuit is $z = \mathrm{AND}(a, b, c)$ with the 8 single stuck-at faults on $a$, $b$, $c$ and $z$. For each fault, how many input vectors detect it? Give the smallest 1-detect test set, and the size of the smallest [N-detect test](/n-detect-test/) set for $N = 2, 3, 4$ and 7.

4. ◦ The circuit computes $z = ab + \bar a c + bc$ with an OR gate fed by three AND gates; let $g = \mathrm{AND}(b, c)$ be the third. Show that $g$/0 is redundant and that $g$/1 is not, and list all vectors $abc$ that detect $g$/1.

5. ◦ The nets $u = \mathrm{AND}(x_1, x_2)$ and $v = \mathrm{OR}(x_2, x_3)$ are shorted, as in the [bridging fault model](/bridging-fault-model/). Which vectors $x_1x_2x_3$ activate the bridge, so that [IDDQ testing](/iddq-testing/) sees a large current?

6. ◦ The output $z = \mathrm{NAND}(a, b)$ is observed directly. List every two-pattern test $(v_1, v_2)$ on $ab$ for the slow-to-rise and for the slow-to-fall [transition fault](/transition-fault-model/) at $z$.

7. ◦ Give the TMS sequence that takes the [boundary scan](/boundary-scan/) TAP controller from Test-Logic-Reset to Shift-IR. Then give the TMS bits that take it from Shift-IR through Update-IR to Run-Test/Idle.

8. ◦ A circuit has 20,000 collapsed faults and a test set of 500 vectors, and the machine word has 64 bits. Without fault dropping, how many groups of faults does [parallel fault simulation](/parallel-fault-simulation/) need, and how many circuit evaluations does it run in all, against a serial simulator that runs the good circuit and each faulty circuit on every vector? How many words of vectors does [PPSFP](/ppsfp/) use?

9. ◦ Take $g = \mathrm{AND}(a, b)$ and $z = \mathrm{OR}(g, c)$, with every input 1 with probability $1/2$. Give the [COP](/cop-testability-measure/) controllabilities of $g$ and $z$, the observabilities of $a$, $c$ and $g$, and the detection probabilities of $a$/0, $a$/1 and $c$/0. Are they exact here?

10. ◦ In [broadcast scan](/broadcast-scan/), three chains of length 4 share one scan input. A test cube has the care bits 1X0X in chain 1, X10X in chain 2 and 1XX1 in chain 3, by position 1 to 4. Does it fit, and what does the shared input carry? What if chain 3 is 0XX1 instead? A test set has 180 patterns that fit and 20 that need the serial mode; how many tester bits does it use, against 2400 with no broadcast?

11. • A 3-input AND gate in [deductive fault simulation](/deductive-fault-simulation/) has the good values $a = 0$, $b = 0$, $c = 1$ and the fault lists $L_a = \{f_1, f_2\}$, $L_b = \{f_2, f_3\}$ and $L_c = \{f_4\}$. Give the list of its output $z$ and say why each of $f_1$, $f_3$ and $f_4$ is left out.

12. • The fanout-free circuit $z = \mathrm{OR}(g, h)$ with $g = \mathrm{AND}(a, b)$ and $h = \mathrm{AND}(c, d)$ gets the vectors $abcd = 1101$ and $abcd = 0101$. For each, give the critical lines found by [critical path tracing](/critical-path-tracing/) and the faults the vector detects.

13. • Six test cubes on five inputs are 1X0XX, 10XX1, X1X0X, 0XX01, XX1X0 and 1XX11. Find the least number of vectors that [static test compaction](/static-test-compaction/) can merge them into, give one merge that reaches it, and prove that fewer is impossible.

14. • A scan chain runs from the scan-in pin $s = (0, 0)$ to the scan-out pin $e = (6, 0)$ through flip-flops $A = (1, 3)$, $B = (5, 3)$, $C = (2, 1)$, $D = (4, 1)$ and $E = (3, 4)$, with Manhattan wire length. Give the length of the netlist order $A, B, C, D, E$ and the best order for [scan chain ordering](/scan-chain-ordering/). Is the best order unique?

15. • A 3-stage [MISR](/multiple-input-signature-register/) has $q = x^3 + x^2 + 1$ and the update $r \leftarrow (x\,r + w) \bmod q$, with registers and words written $r_2 r_1 r_0$. From 000 it takes the words 110, 011, 100 and 111. Give the register after each clock. Then flip bit $r_0$ of the first word and bit $r_1$ of the second, and give the new signature. Show that an error confined to one word never aliases.

16. • An LFSR for [LFSR reseeding](/lfsr-reseeding/) produces the bits $b_0, b_1, \ldots$ with $b_{t+4} = b_{t+3} \oplus b_t$ from the seed $b_0 b_1 b_2 b_3$, and bit $b_t$ fills scan position $t$. Find every seed for the 8-bit cube X1X0X11X. Then show that the cube 0XX01XXX, with only 3 care bits, has no seed.

17. • A 10-input AND gate is tested by [weighted random patterns](/weighted-random-pattern-testing/). Give the detection probability per pattern of $z$/0 and of each input fault $a_i$/1 under uniform patterns and with every input 1 with probability $0.9$. How many patterns detect one given $a_i$/1 with probability at least 0.999 in each case?

18. • A core for the [SoC test wrapper](/soc-test-wrapper-and-tam-design/) has internal scan chains of lengths 40, 30, 20 and 10, 8 functional inputs, 12 functional outputs and 50 patterns. Give the least test time $T(w)$ and a wrapper that reaches it for $w = 1, 2, 3$.

19. • A path runs from $a$ through $g = \mathrm{AND}(a, b)$ to $z = \mathrm{OR}(g, c)$. List all [robust tests](/robust-path-delay-test/) $(v_1, v_2)$ on $abc$ for the rising and for the falling [path delay fault](/path-delay-fault-model/) on this path, using the rule that a steady input has the same value in both vectors.

20. • A memory of $N = 8$ cells has the idempotent [coupling fault](/memory-coupling-fault/) $\langle \uparrow; 0 \rangle$ with aggressor 3 and victim 6. Show that MATS+ passes it. At which element, address and operation does [March C−](/march-test/) first fail? Answer the same two questions with aggressor 6 and victim 3.

21. • In a circuit with outputs $y = \mathrm{AND}(a, b_1)$ and $z = \mathrm{OR}(b_2, c)$, the stem $b$ has the branches $b_1$ and $b_2$, so there are 14 single stuck-at faults. The tests are $abc = 110$, 001 and 100. Build the full and the pass-fail [fault dictionary](/fault-dictionary/) and count their classes. A chip fails only the first test, with $y$ wrong and $z$ right. Give the candidates from each dictionary, and show that [effect-cause diagnosis](/effect-cause-diagnosis/) reaches the same set as the full dictionary.

22. ★ The stem $a$ has the branches $a_1$ and $a_2$, with $g = \mathrm{AND}(a_1, b)$, $h = \mathrm{AND}(a_2, c)$ and $z = \mathrm{OR}(g, h)$. At $abc = 111$ and at $abc = 000$, find which of $a_1$, $a_2$ and $a$ are critical. Use the result to show that the criticality of a stem is not a function of the criticality of its branches, and list the faults that 111 detects.

23. ★ A $k$-bit MISR has $q_0 = 1$. Count the nonzero error patterns confined to two consecutive words $t$ and $t + 1$ that alias, and show that their share is $1/(2^k + 1)$. Compare it with $2^{-k}$ and with the aliasing formula for $m = 2$ when all error streams are equally likely.

24. ★ A single-input signature register with $q = x^2 + x + 1$ takes a stream of $m = 4$ bits, and each bit is in error with probability $p$, independently. Find the exact aliasing probability $P_4(p)$, its values at $p = 1/10$ and $p = 1/2$, and compare them with the limit $2^{-2}$ of the [aliasing theorem](/signature-aliasing-probability/).

25. ★ An [X-Compact](/x-compact/) matrix has $m = 6$ outputs and all 20 columns of weight 3. Show that it detects any 1, 2 or 3 errors with no X and a single error with one X. Count the sets of 4 errors that cancel, and count, among the pairs (error chain, two X chains), those in which the X's hide the error.

26. ★ Three cores share a test bus of $W = 4$ wires. Their least wrapper test times for widths 1, 2, 3, 4 are 5758, 2904, 2090, 2090 for core A, 5554, 2827, 2625, 2625 for core B, and 3408, 1804, 1403, 1002 for core C. Choose the bus widths and the assignment of cores to buses that make the chip test time least, and give the next best value.
