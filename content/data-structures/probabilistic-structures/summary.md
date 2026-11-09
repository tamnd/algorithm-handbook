## What to remember

- A **filter** for $n$ keys has no false negatives and a false positive rate $\varepsilon$. Any filter needs at least $n \log_2(1/\varepsilon)$ bits, whatever the size of the keys and the universe.
- A **Bloom filter** with $m$ bits and $k$ hash functions has a rate of about $(1 - e^{-kn/m})^k$. The best $k$ is $(m/n)\ln 2$, which leaves half of the bits at 0 and gives a rate of about $0.6185^{m/n}$. So it needs $1.44 \log_2(1/\varepsilon)$ bits per key, 44 percent above the lower bound. The classical formula is a slight underestimate of the exact rate.
- A Bloom filter cannot delete. A **counting Bloom filter** can, with 4-bit counters at four times the memory. Deleting a key that was never inserted causes false negatives.
- A **cuckoo filter** stores an $f$-bit fingerprint in one of two buckets of $b$ slots, with a rate of at most $(2b + 1)/(2^f - 1)$, and supports deletion. With $b = 4$ at 95 percent load it beats a Bloom filter below a rate of about 3 percent. A **quotient filter** stores $r$-bit remainders in $2^q$ slots of $r + 3$ bits, with a rate of at most $\alpha 2^{-r}$.
- For a **static** set, the **xor filter** stores $r$-bit fingerprints in about $1.23n$ cells by peeling a random hypergraph, with a rate of exactly $2^{-r}$. The binary fuse filter needs about $1.125n$ cells and the ribbon filter fewer still.
- The **count-min sketch** with $w = \lceil e/\varepsilon \rceil$ columns and $d = \lceil \ln(1/\delta) \rceil$ rows never underestimates a count in the strict turnstile model, and overestimates it by more than $\varepsilon N$ with probability at most $\delta$. The proof needs only pairwise independent hashing and Markov's inequality.
- The **Flajolet–Martin sketch** sets, for each item, the bit whose index is the number of trailing zeros of its hash, and estimates the number of distinct items from the lowest bit that is still 0. With $m$ bitmaps, PCSA has a standard error of about $0.78/\sqrt{m}$, so 64 bitmaps of 32 bits, 256 bytes, give about 10 percent.

## The filters side by side

| Filter | Bits per key | At $\varepsilon = 2^{-8}$ | Insert | Delete |
|---|---|---|---|---|
| Lower bound | $\log_2(1/\varepsilon)$ | 8 | | |
| [Bloom filter](/bloom-filter/) | $1.44 \log_2(1/\varepsilon)$ | 11.5 | yes | no |
| [Counting Bloom filter](/counting-bloom-filter/) | 4 times the Bloom filter | 46 | yes | yes |
| [Cuckoo filter](/cuckoo-filter/), $b = 4$, 95% load | $(\log_2(1/\varepsilon) + 3)/0.95$ | about 11.6 | can fail when full | yes |
| [Quotient filter](/quotient-filter/), $\alpha = 0.75$ | $(\log_2(\alpha/\varepsilon) + 3)/\alpha$ | 14.7 | yes | yes |
| [Xor filter](/xor-filter/) | $1.23 \log_2(1/\varepsilon)$ | 9.84 | static | static |
| [Binary fuse filter](/binary-fuse-filter/) | about $1.125 \log_2(1/\varepsilon)$ | about 9.0 | static | static |
| [Ribbon filter](/ribbon-filter/), $w = 64$ | close to $\log_2(1/\varepsilon)$ | about 8.4 | static | static |

: Space in bits per key for a false positive rate $\varepsilon$. The Bloom filter uses the best $k$. "Static" means the filter is built once from the whole set.

## Choosing a structure

- For a set that only grows, with a moderate rate such as 1 percent, use a Bloom filter. It never refuses an insert, and two filters merge by a bitwise OR.
- When keys must be deleted, use a cuckoo filter or a quotient filter rather than a counting Bloom filter, which costs four times the space. The quotient filter also merges and resizes well on disk.
- When the set is fixed, as for the files of a database that are written once, use an xor, binary fuse or ribbon filter.
- When the final size of the set is not known, use a scalable Bloom filter. When old keys should be forgotten, as in a stream of duplicates, use a stable Bloom filter.
- For counts in a stream, use a count-min sketch for frequent items and point queries, and a Flajolet–Martin sketch or its successor HyperLogLog for the number of distinct items.
