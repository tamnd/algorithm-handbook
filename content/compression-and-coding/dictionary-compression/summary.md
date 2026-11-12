## What to remember

- **A parse is a path.** With a fixed dictionary and a cost for each phrase, the cheapest parse of a text of length $n$ is a shortest path from position 0 to position $n$ in a directed acyclic graph, found by $C[i] = \min_w \bigl(c(w) + C[i + |w|]\bigr)$. With phrases of length at most $L$ in a [trie](/trie/), this takes $O(nL)$ time. Greedy parsing is optimal in phrase count when the dictionary is closed under suffixes, and for LZ77 copies with no minimum length; in general it is not.
- **Two families.** LZ77 copies any earlier substring, given by a distance $d$ and a length $\ell$; with $\ell > d$ the copy overlaps the text it writes. LZ78 and LZW name a whole earlier phrase by its index in a trie. On a run of $n$ equal symbols, LZ77 needs 2 phrases and LZ78 about $\sqrt{2n}$.
- **Parse counts.** For the greedy LZ77 parse into triples ($z_{77}$), the factorization with and without self-reference ($z$ and $z_{no}$) and the LZ78 parse ($c$): $z_{77} \le z \le z_{no}$ and $z \le 2c$. Every string has $c = O(n / \log_\sigma n)$ and $c = \Omega(\sqrt{n})$. The factorization takes $\Theta(n)$ time from a suffix array.
- **The encoder chooses.** Each format fixes its decoder, and any valid parse is a valid stream. Hash chains find candidates; greedy and lazy rules pick among them. In bits, greedy can be worse than optimal by a factor of $\Omega(\log n / \log \log n)$.
- **Decoding is cheap.** Every format of the chapter decodes in $O(n + m)$ time for $n$ output and $m$ input bytes, with a window of earlier output as its only large memory (Brotli adds a static dictionary of 122,784 bytes).
- **Grammars.** A straight-line program is a dictionary of nested phrases. If $g^*$ is the size of a smallest grammar, $z_{no} \le g^* = O(z_{no} \log n)$. Finding $g^*$ is NP-hard, and no polynomial algorithm reaches a ratio below $8569/8568$ unless P = NP; the best known ratio is $O(\log(n / g^*))$.
- **Universality.** For a stationary ergodic source with entropy rate $H$, the LZ78 code length per symbol tends to $H$ almost surely, with no model of the source. The redundancy falls only as $1/\log n$: a fair coin still costs about 12% above $H$ at $n = 2^{20}$.

## The formats side by side

| Format | Entropy coder | Farthest copy | Match lengths | Recent distances |
|---|---|---|---|---|
| [DEFLATE](/deflate/) | Huffman, fixed or dynamic | 32768 | 3 to 258 | none |
| [LZ4](/lz4/) | none | 65535 | 4 and up | none |
| [Snappy](/snappy/) | none | $2^{32} - 1$ | 4 to 11 or 1 to 64 per copy | none |
| [LZO](/lzo/) (LZO1X) | none | 49151 | 2 and up | none |
| [LZX](/lzx/) | Huffman, three trees | window $2^{15}$ to $2^{21}$ | 2 to 257 | 3 |
| [Zstandard](/zstandard/) | Huffman for literals, FSE for sequences | window up to $2^{41} + 7 \cdot 2^{38}$ | 3 and up | 3 |
| [Brotli](/brotli/) | Huffman, with context maps | window up to $2^{24} - 16$ | 2 and up | ring of 4 |
| [LZMA](/lzma/) | adaptive binary range coder | dictionary up to $2^{32} - 1$ | 2 to 273 | 4 |

: The LZ77 formats of the chapter, as their specifications define them; distances and lengths are in bytes. Zstandard recommends windows of at most 8 MB, and the Snappy encoder of its entry works in 64 KiB blocks, so its offsets fit in 2 bytes. The encoders of the entries write valid subsets: for example, the Brotli encoder uses one block type and one tree per category, and the Zstandard encoder writes raw literals and the predefined tables.

## Choosing a method

- When the reader is fixed, use what it reads: DEFLATE for gzip, ZIP, PNG and HTTP; LZW for GIF, TIFF and `.Z` files; LZX for CAB and CHM.
- When speed matters more than size, use LZ4 or Snappy, or LZO for a decoder that needs no memory of its own.
- For a new general-purpose format, use Zstandard, and choose the level for speed or size.
- For web text that is compressed once and sent many times, use Brotli; its static dictionary helps most on short files.
- When the size matters most and encoding may be slow, use LZMA, or LZMA2 in `.xz`.
- For a large, highly repetitive collection that you must search or read in parts, build a grammar with [Re-Pair](/re-pair/) or an [LZ-End](/lz-end/) parse, and work on the compressed form.
