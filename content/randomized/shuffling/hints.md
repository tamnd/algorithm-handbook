1. The array becomes $[a, b, e, d, c]$, then $[d, b, e, a, c]$, and the last two steps swap a position with itself, so the result is $[d, b, e, a, c]$. The reversal comes from $j = 0, 1, 2, 1$: item $a$ must come to position 4 from position 0, then $b$ to position 3 from position 1, and the rest are already in place.

4. Out-shuffles restore the deck after $\operatorname{ord}_{13}(2) = 12$ shuffles, since $2^6 \equiv -1 \pmod{13}$. In-shuffles restore it after $\operatorname{ord}_{15}(2) = 4$, since $2^4 = 16 \equiv 1$. By Elmsley's rule, $5 = 101_2$ needs an in-shuffle, an out-shuffle and an in-shuffle, in that order.

5. There are $\binom52 = 10$ pairs, each equal with probability $1/125$, so the tie probability is at most $10/125 = 0.08$. Exactly, it is $1 - (125 \cdot 124 \cdot 123 \cdot 122 \cdot 121)/125^5 \approx 0.0778$.

7. There are 9 derangements, so a draw succeeds with probability $9/24$ and the mean number of draws is $8/3$. Sattolo's algorithm gives each of the six 4-cycles probability $1/6$ and the three derangements made of two 2-cycles probability 0: they are derangements but not single cycles.

9. The deck stays in order with probability $(n + 1)/2^n = 6/32 = 3/16$, and one shuffle reaches $2^5 - 5 = 27$ orders. The order $[3, 0, 4, 1, 5, 2, 6]$ has two rising sequences, $0, 1, 2$ and $3, 4, 5, 6$. Two shuffles make a 4-shuffle, so the probability is $\binom{4 + 7 - 2}{7}/4^7 = 36/16384 = 9/4096$.

13. At step $i$ the swap is trivial with probability $1/(i+1)$. Summing $1 - 1/(i+1)$ over $i = 1, \ldots, n-1$ gives $n - H_n$, which is about $47.46$ for $n = 52$.

14. Of the 16 words, 6 give 0 mod 3 and 5 each give 1 and 2. So the item that starts at position 0 ends last with probability $3/8$, and each of the two orders that end with it has probability $3/16$; the other four have $5/32$. The distance is $2(3/16 - 1/6) = 1/24$.

16. Follow the coins from the full state $(2, 2)$. A coin that picks a half with no items left stops the merge. Write $E(\ell, r)$ for the expected number left over from the state with $\ell$ and $r$ items, and solve the small recurrence. The answers are $7/8$ and $3/8$.

19. With $m = n = 52$ moves, the bound is at least $\frac12$ as long as $52^t \le 52!/2$, that is, $t \le (\log_2 52! - 1)/\log_2 52 \approx 39.4$. So at least 40 moves are needed. The true answer is close to 205, so the counting bound is weak here.

22. A move leaves a given position alone with probability $(1 - 1/n)^2$, and the moves are independent. The expected number is $n(1 - 1/n)^{2t}$, about $6.90$ for $n = t = 52$. For the bound, $n(1 - 1/n)^{2t} \ge n e^{-2t/(n-1)} = n e^{-\ln n + 2c}$.

23. Build the permutation by inserting item $i$ into the cycles of the first $i - 1$ items: either after one of them, or as a cycle of its own. Item $i$ starts a new cycle with probability $1/i$, whatever happened before. The six permutations of 3 items have 3, 2, 2, 2, 1 and 1 cycles, which gives variance $17/36$.

24. The minimum of $P^k$ is at the reversal, the only order with $n$ rising sequences, and it equals $\binom{2^k}{n}/2^{kn}$. The answers are $k = 11$, with $s(11) \approx 0.48$, for $n = 52$, and $k = 13$ for $n = 104$. For the estimate, take logarithms: $s(k) \approx 1 - \exp(-n^2/2^{k+1})$.

25. The orders with at most 16 rising sequences form a set $S$ with $P^4(S) = 1$, so $d(4) \ge 1 - \pi(S)$. A uniform permutation has $r$ rising sequences exactly when its inverse has $r - 1$ descents, so $\pi(S)$ is a sum of Eulerian numbers divided by $52!$. It is about $4.7 \times 10^{-7}$, smaller than $2^{-17} \approx 7.6 \times 10^{-6}$.

26. Unranking uses $r \bmod n$ as the choice of the first step and $\lfloor r/n \rfloor$ as the rank of the rest, so it is a mixed-radix reading of $r$. For ranking, undo the swaps from the last to the first. Read off $s = \pi[n-1]$, swap $\pi[n-1]$ with $\pi[\pi^{-1}[n-1]]$, and keep $\pi^{-1}$ updated so each step costs $O(1)$. This is the method of Myrvold and Ruskey.

27. Card $v + 1$ starts a new rising sequence exactly when it lies above card $v$, that is, when $\pi^{-1}$ has a descent at $v$. The inverse of a uniform permutation is uniform. Each descent indicator has mean $\frac12$ and variance $\frac14$. Two adjacent ones are both 1 with probability $\frac16$, so their covariance is $-\frac1{12}$; indicators farther apart are independent.
