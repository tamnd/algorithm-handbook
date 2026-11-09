## What to remember

- A **sorting network** is a fixed list of comparators. Its **size** $s$ is the number of comparators and its **depth** $d$ the number of layers of comparators on disjoint wires. Always $d \le s \le d \lfloor n/2 \rfloor$.
- The **zero-one principle**: a comparator network sorts every input if and only if it sorts the $2^n$ inputs of zeros and ones. The proof is that a comparator commutes with every non-decreasing map. A merging network needs only the $(p+1)(q+1)$ pairs of sorted 0-1 lists.
- Deciding whether a given network sorts is **co-NP-complete**, so the $2^n$ test cannot be avoided in general.
- **Lower bounds.** $s \ge \lceil \lg n! \rceil$, as for every comparison sort, and $d \ge \lceil \lg n \rceil$, because after $t$ layers a wire depends on at most $2^t$ inputs. Counting comparators per layer gives the stronger $d \ge \lceil \lg n! \rceil / \lfloor n/2 \rfloor \approx 2 \lg n$.
- **Batcher's networks** are merge sorts whose merge is a network of depth $\lg n$. For $n = 2^k$ both have depth $\tfrac12 k(k+1)$. [Bitonic sort](/bitonic-sort/) has $\tfrac14 n k (k+1)$ comparators and very regular layers; [odd-even merge sort](/odd-even-merge-sort/) has $\tfrac14 n k (k-1) + n - 1$.
- A network cannot adapt, so it often needs more comparators than the best comparison sort: $s(5) = 9$, while merge insertion sorts 5 items with 7 comparisons.
- The exact minimum size is known for $n \le 12$ and the exact minimum depth for $n \le 17$, by computer searches. For $n = 10$ and $n = 12$ no network has both the minimum size and the minimum depth.
- The [AKS network](/aks-sorting-network/) has depth $O(\log n)$ and size $O(n \log n)$, both optimal up to a constant factor. Its constant is so large that Batcher's networks are better for every practical $n$.

## The main networks side by side

| Network | Size | Depth | Size, depth for $n = 16$ |
|---|---|---|---|
| Insertion sort, adjacent comparators | $n(n-1)/2$ | $2n - 3$ | 120, 29 |
| [Odd-even transposition sort](/odd-even-transposition-sort/) | $n(n-1)/2$ | $n$ | 120, 16 |
| [Bitonic sort](/bitonic-sort/) | $\tfrac14 n \lg n (\lg n + 1)$ | $\tfrac12 \lg n (\lg n + 1)$ | 80, 10 |
| [Odd-even merge sort](/odd-even-merge-sort/) | $\tfrac14 n \lg n (\lg n - 1) + n - 1$ | $\tfrac12 \lg n (\lg n + 1)$ | 63, 10 |
| [Pairwise network](/pairwise-sorting-network/) | $\tfrac14 n \lg n (\lg n - 1) + n - 1$ | $\tfrac12 \lg n (\lg n + 1)$ | 63, 10 |
| [Green's network](/green-filter/) | only $n = 16$ | only $n = 16$ | 60, 10 |
| [AKS network](/aks-sorting-network/) | $O(n \log n)$ | $O(\log n)$ | not useful |
| Lower bound | $\lceil \lg n! \rceil$ | $\lceil \lg n! \rceil / \lfloor n/2 \rfloor$ | 45, 6 |

: The main sorting networks. The formulas of Batcher's networks and the pairwise network hold for $n$ a power of 2. For $n = 16$ the optimal depth is 9, reached by a known network with 61 comparators, and the optimal size is not known; it lies between 55 and 60.

## Choosing a network

- For a small fixed $n$, as in a SIMD kernel or a circuit, take a network from the tables of the best known networks. Choose by depth when each layer costs one parallel step, and by size when the comparators run one after another.
- For larger $n$ that are powers of 2, use bitonic sort when the layers must compare $i$ with $i \oplus h$, as on a hypercube or with SIMD shuffles, and odd-even merge sort when the number of comparators matters.
- For other $n$, build the network for the next power of 2 and drop the comparators that touch the extra wires.
- Check any network you copy or write on all $2^n$ inputs of zeros and ones. With one bit per input this takes well under a second for 16 wires.
- On a single processor with no need for obliviousness, do not use a network at all: an $O(n \log n)$ sort such as [merge sort](/merge-sort/) is faster.
