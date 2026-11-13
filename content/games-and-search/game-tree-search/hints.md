1. The MIN children are worth 2, 6 and 1, so the value is 6. Alpha-beta reads all of $(5, 9, 2)$ and all of $(7, 8, 6)$; then $\alpha = 6$, the leaf 1 is at most 6, and the leaves 10 and 4 are cut: 7 of 9 leaves. Put the child worth 6 first and, in each other child, a leaf below 6 first, for example $(6, 7, 8)$, $(2, 5, 9)$, $(1, 10, 4)$. Then alpha-beta reads $3 + 1 + 1 = 5 = 3^1 + 3^1 - 1$ leaves.

2. Minimax reads $10^d$ leaves, so it reaches depth 6. With the best move first alpha-beta reads $10^{\lceil d/2 \rceil} + 10^{\lfloor d/2 \rfloor} - 1$ leaves: 199,999 at depth 10 and 1,099,999 at depth 11, so it reaches depth 10. In its worst case it reads all $10^d$ leaves, like minimax, and reaches depth 6.

3. $2 \oplus 9 \oplus 12 = 7 \ne 0$, so the player to move wins. A winning move turns a heap $a$ into $a \oplus 7$ when that is smaller: $2 \oplus 7 = 5$ and $9 \oplus 7 = 14$ are larger, and $12 \oplus 7 = 11$. The only winning move takes one token from the heap of 12.

4. The four values are 2, 0, 0 and 3. The Grundy numbers for $n = 0, \ldots, 13$ are $0, 0, 1, 1, 0, 2, 1, 0, 0, 1, 1, 0, 2, 1$, which repeat with period 7. The player to move loses at 0, 1, 4, 7, 8 and 11.

5. The row minima are $-2$ and $-3$, so the maximin is $-2$; the column maxima are 4 and 1, so the minimax is 1, and there is no saddle point. The row player plays $(2/5, 3/5)$, the column player $(3/10, 7/10)$, and the value is $-1/5$.

6. Move A is worth $\frac13 \cdot 6 + \frac23 \cdot 3 = 4$ and move B is worth $\frac12 \cdot 0 + \frac12 \cdot 9 = 4.5$, so expectiminimax chooses B with value $4.5$.

7. The means are 0.3, 0.72 and 0.65, and the scores are about 1.260, 1.149 and 1.130. The next playout goes through the first child, which has few visits. If the search stopped now, the program would play the second child, which has both the best mean and the most visits.

8. Every unexpanded node has $(\mathrm{pn}, \mathrm{dn}) = (1, 1)$. An AND node adds the proof numbers and takes the least disproof number, so $a = (2, 1)$, $b = (3, 1)$, $c = (4, 1)$. The OR root takes the least proof number and adds the disproof numbers: $(2, 3)$. The most-proving node is reached through $a$, the child with the least proof number, and then through the child of $a$ with the least disproof number; with a tie, the leftmost. After the expansion that child is $(0, \infty)$, so $a = (1, 1)$ and the root is $(1, 3)$.

9. $f$ has no move and is lost. $d$ and $e$ move to $f$ and are won. $b$ can only move to $d$ and is lost, so $a$, which moves to $b$, is won. $g$ and $h$ only move to each other, so they are draws. $c$ has no move to a lost position, and its move to $g$ avoids losing, so $c$ is a draw. Wins: $a$, $d$, $e$. Losses: $b$, $f$. Draws: $c$, $g$, $h$.

11. The first MIN child reads both its leaves and is worth $m = \min(x_1, x_2)$. The second child reads $x_3$ and stops if $x_3 < m$, which happens when $x_3$ is the smallest of the three, with probability $1/3$. Otherwise it reads $x_4$. The expected count is $2 + 1 + 2/3 = 11/3$.

12. The parts have Grundy numbers 1, 1 and 3, so the sum is worth $1 \oplus 1 \oplus 3 = 3$ and the player to move wins. A winning move must make the XOR 0, so it gives a part the Grundy number $g \oplus 3$. Check each part's options.

15. Trace the plays: after $s \to a$ and $s \to c$ the rest of the play is forced. After $s \to e$ the opponent has two choices; check both.

19. Regret matching plays in proportion to the positive regrets. To update, add to each action's regret its payoff against paper minus the payoff of the current strategy against paper. The next strategy is $(18/31, 0, 13/31)$.

22. If every maximum matching covers $s$, take one, $M$, and always move to the partner of the current vertex in $M$. If the opponent could ever move to a vertex outside the matched path, swapping the edges along the path would give a maximum matching missing $s$. For the converse, take a maximum matching $M$ missing $s$ and play the same strategy as the second player. With the pendant $e$, the only maximum matching is $\{sa, cd, be\}$.

24. Follow the node types of the Knuth-Moore proof. With the best child first, every null-window test of a later child at a PV node fails low, so no re-search happens, and PVS visits the same nodes as alpha-beta with perfect ordering.
