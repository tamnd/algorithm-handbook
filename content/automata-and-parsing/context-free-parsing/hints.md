1. Five parse trees, one for each way to bracket three operators (the Catalan number $C_3$), and five leftmost derivations, since trees and leftmost derivations correspond one to one. The usual rules give $(a + (a * a)) + a$.

2. $A$ is nullable, so is $C$ through $C \to A$, $B$ through $B \to C$, and $S$ through $S \to A B$. $D$ derives no terminal string, so $D$ and the production $S \to a D$ are useless; then $d$ is unreachable. The productions left are $S \to A B$, $A \to a A \mid \varepsilon$, $B \to b B \mid C$ and $C \to c \mid A$.

3. One answer: $S \to A X \mid A B$, $X \to S B$, $A \to a$, $B \to b$. It has four nonterminals and five productions.

4. Number the positions 1 to 4. The cells of length 1 hold $L, L, R, R$. Of length 2 only the span $2..3$ is non-empty, with $S$. Of length 3 only $2..4$, with $X$, from $S$ on $2..3$ and $R$ on $4$. The whole span $1..4$ holds $S$, from $L$ and $X$. So $(())$ is in the language.

6. $\mathrm{FIRST}(S) = \{(, \varepsilon\}$ and $\mathrm{FOLLOW}(S) = \{), \$\}$. The table has $S \to ( S ) S$ under $($ and $S \to \varepsilon$ under $)$ and $\$$. The parser produces $S \Rightarrow ( S ) S \Rightarrow ( ) S \Rightarrow ( )$.

8. Shift $n$, reduce $E \to n$, shift $+$, shift $n$, reduce $E \to E + n$, shift $+$, shift $n$, reduce $E \to E + n$, accept: five shifts and three reductions. The handles are the first $n$, then $E + n$ twice.

9. Six states: $\{S' \to \cdot S, S \to \cdot ( S ), S \to \cdot a\}$; $\{S' \to S \cdot\}$; $\{S \to ( \cdot S ), S \to \cdot ( S ), S \to \cdot a\}$; $\{S \to a \cdot\}$; $\{S \to ( S \cdot )\}$; $\{S \to ( S ) \cdot\}$. No state has a complete item together with another item, so the grammar is LR(0).

10. `3 4 2 * + 1 -` and `2 3 2 ^ ^`.

11. The pairs $(1, 4)$, $(2, 2)$ and $(2, 4)$, each by a path labelled $()$; the longer path $1, 2, 3, 2, 4$ is labelled $(())$. A path from 3 starts with $)$ and is never balanced.

12. Use $S \to S S$ with one side $\varepsilon$ any number of times before $S \to ( S )$. The grammar $S \to ( S ) S \mid \varepsilon$ is unambiguous: the first symbol of a non-empty string is $($, and its matching $)$ is fixed.

15. A string is not of the form $ww$ when its length is odd, or when it can be split as $xy$ with $|x| = |y|$ and some position $i$ where $x$ and $y$ differ. The second kind are the strings $u a v\, u' b v'$ with $|u| = |u'|$ and $|v| = |v'|$, or the same with $a$ and $b$ swapped; regroup them as $(u a u'')(v'' b v')$ with each part of odd length and the differing symbol in its middle. This gives $S \to A B \mid B A \mid O$, $A \to C A C \mid a$, $B \to C B C \mid b$, $C \to a \mid b$, $O \to C \mid C C O$.

18. The state reached on $d$ from the start holds $S \to d \cdot c$ and $A \to d \cdot$; the state reached on $b d$ holds $S \to b d \cdot a$ and $A \to d \cdot$. Since $\mathrm{FOLLOW}(A) = \{a, c\}$, SLR(1) has a shift-reduce conflict on $c$ in the first and on $a$ in the second. The LALR(1) lookahead of $A \to d \cdot$ is $\{a\}$ in the first state and $\{c\}$ in the second, and the two states have different cores, so they are not merged.

21. Two trees, each of probability $p^2 (1 - p)^3$, so $2 p^2 (1 - p)^3$. The probability $x$ that a tree is finite is the least solution of $x = (1 - p) + p x^2$, whose roots are $1$ and $(1 - p)/p$. For $p = 0.4$ it is 1; for $p = 0.6$ it is $2/3$.

24. Exactly when $n = 2^k - 1$ for some $k \ge 1$. Let $f(r)$ be the length that $S$ matches when $r$ symbols remain. Then $f(0)$ fails, and $f(r) = f(r - 1) + 2$ if $f(r - 1)$ succeeds and $r - 1 - f(r - 1) \ge 1$, and $f(r) = 1$ otherwise. Ordered choice never returns to the second option once the first succeeds, so $f$ climbs by 2 and drops back to 1 when it would overrun.

25. Suppose a DPDA $M$ accepts the language. Make two copies of $M$; when the first copy reaches an accepting state, jump to the matching state of the second copy, in which $b$ is renamed $c$. On $a^n b^n c^n$ the first copy accepts after $a^n b^n$, and because $M$ is deterministic the run continues as it would on $a^n b^{2n}$. The result is a PDA for a language whose intersection with $a^* b^* c^+$ is $\{a^n b^n c^n : n \ge 1\}$, which is not context-free. Knuth's theorem then rules out an LR(k) grammar.

26. A linear language has a pumping lemma in which the pumped parts lie within $p$ symbols of the two ends of the string: $w = u v x y z$ with $|u v y z| \le p$. Pump $a^p b^p c^p d^p$: $v$ lies in the $a$s and $y$ in the $d$s, so pumping breaks the equality of $a$s and $b$s.

27. By Exercise 19 both languages are regular, and the proof of Parikh's theorem is effective: from a grammar it computes a finite union of arithmetic progressions for the lengths. Build a DFA from each and compare the DFAs.
