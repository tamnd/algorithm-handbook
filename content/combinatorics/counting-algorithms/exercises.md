1. ◦ Compute $\binom{12}{5}$ with the product formula of [computing binomial coefficients](/binomial-coefficient-computation/), and give the value of $r$ after each of the five steps. How many additions does one row of [Pascal's triangle](/pascal-triangle-dp/) use for the same value?

2. ◦ Count the monotone [lattice paths](/counting-lattice-paths/) from $(0, 0)$ to $(5, 3)$ with unit steps east and north: all of them, those that never go above the diagonal $y = x$, and those that avoid the point $(2, 2)$.

3. ◦ How many integers in $\{1, \ldots, 1000\}$ are divisible by none of 2, 3, 5 and 7? Use the [inclusion-exclusion principle](/inclusion-exclusion-principle/).

4. ◦ Count the solutions of $x_1 + x_2 + x_3 + x_4 = 10$ in integers with $0 \le x_i \le 4$, using [stars and bars](/stars-and-bars/) and the alternating sum of [bounded integer solutions](/bounded-integer-solutions-counting/).

5. ◦ In an election, A gets 6 votes and B gets 4. In how many of the $\binom{10}{4}$ orders of counting is A strictly ahead after every vote? Use the [ballot theorem](/ballot-theorem/).

6. ◦ Use the [hook length formula](/hook-length-formula/) to count the standard Young tableaux of shape $(4, 2, 1)$. Give the hook lengths row by row.

7. ◦ How many labelled trees on $\{1, \ldots, 6\}$ have vertex 1 as a leaf? Use [Cayley's formula](/cayley-formula/), and give the fraction of all trees that this is.

8. ◦ Write 1000 and 100 as sums of Fibonacci numbers, no two of them consecutive, as in [Zeckendorf's theorem](/zeckendorf-theorem/).

9. ◦ Eight different books are split into 3 nonempty piles, with no order on the piles or inside a pile. Separately, eight people sit at 3 identical round tables, none of them empty. Extend row 7 of the tables in [Stirling numbers of the second kind](/stirling-numbers-second-kind/) and [Stirling numbers of the first kind](/stirling-numbers-first-kind/) by one step to count both.

10. • Count the triples $(a, b, c) \in \{1, \ldots, 10\}^3$ with $\gcd(a, b, c) = 1$ by [Möbius inversion](/mobius-inversion/), and list the nonzero terms of the sum.

11. • Evaluate the permanent of
$$M = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$$
with [Ryser's formula](/ryser-formula/), listing the column sets whose terms are nonzero. Check the value by listing the perfect matchings of the bipartite graph whose biadjacency matrix is $M$.

12. • Each of the nine cells of a $3 \times 3$ board is coloured black or white. How many colourings are there when two colourings that differ by a rotation of the board count as one? Use [Burnside's lemma](/burnside-lemma/).

13. • Run the analysis of the [Karp-Luby algorithm](/karp-luby-algorithm/) on $F = (x_1 \land x_2) \lor (x_2 \land x_3) \lor (x_1 \land x_3)$ with $n = 3$ variables. Give the weights $w_i$, the total $W$, the number of pairs $(i, a)$ in which $C_i$ is the first clause that $a$ satisfies, the number of satisfying assignments, and the success probability of one trial. How many trials does the algorithm run for $\varepsilon = 0.1$ and $\delta = 0.05$?

14. • Touchard's congruence in [counting set partitions](/counting-set-partitions/) gives $B_{n+3} \equiv B_n + B_{n+1} \pmod 3$. Starting from $B_0, B_1, B_2$, compute $B_n \bmod 3$ for $n \le 15$. Find the period of the sequence and $B_{100} \bmod 3$.

15. • For the coin values 1, 2 and 5 and the amount 7, fill the one-dimensional table of [coin change counting](/coin-change-counting/) twice: with the loop over coins outside and the loop over amounts inside, and with the two loops swapped. What do the two results count?

16. • Find $\binom{100}{51} \bmod 7$ by [Lucas's theorem](/lucas-theorem/). For how many $k$ with $0 \le k \le 100$ is $\binom{100}{k}$ not divisible by 7?

17. • How many triples of integers satisfy $1 \le i \le j \le k \le n$? This is the number of times the body of three nested loops runs when each loop starts at the index of the loop outside it. Give a closed form by the [hockey-stick identity](/hockey-stick-identity/) and the value for $n = 10$.

18. • List the generalized pentagonal numbers up to 21 and use [Euler's pentagonal recurrence](/euler-pentagonal-recurrence/) to compute $p(21)$ from $p(20) = 627$, $p(19) = 490$, $p(16) = 231$, $p(14) = 135$, $p(9) = 30$ and $p(6) = 11$. How many terms does the recurrence add for $p(1000)$?

19. • Order the divisors of 12 by divisibility. Count the down-sets of this partial order and its linear extensions with the dynamic program of [counting linear extensions](/counting-linear-extensions/). Explain why the second number is a count of standard Young tableaux.

20. • How many monotone lattice paths from $(0, 0)$ to $(7, 4)$ never go above the straight line between these two points? Use the [cycle lemma](/cycle-lemma/).

21. • A gets 7 votes and B gets 2. In how many orders of counting does A always have more than twice as many votes as B, after every vote? Use the general form of the [ballot theorem](/ballot-theorem/).

22. ★ How many ways are there to colour exactly 3 cells of a $3 \times 3$ board black, when colourings that differ by a rotation or a reflection of the board count as one? Write the cycle index of the 8 symmetries acting on the cells and use the [Pólya enumeration theorem](/polya-enumeration-theorem/).

23. ★ Count the pairs of monotone lattice paths, one from $(0, 2)$ to $(3, 5)$ and one from $(2, 0)$ to $(5, 3)$, that have no vertex in common. Use the [Lindström-Gessel-Viennot lemma](/lindstrom-gessel-viennot-lemma/), and say why the other pairing of sources and sinks cannot give non-intersecting pairs.

24. ★ The $2 \times 4$ grid graph has vertices $(r, c)$ with $r \in \{0, 1\}$ and $0 \le c \le 3$. Colour $(r, c)$ black when $r + c$ is even, and let $B$ be the $4 \times 4$ biadjacency matrix, black vertices against white ones. Show that $|\det B|$ is not the number of perfect matchings. Then put $-1$ on the entries of the vertical edges in columns 1 and 3, and show that $|\det|$ of the signed matrix is the number of perfect matchings, as in the bipartite form of [Kasteleyn's method](/kasteleyn-method/). Explain why these signs work.

25. ★ Count the permutations of $\{1, \ldots, 8\}$ in which every cycle has length at least 3. Use the [exponential generating function](/exponential-generating-functions/) of the class, then find a recurrence that gives the same numbers.

26. ★ How many [necklaces](/necklace-counting/) of 12 beads, 4 of them black and 8 white, are there up to rotation? Count the colourings fixed by each rotation with this content, and average.
