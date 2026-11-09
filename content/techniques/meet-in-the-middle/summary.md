## What to remember

- **The method.** Split the unknown into two parts so that the condition becomes $f(x) = g(y)$. List the values of $f$ over all first parts, list the values of $g$ over all second parts, and join the two lists by sorting or hashing. With $N$ choices for each part, $N^2$ trials become about $2N$ evaluations, and one list of $N$ entries must be stored.
- **Double encryption gives little.** For $C = E_{k_2}(E_{k_1}(P))$ with $k$-bit keys, the attack tabulates $E_{k_1}(P)$ and looks up $D_{k_2}(C)$, so it uses about $2^{k+1}$ cipher calls and $2^k$ table entries instead of $2^{2k}$ trials. Double DES gives about 57 bits of work, not 112.
- **Count the false candidates.** With $n$-bit blocks and $t$ known pairs, about $2^{2k - tn}$ wrong key pairs agree with all $t$ pairs by chance. For DES one pair leaves about $2^{48}$ wrong pairs and two pairs leave about $2^{-16}$, so each candidate from the table must be tested on further pairs.
- **Horowitz-Sahni.** The sums of each half are produced in sorted order by repeated merging, and a two-pointer scan over the two lists finds a pair with sum $t$ in at most $|A| + |B| - 1$ steps. Time and space are $\Theta(2^{n/2})$. Moving both pointers forward, or sorting each list from scratch, are the usual mistakes; the second costs an extra factor $n$.
- **Schroeppel-Shamir.** Four quarter lists of $2^{n/4}$ sums, with the second and fourth sorted, and two heaps produce the sums of the left half in increasing order and those of the right half in decreasing order. The scan is the same as before, but the heaps never hold more than $2^{n/4}$ entries. Time $O(n 2^{n/2})$, space $O(2^{n/4})$.
- **Representations.** If a solution of weight $w$ may be split into any two pieces of weight $w/2$, it has $R = \binom{w}{w/2}$ splits. Keep only the pieces whose partial sum has a fixed residue modulo $M \approx R$: each list shrinks by a factor of about $R$, and with probability at least about $1 - 1/e$ one split of the solution survives.
- **Heuristic, not worst case.** The Howgrave-Graham-Joux bounds, about $2^{0.337n}$ time and $2^{0.256n}$ memory, assume that the partial sums of random dense instances spread evenly over the residues. The proven bound of a simple exact version is much worse, and an implementation needs a fallback when the filter loses every split.

## The costs side by side

| Method | Problem | Time | Memory |
|---|---|---|---|
| Exhaustive key search | double encryption, $k$-bit keys | about $2^{2k}$ cipher calls | $O(1)$ |
| [Meet-in-the-middle attack](/meet-in-the-middle-attack/) | double encryption, $k$-bit keys | about $2^{k+1}$ cipher calls | $2^k$ entries |
| Meet in the middle | three-key triple encryption | about $2^{2k}$ cipher calls | $2^k$ entries |
| Exhaustive search | subset sum, $n$ items | $2^n$ subsets | $O(n)$ |
| [Horowitz-Sahni](/horowitz-sahni-algorithm/) | subset sum | $\Theta(2^{n/2})$ | $\Theta(2^{n/2})$ |
| [Schroeppel-Shamir](/schroeppel-shamir-algorithm/) | subset sum | $O(n 2^{n/2})$ | $O(2^{n/4})$ |
| [Howgrave-Graham-Joux](/howgrave-graham-joux-algorithm/) | random dense subset sum | about $2^{0.337n}$, heuristic | about $2^{0.256n}$, heuristic |
| [Representations](/representation-technique/) over $\{-1, 0, 1\}$ | random dense subset sum | about $2^{0.291n}$, heuristic | not stated in the entries |

: Polynomial factors are dropped in the last two rows, which are Becker, Coron and Joux's statements of the bounds. For $n = 64$ items, Horowitz-Sahni stores lists of $2^{32}$ sums and Schroeppel-Shamir quarter lists of $2^{16}$.

## Choosing a method

- If the unknown splits into two parts whose effects can be computed separately and compared, try meet in the middle before any search over all combinations.
- Store the smaller side. When the two parts have $N_1 \le N_2$ choices, tabulate the $N_1$ values and stream the $N_2$ values past the table: time $N_1 + N_2$, memory $N_1$.
- If $2^{n/2}$ entries fit in memory, use Horowitz-Sahni; it is short and has no heuristics. If they do not fit, use Schroeppel-Shamir, which keeps the time and needs only the fourth root of the memory.
- If memory is still too small, make several passes over a part of the table, each pass for a slice of the first keys. Time grows by the number of passes.
- Use representations only for random instances with many solutions of a known weight, and add a fallback for the runs in which the filter keeps no split.
