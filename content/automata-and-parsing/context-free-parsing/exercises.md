1. ◦ The grammar $E \to E + E \mid E * E \mid a$ is [ambiguous](/ambiguity/). How many parse trees does $a + a * a + a$ have? How many leftmost derivations? Which tree matches the usual rules that $*$ binds tighter than $+$ and both group to the left?

2. ◦ Let $G$ have the productions $S \to A B \mid a D$, $A \to a A \mid \varepsilon$, $B \to b B \mid C$, $C \to c \mid A$ and $D \to d D$. Which nonterminals are [nullable](/nullable-symbol/)? Which symbols are [useless](/useless-symbol-elimination/), and which productions are left after removing them?

3. ◦ Convert $S \to a S b \mid a b$ to [Chomsky normal form](/chomsky-normal-form/). How many nonterminals and productions does your grammar have?

4. ◦ The grammar $S \to S S \mid L R \mid L X$, $X \to S R$, $L \to ($, $R \to )$ is in Chomsky normal form and generates the non-empty balanced strings of parentheses. Fill the table of the [CYK algorithm](/cyk-algorithm/) for the input $(())$. Which cells are non-empty?

5. ◦ Give a context-free grammar for $\{a^i b^j : i \le j \le 2i\}$.

6. ◦ For $S \to ( S ) S \mid \varepsilon$, compute the [FIRST and FOLLOW sets](/first-and-follow-sets/) of $S$ and build the [LL parse table](/ll-parse-table/). Run the [LL(1) parser](/ll1-parsing/) on $()$ and give the leftmost derivation it produces.

7. ◦ Remove the [left recursion](/left-recursion/) from $A \to A a \mid A b \mid c \mid d$. What language does the grammar generate?

8. ◦ Run a [shift-reduce parser](/shift-reduce-parsing/) for $E \to E + n \mid n$ on $n + n + n$. List the actions. How many shifts and reductions are there, and what is the handle at each reduction?

9. ◦ Build the LR(0) automaton of the grammar $S \to ( S ) \mid a$, augmented with $S' \to S$, from its [LR items](/lr-item/). How many states does it have? Is the grammar [LR(0)](/lr0-parsing/)?

10. ◦ Use the [shunting-yard algorithm](/shunting-yard-algorithm/) to convert `3 + 4 * 2 - 1` and `2 ^ 3 ^ 2` to reverse Polish notation, with `^` right-associative and binding tighter than `*`.

11. ◦ A graph has the edges $1 \xrightarrow{(} 2$, $2 \xrightarrow{(} 3$, $3 \xrightarrow{)} 2$, $2 \xrightarrow{)} 4$ and $3 \xrightarrow{)} 4$. In the sense of [CFL reachability](/cfl-reachability/) with the [Dyck language](/dyck-language/) of one bracket pair, which pairs $(u, v)$ are joined by a non-empty path whose label is a balanced string?

12. • Show that $S \to S S \mid ( S ) \mid \varepsilon$ gives the string $()$ infinitely many parse trees. Give an unambiguous grammar for the same language.

13. • Use the [pumping lemma](/cfl-pumping-lemma/) to prove that $\{a^i b^j c^k : i \le j \le k\}$ is not context-free.

14. • Prove that the strings over $\{a, b, c\}$ with equal numbers of $a$, $b$ and $c$ do not form a context-free language. Use a [closure property](/cfl-closure-properties/) and a language you know is not context-free.

15. • Give a context-free grammar for the complement $\{a, b\}^* \setminus \{ww : w \in \{a, b\}^*\}$.

16. • Give the binding powers of a [Pratt parser](/pratt-parsing/) for binary `+`, `-`, `*`, `/` (left-associative), `^` (right-associative, tightest) and prefix `-`, so that `-2^2` parses as `-(2^2)` and `-2*3` as `(-2)*3`. How do `a - b - c` and `a ^ b ^ c` parse?

17. • Augment $E \to E + n \mid n$ with $S' \to E$. List all [viable prefixes](/viable-prefix/) of the grammar. Is the set finite?

18. • Show that the grammar $S \to A a \mid b A c \mid d c \mid b d a$, $A \to d$ is not [SLR(1)](/slr-grammar/) but is [LALR(1)](/lalr-grammar/). Name the states and lookaheads involved.

19. • Use [Parikh's theorem](/parikh-theorem/) to prove that every context-free language over a one-letter alphabet is regular.

20. • Given a grammar $G$ in Chomsky normal form with $p$ productions and a DFA $M$ with $q$ states, construct a grammar for $L(G) \cap L(M)$. How many nonterminals and productions does it have?

21. • A [probabilistic grammar](/probabilistic-context-free-grammar/) has $S \to S S$ with probability $p$ and $S \to a$ with probability $1 - p$. What is the probability of the string $aaa$? What is the total probability of all finite trees, for $p = 0.4$ and for $p = 0.6$?

22. • Give a grammar in [Greibach normal form](/greibach-normal-form/) for the non-empty balanced strings of parentheses.

23. • Decide whether each grammar generates a [finite language](/cfg-finiteness-problem/): $G_1$ with $S \to A B \mid c$, $A \to B C \mid a$, $B \to b \mid C A$, $C \to c$; and $G_2$, the same without $B \to C A$. For the finite one, give a longest string.

24. ★ The [parsing expression grammar](/parsing-expression-grammar/) $S \leftarrow a\, S\, a \;/\; a$ looks like a grammar for the strings of $a$s of odd length. For which $n$ does it match all of $a^n$? Prove your answer.

25. ★ Prove that $\{a^n b^n : n \ge 0\} \cup \{a^n b^{2n} : n \ge 0\}$ is not a [deterministic context-free language](/deterministic-context-free-language/), and so has no LR(k) grammar.

26. ★ A [linear grammar](/linear-grammar/) has at most one nonterminal on each right side. Prove that $\{a^n b^n c^m d^m : n, m \ge 0\}$ is context-free but not linear.

27. ★ Show that [equivalence of context-free grammars](/cfg-equivalence-problem/) is decidable when the terminal alphabet has one letter.
