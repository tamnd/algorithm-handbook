Multiple pattern matching searches one text for many patterns at once. A virus scanner checks every file against tens of thousands of byte signatures; a network intrusion detector checks every packet against its rule set; a spam filter looks for a list of phrases; `grep -F` with a file of words does the same on the command line. Running a single-pattern matcher once per pattern costs time proportional to the number of patterns times the length of the text. The methods of this chapter read the text once, whatever the number of patterns.

The central algorithm is [Aho-Corasick](/aho-corasick/). It places the patterns in a [trie](/trie/) and adds to each node a [failure link](/failure-link/), so that the trie becomes an automaton that follows the text one character at a time and never moves back. It runs in $O(n + m + z)$ time for a text of length $n$, patterns of total length $m$ and $z$ occurrences, and this is optimal. The rest of the chapter trades this guarantee for speed in practice, by skipping parts of the text as Boyer-Moore does, or extends the problem to a dictionary that changes and to two dimensions.

## What the chapter covers

The chapter is in five groups, read in order.

1. **The problem.** [Multiple string matching](/multiple-string-matching/) defined, and why its bounds must be [output-sensitive](/output-sensitive-matching/): the number of occurrences alone can be $\Theta(nk)$ for $k$ patterns. [Karp-Rabin for many patterns](/karp-rabin-multiple-patterns/) is the shortest correct solution when the patterns have one length.
2. **The Aho-Corasick automaton.** The [failure link](/failure-link/) as the prefix function of a trie, the algorithm itself, and the [dictionary suffix link](/dictionary-suffix-link/) that makes reporting cost one step per occurrence.
3. **Skipping text.** [Commentz-Walter](/commentz-walter/), [Set Horspool](/set-horspool/) and [Wu-Manber](/wu-manber/), with its [block shift table](/block-shift-table/). These carry the right-to-left reading of Boyer-Moore over to a set of patterns.
4. **A fixed dictionary.** [Dictionary matching](/dictionary-matching/), where the patterns are preprocessed once for many texts, and its [dynamic](/dynamic-dictionary-matching/) form, where patterns come and go.
5. **Two dimensions.** [Two-dimensional dictionary matching](/two-dimensional-dictionary-matching/) and the [Bird-Baker](/bird-baker/) method, which names the rows of the patterns and then matches columns.

## A first reading

For a first reading, take these seven entries in order: [multiple string matching](/multiple-string-matching/), [output-sensitive matching](/output-sensitive-matching/), [failure link](/failure-link/), [Aho-Corasick](/aho-corasick/), [dictionary suffix link](/dictionary-suffix-link/), [Set Horspool](/set-horspool/) and [Wu-Manber](/wu-manber/). The first five give the complete theory of the problem; the last two show why practical tools often use a different method. Commentz-Walter, the hashing method and the last two groups can wait.

## Before you start

You need [Knuth-Morris-Pratt](/knuth-morris-pratt/) and the [prefix function](/prefix-function/) from Chapter 8.1, since Aho-Corasick is their generalization, and [Horspool](/boyer-moore-horspool/) and [Boyer-Moore](/boyer-moore/) for the third group. From Volume 3 you need the [trie](/trie/) and the [hash table](/hash-table/). The hashing method uses [Rabin-Karp](/rabin-karp/) and the [polynomial rolling hash](/polynomial-rolling-hash/) from Chapter 8.6. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
