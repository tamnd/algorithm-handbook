1. The margins are $c$ over $b$ by 11, $c$ over $d$ by 7, $d$ over $b$ by 3, $d$ over $a$ by 3, $a$ over $c$ by 1 and $a$ over $b$ by 1. Every candidate loses at least once ($a$ to $d$, $c$ to $a$, $d$ to $c$, $b$ to all three), so there is no Condorcet winner. The cycle $a \succ c \succ d \succ a$ beats $b$, so the Smith set is $\{a, c, d\}$.

2. Plurality: $c$ has 5 first places, $a$ has 4 and $d$ has 2, so $c$ wins. Borda: $c$ 36, $a$ 27, $d$ 27, $b$ 20, so $c$ wins. Instant runoff: $b$ has no first places and goes out first; then $d$ goes out, and its 2 votes pass to $a$, which beats $c$ by 6 to 5.

5. The quotas are $4.7$, $1.6$, $1.58$, $1.2$, $0.61$ and $0.31$. D'Hondt gives $(5, 2, 2, 1, 0, 0)$: the tenth largest quotient is 790 and the next is about $783.3$. Sainte-Lague gives $(4, 2, 2, 1, 1, 0)$: the tenth quotient is about $526.7$ and the next about $522.2$. Hamilton gives the lower quotas $(4, 1, 1, 1, 0, 0)$ and then the three largest remainders, $0.7$, $0.61$ and $0.6$, which gives $(5, 2, 1, 1, 1, 0)$.

6. With 8 seats the quotas are $3.2$, $3.2$, $1.2$ and $0.4$, and the result is $(3, 3, 1, 1)$. With 9 seats they are $3.6$, $3.6$, $1.35$ and $0.45$, and the result is $(4, 4, 1, 0)$. The smallest state loses its seat when the house grows: this is the Alabama paradox.

7. For $n = 3$ the probability is $p^3 + 3p^2(1 - p) = 20/27 \approx 0.741$. For $n = 5$ it is $p^5 + 5p^4(1 - p) + 10p^3(1 - p)^2 = 64/81 \approx 0.790$.

8. The approval counts are $a$ 7, $b$ 6, $c$ 5, $d$ 4, $e$ 3 and $f$ 1, so $\{a, b, c\}$ has the most approvals, 18. It fails justified representation: $n/k = 4$, and the four voters who approve $d$ approve no member of the committee.

9. (a) It fails neutrality only: swapping the names of the candidates changes the outcome. (b) It fails anonymity, since voter 1 is treated differently. It also fails positive responsiveness: when the other voters tie, a change by voter 1 leaves the tie in place.

13. The Kemeny ranking is $c \succ d \succ a \succ b$, and it is unique. It reverses only one majority, $a$ over $c$, which has the smallest margin. Its total distance to the ballots is 21. Every candidate beats $b$, so a Slater ranking puts $b$ last and breaks the cycle $a \succ c \succ d \succ a$ at one edge. The three Slater rankings are $a c d b$, $c d a b$ and $d a c b$, each with one reversal, and the Kemeny ranking is the second.

15. The sincere scores are $a$ 9, $b$ 10, $c$ 7 and $d$ 4, so $b$ wins. If one of the first voters reports $a \succ c \succ d \succ b$, the scores become $a$ 9, $b$ 8, $c$ 8 and $d$ 5, and $a$ wins alone. The strategy is burying: the voter puts the main rival of its favourite last. Borda is onto and not a dictatorship, and there are more than two candidates, so the Gibbard-Satterthwaite theorem says that some profile must admit such a manipulation.

16. Huntington-Hill gives $(4, 2, 1, 1, 1, 1)$. The divisor for a party's first seat is $\sqrt{0 \cdot 1} = 0$, so each of the six parties gets one seat before any party gets a second. Compared with Sainte-Lague, party 3 (1580 votes) loses a seat and party 6 (310 votes) gains one.

19. The axis $x \lhd w \lhd z \lhd u \lhd v$ works, and it is the only one up to reversal. The peaks are $x$, $w$, $z$, $v$ and $u$, at positions 1, 2, 3, 5 and 4, so the median peak is $z$, and $z$ is the Condorcet winner. The new ballot ranks $w$ and then $u$ first. On this axis $\{w, u\}$ is not an interval, since $z$ lies between them, and no other axis fits the first five ballots.

20. In round 1 the times are $a$ $1/7$, $b$ $1/6$, $c$ $1/5$, $d$ $1/4$, $e$ $1/3$ and $f$ $1$, so $a$ is elected. In round 2 the times are $b$ $13/42$, $c$ $12/35$, $d$ $1/4$, $e$ $1/3$ and $f$ $1$, so $d$ is elected. In round 3 they are $b$ $13/42$, $c$ $12/35$, $e$ $7/12$ and $f$ $1$, so $b$ is elected. The committee $\{a, b, d\}$ satisfies justified representation.

22. A group that JR protects has at least $n/k$ voters, a common approved candidate, and no member of $W$ in any of its ballots. Mark the voters whose ballots miss $W$, then count, for each candidate, how many marked voters approve it. JR fails exactly when some count reaches $n/k$. Both passes read each ballot once.

23. Let $c$ be the Condorcet winner, and take a ranking in which some $y$ sits directly above $c$. Swapping the two changes only the pair $\{c, y\}$, and a majority prefers $c$ to $y$, so the swap strictly lowers the total distance. A ranking that does not put $c$ first is therefore not optimal.

24. A voter gives $x$ one point plus one for each candidate it ranks below $x$; summing over voters gives the formula. The sum of $\sum_{y \ne x} N(x, y)$ over all $x$ is $n \binom{m}{2}$, so the average is $(m - 1)n/2$. A Condorcet loser has $N(x, y) < n/2$ for every $y$, so its score is below the average, and some candidate scores more.

25. With no ties there is a divisor $\lambda$ with $a_i = \lfloor p_i / \lambda \rfloor$ and $\sum a_i = h$. If $\lambda > P/h$, then $\sum a_i \le \sum p_i/\lambda < h$, which is a contradiction. So $\lambda \le P/h$, and $a_i \ge \lfloor h p_i / P \rfloor$.

26. Fix the other reports. A voter whose peak lies below the outcome can move the median only by reporting a peak on the other side of it, and that moves the outcome up, further from its peak. A voter above the outcome is in the mirror position. Single-peakedness turns "further away on the same side" into "worse".

27. For three candidates with $b$ between $a$ and $c$ on the axis, no single-peaked voter ranks $b$ last among them. With an odd number of voters the majority relation is strict and complete. In a cycle, any two of its three majorities share a voter, and one of those pairs forces that voter to rank $b$ last.
