A dictionary coder replaces repeated text by a reference to an earlier copy. In `the cat and the hat`, the second `the ` can be written as "go back 12 bytes and copy 4". The decoder keeps what it has written, follows the reference, and gets the bytes back. That one step, a copy from earlier output, is the core of zip, gzip and PNG, of the LZ4 and Zstandard streams inside file systems and databases, of Brotli on the web, and of the 7z and xz archives.

The methods differ in what the dictionary is and in how the coder picks its phrases. In the LZ77 family the dictionary is all the text seen so far, and a phrase is a copy given by a distance and a length. In the LZ78 family the dictionary is a growing list of earlier phrases, and a phrase is named by its index. In a grammar the dictionary is a set of rules, each naming a phrase built from smaller ones. All three are lossless, and all three decode in time linear in the output. The hard part is on the encoder's side: which matches to look for, and which of them to use.

## What the chapter covers

The chapter is in nine groups, read in order.

1. **Dictionaries and parses.** The model behind every method: a dictionary, a parse of the text into its phrases, and a cost. [Dictionary-based compression](/dictionary-based-compression/) shows that the parse of least cost is a shortest path, and [adaptive dictionary compression](/adaptive-dictionary-compression/) shows why a dictionary built from the text itself needs no table in the output.
2. **Copies and factors.** The [back-reference](/back-reference/), the [Lempel-Ziv factor](/lempel-ziv-factor/), the ways to cut a text into factors in [Lempel-Ziv parsing](/lempel-ziv-parsing/), and the linear-time [Lempel-Ziv factorization](/lempel-ziv-factorization/).
3. **The LZ77 family.** [LZ77](/lz77/) with its triples, and [LZSS](/lzss/), which writes a literal or a copy with a flag bit.
4. **The LZ78 family.** [LZ78 parsing](/lz78-parsing/), the [LZ78](/lz78/) coder, and [LZW](/lzw/), the coder of compress and GIF.
5. **Finding and choosing matches.** [Match finding](/match-finding/) with hash chains, [greedy parsing](/greedy-parsing/), [lazy matching](/lazy-matching/), and parses of least cost in phrases or in bits.
6. **Byte-aligned formats.** [LZ4](/lz4/), [Snappy](/snappy/) and [LZO](/lzo/), which write whole bytes and use no entropy coder.
7. **Entropy-coded formats.** [DEFLATE](/deflate/), then [LZX](/lzx/), [Zstandard](/zstandard/), [Brotli](/brotli/) and [LZMA](/lzma/). Each entry gives the format as its specification defines it, and an example encoder that writes valid streams. The example encoders are simpler than the reference ones and often use only part of the format: the Brotli encoder, for one, uses one block type and one tree per category.
8. **Grammars.** The [straight-line program](/straight-line-program-grammar/), [grammar-based compression](/grammar-based-compression/), three ways to build a grammar ([byte pair encoding](/byte-pair-encoding/), [Re-Pair](/re-pair/), [Sequitur](/sequitur/)), and the [smallest grammar problem](/smallest-grammar-problem/), which is NP-hard.
9. **Measures and limits.** The [longest previous factor](/longest-previous-factor/) array, [Lempel-Ziv complexity](/lempel-ziv-complexity/), the [Ziv-Lempel entropy theorem](/ziv-lempel-entropy-theorem/), and [LZ-End](/lz-end/).

## A first reading

For a first reading, take these fourteen entries in order: [dictionary-based compression](/dictionary-based-compression/), [adaptive dictionary compression](/adaptive-dictionary-compression/), [back-reference](/back-reference/), [Lempel-Ziv factor](/lempel-ziv-factor/), [Lempel-Ziv parsing](/lempel-ziv-parsing/), [LZ77](/lz77/), [LZSS](/lzss/), [LZ78](/lz78/), [LZW](/lzw/), [match finding](/match-finding/), [greedy parsing](/greedy-parsing/), [lazy matching](/lazy-matching/), [LZ4](/lz4/) and [DEFLATE](/deflate/). They give the two families, the encoder's choices, the simplest byte format and the most widely used entropy-coded one. Work the small examples in each by hand: a parse of ten symbols shows more than a page of description.

Skip at first the format details of LZX, Zstandard, Brotli and LZMA, the grammars after Re-Pair, and the last group. Come back to the grammars and to the [Ziv-Lempel entropy theorem](/ziv-lempel-entropy-theorem/) when you want to know how small a parse can be and why these coders work on any source.

## Before you start

From the chapter on entropy coding you need [lossless compression](/lossless-compression/) and [prefix codes](/prefix-code/), and, for the entropy-coded formats, [Huffman coding](/huffman-coding/), [canonical Huffman codes](/canonical-huffman-code/), [range coding](/range-coding/) and [tabled ANS](/tabled-asymmetric-numeral-systems/). The theorem of the last group uses the [entropy rate](/entropy-rate/) of a source. Match finding uses a [hash table](/hash-table/) and a [trie](/trie/) from the volume on data structures. The linear-time factorization uses the [suffix array](/suffix-array/) and the [LCP array](/lcp-array/) from the volume on strings. For the hardness proof you need [NP-completeness](/np-complete/) and [vertex cover](/vertex-cover/).
