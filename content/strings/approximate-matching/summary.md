## What to remember

- The **edit distance** of two strings is the least number of insertions, deletions and substitutions that turn one into the other. It is a metric, and the Wagner-Fischer table computes it in $\Theta(mn)$ time and, for the distance alone, $O(\min(m, n))$ space.
- Under the Strong Exponential Time Hypothesis, no algorithm computes the edit distance in time $O(n^{2-\varepsilon})$. Faster methods win by using a small $k$, a short pattern, or the structure of typical inputs.
- **Sellers' algorithm** is the Wagner-Fischer table with the first row set to zero, so that a match can start anywhere. It reports the end positions of all approximate occurrences in $\Theta(mn)$ time and reads the text once.
- **The k-mismatch problem** allows substitutions only, so every match has length $m$. **The k-differences problem** allows all three edits. Methods for one do not always carry over to the other.
- The values along a diagonal of the table never decrease, and neighboring cells differ by at most 1. The first fact gives the **diagonal methods** with longest common extensions in $O(kn)$ time; the second lets **bit-parallel** methods store a column in two bit vectors.
- **Filters** rest on counting: with $k$ errors, one of $k + 1$ pieces of the pattern survives exactly, and at least $m - q + 1 - kq$ of its q-grams survive. A filter never loses a match; its speed depends on how much text it rules out.
- A **phonetic code** such as Soundex compares names by key, not by distance: it finds spellings that sound alike and misses typing errors that change the first letter.

## The main algorithms side by side

| Algorithm | Problem | Worst time | Expected or typical time | Notes |
|---|---|---|---|---|
| [Sellers](/sellers-algorithm/) | k-differences | $\Theta(mn)$ | $\Theta(mn)$ | simplest, any costs |
| [Ukkonen cut-off](/ukkonen-cutoff-algorithm/) | k-differences | $\Theta(mn)$ | $O(kn)$ on random text | a small change to Sellers |
| [Myers bit-parallel](/myers-bit-parallel-algorithm/) | k-differences | $O(\lceil m/w \rceil n)$ | same | fastest for $m \le w$ |
| [Wu-Manber](/wu-manber-approximate-matching/) | k-differences | $O((k+1)\lceil m/w \rceil n)$ | same | basis of `agrep` |
| [Landau-Vishkin](/landau-vishkin-algorithm/) | k-differences | $O(kn)$ | same | needs LCE queries |
| [Fischer-Paterson](/fischer-paterson-algorithm/) | all Hamming distances | $O(\sigma n \log m)$ | same | small alphabets |
| [Amir-Lewenstein-Porat](/amir-lewenstein-porat-algorithm/) | k-mismatch | $O(n\sqrt{k \log k})$ | same | any alphabet |
| [Pigeonhole filter](/pigeonhole-filtering/) | k-differences | as the verifier | near $O(n)$ for small $k/m$ | pieces searched exactly |

: Approximate matching of a pattern of length $m$ in a text of length $n$ with at most $k$ errors, on a word RAM with $w$-bit words and an alphabet of $\sigma$ symbols. The times omit preprocessing of the pattern, which is $O(m)$ to $O(m^2)$, and the Landau-Vishkin bound counts the $O(n + m)$ time to build the LCE structure.

## Choosing a method

- To compare two strings, use the Wagner-Fischer table, or Myers' bit vectors when one string is at most a few words long.
- To search a text for a short pattern with errors, use Myers' algorithm or Wu-Manber; both are short to write and fast in practice.
- For a long pattern and a small error rate, filter first: search the $k + 1$ pieces with Aho-Corasick, or count q-grams, and verify the candidate regions with Sellers.
- For substitutions only over a small alphabet, such as DNA, compute all Hamming distances with one convolution per symbol.
- To correct words against a dictionary, walk a trie of the dictionary with a Levenshtein automaton, or with the rows of the table, and stop each branch once every entry exceeds $k$.
- For names, use a phonetic code such as Soundex or Metaphone, often together with a small edit distance on the codes.
