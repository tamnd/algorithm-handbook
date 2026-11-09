## What to remember

- A **distribution sort** computes a bucket from the key, by arithmetic or by indexing, instead of comparing keys. That is why the $\lceil \lg n! \rceil$ bound of comparison sorts does not apply to it. A top-down step sorts only if its bucket map is order-preserving.
- **Counting sort** sorts $n$ items with keys in $\{0, \ldots, k-1\}$ in $\Theta(n + k)$ time and space, with counts, a prefix sum and one placing pass. It is stable, and linear when $k = O(n)$.
- **LSD radix sort** sorts $d$-digit keys in base $b$ in $\Theta(d(n + b))$ time. Every pass after the first must be stable. For $w$-bit keys, digits of about $\lg n$ bits give $\Theta(wn/\log n)$, so keys in $\{0, \ldots, n^c - 1\}$ sort in $\Theta(cn)$ time.
- **Bucket sort** with $n$ buckets runs in $\Theta(n)$ expected time on independent uniform keys, because $\mathbb{E}[n_j^2] = 2 - 1/n$ for each bucket. The expectation is over the input, not over coin flips, and a bad input stays bad: the worst case is $\Theta(n^2)$.
- **Strings** are measured by $D$, the total length of the distinguishing prefixes. Any sort must read $\Omega(D)$ characters, and over a comparison alphabet it needs $\Omega(D + n \log n)$ time. [MSD radix sort](/msd-radix-sort/) reads $O(n + D)$ characters but pays $\Theta(R)$ for each bucket split; [multikey quicksort](/multikey-quicksort/) takes $O(n \log n + D)$ expected time and pays nothing for a large alphabet.
- **In place costs stability.** [American flag sort](/american-flag-sort/), [radix exchange sort](/radix-exchange-sort/), multikey quicksort and [flashsort](/flashsort/) permute in place and are not stable. Counting sort, LSD and MSD radix sort use a second array and are stable.
- **Integer sorting** on the word RAM is not settled. The best known bounds in linear space are $O(n \log \log n)$ deterministic and $O(n \sqrt{\log \log n})$ expected; the only lower bound known is $\Omega(n)$.

## The main sorts side by side

| Sort | Best | Average | Worst | Extra space | Stable |
|---|---|---|---|---|---|
| [Counting sort](/counting-sort/) | $\Theta(n + k)$ | $\Theta(n + k)$ | $\Theta(n + k)$ | $\Theta(n + k)$ | yes |
| [Pigeonhole sort](/pigeonhole-sort/) | $\Theta(n + k)$ | $\Theta(n + k)$ | $\Theta(n + k)$ | $\Theta(n + k)$ | yes |
| [LSD radix sort](/radix-sort/) | $\Theta(d(n + b))$ | $\Theta(d(n + b))$ | $\Theta(d(n + b))$ | $\Theta(n + b)$ | yes |
| [Bucket sort](/bucket-sort/) | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n)$ | yes |
| [MSD radix sort](/msd-radix-sort/) | $\Theta(n + R)$ | — | $O(R(n + D))$ | $\Theta(n + R)$ | yes |
| [American flag sort](/american-flag-sort/) | $\Theta(n + R)$ | — | $O(R(n + D))$ | $O(RL)$ | no |
| [Radix exchange sort](/radix-exchange-sort/) | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(nw)$ | $O(w)$ | no |
| [Multikey quicksort](/multikey-quicksort/) | $\Theta(n + D)$ | $O(n \log n + D)$ | $O(\min(n, \sigma)(n + D))$ | $O(n)$ | no |
| [Flashsort](/flashsort/) | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(m)$ | no |

: The main distribution sorts. Here $k$ is the number of possible keys, $d$ the number of digits in base $b$, $w$ the number of bits of a key, $R$ or $\sigma$ the size of the alphabet, $D$ the total length of the distinguishing prefixes, $L$ the longest distinguishing prefix, and $m$ the number of classes of flashsort. The average cases of bucket sort and flashsort are for keys close to uniform, that of radix exchange sort is for random keys, and that of multikey quicksort is over its random pivots.

## Choosing a method

- For keys that are small integers, such as bytes, grades or codes with $k$ not much larger than $n$, use counting sort.
- For many fixed-width integers, such as 32-bit or 64-bit keys, use LSD radix sort with 8-bit to 16-bit digits. For a few thousand keys, a comparison sort is usually just as fast.
- For signed integers or floating-point numbers, first map the bit patterns to unsigned integers in the same order, then use radix sort.
- For strings over bytes, use MSD radix sort with a cut-off to insertion sort for small buckets. For large alphabets or long common prefixes, use [three-way radix quicksort](/three-way-radix-quicksort/). For very large sets of strings, [burstsort](/burstsort/) makes fewer cache misses.
- Use bucket sort or flashsort only when you know the keys are spread evenly. If you do not know, sort large buckets with an $O(m \log m)$ method so that the worst case stays $O(n \log n)$.
- For keys of very different lengths, padding every key to the longest one can cost far more than the total length; see [sorting variable-length items](/sorting-variable-length-items/).
