1. (a), (b), (c) and (d) are noninterfering: the final $l$ is the starting $l$ in (a), always 1 in (b) and always 0 in (d), and (c) writes only $h$. (e) leaks: $l = 0, h = 1$ and $l = 0, h = 0$ end with $l = 1$ and $l = 0$. (f) leaks: $h = 0$ and $h = 1$ give $l = 0$ and $l = 1$.

4. It reports (a), (d) and (f), where an expression that contains $h$ is assigned to $l$, so (a) and (d) are false alarms. It misses (e): the leak is an implicit flow through the branch, and taint follows data dependences only.

6. (a) yes; (b) no, $B \not\le A$; (c) yes; (d) no for a flow check on levels, since $A \not\le \mathit{Low}$, although the program is noninterfering because $a - a = 0$; (e) no, the branch on $a$ makes an implicit flow from $A$ to $B$; (f) yes, both assignments go to levels at or above $\mathit{Low}$.

8. (a) If $s_1 =_L s_2$ and both runs of $P_1;\ P_2$ stop, the intermediate states are low-equivalent because $P_1$ is noninterfering, and then the final states are low-equivalent because $P_2$ is. (b) $P_1 = (l := 0)$ and $P_2 = (l := 1)$.

9. A set whose complement is recursively enumerable, and which is itself recursively enumerable, is decidable: run both enumerations side by side. Noninterference is undecidable, so its set is not recursively enumerable. If every noninterfering program had a proof that an algorithm can check, listing all proofs would enumerate the set.

10. From $h = 0$ the possible final values of $l$ are $\{0, 1\}$, and from $h = 1$ they are $\{1, 0\}$, the same set. Always choosing the left branch gives $l := h$, which leaks. A refinement removes behaviours, and the removed behaviours were what hid the secret, so possibilistic noninterference is not kept by refinement. This is called the refinement paradox.
