## What to remember

- A **shuffle is exact** when each of the $n!$ orders has probability $1/n!$. Any method needs at least $\log_2 n!$ random bits on average, about 226 for 52 cards, and no method on fair bits has a bounded worst case for $n \ge 3$, because 3 divides $n!$ and never divides a power of 2.
- **Fisher-Yates** is the shuffle to use. For $i$ from $n-1$ down to 1 it swaps position $i$ with a uniform position $j \in \{0, \dots, i\}$. The $n!$ sequences of choices map one-to-one to the $n!$ orders. It takes $\Theta(n)$ time and no extra space.
- **Count the runs to find a bias.** The [naive shuffle](/naive-shuffle/) has $n^n$ equally likely runs, and $n^n$ is not a multiple of $n!$ for $n \ge 3$. A sort with a coin-flipping comparator gives probabilities of the form $m/2^B$. Neither can be uniform. Drawing the integer by a remainder adds [modulo bias](/modulo-bias/) to any shuffle.
- **Sorting and merging can shuffle exactly** if the randomness is attached to the items, not the comparisons. Permute by sorting draws keys from a range of size $n^3$ and redraws on a tie. A merge must take from the left part with probability $\ell/(\ell+r)$; [MergeShuffle](/merge-shuffle/) keeps fair coins by stopping early and fixing the rest with Fisher-Yates.
- **Sattolo's algorithm** draws $j$ from $\{0, \dots, i-1\}$ instead of $\{0, \dots, i\}$ and gives each of the $(n-1)!$ permutations with one cycle probability $1/(n-1)!$.
- **A card shuffle is a random walk** on the $n!$ orders, and its quality is measured by the [total variation distance](/total-variation-distance/) to uniform after $t$ moves. Many such walks show a cutoff: the distance stays near 1, then falls to near 0 in a short window.
- **A strong uniform time** is a stopping rule after which the deck is exactly uniform, whatever time it stops. Its tail bounds the distance. For top-to-random it is one move after the original bottom card reaches the top, with mean $n H_n$.
- **Seven riffles for 52 cards.** Under the Gilbert-Shannon-Reeds model the probability of an order depends only on its number $r$ of rising sequences, and the deck mixes after about $\frac32 \log_2 n$ shuffles. The distance for 52 cards is $0.924$ after five shuffles, $0.334$ after seven and $0.085$ after nine.

## Shuffles side by side

| Method | Exact | Time | Extra space | Randomness |
|---|---|---|---|---|
| [Fisher-Yates](/fisher-yates-shuffle/) | yes | $\Theta(n)$ | $O(1)$ | $n - 1$ random integers |
| [Permute by sorting](/permute-by-sorting/) | yes, with redraws | $\Theta(n \log n)$ | $\Theta(n)$ keys | about $3 n \log_2 n$ bits |
| [Linked list, weighted merge](/shuffling-a-linked-list/) | yes | $\Theta(n \log n)$ | $O(\log n)$ | biased coins |
| [MergeShuffle](/merge-shuffle/) | yes | $\Theta(n \log n)$ | $O(\log n)$ | $n \log_2 n + O(n)$ bits |
| [Sattolo](/sattolo-algorithm/) | uniform on $n$-cycles | $\Theta(n)$ | $O(1)$ | $n - 1$ random integers |
| [Naive shuffle](/naive-shuffle/) | no | $\Theta(n)$ | $O(1)$ | $n$ random integers |
| [Random comparator](/sort-based-shuffle/) | no | depends on the sort | depends on the sort | one coin per comparison |

: Shuffles as programs. "Exact" assumes a fair source of random integers; with a remainder in place of rejection, every row is biased.

| Shuffle | Mixing time, in moves | For 52 cards |
|---|---|---|
| [Riffle (GSR)](/gilbert-shannon-reeds-model/) | $\frac32 \log_2 n$ | 7 to 9 |
| [Random transpositions](/random-transposition-shuffle/) | $\frac12 n \ln n$ | about 103 |
| [Top to random](/top-to-random-shuffle/) | $n \ln n$ | about 205 |
| [Overhand](/overhand-shuffle-model/) | $\Theta(n^2 \log n)$ | over 100 for the top card alone |
| [Faro](/faro-shuffle/) | never | period 8 for out-shuffles |

: Card shuffles, by the point where the total variation distance drops. The first three are cutoffs with known constants; the overhand bound is known only up to a constant factor.

## Choosing a method

- For an array in memory, use Fisher-Yates with an unbiased bounded integer, such as [Lemire's method](/lemire-bounded-integers/) or rejection. Do not write the naive loop and do not sort with a random comparator.
- For a random sample of $k$ items in order, run only the first $k$ steps of Fisher-Yates.
- For a linked list, copy the pointers to an array and use Fisher-Yates when memory allows; otherwise use the weighted-coin merge.
- On a parallel machine or in a database, attach random keys and sort.
- For a random single cycle, use Sattolo's algorithm.
- For a real deck, riffle seven to nine times. Overhand shuffles alone need far more than a hundred.
