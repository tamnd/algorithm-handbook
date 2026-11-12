## What to remember

- The [entropy](/shannon-entropy/) $H(X) = \sum_x p(x) \log_2(1/p(x))$ is the mean information of one outcome. The empirical entropies $H_0(s) \ge H_1(s) \ge \cdots$ measure one string with no source assumed. A stationary Markov source has the [entropy rate](/entropy-rate/) $\sum_i \mu_i H(P_{i\cdot})$.
- By the [Kraft inequality](/kraft-inequality/) and McMillan's theorem, every uniquely decodable code has $\sum_i 2^{-\ell_i} \le 1$, and every such list of lengths has a [prefix code](/prefix-code/). Prefix codes lose nothing.
- The [source coding theorem](/source-coding-theorem/), for a memoryless source: the best symbol code has $H \le L^* < H + 1$, and codes for blocks of $n$ symbols get below $H + 1/n$ bits per symbol. For a stationary ergodic source the limit is the entropy rate. With no model, the [incompressibility argument](/incompressibility-argument/) says that fewer than a fraction $2^{1-c}$ of the $n$-bit strings shrink by $c$ bits.
- [Huffman's algorithm](/huffman-coding/) gives an optimal symbol code for known weights in $O(n \log n)$ time, or $O(n)$ from sorted weights, with redundancy at most $p_1 + 0.0861$. A codeword can have $n - 1$ bits; [package-merge](/package-merge/) finds the best code with a length limit $L$ in $O(nL)$ time.
- [Elias gamma](/elias-gamma-coding/) spends $2\lfloor \log_2 x \rfloor + 1$ bits on $x$ and is [universal](/universal-code/): within a constant factor of $H$ on every decreasing law. For a geometric law $(1-\theta)\theta^x$, the [Golomb code](/golomb-coding/) with the least $m$ such that $\theta^m + \theta^{m+1} \le 1$ is optimal, and the best [Rice code](/rice-coding/) is at most about 0.09 bits worse.
- [Arithmetic coding](/arithmetic-coding/) writes at most $\sum_i \log_2(1/p_i) + 2$ bits for every input and every model when the arithmetic is exact; a 32-bit integer coder adds under $10^{-4}$ bits per symbol. [ANS](/asymmetric-numeral-systems/) reaches the same rate with one integer of state, but decodes in the reverse order of encoding.
- An [adaptive model](/adaptive-modeling/) pays a bounded regret on every input. Against the best memoryless model in hindsight, the KT estimator pays at most $\tfrac12 \log_2 n + 1$ bits on a binary sequence. [Context tree weighting](/context-tree-weighting/) has a bound of the same kind against every tree source of depth at most $D$.

| Method | Unit coded | Length bound | Model of the bound | Time |
|---|---|---|---|---|
| Huffman | one symbol | $H \le L < H + 1$ | memoryless, known $p$ | $O(n \log n)$ |
| Package-merge | one symbol, at most $L$ bits | optimal under the limit | known weights | $O(nL)$ |
| Garsia-Wachs | one symbol, order kept | $H \le L < H + 2$ | memoryless, known $p$ | $O(n \log n)$ |
| Shannon-Fano-Elias | one symbol | $H + 1 \le L < H + 2$ | memoryless, known $p$ | $\Theta(n + B)$ |
| Arithmetic coding | whole message | $\sum \log_2(1/p_i) + 2$ | every input, any model | $O(\log \sigma)$ per symbol |
| Range coder (LZMA) | binary decisions | $\sum \log_2(1/p_j) + 40$, plus $< 1.8 \times 10^{-4}$ per decision | every input, any model | $\Theta(n)$ |
| rANS | one symbol | $\sum \log_2(M/f) + 64$, plus $< 7.1 \times 10^{-4}$ per symbol | every input, static frequencies | $\Theta(n + k \log k + M)$ |
| CABAC | binary decisions | $\sum \log_2(1/p_i) + 9$ | every input, the engine's probabilities | $\Theta(n + c)$ |

: Entropy coders and their guarantees. For the code builders $n$ is the alphabet size and $B$ the total codeword length; for the coders $n$ is the number of symbols, $\sigma$ or $k$ the alphabet size, $M$ the rANS total and $c$ the number of contexts. Arithmetic coding uses exact arithmetic and a Fenwick tree; the range coder and rANS figures are for the parameters of their entries.

## Choosing a method

For a static alphabet with known counts, use a canonical Huffman code with a length limit, as DEFLATE and JPEG do. Decoding is a table lookup, and the loss is small unless one symbol has a probability near 1. When it has, or when the model changes from symbol to symbol, use an arithmetic or range coder; the adaptive binary coders of LZMA and CABAC suit skewed yes-or-no decisions. When the frequencies are fixed per block and speed matters, use tANS for small alphabets and rANS for large alphabets or interleaved streams.

For integers, choose the code from the law of the values. Small values with a geometric law suit Rice or Golomb codes, with the parameter set from the mean. Values with no known law suit Elias gamma or delta. Lists that must decode fast suit variable-byte codes or PForDelta, and sorted lists with clusters suit interpolative coding.
