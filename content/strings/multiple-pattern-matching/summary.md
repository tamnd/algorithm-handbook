## What to remember

- **Multiple string matching** with a text of length $n$, patterns of total length $m$ and $z$ occurrences takes $\Theta(n + m + z)$ time, and [Aho-Corasick](/aho-corasick/) reaches this bound when a trie step costs $O(1)$. With children kept in sorted order it is $O((n + m)\log \sigma + z)$.
- The output can dominate: $k$ patterns can have $\Theta(nk)$ occurrences in all. A good bound is **output-sensitive**, linear in $n + m$ plus one unit per occurrence.
- A **failure link** points from a trie node to the node of its longest proper suffix in the trie. For one pattern the failure links are the [prefix function](/prefix-function/). They are computed in breadth-first order in $O(m)$ time, in the same amortized way.
- Following the failure chain at every text position can cost $\Theta(n \cdot \text{depth})$ even when there are no occurrences. The **dictionary suffix link** skips the nodes that are not patterns, so reporting costs $O(1 + \text{occurrences})$ per position.
- **Skipping algorithms** (Commentz-Walter, Set Horspool, Wu-Manber) use a window as long as the shortest pattern, so one very short pattern makes every shift small. Their worst cases are not linear, but with few or long patterns they read only part of the text.
- **Wu-Manber** shifts on blocks of $B$ characters instead of single characters. With $B$ about $\log_\sigma(2k\ell)$ for $k$ patterns cut to length $\ell$, most blocks occur in no pattern, and the shifts stay long for thousands of patterns.
- **Two-dimensional** matching of patterns of one width reduces to string matching: name the pattern rows with Aho-Corasick, then match the columns of names.

## The main algorithms side by side

| Algorithm | Worst time | Best or expected time | Extra space | Best for |
|---|---|---|---|---|
| [Aho-Corasick](/aho-corasick/) | $O(n + m + z)$ | $O(n + m + z)$ | $O(m)$ | any set, guaranteed |
| [Commentz-Walter](/commentz-walter/) | $O(nL + z)$ | $O(n/w + z)$ | $O(m)$ | few patterns |
| [Set Horspool](/set-horspool/) | $O(nL + z)$ | $O(n/\ell + z)$ | $O(m)$ | few patterns, large alphabet |
| [Wu-Manber](/wu-manber/) | $O(n(B + m))$ | $O(Bn/\ell + zL)$ expected | $O(m)$ | many long patterns |
| [Karp-Rabin](/karp-rabin-multiple-patterns/) | $O(k + m + nm + z)$ | linear expected for one length | $O(m)$ | patterns of one length |

: Multiple-pattern matchers on a text of length $n$, with $k$ patterns of total length $m$, $z$ occurrences, longest pattern length $L$ and shortest length $w$ (written $\ell$ for Set Horspool and Wu-Manber), and blocks of $B$ characters. Build times are $O(m)$ for the trie-based methods and $O(Bm)$ for Wu-Manber. The Aho-Corasick bound assumes $O(1)$ trie steps; the Karp-Rabin bound is the worst case, its expected time is linear for one pattern length plus a term for each distinct length.

## Choosing a method

- When the worst case matters, or the set is large and contains short patterns, use Aho-Corasick. It is also the right choice for a stream, since it handles each text character as it arrives.
- For a handful of patterns over a large alphabet, such as words in natural text, Set Horspool reads much less of the text.
- For thousands of patterns none of which is very short, Wu-Manber is among the fastest in practice.
- When all patterns have the same length, as for $k$-mers in a genome or fixed-size signatures, a hash table of fingerprints is the simplest correct method.
- When the dictionary is fixed and the texts arrive later, build the Aho-Corasick automaton once; when patterns are added and removed, see [dynamic dictionary matching](/dynamic-dictionary-matching/).
