## What to remember

- A **regular expression** is built from symbols, $\varepsilon$ and $\emptyset$ with union, concatenation and star, and it denotes exactly the regular languages. The extra operators of POSIX syntax, such as `+`, `?`, classes and `{i,j}`, are shorthands. [Backreferences](/backreference/) are not: they leave the regular languages.
- **Expression to automaton is cheap.** [Thompson's construction](/thompson-construction/) gives an epsilon-NFA with at most $2m$ states in $\Theta(m)$ time, and the [Glushkov automaton](/glushkov-automaton/) gives an NFA without $\varepsilon$-moves and with $k + 1$ states, one per symbol occurrence. The DFA can need $2^n$ states for an expression of size $4n + 2$, so engines do not build it ahead of time.
- **Automaton to expression is expensive.** [State elimination](/state-elimination/) and [Arden's lemma](/arden-lemma/) always work, but the expression can be exponentially larger than the automaton, and for some automata it must be.
- **Matching takes $O(mn)$ time with automata.** [Thompson's NFA simulation](/thompson-nfa-simulation/) keeps the set of active states and never takes longer, whatever the pattern. Under SETH, no algorithm is polynomially faster ([Backurs and Indyk](/backurs-indyk-regex-hardness/)).
- **Backtracking is exponential in the worst case.** It is the engine of Perl, Python, Java and JavaScript because it handles backreferences and lookaround. Ambiguous patterns such as $(a \mid aa)^*$ make it slow, and that is what [ReDoS](/redos/) attacks exploit.
- **A match is more than yes or no.** Searches and capture groups need a rule that picks one of many matches: leftmost-first in Perl-style engines, leftmost-longest in [POSIX](/posix-regex-semantics/). The [Pike VM](/pike-vm/) gives leftmost-first submatches in $O(mnc)$ time.
- **Questions about two expressions are hard.** [Equivalence](/regex-equivalence/), inclusion and universality are PSPACE-complete, while emptiness takes linear time. [Derivatives](/regex-derivative/) and [Kleene algebra](/kleene-algebra/) give ways to compare expressions without building DFAs first.

## The main algorithms side by side

| Task | Method | Time | Note |
|---|---|---|---|
| Expression to epsilon-NFA | [Thompson](/thompson-construction/) | $\Theta(m)$ | at most $2m$ states and $4m$ moves |
| Expression to NFA | [Glushkov](/glushkov-automaton/) | $O(m k^2)$ | $k + 1$ states, no $\varepsilon$-moves |
| Automaton to expression | [State elimination](/state-elimination/) | $O(n^3 + t)$ | with shared labels; written out, exponential |
| Match a string | [Thompson's simulation](/thompson-nfa-simulation/) | $O(mn)$ | $\Theta(m)$ space; no bad patterns |
| Print matching lines | [grep](/grep/) | $O(m(N + 1))$ | adds the start state at each character |
| Match a string | [Lazy DFA](/lazy-dfa-construction/) | $O(mn)$ | $O(k(m + s))$ space; usually one lookup per symbol |
| Match a string | [Derivatives](/brzozowski-derivatives/) | $O(m + nd)$ expected | supports intersection and complement |
| Match a string | [Partial derivatives](/antimirov-derivatives/) | $O(s m k^2 + n k^2)$ expected | at most $k + 1$ states |
| Match, one-unambiguous expression | [One-pass](/one-pass-regex-matching/) | $O(m k^2 + n)$ | one state, one lookup per symbol |
| Leftmost-first submatches | [Pike VM](/pike-vm/) | $O(mnc)$ | same groups as backtracking when no star body is nullable |
| Match with backreferences | [Backtracking](/backtracking-regex-matching/) | $2^{O(m^2 n)}$ | NP-complete in general |

: The main algorithms of the chapter. Here $m$ is the size of the expression, $k$ the number of symbol occurrences in it, $s$ the number of distinct symbols, $n$ the length of the text, $N$ the total length of the input lines, $c$ the number of capture groups, $t$ the number of moves of the automaton, $d$ the largest size of a normalized derivative, and $k$ in the lazy DFA row the cache capacity in states.

## Choosing an engine

- If patterns come from users or from the network, use an automaton engine such as Thompson's simulation, a lazy DFA or the Pike VM. They take $O(mn)$ time on every input and cannot be attacked by ReDoS.
- If you need backreferences, you need backtracking, and you should bound its running time or reject ambiguous patterns with an [ambiguity check](/regex-ambiguity-detection/).
- For a fixed pattern run over a lot of text, a lazy DFA is the fastest general choice: after warm-up it costs about one table lookup per character. Watch the cache when the pattern has large [bounded repetitions](/bounded-repetition/).
- Decide early whether you want POSIX or Perl-style matches. The two agree on whether a text matches, but they often report different spans and different groups.
- To test whether two patterns mean the same thing, build their automata and compare them; expect exponential time on bad inputs, and stop the search at the first counterexample.
