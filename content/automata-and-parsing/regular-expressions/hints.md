1. $\mathrm{First} = \{1, 2, 3\}$, $\mathrm{Last} = \{5\}$, $\mathrm{Follow}(1) = \mathrm{Follow}(2) = \{1, 2, 3\}$, $\mathrm{Follow}(3) = \{4\}$, $\mathrm{Follow}(4) = \{5\}$ and $\mathrm{Follow}(5) = \emptyset$. The automaton has $5 + 1 = 6$ states, and state 5 is the only accepting one. It is not deterministic: from the initial state, and from states 1 and 2, the symbol $a$ leads to both 1 and 3.

2. $\partial_a (ab)^* = b(ab)^*$ and $\partial_b (ab)^* = \emptyset$; $\partial_a\, b(ab)^* = \emptyset$ and $\partial_b\, b(ab)^* = (ab)^*$. The DFA has three states, $(ab)^*$, $b(ab)^*$ and $\emptyset$, and only $(ab)^*$ is accepting, since it is the only nullable one. $abab$ ends in $(ab)^*$ and matches; $aba$ ends in $b(ab)^*$ and does not.

3. The subexpressions $\emptyset$, $a\emptyset$, $b\emptyset$ and the whole first branch $(a\emptyset)^* b \emptyset$ denote $\emptyset$; the stars $(a\emptyset)^*$ and $(b\emptyset)^*$ denote $\{\varepsilon\}$, not $\emptyset$. So $L(r) = \{ac\}$: not empty, and $ac$ is the shortest string.

4. $X_0 = b X_0 \cup a X_1 \cup \varepsilon$ and $X_1 = b X_1 \cup a X_0$. Arden's lemma gives $X_1 = b^* a X_0$; substituting, $X_0 = (b \cup a b^* a) X_0 \cup \varepsilon$, so $X_0 = (b \mid a b^* a)^*$: the strings with an even number of $a$s.

5. No. The lengths it accepts are the sums of 2s and 5s, which are all numbers except 1 and 3, so it misses $a$ and $aaa$. The expression $(aa \mid aaaaa)^* \mid a \mid aaa$ is universal.

6. Both rules give the overall match $(0, 3)$, the whole text. Leftmost-first: group 1 is $(0, 1) = a$, since $a$ is tried before $ab$, and group 2 is $(1, 3) = ba$. POSIX: group 1 takes the longest string that still allows the overall match, $(0, 2) = ab$, and group 2 is $(2, 3) = a$.

7. The greedy `a.*b` reports `aXbYb`, the lazy `a.*?b` reports `aXb`. Both match the whole string `aXbYb`: as whole-string matches they accept the same language.

8. 13 ways. The number of ways for $a^n$ is the Fibonacci number $F_{n+1}$ (with $F_1 = F_2 = 1$), since the last piece is $a$ or $aa$. The matcher fails on $c$ after each way of covering every prefix, and it tries them all before it reports no match, so its time grows like $1.618^n$.

9. Size $4 \cdot 3 + 2 = 14$, and the minimal DFA has $2^3 = 8$ states. With $z$ empty both strings match, and with one more symbol neither does. The shortest suffixes are the four strings of length 2: each moves the last symbol of $aba$ or $abb$ to the third position from the end, where they differ.

10. With $r = (a \mid b)^* abb$, the states are $r$, $r \mid bb$, $r \mid b$ and $r \mid \varepsilon$, the last one accepting: four states, the same as the minimal DFA for "ends in $abb$".

13. $(aa+)$ captures $a^k$ with $k \ge 2$, and $\backslash 1+$ repeats it at least once more, so the pattern matches $a^n$ exactly when $n = kj$ with $k, j \ge 2$, that is, when $n$ is composite: $n = 4, 6, 8, 9, 10, 12$. If this language were regular, so would be its complement within $a^*$, which contains the primes and only finitely many other lengths; the primes are not regular.

15. $n + 2$ states: count the first $n - 1$ symbols, then look at the $n$-th, then go to an accepting or a rejecting sink. A pattern anchored at the start that looks a fixed distance ahead has a small DFA, and running the DFA of the reversed pattern backwards over the text is how some engines avoid the blowup.

16. The pattern denotes $L_{N+1}$, so its minimal DFA has $2^{N+1}$ states. With $d = \ell - 14$ digits, take $N = 10^{d - 1}$.

20. The partial derivatives are $r_n$ and $(a \mid b)^j$ for $j = n - 1, \ldots, 0$, with $(a \mid b)^0 = \varepsilon$: $n + 1$ states. The expression has $k = 2n + 1$ symbol occurrences, so the Glushkov automaton has $2n + 2$ states.

21. Take $a a^* \cap (a^{p_1})^* \cap \cdots \cap (a^{p_n})^*$, where $p_1, \ldots, p_n$ are the first $n$ primes. Its size is $O(p_1 + \cdots + p_n)$, which is polynomial in $n$, and its shortest non-empty string has length $p_1 \cdots p_n \ge 2^n$. The shortest string of $r \cap s$ is not determined by the shortest strings of $r$ and $s$.

22. Take $(\varepsilon, a b^{n-1})$ and $(a b^i, b^{n-1-i})$ for $0 \le i \le n - 1$. For $i \ne j$, $a b^i b^{n-1-j}$ has length different from $n$ and a single $a$ at the front, so its $n$-th symbol from the end is not $a$; and $\varepsilon \cdot b^{n-1-i}$ has no $a$ at all.

23. Write the text as $n$ copies of `rgb`, then $m$ copies of `rg,rb,gr,gb,br,bg`, all separated by `;`. For vertex $i$ the pattern has `[rgb]*([rgb])[rgb]*`; for an edge $\{u, v\}$ it has `[^;]*\u\v[^;]*`; join the parts with `;` and anchor the whole pattern. Two adjacent colour letters occur in an edge block only as a pair of different colours, so each edge part matches exactly when the groups of $u$ and $v$ hold different colours.

24. A DFA over one letter is a path of $t$ states followed by a cycle of $p$ states. Its language is a finite set of strings of length less than $t$ together with a union of sets $a^{t + i} (a^p)^*$ for the accepting states $i$ on the cycle, which is an expression of star height at most 1. Star height 0 means no star at all, which gives exactly the finite languages.

25. Let $x = a^*(b a^*)^*$. For $(a + b)^* \le x$, show $1 + (a + b) x \le x$ and apply induction with $b = 1$: use $a a^* \le a^*$ for the $a$ part and $b a^* (b a^*)^* \le (b a^*)^* \le x$ for the $b$ part. For the other direction, let $y = (a + b)^*$; induction shows $a^* \le y$ and $(b a^*)^* \le y$, and then $x \le y y = y$.
