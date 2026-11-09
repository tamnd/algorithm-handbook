2. The depth is 3, and it holds at every time from 2 to 10: for example at time 4 the talks $c$, $d$ and $e$ are running. Greedy by start time opens three rooms, holding $\{a, d, f, h\}$, $\{b, e, i\}$ and $\{c, g, j\}$.

3. The ratios are 6, 5, 4.5 and 2. The fractional optimum takes $A$ and $B$ whole and half of $C$, for $36 + 40 + 27 = 103$. On whole items the ratio rule takes $A$ and $B$, cannot fit $C$, and adds $D$, for 86. The optimum is $\{B, C\}$ with weight 20 and value 94.

5. $\{1, 3, 7\}$: $q = 2$, $r = 1$, $a - q = 1$, so it is canonical. $\{1, 4, 9\}$: $q = 2$, $r = 1 < 2$; at 12 greedy pays $9 + 1 + 1 + 1$ and the optimum is $4 + 4 + 4$. $\{1, 7, 10\}$: $q = 1$, $r = 3 < 6$; at 14 greedy pays $10 + 1 + 1 + 1 + 1$ and the optimum is $7 + 7$. $\{1, 5, 12\}$: $q = 2$, $r = 2 < 3$; at 15 greedy pays $12 + 1 + 1 + 1$ and the optimum is $5 + 5 + 5$.

7. Earliest due date first runs $e, f, d, c, a, b$, with completion times 2, 6, 8, 13, 17, 20 and lateness $-2, 1, 0, 4, 7, 5$. So $L_{\max} = 7$, and four jobs are late. Moore-Hodgson drops $f$ when $f$ itself is late at time 6, then drops $c$, the longest kept job, when $a$ would finish at 13 after its due date 10. It keeps $e, d, a, b$, all on time, and two jobs end late.

11. Take $[3, 4)$, $[0, 5)$, $[6, 8)$ and $[4, 9)$. By finish time, $[3, 4)$ opens room 1, $[0, 5)$ opens room 2, $[6, 8)$ goes to room 1, and $[4, 9)$ finds room 1 busy until 8 and room 2 busy until 5, so it opens room 3. Two rooms suffice: $\{[0, 5), [6, 8)\}$ and $\{[3, 4), [4, 9)\}$.

12. Earliest finish time first takes $a$ and $c$, worth 6. Largest value first takes $e$, which overlaps all the others, worth 10. Sorted by finish time the talks are $a, b, c, e, d$ with $p = 0, 0, 1, 0, 2$, and $M = 3, 6, 6, 10, 12$. The optimum is $\{b, d\}$, worth 12.

14. The sum of the first $k$ Fibonacci numbers is $F_{k+2} - 1$, and $F_{k+1} \le F_{k+2} - 1 \le F_{k+2}$, so after $k$ files are merged the two smallest piles are the merged file and $F_{k+1}$. The merged files have sizes 2, 4, 7, 12, 20 and 33, and the cost is their sum, 78.

16. $\{1, a, 2a + 1\}$ has $q = 2$ and $r = 1$, so it fails exactly when $1 < a - 2$, that is for $a \ge 4$, and the smallest counterexample is $3a$: greedy pays $2a + 1$ and $a - 1$ ones, against three coins $a$. $\{1, a, 2a - 1\}$ has $q = 1$ and $r = a - 1$, and $r < a - 1$ never holds, so it is canonical for every $a$.

21. Let $w$ be the smallest weight in the greedy basis $B$, and suppose a basis $B'$ uses only weights above $w$. Let $S$ be the set of elements heavier than $w$. Greedy scans all of $S$ before it reaches weight $w$, and what it has kept from $S$ is a maximal independent subset of $S$. Since $B' \subseteq S$ has $r$ elements, every maximal independent subset of $S$ has $r$ elements, so greedy has a full basis before it reaches weight $w$, a contradiction.

22. At $x = (q + 1)a$ greedy pays one $b$ and $a - r$ ones, against $q + 1$ coins $a$, so it loses when $a - r > q$ and $r > 0$. Conversely, if the system is not canonical, the smallest counterexample $x$ lies strictly between $b + 1$ and $a + b$, its optimum uses no $b$, and greedy pays $1 + (x - b)$ coins. Write $x = b + t$ with $1 < t < a$ and compare with $\lfloor x / a \rfloor + (x \bmod a)$; greedy loses only when $r + t \ge a$, which forces $r > 0$, and $r < a - q$.

23. On one tape the file that is $k$-th from the end is read in the retrieval of $k$ files, so its length counts $k$ times. Over $m$ tapes each multiplier $k$ is available at most $m$ times, so the best is to use the multiplier 1 for $m$ files, 2 for the next $m$, and so on, and by the rearrangement inequality to give the smallest multipliers to the longest files. Round robin on the decreasing order does exactly this. For the example the multipliers 1, 1, 2, 2, 3, 3, 4 meet the lengths 12, 9, 7, 6, 4, 3, 2, for $21 + 26 + 21 + 8 = 76$.

24. Starting the shortest released job gives $C_a = 10$, $C_b = 11$, total 21. Waiting one unit and running $b$ first gives $2 + 12 = 14$. Preemption gives $C_b = 2$, $C_a = 11$, total 13. For the proof, if at some time a job $j$ runs while a released job $k$ has less remaining work, take the time units that $j$ and $k$ use from then on and give the first ones to $k$: the later of the two completion times does not change and the earlier one does not increase.

25. The forward rule runs $b$, $a$, $c$, and $c$ finishes at 7, so $L_{\max} = 5$; the order $a, c, b$ gives $L_{\max} = 1$. For the backward rule, the last job of any order ends at $P = \sum p_j$. If an optimal order ends with a job $k$ other than the chosen $j$, move $j$ to the end: $j$ has no successors, the jobs after it move earlier, and $j$ ends at $P$ with lateness $P - d_j \le P - d_k$. Induct on the rest.
