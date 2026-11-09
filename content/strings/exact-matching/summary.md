## What to remember

- **String matching** takes $\Theta(n + m)$ time in the worst case, and no deterministic algorithm can do better: on some text it must read at least $n - m + 1$ characters (Rivest). On random text the best average is $\Theta((n/m) \log_\sigma m)$ characters read (Yao), which is sublinear for long patterns.
- **Naive matching** takes $\Theta((n - m + 1)m)$ time in the worst case, as on $T = a^n$, $P = a^{m-1}b$, but $O(n)$ on average on random text. It is still the right choice for very short patterns.
- The **prefix function** $\pi[q]$ is the length of the longest proper [border](/border/) of $P[0 \ldots q]$, and $m - \pi[m-1]$ is the smallest [period](/string-period/) of $P$. It is computed in $O(m)$ time with at most $2m$ comparisons; the [Z-array](/z-algorithm/) carries the same information in another form.
- **Knuth-Morris-Pratt** never moves back in the text and makes at most $2n$ comparisons in the search. The amortized argument is always the same: each comparison either advances the text position or shortens the current match.
- **Boyer-Moore** compares right to left and shifts by the larger of the bad-character and good-suffix shifts. Its best case reads only about $n/m$ characters, but plain Boyer-Moore takes $\Theta(nm)$ time when the pattern occurs often. The [Galil rule](/galil-rule/) makes it linear; [Cole](/boyer-moore-comparison-bound/) proved about $3n$ comparisons for non-periodic patterns.
- **Horspool** and **Quick Search** keep only the bad-character rule. Their worst case is $\Theta(nm)$, but on natural text and large alphabets they are as fast as anything known, with a table of $\sigma$ entries.
- **Shift-Or** keeps the set of all partial matches in a bit vector and spends $\Theta(\lceil m/w \rceil)$ word operations per text character. It extends with little change to character classes and to errors.
- **Constant extra space** and linear time are possible together: [Galil-Seiferas](/galil-seiferas/) and the [two-way algorithm](/two-way-string-matching/) both use the periodicity of the pattern.

## The main algorithms side by side

| Algorithm | Worst time | Best time | Extra space | Reads text |
|---|---|---|---|---|
| [Naive](/naive-string-matching/) | $\Theta((n - m + 1)m)$ | $\Theta(n - m + 1)$ | $\Theta(1)$ | left to right |
| [Automaton](/string-matching-automaton/) | $\Theta(m\sigma + n)$ | $\Theta(m\sigma + n)$ | $\Theta(m\sigma)$ | left to right |
| [Knuth-Morris-Pratt](/knuth-morris-pratt/) | $\Theta(n + m)$ | $\Theta(n + m)$ | $\Theta(m)$ | left to right |
| [Z-algorithm](/z-algorithm/) | $\Theta(n + m)$ | $\Theta(n + m)$ | $\Theta(n + m)$ | left to right |
| [Shift-Or](/shift-or/) | $\Theta(n \lceil m/w \rceil)$ | $\Theta(n \lceil m/w \rceil)$ | $\Theta(\sigma \lceil m/w \rceil)$ | left to right |
| [Boyer-Moore](/boyer-moore/) | $\Theta(nm)$ | $\Theta(n/m + m + \sigma)$ | $\Theta(m + \sigma)$ | windows right to left |
| [Horspool](/boyer-moore-horspool/) | $\Theta(nm)$ | $\Theta(n/m + m + \sigma)$ | $\Theta(\sigma)$ | windows |
| [Turbo-BM](/turbo-boyer-moore/) | $O(n + m + \sigma)$ | $\Theta(n/m + m + \sigma)$ | $\Theta(m + \sigma)$ | windows right to left |
| [Backward DAWG](/backward-dawg-matching/) | $\Theta(nm)$ | $\Theta(n/m)$ | $\Theta(m)$ | windows right to left |
| [Two-way](/two-way-string-matching/) | $\Theta(n + m)$ | $\Theta(n/m + m)$ | $\Theta(1)$ | two directions |
| [Galil-Seiferas](/galil-seiferas/) | $O(n + m)$ | $\Theta(n)$ | $O(1)$ | left to right |

: Exact matchers for a text of length $n$, a pattern of length $m$, an alphabet of size $\sigma$ and a word of $w$ bits. Times include preprocessing, except for the search-only bounds of Shift-Or and backward DAWG matching, whose preprocessing is $\Theta(m + \sigma \lceil m/w \rceil)$ and $O(m)$. Backward DAWG matching reads $O(n \log_\sigma m / m)$ characters on average, which is optimal.

## Choosing a method

Use the library's search function first; good libraries already pick well. When you write your own:

- For one search with a short pattern, naive matching or Horspool is enough, and often fastest.
- For natural text, long patterns or large alphabets, use [Horspool](/boyer-moore-horspool/) or [Quick Search](/quick-search/).
- When the worst case matters, as with input chosen by an adversary, use Knuth-Morris-Pratt, or the two-way algorithm when you cannot allocate memory.
- When the text arrives as a stream and must be handled one character at a time, use Knuth-Morris-Pratt or the automaton.
- For patterns up to 64 characters, and for classes of characters, use Shift-Or.
- When many patterns are searched in the same text, or one text is searched many times, leave this chapter: see [Aho-Corasick](/aho-corasick/) in Chapter 8.2 and the [suffix array](/suffix-array/) in Chapter 8.3.
