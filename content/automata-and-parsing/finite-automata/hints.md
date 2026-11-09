1. Three states: "no $a$ waiting", "last symbol was $a$", and an accepting sink "found $ab$". The complement is the set of strings with no $a$ before a $b$, which is $b^* a^*$.

2. The reachable subsets are $\{0\}$, $\{0, 1\}$, $\{0, 2\}$ and $\{0, 1, 2\}$; the last two are accepting. On $a$ each subset goes to $\{0, 1\}$ or, from a subset containing 1, to $\{0, 1, 2\}$; on $b$ it goes to $\{0\}$ or, from a subset containing 1, to $\{0, 2\}$. $N$ accepts the strings whose second symbol from the end is $a$.

3. $E(\{1\}) = E(\{2\}) = \{1, 2, 3, 4\}$ and $E(\{4\}) = \{4\}$. After $a$ the active set is $E(\{5\}) = \{5\}$.

4. All $2 \cdot 3 = 6$ pairs are reachable. One pair is accepting for the intersection, $3 + 2 - 1 = 4$ for the union, and $4 - 1 = 3$ for the symmetric difference.

5. The language is $\{aa\}$: non-empty and finite. The only cycles are the loops on state 3, which cannot reach an accepting state, so state 3 is not useful.

6. Three classes: the strings that end in $a$; the strings that end in $ab$; and all others, which include $\varepsilon$, $b$ and the strings ending in $bb$. So the minimal DFA has three states.

7. Round 0: $\{0, 1, 2, 4\}, \{3\}$. Round 1 splits by the classes of the successors: $\{0, 1\}, \{2, 4\}, \{3\}$. Round 2 splits nothing. The minimal DFA has three states and accepts the strings that end in $ba$.

8. The run is $e, o, o, o, e$. Among the first $p + 1 = 3$ states, $r_1 = r_2 = o$, so $x = 1$, $y = 0$, $z = 01$. Indeed $1\,0^i\,01$ has two 1s for every $i$.

9. Both accept $\varepsilon$ and $b$ and reject $a$. At length 2, $A$ accepts $aa$ and $B$ rejects it, and $B$ accepts $ab$ and $A$ rejects it; $ba$ and $bb$ get the same answer from both. So the answers are $aa$ and $ab$.

10. The occurrences of $01$ and $10$ alternate along the string, so they are equal in number exactly when the string is empty or its first and last symbols agree. The DFA remembers the first symbol and the last one: five states, all pairwise distinguishable.

12. Let $c_\ell(q)$ be the number of strings of length $\ell$ that lead from $q$ to an accepting state; then $c_0(q) = [q \in F]$ and $c_{\ell}(q) = \sum_{a} c_{\ell - 1}(\delta(q, a))$. For Exercise 1, the rejected strings of length $\ell$ are $b^i a^{\ell - i}$, so the answer is $2^\ell - \ell - 1$.

14. A Moore machine's output must be a function of the state, so it must remember the last bit and also whether the last output was 1. With the start state this gives five classes of prefixes: $\varepsilon$, and "ends in $c$, last output $o$" for $c, o \in \{0, 1\}$. Check that the five are pairwise distinguishable.

15. The answer depends only on $k \bmod 15$, and the accepted residues $\{0, 3, 5, 6, 9, 10, 12\}$ have no smaller period, so the minimal DFA has 15 states. An NFA guesses which divisor to test: a start state that moves into a 3-cycle and a 5-cycle.

16. Since $2 \equiv -1 \pmod 3$, a bit string with bits $b_0 b_1 \cdots b_{t-1}$ has value $\pm \sum_i (-1)^i b_i$ modulo 3 in either reading. So the two values are both divisible by 3 or both not. For 5 it fails: $11001$ is 25 read from the left and 19 read from the right.

20. $x \equiv_L y$ if and only if $x \equiv_{\bar L} y$, so the two relations have the same classes. For partial DFAs the counts can differ by one: over $\{a, b\}$, $a^*$ needs one state and its complement two.

21. Run the DFA on $x$ and, at the same time, track the set $S_k$ of states from which some string of length $k = |x|$ reaches an accepting state. $S_0 = F$, and $S_{k+1}$ is the set of states with some move into $S_k$. Accept when the current state is in the current set. The states are pairs in $Q \times 2^Q$.

22. A start state that accepts $\varepsilon$ and moves on $a$ into position 1 of a cycle of length $p_i$ for each $i$; in each cycle, every position except 0 is accepting. The NFA accepts $a^k$ for $k \ge 1$ exactly when some $p_i$ does not divide $k$. With the first $k$ primes, the number of states grows like $k^2 \log k$ and the shortest rejected length like $e^{k \log k}$.

23. Use the minimal DFA with states "nothing", "last symbol $a$" and "found". The transformations of $\varepsilon$, $a$, $b$, $ab$ and $ba$ are distinct, and every other string acts like one of them: $a^2 = a$, $b^2 = b$, and any string containing $ab$ acts like $ab$, which sends every state to "found". Each element satisfies $x^2 = x^3$. A star-free expression is $\overline{\emptyset}\, a b\, \overline{\emptyset}$.

24. The first partition has at most two blocks, each round that splits adds at least one block, and there are at most $n$ blocks. For the lower bound, take states $0, \ldots, n - 1$ with $i \to i + 1$, a loop on $n - 1$, and $n - 1$ the only accepting state: round $j$ splits off state $n - 1 - j$ and nothing else.
