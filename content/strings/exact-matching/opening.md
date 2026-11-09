Exact string matching is the problem of finding every place where a pattern occurs in a text, letter for letter. It is the search command of every text editor, the core of tools such as `grep`, and the inner loop of the C library function `strstr`. A virus scanner looks for known byte strings in a file; a biologist looks for a short DNA motif in a genome. The problem is easy to state and easy to solve slowly. The interest lies in solving it in time $\Theta(n + m)$ for a text of length $n$ and a pattern of length $m$, or in reading only a fraction of the text.

The chapter holds the classic answers. They fall into two families that read the text in opposite directions. The left-to-right family, led by [Knuth-Morris-Pratt](/knuth-morris-pratt/), never moves back in the text and guarantees linear time. The right-to-left family, led by [Boyer-Moore](/boyer-moore/), compares the pattern from its end and can skip most of the text on large alphabets. Both families depend on what the pattern says about itself: its [borders](/border/) and its [periods](/string-period/).

## What the chapter covers

The chapter is in seven groups, read in order.

1. **The problem and the baseline.** [String matching](/string-matching/) defined precisely, its $\Omega(n + m)$ lower bound, and [naive matching](/naive-string-matching/), which takes $\Theta((n - m + 1)m)$ time in the worst case but $O(n)$ on average. A [spurious hit](/spurious-hit/) is the false alarm of hash-based matching.
2. **Tables of the pattern.** The [prefix function](/prefix-function/) and the [Z-algorithm](/z-algorithm/), each computed in linear time, each enough to match in linear time.
3. **Scanning left to right.** The [string-matching automaton](/string-matching-automaton/), [Morris-Pratt](/morris-pratt/), Knuth-Morris-Pratt and the bit-parallel [Shift-Or](/shift-or/).
4. **Scanning right to left.** The [bad-character rule](/bad-character-rule/), the [good-suffix rule](/good-suffix-rule/), Boyer-Moore and its two simple forms, [Horspool](/boyer-moore-horspool/) and [Quick Search](/quick-search/), which are the fastest exact matchers in practice on natural text.
5. **Boyer-Moore with guarantees.** The [Galil rule](/galil-rule/), [Cole's bound](/boyer-moore-comparison-bound/) of about $3n$ comparisons, [Turbo-BM](/turbo-boyer-moore/), [Apostolico-Giancarlo](/apostolico-giancarlo/), and [backward DAWG matching](/backward-dawg-matching/), which is optimal on average.
6. **Linear time in constant space.** [Galil-Seiferas](/galil-seiferas/) and the [two-way algorithm](/two-way-string-matching/), which glibc uses for `strstr`.
7. **Other kinds of match.** [Rotations of the pattern](/circular-pattern-matching/), [order-preserving](/order-preserving-matching/) and [parameterized](/parameterized-pattern-matching/) matching, and [matching in compressed text](/pattern-matching-in-compressed-text/).

## A first reading

For a first reading, take these eleven entries in order: [string matching](/string-matching/), [naive string matching](/naive-string-matching/), [the prefix function](/prefix-function/), [Knuth-Morris-Pratt](/knuth-morris-pratt/), [the Z-algorithm](/z-algorithm/), [the string-matching automaton](/string-matching-automaton/), [the bad-character rule](/bad-character-rule/), [the good-suffix rule](/good-suffix-rule/), [Boyer-Moore](/boyer-moore/), [Horspool](/boyer-moore-horspool/) and [Shift-Or](/shift-or/). Add [Rabin-Karp](/rabin-karp/) from Chapter 8.6, the third classic approach, and its [spurious hits](/spurious-hit/). Morris-Pratt can be read as a simpler first version of Knuth-Morris-Pratt. Groups 5 to 7 can wait: they matter when you need a worst-case guarantee from a Boyer-Moore matcher, constant extra space, or a different notion of match.

## Before you start

You need [asymptotic notation](/asymptotic-notation/) and [loop invariants](/loop-invariant/) from Volume 1, and the [potential method](/potential-method/) of amortized analysis for the linear bounds of Knuth-Morris-Pratt and the prefix function. For the automaton you need [deterministic finite automata](/deterministic-finite-automaton/) from Volume 9; for Shift-Or, [bit-parallelism](/bit-parallelism/) and the [word RAM](/word-ram/). From Chapter 8.7 of this volume you need the [alphabet](/alphabet/), the [border](/border/) and the [period](/string-period/) of a string: read those three short entries first if the words are new. The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
