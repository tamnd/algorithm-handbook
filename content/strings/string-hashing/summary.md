## What to remember

- A **fingerprint** errs in one direction only: equal strings always get equal values, and a collision makes different strings look equal. The error probability is over a random key, never over the inputs.
- The **polynomial hash** $\sum_i c(x_i)\, r^{\ell-1-i} \bmod p$ moves along a text in $O(1)$ time per step, and with prefix hashes gives the hash of any substring in $O(1)$ time.
- With $p$ prime and $r$ uniform, two fixed different strings of length at most $n$ collide with probability at most $(n-1)/p$: their difference is a nonzero polynomial of degree less than $n$, with at most $n - 1$ roots.
- The bound is for one pair. For $q$ comparisons the union bound gives $q(n-1)/p$, and for $N$ values that must all differ the birthday paradox asks for $p$ much larger than $N^2$. A prime near $2^{61}$ covers most uses; a prime near $10^9$ often does not.
- **Rabin-Karp** compares symbols only where hashes agree. With a random base its expected time is $O(n + m)$ plus $O(m)$ per occurrence; its worst case is $O(nm)$.
- A fixed base, a visible hash, or arithmetic modulo $2^{64}$ voids the bound. **Anti-hash tests** make such hashes collide on purpose, for example with Thue-Morse strings modulo $2^{64}$.
- Fast table hashes such as **FNV** and **MurmurHash** have no random key in this sense; they suit trusted keys, and a table that faces chosen keys needs a keyed or universal hash.

## The main methods side by side

| Method | Task | Time | Error for one comparison | Notes |
|---|---|---|---|---|
| [Polynomial hash](/polynomial-rolling-hash/), random base | fingerprint of a string | $\Theta(n)$, then $O(1)$ per slide | $(n-1)/p$ | the standard tool |
| [Prefix hashes](/substring-equality-queries/) | substring equality | $O(n)$ build, $O(1)$ query | $(\ell-1)/p$ | LCE by binary search in $O(\log n)$ |
| [Rabin-Karp](/rabin-karp/) | exact matching | $O(n + m + zm)$ expected | none, with verification | extends to 2D and many patterns |
| [Dynamic hashing](/dynamic-polynomial-hashing/) | substring equality under updates | $O(\log n)$ per operation | $(\ell-1)/p$ | Fenwick or segment tree |
| [Universal string hashing](/universal-string-hashing/) | hash table with string keys | $\Theta(\ell)$ per key | $(\ell-1)/p + 1/M$ | bound for every key set |
| [Rabin fingerprint](/rabin-fingerprint/) | bit strings, chunking | $O(1)$ word operations per step | about $n/2^k$ | random irreducible polynomial |
| [FNV-1a](/fnv-hash/), [MurmurHash3](/murmurhash/) | hash table buckets | $\Theta(n)$ | no bound | fast, no key |

: Hashing methods for strings of length $n$ (or $\ell$) with a prime modulus $p$, a table of $M$ buckets, a pattern of length $m$ with $z$ occurrences in Rabin-Karp, and a Rabin fingerprint of $k$ bits. The errors hold when the random choices are made after the inputs are fixed.

## Choosing a method

- To compare substrings of one fixed text many times, use prefix hashes with a random base modulo $2^{61} - 1$; if no error is allowed, use a suffix array with an LCP array instead.
- To search a text for one pattern, prefer Knuth-Morris-Pratt or Boyer-Moore; use Rabin-Karp for two-dimensional patterns, for many patterns of one length, or when hashes are already at hand.
- To compare large files on two machines, send a fingerprint with its random base, not the file.
- For a hash table with keys from users, use a keyed hash or a universal family with a fresh random key; for trusted keys, FNV-1a or MurmurHash3 is enough.
- Never take the base from a constant in the code, and never use the overflow of 64-bit arithmetic as the modulus, when an adversary can choose the input.
