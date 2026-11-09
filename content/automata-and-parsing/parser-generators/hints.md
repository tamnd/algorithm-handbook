1. Only $A$ is nullable. $\mathrm{FIRST}(A) = \{a\}$, $\mathrm{FIRST}(B) = \{b, c\}$ and $\mathrm{FIRST}(S) = \{a, b, c\}$, since $A$ can vanish. $\mathrm{FOLLOW}(S) = \mathrm{FOLLOW}(B) = \{\$\}$ and $\mathrm{FOLLOW}(A) = \{b, c\}$. The PREDICT sets are $\{a\}$ and $\{b, c\}$ for $A$, and $\{b\}$ and $\{c\}$ for $B$, so the grammar is LL(1).

2. $\mathrm{FOLLOW}(A) = \{b\}$, so the cell $M[A, b]$ holds both $A \to b\,A$ and $A \to \varepsilon$. The language is $\{b^k : k \ge 1\} \cup \{c\}$, and $S \to b\,T \mid c$, $T \to b\,T \mid \varepsilon$ is LL(1), with PREDICT sets $\{b\}$ and $\{\$\}$ for $T$.

4. From $S \to a\,S\,b$: $a \doteq b$, $a \lessdot a$ and $a \lessdot c$ (the leading terminals of $S$), $b \gtrdot b$ and $c \gtrdot b$ (the trailing ones). With the end marker: $\$ \lessdot a$, $\$ \lessdot c$, $b \gtrdot \$$ and $c \gtrdot \$$. No pair has two relations, so it is an operator precedence grammar.

7. The grammar is LL(2) and not LL(1): both productions of $S$ begin with $c$, and the second token, $a$ or $b$, separates them. It is LR(1) and not LR(0): after $c$ the LR(0) state holds $A \to c\,\cdot$ and $B \to c\,\cdot$, and the next token decides.

9. For $k = 1$, $\mathrm{FIRST}_1(\beta L)$ is $\mathrm{FIRST}(\beta)$ when $\beta$ is not nullable and $\mathrm{FIRST}(\beta) \cup L$ when it is. Both alternatives cannot be nullable, so a strong conflict pairs a token of $\mathrm{FIRST}(\gamma)$ with one token of $\mathrm{FOLLOW}(A)$, and a single left-sentential form that puts that token after $A$ shows the same conflict. For $k = 2$ a lookahead string can take one token from $\beta$ and one from the context, and the union over all contexts makes pairs that no single context produces.

10. $E \to T\,E'$, $E' \to -\,T\,E' \mid \varepsilon$, with PREDICT sets $\{-\}$ and $\{\$\}$ for $E'$. Computing bottom-up on the right-recursive $E'$ gives $5 - (3 - 1) = 3$. Pass the value so far down into $E'$ as an inherited attribute and subtract each new $T$ from it; then the result is $(5 - 3) - 1 = 1$.

12. The LR(0) automaton has 6 states. The canonical LR(1) collection has 10: the start state, the accepting state, and two copies, with lookahead $\$$ and with lookahead $b$, of each of the states after $a$, after $c$, after $a\,S$ and after $a\,S\,b$. LALR(1) merges those four pairs.

16. A deterministic LR(k) parser traces the rightmost derivation backwards, and each step is fixed by the stack and the next $k$ tokens. Two parse trees give two rightmost derivations; at the last step where they differ, the definition of LR(k) forces the same handle and production.

17. The old tree has $n$ nodes labelled $A$, and the new one needs $n$ nodes labelled $B$, none of which exist. In $S \to T\,x \mid T\,y$, $T \to a\,T \mid a$, the subtree for $a^n$ stays and only the root changes.

18. Every nonterminal except $S$ and $X$ has one production, and the PREDICT sets are $\{(\}$, $\{]\}$ and $\{)\}$ for $S$ and $\{)\}$ and $\{]\}$ for $X$. In the LR(1) collection the state reached on $A$ from the start holds $[E \to A\,\cdot,\ ]]$ and $[F \to A\,\cdot,\ )]$, and the state reached on $A$ after $($ holds the same cores with the lookaheads swapped. LALR(1) merges them into a reduce-reduce conflict on both tokens.

19. In an LL(1) grammar the production at a node of the tree is fixed by the first token of its yield, or by the token after it when the yield is empty. An LR(1) parser reduces that node only after it has seen both, so a conflict in the LR(1) collection would give two leftmost derivations that agree on a prefix and one token but choose different productions.

20. A rightmost derivation in $G$ that reaches the LR(0) state $p$ and then $A$ corresponds to a derivation in $G'$ that reaches $[p, A]$, because the states $p_i$ are exactly those the parser passes through on the right side. The relations DR, reads and includes are then the rules of an ordinary FOLLOW computation in $G'$: a terminal right after $[p, A]$, a nullable symbol in between, and $[p, A]$ at the right end of a production of $[p', B]$.

21. Go through a deterministic pushdown automaton. An LR(k) parser is one, after the lookahead is folded into the states; then build a grammar from the automaton whose nonterminals record a state, a stack symbol and the state after it is popped, and check that one token of lookahead decides every reduction.
