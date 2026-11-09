1. The distance is 3. The last row of the table, for $\texttt{cocoa}$ against the prefixes of $\texttt{cacao}$, is $5, 4, 3, 3, 2, 3$. One optimal alignment keeps both $\texttt{c}$s and substitutes the other three characters.

2. $\texttt{recieve}$ and $\texttt{receive}$: Levenshtein 2, Damerau-Levenshtein 1, since $\texttt{ie}$ and $\texttt{ei}$ are one transposition. $\texttt{word}$ and $\texttt{drow}$: Levenshtein 4, Damerau-Levenshtein 3, for example by the transposition $\texttt{word} \to \texttt{wrod}$ and two substitutions.

3. T652, H160, L142, K530, S530. In Schmidt, the C has the same digit as the S before it, the H is skipped, and the T has the same digit as the D.

4. The distances are $1, 1, 2, 2, 0, 3$ at positions 0 to 5. With $k = 1$ the answer is positions 0, 1 and 4.

5. At positions 3, 5, 6 and 7, each with one error: for example $\texttt{bc}$ ends at 3, $\texttt{ab}$ at 5, $\texttt{abb}$ at 6 and $\texttt{bbc}$ at 7.

6. Three pieces of length 4: $\texttt{algo}$, $\texttt{rith}$, $\texttt{mics}$. The two errors fall in the first and the third piece, so $\texttt{rith}$ occurs exactly and leads to the occurrence.

7. With $k = 3$ the field has 3 bits and the pattern needs 60 bits: one word. With $k = 4$ the field has 4 bits and the pattern needs 80 bits: two words.

8. It accepts $\texttt{ward}$, $\texttt{wrd}$, $\texttt{words}$ and $\texttt{sword}$, each at distance 1. It rejects $\texttt{wodr}$, at distance 2, and $\texttt{drow}$, at distance 4.

10. With these costs a substitution is never cheaper than a deletion and an insertion, so an optimal script uses no substitutions. The characters left untouched form a common subsequence, and every other character of either string costs 1. For $\texttt{garden}$ and $\texttt{danger}$ the LCS has length 2, for example $\texttt{an}$, so the distance is $12 - 4 = 8$.

11. The distances are 1 for $\texttt{ba}$ and $\texttt{ab}$ and 1 for $\texttt{ab}$ and $\texttt{acb}$, but 3 for $\texttt{ba}$ and $\texttt{acb}$, since after the transposition the inserted $\texttt{c}$ would edit the transposed pair. The true Damerau-Levenshtein distance is 2.

12. For 0 or 1 symbols, $p \ne t$ exactly when $p + t - 2pt = 1$. Sum over the window: the pattern sum is a constant, the window sum of the text comes from prefix sums, and $\sum_j p_j t_{i+j}$ is one convolution of the reversed pattern with the text.

14. Deletions give $n$ different strings, substitutions $n(\sigma - 1)$, and insertions $(n + 1)\sigma - n$, because inserting $w_i$ just before or just after $w_i$ gives the same string. The three kinds have different lengths, so they do not overlap. For $\texttt{word}$ this is $9 \cdot 26 - 4 = 230$. In $\texttt{aab}$ the deletion of either $\texttt{a}$ gives $\texttt{ab}$, and the count is 10, not 11.

15. Nine rows are reachable: $(0,1,2)$, $(1,0,1)$, $(1,1,1)$, $(1,1,2)$, $(2,1,0)$, $(2,1,1)$, $(2,1,2)$, $(2,2,1)$ and the dead row $(2,2,2)$. The five rows whose last entry is at most 1 accept.

16. For the lower bound, take an optimal script for the prefixes of lengths $i$ and $j$ and look at what happens to the last characters; in each case removing them costs at least as much as it saves. The upper bound is the substitution or match step. So along a diagonal the values increase by 0 or 1 at each step, and the diagonal is described by the rows where it first exceeds $0, 1, \ldots, k$.

17. For $i > \ell_j + 1$ the bound of exercise 16 gives $D[i][j+1] \ge D[i-1][j] > k$.

18. For each $e$, the furthest point on diagonal $d$ is the maximum of the three candidates from $e - 1$, followed by a slide along equal characters. The diagonals with $|d| \le e$ suffice, and the slide on each diagonal only moves forward, so the total is $O((m + n)d)$. Stop when the point $(m, n)$ is reached. With constant-time LCE queries each slide is one step, and the time is $O(m + n + d^2)$.

19. Call a symbol frequent if it occurs more than $f$ times in the pattern. There are at most $m/f$ frequent symbols, each handled by one convolution in $O(n \log m)$ time. For each text position with a rare symbol, add one match to each of the at most $f$ alignments where that symbol meets itself, in $O(nf)$ time. With $f = \sqrt{m \log m}$ both terms are $O(n\sqrt{m \log m})$.

20. The proof is the same as in exercise 16, in the vertical direction. The first entry of each column is 0, so a column is fixed by its $m$ differences, each $-1$, $0$ or $+1$, and capping at $k + 1$ keeps the differences in this range. Each capped column with one text symbol determines the next, which is a transition of the automaton.

21. Map each symbol of the first string to its position. The second string becomes a sequence of positions, and a common subsequence is an increasing subsequence of it. A longest increasing subsequence takes $O(n \log n)$ time with patience sorting, and the distance is $2n - 2\,\mathrm{LCS}$.
