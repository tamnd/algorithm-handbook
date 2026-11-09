1. ◦ Mark the symbols of $r = (a \mid b)^* abb$ as positions $a_1 b_2 a_3 b_4 b_5$. Compute $\mathrm{First}$, $\mathrm{Last}$ and $\mathrm{Follow}(p)$ for each position, and give the [Glushkov automaton](/glushkov-automaton/) of $r$. How many states does it have, and is it deterministic?

2. ◦ Compute the [derivatives](/regex-derivative/) $\partial_a r$ and $\partial_b r$ of $r = (ab)^*$, then the derivatives of the results, simplifying $\emptyset \cdot x$ to $\emptyset$ and $\varepsilon \cdot x$ to $x$. Draw the DFA whose states are these expressions. Which states are accepting? Use it to decide whether $abab$ and $aba$ match $r$.

3. ◦ Let $r = (a\emptyset)^*\, b\, \emptyset \mid (\emptyset \mid a)(b\emptyset)^*(c \mid \emptyset)$. Which subexpressions denote $\emptyset$, and which denote $\{\varepsilon\}$? Is $L(r)$ empty? Give a shortest string in it, as the bottom-up pass of [regex emptiness](/regex-emptiness/) would.

4. ◦ The DFA over $\{a, b\}$ with states $0$ (start, accepting) and $1$ moves between the two states on $a$ and stays put on $b$. Write the equations $X_0 = \ldots$ and $X_1 = \ldots$ for the languages accepted from each state and solve them with [Arden's lemma](/arden-lemma/) to get a regular expression for the language.

5. ◦ Over the alphabet $\{a\}$, is $(aa \mid aaaaa)^*$ [universal](/regex-universality/)? If not, list every string it misses. Give the shortest expression of the form $(aa \mid aaaaa)^* \mid s$, with $s$ a union of strings, that is universal.

6. ◦ Search the text $aba$ for the pattern $(a \mid ab)(ba \mid a)^*$. Give the overall match and the span of each group under leftmost-first rules and under [POSIX rules](/posix-regex-semantics/). For a group inside a star, report its last iteration.

7. ◦ On the text `aXbYb`, which match does a [regex search](/regex-search/) report for `a.*b`, and which for `a.*?b`, under leftmost-first rules? Does each pattern match the whole string `aXbYb`?

8. ◦ In how many ways can $(a \mid aa)^*$ match the string $a^6$? Give a formula for the number of ways it can match $a^n$. Why does this count matter to a [backtracking matcher](/backtracking-regex-matching/) that is asked to match $(a \mid aa)^* c$ against $a^n$?

9. ◦ Let $r_3 = (a \mid b)^* a (a \mid b)(a \mid b)$, from the [exponential blowup](/regex-dfa-state-blowup/) entry. What is its size, and how many states has its minimal DFA? Find all shortest suffixes $z$ such that exactly one of $abaz$ and $abbz$ matches $r_3$.

10. • Build the [derivative](/regex-derivative/) DFA of $(a \mid b)^* abb$, simplifying unions with associativity, commutativity and idempotence and dropping $\emptyset$ from unions. How many states does it have, and which are accepting? Compare it with the minimal DFA of the language.

11. • A DFA over $\{a, b\}$ has states $0, 1, 2$, start and accepting state 0, the moves $i \xrightarrow{a} i + 1 \bmod 3$, and a loop on $b$ at each state. Use [state elimination](/state-elimination/), removing state 2 first and then state 1, to get a regular expression for its language.

12. • Over $\{a, b, c\}$, the pattern `(?=.*a)(?=.*b).*`, used as a whole-string match, uses [lookahead](/regex-lookaround/). Give an ordinary regular expression for the same language, and the number of states of its minimal complete DFA.

13. • Over the alphabet $\{a\}$, the pattern `^(aa+)\1+$` uses a [backreference](/backreference/). For which $n$ does it match $a^n$? List the matching $n$ with $1 \le n \le 12$, and show that the language is not regular.

14. • In the Glushkov automaton of Exercise 1, number the states $0$ (initial) to $5$. [Bit-parallel matching](/bit-parallel-regex-matching/) keeps the active set $D$ and updates it by $D \leftarrow T[D] \mathbin{\&} B[c]$. Give the masks $B[a]$ and $B[b]$ and the set $T[\{0\}]$, and run the update on the input $aabb$. Does it match?

15. • Let $L_n = L((a \mid b)^* a (a \mid b)^{n - 1})$, whose minimal DFA has $2^n$ states. How many states has the minimal complete DFA of the reversal $L_n^R$? What does the pair tell you about building a DFA for a pattern that is anchored at the start instead of the end?

16. • The pattern `(a|b)*a(a|b){N}`, with $N$ written in decimal, has $14 + d$ characters, where $d$ is the number of digits of $N$. How many states has its minimal DFA? Show that some patterns of $\ell$ characters with [bounded repetition](/bounded-repetition/) need DFAs with at least $2^{10^{\ell - 15}}$ states.

17. • Show that $(a \mid b)^* a (a \mid b)^*$ is [ambiguous](/regex-ambiguity-detection/): in how many ways does it match a string with $j \ge 1$ occurrences of $a$? Give an unambiguous expression for the same language.

18. • Arden's lemma needs $\varepsilon \notin A$ for uniqueness. Show that when $\varepsilon \in A$, every language $A^*(B \cup C)$ solves $X = AX \cup B$. Give two different solutions of $X = (\varepsilon \mid a) X \cup b$.

19. • Over $\{a, b\}$, give a [star-free expression](/star-free-expressions/), using union, concatenation, complement and intersection but no star, for $(ab)^*$. Write $\Sigma^*$ as the complement of $\emptyset$.

20. • Compute the [partial derivatives](/antimirov-derivatives/) of $r_n = (a \mid b)^* a (a \mid b)^{n - 1}$ by all words. How many states has Antimirov's NFA, and how many has the Glushkov automaton of $r_n$?

21. • Find expressions with intersection, of size polynomial in $n$, whose shortest non-empty string has length at least $2^n$. Why does this rule out deciding emptiness of such expressions by the bottom-up pass of Exercise 3?

22. ★ A *fooling set* for a language $L$ is a set of pairs $(x_i, y_i)$, $1 \le i \le p$, with every $x_i y_i \in L$ and, for $i \ne j$, $x_i y_j \notin L$ or $x_j y_i \notin L$. Every NFA for $L$ then has at least $p$ states ([fooling set method](/fooling-set-method/)). Find a fooling set of size $n + 1$ for $L_n$ of Exercise 15, and conclude that Antimirov's NFA of Exercise 20 is a minimal NFA.

23. ★ Show that [matching with backreferences](/backreference-matching/) is NP-hard by a polynomial reduction from [3-colouring](/three-coloring/) of graphs: from a graph $G$, build a text and a pattern with one capture group per vertex such that the pattern matches the text if and only if $G$ has a proper 3-colouring.

24. ★ Prove that every regular language over a one-letter alphabet has an expression of [star height](/star-height-problem/) at most 1. Which unary regular languages have star height 0?

25. ★ Prove the denesting law $(a + b)^* = a^*(b a^*)^*$ from the axioms of [Kleene algebra](/kleene-algebra/), using the identity $x^* x^* = x^*$ and the induction axiom $b + a x \le x \Rightarrow a^* b \le x$.
