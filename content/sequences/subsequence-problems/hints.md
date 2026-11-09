1. AGRIM matches at positions 1, 3, 5, 6, 9 and GOTH at 3, 4, 7, 8. HIT fails because no I follows the H at position 8, and LIAR fails because no A follows the I at position 6. RITH matches at 5 to 8 and is the only substring.

2. The length is 4. The last row of the table is $0, 1, 2, 3, 3, 3, 4$, and the traceback returns ABAD. It is the only longest common subsequence of these two strings.

3. The tails go $[2]$, $[2, 9]$, $[2, 5]$, $[2, 3]$, $[2, 3, 7]$, $[2, 3, 7, 11]$, $[2, 3, 7, 8]$, $[2, 3, 7, 8, 10]$, $[2, 3, 4, 8, 10]$. The length is 5, reached by $2, 3, 7, 8, 10$ and $2, 5, 7, 8, 10$. The last item 4 replaced 7 without changing the length; the tail array mixes items from different subsequences.

5. For abab the values are $1, 2, 4, 7, 12$, and for abcab they are $1, 2, 4, 8, 15, 28$.

7. $L = 5$ with suday, the edit script has $6 + 8 - 10 = 4$ steps, and the shortest common supersequence has length $6 + 8 - 5 = 9$. The edit distance is 3: insert a, insert t, and change n to r.

8. With $n = m = 4$, 17 numbers force a monotone subsequence of length 5. The sequence $4, 3, 2, 1, 8, 7, 6, 5, 12, 11, 10, 9, 16, 15, 14, 13$ has four decreasing blocks; an increasing subsequence takes at most one item from each block.

10. Take $X = \text{AB}$, $Y = \text{BA}$, $Z = \text{A}$. The first step may return B, which has nothing in common with $Z$, yet A is common to all three. The three-string table has $c[i,j,k] = c[i-1,j-1,k-1] + 1$ when the three letters agree, and otherwise the largest of the three cells with one index lowered.

13. Without the rule, $(1, 1)$ and $(1, 2)$ form an increasing run of heights and count as nested. With it, equal widths can never both be chosen. The answer for the example is 3: $(2, 3), (5, 4), (6, 7)$.

16. $W_i = \max(W_{i-1},\; w_i + W_{i-2},\; w_i + w_{i-1} + W_{i-3})$. The values are $0, 3, 5, 8, 18, 22$, so the best sum is 22, from positions 1, 2, 4, 5.

19. By the arithmetic-geometric mean inequality, $L_\uparrow + L_\downarrow \ge 2\sqrt{L_\uparrow L_\downarrow} \ge 2\sqrt{n}$. Reversing a random permutation gives a random permutation and swaps the two lengths, so they have the same expectation.

22. The expected number of increasing subsequences of length $k$ is $\binom{n}{k}/k! \le n^k/(k!)^2 \le (e\sqrt{n}/k)^{2k}$. With $k = (1+\delta)e\sqrt{n}$ this is exponentially small, so $\Pr[L_n \ge k]$ is too, and $E[L_n] \le k + n \Pr[L_n \ge k]$.

23. Let $E_a$ and $E_b$ be the numbers of distinct subsequences that end in $a$ and in $b$. Appending $a$ sets $E_a \leftarrow E_a + E_b + 1$ and leaves $E_b$ alone. The total is largest when each step replaces the smaller of the two, which is what alternation does, and then the pair moves along the Fibonacci numbers.

24. Any string of length $k$ embeds by putting its $i$-th letter in block $i$. For the other direction, take the last letter of each block, which occurs in that block only at its end, and then a letter missing from the remainder after the last block. Show by induction that the greedy embedding of the first $i$ letters cannot end before the end of block $i$.

25. Keep $f[j]$, the length of the longest common increasing subsequence that ends with $y_j$. For each $x_i$, scan $j$ from left to right with a running best over the cells with $y_j < x_i$, and when $y_j = x_i$ set $f[j] \leftarrow \max(f[j], \text{best} + 1)$. The answer for the example is 4, for instance $1, 4, 5, 9$ or $1, 4, 5, 6$.

26. In such a permutation the items that are not left-to-right minima must appear in decreasing order, so the permutation is fixed by the values and positions of its left-to-right minima. Turn that data into a path of up and down steps that never goes below zero. The counts are 5 for $n = 3$ and 14 for $n = 4$.
