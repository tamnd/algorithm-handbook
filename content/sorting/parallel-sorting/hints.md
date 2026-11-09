1. After the rounds: $\langle 1, 5, 2, 4, 3 \rangle$, $\langle 1, 2, 5, 3, 4 \rangle$, $\langle 1, 2, 3, 5, 4 \rangle$, $\langle 1, 2, 3, 4, 5 \rangle$, and the fifth round changes nothing. The keys are sorted after round 4. The rounds make $2 + 2 + 2 + 2 + 2 = 10$ compare-exchanges.

2. $A$ goes to positions $1, 2, 5$ and $B$ to $0, 3, 4, 6$. If both lists count only smaller keys, the two $5$s both go to position $2$ and position $3$ stays empty. One list must count equal keys and the other not.

3. The parallelism is $20 \cdot 2^{20} / 8000 \approx 2621$. Brent's theorem gives at most $20 \cdot 2^{20}/1024 + 8000 = 20480 + 8000 = 28480$ steps, and the work term is the larger one.

4. Row phase 1 gives rows $\langle 3, 6, 11, 16 \rangle$, $\langle 14, 9, 8, 1 \rangle$, $\langle 2, 5, 12, 15 \rangle$, $\langle 13, 10, 7, 4 \rangle$; the column phase gives $\langle 2, 5, 7, 1 \rangle$, $\langle 3, 6, 8, 4 \rangle$, $\langle 13, 9, 11, 15 \rangle$, $\langle 14, 10, 12, 16 \rangle$. Row phase 2 gives $\langle 1, 2, 5, 7 \rangle$, $\langle 8, 6, 4, 3 \rangle$, $\langle 9, 11, 13, 15 \rangle$, $\langle 16, 14, 12, 10 \rangle$; the column phase gives $\langle 1, 2, 4, 3 \rangle$, $\langle 8, 6, 5, 7 \rangle$, $\langle 9, 11, 12, 10 \rangle$, $\langle 16, 14, 13, 15 \rangle$. The last row phase gives the snake $\langle 1, 2, 3, 4 \rangle$, $\langle 8, 7, 6, 5 \rangle$, $\langle 9, 10, 11, 12 \rangle$, $\langle 16, 15, 14, 13 \rangle$. Five phases of $4$ steps make $20$ steps, against the bound $2 \cdot 4 - 2 = 6$.

5. The sorted sample is $5, 12, 29, 41, 52, 63, 70, 88$, so the splitters are $12, 41, 63$. The buckets are $\{5, 9, 12\}$, $\{17, 23, 29, 36, 41\}$, $\{47, 52, 58, 63\}$ and $\{70, 81, 88, 94\}$, all within $2n/p = 8$.

6. Processor 0 counts one key of each digit; processor 1 counts digit $1$ twice and digits $2$ and $3$ once. Taken digit by digit and, within a digit, processor by processor, the starting slots are $0, 1$ for digit $0$, then $1, 2$, then $4, 5$, then $6, 7$. Processor 1's key $2$ goes to slot $5$.

7. Diagonal $3$ has co-rank $(1, 2)$ and diagonal $6$ has co-rank $(2, 4)$. The processors merge $\langle 2 \rangle$ with $\langle 1, 3 \rangle$, $\langle 5 \rangle$ with $\langle 4, 6 \rangle$, and $\langle 7, 8 \rangle$ with $\langle 9, 10 \rangle$.

8. The first pivot is $1$, so after the first round the lists are $\{0, 1\}$, $\{\}$, $\{2, 3, 8, 9, 10, 11\}$ and $\{4, \ldots, 7, 12, \ldots, 15\}$. The second round has pivots $0$ and $8$, and the loads end as $1, 1, 7, 7$. Sorted input is a bad case for this pivot rule.

9. The fan-in bound is $\lg 16 = 4$. A layer of $8$ comparators has at most $2^8$ outcomes, so a network needs $\lceil 45/8 \rceil = 6$ layers. With $16$ comparisons per round, the comparison model needs $\lceil 45/16 \rceil = 3$ rounds. Bitonic sort's depth of $10$ is above all three.

10. Follow the key $1$. In round 1 it is at position $n - 1$ and is compared with $0$; in round 2 position $n - 1$ is not compared. It must then move $n - 2$ places to position $1$, one per round.

16. Each bucket holds exactly $ps$ samples. In one sorted block, a stretch with $c$ samples has at most $(c + 1) w - 1$ keys, where $w = n/(p^2 s)$.

22. A bucket with more than $t$ keys means that $t$ keys in a row of the sorted order hold no sample. Each such run has probability at most $(1 - t/n)^p \le e^{-tp/n}$, and there are fewer than $n$ runs.

23. For size: on the reversed input, each comparator removes at most one inversion. For depth: on the reversed input, in a network of depth $n - 1$ the largest key must move at every layer, so layer 1 has the comparator $(0, 1)$, which sends the second largest key to wire $0$. That key must then move at every later layer as well. In layer 2 both keys need wire $1$.

24. With $c$ candidates left, split them into groups of about $2n/c$ and compare all pairs inside each group, using about $n$ comparisons. The winners number about $c^2 / (2n)$, so the count goes $n, n/2, n/8, n/128, \ldots$.

25. Before column phase $k$ at most $r / 2^{k-1}$ rows are dirty, and the dirty rows lie between the clean rows of zeros and the clean rows of ones. The column phases then take $r + r/2 + \cdots + 2 = 2r - 2$ steps, and the $\tfrac12 \lg n + 1$ row phases take $r$ steps each. For $r = 4$ this gives $18$ steps.

26. Search over inputs of zeros and ones, given by the number of zeros in each column after the first column sort. For $s = 3$, $r = 6$ fails when each column has one zero, and $r = 9$ is the smallest that works. For $s = 4$ the smallest is $r = 20$. Both are the smallest multiples of $s$ with $r \ge 2(s - 1)^2$.
