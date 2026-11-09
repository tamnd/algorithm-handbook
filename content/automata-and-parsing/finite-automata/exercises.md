1. ◦ Give a complete [DFA](/deterministic-finite-automaton/) over $\{a, b\}$ that accepts the strings containing $ab$ as a substring. How many states does the smallest such DFA have? Describe its complement by a regular expression.

2. ◦ An NFA $N$ over $\{a, b\}$ has states $0, 1, 2$, start state 0 and accepting state 2. Its moves are $0 \xrightarrow{a,b} 0$, $0 \xrightarrow{a} 1$ and $1 \xrightarrow{a,b} 2$. Run the [subset construction](/subset-construction/) on $N$, building only reachable subsets. List the subsets, the accepting ones, and the moves between them. What language does $N$ accept?

3. ◦ An [epsilon-NFA](/epsilon-nfa/) has states $1, \ldots, 5$, start state 1, the $\varepsilon$-moves $1 \to 2$, $2 \to 3$, $3 \to 1$ and $3 \to 4$, and the $a$-moves $1 \to 5$ and $4 \to 5$. Compute the [epsilon-closures](/epsilon-closure/) $E(\{1\})$, $E(\{2\})$ and $E(\{4\})$, and the set of active states after the input $a$.

4. ◦ $A$ is the two-state DFA for "the number of $a$s is even" and $B$ the three-state DFA for "the number of $b$s is divisible by 3", both over $\{a, b\}$. How many states of the [product](/product-construction/) are reachable? How many pairs are accepting for the intersection, for the union, and for the symmetric difference?

5. ◦ A DFA over $\{a, b\}$ has states $0, 1, 2, 3$, start state 0, accepting state 2, and the moves $0 \xrightarrow{a} 1$, $0 \xrightarrow{b} 3$, $1 \xrightarrow{a} 2$, $1 \xrightarrow{b} 3$, and $2 \xrightarrow{a,b} 3$, $3 \xrightarrow{a,b} 3$. Is its language empty? Is it finite? Its graph has a cycle; why does the cycle not make the language infinite?

6. ◦ Let $L$ be the set of strings over $\{a, b\}$ that end in $ab$. Describe the classes of the [Myhill-Nerode relation](/myhill-nerode-relation/) of $L$. How many states has the minimal complete DFA?

7. ◦ A DFA over $\{a, b\}$ has states $0, \ldots, 4$, start state 0, accepting state 3, and the moves $\delta(0, a) = 1$, $\delta(0, b) = 2$, $\delta(1, a) = 0$, $\delta(1, b) = 4$, $\delta(2, a) = 3$, $\delta(2, b) = 4$, $\delta(3, a) = 1$, $\delta(3, b) = 2$, $\delta(4, a) = 3$ and $\delta(4, b) = 2$. Run [Moore's algorithm](/moore-minimization/). Give the partition after each round and the number of states of the minimal DFA. What language does the DFA accept?

8. ◦ The DFA $M_1$ of the [DFA](/deterministic-finite-automaton/) entry accepts the binary strings with an even number of 1s and has $p = 2$ states. Apply the proof of the [pumping lemma](/pumping-lemma-for-regular-languages/) to $w = 1001$: which split $w = xyz$ does the proof produce?

9. ◦ $A$ accepts the strings over $\{a, b\}$ with an even number of $a$s, and $B$ accepts the empty string and the strings that end in $b$. Give all shortest strings on which $A$ and $B$ disagree, as a search of the product for [DFA equivalence](/dfa-equivalence/) would find them.

10. • Show that the binary strings with as many occurrences of $01$ as of $10$ form a regular language, and give its minimal complete DFA. How many states does it have?

11. • Prove that $\{a^i b^j : i \ne j\}$ is not regular, using closure properties and a language whose non-regularity you know. Then prove that $\{ww : w \in \{a, b\}^*\}$ is not regular by giving infinitely many pairwise distinguishable strings.

12. • Given a DFA $M$ with $n$ states and a number $\ell$, compute the number of strings of length $\ell$ that $M$ accepts in $O(\ell \sigma n)$ arithmetic operations. Apply your method to the DFA of Exercise 1 and find a closed form.

13. • For a language $L$ let $\mathrm{drop}(L) = \{xy : xay \in L \text{ for some symbol } a\}$. Show that if a DFA with $n$ states accepts $L$, then an NFA with $2n$ states accepts $\mathrm{drop}(L)$.

14. • A machine reads bits and, after each bit, outputs 1 if the bit equals the previous bit and 0 otherwise (0 after the first bit). Give a [Mealy machine](/mealy-machine/) with three states for it, and show that the smallest [Moore machine](/moore-machine/) needs five states (drop the Moore machine's first output when you compare).

15. • Let $L = \{a^k : 3 \mid k \text{ or } 5 \mid k\}$. How many states has the minimal DFA of $L$? Give an NFA for $L$ with at most 9 states.

16. • The DFA $M_2$ of the [DFA](/deterministic-finite-automaton/) entry reads a binary number with the most significant bit first and accepts the multiples of 3. Show that the same DFA accepts exactly the strings that are multiples of 3 when read with the *least* significant bit first. Does the same trick work for the DFA of multiples of 5?

17. • Show that swapping the accepting and non-accepting states of an [NFA](/nondeterministic-finite-automaton/) need not give its complement: find an NFA with two states over $\{a\}$ where it fails. Why does the [product construction](/product-construction/) for intersection still work on NFAs?

18. • Give an algorithm that decides whether $L(A) \subseteq L(B)$ for DFAs $A$ and $B$ with $n_A$ and $n_B$ states, and that returns a string of $L(A) \setminus L(B)$ when the answer is no. What is its running time?

19. • Show that if $L$ is regular, so are the set of prefixes and the set of suffixes of strings of $L$. For prefixes, change only the accepting states of a DFA for $L$; which states become accepting?

20. • Prove that a regular language $L$ and its complement have minimal complete DFAs with the same number of states. Does the same hold for minimal *partial* DFAs?

21. ★ Let $\mathrm{half}(L) = \{x : xy \in L \text{ for some } y \text{ with } |y| = |x|\}$. Prove that if $L$ is regular, so is $\mathrm{half}(L)$.

22. ★ For distinct primes $p_1, \ldots, p_k$, build an NFA over $\{a\}$ with $1 + p_1 + \cdots + p_k$ states whose shortest rejected string has length $p_1 p_2 \cdots p_k$. Use it to explain why searching for a rejected string of an NFA by trying lengths in order is hopeless, and relate it to [NFA universality](/nfa-universality/).

23. ★ Compute the [syntactic monoid](/syntactic-monoid/) of the language of strings over $\{a, b\}$ that contain $ab$. Show that it has five elements and is aperiodic, and give a star-free expression for the language, as [Schützenberger's theorem](/schutzenberger-theorem/) predicts.

24. ★ Show that [Moore's algorithm](/moore-minimization/) on a DFA with $n \ge 2$ states performs at most $n - 2$ rounds that split some block before the round that splits nothing. Give, for each $n \ge 2$, a DFA over one letter that needs exactly $n - 2$ such rounds.
