1. It detects 5 errors, corrects 2 and fills in 5 erasures. Two errors and one erasure work, because $2 \cdot 2 + 1 = 5 < 6$. Correcting $t'$ and detecting $s$ needs $t' + s < d$, so the pairs are $(0, 5)$, $(1, 4)$ and $(2, 3)$.

3. The ones are in positions 1, 2, 4, 5 and 6, and $1 \oplus 2 \oplus 4 \oplus 5 \oplus 6 = 4$, so the syndrome is $100$ and bit 4 is wrong. The codeword is $1100110$, and the data bits in positions 3, 5, 6 and 7 are $0110$.

5. $V(10, 2) = 56$ and $1024/56 \approx 18.3$, so at most 18 words. $V(10, 4) = 386$, so the greedy code has at least $\lceil 1024/386 \rceil = 3$ words. $V(9, 3) = 130 < 2^8$ but $130 > 2^7$, so $k = 2$: a linear code with 4 words. The Hamming bound of 18 is the closest to 12, but the gap is still large.

13. The Plotkin bound with $2d > n$ gives $2\lfloor 6/2 \rfloor = 6$. For a code, index the 10 positions by the pairs of $\{1, \dots, 5\}$. Take the zero word, and for each $v$ the word whose ones are the 6 pairs that avoid $v$; any two of these words differ in exactly 6 positions.

14. Each of the 4 codewords sees every fourth byte of the burst and corrects 16 byte errors. A bit burst is safe while it touches at most 64 bytes, so $\lceil (b - 1)/8 \rceil \le 63$.

15. Keep the current connection polynomial and the one in use before the last change of length; at a discrepancy, add a shifted copy of the older one. Check the result: each bit from the fourth on is the sum of the bits two and three places back. A recurrence of length $L$ is unique once at least $2L$ terms are known.

17. Apply the two maps once to $0.3$, then again to each result. The positions with the smallest erasure probabilities carry data, and the union bound adds their erasure probabilities.

20. Every received bit is the sum of at least two unknowns, so no unknown is ever alone. Over $\mathrm{GF}(2)$, adding the third and fourth equations gives $s_2$ directly; the four rows have rank 4.

21. The unique decoder handles $\lfloor (n - k)/2 \rfloor$ errors. Guruswami-Sudan handles every $e$ strictly below $n - \sqrt{n(k - 1)}$; here $\sqrt{255 \cdot 31} \approx 88.9$.

22. The columns of the parity-check matrix form a set $S$ of nonzero vectors of $\mathrm{GF}(2)^r$ with no three summing to zero. For $a \in S$, the sets $S$ and $a + S$ do not meet, so $2|S| \le 2^r$. The vectors of odd weight reach the bound.

23. An outer symbol is wrong only if its inner block holds at least 2 errors, and the outer decoder fails only with at least 4 wrong symbols. So it needs 8 errors to fail, two in each of four blocks. GMD decoding reaches half the designed distance $7 \cdot 3$.

24. A nonzero codeword has at least two nonzero rows, and each nonzero row has at least two ones; the same holds for columns. A word of weight 4 is therefore the four corners of a rectangle: two rows and two columns.

25. Evaluate $h$ at $0.1$, at $0.05$ and at $J(0.1) \approx 0.053$. The lower end comes from Gilbert-Varshamov and the upper end from the smallest of the three upper bounds.

26. The output of the combined channel is a BSC output that is erased with probability $0.2$ independently of everything else. The same uniform input maximizes both stages, so the capacity is $(1 - 0.2)(1 - h(0.1)) \approx 0.425$ bits per use.
