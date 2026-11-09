1. The ceilings are $n - k + i = 5, 6, 7, 8$. In $\{2, 5, 7, 8\}$ the last two entries sit at their ceilings, so $a_2 = 5$ grows to 6 and the result is $\{2, 6, 7, 8\}$. In $\{1, 6, 7, 8\}$ only $a_1$ can grow, and the result is $\{2, 3, 4, 5\}$.

2. $\binom{6}{3} + \binom{3}{2} + \binom{1}{1} = 20 + 3 + 1 = 24$. The integer is $2 + 8 + 64 = 74$, and it is the 25th integer with three one bits, since increasing order of integers of fixed weight is colex order.

3. Take the largest $c$ with $\binom{c}{3} \le 1000$: $\binom{19}{3} = 969$ and $\binom{20}{3} = 1140$. The rest is 31, so $c_2 = 8$ with $\binom{8}{2} = 28$, and then $c_1 = 3$. So $1000 = \binom{19}{3} + \binom{8}{2} + \binom{3}{1}$.

4. $\binom{4 + 5 - 1}{5} = \binom{8}{5} = 56$. The multiset becomes $\{1, 2, 5, 7, 8\}$.

8. Count the subsets that come after $A$: for each $i$, those that agree with $A$ before position $i$ and have a larger entry at position $i$. There are $\binom{n - a_i}{k - i + 1}$ of them, so the rank is $\binom{10}{4} - 1 - \bigl[\binom{8}{4} + \binom{5}{3} + \binom{4}{2} + \binom{1}{1}\bigr] = 209 - 87 = 122$. The subset of rank 100 is $\{2, 3, 7, 9\}$.

9. For two sets of the same size, $A$ is lexicographically smaller exactly when the smallest element of $A \mathbin{\triangle} B$ lies in $A$, and colex smaller exactly when the largest element lies in $B$. The map $a \mapsto n - a$ reverses the order of elements, so it swaps the two tests. Hence the lexicographic rank of $A$ is $\binom{n}{k} - 1$ minus the colex rank of $A'$.

10. Write $m$ in the combinatorial number system and lower the bottom index of each binomial by one. From $7 = \binom{4}{3} + \binom{3}{2}$ the shadow is $\binom{4}{2} + \binom{3}{1} = 9$, and from $5 = \binom{4}{3} + \binom{2}{2}$ it is $\binom{4}{2} + \binom{2}{1} = 8$. The first seven colex sets are the four 3-subsets of $\{0, 1, 2, 3\}$ and $\{0, 1, 4\}$, $\{0, 2, 4\}$, $\{1, 2, 4\}$.

12. The ranks are 15 and 17. With $c_3 > c_2 > c_1$, the formula gives $\binom{c_3 + 1}{3} - \binom{c_2 + 1}{2} + \binom{c_1 + 1}{1} - 1$, which is $20 - 6 + 2 - 1$ for $\{1, 3, 5\}$ and $20 - 3 + 1 - 1$ for $\{0, 2, 5\}$.

16. The reflected Gray code on $n$ bits is the code on $n - 1$ bits with top bit 0, then the same code reversed with top bit 1. Keep only the strings of weight $k$. By induction the first subset is $\{0, \ldots, k-1\}$, and the last is the first subset of $R(n-1, k-1)$ with $n - 1$ added, that is, $\{0, \ldots, k-2, n-1\}$. The last and first differ by the exchange of $k - 1$ and $n - 1$.

17. Color a pair by the parity of its sum. Each allowed step changes the sum by one, so a list alternates colors, and the two color classes can differ in size by at most one. There are $\lfloor n/2 \rfloor$ more pairs with odd sum than with even sum: 4 against 2 for $n = 4$, 6 against 4 for $n = 5$. So the answer is no for every $n \ge 4$. For $n = 3$ the list $\{1, 2\}, \{1, 3\}, \{2, 3\}$ works.

18. The answers are 19 and 69. The rotated prefix is $1^a 0^m 1 x$ with $a \ge 0$ and $m \ge 1$, and the step changes four bits only when $a \ge 1$ and $x = 0$. Count the strings $1^a 0^m 1 0 w$ with $k - a - 1$ ones in $w$, sum over $m$ with the hockey stick identity to get $\binom{n-a-2}{k-a}$, and then sum over $1 \le a \le k - 1$ by parallel summation.
