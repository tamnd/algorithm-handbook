1. ◦ Compute the [prefix function](/prefix-function/) of $P = \texttt{abacaba}$. What is the smallest period of $P$, and what are all its borders?

2. ◦ Compute the Z-array of $S = \texttt{aabxaab}$ with the [Z-algorithm](/z-algorithm/), for the positions $k = 1, \ldots, 6$.

3. ◦ How many character comparisons does [naive string matching](/naive-string-matching/) make on the text $a^{10}$ and the pattern $\texttt{aaab}$, comparing each window from left to right? Give a formula for $T = a^n$ and $P = a^{m-1}b$.

4. ◦ A matcher hashes a string of decimal digits to its value modulo 11, and compares windows of the text $T = \texttt{3141592653}$ with the pattern $P = \texttt{26}$ by hash first. List the shifts where the hashes agree, and say which of them are [spurious hits](/spurious-hit/).

5. ◦ Build the shift table of [Horspool](/boyer-moore-horspool/) for $P = \texttt{abcab}$. Run the search on $T = \texttt{abacabcabxabcab}$ and list the shifts of the windows it tests and the occurrences it reports.

6. ◦ Give the full transition table of the [string-matching automaton](/string-matching-automaton/) of $P = \texttt{aba}$ over the alphabet $\{\texttt{a}, \texttt{b}\}$, with states $0$ to $3$.

7. ◦ For $P = \texttt{abab}$, compute the prefix function $\pi$ and the strong failure table $\mathrm{nxt}[0 \ldots 4]$ of [Knuth-Morris-Pratt](/knuth-morris-pratt/). At which entries does $\mathrm{nxt}[q]$ differ from the fall-back $\pi[q-1]$ of [Morris-Pratt](/morris-pratt/)?

8. ◦ Which shifts of $T = \texttt{cabbcabca}$ start an occurrence of some rotation of $P = \texttt{abc}$, in the sense of [circular pattern matching](/circular-pattern-matching/)?

9. ◦ In the sense of [order-preserving matching](/order-preserving-matching/), which windows of $T = (5, 9, 7, 2, 4, 3, 8, 10, 1, 6)$ match the pattern $P = (1, 3, 2)$? Give their starting shifts, counting from 0.

10. ◦ In [parameterized matching](/parameterized-pattern-matching/) with every symbol a parameter, write the prev-encoding of $\texttt{xyxzy}$, where each symbol is replaced by the distance to its previous occurrence, or 0 if it has none. Which windows of $T = \texttt{abbaccab}$ match $P = \texttt{xyyx}$?

11. • The [Morris-Pratt](/morris-pratt/) entry shows that on $P = a^{m-1}b$ and text $a^{m-1}c$ the last text character is compared $m$ times. How many times does Knuth-Morris-Pratt compare it? Explain from the strong failure table.

12. • Horspool takes $\Theta(nm)$ time on $T = a^n$ and $P = b\,a^{m-1}$. How many comparisons does [Boyer-Moore](/boyer-moore/) make on the same input, and which of its two rules is responsible?

13. • Build the shift table of [Quick Search](/quick-search/) for $P = \texttt{abcab}$ and run it on the text of exercise 5. Which windows does it test? Which text characters give the largest possible shift, and why can that shift be $m + 1$?

14. • Show how to compute the prefix function of a string from its Z-array in $O(m)$ time.

15. • Let $P = a^m$ and $T = a^n$ with $n \ge m \ge 1$, over an alphabet with at least two letters. Prove that any algorithm that reports all occurrences of $P$ in $T$ must read every character of $T$.

16. • Prove that if $P$ occurs in $T$ at shifts $s$ and $s + d$ with $0 < d < m$, then $d$ is a [period](/string-period/) of $P$. Deduce that a pattern with smallest period $p$ occurs at most $\lfloor (n - m)/p \rfloor + 1$ times in a text of length $n$.

17. • Extend [Shift-Or](/shift-or/) to patterns in which each position is a set of characters, such as $\texttt{[ab]c[abc]}$. What changes in the preprocessing, and what changes in the search?

18. • Let $P$ be any fixed pattern and let $T$ be a text whose characters are drawn independently and uniformly from an alphabet of size $\sigma \ge 2$. Show that naive matching makes fewer than $\sigma/(\sigma - 1)$ comparisons per window on average, so at most $2(n - m + 1)$ in expectation.

19. • Give an $O(n + m)$ algorithm that finds the longest prefix of $P$ that is also a suffix of $T$.

20. • On $T = a^n$ and $P = a^m$, how many comparisons does Boyer-Moore make without the [Galil rule](/galil-rule/), and how many with it?

21. • Compute the local period at each cut $1, \ldots, 4$ of $\texttt{abaab}$ and list its critical cuts, in the sense used by the [two-way algorithm](/two-way-string-matching/).

22. • Show that Morris-Pratt makes exactly $2n - 1$ comparisons on $P = \texttt{ab}$ and $T = a^n$, so its bound of $2n - 1$ comparisons in the search is tight.

23. ★ Let $P$ have smallest period $p$, and let $P$ occur in $T$ at shifts $s$ and $s + d$ with $0 < d \le m - p$. Prove that $p$ divides $d$.

24. ★ Let $P = \texttt{ab}$ over the alphabet $\{\texttt{a}, \texttt{b}\}$. Prove that any deterministic algorithm that decides whether $P$ occurs in $T$ reads at least $n - 1$ characters of some text of length $n$. (This is the case $m = 2$ of Rivest's bound $n - m + 1$.)

25. ★ In the string-matching automaton, call a transition $\delta(q, c) = k$ *backward* if $k \ge 1$ and it is not the forward step $q \to q + 1$ on $c = P[q]$. Prove that the automaton has at most $m$ backward transitions, so at most $2m$ transitions that do not lead to state 0.

26. ★ Pattern and text are strings of positive integers in which the value 0 is a *wildcard* that matches any symbol. Show that $\sum_j p_j t_{i+j} (p_j - t_{i+j})^2 = 0$ exactly when the pattern matches at shift $i$, and use this to find all matches in $O(n \log m)$ time with the fast Fourier transform.

27. ★ The text and the pattern are given run-length encoded, as lists of pairs (character, run length), with $r_T$ and $r_P$ runs. Find all occurrences of $P$ in $T$ in $O(r_T + r_P)$ time, plus the number of occurrences reported.
