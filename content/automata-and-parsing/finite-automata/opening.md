A finite automaton is the simplest machine that computes anything at all. It reads a string one symbol at a time, from left to right, and remembers only which of a fixed, finite set of states it is in. When the input ends, it says yes or no. That is all. Yet this machine is everywhere: the lexer of a compiler is a finite automaton, so is the matcher behind `grep`, the checker of a network protocol, and the controller of a traffic light or a vending machine. When a model checker verifies that a system never deadlocks, it builds automata and asks whether their product accepts anything.

The languages that finite automata accept are the [regular languages](/regular-language/). The chapter studies them from three sides: the machines themselves and how to convert between them, the questions one can ask about a machine and how fast they can be answered, and the structure of the class, which turns out to have a unique smallest machine for each language.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **Machines and their languages.** The [deterministic finite automaton](/deterministic-finite-automaton/), the [nondeterministic](/nondeterministic-finite-automaton/) one, and the [epsilon-NFA](/epsilon-nfa/), with [Kleene's theorem](/kleene-theorem/) showing that they and regular expressions describe one class.
2. **Running and determinizing an NFA.** [NFA simulation](/nfa-simulation/) follows the set of active states in $O(\ell(n + m))$ time. The [subset construction](/subset-construction/) builds the whole DFA, with up to $2^n$ states.
3. **Building new automata from old.** The [product construction](/product-construction/), the [closure properties](/closure-properties-of-regular-languages/) it proves, and the [pumping lemma](/pumping-lemma-for-regular-languages/) for proving that a language is not regular.
4. **Questions about a DFA.** [Emptiness](/dfa-emptiness/), [finiteness](/dfa-finiteness/) and [equivalence](/dfa-equivalence/), each a search in the transition graph.
5. **The minimal DFA.** The [Myhill-Nerode theorem](/myhill-nerode-theorem/) and the algorithms of [DFA minimization](/dfa-minimization/), with [Hopcroft's algorithm](/hopcroft-minimization/) at $O(\sigma n \log n)$.
6. **Size, and what nondeterminism costs.** The [blow-up lower bound](/determinization-blowup-lower-bound/), and the PSPACE-hardness of [NFA universality](/nfa-universality/), equivalence and minimization.
7. **Automata with output.** [Moore](/moore-machine/) and [Mealy machines](/mealy-machine/), [transducers](/finite-state-transducer/) and [weighted automata](/weighted-automaton/).
8. **Other kinds of finite automata.** Unambiguous, alternating, two-way and probabilistic automata, and the [Büchi automaton](/buchi-automaton/) on infinite words.
9. **The algebra of regular languages.** The [syntactic monoid](/syntactic-monoid/), star-free languages and [Schützenberger's theorem](/schutzenberger-theorem/).
10. **Learning automata.** [DFA learning](/dfa-learning/) and Angluin's [L* algorithm](/lstar-algorithm/).

## A first reading

For a first reading, take these fourteen entries in order: [deterministic finite automaton](/deterministic-finite-automaton/), [regular language](/regular-language/), [nondeterministic finite automaton](/nondeterministic-finite-automaton/), [epsilon-NFA](/epsilon-nfa/), [epsilon-closure](/epsilon-closure/), [NFA simulation](/nfa-simulation/), [subset construction](/subset-construction/), [Kleene's theorem](/kleene-theorem/), [product construction](/product-construction/), [closure properties](/closure-properties-of-regular-languages/), [pumping lemma](/pumping-lemma-for-regular-languages/), [DFA emptiness](/dfa-emptiness/), [Myhill-Nerode theorem](/myhill-nerode-theorem/) and [Hopcroft's algorithm](/hopcroft-minimization/). Kleene's theorem uses [regular expressions](/regular-expression/), defined at the start of Chapter 9.2; read that entry when you reach it. Groups 7 to 10 can wait until the rest of the volume is done; group 6 is worth reading early, since it explains why regular expression engines avoid building full DFAs.

## Before you start

An automaton is a labelled [directed graph](/directed-graph/), and most algorithms here are graph searches: you need [graph reachability](/graph-reachability/), [breadth-first search](/breadth-first-search/) and [depth-first search](/depth-first-search/) from Volume 7. The minimization algorithms use [partition refinement](/partition-refinement/), and the Hopcroft-Karp test uses the [disjoint-set](/disjoint-set/) structure. Strings and alphabets are defined in [alphabet](/alphabet/). The proofs use induction on the length of a string and the [pigeonhole principle](/pigeonhole-principle/). The hardness results of group 6 assume [PSPACE](/pspace/) from the volume on complexity. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
