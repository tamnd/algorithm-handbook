1. $o \circ s = \{o\}$ and $d \circ o = \{b, m, o, s, d\}$. With $Y = (0, 4)$ and $Z = (3, 6)$, take $X = (1, 2)$ for $X \mathrel{b} Z$ and $X = (3, 3.5)$ for $X \mathrel{s} Z$.

3. Draw an edge $u \to v$ for each $u \le v$ or $u < v$, and find the strongly connected components. A network is inconsistent exactly when some component contains a $<$ edge or a $\ne$ pair. (a) Inconsistent: $x$, $y$, $z$ form one component, and it contains $x < y$. (b) Inconsistent: the cycle forces $x = y = z$, against $x \ne z$. (c) Consistent: $x = 0$, $y = 1$, $z = 2$, for example. Closure refines the label of $(x, z)$ to $\le \cap \ne$, that is $<$.

5. On the $x$ axis $(0, 2)$ meets $(2, 5)$, and on the $y$ axis $(1, 4)$ starts inside $(0, 3)$ and ends after it. So $A \mathrel{(m, oi)} B$, and by taking converses on each axis $B \mathrel{(mi, o)} A$.

7. With $d = (0, 3)$: $(0, 2)$ is left, between; $(3, 6)$ is right, front; $(1, 0)$ is straight, back; $(2, 1)$ is right, at $a$. For $(2, 1)$ the cross product is $-3$ and $p = 0$.

10. There are $2 \cdot 2 \cdot 1 = 4$ labelings. The sums of the chosen intervals are $[0, 10]$, $[10, 20]$, $[10, 20]$ and $[20, 30]$, and only the last meets $[22, 24]$. That labeling is the STP with $X_1 - X_0, X_2 - X_1 \in [10, 15]$ and $X_2 - X_0 \in [22, 24]$. Its minimal network is $X_1 - X_0 \in [10, 14]$, $X_2 - X_1 \in [10, 14]$, $X_2 - X_0 \in [22, 24]$, since each of the first two is at least $22 - 15 = 7$ and at most $24 - 10 = 14$.

12. $TPP \circ TPP = \{TPP, NTPP\}$, so $(A, C)$ gets $\{TPP, NTPP\}$. Both $TPP \circ EC$ and $NTPP \circ EC$ lie in $\{DC, EC\}$, so $(A, D)$ and $(B, D)$ get $\{DC, EC\}$. Adding $A \mathrel{PO} D$ empties the label of $(A, D)$: a part of $C$ cannot overlap a region that only touches $C$.

14. $\{b, o\}$ is ORD-Horn and pointisable but not convex. $\{b, d\}$ and $\{m, mi\}$ are not ORD-Horn. $\{o, s, fi\}$ is ORD-Horn but not pointisable. The ORD-Horn hull of $\{b, d\}$ is $\{b, o, d\}$, which is pointisable: $x^+ < y^+$, $x^- \ne y^-$, $x^+ \ne y^-$. All of these were checked against the 868 relations generated from ORD-Horn clauses.

16. With start times $s_A, s_B$ and end times $e_A = s_A + 4$, $e_B = s_B + 3$, the constraints are $s_A \ge 0$, $s_B \ge 1$, $e_A \le 6$, $e_A \le D$, $e_B \le D$ and the disjunction $e_A \le s_B \lor e_B \le s_A$. "$A$ first" gives $s_A = 0$, $s_B = 4$ and $D = 7$. "$B$ first" chains $s_B \ge 1$, $s_A \ge e_B = s_B + 3$ and $e_A = s_A + 4$, so $e_A \ge 8$, against $e_A \le 6$: with a time origin $Z$, the cycle $Z \to e_A \to s_A \to s_B \to Z$ has weights $6$, $-4$, $-3$, $-1$, in total $-2$.

18. For a fixed offset $w = t_B - t_A$ the requirement must hold for every duration $d \in [2, 6]$. (a) Needs $2 - w \ge 0$ and $6 - w \le 5$, so $w \in \{1, 2\}$: strongly, hence dynamically and weakly, controllable. (b) Needs $w \le 1$ and $w \ge 3$, so not strong. $B$ must precede $C$, so it cannot wait to see $C$; if $C$ can come at 2, then $B$ must run by time 1, and then $C$ at 6 is too late. So not dynamic either. It is weakly controllable: for known $d$ take $w = d - 2$.

20. $\{b, o\}$ is $x^- < y^-$, $x^+ < y^+$ and $x^+ \ne y^-$; the last excludes $m$ and needs $\ne$. $\{b, m, o\}$ is $x^- < y^-$ and $x^+ < y^+$ alone, so it is convex.

21. Pick a base relation $r_{02}$ in the label of $(I_0, I_2)$. Closure gives $r_{02} \in R_{01} \circ R_{12}$, so some $r_{01} \in R_{01}$ and $r_{12} \in R_{12}$ have $r_{02} \in r_{01} \circ r_{12}$. Composition in the interval algebra is exact, so three intervals realize the triple. With four intervals, the choices for different triangles must agree on shared edges, and the network on the [NP-completeness](/interval-algebra-np-completeness/) entry, $0\{o, si\}1$, $0\{fi, si\}2$, $0\{o, fi\}3$, $1\{m, mi\}2$, $1\{b, f\}3$, $2\{b, s\}3$ is closed and inconsistent. A check on 1528 random closed three-interval networks (`random.Random(7)`, 3000 draws) found none inconsistent.

22. Twelve base relations besides $eq$ give $2^{12}$ relations that contain $eq$, plus the empty one. Intersection keeps $eq$; $eq$ is its own converse; and $eq \in eq \circ eq \subseteq R \circ S$. A network with no empty label is solved by making all intervals equal, so the test is one scan of the labels.

24. Take a link from $A$ to $C$ in $[1, 3]$ and require $1 \le t_B - t_C \le 2$. Strategy: wait for $C$, then execute $B$ one unit later. A fixed offset $w$ would need $w \ge 3 + 1$ and $w \le 1 + 2$.

25. Normal form: add $A'$ with $t_{A'} - t_A = 2$, and a link from $A'$ to $C$ in $[0, 4]$. Edges: $B \to C$ weight 3 and $C \to B$ weight $-1$ from the requirement, lower-case $A' \to C$ $c{:}0$, upper-case $C \to A'$ $C{:}{-4}$, and the ordinary edges of the link and of $A \to A'$. The lower-case reduction of $A' \to C \to B$ gives $A' \to B$ weight $-1$. The upper-case reduction of $B \to C \to A'$ gives $B \to A'$ $C{:}{-1}$, and its label stays since $-1 < 0$. The cycle $A' \to B \to A'$ has weight $-2$, so the network is not dynamically controllable, as exercise 18 found.
