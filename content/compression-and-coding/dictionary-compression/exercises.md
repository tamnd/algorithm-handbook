1. ◦ Parse `abcabcabcd` with greedy [LZ77](/lz77/) into triples $(d, \ell, c)$, with an unbounded window and $(0, 0, c)$ for a symbol with no copy. How many symbols does the last copy read that it writes itself?

2. ◦ Give the [LZ78](/lz78/) pairs and the [LZW](/lzw/) codes for `aababcabcd`, with LZW starting from the 256 byte values and new codes from 256. How many bits do the LZW codes take at a width of 9 bits, against the 80 bits of the input?

3. ◦ An LZW decoder that starts with the 256 byte values and adds codes from 256 receives 97, 256, 257, 97. What text does it write? How many times does it receive a code that is not yet in its table?

4. ◦ Compute the [longest previous factor](/longest-previous-factor/) array of `aabaabab` (copies may overlap their target), and from it the [Lempel-Ziv factorization](/lempel-ziv-factorization/).

5. ◦ Use the [LZSS](/lzss/) costs of a flag bit plus 8 bits for a literal and a flag bit plus 16 bits for a copy, with lengths 2 to 17. How many bits does greedy LZSS write for 100 copies of `a`? What does the ratio of output to input bits tend to for long runs?

6. ◦ With the costs of the previous exercise, the window holds `xabcybcdefz` and the next six symbols are `abcdef`. How many bits do greedy parsing and one-step [lazy matching](/lazy-matching/) spend on those six symbols?

7. ◦ Write the [Snappy](/snappy/) preamble for an input of 300 bytes. Which element and how many bytes does Snappy need for a copy of length 10 at offset 1000, for one of length 10 at offset 3000, and, at least, for one of length 70 at offset 1000?

8. ◦ An [LZMA](/lzma/) stream uses $lc = 0$, $lp = 2$, $pb = 2$. What is its property byte? How many literal probability tables does the decoder keep, and how many probabilities do they hold in all?

9. ◦ Run [Re-Pair](/re-pair/) on $(ab)^8$, the string of 16 symbols. Give the rules and the size of the grammar, counted as two per rule plus the length of the final string.

10. • Let $D = \lbrace a, b, c, ab, bca \rbrace$, each phrase with cost 1, and $T$ = `abcabca`. Parse $T$ greedily. Then compute $C[i]$, the fewest phrases for the suffix from position $i$, for $i = 7, 6, \ldots, 0$, and give an optimal parse.

11. • A dictionary is prefix-closed when each prefix of a phrase is a phrase. Give, for each $k \ge 1$, a prefix-closed dictionary that contains each single symbol and a text on which greedy parsing uses $k + 1$ phrases and the optimal parse uses 2. So the ratio of greedy to optimal is unbounded, even for prefix-closed dictionaries.

12. • Show that the $k$-th phrase of an [LZ78 parse](/lz78-parsing/) has length at most $k$, and deduce that a string of length $n$ has at least $(\sqrt{8n + 1} - 1)/2$ phrases. How many LZ78 phrases and how many LZW codes does $a^{100}$ give?

13. • An LZ78 coder writes pair $k$ with $\lceil \log_2 k \rceil$ bits for the index and 8 bits for the symbol. Show that it spends $\Theta(\sqrt{n} \log n)$ bits on $a^n$, while one literal and the single copy $(1, n - 1)$, with both numbers in [Elias gamma code](/elias-gamma-coding/), take $O(\log n)$ bits.

14. • In one [DEFLATE](/deflate/) block with the fixed codes, count the bits for 259 copies of `a`, including the 3 header bits and the end-of-block code. Then show that 517 copies cost fewer bits than 516, and find both numbers.

15. • A [straight-line program](/straight-line-program-grammar/) in Chomsky normal form has rules $X \to YZ$ and $X \to a$. Find the fewest rules for $a^{15}$, and prove that fewer are impossible. Compare with the bound $n \le 2^{m - 1}$ for $m$ rules.

16. • Show that the longest previous factor array satisfies $\mathrm{LPF}[i + 1] \ge \mathrm{LPF}[i] - 1$. Give, for each $n$, a string of length $n$ on which equality holds at every $i \ge 1$.

17. • An input of 1000 bytes contains no 4-byte string twice. How many bytes do an [LZ4](/lz4/) block and a Snappy stream take for it?

18. • Show that the Lempel-Ziv factorization of $(ab)^m$, $m \ge 2$, has 3 factors when copies may overlap their target. How many factors does the factorization without self-reference have for $(ab)^{2^k}$?

19. • Write all binary strings of length 1, then of length 2, and so on up to length $k$, each length in lexicographic order, one after another. Show that the LZ78 parse of the result has exactly those strings as phrases, give its length $n$ and its number of phrases $c$, and show that $c \log_2 c / n \to 1$ as $k \to \infty$.

20. ★ Show that the LZ78 parse of every string of length $n$ over $\sigma \ge 2$ symbols has $c = O(n / \log_\sigma n)$ phrases.

21. ★ Show that, for every large $n$, more than half of the binary strings of length $n$ have a Lempel-Ziv factorization with more than $n / (3 \log_2 n)$ factors. Together with the previous exercise and $z \le 2c$, what does this say about the factor count of a typical string?

22. ★ A [string attractor](/string-attractor/) of $T$ is a set $\Gamma$ of positions such that each substring of $T$ has an occurrence that contains a position of $\Gamma$. Show that the last positions of the factors of the Lempel-Ziv factorization form a string attractor, so the smallest attractor has at most $z$ positions.

23. ★ Use the previous exercise to show that $T$ has at most $\ell z$ distinct substrings of length $\ell$. Give a string on which the bound is reached for $\ell = 1$.

24. ★ The size of a grammar is the total length of its right-hand sides. Show that a grammar of size $g$ that derives one string of length $n$ has $n \le 3^{g/3}$. Deduce the size of a smallest grammar for $a^{3^k}$.
