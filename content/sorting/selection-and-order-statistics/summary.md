## What to remember

- **Selection is easier than sorting.** The item of rank $k$ among $n$ can be found in $\Theta(n)$ time, while sorting needs $\Omega(n \log n)$ comparisons. Any rank reduces to the [median](/median/), so the median is the hard case.
- **Extreme ranks have exact answers.** The minimum takes $n - 1$ comparisons. The [minimum and maximum together](/minimum-and-maximum-finding/) take $\lceil 3n/2 \rceil - 2$, by comparing items in pairs. The smallest and second smallest take $n + \lceil \lg n \rceil - 2$, by the [tournament method](/tournament-method/). Each count is also a lower bound.
- **[Quickselect](/quickselect/)** partitions around a pivot and keeps one side. With a random pivot it makes fewer than $4n$ comparisons on average: about $2n$ for the minimum and $2(1 + \ln 2) n \approx 3.39n$ for the median. Its worst case is $\Theta(n^2)$.
- **[Median of medians](/median-of-medians/)** takes as pivot the median of the medians of groups of five. At most about $7n/10$ items fall on either side, so $T(n) \le T(n/5) + T(7n/10) + O(n)$, which is $\Theta(n)$ because $1/5 + 7/10 < 1$. The constant is large, so it serves as a fallback, as in [introselect](/introselect/), more than as a first choice.
- **Lower bounds.** Every comparison method needs $n - 1 + \min(k - 1, n - k)$ comparisons in the worst case for rank $k$, which is $\lceil 3n/2 \rceil - 2$ for the median. The best known worst-case bounds for the median lie between about $2n$ and $2.95n$.
- **Sampling wins on average.** [Floyd-Rivest select](/floyd-rivest-select/) makes $n + \min(k, n - k) + o(n)$ comparisons on average, $1.5n$ for the median, and no method does better on average.
- **The k smallest.** As a set they take $\Theta(n)$ time, by selection and one partition; in sorted order, $\Theta(n + k \log k)$. A [heap of k candidates](/heap-select/) takes $O(n \log k)$ time and works on a stream.
- **Many ranks.** [Multiple selection](/multiple-selection/) of $m$ ranks takes $O(n \log m)$ time, between the cost of one selection and that of a full sort.

## Selection methods side by side

| Method | Worst case | Expected | Comparisons | Extra space |
|---|---|---|---|---|
| [Quickselect](/quickselect/), random pivot | $\Theta(n^2)$ | $\Theta(n)$ | $< 4n$ on average | $\Theta(1)$ |
| [Median of medians](/median-of-medians/) | $\Theta(n)$ | $\Theta(n)$ | at most $5.4305n$ in the tuned form PICK | $\Theta(n)$ |
| [Introselect](/introselect/) | $\Theta(n)$ | $\Theta(n)$ | close to quickselect | $\Theta(n)$ |
| [Floyd-Rivest select](/floyd-rivest-select/) | $O(n^2)$ | $\Theta(n)$ | $n + \min(k, n-k) + o(n)$ on average | $\Theta(n)$ |
| [Radix select](/radix-select/), $w$-bit keys | $O((n + 2^r) w / r)$ | — | none | $O(n + 2^r)$ |
| [Heap select](/heap-select/), $k$ smallest | $\Theta(n \log k)$ | — | $n + O(k \log k \log(n/k))$ on random order | $\Theta(k)$ |
| [Partial quicksort](/partial-sorting/), $k$ smallest sorted | $\Theta(n^2)$ | $\Theta(n + k \log k)$ | $2n + O(k \log n)$ on average | $O(\log n)$ stack |

: The main selection methods. The space of median of medians and introselect is that of the forms given in their entries; both can also run in place with a recursion stack. Radix select reads $r$ bits of each key per pass and makes no key comparisons.

## Choosing a method

Use the selection routine of your library, such as nth_element in C++, unless you have measured a reason not to. When you write one:

- For a single rank on data in memory, use quickselect with a random pivot and a three-way partition. The three-way partition matters: with many equal keys, a two-way partition can make quickselect quadratic even with random pivots.
- When an adversary may choose the input, or the worst case matters, use introselect: quickselect that switches to median of medians when its pivots go bad.
- When comparisons are expensive and $n$ is large, use Floyd-Rivest select.
- When the keys are fixed-width integers, radix select reads each key only a few times.
- For the $k$ smallest of a stream, or when $k$ is much smaller than $n$, keep a max-heap of $k$ candidates.
- For several ranks at once, such as the deciles, use multiple selection rather than separate selections.
