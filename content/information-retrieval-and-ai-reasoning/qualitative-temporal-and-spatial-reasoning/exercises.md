1. ◦ From the composition table of [Allen's interval algebra](/allens-interval-algebra/), find $o \circ s$ and $d \circ o$. For $d \circ o$, give concrete intervals $X$, $Y$, $Z$ with $X \mathrel{d} Y$ and $Y \mathrel{o} Z$ for which $X \mathrel{b} Z$, and others for which $X \mathrel{s} Z$.

2. ◦ [RCC5](/rcc5/) merges some base relations of [RCC8](/region-connection-calculus-rcc8/). Which RCC8 base relations become DR, and which become PP? Translate the RCC8 relations $\{EC, TPP, NTPP\}$ and $\{DC, EQ\}$ into RCC5.

3. ◦ Decide each [point algebra](/point-algebra/) network and say why: (a) $x < y$, $y \le z$, $z \le x$; (b) $x \le y$, $y \le z$, $z \le x$, $x \ne z$; (c) $x \le y$, $y \le z$, $x \ne z$.

4. ◦ Let $a = (0, 0)$, $b = (3, -2)$ and $c = (3, 5)$. Give the [cardinal direction](/cardinal-direction-calculus/) of $a$ to $b$, of $b$ to $a$, and of $c$ to $b$.

5. ◦ Let $A = [0, 2] \times [1, 4]$ and $B = [2, 5] \times [0, 3]$. Give the [rectangle algebra](/rectangle-algebra/) relation of $A$ to $B$ and of $B$ to $A$.

6. ◦ Let $A = [0, 1]^2$ and $B = [1, 2] \times [0, 1]$. Give the [4-intersection](/nine-intersection-model/) matrix of $A$ and $B$ (interior and boundary of each) and name the relation. What are the matrix and the relation when $B$ moves to $[2, 3] \times [0, 1]$?

7. ◦ Let $a = (1, 1)$ and $b = (1, 4)$. Give the [double-cross](/double-cross-calculus/) relation of each point $c$ to the oriented segment $(a, b)$: $(0, 2)$, $(3, 6)$, $(1, 0)$ and $(2, 1)$.

8. ◦ Three objects $s$, $m$ and $d$ have $T(s) > T(m) > T(d)$. Heat paths join $s$ to $m$ and $m$ to $d$, and nothing else acts. Using the heat-flow process of [qualitative process theory](/qualitative-process-theory/), give the sign of the derivative of the heat of each object. Which one is ambiguous, and how many branches does it give?

9. ◦ A [simple temporal network with uncertainty](/simple-temporal-network-with-uncertainty/) has a contingent link from $A$ to $C$ with duration in $[2, 5]$ and one requirement, $t_C - t_A \le 4$. Is it strongly, dynamically or weakly controllable? What if the requirement is $t_C - t_A \le 6$?

10. • A [TCSP](/temporal-constraint-satisfaction-problem/) on $X_0$, $X_1$, $X_2$ has $X_1 - X_0 \in [0, 5] \cup [10, 15]$, $X_2 - X_1 \in [0, 5] \cup [10, 15]$ and $X_2 - X_0 \in [22, 24]$. How many STP labelings does it have, and which are consistent? Give the minimal network.

11. • Run [algebraic closure](/algebraic-closure/) on the interval network $I_0 \{s, d\} I_1$, $I_1 \{m\} I_2$, $I_2 \{o, s\} I_3$, $I_0 \{b, m, o, di\} I_3$, with every other label universal. Give the closed labels on $(I_0, I_2)$, $(I_0, I_3)$ and $(I_1, I_3)$, and give a solution.

12. • In RCC8, let $A \mathrel{TPP} B$, $B \mathrel{TPP} C$ and $C \mathrel{EC} D$. Find the labels that closure gives on $(A, C)$, $(A, D)$ and $(B, D)$. What happens if you add $A \mathrel{PO} D$?

13. • For each RCC8 relation $\{NTPP, EQ\}$, $\{EC, NTPP\}$ and $\{TPP, TPPi\}$, say which of the [maximal tractable classes](/rcc8-tractable-subclasses/) $\hat{H}_8$, $C_8$ and $Q_8$ contain it. A network uses base relations together with both $\{NTPP, EQ\}$ and $\{EC, NTPP\}$. Does one of the three theorems tell you that closure decides it?

14. • For each interval relation $\{b, o\}$, $\{b, d\}$, $\{m, mi\}$ and $\{o, s, fi\}$, say whether it is [ORD-Horn](/ord-horn-subclass/), whether it is pointisable, and whether it is convex. For $\{b, d\}$, give the smallest ORD-Horn relation that contains it.

15. • Use the [strongly connected components](/point-algebra-consistency/) method on the point network $x_1 \le x_2$, $x_2 \le x_3$, $x_3 \le x_1$, $x_1 \ne x_4$, $x_4 \le x_2$, $x_3 < x_5$. Is it consistent? If so, give a solution. Then add $x_2 \le x_4$ and decide again.

16. • Two jobs share a machine. Job $A$ takes 4 time units and must end by time 6. Job $B$ takes 3 units and cannot start before time 1. Both start at time 0 or later. Write this as a [disjunctive temporal problem](/disjunctive-temporal-problem/) with makespan bound $D$, and find the smallest $D$. For the order "$B$ first", give the negative cycle that rules it out.

17. • For cardinal directions of points, compute $N \circ S$, $NE \circ N$ and $NW \circ SE$.

18. • A contingent link from $A$ to $C$ has duration in $[2, 6]$, and $B$ is an executable time point. Classify the network as strongly, dynamically or weakly controllable (each that applies) when the requirement is (a) $0 \le t_C - t_B \le 5$; (b) $1 \le t_C - t_B \le 3$. In case (a), give every integer offset $t_B - t_A$ that works.

19. • In [QSIM](/qsim/), a body cools toward room temperature. Let $T$ be its excess temperature and $R = T'$, with DERIV$(T, R)$ and $M^-(R, T)$ with the corresponding values $(0, 0)$. The quantity spaces are $-\infty, 0, T_0, \infty$ for $T$ and $-\infty, 0, \infty$ for $R$. At $t_0$, $T = T_0$ dec and $R \in (-\infty, 0)$ inc. Give the state on $(t_0, t_1)$. Then list the candidate transitions from it, the tuples that both constraints accept, and the behavior that QSIM returns.

20. • Write the interval relation $\{b, o\}$ as a conjunction of point relations between the endpoints $x^-, x^+, y^-, y^+$. Which point relation does it need that the convex point algebra lacks? Do the same for $\{b, m, o\}$.

21. ★ Prove that an algebraically closed network of three intervals with no empty label is consistent. Then explain why the proof does not extend to four intervals.

22. ★ Let $A_{\equiv}$ be the set of interval relations that contain $eq$, together with the empty relation. Show that it has 4097 relations, that it is closed under intersection, converse and composition, and that consistency of networks over $A_{\equiv}$ is decided in $O(n^2)$ time.

23. ★ Prove that strong controllability implies [dynamic controllability](/dynamic-controllability/), and that dynamic controllability implies weak controllability.

24. ★ Build an STNU with one contingent link, one executable point and one requirement that is dynamically but not strongly controllable. Give the dispatch strategy and the reason no fixed schedule works.

25. ★ Run the reductions of [Morris's algorithm](/morris-dynamic-controllability/) on network (b) of exercise 18. Put it in normal form, draw the labelled distance graph, apply one lower-case and one upper-case reduction, and find a negative cycle in the AllMax projection.
