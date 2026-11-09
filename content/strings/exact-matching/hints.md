1. $\pi = 0, 0, 1, 0, 1, 2, 3$. The longest proper border has length 3, so the smallest period is $7 - 3 = 4$. The borders are $\texttt{aba}$ and $\texttt{a}$: follow the chain $\pi[6] = 3$, $\pi[2] = 1$, $\pi[0] = 0$.

2. $Z[1..6] = 1, 0, 0, 3, 1, 0$.

3. Each of the 7 windows matches three characters and fails on the fourth, so 28 comparisons. In general $(n - m + 1)m$.

4. The window hashes are 9, 3, 8, 4, 4, 4, 4, 10, 9 and the pattern hash is $26 \bmod 11 = 4$. They agree at shifts 3, 4, 5 and 6; the windows 15, 59 and 92 are spurious hits, and 26 at shift 6 is the only occurrence.

5. The shifts are 1 for $\texttt{a}$, 3 for $\texttt{b}$, 2 for $\texttt{c}$ and 5 for any other character. The windows tested start at 0, 1, 4, 7 and 10, and the occurrences are at 4 and 10.

6. From state 0: $\texttt{a} \to 1$, $\texttt{b} \to 0$. From 1: $\texttt{a} \to 1$, $\texttt{b} \to 2$. From 2: $\texttt{a} \to 3$, $\texttt{b} \to 0$. From 3: $\texttt{a} \to 1$, $\texttt{b} \to 2$.

7. $\pi = 0, 0, 1, 2$ and $\mathrm{nxt} = -1, 0, -1, 0, 2$. The Morris-Pratt fall-backs are $-1, 0, 0, 1, 2$, so the tables differ at $q = 2$ and $q = 3$, where the character after the border equals $P[q]$ and the fall-back would only repeat a failed comparison.

8. Shifts 0, 3, 4, 5 and 6 (the windows $\texttt{cab}$, $\texttt{bca}$, $\texttt{cab}$, $\texttt{abc}$, $\texttt{bca}$).

9. Shifts 0 and 3: the windows $(5, 9, 7)$ and $(2, 4, 3)$ rise and then fall to a value between the two.

10. $0, 0, 2, 0, 3$. The pattern encodes as $0, 0, 1, 3$, and so do the windows $\texttt{abba}$ at shift 0 and $\texttt{acca}$ at shift 3; no other window does.

11. Twice. The character is compared with $P[m-1] = \texttt{b}$, then with $P[m-2] = \texttt{a}$ via $\mathrm{nxt}[m-1] = m - 2$. Every border of $a^{q}$ is followed by $\texttt{a} = P[q]$ for $q < m - 1$, so $\mathrm{nxt}[m-2] = -1$ and the search moves on.

12. At most $n$. Each window compares $m$ characters and fails on $\texttt{b}$; the good-suffix shift is $m$, because the matched suffix $a^{m-1}$ occurs nowhere else in $P$ and no prefix of $P$ begins with $\texttt{a}$. The bad-character rule gives nothing here: the last $\texttt{a}$ of $P$ lies to the right of the mismatch.

13. The shifts are 2 for $\texttt{a}$, 1 for $\texttt{b}$, 3 for $\texttt{c}$ and 6 for any other character. The windows start at 0, 1, 4 and 10. A character that does not occur in $P$ cannot lie inside any occurrence, so the next window can start just after it.

14. For each $k \ge 1$ in increasing order, and $i$ from $Z[k] - 1$ down to 0, set $\pi[k + i] = i + 1$ if it is not set yet, and stop the inner loop at the first entry already set. Unset entries get 0. Each entry is set once.

16. For $0 \le j < m - d$, $P[j] = T[s + d + j] = P[d + j]$. So the gap between two consecutive occurrences is a period of $P$ when it is less than $m$, and at least $m \ge p$ otherwise.

17. Clear bit $j$ of the mask of every character in the set at position $j$. The search does not change at all.

18. The $j$-th comparison of a window happens only if the first $j - 1$ succeeded, which has probability $\sigma^{-(j-1)}$. Sum the geometric series.

19. Run the Knuth-Morris-Pratt search over $T$ and return the final number of matched characters $q$, taking $q = m$ if the last window is an occurrence.

20. Without the rule, every window is an occurrence, each costs $m$ comparisons and the shift is the period 1: $(n - m + 1)m$ comparisons. With it, $m$ for the first window and one for each later one: $n$ in all.

21. The local periods are 2, 3, 1, 3 and the period is 3, so the critical cuts are 2 and 4.

23. Both $d$ and $p$ are periods of $P$ and $d + p \le m$, so by the [Fine and Wilf theorem](/fine-and-wilf-theorem/) $\gcd(d, p)$ is a period too. Since $p$ is the smallest period, $\gcd(d, p) = p$.

24. Use an adversary that answers $\texttt{a}$ to every read. If the algorithm stops with some position $i$, $1 \le i \le n - 1$, unread, the text $a^n$ and the text with $T[i] = \texttt{b}$ (and $T[i-1] = \texttt{a}$) agree with every answer, but only the second contains $\texttt{ab}$.

25. Map a backward transition $\delta(q, c) = k$ to $q - k + 1$, a number from 1 to $m$. If two transitions from $q < q'$ had the same image $d$, the second would give $P[q - d] = P[q]$ and the first $P[q - d] = c \neq P[q]$.

26. Each term is at least 0 and is 0 exactly when one symbol is a wildcard or the two are equal. Expand the sum into $\sum p_j^3 t_{i+j} - 2\sum p_j^2 t_{i+j}^2 + \sum p_j t_{i+j}^3$: three correlations, each computed by FFT on blocks of the text of length $2m$ that overlap by $m$.

27. If $P$ has at least three runs, its inner runs must match runs of $T$ exactly: search for them in the sequence of pairs of $T$ with Knuth-Morris-Pratt, and at each hit check that the run before has the first character of $P$ and is long enough, and the same for the run after. Patterns of one or two runs are checked run by run.
