1. ◦ A designer wrote $f = a \oplus b$, and the netlist computes $g = a \vee b$. Build the [miter](/miter-circuit/) of $f$ and $g$ and list every input on which its output is 1.

2. ◦ For the decision `a && b`, find a smallest set of evaluations that reaches 100 percent unique-cause MC/DC, as defined in [code coverage metrics](/code-coverage-metrics/). How many evaluations does it have, and which ones?

3. ◦ A controller declares four states A, B, C, D and six arcs. State D is unreachable from reset, and two of the six arcs leave D. A test suite visits A, B and C and takes three of the four arcs among them. Give the state and arc coverage of [FSM coverage](/fsm-coverage/) with the declared denominator and with the reachable denominator.

4. ◦ A covergroup has 4 bins, and each simulation run hits exactly one of them, uniformly at random and independently of other runs. What is the expected number of runs until every bin of this [functional coverage](/functional-coverage/) model is hit?

5. ◦ A two-flip-flop synchronizer has $\tau = 20$ ps. By what factor does the [MTBF](/synchronizer-mtbf/) grow when a third flip-flop at 1 GHz adds 1 ns of resolution time? How much extra resolution time multiplies the MTBF by 10?

6. ◦ An asynchronous FIFO of depth 8 uses Gray-coded pointers, as in [CDC verification](/clock-domain-crossing-verification/). How many bits does each pointer have? Give the Gray code of the pointer value 11, and the number of bits that change from 7 to 8 in binary and in Gray code.

7. ◦ A 2-bit binary counter changes from 01 to 10 at the moment the other clock domain samples it, and each bit, synchronized on its own, settles to its old or its new value. Which values can the destination see? Answer the same question for a Gray counter that changes from 01 to 11.

8. ◦ The SVA property `req |-> ##[1:3] gnt` is checked on a trace where `req` is 1 in cycles 0 and 2 and `gnt` is 1 only in cycle 4. Which attempts of this [assertion](/assertion-based-verification/) pass, which fail, and in which cycle is each failure reported?

9. ◦ A circuit has one output, some tests fail, and the output gate is among the suspects of [SAT-based design debugging](/sat-based-design-debugging/). Show that the formula has a model for $k = 1$ with the select of the output gate, and that this is a real fix when no two tests have the same input vector. What does this mean for the least $k$ and for the list of sets?

10. • Machine $M_1$ has one state bit $p$, initial 0, next $p \oplus x$, output $p$. Machine $M_2$ has one state bit $q$, initial 1, next $q \oplus x$, output $\neg q$. List the reachable states of the [product machine](/product-machine/) and decide whether the machines are equivalent.

11. • A stimulus is a pair of 4-bit unsigned values $a$, $b$ with the constraint $a + b \le 15$. Count the solutions and give the expected number of draws of [rejection sampling](/rejection-sampling/) per accepted stimulus, as in [constrained random stimulus generation](/constrained-random-stimulus-generation/).

12. • Two 2-bit values have the constraint $a \le b$. Give $P(a = 3)$, $P(a = 0, b = 0)$ and $P(b = 3)$ under the uniform law on solutions, and again under `solve a before b`, where $a$ is uniform over the values that have a solution and then $b$ is uniform given $a$.

13. • A 2-bit value $a$ and a bit $b$ have the constraint $b \vee (a = 0)$, and only $a$ goes to the design. What is $P(a = 0)$ when the pairs are drawn uniformly? What would it be if the values of $a$ that have a solution were drawn uniformly?

14. • The constraint is $C = x_1 \wedge (x_2 \vee x_4)$ over $x_1, \ldots, x_5$, with the order $x_1 < \cdots < x_5$. Count the solutions with the $2^{\text{skip}}$ factors of the [BDD generator](/bdd-constrained-random-generation/), and give $P(x_2 = 1)$ under the uniform law.

15. • The constraint is $C = x_0 \vee (x_1 \wedge x_2)$. The [BDD generator](/bdd-constrained-random-generation/) draws with a bias $p_0 = 1/3$ on $x_0$ and $1/2$ on the other variables. Give $P(x_0 = 1)$ in the samples, and compare it with the bias and with the uniform law.

16. • A circuit has state bits $s_1 s_2$, an input $x$, and next-state functions $\delta_1 = s_2 \oplus x$, $\delta_2 = s_1 \wedge x$. Compute the image of $S = \neg s_1$ with [Coudert-Madre image computation](/transition-function-image-computation/) under the order $s_1 < s_2 < x$, and then the layers of [symbolic reachability](/symbolic-reachability/) from the state 00.

17. • A multiplexer computes $\mathit{out} = (a \wedge b) \vee (\neg a \wedge c)$. An [STE](/symbolic-trajectory-evaluation/) assertion has the antecedent "$b$ is $x$ and $c$ is $x$" and the consequent "$\mathit{out}$ is $x$". Compute the residual. Is the failure real, and how do you fix the check?

18. • A full adder has the sum $s = a \oplus b \oplus c$ and, by a bug, the carry $c_{\mathrm{out}} = a \vee b \vee c$. Rewrite $2c_{\mathrm{out}} + s - a - b - c$ backward with the gate polynomials of [algebraic verification](/algebraic-arithmetic-circuit-verification/), give the remainder and the counterexample of least degree, and check it by simulation.

19. • Circuit 1 computes $u = a \oplus b$ and $\mathit{out}_1 = u \oplus b$. Circuit 2 computes $\mathit{out}_2 = a$. A [cutpoint](/cutpoint-equivalence-checking/) checker puts a free variable in place of $u$. List the points $(u, a, b)$ where the cut miter is 1, show that each is a false negative, and say how the method resolves them.

20. • With $\tau = T_W = 20$ ps, $f_c = 1$ GHz and $f_d = 10^8$ per second, what resolution time gives one [synchronizer](/synchronizer-mtbf/) an MTBF of 10 years? A chip has 1000 such synchronizers, and the whole chip must have an MTBF of 10 years. What resolution time does each need?

21. ★ Each run hits exactly one of three bins, with probabilities $1/2$, $1/4$ and $1/4$. Find the exact expected number of runs until all three are hit, and compare it with three equally likely bins.

22. ★ A covergroup has a coverpoint $A$ with 4 bins, a coverpoint $B$ with 3 bins and their cross with 12 bins. Each run samples one pair, with $A$ and $B$ uniform and independent. Find the expected number of runs to cover the cross, and the exact expected number to cover both coverpoints.

23. ★ A circuit has $p = x \wedge b$, $q = x \wedge c$ and the output $y = p \oplus q$. For the vectors $(x, b, c) = (1, 1, 1)$ and $(1, 1, 0)$, give the sites observable at $y$ and the tagged sites of [observability-based coverage](/observability-based-coverage/). Explain both results by reconvergence.

24. ★ Design A is a 2-bit counter $0 \to 1 \to 2 \to 0$, with $3 \to 0$, and output $s = 2$. Design B is a 3-bit ring $(b_1, b_2, b_3) \mapsto (b_3, b_1, b_2)$ starting at 100, with output $b_3$. Both start together. On the [product machine](/product-machine/) with the property "the outputs agree", give the number of reachable states and the least $k$ for which [k-induction](/k-induction/) proves the property. Then add an enable input that makes both designs hold their state when it is 0, and answer again without and with the simple-path constraint.

25. ★ Show that for $w$-bit unsigned words the polynomial $2^{w-1}(x^2 + x)$ is 0 modulo $2^w$ for every $x$, although its [Taylor expansion diagram](/taylor-expansion-diagram/) over the rationals is not the zero diagram. What does this say about comparing two datapaths by their diagrams?
