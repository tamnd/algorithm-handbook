## What to remember

- A **DFA** has exactly one next state for each state and symbol, reads its input once, and keeps only its current state. It decides membership of a string of length $\ell$ in $\ell$ steps. The languages of DFAs are the **regular languages**.
- **NFAs and epsilon-NFAs** accept the same class. The [subset construction](/subset-construction/) turns $n$ states into at most $2^n$, and the [lower bound](/determinization-blowup-lower-bound/) shows that $2^n$ is sometimes needed. To run an NFA on one input, do not determinize: [simulate](/nfa-simulation/) the set of active states in $O(\ell(n + m))$ time and $O(n)$ space.
- **Kleene's theorem**: regular expressions, DFAs, NFAs and epsilon-NFAs describe exactly the same languages, and each conversion is an algorithm.
- **Closure.** Regular languages are closed under union, intersection, complement, concatenation, star, reversal, homomorphism and inverse homomorphism. The [product construction](/product-construction/) gives the Boolean operations with $n_1 n_2$ states. Complement a DFA by swapping accepting and rejecting states, but only when the DFA is complete; swapping fails for an NFA.
- **Non-regularity** is proved with the [pumping lemma](/pumping-lemma-for-regular-languages/) or, more exactly, by finding infinitely many pairwise distinguishable strings.
- **Myhill-Nerode.** $L$ is regular if and only if $\equiv_L$ has finitely many classes, and the number of classes is the number of states of the unique minimal complete DFA. Every minimization algorithm computes these classes by refining a partition.
- **DFA questions are graph searches.** Emptiness and finiteness take $O(\sigma n)$ time, and equivalence takes $O(\sigma n\, \alpha(n))$ time with [Hopcroft-Karp](/hopcroft-karp-equivalence/). For NFAs, universality and equivalence are PSPACE-complete, and so is the decision version of minimization.

## The main algorithms side by side

| Task | Method | Time | Note |
|---|---|---|---|
| Run an NFA on a string | [NFA simulation](/nfa-simulation/) | $O(\ell(n + m))$ | $O(n)$ extra space |
| NFA to DFA | [Subset construction](/subset-construction/) | $O(2^n \sigma (n + m))$ | up to $2^n$ states, which can be needed |
| Intersection, union | [Product construction](/product-construction/) | $O(n k \sigma)$ | $nk$ states, which can be needed |
| Is $L(M)$ empty? | [DFA emptiness](/dfa-emptiness/) | $O(n \sigma)$ | reachability of an accepting state |
| Is $L(M)$ finite? | [DFA finiteness](/dfa-finiteness/) | $O(n \sigma)$ | a cycle among the useful states |
| Same language? | [Hopcroft-Karp](/hopcroft-karp-equivalence/) | $O(\sigma n\, \alpha(n))$ | gives a counterexample when "no" |
| Minimize | [Table filling](/table-filling-minimization/) | $O(\sigma n^2)$ | $O(\sigma n^2)$ space; distinguishing strings |
| Minimize | [Moore](/moore-minimization/) | $O(\sigma n^2)$ | few rounds on typical inputs |
| Minimize | [Hopcroft](/hopcroft-minimization/) | $O(\sigma n \log n)$ | best worst-case bound known |
| Minimize | [Brzozowski](/brzozowski-minimization/) | $O(\sigma 4^n)$ | works on NFAs; often fast in practice |
| Is $L(N) = \Sigma^*$? | [NFA universality](/nfa-universality/) | $O(2^n \sigma (n + m))$ | PSPACE-complete |
| Same language, NFAs | [NFA equivalence](/nfa-equivalence/) | $O(2^n \sigma (n + m))$ | PSPACE-complete |

: The main algorithms of the chapter. Here $\ell$ is the length of the input, $n$ and $k$ are numbers of states, $m$ is the number of NFA transitions, $\sigma$ is the size of the alphabet and $\alpha$ is the inverse Ackermann function. For NFA equivalence, $n$ and $m$ count both automata.

## Choosing a representation

- To match one string, or many strings against a pattern that changes often, keep the NFA and simulate it. Build the DFA only when the same automaton runs over a lot of input, and then build it lazily, state by state, as [lazy DFA construction](/lazy-dfa-construction/) does.
- To test equality, inclusion or emptiness, work with DFAs when you have them. If you only have NFAs, expect exponential worst cases, and determinize on the fly so that the search can stop early.
- To compare two languages often, or to store them, minimize first: the minimal DFA is a canonical form, so equal languages give equal machines up to renaming.
- For minimization in code, Hopcroft's algorithm is the safe choice. Moore's algorithm is shorter and usually fast; the table-filling algorithm is the easiest to prove and to explain.
