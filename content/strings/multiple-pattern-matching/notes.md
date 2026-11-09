## History

Alfred Aho and Margaret Corasick published *Efficient string matching: an aid to bibliographic search* in the Communications of the ACM in 1975. They built the algorithm to speed up a bibliographic search program at Bell Laboratories that looked for many keywords at once. The paper defines the goto, failure and output functions, proves the linear bound, and shows how to turn the machine into a deterministic automaton. Its failure function extends that of Knuth, Morris and Pratt, whose journal paper appeared only in 1977 but had circulated before as a report. Aho's `fgrep` program for Unix used the method, and it remains the basis of virus scanners and intrusion detection systems.

The idea of skipping text came over from single-pattern matching soon after. Beate Commentz-Walter presented her algorithm at ICALP in 1979, combining the shifts of Boyer-Moore with a trie of the reversed patterns; Andrew Hume's `gre` and version 2.0 of GNU `fgrep` were based on it. Sun Wu and Udi Manber described their block-shift algorithm in a University of Arizona technical report in 1994; an earlier version was part of `agrep`, and it was the engine of the `glimpse` search tool. Gonzalo Navarro and Mathieu Raffinot, in their book of 2002, named the simplified Set Horspool algorithm and measured where each method wins.

Richard Karp and Michael Rabin introduced fingerprinting for pattern matching in a report of 1981, published in 1987; keeping the fingerprints of many patterns in a hash table is the direct extension. Two-dimensional matching is nearly as old as the one-dimensional algorithms: Richard Bird (1977) and Theodore Baker (1978) independently reduced it to string matching by naming the rows of the pattern. Amihood Amir, Gary Benson and Martin Farach later made two-dimensional matching independent of the alphabet (1994).

Research on dictionaries asked what happens when the set changes. Amir, Farach, Galil, Giancarlo and Park stated dynamic dictionary matching and solved it with a logarithmic slowdown in 1994; Ramana Idury and Alejandro Schäffer gave a solution based on failure functions the same year, and Süleyman Cenk Sahinalp and Uzi Vishkin removed the slowdown in 1996. Later work studied dictionaries in compressed space and in a stream.

## Further reading

- Alfred V. Aho and Margaret J. Corasick, *Efficient string matching: an aid to bibliographic search*, Communications of the ACM 18(6), 1975. Short and readable; the original account of the automaton.
- Gonzalo Navarro and Mathieu Raffinot, *Flexible Pattern Matching in Strings* (2002). Chapter 3 compares the prefix-, suffix- and factor-based methods for sets of patterns, with experiments that show which to use when.
- Dan Gusfield, *Algorithms on Strings, Trees, and Sequences* (1997). Section 3.4 develops Aho-Corasick with full proofs and its uses in biology.
- Maxime Crochemore, Christophe Hancart and Thierry Lecroq, *Algorithms on Strings* (2007). The dictionary automaton in the language of automata, with careful complexity analysis.
- Sun Wu and Udi Manber, *A fast algorithm for multi-pattern searching*, Technical Report TR 94-17, University of Arizona, 1994. The block-shift idea and its measurements.
