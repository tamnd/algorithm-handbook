## What to remember

- On unsigned $w$-bit words with arithmetic modulo $2^w$, $-x = \overline{x} + 1$. Hence $x \wedge (-x)$ keeps only the lowest 1-bit of $x$, and $x \wedge (x - 1)$ clears it. Most tricks in the chapter start from these two expressions.
- A word is a set: bit $i$ is 1 when $i$ is a member. AND, OR, XOR and NOT are intersection, union, symmetric difference and complement, each in one step. A [bit vector](/bit-set/) over $n$ items does them in $\Theta(n / w)$ steps.
- $x$ is a power of two exactly when $x \ne 0$ and $x \wedge (x - 1) = 0$. The index of the lowest 1-bit is $\operatorname{ctz}(x)$; the index of the highest is $\lfloor \lg x \rfloor = w - 1 - \operatorname{clz}(x)$.
- The population count $\nu(x)$ takes $\nu(x)$ rounds by [Kernighan's loop](/kernighan-popcount/), $\Theta(\log w)$ word operations by the [SWAR method](/swar-popcount/), and one instruction on most current processors. Parity is $\nu(x) \bmod 2$.
- XOR cancels in pairs: $a \oplus a = 0$. That finds the [single number](/single-number/) in one pass and swaps two words with no temporary, but the [XOR swap](/xor-swap/) zeroes a location swapped with itself.
- Reversal, interleaving and transposition of bits take $\lg w$ rounds, each a few shifts and masked swaps of blocks half the size of the last.
- Loops over subsets of $n$ items: [Gosper's hack](/gospers-hack/) gives the next subset of the same size in $O(1)$; the loop $s \gets (s - 1) \wedge m$ visits the $2^{\nu(m)}$ submasks of $m$, $3^n$ steps over all $m$; [SOS DP](/sos-dp/) computes all submask sums in $n 2^{n-1}$ additions.
- Many tricks are correct only on unsigned words. In C a shift by $w$ or more and a signed overflow are undefined.

| Task | Method | Word operations | Extra space |
|---|---|---|---|
| population count | [Kernighan's loop](/kernighan-popcount/) | $\Theta(\nu(x))$ rounds, $w$ in the worst case | none |
| population count | [table lookup](/table-lookup/) by bytes | $w / 8$ lookups | 256 entries |
| population count | [SWAR](/swar-popcount/) | 12 for $w = 32$ or $64$, one multiplication | none |
| trailing zero count | binary search | $\Theta(\log w)$; five tests for $w = 32$ | none |
| trailing zero count | [de Bruijn bit scan](/de-bruijn-bit-scan/) | $O(1)$: negate, AND, multiply, shift, lookup | $w$ entries |
| all submask sums | submask enumeration | $3^n$ steps | none |
| all submask sums | [SOS DP](/sos-dp/) | $n 2^{n-1}$ additions | in place |

: Costs of the main methods for counting bits, finding a bit and summing over submasks, as given in their entries. A hardware instruction does each of the first five in one or two steps.

## Choosing a method

Use the instruction when the processor has one and the compiler exposes it, through a builtin or a standard library function such as C++20's `std::popcount`. Write the trick yourself when the code must be portable to machines without the instruction, when you need it on many fields of a word at once, or when you need to understand what the compiler did.

Among the software methods, Kernighan's loop wins on sparse words, the SWAR method has a fixed cost and no memory traffic, and a table pays only when the table stays in cache. For loops over subsets, prefer SOS DP whenever the work for each pair $s \subseteq m$ is a plain sum; keep submask enumeration for recurrences that combine $s$ and $m \setminus s$ in other ways, as in [bitmask DP](/bitmask-dp/) for partitions.

Branch-free code is not free. It computes both sides of a choice, so it pays only when the branch is hard to predict, as in sorting and searching on random data, or when the time must not depend on secret data, as in cryptographic code.
