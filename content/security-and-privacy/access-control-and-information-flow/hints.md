1. The list of $f$ is ann: $\{\text{own}, r, w\}$, cy: $\{r\}$. The list of cy is $f$: $\{r\}$, $h$: $\{\text{own}, r, w\}$. Both views store the 6 nonempty cells of the 9, so each holds 6 entries in all.

4. $o_1$: read only. $o_2$: read, append and write. $o_3$: append only, since $f_c$ does not dominate it. $o_4$: append only, since reading fails the simple security property. $o_5$: nothing, since $\{\text{NATO}\}$ and $\{\text{Crypto}\}$ are incomparable.

5. The level becomes system $\sqcup$ user = user. It may modify the user file and the web file, but not the system file.

7. GRANT and REVOKE are mono-operational; CREATE has two operations. CREATE and GRANT are monotonic; REVOKE deletes. All three are monoconditional. Safety is decidable for the first system because it is mono-operational, and for the second because it is monotonic and monoconditional.

9. The system accepts (a), (b) and (d), and rejects (c) and (e). Only (e) is noninterfering: its $l$ is always 0.

11. The outputs 0 to 3 are all possible, so the min-entropy leakage is $\log_2 4 = 2$ bits. The output distribution is $(3, 3, 2, 2)/10$, and its Shannon entropy is about 1.971 bits.

13. No single user holds $P$, and the only pair that does is $\{u_2, u_4\}$. So the policy holds for $k \le 2$ and fails first at $k = 3$, broken by $\{u_2, u_4\}$ alone.

14. The rank is 4. The counting bound gives only $\lceil \log_2 5 \rceil = 3$. The pairs $(u_i, p_i)$ form an isolated set of size 4: no role can cover two of them, because for $i \ne j$ one of $(u_i, p_j)$ and $(u_j, p_i)$ is a 0.

16. $a$, $b$, $c$ and $d$ are joined by $t$ and $g$ edges, and $d$ holds $r$ to $e$, so $\mathit{can\_share}(r, a, e)$ holds. One sequence: $c$ takes ($r$ to $e$) from $d$; $c$ grants ($r$ to $e$) to $b$; $a$ takes ($r$ to $e$) from $b$. $f$ has no $t$ or $g$ edge at all, so $\mathit{can\_share}(r, f, e)$ is false.

17. Clinic.partner is $\{\text{HospA}, \text{HospB}\}$, so Clinic.view is $\{\text{Dan}, \text{Eve}\}$; Fay is out because HospC is no partner. Clinic.write is $\{\text{Eve}\}$. Without the missing credential, Clinic.view is $\{\text{Dan}\}$ and Clinic.write is empty.

19. (a) With $h = 0$ the run ends with $l = 0$ labeled $L$. With $h = 1$ the first assignment lowers the label of $t$ to $L$ at a public pc, and the assignment $t := 1$ under the secret branch is an upgrade, so the monitor stops. (b) Now $t$ keeps label $H$, both runs end with $l$ labeled $H$, and the public observer sees nothing. (c) $t = \langle 1 : 0 \rangle$ and $l = \langle 1 : 0 \rangle$; the public view of $l$ is 0 for both values of $h$.

21. (a) and (c) satisfy it, since their outputs are functions of $h_1 + h_2$. (b) fails: the stores $(h_1, h_2) = (0, 1)$ and $(1, 0)$ have the same sum but give $l = 2$ and $l = 0$. (d) fails: $(0, 0)$ and $(1, -1)$ give $l = 0$ and $l = 2$.

23. The capacity per slot is $1 - H(0.05) \approx 0.7136$ bits. At 200 slots per second this is about 142.7 bit/s, above the 100 bit/s that TCSEC calls high. At 50 slots per second it is about 35.7 bit/s, below that line but well above 1 bit/s, so it must still be audited.

25. Lower bound: suppose $k$ roles cover the matrix. Let $S_j$ be the set of roles that contain $p_j$ and $T_i$ the set of roles of user $i$; user $i$ has $p_j$ exactly when $T_i \cap S_j \ne \emptyset$. If $S_j \subseteq S_i$ for some $j \ne i$, then user $i$ would miss $p_j$ too, so the six sets $S_j$ are pairwise incomparable, and Sperner's theorem gives $\binom{k}{\lfloor k/2 \rfloor} \ge 6$, so $k \ge 4$. Upper bound: give the six permissions six distinct 2-subsets $S_1, \dots, S_6$ of 4 roles, and give user $i$ the roles outside $S_i$. Then user $i$ misses $p_j$ exactly when $S_j \subseteq S_i$, that is when $j = i$.

26. State 1: current level $S$, read access to a secret object. State 2: the subject gives up that access. State 3: it lowers its current level to $U$, which the \*-property allows because it holds no access. State 4: it gets write access to an unclassified object and writes what it remembers. Each state is secure, so the theorem holds, yet the secret reached an unclassified object. The theorem speaks of states, and a state does not record what a subject has read.

27. $x$ creates a new object $n$ with $\{t, g\}$ to it. $x$ grants ($g$ to $n$) to $o$. $z$ takes ($g$ to $n$) from $o$. $z$ grants ($r$ to $f$) to $n$. $x$ takes ($r$ to $f$) from $n$. The path from $x$ to $z$ has the word $\overrightarrow{g}\,\overleftarrow{t}$, a bridge of the form $\overrightarrow{t}^*\,\overrightarrow{g}\,\overleftarrow{t}^*$ with no $t$ edge before the $g$ and one after it.

28. For a deterministic total program, the min-capacity is $\log_2$ of the number of distinct outputs. So the bound fails exactly when some $m + 1$ runs have pairwise distinct outputs, which is a bad set of $(m+1)$-tuples of runs. For $k \le m$, take a program with $m + 1$ outputs, which breaks the bound. Any $k$ of its runs are also runs of a program that keeps those $k$ outputs and maps every other input to one of them; that program has at most $m$ outputs and meets the bound, so no set of bad $k$-tuples can tell the two apart. The case $m = 1$ is 2-safety: zero leakage, that is noninterference.

29. The column maxima are 1 and $1/2$, so the min-capacity is $\log_2(3/2) \approx 0.585$ bits. For Shannon capacity, with $P(x = 1) = q$ the mutual information is $H(q/2) - q$, which is largest at $q = 2/5$ and gives $\log_2(5/4) \approx 0.322$ bits.
