1. The sorted suffixes are $\texttt{a}$, $\texttt{apaya}$, $\texttt{aya}$, $\texttt{papaya}$, $\texttt{paya}$, $\texttt{ya}$, so $SA = [5, 1, 3, 0, 2, 4]$ and $LCP = [0, 1, 1, 0, 2, 0]$.

2. There are $21$ substring occurrences and $\sum LCP = 4$, so $17$ distinct substrings. The maximum of the LCP array is 2, between $\texttt{papaya}$ and $\texttt{paya}$, so the longest repeated substring is $\texttt{pa}$.

3. The trie has one node for each of the 12 distinct substrings plus the root: 13 nodes. The tree of $\texttt{cocoa\$}$ has 6 leaves and 3 internal nodes, the root, $\texttt{co}$ and $\texttt{o}$: 9 nodes.

5. The circular suffix array is $[2, 3, 0, 1]$ and the suffix array is $[3, 2, 0, 1]$. The suffix $\texttt{a}$ is a prefix of $\texttt{aa}$ and sorts first, but its rotation $\texttt{aaba}$ sorts after the rotation $\texttt{aaab}$ of position 2. The transform is $\texttt{baaa}$.

7. Positions 0 and 2 have ranks 3 and 4, and $LCP[4] = 2$. Positions 1 and 5 have ranks 1 and 0, and $LCP[1] = 1$. The answers are 2 and 1.

9. $[3, 2, 1, 0]$: $\texttt{coa}$, $\texttt{oa}$ and $\texttt{a}$ occur in $\texttt{cocoa}$, and $\texttt{t}$ does not.

10. With $C(\texttt{\$}) = 0$, $C(\texttt{a}) = 1$, $C(\texttt{p}) = 4$, $C(\texttt{y}) = 6$, the range for $\texttt{a}$ is rows 1 to 3. For $\texttt{pa}$, the next range is rows 4 to 5: two occurrences. For $\texttt{aya}$, the step with $\texttt{y}$ gives row 6, and the step with $\texttt{a}$ gives row 3: one occurrence.

12. A substring occurs at least $k$ times exactly when it is a common prefix of $k$ suffixes adjacent in sorted order. Take the maximum, over all windows of $k - 1$ consecutive LCP values, of the window minimum; a sliding-window minimum with a deque does this in $O(n)$. The answers are $\texttt{a}$ and $\texttt{mur}$.

14. Walk the automaton breadth first from the start state. The first state found that lacks a transition on some symbol $c$ gives an absent word: the shortest path label to it followed by $c$. For $\texttt{aabbab}$ all four strings of length 2 occur, and the shortest absent words are $\texttt{aaa}$, $\texttt{aba}$, $\texttt{baa}$ and $\texttt{bbb}$.

15. The new substrings are the suffixes of the new prefix that did not occur before, and these are exactly the ones longer than $\mathrm{len}(\mathrm{link}(\mathit{last}))$. For $\texttt{cocoa}$ the increments are $1, 2, 2, 2, 5$, with sum 12.

19. $SA = [6, 5, 1, 3, 0, 2, 4]$ and $\Psi = [4, 0, 5, 6, 2, 3, 1]$. On the rows starting with $\texttt{a}$ it reads $0, 5, 6$, and on those starting with $\texttt{p}$ it reads $2, 3$. Start at row $SA^{-1}[0] = 4$ and follow $\Psi$: the rows $4, 2, 5, 3, 6, 1, 0$ start with $\texttt{p}, \texttt{a}, \texttt{p}, \texttt{a}, \texttt{y}, \texttt{a}, \texttt{\$}$.

20. If the $n$ symbols are distinct, the order of the suffixes is the order of their first symbols, so the suffix array sorts the symbols and the comparison lower bound for sorting applies. The children of the root of the suffix tree are then the $n + 1$ leaves, in sorted order, so the same bound holds.

21. If a non-overlapping repeat of length $L$ exists, so does one of length $L - 1$, so binary search on $L$. For a fixed $L$, cut the suffix array into groups of consecutive ranks with LCP at least $L$, and test whether some group has largest minus smallest start position at least $L$. Each test is $O(n)$. The answers are 3 ($\texttt{mur}$) and 2 ($\texttt{aa}$).

22. Use distinct separators so that no common prefix runs across a string end, and label each rank with its string. Slide a window over the ranks with two pointers, keeping it as short as possible while it holds suffixes from $k$ different strings; a count per string tracks this. The common prefix of the window is the minimum of the LCP values inside it, kept by a deque. Each pointer moves $N$ times.

23. If $R(SA[i] + 1) > R(SA[i + 1] + 1)$, the suffixes at ranks $i$ and $i + 1$ cannot start with the same symbol, because then the suffixes after their first symbols would be in the wrong order. So the first symbols, read in rank order, must increase at each such $i$. Conversely, give rank 0 the letter 0 and increase the letter exactly at these ranks; an induction on the length of the suffixes shows that the resulting string has suffix array $SA$. For $[5, 1, 3, 0, 2, 4]$ the values $R(SA[i] + 1)$ are $-1, 4, 5, 1, 2, 0$, with two descents, so 3 letters. For $[2, 0, 3, 1]$ there is one descent, so 2 letters, as for $\texttt{abab}$.
